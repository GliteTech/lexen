"""Build and publish the Hugging Face dataset release for lexEN.

The dataset card is generated rather than hand-written. Every count, agreement figure
and hash in it is read from the release artifacts, so the card cannot drift away from
the data the way a hand-maintained document would.

The published payload is a curated subset of the repository, not a mirror: the
SenseBench items export, the reviewer record, the Raganato-format exports, the
datasheet and the citation file.
"""

from __future__ import annotations

import shutil
import sys
from argparse import ArgumentParser
from dataclasses import dataclass
from pathlib import Path
from tempfile import TemporaryDirectory
from typing import Any

from lexen.io import read_json_object, sha256_file
from lexen.models import JsonObject
from lexen.paths import (
    ACTIVE_RELEASE_ID,
    DATA_DIRNAME,
    DATASET_CANARY,
    DEFAULT_REPO_ROOT,
    EXPORTS_DIRNAME,
    RAGANATO_EXPORT_DIRNAME,
    REPORTS_DIRNAME,
    SENSEBENCH_EXPORT_DIRNAME,
)

HF_REPO_ID: str = "GliteTech/lexen"
HF_REPO_TYPE: str = "dataset"

AGREEMENT_REPORT_DIRNAME: str = "rf-pw-ph-2026-06-13"
AGREEMENT_METRICS_FILENAME: str = "metrics.json"

FINE_GRANULARITY_KEY: str = "fine"
COARSE_GRANULARITY_KEY: str = "glite"
NON_UNANIMOUS_RESOLVED_KEY: str = "fine_non_unanimous_resolved_by_glite"

DATASHEET_FILENAME: str = "DATASHEET.md"
CITATION_FILENAME: str = "CITATION.cff"
CARD_FILENAME: str = "README.md"

# The one file SenseBench pins by content hash. If this changes, every published run
# on the leaderboard silently stops referring to the same data, so publication aborts.
PINNED_EXPORT_SHA256: str = (
    "sha256:5fd4382b93f19087a1e31f6dd7d1db17c1eb17ff80fcbe1d3fdd55c0c3ecefe8"
)

COMMIT_MESSAGE: str = f"Publish {ACTIVE_RELEASE_ID}"
TAG_MESSAGE: str = f"lexEN {ACTIVE_RELEASE_ID} release as pinned by SenseBench"

TAG_CREATED: str = "created"
TAG_MOVED: str = "moved"
TAG_UNCHANGED: str = "unchanged"

HUB_CLIENT_MISSING_MESSAGE: str = (
    "the Hugging Face client is not installed. It is an optional extra because building and "
    "verifying the release does not need it:\n\n    uv sync --extra huggingface\n\n"
    "Re-run with --dry-run to render the card and inspect the payload without it."
)


@dataclass(frozen=True, slots=True)
class PublishedFile:
    source: Path
    target: str


@dataclass(frozen=True, slots=True)
class CardFacts:
    """Every number the card states, read from the release rather than typed."""

    total_items: int
    reviewed_items: int
    source_items: int
    unreviewed_items: int
    changed_labels: int
    removed_items: int
    retained_unanimous: int
    retained_two_of_three: int
    removed_cannot_answer: int
    removed_no_consensus: int
    fine_kappa: float
    coarse_kappa: float
    fine_agreement_pct: float
    coarse_agreement_pct: float
    non_unanimous_resolved_pct: float
    items_sha256: str


def _published_files(*, repo_root: Path) -> tuple[PublishedFile, ...]:
    exports = repo_root / EXPORTS_DIRNAME
    data = repo_root / DATA_DIRNAME / ACTIVE_RELEASE_ID
    raganato = exports / RAGANATO_EXPORT_DIRNAME / ACTIVE_RELEASE_ID
    return (
        PublishedFile(
            source=exports / SENSEBENCH_EXPORT_DIRNAME / ACTIVE_RELEASE_ID / "items.jsonl",
            target=f"{DATA_DIRNAME}/items.jsonl",
        ),
        PublishedFile(source=data / "reviews.jsonl", target=f"{DATA_DIRNAME}/reviews.jsonl"),
        PublishedFile(
            source=raganato / f"{ACTIVE_RELEASE_ID}.data.xml",
            target=f"{RAGANATO_EXPORT_DIRNAME}/{ACTIVE_RELEASE_ID}.data.xml",
        ),
        PublishedFile(
            source=raganato / f"{ACTIVE_RELEASE_ID}.gold.key.txt",
            target=f"{RAGANATO_EXPORT_DIRNAME}/{ACTIVE_RELEASE_ID}.gold.key.txt",
        ),
        PublishedFile(
            source=raganato / f"{ACTIVE_RELEASE_ID}.removed.json",
            target=f"{RAGANATO_EXPORT_DIRNAME}/{ACTIVE_RELEASE_ID}.removed.json",
        ),
        PublishedFile(source=repo_root / DATASHEET_FILENAME, target=DATASHEET_FILENAME),
        PublishedFile(source=repo_root / CITATION_FILENAME, target=CITATION_FILENAME),
    )


def collect_facts(*, repo_root: Path) -> CardFacts:
    dataset = read_json_object(path=repo_root / DATA_DIRNAME / ACTIVE_RELEASE_ID / "dataset.json")
    metrics = read_json_object(
        path=repo_root / REPORTS_DIRNAME / AGREEMENT_REPORT_DIRNAME / AGREEMENT_METRICS_FILENAME
    )["metrics"]
    counts = dataset["counts"]
    items_path = (
        repo_root / EXPORTS_DIRNAME / SENSEBENCH_EXPORT_DIRNAME / ACTIVE_RELEASE_ID / "items.jsonl"
    )
    fine = metrics[FINE_GRANULARITY_KEY]
    coarse = metrics[COARSE_GRANULARITY_KEY]
    return CardFacts(
        total_items=counts["total_items"],
        reviewed_items=counts["reviewed_audit_items"],
        source_items=counts["total_source_items"],
        unreviewed_items=counts["unreviewed_items"],
        changed_labels=counts["lexen_gold_changed_from_maru"],
        removed_items=counts["removed_items"],
        retained_unanimous=counts["decision.three_way_exact_agreement"],
        retained_two_of_three=counts["decision.two_of_three_sense_agreement"],
        removed_cannot_answer=counts["decision.two_of_three_cannot_answer_removed"],
        removed_no_consensus=counts["decision.three_way_no_consensus_removed"],
        fine_kappa=fine["fleiss_kappa"],
        coarse_kappa=coarse["fleiss_kappa"],
        fine_agreement_pct=_agreement_percent(granularity=fine),
        coarse_agreement_pct=_agreement_percent(granularity=coarse),
        non_unanimous_resolved_pct=metrics[NON_UNANIMOUS_RESOLVED_KEY]["percent"],
        items_sha256=sha256_file(path=items_path),
    )


def _agreement_percent(*, granularity: JsonObject) -> float:
    relationships = granularity["relationship_counts"]
    unanimous: int = int(relationships["all_three_agree_and_gold"]["count"]) + int(
        relationships["all_three_agree_but_different"]["count"]
    )
    return 100.0 * unanimous / int(granularity["total_items"])


def tag_release(*, api: Any, repo_id: str, commit_oid: str) -> str:
    """Point the release tag at the commit just published.

    Tagging with `exist_ok=True` and no revision would be a silent no-op whenever the tag
    already exists, leaving it on an older commit while the card claims that revision is the
    release. Bind the tag to the upload commit, and move it deliberately when it has drifted.
    """
    existing = next(
        (
            tag
            for tag in api.list_repo_refs(repo_id=repo_id, repo_type=HF_REPO_TYPE).tags
            if tag.name == ACTIVE_RELEASE_ID
        ),
        None,
    )
    if existing is not None:
        if existing.target_commit == commit_oid:
            return TAG_UNCHANGED
        api.delete_tag(repo_id=repo_id, repo_type=HF_REPO_TYPE, tag=ACTIVE_RELEASE_ID)

    api.create_tag(
        repo_id=repo_id,
        repo_type=HF_REPO_TYPE,
        tag=ACTIVE_RELEASE_ID,
        tag_message=TAG_MESSAGE,
        revision=commit_oid,
    )
    return TAG_CREATED if existing is None else TAG_MOVED


def verify_pinned_export(*, facts: CardFacts) -> None:
    if facts.items_sha256 != PINNED_EXPORT_SHA256:
        raise ValueError(
            "refusing to publish: the items export no longer matches the hash SenseBench "
            f"pins.\n  expected {PINNED_EXPORT_SHA256}\n  found    {facts.items_sha256}\n"
            "Publishing this would silently detach the Hub copy from every result already "
            "on the leaderboard. Ship a new release id instead of changing this one."
        )


def render_card(*, facts: CardFacts, template_path: Path) -> str:
    reviewed_share = 100.0 * facts.reviewed_items / facts.source_items
    replacements = {
        "{{TOTAL_ITEMS}}": f"{facts.total_items:,}",
        "{{REVIEWED_ITEMS}}": f"{facts.reviewed_items:,}",
        "{{SOURCE_ITEMS}}": f"{facts.source_items:,}",
        "{{UNREVIEWED_ITEMS}}": f"{facts.unreviewed_items:,}",
        "{{REVIEWED_SHARE_PCT}}": f"{reviewed_share:.1f}",
        "{{CHANGED_LABELS}}": f"{facts.changed_labels:,}",
        "{{REMOVED_ITEMS}}": f"{facts.removed_items:,}",
        "{{RETAINED_TOTAL}}": f"{facts.retained_unanimous + facts.retained_two_of_three:,}",
        "{{RETAINED_UNANIMOUS}}": f"{facts.retained_unanimous:,}",
        "{{RETAINED_TWO_OF_THREE}}": f"{facts.retained_two_of_three:,}",
        "{{REMOVED_CANNOT_ANSWER}}": f"{facts.removed_cannot_answer:,}",
        "{{REMOVED_NO_CONSENSUS}}": f"{facts.removed_no_consensus:,}",
        "{{FINE_KAPPA}}": f"{facts.fine_kappa:.3f}",
        "{{COARSE_KAPPA}}": f"{facts.coarse_kappa:.3f}",
        "{{FINE_AGREEMENT_PCT}}": f"{facts.fine_agreement_pct:.1f}",
        "{{COARSE_AGREEMENT_PCT}}": f"{facts.coarse_agreement_pct:.1f}",
        "{{NON_UNANIMOUS_RESOLVED_PCT}}": f"{facts.non_unanimous_resolved_pct:.1f}",
        "{{ITEMS_SHA256}}": facts.items_sha256.removeprefix("sha256:"),
        "{{RELEASE_ID}}": ACTIVE_RELEASE_ID,
        "{{DATASET_CANARY}}": DATASET_CANARY,
    }
    card = template_path.read_text(encoding="utf-8")
    for placeholder, value in replacements.items():
        card = card.replace(placeholder, value)
    unresolved = [line for line in card.splitlines() if "{{" in line]
    if len(unresolved) > 0:
        raise ValueError(f"card template has unresolved placeholders: {unresolved[:3]}")
    return card


def stage_release(*, repo_root: Path, staging_dir: Path, card: str) -> list[str]:
    staged: list[str] = []
    for published in _published_files(repo_root=repo_root):
        if not published.source.exists():
            raise FileNotFoundError(f"missing publishable file: {published.source}")
        target = staging_dir / published.target
        target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(published.source, target)
        staged.append(published.target)
    (staging_dir / CARD_FILENAME).write_text(card, encoding="utf-8")
    staged.append(CARD_FILENAME)
    return sorted(staged)


def main() -> int:
    parser = ArgumentParser(description=__doc__)
    parser.add_argument("--repo-root", type=Path, default=DEFAULT_REPO_ROOT)
    parser.add_argument("--repo-id", type=str, default=HF_REPO_ID)
    parser.add_argument(
        "--card-template",
        type=Path,
        default=None,
        help="Defaults to <repo-root>/templates/huggingface_card.md",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Render the card and list the payload without contacting the Hub.",
    )
    args = parser.parse_args()

    repo_root: Path = args.repo_root
    template_path: Path = args.card_template or repo_root / "templates" / "huggingface_card.md"

    facts = collect_facts(repo_root=repo_root)
    verify_pinned_export(facts=facts)
    card = render_card(facts=facts, template_path=template_path)

    with TemporaryDirectory() as tmp:
        staging_dir = Path(tmp)
        staged = stage_release(repo_root=repo_root, staging_dir=staging_dir, card=card)
        if args.dry_run:
            print(f"card rendered from {ACTIVE_RELEASE_ID} ({len(card.splitlines())} lines)")
            print(f"items export verified: {facts.items_sha256}")
            print("payload:")
            for name in staged:
                print(f"  {name}")
            print(f"\nwould publish to https://huggingface.co/datasets/{args.repo_id}")
            return 0

        # Deferred so that --dry-run works without the optional extra installed.
        try:
            from huggingface_hub import HfApi
        except ModuleNotFoundError:
            print(HUB_CLIENT_MISSING_MESSAGE, file=sys.stderr)
            return 1

        api = HfApi()
        api.create_repo(repo_id=args.repo_id, repo_type=HF_REPO_TYPE, exist_ok=True)
        commit = api.upload_folder(
            folder_path=str(staging_dir),
            repo_id=args.repo_id,
            repo_type=HF_REPO_TYPE,
            commit_message=COMMIT_MESSAGE,
        )
        outcome = tag_release(api=api, repo_id=args.repo_id, commit_oid=commit.oid)
    print(f"published https://huggingface.co/datasets/{args.repo_id}")
    print(f"tag {ACTIVE_RELEASE_ID} {outcome} at {commit.oid[:8]}")
    return 0
