---
spec_version: "1"
dataset_id: "lexen-model-panel"
source_package_described_at: "2026-06-14"
---
# Model-Panel Predictions

This directory contains the model-prediction assets used to identify the 363 Maru2022 items sent to
lexicographers. Selection: a model panel of three families - SANDWiCH; GPT-5.5; and a CatBoost
ensemble of WSD models (ConSeC, ESCHER, BEM, MFS, gpt-5-mini) - flagged 363 items for review via an
S1-S6 waterfall (S1 55, S2 138, S3 41, S4 75, S5 48, S6 6; not flagged 4,554).

The selection script recomputes the S1-S6 suspicion buckets from these files and the Maru2022 gold
key.

The GPT prediction files retain prompts, raw model responses, normalized predictions, and
model-facing item metadata needed for reproducibility. Transport and telemetry fields such as
provider request IDs, token counts, costs, latency, retry metadata, and HTTP status codes are not
part of this public source package.

## Models

| Label | File | Role |
| --- | --- | --- |
| `gpt55_t0152_p01` | `predictions/gpt55_t0152_p01/predictions.jsonl.gz` | GPT-5.5 prompt variant |
| `gpt55_t0152_p02` | `predictions/gpt55_t0152_p02/predictions.jsonl.gz` | GPT-5.5 prompt variant |
| `gpt55_t0152_p03` | `predictions/gpt55_t0152_p03/predictions.jsonl.gz` | GPT-5.5 prompt variant |
| `gpt55_t0156_e69` | `predictions/gpt55_t0156_e69/predictions.jsonl.gz` | GPT-5.5 prompt variant |
| `gpt55_t0158_headerfooter` | `predictions/gpt55_t0158_headerfooter/predictions.jsonl.gz` | GPT-5.5 prompt variant with justifications |
| `gpt55_t0173_v01` | `predictions/gpt55_t0173_v01/predictions.jsonl.gz` | GPT-5.5 prompt variant |
| `gpt55_t0173_v03` | `predictions/gpt55_t0173_v03/predictions.jsonl.gz` | GPT-5.5 prompt variant used for candidate-list extraction |
| `gpt55_t0173_v06` | `predictions/gpt55_t0173_v06/predictions.jsonl.gz` | GPT-5.5 prompt variant |
| `sandwich` | `predictions/sandwich/ALL.key.txt` | SANDWiCH prediction key |
| `catboost` | `predictions/catboost/predictions-raganato-all.jsonl` | CatBoost ensemble selector predictions |

## Selection Policy

The S1-S6 suspicion buckets use only the eight GPT-5.5 variants for bucket membership. SANDWiCH and
CatBoost participate in the modal vote, and S1 requires both to agree with the GPT-5.5 consensus.
The public selection script verifies that these files reproduce 363 suspicious items:

```bash
uv run python scripts/build_selection_source.py --verify
```

The prediction files are research artifacts used for dataset construction and auditability. They are
not part of the scoring benchmark.
