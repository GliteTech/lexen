from __future__ import annotations

from dataclasses import replace
from pathlib import Path

import pytest

from lexen.huggingface import (
    CARD_FILENAME,
    PINNED_EXPORT_SHA256,
    CardFacts,
    collect_facts,
    render_card,
    stage_release,
    verify_pinned_export,
)
from lexen.paths import DATASET_CANARY, DEFAULT_REPO_ROOT

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
