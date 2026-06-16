"""Glite coarsening helpers shared by release artifacts and reports."""

from __future__ import annotations

import json
from dataclasses import dataclass
from pathlib import Path

from pydantic import BaseModel, ConfigDict, TypeAdapter

from lexen.models import JsonObject, SenseKey
from lexen.paths import (
    DEFAULT_REPO_ROOT,
    GLITE_COARSENING_FILES_DIR,
    GLITE_REPORT_ALIASES_FILENAME,
    GLITE_SENSE_TO_CONCEPT_FILENAME,
)

GLITE_SCHEMA_VERSION: str = "lexen.glite.v1"
GLITE_MAPPING_ID: str = "glite-coarsening-maru2022-subset"
UNMAPPED_PREFIX: str = "unmapped:"


class GliteAliasRecord(BaseModel):
    """One explicit sense-key alias used by the Glite coarsener."""

    model_config = ConfigDict(frozen=True, extra="forbid")

    source_sense_key: SenseKey
    target_sense_key: SenseKey
    concept_id: str
    reason: str


class GliteAliasFile(BaseModel):
    """Alias file schema."""

    model_config = ConfigDict(frozen=True, extra="ignore")

    aliases: list[GliteAliasRecord]


@dataclass(frozen=True, slots=True)
class GliteLabel:
    """Coarsened representation of a fine-grained sense-key list."""

    concept_ids: list[str]
    unmapped_sense_keys: list[SenseKey]

    def to_json_object(self) -> JsonObject:
        return {
            "concept_ids": self.concept_ids,
            "unmapped_sense_keys": self.unmapped_sense_keys,
        }


_GLITE_ALIAS_ADAPTER: TypeAdapter[GliteAliasFile] = TypeAdapter(GliteAliasFile)


def load_glite_mapping(
    *,
    repo_root: Path = DEFAULT_REPO_ROOT,
    required_sense_keys: set[SenseKey] | None = None,
) -> dict[SenseKey, str]:
    """Load the WordNet sense-key to Glite concept map.

    The committed map is already the public Maru2022/lexEN subset. If ``required_sense_keys`` is
    provided, only those keys are retained, plus any aliases for those keys.
    """
    path = repo_root / GLITE_COARSENING_FILES_DIR / GLITE_SENSE_TO_CONCEPT_FILENAME
    mapping: dict[SenseKey, str] = {}
    with path.open(encoding="utf-8") as handle:
        for raw_line in handle:
            row = json.loads(raw_line)
            if not isinstance(row, dict):
                raise TypeError(f"Glite mapping row must be an object in {path}")
            sense_key = str(row["sense_key"])
            if required_sense_keys is not None and sense_key not in required_sense_keys:
                continue
            mapping[sense_key] = str(row["concept_id"])
            if required_sense_keys is not None and len(mapping) == len(required_sense_keys):
                break

    alias_path = repo_root / GLITE_COARSENING_FILES_DIR / GLITE_REPORT_ALIASES_FILENAME
    if alias_path.exists():
        alias_file = _GLITE_ALIAS_ADAPTER.validate_json(alias_path.read_bytes())
        for alias in alias_file.aliases:
            if (
                required_sense_keys is not None
                and alias.source_sense_key not in required_sense_keys
            ):
                continue
            target_concept_id = mapping.get(alias.target_sense_key)
            if target_concept_id is not None and target_concept_id != alias.concept_id:
                raise ValueError(
                    "Glite alias concept differs from canonical target mapping: "
                    f"{alias.source_sense_key}"
                )
            mapping[alias.source_sense_key] = alias.concept_id
    return mapping


def glite_concept_id(*, sense_key: SenseKey, mapping: dict[SenseKey, str]) -> str:
    """Return a Glite concept id or an explicit unmapped marker."""
    return mapping.get(sense_key, f"{UNMAPPED_PREFIX}{sense_key}")


def coarsen_sense_keys(
    *,
    sense_keys: list[SenseKey],
    mapping: dict[SenseKey, str],
) -> GliteLabel:
    """Coarsen a fine-grained sense-key list into a sorted unique concept set."""
    concept_ids = sorted({glite_concept_id(sense_key=key, mapping=mapping) for key in sense_keys})
    unmapped = sorted(key for key in set(sense_keys) if key not in mapping)
    return GliteLabel(concept_ids=concept_ids, unmapped_sense_keys=unmapped)


def candidate_sense_mappings(
    *,
    sense_keys: list[SenseKey],
    mapping: dict[SenseKey, str],
) -> list[JsonObject]:
    """Return per-candidate sense-key to Glite mapping records."""
    rows: list[JsonObject] = []
    for sense_key in sorted(set(sense_keys)):
        mapped = sense_key in mapping
        rows.append(
            {
                "concept_id": glite_concept_id(sense_key=sense_key, mapping=mapping),
                "mapped": mapped,
                "sense_key": sense_key,
            }
        )
    return rows
