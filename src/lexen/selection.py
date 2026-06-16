"""Build and verify the suspicious-item selection source package."""

from __future__ import annotations

import argparse
import gzip
import json
import re
import xml.etree.ElementTree as ET
from collections import Counter
from pathlib import Path
from typing import Any

from lexen.io import read_gzip_jsonl_text, read_json_object, sha256_file
from lexen.models import JsonObject, SenseKey
from lexen.paths import (
    DEFAULT_REPO_ROOT,
    EXPECTED_REVIEWED_AUDIT_ITEMS,
    EXPECTED_SOURCE_ITEMS,
    MARU_GOLD_FILENAME,
    MARU_SOURCE_DIR,
    MARU_XML_FILENAME,
    MODEL_PANEL_SOURCE_DIR,
    SELECTION_JSONL_GZ_FILENAME,
    SELECTION_SCHEMA_FILENAME,
    SELECTION_SOURCE_DIR,
    WATERFALL_SUMMARY_FILENAME,
)

GPT55_MODEL_LABELS: tuple[str, ...] = (
    "gpt55_t0152_p01",
    "gpt55_t0152_p02",
    "gpt55_t0152_p03",
    "gpt55_t0156_e69",
    "gpt55_t0158_headerfooter",
    "gpt55_t0173_v01",
    "gpt55_t0173_v03",
    "gpt55_t0173_v06",
)
SUPERVISED_MODEL_LABELS: tuple[str, ...] = ("sandwich", "catboost")
ALL_MODEL_LABELS: tuple[str, ...] = (*GPT55_MODEL_LABELS, *SUPERVISED_MODEL_LABELS)
N_MODELS_TOTAL: int = len(ALL_MODEL_LABELS)
_SENSE_KEY_RE: re.Pattern[str] = re.compile(r"sense_key=([^\s|]+)")


def read_gold_key(*, path: Path) -> dict[str, list[SenseKey]]:
    labels: dict[str, list[SenseKey]] = {}
    with path.open(encoding="utf-8") as handle:
        for line_number, raw_line in enumerate(handle, start=1):
            line = raw_line.strip()
            if len(line) == 0:
                continue
            parts = line.split()
            if len(parts) < 2:
                raise ValueError(f"gold key line has no sense key at {path}:{line_number}")
            if parts[0] in labels:
                raise ValueError(f"duplicate gold-key id {parts[0]} in {path}")
            labels[parts[0]] = parts[1:]
    return labels


def load_xml_instance_metadata(*, path: Path) -> dict[str, JsonObject]:
    """Load item metadata from a Raganato-format XML file."""
    root = ET.parse(path).getroot()
    metadata: dict[str, JsonObject] = {}
    for text_element in root.iter("text"):
        document_id = str(text_element.attrib["id"])
        for sentence_element in text_element.iter("sentence"):
            sentence_id = str(sentence_element.attrib["id"])
            for child in sentence_element:
                if child.tag != "instance":
                    continue
                item_id = str(child.attrib["id"])
                if item_id in metadata:
                    raise ValueError(f"duplicate XML instance id {item_id} in {path}")
                metadata[item_id] = {
                    "dataset": item_id.split(".")[0],
                    "document_id": document_id,
                    "lemma": str(child.attrib["lemma"]),
                    "pos": str(child.attrib["pos"]),
                    "sentence_id": sentence_id,
                    "surface": child.text or "",
                }
    return metadata


def open_jsonl_text(*, path: Path) -> Any:
    if path.suffix == ".gz":
        return gzip.open(path, mode="rt", encoding="utf-8")
    return path.open(encoding="utf-8")


def load_jsonl_predictions(*, path: Path) -> dict[str, SenseKey | None]:
    predictions: dict[str, SenseKey | None] = {}
    with open_jsonl_text(path=path) as handle:
        for raw_line in handle:
            row = json.loads(raw_line)
            if not isinstance(row, dict):
                raise TypeError(f"prediction row must be an object in {path}")
            item_id = str(row["instance_id"])
            provider_status = row.get("provider_status")
            if provider_status is not None and provider_status != "success":
                predictions[item_id] = None
            else:
                predicted = row.get("predicted_sense_key")
                predictions[item_id] = None if predicted is None else str(predicted)
    return predictions


def load_key_predictions(*, path: Path) -> dict[str, SenseKey | None]:
    predictions: dict[str, SenseKey | None] = {}
    with path.open(encoding="utf-8") as handle:
        for line_number, raw_line in enumerate(handle, start=1):
            line = raw_line.strip()
            if len(line) == 0:
                continue
            parts = line.split()
            if len(parts) < 2:
                raise ValueError(f"prediction line has no sense key at {path}:{line_number}")
            predictions[parts[0]] = parts[1]
    return predictions


def load_v03_candidates(*, path: Path) -> dict[str, list[SenseKey]]:
    candidates: dict[str, list[SenseKey]] = {}
    with open_jsonl_text(path=path) as handle:
        for raw_line in handle:
            row = json.loads(raw_line)
            if not isinstance(row, dict):
                raise TypeError(f"prediction row must be an object in {path}")
            candidates[str(row["instance_id"])] = _SENSE_KEY_RE.findall(
                str(row.get("prompt_text", ""))
            )
    return candidates


def load_all_model_predictions(*, repo_root: Path) -> dict[str, dict[str, SenseKey | None]]:
    source_dir = repo_root / MODEL_PANEL_SOURCE_DIR
    predictions: dict[str, dict[str, SenseKey | None]] = {
        "gpt55_t0152_p01": load_jsonl_predictions(
            path=source_dir / "gpt55_t0152_p01" / "predictions.jsonl.gz"
        ),
        "gpt55_t0152_p02": load_jsonl_predictions(
            path=source_dir / "gpt55_t0152_p02" / "predictions.jsonl.gz"
        ),
        "gpt55_t0152_p03": load_jsonl_predictions(
            path=source_dir / "gpt55_t0152_p03" / "predictions.jsonl.gz"
        ),
        "gpt55_t0156_e69": load_jsonl_predictions(
            path=source_dir / "gpt55_t0156_e69" / "predictions.jsonl.gz"
        ),
        "gpt55_t0158_headerfooter": load_jsonl_predictions(
            path=source_dir / "gpt55_t0158_headerfooter" / "predictions.jsonl.gz"
        ),
        "gpt55_t0173_v01": load_jsonl_predictions(
            path=source_dir / "gpt55_t0173_v01" / "predictions.jsonl.gz"
        ),
        "gpt55_t0173_v03": load_jsonl_predictions(
            path=source_dir / "gpt55_t0173_v03" / "predictions.jsonl.gz"
        ),
        "gpt55_t0173_v06": load_jsonl_predictions(
            path=source_dir / "gpt55_t0173_v06" / "predictions.jsonl.gz"
        ),
        "sandwich": load_key_predictions(path=source_dir / "sandwich" / "ALL.key.txt"),
        "catboost": load_jsonl_predictions(
            path=source_dir / "catboost" / "predictions-raganato-all.jsonl"
        ),
    }
    return predictions


def compute_modal(*, model_predictions: dict[str, SenseKey | None]) -> tuple[SenseKey | None, int]:
    votes: Counter[SenseKey] = Counter()
    for prediction in model_predictions.values():
        if prediction is not None:
            votes[prediction] += 1
    if len(votes) == 0:
        return None, 0
    max_count = max(votes.values())
    tied = sorted(key for key, count in votes.items() if count == max_count)
    return tied[0], max_count


def classify_waterfall(
    *,
    gpt55_predictions: list[SenseKey | None],
    sandwich_prediction: SenseKey | None,
    catboost_prediction: SenseKey | None,
    gold_keys: set[SenseKey],
) -> str | None:
    non_null_gpt = [prediction for prediction in gpt55_predictions if prediction is not None]
    if len(non_null_gpt) == 0:
        return None

    gpt_counter: Counter[SenseKey] = Counter(non_null_gpt)
    max_gpt_count = max(gpt_counter.values())
    n_gpt = len(non_null_gpt)
    modal_gpt = sorted(key for key, count in gpt_counter.items() if count == max_gpt_count)[0]
    modal_gpt_correct = modal_gpt in gold_keys

    if (
        n_gpt == 8
        and max_gpt_count == 8
        and not modal_gpt_correct
        and sandwich_prediction == modal_gpt
        and catboost_prediction == modal_gpt
    ):
        return "S1"
    if (
        n_gpt == 8
        and max_gpt_count == 8
        and not modal_gpt_correct
        and not (sandwich_prediction == modal_gpt and catboost_prediction == modal_gpt)
    ):
        return "S2"
    if (
        n_gpt == 8
        and max_gpt_count < 8
        and all(prediction not in gold_keys for prediction in non_null_gpt)
    ):
        return "S3"
    if n_gpt == 8 and max_gpt_count == 7 and not modal_gpt_correct:
        return "S4"
    if n_gpt == 8 and max_gpt_count == 6 and not modal_gpt_correct:
        return "S5"
    wrong_count = sum(1 for prediction in non_null_gpt if prediction not in gold_keys)
    if n_gpt == 8 and wrong_count >= 6 and max_gpt_count < 6:
        return "S6"
    return None


def build_suspicion_rationale(
    *,
    suspicion_set: str | None,
    modal_key: SenseKey | None,
    n_models_total: int,
    gold_keys: set[SenseKey],
    gpt55_predictions: list[SenseKey | None],
) -> str:
    if suspicion_set is None:
        return ""

    n_gpt_non_null = sum(1 for prediction in gpt55_predictions if prediction is not None)
    n_gpt_agreeing = sum(
        1 for prediction in gpt55_predictions if prediction is not None and prediction == modal_key
    )
    gold_repr = ", ".join(f"`{key}`" for key in sorted(gold_keys))
    modal_repr = f"`{modal_key}`" if modal_key is not None else "unknown"

    if suspicion_set == "S1":
        return (
            f"{n_models_total}/{n_models_total} models (all gpt-5.5 + supervised) agree on "
            f"{modal_repr} but gold is {gold_repr}"
        )
    if suspicion_set == "S2":
        return (
            f"{n_gpt_non_null}/{n_gpt_non_null} gpt-5.5 agree on {modal_repr} "
            f"but gold is {gold_repr}; supervised systems differ or missing"
        )
    if suspicion_set == "S3":
        return (
            f"All {n_gpt_non_null} gpt-5.5 predict wrong senses but disagree; gold is {gold_repr}"
        )
    if suspicion_set in {"S4", "S5"}:
        return f"{n_gpt_agreeing}/8 gpt-5.5 agree on {modal_repr} but gold is {gold_repr}"
    if suspicion_set == "S6":
        wrong_count = sum(
            1
            for prediction in gpt55_predictions
            if prediction is not None and prediction not in gold_keys
        )
        return (
            f"{wrong_count}/8 gpt-5.5 predict wrong senses but no single wrong sense "
            f"has >=6 agreements; gold is {gold_repr}"
        )
    raise ValueError(f"unknown suspicion set: {suspicion_set}")


def recompute_record_fields(
    *,
    item_id: str,
    gold_keys: list[SenseKey],
    predictions: dict[str, dict[str, SenseKey | None]],
) -> JsonObject:
    gold_key_set = set(gold_keys)
    all_predictions = {label: predictions[label].get(item_id) for label in ALL_MODEL_LABELS}
    modal_key, modal_count = compute_modal(model_predictions=all_predictions)
    non_null_predictions = [
        prediction for prediction in all_predictions.values() if prediction is not None
    ]
    model_predictions: dict[str, JsonObject] = {}
    for label in ALL_MODEL_LABELS:
        prediction = all_predictions[label]
        is_correct = prediction in gold_key_set if prediction is not None else None
        model_predictions[label] = {
            "agrees_with_gold": is_correct,
            "agrees_with_modal": prediction == modal_key if prediction is not None else None,
            "is_correct": is_correct,
            "predicted_sense_key": prediction,
        }
    gpt55_predictions = [all_predictions[label] for label in GPT55_MODEL_LABELS]
    suspicion_set = classify_waterfall(
        gpt55_predictions=gpt55_predictions,
        sandwich_prediction=all_predictions["sandwich"],
        catboost_prediction=all_predictions["catboost"],
        gold_keys=gold_key_set,
    )
    return {
        "gold_sense_id": gold_keys[0] if len(gold_keys) > 0 else None,
        "gold_sense_keys": gold_keys,
        "modal_count": modal_count,
        "modal_predicted_sense_id": modal_key,
        "model_predictions": model_predictions,
        "n_correct": sum(
            1 for prediction in all_predictions.values() if prediction in gold_key_set
        ),
        "n_distinct_predictions": len(set(non_null_predictions)),
        "n_models_total": N_MODELS_TOTAL,
        "suspicion_rationale": build_suspicion_rationale(
            suspicion_set=suspicion_set,
            modal_key=modal_key,
            n_models_total=N_MODELS_TOTAL,
            gold_keys=gold_key_set,
            gpt55_predictions=gpt55_predictions,
        ),
        "suspicion_set": suspicion_set,
        "top_prediction_share": round(modal_count / N_MODELS_TOTAL, 4) if modal_count > 0 else 0.0,
    }


def merge_recomputed_fields(*, record: JsonObject, recomputed: JsonObject) -> JsonObject:
    updated = dict(record)
    existing_model_predictions = record["model_predictions"]
    if not isinstance(existing_model_predictions, dict):
        raise TypeError("model_predictions must be an object")
    merged_predictions: dict[str, JsonObject] = {}
    for label in ALL_MODEL_LABELS:
        old_entry = existing_model_predictions.get(label, {})
        if not isinstance(old_entry, dict):
            raise TypeError(f"model prediction entry must be an object: {label}")
        new_entry = dict(recomputed["model_predictions"][label])
        if "justifications" in old_entry:
            new_entry["justifications"] = old_entry["justifications"]
        else:
            new_entry["justifications"] = None
        if "coverage" in old_entry:
            new_entry["coverage"] = old_entry["coverage"]
        merged_predictions[label] = new_entry
    for key, value in recomputed.items():
        updated[key] = value
    updated["model_predictions"] = merged_predictions
    return updated


def build_waterfall_summary(*, records: list[JsonObject]) -> JsonObject:
    suspicion_counts: Counter[str] = Counter()
    coverage: dict[str, int] = dict.fromkeys(ALL_MODEL_LABELS, 0)
    for record in records:
        suspicion_set = record["suspicion_set"]
        if suspicion_set is not None:
            suspicion_counts[str(suspicion_set)] += 1
        model_predictions = record["model_predictions"]
        if not isinstance(model_predictions, dict):
            raise TypeError("model_predictions must be an object")
        for label in ALL_MODEL_LABELS:
            entry = model_predictions[label]
            if not isinstance(entry, dict):
                raise TypeError(f"model prediction entry must be an object: {label}")
            if entry["predicted_sense_key"] is not None:
                coverage[label] += 1
    suspicious_total = sum(suspicion_counts.values())
    return {
        "model_coverage": coverage,
        "model_labels": list(ALL_MODEL_LABELS),
        "n_models_total": N_MODELS_TOTAL,
        "not_suspicious": len(records) - suspicious_total,
        "source_hashes": {},
        "suspicion_counts": dict(sorted(suspicion_counts.items())),
        "suspicious_total": suspicious_total,
        "total_records": len(records),
    }


def source_hashes(*, repo_root: Path) -> dict[str, str]:
    paths = [
        repo_root / MARU_SOURCE_DIR / MARU_XML_FILENAME,
        repo_root / MARU_SOURCE_DIR / MARU_GOLD_FILENAME,
    ]
    source_dir = repo_root / MODEL_PANEL_SOURCE_DIR
    for label in GPT55_MODEL_LABELS:
        paths.append(source_dir / label / "predictions.jsonl.gz")
    paths.extend(
        [
            source_dir / "sandwich" / "ALL.key.txt",
            source_dir / "catboost" / "predictions-raganato-all.jsonl",
        ]
    )
    return {str(path.relative_to(repo_root)): sha256_file(path=path) for path in paths}


def build_selection_records(*, repo_root: Path) -> tuple[list[JsonObject], JsonObject]:
    selection_path = repo_root / SELECTION_SOURCE_DIR / SELECTION_JSONL_GZ_FILENAME
    records = [json.loads(line) for line in read_gzip_jsonl_text(path=selection_path)]
    gold = read_gold_key(path=repo_root / MARU_SOURCE_DIR / MARU_GOLD_FILENAME)
    xml_metadata = load_xml_instance_metadata(path=repo_root / MARU_SOURCE_DIR / MARU_XML_FILENAME)
    predictions = load_all_model_predictions(repo_root=repo_root)
    v03_candidates = load_v03_candidates(
        path=repo_root / MODEL_PANEL_SOURCE_DIR / "gpt55_t0173_v03" / "predictions.jsonl.gz"
    )

    if len(records) != EXPECTED_SOURCE_ITEMS:
        raise ValueError(f"selection has {len(records)} rows, expected {EXPECTED_SOURCE_ITEMS}")
    record_ids = [str(record["instance_id"]) for record in records]
    if len(set(record_ids)) != len(record_ids):
        raise ValueError("selection records contain duplicate instance ids")
    if set(record_ids) != set(gold):
        raise ValueError("selection record ids differ from Maru2022 gold-key ids")
    if set(record_ids) != set(xml_metadata):
        raise ValueError("selection record ids differ from Maru2022 XML instance ids")

    rebuilt_records: list[JsonObject] = []
    for record in records:
        item_id = str(record["instance_id"])
        metadata = xml_metadata[item_id]
        if record["lemma"] != metadata["lemma"] or record["pos"] != metadata["pos"]:
            raise ValueError(f"selection lemma/POS differ from XML for {item_id}")
        if record["dataset"] != metadata["dataset"]:
            raise ValueError(f"selection dataset differs from XML for {item_id}")
        if record["candidates_in_maru_prompt"] != v03_candidates.get(item_id, []):
            raise ValueError(f"selection candidate list differs from V03 prompt for {item_id}")
        recomputed = recompute_record_fields(
            item_id=item_id,
            gold_keys=gold[item_id],
            predictions=predictions,
        )
        rebuilt_records.append(merge_recomputed_fields(record=record, recomputed=recomputed))

    summary = build_waterfall_summary(records=rebuilt_records)
    summary["source_hashes"] = source_hashes(repo_root=repo_root)
    if summary["suspicious_total"] != EXPECTED_REVIEWED_AUDIT_ITEMS:
        raise ValueError(
            f"selection has {summary['suspicious_total']} suspicious rows, "
            f"expected {EXPECTED_REVIEWED_AUDIT_ITEMS}"
        )
    return rebuilt_records, summary


def compare_selection(
    *,
    current_records: list[JsonObject],
    rebuilt_records: list[JsonObject],
) -> None:
    for index, (current, rebuilt) in enumerate(
        zip(current_records, rebuilt_records, strict=True),
        start=1,
    ):
        current_id = str(current["instance_id"])
        rebuilt_id = str(rebuilt["instance_id"])
        if current_id != rebuilt_id:
            raise ValueError(f"record order mismatch at row {index}: {current_id} != {rebuilt_id}")
        keys_to_compare = [
            "gold_sense_id",
            "gold_sense_keys",
            "modal_count",
            "modal_predicted_sense_id",
            "n_correct",
            "n_distinct_predictions",
            "n_models_total",
            "suspicion_rationale",
            "suspicion_set",
            "top_prediction_share",
        ]
        for key in keys_to_compare:
            if current[key] != rebuilt[key]:
                raise ValueError(
                    f"selection field mismatch for {current_id}.{key}: "
                    f"{current[key]!r} != {rebuilt[key]!r}"
                )
        current_predictions = current["model_predictions"]
        rebuilt_predictions = rebuilt["model_predictions"]
        if not isinstance(current_predictions, dict) or not isinstance(rebuilt_predictions, dict):
            raise TypeError("model_predictions must be objects")
        for label in ALL_MODEL_LABELS:
            for key in [
                "agrees_with_gold",
                "agrees_with_modal",
                "is_correct",
                "predicted_sense_key",
            ]:
                if current_predictions[label][key] != rebuilt_predictions[label][key]:
                    current_value = current_predictions[label][key]
                    rebuilt_value = rebuilt_predictions[label][key]
                    raise ValueError(
                        f"selection prediction mismatch for {current_id}.{label}.{key}: "
                        f"{current_value!r} != {rebuilt_value!r}"
                    )


def write_jsonl_gz(*, path: Path, records: list[JsonObject]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with (
        path.open("wb") as raw_handle,
        gzip.GzipFile(
            fileobj=raw_handle,
            mode="wb",
            mtime=0,
        ) as gzip_handle,
    ):
        for record in records:
            line = json.dumps(record, ensure_ascii=False, sort_keys=True) + "\n"
            gzip_handle.write(line.encode("utf-8"))


def write_json_object(*, path: Path, data: JsonObject) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        json.dumps(data, ensure_ascii=False, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )


def verify_selection(*, repo_root: Path = DEFAULT_REPO_ROOT) -> JsonObject:
    rebuilt_records, rebuilt_summary = build_selection_records(repo_root=repo_root)
    current_records = [
        json.loads(line)
        for line in read_gzip_jsonl_text(
            path=repo_root / SELECTION_SOURCE_DIR / SELECTION_JSONL_GZ_FILENAME
        )
    ]
    compare_selection(current_records=current_records, rebuilt_records=rebuilt_records)
    current_summary = read_json_object(
        path=repo_root / SELECTION_SOURCE_DIR / WATERFALL_SUMMARY_FILENAME
    )
    current_suspicion_counts = current_summary.get(
        "suspicion_counts",
        current_summary.get("waterfall_counts"),
    )
    if current_suspicion_counts != rebuilt_summary["suspicion_counts"]:
        raise ValueError(
            "selection summary mismatch for suspicion counts: "
            f"{current_suspicion_counts!r} != {rebuilt_summary['suspicion_counts']!r}"
        )
    for key in ["suspicious_total", "total_records"]:
        if current_summary.get(key) != rebuilt_summary[key]:
            raise ValueError(
                f"selection summary mismatch for {key}: "
                f"{current_summary.get(key)!r} != {rebuilt_summary[key]!r}"
            )
    return {
        "selection_rows": len(rebuilt_records),
        "status": "ok",
        "suspicion_counts": rebuilt_summary["suspicion_counts"],
        "suspicious_total": rebuilt_summary["suspicious_total"],
    }


def build_selection_source(
    *,
    repo_root: Path = DEFAULT_REPO_ROOT,
    verify: bool = False,
) -> JsonObject:
    if verify:
        return verify_selection(repo_root=repo_root)

    records, summary = build_selection_records(repo_root=repo_root)
    selection_dir = repo_root / SELECTION_SOURCE_DIR
    write_jsonl_gz(path=selection_dir / SELECTION_JSONL_GZ_FILENAME, records=records)
    write_json_object(path=selection_dir / WATERFALL_SUMMARY_FILENAME, data=summary)
    schema_path = selection_dir / SELECTION_SCHEMA_FILENAME
    if not schema_path.exists():
        write_json_object(
            path=schema_path,
            data={
                "$schema": "http://json-schema.org/draft-07/schema#",
                "description": "Generated lexEN selection source package.",
                "type": "object",
            },
        )
    return {
        "selection_rows": len(records),
        "status": "written",
        "suspicion_counts": summary["suspicion_counts"],
        "suspicious_total": summary["suspicious_total"],
    }


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--repo-root",
        type=Path,
        default=DEFAULT_REPO_ROOT,
        help="Path to the lexEN repository root.",
    )
    parser.add_argument(
        "--verify",
        action="store_true",
        help="Verify the committed selection package instead of rewriting it.",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    report = build_selection_source(repo_root=args.repo_root.resolve(), verify=bool(args.verify))
    print(json.dumps(report, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
