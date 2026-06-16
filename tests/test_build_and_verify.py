from __future__ import annotations

import shutil
import xml.etree.ElementTree as ET
from pathlib import Path

from lexen.io import read_json_object, read_jsonl_objects
from lexen.paths import (
    ACTIVE_RELEASE_ID,
    CANONICAL_ANNOTATORS,
    CANONICAL_ITEMS_FILENAME,
    DATA_DIRNAME,
    DATASET_METADATA_FILENAME,
    DECISION_THREE_WAY_EXACT,
    DECISION_THREE_WAY_NO_CONSENSUS,
    DECISION_TWO_OF_THREE_CANNOT_ANSWER,
    DECISION_TWO_OF_THREE_SENSE,
    DECISION_UNREVIEWED,
    EXPECTED_LEXEN_GOLD_CHANGED_FROM_MARU,
    EXPECTED_REMOVED_ITEMS,
    EXPECTED_REMOVED_THREE_WAY_NO_CONSENSUS,
    EXPECTED_REMOVED_TWO_OF_THREE_CANNOT_ANSWER,
    EXPECTED_REVIEWED_AUDIT_ITEMS,
    EXPECTED_REVIEWED_ITEMS,
    EXPECTED_SOURCE_ITEMS,
    EXPECTED_THREE_WAY_EXACT_AGREEMENT,
    EXPECTED_TOTAL_ITEMS,
    EXPECTED_TWO_OF_THREE_SENSE_AGREEMENT,
    EXPECTED_UNREVIEWED_ITEMS,
    EXPORTS_DIRNAME,
    GOLD_KEY_SUFFIX,
    RAGANATO_EXPORT_DIRNAME,
    REMOVED_SUFFIX,
    REVIEWS_FILENAME,
    SOURCE_MANIFEST_FILENAME,
    SOURCES_DIRNAME,
)
from lexen.release import build_release
from lexen.selection import build_selection_source
from lexen.source_manifest import write_source_manifest
from lexen.verify import verify_release

REPO_ROOT = Path(__file__).resolve().parents[1]


def copy_public_inputs(*, target_root: Path) -> None:
    shutil.copytree(REPO_ROOT / "sources", target_root / "sources")
    shutil.copytree(REPO_ROOT / "reports", target_root / "reports")


def test_release_builds_and_verifies_from_repo_local_sources(tmp_path: Path) -> None:
    copy_public_inputs(target_root=tmp_path)

    build_result = build_release(
        repo_root=tmp_path,
        output_root=tmp_path,
        release_id=ACTIVE_RELEASE_ID,
    )
    verify_report = verify_release(repo_root=tmp_path, release_id=ACTIVE_RELEASE_ID)

    expected_counts = {
        "decision." + DECISION_THREE_WAY_EXACT: EXPECTED_THREE_WAY_EXACT_AGREEMENT,
        "decision." + DECISION_THREE_WAY_NO_CONSENSUS: (EXPECTED_REMOVED_THREE_WAY_NO_CONSENSUS),
        "decision." + DECISION_TWO_OF_THREE_CANNOT_ANSWER: (
            EXPECTED_REMOVED_TWO_OF_THREE_CANNOT_ANSWER
        ),
        "decision." + DECISION_TWO_OF_THREE_SENSE: EXPECTED_TWO_OF_THREE_SENSE_AGREEMENT,
        "decision." + DECISION_UNREVIEWED: EXPECTED_UNREVIEWED_ITEMS,
        "lexen_gold_changed_from_maru": EXPECTED_LEXEN_GOLD_CHANGED_FROM_MARU,
        "removed_items": EXPECTED_REMOVED_ITEMS,
        "reviewed_audit_items": EXPECTED_REVIEWED_AUDIT_ITEMS,
        "reviewed_items": EXPECTED_REVIEWED_ITEMS,
        "total_source_items": EXPECTED_SOURCE_ITEMS,
        "total_items": EXPECTED_TOTAL_ITEMS,
        "unreviewed_items": EXPECTED_UNREVIEWED_ITEMS,
    }
    assert build_result.counts == expected_counts
    assert verify_report["status"] == "ok"
    assert verify_report["counts"] == expected_counts


def test_release_sources_include_same_protocol_reviews(tmp_path: Path) -> None:
    copy_public_inputs(target_root=tmp_path)

    build_release(repo_root=tmp_path, output_root=tmp_path, release_id=ACTIVE_RELEASE_ID)

    review_source_dirs = sorted(path.name for path in (tmp_path / "sources" / "reviews").iterdir())
    assert review_source_dirs == [
        "ph-2026-06-13",
        "protocols",
        "pw-2026-05-29",
        "rf-2026-05-26",
    ]

    dataset = read_json_object(
        path=tmp_path / DATA_DIRNAME / ACTIVE_RELEASE_ID / DATASET_METADATA_FILENAME
    )
    source_artifacts = dataset["source_artifacts"]
    assert isinstance(source_artifacts, list)
    source_paths = {str(artifact["path"]) for artifact in source_artifacts}
    assert str(Path(SOURCES_DIRNAME) / SOURCE_MANIFEST_FILENAME) in source_paths
    assert any("/raganato/original/files/ALL.gold.key.txt" in path for path in source_paths)
    assert any("/maru2022/original/files/ALLamended.gold.key.txt" in path for path in source_paths)
    assert any("/ph-2026-06-13/" in path for path in source_paths)
    assert any("/protocols/marureview-brief-2026-05-26.md" in path for path in source_paths)


def test_review_export_keeps_full_three_annotator_notes(tmp_path: Path) -> None:
    copy_public_inputs(target_root=tmp_path)

    build_release(repo_root=tmp_path, output_root=tmp_path, release_id=ACTIVE_RELEASE_ID)

    reviews = read_jsonl_objects(
        path=tmp_path / DATA_DIRNAME / ACTIVE_RELEASE_ID / REVIEWS_FILENAME
    )
    assert len(reviews) == EXPECTED_REVIEWED_AUDIT_ITEMS
    assert all(set(review["annotators"]) == {"RF", "PW", "PH"} for review in reviews)
    assert any(review["annotators"]["RF"]["comment"] is not None for review in reviews)
    assert any(review["annotators"]["PW"]["comment"] is not None for review in reviews)
    assert any(review["annotators"]["PH"]["comment"] is not None for review in reviews)
    assert any(review["annotators"]["RF"]["cannot_answer_notes"] is not None for review in reviews)
    assert any(review["annotators"]["PW"]["cannot_answer_notes"] is not None for review in reviews)
    assert any(review["annotators"]["PH"]["cannot_answer_notes"] is not None for review in reviews)


def test_canonical_records_use_lexen_gold_schema(tmp_path: Path) -> None:
    copy_public_inputs(target_root=tmp_path)

    build_release(repo_root=tmp_path, output_root=tmp_path, release_id=ACTIVE_RELEASE_ID)

    items = read_jsonl_objects(
        path=tmp_path / DATA_DIRNAME / ACTIVE_RELEASE_ID / CANONICAL_ITEMS_FILENAME
    )
    assert len(items) == EXPECTED_TOTAL_ITEMS
    assert all("lexen_gold" in item["labels"] for item in items)
    assert all("maru2022" in item["labels"] for item in items)
    assert all("raganato_original" in item["labels"] for item in items)
    assert all("lexen_majority" not in item["labels"] for item in items)
    assert all("lexen_primary_scorable" not in item["labels"] for item in items)
    assert all(not item["labels"]["lexen_gold"]["is_empty"] for item in items)
    assert all(item["labels"]["maru2022"]["sense_keys"] for item in items)
    assert all(item["labels"]["raganato_original"]["sense_keys"] for item in items)
    assert all(item["glite"]["schema_version"] == "lexen.glite.v1" for item in items)
    assert all(
        {"raganato_original", "maru2022", "lexen_gold"} <= set(item["glite"]["labels"])
        for item in items
    )
    assert all(item["glite"]["candidate_sense_mappings"] for item in items)

    reviewed_items = [item for item in items if item["review"]["status"] == "reviewed"]
    unreviewed_items = [item for item in items if item["review"]["status"] == "unreviewed"]
    assert len(reviewed_items) == EXPECTED_REVIEWED_ITEMS
    assert len(unreviewed_items) == EXPECTED_UNREVIEWED_ITEMS
    assert all(
        set(item["review"]["annotators"]) == set(CANONICAL_ANNOTATORS) for item in reviewed_items
    )
    assert all(
        set(item["glite"]["reviewers"]) == set(CANONICAL_ANNOTATORS) for item in reviewed_items
    )
    assert all(item["review"]["annotators"] is None for item in unreviewed_items)
    assert all(item["glite"]["reviewers"] is None for item in unreviewed_items)


def test_removed_items_are_excluded_from_benchmark_exports(tmp_path: Path) -> None:
    copy_public_inputs(target_root=tmp_path)

    build_release(repo_root=tmp_path, output_root=tmp_path, release_id=ACTIVE_RELEASE_ID)

    release_dir = tmp_path / DATA_DIRNAME / ACTIVE_RELEASE_ID
    raganato_dir = tmp_path / EXPORTS_DIRNAME / RAGANATO_EXPORT_DIRNAME / ACTIVE_RELEASE_ID
    items = read_jsonl_objects(path=release_dir / CANONICAL_ITEMS_FILENAME)
    item_ids = {str(item["item_id"]) for item in items}
    removed = read_json_object(path=raganato_dir / f"{ACTIVE_RELEASE_ID}{REMOVED_SUFFIX}")
    removed_items = removed["items"]
    assert isinstance(removed_items, list)
    removed_ids = {str(item["item_id"]) for item in removed_items}

    assert len(removed_ids) == EXPECTED_REMOVED_ITEMS
    assert item_ids.isdisjoint(removed_ids)
    assert all(item["labels"]["lexen_gold"]["is_empty"] for item in removed_items)
    assert all(item["labels"]["maru2022"]["sense_keys"] for item in removed_items)
    assert all(item["labels"]["raganato_original"]["sense_keys"] for item in removed_items)
    assert all(
        set(item["review"]["annotators"]) == set(CANONICAL_ANNOTATORS) for item in removed_items
    )
    assert all(
        set(item["glite"]["reviewers"]) == set(CANONICAL_ANNOTATORS) for item in removed_items
    )
    assert {
        str(item["removal"]["decision"]) for item in removed_items if isinstance(item, dict)
    } == {DECISION_TWO_OF_THREE_CANNOT_ANSWER, DECISION_THREE_WAY_NO_CONSENSUS}
    assert (
        sum(
            1
            for item in removed_items
            if item["removal"]["decision"] == DECISION_TWO_OF_THREE_CANNOT_ANSWER
        )
        == EXPECTED_REMOVED_TWO_OF_THREE_CANNOT_ANSWER
    )
    assert (
        sum(
            1
            for item in removed_items
            if item["removal"]["decision"] == DECISION_THREE_WAY_NO_CONSENSUS
        )
        == EXPECTED_REMOVED_THREE_WAY_NO_CONSENSUS
    )

    gold_path = raganato_dir / f"{ACTIVE_RELEASE_ID}{GOLD_KEY_SUFFIX}"
    gold_ids = {line.split()[0] for line in gold_path.read_text(encoding="utf-8").splitlines()}
    assert gold_ids == item_ids
    assert gold_ids.isdisjoint(removed_ids)

    xml_path = raganato_dir / f"{ACTIVE_RELEASE_ID}.data.xml"
    xml_ids = {element.attrib["id"] for element in ET.parse(xml_path).getroot().iter("instance")}
    assert xml_ids == item_ids
    assert xml_ids.isdisjoint(removed_ids)


def test_selection_source_verifies_from_committed_model_panel(tmp_path: Path) -> None:
    copy_public_inputs(target_root=tmp_path)

    report = build_selection_source(repo_root=tmp_path, verify=True)

    assert report["status"] == "ok"
    assert report["selection_rows"] == EXPECTED_SOURCE_ITEMS
    assert report["suspicious_total"] == EXPECTED_REVIEWED_AUDIT_ITEMS
    assert report["suspicion_counts"] == {
        "S1": 55,
        "S2": 138,
        "S3": 41,
        "S4": 75,
        "S5": 48,
        "S6": 6,
    }


def test_source_manifest_covers_primary_source_packages(tmp_path: Path) -> None:
    copy_public_inputs(target_root=tmp_path)

    manifest_path = write_source_manifest(repo_root=tmp_path)
    manifest = read_json_object(path=manifest_path)
    packages = manifest["packages"]
    assert isinstance(packages, list)
    package_by_id = {str(package["package_id"]): package for package in packages}

    for package_id in [
        "raganato-original-all",
        "maru2022-allamended",
        "lexen-model-panel",
        "lexen-selection",
        "lexen-reviews",
        "glite-coarsening",
    ]:
        package = package_by_id[package_id]
        assert package["files"]
        assert all(
            str(file_record["sha256"]).startswith("sha256:") for file_record in package["files"]
        )
