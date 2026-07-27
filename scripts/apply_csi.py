#!/usr/bin/env python3
"""Build the CSI coarse-sense sidecar for the frozen lexen-v1 release.

Add-on resource: this does NOT modify data/lexen-v1/items.jsonl. It emits
data/lexen-v1/csi_layer.jsonl, one line per item `{ "item_id", "csi": {...} }`,
where the `csi` block mirrors the in-record `glite` block exactly (same shape),
computed from sources/csi-coarsening. Consumers join on item_id.

Self-contained (stdlib only). As a fidelity guarantee it also rebuilds the GLITE
block from the Glite map and asserts it reproduces each item's existing `glite`
block byte-for-value — proving the builder is structurally identical to the
release-time coarsener before trusting the CSI output.
"""

import json
import sys
from pathlib import Path
from typing import Any

# JSON record (same alias the package uses in src/lexen/models.py); kept local so this
# build script stays stdlib-only.
type JsonObject = dict[str, Any]

REPO: Path = Path(__file__).resolve().parents[1]
ITEMS: Path = REPO / "data/lexen-v1/items.jsonl"
# CSI is an add-on over the FROZEN lexen-v1; it lives outside the pinned release
# surface (data/lexen-v1/ + sources/manifest.json are verified by lexen-verify-release).
SIDECAR: Path = REPO / "coarsenings/csi/csi_layer.jsonl"

CSI_DIR: Path = REPO / "coarsenings/csi/files"
GLITE_DIR: Path = REPO / "sources/glite-coarsening/files"
UNMAPPED_PREFIX: str = "unmapped:"
ANNOTATORS: tuple[str, ...] = ("PH", "PW", "RF")


def load_mapping(*, map_path: Path, alias_path: Path) -> dict[str, str]:
    mapping: dict[str, str] = {}
    with map_path.open(encoding="utf-8") as fh:
        for raw_line in fh:
            line = raw_line.strip()
            if len(line) > 0:
                row = json.loads(line)
                mapping[row["sense_key"]] = row["concept_id"]
    if alias_path.exists():
        for alias in json.loads(alias_path.read_text(encoding="utf-8"))["aliases"]:
            mapping[alias["source_sense_key"]] = alias["concept_id"]
    return mapping


def concept_for(key: str, mapping: dict[str, str]) -> str:
    return mapping.get(key, f"{UNMAPPED_PREFIX}{key}")


def label(keys: list[str], mapping: dict[str, str]) -> dict[str, list[str]]:
    return {
        "concept_ids": sorted({concept_for(k, mapping) for k in keys}),
        "unmapped_sense_keys": sorted(k for k in set(keys) if k not in mapping),
    }


def cand_mappings(keys: list[str], mapping: dict[str, str]) -> list[dict[str, str | bool]]:
    return [
        {"concept_id": concept_for(k, mapping), "mapped": k in mapping, "sense_key": k}
        for k in sorted(set(keys))
    ]


def record(
    *, item: JsonObject, mapping: dict[str, str], mapping_id: str, schema_version: str
) -> JsonObject:
    rows = cand_mappings(item["candidate_sense_keys"], mapping)
    review = item.get("review")
    review_annotators = review.get("annotators") if isinstance(review, dict) else None
    reviewers = None
    if isinstance(review_annotators, dict):
        reviewers = {
            annotator: label(
                [str(k) for k in review_annotators[annotator]["chosen_sense_keys"]], mapping
            )
            for annotator in ANNOTATORS
        }
    labels = item["labels"]
    return {
        "candidate_concept_ids": sorted({r["concept_id"] for r in rows}),
        "candidate_sense_mappings": rows,
        "labels": {
            "lexen_gold": label(labels["lexen_gold"]["sense_keys"], mapping),
            "maru2022": label(labels["maru2022"]["sense_keys"], mapping),
            "raganato_original": label(labels["raganato_original"]["sense_keys"], mapping),
        },
        "mapping_id": mapping_id,
        "reviewers": reviewers,
        "schema_version": schema_version,
        "unmapped_prefix": UNMAPPED_PREFIX,
    }


def main() -> None:
    with ITEMS.open(encoding="utf-8") as fh:
        items = [json.loads(line) for line in fh]
    assert len(items) > 0, "items.jsonl contains at least one item"
    glite = load_mapping(
        map_path=GLITE_DIR / "wordnet_sense_key_to_glite_concept.jsonl",
        alias_path=GLITE_DIR / "lexen_report_aliases.json",
    )
    csi = load_mapping(
        map_path=CSI_DIR / "wordnet_sense_key_to_csi_concept.jsonl",
        alias_path=CSI_DIR / "csi_report_aliases.json",
    )

    # fidelity regression: our builder must reproduce the existing glite block exactly
    mismatches = 0
    for item in items:
        rebuilt = record(
            item=item,
            mapping=glite,
            mapping_id="glite-coarsening-maru2022-subset",
            schema_version="lexen.glite.v1",
        )
        if rebuilt != item["glite"]:
            mismatches += 1
            if mismatches <= 3:
                print(f"  glite mismatch on {item['item_id']}", file=sys.stderr)
    assert mismatches == 0, "builder reproduces every glite block exactly"
    print(f"fidelity OK: glite block reproduced for all {len(items)} items")

    n_unmapped = 0
    with SIDECAR.open("w", encoding="utf-8") as fh:
        for item in items:
            block = record(
                item=item,
                mapping=csi,
                mapping_id="csi-coarsening-maru2022-subset",
                schema_version="lexen.csi.v1",
            )
            if any(not r["mapped"] for r in block["candidate_sense_mappings"]):
                n_unmapped += 1
            fh.write(json.dumps({"item_id": item["item_id"], "csi": block}) + "\n")
    print(
        f"wrote {SIDECAR} ({len(items)} items; "
        f"{n_unmapped} items have >=1 unmapped candidate under CSI)"
    )


if __name__ == "__main__":
    main()
