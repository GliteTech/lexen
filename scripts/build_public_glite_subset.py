"""Build the public Glite coarsening subset used by lexEN.

The input full Glite map is a private construction artifact. The public lexEN release only carries
the WordNet sense-key to Glite concept-id rows needed by the Maru2022/lexEN candidate inventories
and reviewed labels.
"""

from __future__ import annotations

import argparse
import gzip
import json
from dataclasses import dataclass
from pathlib import Path
from typing import Any

from lexen.io import read_json_object
from lexen.models import JsonObject, SenseKey
from lexen.paths import (
    DEFAULT_REPO_ROOT,
    GLITE_COARSENING_FILES_DIR,
    GLITE_MAPPING_COVERAGE_FILENAME,
    GLITE_REPORT_ALIASES_FILENAME,
    GLITE_SENSE_TO_CONCEPT_FILENAME,
    PH_REVIEW_SOURCE_DIR,
    PH_VERDICTS_FILENAME,
    PW_REVIEW_SOURCE_DIR,
    PW_VERDICTS_FILENAME,
    RAGANATO_GOLD_FILENAME,
    RAGANATO_SOURCE_DIR,
    RF_REVIEW_SOURCE_DIR,
    RF_VERDICTS_FILENAME,
    SELECTION_JSONL_GZ_FILENAME,
    SELECTION_SOURCE_DIR,
)

GLITE_SUBSET_SCHEMA_VERSION: str = "lexen.glite_public_subset.v1"
WORDNET_POS_BY_SENSE_KIND: dict[str, str] = {
    "1": "n",
    "2": "v",
    "3": "a",
    "4": "r",
    "5": "s",
}


@dataclass(frozen=True, slots=True)
class SubsetResult:
    """Summary of a generated public coarsening subset."""

    mapped_rows: int
    missing_required_sense_keys: list[SenseKey]
    output_path: Path
    required_sense_keys: int
    unique_concept_ids: int

    def to_json_object(self) -> JsonObject:
        return {
            "mapped_rows": self.mapped_rows,
            "missing_required_sense_keys": self.missing_required_sense_keys,
            "output_path": str(self.output_path),
            "required_sense_keys": self.required_sense_keys,
            "unique_concept_ids": self.unique_concept_ids,
        }


def read_jsonl_gz(*, path: Path) -> list[JsonObject]:
    records: list[JsonObject] = []
    with gzip.open(path, mode="rt", encoding="utf-8") as handle:
        for raw_line in handle:
            row = json.loads(raw_line)
            if not isinstance(row, dict):
                raise TypeError(f"expected JSON object row in {path}")
            records.append(row)
    return records


def read_gold_key(*, path: Path) -> dict[str, list[SenseKey]]:
    labels: dict[str, list[SenseKey]] = {}
    with path.open(encoding="utf-8") as handle:
        for raw_line in handle:
            parts = raw_line.strip().split()
            if len(parts) >= 2:
                labels[parts[0]] = parts[1:]
    return labels


def add_sense_keys_from_value(*, value: Any, required_sense_keys: set[SenseKey]) -> None:
    if isinstance(value, str) and "%" in value:
        required_sense_keys.add(value)
        return
    if isinstance(value, list):
        for item in value:
            add_sense_keys_from_value(value=item, required_sense_keys=required_sense_keys)
        return
    if isinstance(value, dict):
        for item in value.values():
            add_sense_keys_from_value(value=item, required_sense_keys=required_sense_keys)


def required_sense_keys_from_sources(*, repo_root: Path) -> set[SenseKey]:
    required_sense_keys: set[SenseKey] = set()
    selection_rows = read_jsonl_gz(
        path=repo_root / SELECTION_SOURCE_DIR / SELECTION_JSONL_GZ_FILENAME
    )
    for row in selection_rows:
        for sense in row.get("all_wordnet_senses", []):
            if isinstance(sense, dict):
                sense_key = sense.get("sense_key")
                if isinstance(sense_key, str):
                    required_sense_keys.add(sense_key)
        add_sense_keys_from_value(
            value=row.get("candidates_in_maru_prompt", []),
            required_sense_keys=required_sense_keys,
        )
        add_sense_keys_from_value(
            value=row.get("gold_sense_keys", []),
            required_sense_keys=required_sense_keys,
        )

    for labels in read_gold_key(
        path=repo_root / RAGANATO_SOURCE_DIR / RAGANATO_GOLD_FILENAME
    ).values():
        required_sense_keys.update(labels)

    review_paths = [
        repo_root / RF_REVIEW_SOURCE_DIR / RF_VERDICTS_FILENAME,
        repo_root / PW_REVIEW_SOURCE_DIR / PW_VERDICTS_FILENAME,
        repo_root / PH_REVIEW_SOURCE_DIR / PH_VERDICTS_FILENAME,
    ]
    for path in review_paths:
        review_file = read_json_object(path=path)
        add_sense_keys_from_value(
            value=review_file.get("verdicts", []),
            required_sense_keys=required_sense_keys,
        )
    return required_sense_keys


def lemma_from_sense_key(*, sense_key: SenseKey) -> str:
    return sense_key.split("%", maxsplit=1)[0]


def wordnet_pos_from_sense_key(*, sense_key: SenseKey) -> str:
    parts = sense_key.split("%", maxsplit=1)
    if len(parts) != 2 or len(parts[1]) == 0:
        return "unknown"
    return WORDNET_POS_BY_SENSE_KIND.get(parts[1][0], "unknown")


def sanitized_mapping_row(*, row: JsonObject) -> JsonObject:
    sense_key = str(row["sense_key"])
    return {
        "concept_id": str(row["concept_id"]),
        "lemma": lemma_from_sense_key(sense_key=sense_key),
        "sense_key": sense_key,
        "wordnet_pos": wordnet_pos_from_sense_key(sense_key=sense_key),
    }


def load_alias_source_keys(*, repo_root: Path) -> set[SenseKey]:
    path = repo_root / GLITE_COARSENING_FILES_DIR / GLITE_REPORT_ALIASES_FILENAME
    if not path.exists():
        return set()
    data = read_json_object(path=path)
    aliases = data.get("aliases", [])
    if not isinstance(aliases, list):
        raise TypeError("aliases must be a list")
    source_keys: set[SenseKey] = set()
    for alias in aliases:
        if not isinstance(alias, dict):
            raise TypeError("alias rows must be objects")
        source_keys.add(str(alias["source_sense_key"]))
    return source_keys


def build_public_glite_subset(
    *,
    full_map_path: Path,
    repo_root: Path = DEFAULT_REPO_ROOT,
    output_path: Path | None = None,
) -> SubsetResult:
    required_sense_keys = required_sense_keys_from_sources(repo_root=repo_root)
    alias_source_keys = load_alias_source_keys(repo_root=repo_root)
    map_required_keys = required_sense_keys - alias_source_keys
    output = (
        repo_root / GLITE_COARSENING_FILES_DIR / GLITE_SENSE_TO_CONCEPT_FILENAME
        if output_path is None
        else output_path
    )
    rows_by_key: dict[SenseKey, JsonObject] = {}
    with full_map_path.open(encoding="utf-8") as handle:
        for raw_line in handle:
            row = json.loads(raw_line)
            if not isinstance(row, dict):
                raise TypeError(f"expected JSON object row in {full_map_path}")
            sense_key = str(row["sense_key"])
            if sense_key in map_required_keys:
                rows_by_key[sense_key] = sanitized_mapping_row(row=row)

    output.parent.mkdir(parents=True, exist_ok=True)
    with output.open("w", encoding="utf-8") as handle:
        for sense_key in sorted(rows_by_key):
            handle.write(json.dumps(rows_by_key[sense_key], ensure_ascii=False, sort_keys=True))
            handle.write("\n")

    mapped_required_keys = set(rows_by_key) | alias_source_keys
    missing_keys = sorted(required_sense_keys - mapped_required_keys)
    concept_ids = {str(row["concept_id"]) for row in rows_by_key.values()}
    coverage = {
        "coverage_scope": (
            "WordNet sense keys referenced by Maru2022/lexEN candidate inventories, source labels, "
            "and lexicographer review labels."
        ),
        "fields_in_public_map": ["concept_id", "lemma", "sense_key", "wordnet_pos"],
        "mapping_file": str(output.relative_to(repo_root)),
        "missing_required_sense_keys": missing_keys,
        "public_subset_schema_version": GLITE_SUBSET_SCHEMA_VERSION,
        "required_sense_keys": len(required_sense_keys),
        "required_sense_keys_mapped_by_alias": len(alias_source_keys & required_sense_keys),
        "required_sense_keys_mapped_in_file": len(rows_by_key),
        "unique_concept_ids_in_public_subset": len(concept_ids),
    }
    coverage_path = repo_root / GLITE_COARSENING_FILES_DIR / GLITE_MAPPING_COVERAGE_FILENAME
    coverage_path.write_text(
        json.dumps(coverage, ensure_ascii=False, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    return SubsetResult(
        mapped_rows=len(rows_by_key),
        missing_required_sense_keys=missing_keys,
        output_path=output,
        required_sense_keys=len(required_sense_keys),
        unique_concept_ids=len(concept_ids),
    )


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--full-map",
        required=True,
        type=Path,
        help="Private full Glite WordNet sense-key to concept-id map.",
    )
    parser.add_argument(
        "--repo-root",
        type=Path,
        default=DEFAULT_REPO_ROOT,
        help="Path to the lexEN repository root.",
    )
    parser.add_argument(
        "--output",
        type=Path,
        default=None,
        help="Optional output path for the public subset JSONL.",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    result = build_public_glite_subset(
        full_map_path=args.full_map.resolve(),
        repo_root=args.repo_root.resolve(),
        output_path=args.output.resolve() if args.output is not None else None,
    )
    print(json.dumps(result.to_json_object(), indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
