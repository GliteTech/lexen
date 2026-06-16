from __future__ import annotations

import gzip
import json
from pathlib import Path

from lexen.paths import (
    GLITE_COARSENING_FILES_DIR,
    GLITE_SENSE_TO_CONCEPT_FILENAME,
    MODEL_PANEL_SOURCE_DIR,
)
from lexen.selection import GPT55_MODEL_LABELS

REPO_ROOT = Path(__file__).resolve().parents[1]

PUBLIC_GLITE_FIELDS = {
    "concept_id",
    "lemma",
    "sense_key",
    "wordnet_pos",
}
REMOVED_GLITE_FIELDS = {
    "cluster_id",
    "concept_description",
    "concept_pos",
    "fine_sense_id",
    "headword",
    "oewn_synset_id",
    "wordnet_synset_id",
    "wordnet_synset_offset",
}
REMOVED_MODEL_FIELDS = {
    "cost_usd",
    "http_status",
    "input_tokens",
    "latency_seconds",
    "output_tokens",
    "prompt_hash",
    "provider_request_id",
    "reasoning_tokens",
    "retry_after",
    "retry_count",
    "retry_reasons",
    "run_id",
    "variant_id",
}


def test_public_glite_map_contains_only_release_subset_fields() -> None:
    path = REPO_ROOT / GLITE_COARSENING_FILES_DIR / GLITE_SENSE_TO_CONCEPT_FILENAME
    line_count = 0
    with path.open(encoding="utf-8") as handle:
        for raw_line in handle:
            row = json.loads(raw_line)
            assert set(row) == PUBLIC_GLITE_FIELDS
            assert set(row).isdisjoint(REMOVED_GLITE_FIELDS)
            line_count += 1

    assert line_count == 10412


def test_public_model_panel_predictions_omit_transport_telemetry() -> None:
    prediction_root = REPO_ROOT / MODEL_PANEL_SOURCE_DIR
    for model_label in GPT55_MODEL_LABELS:
        path = prediction_root / model_label / "predictions.jsonl.gz"
        with gzip.open(path, mode="rt", encoding="utf-8") as handle:
            first_row = json.loads(next(handle))
        assert set(first_row).isdisjoint(REMOVED_MODEL_FIELDS)
        assert "prompt_text" in first_row
        assert "raw_response" in first_row
