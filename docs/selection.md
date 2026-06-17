# Suspicious-Item Selection

The selection package is stored under `sources/selection/`.

## Inputs

Selection is derived from committed source files:

* `sources/maru2022/original/files/ALLamended.data.xml`
* `sources/maru2022/original/files/ALLamended.gold.key.txt`
* model-prediction files under `sources/model-panel/predictions/`

The generated compact selection file is `sources/selection/lexicographer_review.jsonl.gz`. It
contains one record for each of the 4,917 Maru 2022 ALL_NEW / ALLamended instances.

Each row includes:

* item id, lemma, POS, target context, and WordNet candidates
* the Maru 2022 gold sense keys
* the compact model-panel predictions used by the audit
* derived model-panel statistics
* `suspicion_set` and `suspicion_rationale`

The compact package is committed for review convenience. It is not an opaque source: the selection
script verifies the decisive fields against Maru2022 labels and the committed model-panel
predictions.

## Selection Summary

Selection: a model panel of three families - SANDWiCH; GPT-5.5; and a CatBoost ensemble of WSD
models (ConSeC, ESCHER, BEM, MFS, gpt-5-mini) - flagged 363 items for review via an S1-S6 waterfall
(S1 55, S2 138, S3 41, S4 75, S5 48, S6 6; not flagged 4,554).

`sources/selection/waterfall_summary.json` records the lexEN v1 selection summary and source hashes:

| Metric | Value |
| --- | ---: |
| Total records | 4,917 |
| Suspicious items selected for review | 363 |
| Not suspicious | 4,554 |
| Model panel size | 10 |

Waterfall counts:

| Set | Count |
| --- | ---: |
| S1 | 55 |
| S2 | 138 |
| S3 | 41 |
| S4 | 75 |
| S5 | 48 |
| S6 | 6 |

When multiple sense keys tied for the highest model-vote count, the selection package used the
alphabetically first sense key as the modal prediction.

## Build Contract

The release builder consumes the compact selection package. Before publishing, the package is
verified from committed source inputs:

```bash
uv run python scripts/build_selection_source.py --verify
```

To rewrite the generated selection package and summary from the committed inputs:

```bash
uv run python scripts/build_selection_source.py
```

The verification checks:

* all 4,917 Maru2022 source IDs are present exactly once
* Maru2022 labels match `ALLamended.gold.key.txt`
* item metadata matches `ALLamended.data.xml`
* model predictions match the ten committed model-panel files
* V03 candidate sense lists match the V03 prompt source
* modal predictions, correctness counts, S1-S6 classes, and suspicion rationales recompute exactly
* the suspicious set contains 363 items
