"""Verify generated lexEN release artifacts."""

from __future__ import annotations

import argparse
import json
import xml.etree.ElementTree as ET
from collections import Counter
from dataclasses import dataclass
from pathlib import Path

from lexen.io import read_json_object, read_jsonl_objects, sha256_file
from lexen.models import JsonObject, SenseKey
from lexen.paths import (
    ACTIVE_RELEASE_ID,
    CANONICAL_ITEMS_FILENAME,
    DATA_DIRNAME,
    DATASET_CANARY,
    DATASET_METADATA_FILENAME,
    DECISION_THREE_WAY_EXACT,
    DECISION_THREE_WAY_NO_CONSENSUS,
    DECISION_TWO_OF_THREE_CANNOT_ANSWER,
    DECISION_TWO_OF_THREE_SENSE,
    DEFAULT_REPO_ROOT,
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
    MARU_SOURCE_DIR,
    MARU_XML_FILENAME,
    PH_ANNOTATOR_ID,
    PW_ANNOTATOR_ID,
    RAGANATO_EXPORT_DIRNAME,
    REMOVED_SCHEMA_VERSION,
    REMOVED_SUFFIX,
    REVIEWS_FILENAME,
    RF_ANNOTATOR_ID,
    SENSEBENCH_EXPORT_DIRNAME,
    SOURCE_MANIFEST_FILENAME,
    SOURCES_DIRNAME,
    SUPPORTED_RELEASE_IDS,
    XML_CANARY_PREFIX,
    XML_CANARY_SUFFIX,
)


@dataclass(frozen=True, slots=True)
class LabelView:
    """Labels extracted from a canonical item."""

    canonical_prefix: str
    maru_keys: list[SenseKey]
    raganato_original_keys: list[SenseKey]
    canonical_keys: list[SenseKey]
    canonical_is_empty: bool
    decision: str


def read_gold_key(*, path: Path) -> dict[str, list[SenseKey]]:
    labels: dict[str, list[SenseKey]] = {}
    with path.open(encoding="utf-8") as handle:
        for line_number, raw_line in enumerate(handle, start=1):
            parts = raw_line.strip().split()
            if len(parts) < 2:
                raise ValueError(f"gold key line has no sense key at {path}:{line_number}")
            item_id = parts[0]
            if item_id in labels:
                raise ValueError(f"duplicate gold key item id {item_id}")
            labels[item_id] = parts[1:]
    return labels


def dataset_canary_value(*, dataset: JsonObject) -> str:
    canary = dataset["contamination_canary"]
    if not isinstance(canary, dict):
        raise TypeError("contamination_canary must be an object")
    value = canary["value"]
    if not isinstance(value, str) or len(value) == 0:
        raise ValueError("contamination_canary.value must be a non-empty string")
    return value


def require_unique_item_ids(*, rows: list[JsonObject], path: Path) -> None:
    seen: set[str] = set()
    for row in rows:
        item_id = str(row["item_id"])
        if item_id in seen:
            raise ValueError(f"duplicate item_id {item_id} in {path}")
        seen.add(item_id)


def label_view(*, item: JsonObject) -> LabelView:
    labels = item["labels"]
    if not isinstance(labels, dict):
        raise TypeError("labels must be an object")
    if "lexen_primary_scorable" in labels:
        raise ValueError(f"legacy lexen_primary_scorable field present for {item['item_id']}")
    maru = labels["maru2022"]
    if not isinstance(maru, dict):
        raise TypeError("label entries must be objects")
    raganato_original = labels["raganato_original"]
    if not isinstance(raganato_original, dict):
        raise TypeError("Raganato original label entry must be an object")
    if "lexen_gold" in labels:
        canonical = labels["lexen_gold"]
        prefix = "lexen_gold"
    else:
        raise ValueError(f"canonical lexen_gold field missing for {item['item_id']}")
    if not isinstance(canonical, dict):
        raise TypeError("canonical label entry must be an object")
    return LabelView(
        canonical_is_empty=bool(canonical["is_empty"]),
        canonical_keys=[str(key) for key in canonical["sense_keys"]],
        canonical_prefix=prefix,
        decision=str(canonical["decision"]),
        maru_keys=[str(key) for key in maru["sense_keys"]],
        raganato_original_keys=[str(key) for key in raganato_original["sense_keys"]],
    )


def verify_glite_layer(
    *,
    item: JsonObject,
    labels: LabelView,
    reviewed: bool,
) -> None:
    glite = item["glite"]
    if not isinstance(glite, dict):
        raise TypeError(f"glite must be an object for {item['item_id']}")
    glite_labels = glite["labels"]
    if not isinstance(glite_labels, dict):
        raise TypeError(f"glite.labels must be an object for {item['item_id']}")
    for label_name, fine_keys in [
        ("raganato_original", labels.raganato_original_keys),
        ("maru2022", labels.maru_keys),
        ("lexen_gold", labels.canonical_keys),
    ]:
        label = glite_labels[label_name]
        if not isinstance(label, dict):
            raise TypeError(f"glite label {label_name} must be an object")
        if len(fine_keys) > 0 and len(label["concept_ids"]) == 0:
            raise ValueError(
                f"glite label {label_name} empty for non-empty label {item['item_id']}"
            )
    candidate_sense_keys = {str(key) for key in item["candidate_sense_keys"]}
    candidate_mappings = glite["candidate_sense_mappings"]
    if not isinstance(candidate_mappings, list):
        raise TypeError(f"glite candidate_sense_mappings must be a list for {item['item_id']}")
    mapped_candidate_keys = {str(row["sense_key"]) for row in candidate_mappings}
    if mapped_candidate_keys != candidate_sense_keys:
        raise ValueError(
            f"glite candidate mappings differ from candidate_sense_keys for {item['item_id']}"
        )
    reviewers = glite["reviewers"]
    if reviewed:
        if not isinstance(reviewers, dict):
            raise TypeError(f"reviewed item missing glite reviewer labels for {item['item_id']}")
        if set(reviewers) != {RF_ANNOTATOR_ID, PW_ANNOTATOR_ID, PH_ANNOTATOR_ID}:
            raise ValueError(f"bad glite reviewer keys for {item['item_id']}")
    elif reviewers is not None:
        raise ValueError(f"unreviewed item has glite reviewer labels for {item['item_id']}")


def verify_artifact_hashes(
    *,
    artifacts: object,
    repo_root: Path,
    label: str,
) -> None:
    if not isinstance(artifacts, list):
        raise TypeError(f"{label} must be a list")
    for artifact in artifacts:
        if not isinstance(artifact, dict):
            raise TypeError(f"{label} entries must be objects")
        path = repo_root / str(artifact["path"])
        expected_hash = str(artifact["sha256"])
        actual_hash = sha256_file(path=path)
        if actual_hash != expected_hash:
            raise ValueError(
                f"hash mismatch for {path}: expected {expected_hash}, got {actual_hash}"
            )


def verify_source_manifest(*, repo_root: Path) -> None:
    manifest_path = repo_root / SOURCES_DIRNAME / SOURCE_MANIFEST_FILENAME
    manifest = read_json_object(path=manifest_path)
    packages = manifest["packages"]
    if not isinstance(packages, list):
        raise TypeError("source manifest packages must be a list")
    for package in packages:
        if not isinstance(package, dict):
            raise TypeError("source manifest package entries must be objects")
        files = package["files"]
        if not isinstance(files, list):
            raise TypeError("source manifest package files must be a list")
        verify_artifact_hashes(
            artifacts=files,
            repo_root=repo_root,
            label=f"source_manifest:{package['package_id']}",
        )


def verify_items(
    *,
    release_id: str,
    items: list[JsonObject],
    reviews: list[JsonObject],
    removed_items: list[JsonObject],
    dataset_canary: str,
) -> dict[str, int]:
    counts: Counter[str] = Counter()
    item_ids = {str(item["item_id"]) for item in items}
    reviewed_ids = {str(review["item_id"]) for review in reviews}
    removed_ids = {str(item["item_id"]) for item in removed_items}
    if item_ids & removed_ids:
        overlap = ", ".join(sorted(item_ids & removed_ids)[:5])
        raise ValueError(f"removed ids appear in canonical items: {overlap}")
    for review in reviews:
        if review["dataset_canary"] != dataset_canary:
            raise ValueError(f"review canary mismatch for {review['item_id']}")
        if release_id == ACTIVE_RELEASE_ID:
            annotators = review["annotators"]
            if not isinstance(annotators, dict):
                raise TypeError("annotators must be an object")
            if set(annotators) != {RF_ANNOTATOR_ID, PW_ANNOTATOR_ID, PH_ANNOTATOR_ID}:
                raise ValueError(
                    f"release review has non-canonical annotators: {review['item_id']}"
                )
        consensus = review["consensus"]
        if not isinstance(consensus, dict):
            raise TypeError("review consensus must be an object")
        if str(review["item_id"]) in removed_ids:
            if consensus["disposition"] != "removed":
                raise ValueError(f"removed review has non-removed disposition: {review['item_id']}")
        elif str(review["item_id"]) in item_ids and consensus["disposition"] != "retained":
            raise ValueError(f"retained review has non-retained disposition: {review['item_id']}")

    missing_reviewed_ids = reviewed_ids - item_ids - removed_ids
    if len(missing_reviewed_ids) > 0:
        sample = ", ".join(sorted(missing_reviewed_ids)[:5])
        raise ValueError(f"reviewed ids are neither retained nor removed: {sample}")

    for item in items:
        if item["dataset_canary"] != dataset_canary:
            raise ValueError(f"item canary mismatch for {item['item_id']}")
        labels = label_view(item=item)
        reviewed = bool(item["review"]["is_reviewed"])
        item_id = str(item["item_id"])
        review_status = item["review"].get("status")
        expected_status = "reviewed" if reviewed else "unreviewed"
        if review_status != expected_status:
            raise ValueError(f"bad review status for {item_id}: {review_status}")
        if reviewed and item_id not in reviewed_ids:
            raise ValueError(f"reviewed item missing review row: {item_id}")
        if not reviewed and item_id in reviewed_ids:
            raise ValueError(f"unreviewed item has review row: {item_id}")
        embedded_annotators = item["review"].get("annotators")
        embedded_consensus = item["review"].get("consensus")
        if reviewed:
            if not isinstance(embedded_annotators, dict):
                raise TypeError(f"reviewed item missing embedded annotators: {item_id}")
            if set(embedded_annotators) != {RF_ANNOTATOR_ID, PW_ANNOTATOR_ID, PH_ANNOTATOR_ID}:
                raise ValueError(f"bad embedded annotators for {item_id}")
            if not isinstance(embedded_consensus, dict):
                raise TypeError(f"reviewed item missing embedded consensus: {item_id}")
        elif embedded_annotators is not None or embedded_consensus is not None:
            raise ValueError(f"unreviewed item has embedded review details: {item_id}")
        if len(labels.maru_keys) == 0:
            raise ValueError(f"Maru label is empty for {item_id}")
        if len(labels.raganato_original_keys) == 0:
            raise ValueError(f"Raganato original label is empty for {item_id}")
        if labels.canonical_is_empty != (len(labels.canonical_keys) == 0):
            raise ValueError(f"bad canonical is_empty flag for {item_id}")
        if labels.canonical_is_empty or len(labels.canonical_keys) == 0:
            raise ValueError(f"retained item has empty lexEN label for {item_id}")
        verify_glite_layer(item=item, labels=labels, reviewed=reviewed)
        if sorted(labels.canonical_keys) != sorted(labels.maru_keys):
            counts[f"{labels.canonical_prefix}_changed_from_maru"] += 1
        counts[f"decision.{labels.decision}"] += 1
        counts["reviewed_items" if reviewed else "unreviewed_items"] += 1
        counts["total_items"] += 1
    counts["removed_items"] = len(removed_ids)
    counts["reviewed_audit_items"] = len(reviewed_ids)
    counts["total_source_items"] = len(item_ids) + len(removed_ids)
    return dict(sorted(counts.items()))


def verify_active_expected_counts(*, counts: dict[str, int]) -> None:
    expected = {
        "decision." + DECISION_THREE_WAY_EXACT: EXPECTED_THREE_WAY_EXACT_AGREEMENT,
        "decision." + DECISION_THREE_WAY_NO_CONSENSUS: (EXPECTED_REMOVED_THREE_WAY_NO_CONSENSUS),
        "decision." + DECISION_TWO_OF_THREE_CANNOT_ANSWER: (
            EXPECTED_REMOVED_TWO_OF_THREE_CANNOT_ANSWER
        ),
        "decision." + DECISION_TWO_OF_THREE_SENSE: EXPECTED_TWO_OF_THREE_SENSE_AGREEMENT,
        "lexen_gold_changed_from_maru": EXPECTED_LEXEN_GOLD_CHANGED_FROM_MARU,
        "removed_items": EXPECTED_REMOVED_ITEMS,
        "reviewed_audit_items": EXPECTED_REVIEWED_AUDIT_ITEMS,
        "reviewed_items": EXPECTED_REVIEWED_ITEMS,
        "total_source_items": EXPECTED_SOURCE_ITEMS,
        "total_items": EXPECTED_TOTAL_ITEMS,
        "unreviewed_items": EXPECTED_UNREVIEWED_ITEMS,
    }
    for key, expected_value in expected.items():
        actual_value = counts.get(key)
        if actual_value != expected_value:
            raise ValueError(f"expected {key}={expected_value}, got {actual_value}")


def verify_metadata_counts(*, dataset: JsonObject, computed_counts: dict[str, int]) -> None:
    metadata_counts = dataset["counts"]
    if not isinstance(metadata_counts, dict):
        raise TypeError("dataset counts must be an object")
    for key, value in computed_counts.items():
        if int(metadata_counts.get(key, -1)) != value:
            raise ValueError(
                f"metadata count mismatch for {key}: expected {value}, "
                f"got {metadata_counts.get(key)}"
            )


def verify_gold_export(*, items: list[JsonObject], gold_labels: dict[str, list[SenseKey]]) -> None:
    if len(gold_labels) != len(items):
        raise ValueError(f"gold key has {len(gold_labels)} rows for {len(items)} items")
    for item in items:
        item_id = str(item["item_id"])
        expected = label_view(item=item).canonical_keys
        actual = gold_labels.get(item_id)
        if actual is None:
            raise ValueError(f"missing gold key line for {item_id}")
        if actual != expected:
            raise ValueError(f"gold key mismatch for {item_id}: expected {expected}, got {actual}")


def verify_sensebench_export(
    *,
    items: list[JsonObject],
    sensebench_rows: list[JsonObject],
    dataset_canary: str,
) -> None:
    if len(sensebench_rows) != len(items):
        raise ValueError(
            f"SenseBench export has {len(sensebench_rows)} rows for {len(items)} items"
        )
    items_by_id = {str(item["item_id"]): item for item in items}
    for row in sensebench_rows:
        metadata = row["metadata"]
        if not isinstance(metadata, dict):
            raise TypeError("SenseBench metadata must be an object")
        if metadata["dataset_canary"] != dataset_canary:
            raise ValueError(f"SenseBench canary mismatch for {row['item_id']}")
        item = items_by_id[str(row["item_id"])]
        expected = label_view(item=item).canonical_keys
        if row["gold_sense_keys"] != expected:
            raise ValueError(f"SenseBench gold mismatch for {row['item_id']}")


def verify_removed_export(
    *,
    path: Path,
    items: list[JsonObject],
    reviews: list[JsonObject],
    dataset_canary: str,
) -> list[JsonObject]:
    removed = read_json_object(path=path)
    if removed["dataset_canary"] != dataset_canary:
        raise ValueError(f"removed export canary mismatch for {path}")
    if removed["schema_version"] != REMOVED_SCHEMA_VERSION:
        raise ValueError(f"removed export schema mismatch for {path}")
    exported_items = removed["items"]
    if not isinstance(exported_items, list):
        raise TypeError("removed items must be a list")
    canonical_ids = {str(item["item_id"]) for item in items}
    review_ids = {str(review["item_id"]) for review in reviews}
    removed_ids: set[str] = set()
    for item in exported_items:
        item_id = str(item["item_id"])
        if item_id in removed_ids:
            raise ValueError(f"duplicate removed item id {item_id}")
        removed_ids.add(item_id)
        if item_id in canonical_ids:
            raise ValueError(f"removed item also appears in canonical items: {item_id}")
        if item_id not in review_ids:
            raise ValueError(f"removed item missing review row: {item_id}")
        if item["dataset_canary"] != dataset_canary:
            raise ValueError(f"removed item canary mismatch for {item_id}")
        labels = label_view(item=item)
        if not labels.canonical_is_empty or len(labels.canonical_keys) != 0:
            raise ValueError(f"removed item has non-empty lexEN label: {item_id}")
        if len(labels.maru_keys) == 0 or len(labels.raganato_original_keys) == 0:
            raise ValueError(f"removed item missing source labels: {item_id}")
        annotators = item["annotators"]
        if not isinstance(annotators, dict):
            raise TypeError(f"removed item annotators must be an object: {item_id}")
        if set(annotators) != {RF_ANNOTATOR_ID, PW_ANNOTATOR_ID, PH_ANNOTATOR_ID}:
            raise ValueError(f"removed item has non-canonical annotators: {item_id}")
        verify_glite_layer(item=item, labels=labels, reviewed=True)
        removal = item["removal"]
        if not isinstance(removal, dict):
            raise TypeError("removed item removal field must be an object")
        decision = str(removal["decision"])
        if decision not in {DECISION_TWO_OF_THREE_CANNOT_ANSWER, DECISION_THREE_WAY_NO_CONSENSUS}:
            raise ValueError(f"unexpected removed decision for {item_id}: {decision}")
    return exported_items


def removed_counts(*, removed_items: list[JsonObject]) -> dict[str, int]:
    counts: Counter[str] = Counter()
    for item in removed_items:
        removal = item["removal"]
        if not isinstance(removal, dict):
            raise TypeError("removed item removal field must be an object")
        counts[f"decision.{removal['decision']}"] += 1
    return dict(sorted(counts.items()))


def verify_xml_canary(*, path: Path, dataset_canary: str) -> None:
    expected_line = f"{XML_CANARY_PREFIX}{dataset_canary}{XML_CANARY_SUFFIX}"
    first_lines = path.read_text(encoding="utf-8").splitlines()[:5]
    if expected_line not in [line.strip() for line in first_lines]:
        raise ValueError(f"Raganato XML canary missing from first lines of {path}")


def xml_instance_ids(*, path: Path) -> set[str]:
    root = ET.parse(path).getroot()
    ids: set[str] = set()
    for element in root.iter("instance"):
        item_id = element.attrib.get("id")
        if item_id is None:
            raise ValueError(f"XML instance without id in {path}")
        if item_id in ids:
            raise ValueError(f"duplicate XML instance id {item_id}")
        ids.add(item_id)
    return ids


def verify_xml_export(
    *,
    path: Path,
    items: list[JsonObject],
    removed_items: list[JsonObject],
) -> None:
    instance_ids = xml_instance_ids(path=path)
    expected_ids = {str(item["item_id"]) for item in items}
    removed_ids = {str(item["item_id"]) for item in removed_items}
    if instance_ids != expected_ids:
        missing = sorted(expected_ids - instance_ids)
        extra = sorted(instance_ids - expected_ids)
        raise ValueError(
            "Raganato XML ids differ from canonical items: "
            f"missing={missing[:5]}, extra={extra[:5]}"
        )
    leaked_removed = instance_ids & removed_ids
    if len(leaked_removed) > 0:
        sample = ", ".join(sorted(leaked_removed)[:5])
        raise ValueError(f"removed ids still present as XML instances: {sample}")


def verify_original_maru_xml_has_no_release_canary(*, repo_root: Path) -> None:
    source_xml = repo_root / MARU_SOURCE_DIR / MARU_XML_FILENAME
    text = source_xml.read_text(encoding="utf-8")
    if DATASET_CANARY in text:
        raise ValueError(f"source Maru XML unexpectedly contains release canary: {source_xml}")


def verify_release(
    *,
    repo_root: Path = DEFAULT_REPO_ROOT,
    release_id: str = ACTIVE_RELEASE_ID,
) -> JsonObject:
    if release_id not in SUPPORTED_RELEASE_IDS:
        known = ", ".join(sorted(SUPPORTED_RELEASE_IDS))
        raise ValueError(f"unsupported release {release_id}; known releases: {known}")
    repo_root = repo_root.resolve()
    release_dir = repo_root / DATA_DIRNAME / release_id
    raganato_dir = repo_root / EXPORTS_DIRNAME / RAGANATO_EXPORT_DIRNAME / release_id
    sensebench_dir = repo_root / EXPORTS_DIRNAME / SENSEBENCH_EXPORT_DIRNAME / release_id

    dataset = read_json_object(path=release_dir / DATASET_METADATA_FILENAME)
    dataset_canary = dataset_canary_value(dataset=dataset)
    items = read_jsonl_objects(path=release_dir / CANONICAL_ITEMS_FILENAME)
    reviews = read_jsonl_objects(path=release_dir / REVIEWS_FILENAME)
    sensebench_rows = read_jsonl_objects(path=sensebench_dir / CANONICAL_ITEMS_FILENAME)
    gold_labels = read_gold_key(path=raganato_dir / f"{release_id}{GOLD_KEY_SUFFIX}")
    removed_items = verify_removed_export(
        path=raganato_dir / f"{release_id}{REMOVED_SUFFIX}",
        items=items,
        reviews=reviews,
        dataset_canary=dataset_canary,
    )

    require_unique_item_ids(rows=items, path=release_dir / CANONICAL_ITEMS_FILENAME)
    require_unique_item_ids(rows=reviews, path=release_dir / REVIEWS_FILENAME)
    computed_counts = verify_items(
        release_id=release_id,
        items=items,
        reviews=reviews,
        removed_items=removed_items,
        dataset_canary=dataset_canary,
    )
    computed_counts.update(removed_counts(removed_items=removed_items))
    if release_id == ACTIVE_RELEASE_ID:
        verify_active_expected_counts(counts=computed_counts)
        verify_artifact_hashes(
            artifacts=dataset["source_artifacts"],
            repo_root=repo_root,
            label="source_artifacts",
        )
        verify_source_manifest(repo_root=repo_root)
        verify_artifact_hashes(
            artifacts=dataset["report_artifacts"],
            repo_root=repo_root,
            label="report_artifacts",
        )
        verify_original_maru_xml_has_no_release_canary(repo_root=repo_root)
    verify_artifact_hashes(
        artifacts=dataset["output_artifacts"],
        repo_root=repo_root,
        label="output_artifacts",
    )
    verify_metadata_counts(dataset=dataset, computed_counts=computed_counts)
    verify_gold_export(items=items, gold_labels=gold_labels)
    verify_sensebench_export(
        items=items,
        sensebench_rows=sensebench_rows,
        dataset_canary=dataset_canary,
    )
    verify_xml_canary(path=raganato_dir / f"{release_id}.data.xml", dataset_canary=dataset_canary)
    verify_xml_export(
        path=raganato_dir / f"{release_id}.data.xml",
        items=items,
        removed_items=removed_items,
    )
    return {
        "counts": computed_counts,
        "release_id": release_id,
        "status": "ok",
    }


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--release", default=ACTIVE_RELEASE_ID, help="Release id to verify.")
    parser.add_argument(
        "--repo-root",
        type=Path,
        default=DEFAULT_REPO_ROOT,
        help="Path to the lexEN repository root.",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    report = verify_release(repo_root=args.repo_root, release_id=str(args.release))
    print(json.dumps(report, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
