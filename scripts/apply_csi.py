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

REPO = Path(__file__).resolve().parents[1]
ITEMS = REPO / "data/lexen-v1/items.jsonl"
# CSI is an add-on over the FROZEN lexen-v1; it lives outside the pinned release
# surface (data/lexen-v1/ + sources/manifest.json are verified by lexen-verify-release).
SIDECAR = REPO / "coarsenings/csi/csi_layer.jsonl"

CSI_DIR = REPO / "coarsenings/csi/files"
GLITE_DIR = REPO / "sources/glite-coarsening/files"
UNMAPPED_PREFIX = "unmapped:"
ANNOTATORS = ("PH", "PW", "RF")


def load_mapping(map_path: Path, alias_path: Path) -> dict[str, str]:
    mapping: dict[str, str] = {}
    with map_path.open(encoding="utf-8") as fh:
        for line in fh:
            line = line.strip()
            if line:
                row = json.loads(line)
                mapping[row["sense_key"]] = row["concept_id"]
    if alias_path.exists():
        for a in json.loads(alias_path.read_text())["aliases"]:
            mapping[a["source_sense_key"]] = a["concept_id"]
    return mapping


def concept_for(key: str, m: dict[str, str]) -> str:
    return m.get(key, f"{UNMAPPED_PREFIX}{key}")


def label(keys: list[str], m: dict[str, str]) -> dict[str, list[str]]:
    return {
        "concept_ids": sorted({concept_for(k, m) for k in keys}),
        "unmapped_sense_keys": sorted(k for k in set(keys) if k not in m),
    }


def cand_mappings(keys: list[str], m: dict[str, str]) -> list[dict[str, str | bool]]:
    return [
        {"concept_id": concept_for(k, m), "mapped": k in m, "sense_key": k}
        for k in sorted(set(keys))
    ]


def record(item: JsonObject, m: dict[str, str], mapping_id: str, schema_version: str) -> JsonObject:
    rows = cand_mappings(item["candidate_sense_keys"], m)
    review = item.get("review") or {}
    ann = review.get("annotators")
    reviewers = None
    if isinstance(ann, dict):
        reviewers = {a: label([str(k) for k in ann[a]["chosen_sense_keys"]], m) for a in ANNOTATORS}
    L = item["labels"]
    return {
        "candidate_concept_ids": sorted({r["concept_id"] for r in rows}),
        "candidate_sense_mappings": rows,
        "labels": {
            "lexen_gold": label(L["lexen_gold"]["sense_keys"], m),
            "maru2022": label(L["maru2022"]["sense_keys"], m),
            "raganato_original": label(L["raganato_original"]["sense_keys"], m),
        },
        "mapping_id": mapping_id,
        "reviewers": reviewers,
        "schema_version": schema_version,
        "unmapped_prefix": UNMAPPED_PREFIX,
    }


def main() -> None:
    with ITEMS.open() as fh:
        items = [json.loads(line) for line in fh]
    glite = load_mapping(
        GLITE_DIR / "wordnet_sense_key_to_glite_concept.jsonl",
        GLITE_DIR / "lexen_report_aliases.json",
    )
    csi = load_mapping(
        CSI_DIR / "wordnet_sense_key_to_csi_concept.jsonl", CSI_DIR / "csi_report_aliases.json"
    )

    # fidelity regression: our builder must reproduce the existing glite block exactly
    mismatches = 0
    for it in items:
        rebuilt = record(it, glite, "glite-coarsening-maru2022-subset", "lexen.glite.v1")
        if rebuilt != it["glite"]:
            mismatches += 1
            if mismatches <= 3:
                print(f"  glite mismatch on {it['item_id']}", file=sys.stderr)
    assert mismatches == 0, f"builder does not reproduce glite block ({mismatches} mismatches)"
    print(f"fidelity OK: glite block reproduced for all {len(items)} items")

    n_unmapped = 0
    with SIDECAR.open("w") as fh:
        for it in items:
            block = record(it, csi, "csi-coarsening-maru2022-subset", "lexen.csi.v1")
            if any(not r["mapped"] for r in block["candidate_sense_mappings"]):
                n_unmapped += 1
            fh.write(json.dumps({"item_id": it["item_id"], "csi": block}) + "\n")
    print(
        f"wrote {SIDECAR} ({len(items)} items; "
        f"{n_unmapped} items have >=1 unmapped candidate under CSI)"
    )


if __name__ == "__main__":
    main()
