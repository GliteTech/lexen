from __future__ import annotations

import re
from dataclasses import replace
from pathlib import Path
from types import SimpleNamespace

import pytest

from lexen.huggingface import (
    CARD_FILENAME,
    HF_REPO_ID,
    PINNED_EXPORT_SHA256,
    TAG_CREATED,
    TAG_MOVED,
    TAG_UNCHANGED,
    CardFacts,
    collect_facts,
    render_card,
    stage_release,
    tag_release,
    verify_pinned_export,
)
from lexen.paths import ACTIVE_RELEASE_ID, DATASET_CANARY, DEFAULT_REPO_ROOT

CARD_TEMPLATE_PATH = DEFAULT_REPO_ROOT / "templates" / "huggingface_card.md"


def _facts() -> CardFacts:
    return collect_facts(repo_root=DEFAULT_REPO_ROOT)


def test_card_facts_match_the_release() -> None:
    facts = _facts()

    assert facts.total_items == 4861
    assert facts.reviewed_items == 363
    assert facts.source_items == 4917
    assert facts.unreviewed_items == 4554
    assert facts.changed_labels == 211
    assert facts.removed_items == 56

    # The four adjudication outcomes have to account for every reviewed item.
    assert (
        facts.retained_unanimous
        + facts.retained_two_of_three
        + facts.removed_cannot_answer
        + facts.removed_no_consensus
        == facts.reviewed_items
    )
    assert facts.removed_cannot_answer + facts.removed_no_consensus == facts.removed_items

    assert facts.fine_kappa == pytest.approx(0.537, abs=0.0005)
    assert facts.coarse_kappa == pytest.approx(0.740, abs=0.0005)
    assert facts.fine_agreement_pct == pytest.approx(35.5, abs=0.05)
    assert facts.coarse_agreement_pct == pytest.approx(63.1, abs=0.05)


def test_published_items_export_still_matches_the_hash_sensebench_pins() -> None:
    verify_pinned_export(facts=_facts())


def test_publication_is_refused_when_the_items_export_changes() -> None:
    detached = replace(_facts(), items_sha256="sha256:0000")

    with pytest.raises(ValueError, match="refusing to publish"):
        verify_pinned_export(facts=detached)


def test_card_states_the_release_figures_and_leaves_no_placeholder() -> None:
    card = render_card(facts=_facts(), template_path=CARD_TEMPLATE_PATH)

    assert "{{" not in card
    assert "4,861" in card
    assert "0.537" in card
    assert PINNED_EXPORT_SHA256.removeprefix("sha256:") in card
    assert DATASET_CANARY in card


def test_a_template_placeholder_without_a_fact_fails_loudly(tmp_path: Path) -> None:
    template = tmp_path / "card.md"
    template.write_text("kappa {{FINE_KAPPA}}, unknown {{NOT_A_FACT}}\n", encoding="utf-8")

    with pytest.raises(ValueError, match="unresolved placeholders"):
        render_card(facts=_facts(), template_path=template)


def test_staged_payload_is_the_curated_subset(tmp_path: Path) -> None:
    card = render_card(facts=_facts(), template_path=CARD_TEMPLATE_PATH)

    staged = stage_release(repo_root=DEFAULT_REPO_ROOT, staging_dir=tmp_path, card=card)

    assert staged == [
        "CITATION.cff",
        "DATASHEET.md",
        "README.md",
        "data/items.jsonl",
        "data/reviews.jsonl",
        "raganato/lexen-v1.data.xml",
        "raganato/lexen-v1.gold.key.txt",
        "raganato/lexen-v1.removed.json",
    ]
    assert (tmp_path / CARD_FILENAME).read_text(encoding="utf-8") == card
    # Nothing beyond the curated subset leaks into the upload.
    published = sorted(
        str(path.relative_to(tmp_path)) for path in tmp_path.rglob("*") if path.is_file()
    )
    assert published == staged


def _declared_configs() -> set[str]:
    """Config names the card's front matter actually declares to the Hub."""
    card = CARD_TEMPLATE_PATH.read_text(encoding="utf-8")
    return set(re.findall(r"^- config_name: (\S+)$", card, flags=re.MULTILINE))


# A load_dataset call naming a config that the card does not declare raises
# `ValueError: BuilderConfig ... not found` for every reader who copies it. This shipped
# once: the README said `load_dataset("GliteTech/lexen", "items", ...)` while the config
# is named `default`, because the underlying file is data/items.jsonl.
LOAD_DATASET_WITH_CONFIG = re.compile(
    r"""load_dataset\(\s*["']GliteTech/lexen["']\s*,\s*["'](?P<config>[^"']+)["']"""
)


def _documented_snippets() -> dict[str, str]:
    """Every text a reader copies a load_dataset call out of.

    The card is checked AFTER rendering, because the template carries {{RELEASE_ID}} rather
    than the literal tag.
    """
    return {
        "rendered card": render_card(facts=_facts(), template_path=CARD_TEMPLATE_PATH),
        "README.md": (DEFAULT_REPO_ROOT / "README.md").read_text(encoding="utf-8"),
    }


def test_every_documented_load_dataset_config_exists() -> None:
    declared = _declared_configs()
    assert declared == {"default", "reviews"}

    for name, text in _documented_snippets().items():
        used = {m.group("config") for m in LOAD_DATASET_WITH_CONFIG.finditer(text)}
        assert used <= declared, (
            f"{name} documents load_dataset config(s) {sorted(used - declared)} that the card "
            f"does not declare. Declared: {sorted(declared)}. Readers copying this get "
            f"ValueError: BuilderConfig not found."
        )


def test_pinned_revisions_name_the_tag_publication_creates() -> None:
    """`revision=` must name the tag publication creates, or the snippet 404s."""
    for name, text in _documented_snippets().items():
        revisions = set(re.findall(r"""revision=["']([^"']+)["']""", text))
        assert revisions == {ACTIVE_RELEASE_ID}, (
            f"{name} should pin exactly {{{ACTIVE_RELEASE_ID!r}}}, found {sorted(revisions)}. "
            f"An empty set means the pin was dropped; anything else names a tag publication "
            f"never creates."
        )


class _StubHub:
    """Minimal stand-in for HfApi, recording the calls tag_release makes."""

    def __init__(self, *, tags: dict[str, str]) -> None:
        self._tags = tags
        self.calls: list[tuple[str, str]] = []

    def list_repo_refs(self, *, repo_id: str, repo_type: str) -> SimpleNamespace:
        return SimpleNamespace(
            tags=[SimpleNamespace(name=n, target_commit=c) for n, c in self._tags.items()]
        )

    def delete_tag(self, *, repo_id: str, repo_type: str, tag: str) -> None:
        self.calls.append(("delete", tag))

    def create_tag(
        self, *, repo_id: str, repo_type: str, tag: str, revision: str, **_: str
    ) -> None:
        self.calls.append(("create", revision))


def test_tag_is_created_on_a_repo_that_has_none() -> None:
    api = _StubHub(tags={})

    assert tag_release(api=api, repo_id=HF_REPO_ID, commit_oid="abc123") == TAG_CREATED
    assert api.calls == [("create", "abc123")]


def test_tag_already_on_the_upload_commit_is_left_alone() -> None:
    api = _StubHub(tags={ACTIVE_RELEASE_ID: "abc123"})

    assert tag_release(api=api, repo_id=HF_REPO_ID, commit_oid="abc123") == TAG_UNCHANGED
    assert api.calls == []


def test_stale_tag_is_moved_to_the_upload_commit() -> None:
    """`exist_ok=True` alone would silently leave the tag on the old commit."""
    api = _StubHub(tags={ACTIVE_RELEASE_ID: "old999"})

    assert tag_release(api=api, repo_id=HF_REPO_ID, commit_oid="new123") == TAG_MOVED
    assert api.calls == [("delete", ACTIVE_RELEASE_ID), ("create", "new123")]
