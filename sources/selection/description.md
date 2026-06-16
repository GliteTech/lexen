---
spec_version: "2"
dataset_id: "lexicographer-review-all-new"
source_package_described_at: "2026-04-30"
---
# Lexicographer Review ALL_NEW

## Metadata

* **Name**: Lexicographer Review ALL_NEW
* **Year**: 2026
* **Authors**: Vassili Philippov
* **License**: research-only
* **Access**: versioned repository source package
* **Size**: 4,917 instances with 10 model predictions each, structured context windows, and complete
  WordNet sense inventories

## Overview

The Lexicographer Review ALL_NEW package is the generated selection source used to identify and
inspect suspicious Maru2022 instances. It is rebuilt from the Maru2022 ALLamended XML and gold-key
files plus the committed model-panel prediction files by `scripts/build_selection_source.py`.
ALL_NEW is a corrected version of the Raganato evaluation benchmark covering 4,917 polysemous
content-word instances from four evaluation datasets: Senseval-2 (SE2), Senseval-3 (SE3),
SemEval-2013 (SE13), and SemEval-2015 (SE15). SemEval-2007 is excluded from ALL_NEW as it overlaps
with the other four datasets.

The dataset packages all information a lexicographer needs to adjudicate a single instance into one
JSON record: structured context window (5 preceding + 2 following sentences with token-level
metadata), the complete WordNet 3.0 sense inventory for the target lemma, the Maru2022 source
annotation, and predictions from a model panel of three families: SANDWiCH, GPT-5.5, and a CatBoost
ensemble of WSD models (ConSeC, ESCHER, BEM, MFS, gpt-5-mini). Each record also carries a waterfall
suspicion classification (S1-S6) that flags instances where models systematically disagree with the
Maru2022 source annotation.

The motivation for this package is to identify potential annotation errors in ALL_NEW. Even after
Maru 2022's corrections, systematic model disagreement with Maru2022 labels can signal remaining
errors, overly fine-grained WordNet distinctions that should be coarsened, or genuinely hard
disambiguation cases that warrant expert review.

## Content & Annotation

Each record in `lexicographer_review.jsonl.gz` is a JSON object with the following structure:

**Instance identification**: `instance_id` (Raganato XML format, e.g.,
`semeval2013.d001.s001.t001`), `lemma`, `pos` (NOUN/VERB/ADJ/ADV), `dataset` (SE2/SE3/SE13/SE15).

**Context**: Structured context window with `preceding_sentences` (up to 5), `target_sentence`,
`following_sentences` (up to 2), and `target_token_index` (0-based index of the target token in the
target sentence). Each sentence is a list of token dicts with `surface`, `lemma`, `pos`,
`is_target_instance`, and `instance_id` fields.

**Sense inventory**: `candidates_in_maru_prompt` (the sense keys presented to LLMs in the Maru V03
prompt format) and `all_wordnet_senses` (all WordNet 3.0 senses for the lemma+POS pair, including
senses not in the Maru prompt). Each sense entry includes `sense_key`, `synset_name`, `lemma`,
`pos`, `definition`, `examples`, `synonyms`, and `in_maru_prompt` flag.

**Maru2022 source annotation**: `gold_sense_keys` (list, usually one key but may have multiple
acceptable answers), `gold_sense_id` (primary source key). The field names preserve the upstream
package schema.

**Model predictions**: `modal_predicted_sense_id` (modal across all 10 models with alphabetical
tie-break), `modal_count` (vote count), `model_predictions` (dict with one entry per model).

Each model prediction entry contains: `predicted_sense_key` (null for failures), `is_correct`,
`agrees_with_modal`, `agrees_with_gold`, and `justifications` (only populated for the
`gpt55_t0158_headerfooter` model, which returns structured sense-by-sense justifications).

**Agreement statistics**: `n_models_total` (10), `n_correct`, `n_distinct_predictions`,
`top_prediction_share` (modal vote share).

**Waterfall classification**: `suspicion_set` (S1-S6 or null) and `suspicion_rationale`
(natural-language explanation).

### Model Labels

The 10 models are:

| Label | Source | Description |
| --- | --- | --- |
| `gpt55_t0152_p01` | t0152 | GPT-5.5, prompt variant P01 (basic definition) |
| `gpt55_t0152_p02` | t0152 | GPT-5.5, prompt variant P02 (examples) |
| `gpt55_t0152_p03` | t0152 | GPT-5.5, prompt variant P03 (chain-of-thought) |
| `gpt55_t0156_e69` | t0156 | GPT-5.5, E69 ensemble-style prompt |
| `gpt55_t0158_headerfooter` | t0158 | GPT-5.5, header+footer prompt with justifications |
| `gpt55_t0173_v01` | t0173 | GPT-5.5, V01 updated prompt |
| `gpt55_t0173_v03` | t0173 | GPT-5.5, V03 frequency-ordered candidate list |
| `gpt55_t0173_v06` | t0173 | GPT-5.5, V06 refined prompt |
| `sandwich` | t0058 | SANDWiCH |
| `catboost` | t0070 | CatBoost ensemble selector over ConSeC, ESCHER, BEM, MFS, and gpt-5-mini |

### Waterfall Suspicion Classes

Selection: a model panel of three families - SANDWiCH; GPT-5.5; and a CatBoost
ensemble of WSD models (ConSeC, ESCHER, BEM, MFS, gpt-5-mini) - flagged 363
items for review via an S1-S6 waterfall (S1 55, S2 138, S3 41, S4 75, S5 48,
S6 6; not flagged 4,554).

Operationally, the S1-S6 waterfall classification is applied to each instance based on the 8 GPT-5.5
predictions. SANDWiCH and CatBoost participate in the modal vote, and S1 requires both to agree
with the GPT-5.5 consensus:

* **S1**: All 8 GPT-5.5 variants agree on one sense different from Maru2022, and both SANDWiCH and
  CatBoost also agree on that alternative sense. Highest suspicion that the Maru2022 label is
  incorrect.
* **S2**: All 8 GPT-5.5 variants agree on one sense different from Maru2022, but at least one
  of SANDWiCH or CatBoost disagrees or is missing.
* **S3**: All 8 GPT-5.5 variants differ from Maru2022 but disagree on which alternative sense to
  predict.
* **S4**: Exactly 7/8 GPT-5.5 variants agree on one alternative sense (one dissents).
* **S5**: Exactly 6/8 GPT-5.5 variants agree on one alternative sense (two dissent).
* **S6**: At least 6/8 GPT-5.5 variants predict senses different from Maru2022 but no single
  alternative sense has at least 6 agreements.

Buckets are exclusive and applied in order S1 > S2 > S3 > S4 > S5 > S6. An instance with all 8
GPT-5.5 agreeing unanimously cannot fall into S3 (which requires disagreement), so S1 and S2 are
checked first.

## Statistics

| Field | Value |
| --- | --- |
| Total instances | 4,917 |
| Source datasets | SE2, SE3, SE13, SE15 |
| GPT-5.5 model variants | 8 |
| Other model-panel families | SANDWiCH, CatBoost ensemble |
| SANDWiCH missing | 7 (instances not in SANDWiCH's training distribution) |
| CatBoost missing | 0 |

Waterfall counts are recomputed from the committed inputs and recorded in `waterfall_summary.json`:
S1 = 55, S2 = 138, S3 = 41, S4 = 75, S5 = 48, S6 = 6.

## Usage Notes

Load the JSONL.gz file in Python:

```python
import gzip, json

records = []
with gzip.open("lexicographer_review.jsonl.gz", "rt", encoding="utf-8") as f:
    for line in f:
        records.append(json.loads(line))
```

Filter to suspicious instances only:

```python
suspicious = [r for r in records if r["suspicion_set"] is not None]
s1_s2 = [r for r in records if r["suspicion_set"] in {"S1", "S2"}]
```

The `schema.json` file documents the full JSON Schema (draft-07) for record validation. SANDWiCH
predictions may have `"coverage": "missing"` for 7 instances where the model had no coverage. When
`predicted_sense_key` is null for a GPT-5.5 model, the model failed to return a parseable prediction
for that instance.

T0158 justifications are pre-resolved: each entry in the `justifications` list has a `sense_key`
field (derived from the V03 candidate list's 1-based `sense_index`) alongside the text `reason`.
Out-of-range indices are preserved as `<unknown_index_N>` strings.

## Build Contract

The package is deterministic. Run:

```bash
uv run python scripts/build_selection_source.py --verify
```

to verify the committed JSONL and summary against the Maru2022 source files and all ten committed
model-prediction files. Run the same script without `--verify` to regenerate the JSONL and summary.

The verification checks item IDs, source labels, source XML metadata, V03 prompt candidate lists,
model predictions, modal predictions, correctness counts, suspicion rationales, and S1-S6 class
membership.

## Summary

The Lexicographer Review ALL_NEW package contains the information needed for expert adjudication of
ALL_NEW (Maru 2022) instances in a single JSONL.gz file. Each of the 4,917 records combines
structured context, the full WordNet sense inventory, the Maru2022 source annotation, 10 model
predictions, and a waterfall suspicion classification.

This package is the source for the 363-item lexicographer review queue used by lexEN. It lets a
reviewer inspect the context, read all WordNet definitions, and compare model agreement patterns
before deciding whether to confirm or correct the Maru2022 annotation. The suspicion classification
makes triage efficient by prioritizing the 363 high-signal suspicious instances over the 4,554 items
outside the review queue.
