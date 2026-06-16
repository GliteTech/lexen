# lexEN Dataset Schema

The canonical dataset file is `data/<release>/items.jsonl`. Each line is one JSON object. The
current schema is `lexen.item.v2` for `lexen-v1`.

## Item Record

Required fields:

| Field | Type | Description |
| --- | --- | --- |
| `schema_version` | string | Item schema version. Current value: `lexen.item.v2`. |
| `dataset_canary` | string | High-entropy contamination canary from release metadata. |
| `item_id` | string | Raganato/Maru instance id. |
| `document_id` | string | Source document id inferred from `item_id`. |
| `sentence_id` | string | Source sentence id inferred from `item_id`. |
| `source_dataset` | string | Source corpus: `senseval2`, `senseval3`, `semeval2013`, or `semeval2015`. |
| `lemma` | string | Target lemma. |
| `pos` | string | Target POS in Maru format. |
| `target` | object | Target surface string and zero-based token index in the target sentence. |
| `context` | object | Tokenized preceding sentences, target sentence, and following sentences. |
| `candidate_sense_keys` | array | Full WordNet 3.0 candidate sense keys for lemma and POS. |
| `maru_prompt_sense_keys` | array | Sense keys shown in the original Maru-style prompt asset. |
| `labels` | object | Label sets described below. |
| `review` | object | Selection and lexicographer-review provenance. |
| `glite` | object | Coarse Glite concept mappings for labels, reviewers, and candidate senses. |

## Labels

`labels.raganato_original.sense_keys` is the original Raganato ALL gold label for the same instance
ID.

`labels.maru2022.sense_keys` is the Maru2022 ALL_NEW / ALLamended source label.

`labels.lexen_gold.sense_keys` is the canonical lexEN label:

* Unreviewed items keep the Maru2022 label.
* Reviewed items use any non-empty sense-key set selected by at least two of RF, PW, and PH.
* Reviewed items are removed from `items.jsonl` when at least two reviewers mark `cannot_answer`.
* Reviewed items are also removed from `items.jsonl` when no fine-grained sense set receives
  two-reviewer support.

Every retained item has a non-empty `labels.lexen_gold.sense_keys` list.

`labels.lexen_gold.decision` records the decision path:

* `unreviewed_kept_maru`
* `three_way_exact_agreement`
* `two_of_three_sense_agreement`

The removed-items sidecar uses the same label object shape, but removed items have
`labels.lexen_gold.sense_keys: []` and `labels.lexen_gold.is_empty: true`.

## Target Location

The authoritative target location is `target.token_index`, which indexes into
`context.target_sentence`. The index is zero-based. Example:

```json
{
  "target": {
    "text": "art",
    "token_index": 1
  },
  "context": {
    "target_sentence": ["The", "art", "of", "change-ringing"]
  }
}
```

In this example the target word is `context.target_sentence[1]`, i.e. `art`.

The compact SenseBench export uses the same value under the flat field name `target_token_index`.

## Reviews

Reviewed canonical items embed the review evidence directly under `review`:

* `review.status`: `reviewed`
* `review.annotators.RF`, `review.annotators.PW`, `review.annotators.PH`
* `review.consensus`
* `review.model_panel`
* `review.suspicion_set` and `review.suspicion_rationale`

Unreviewed canonical items have `review.status: unreviewed`, `review.annotators: null`, and
`review.consensus: null`.

`data/lexen-v1/reviews.jsonl` stores one normalized convenience row per reviewed item. It mirrors
the RF/PW/PH evidence used by the label policy:

* `annotators.RF.chosen_sense_keys`
* `annotators.RF.cannot_answer`
* `annotators.RF.cannot_answer_notes`
* `annotators.RF.comment`
* the same fields under `annotators.PW`
* the same fields under `annotators.PH`
* `consensus.decision`
* `consensus.disposition`
* `consensus.removal_reason`
* `consensus.sense_keys`

The raw RF/PW/PH JSON files are also stored under `sources/reviews/`.

## Glite Layer

Every retained item has a `glite` object:

| Field | Description |
| --- | --- |
| `schema_version` | Current value: `lexen.glite.v1`. |
| `mapping_id` | Glite mapping package identifier. |
| `unmapped_prefix` | Prefix used when a fine sense key is absent from the map. |
| `labels.raganato_original.concept_ids` | Coarsened concepts for the Raganato label. |
| `labels.maru2022.concept_ids` | Coarsened concepts for the Maru2022 label. |
| `labels.lexen_gold.concept_ids` | Coarsened concepts for the lexEN label. |
| `reviewers.RF/PW/PH.concept_ids` | Coarsened reviewer selections for reviewed items; `null` for unreviewed items. |
| `candidate_sense_mappings` | One row per candidate sense key with `sense_key`, `concept_id`, and `mapped`. |
| `candidate_concept_ids` | Sorted unique concept IDs present among candidate senses. |

If a sense key is not present in the Glite map or alias table, the concept ID is
`unmapped:<sense_key>` and the sense key is listed in `unmapped_sense_keys`.

## Removed Items Sidecar

`exports/raganato/lexen-v1/lexen-v1.removed.json` stores reviewed items excluded from the benchmark.
The top-level schema version is `lexen.removed.v2`.

Each removed item includes:

| Field | Description |
| --- | --- |
| `item_id`, `document_id`, `sentence_id`, `source_dataset`, `lemma`, `pos`, `target`, `context` | Source context for audit. |
| `labels.raganato_original.sense_keys` | Original Raganato label, retained as lineage evidence. |
| `labels.maru2022.sense_keys` | Maru2022 label, retained as source evidence. |
| `labels.lexen_gold.sense_keys` | Empty list because the item is removed from scoring. |
| `removal.decision` | `two_of_three_cannot_answer_removed` or `three_way_no_consensus_removed`. |
| `annotators` | RF/PW/PH selected senses, cannot-answer flags, notes, and comments. |
| `review` | Embedded reviewed-item status, annotators, consensus, model-panel evidence, and suspicion metadata. |
| `glite` | Glite label, reviewer, and candidate mappings. |
| `model_panel` | Suspicious-item selection evidence. |

Removed items remain in `data/lexen-v1/reviews.jsonl`, but they are absent from all benchmark
scoring exports.

## Compatibility Exports

`exports/raganato/<release>/<release>.data.xml` contains only retained benchmark instances. Removed
targets are preserved in the XML text as ordinary `<wf>` tokens, not `<instance>` targets.

`exports/raganato/<release>/<release>.gold.key.txt` uses `labels.lexen_gold.sense_keys` and has one
row for each retained benchmark item.

`exports/sensebench/<release>/items.jsonl` uses the same `lexen_gold` label and the compact record
shape expected by SenseBench.

## Metadata

`data/<release>/dataset.json` stores:

* release id, release type, schema version, and created date
* contamination canary
* count totals and decision totals
* label policy
* source artifact checksums
* source manifest path
* report artifact checksums
* output artifact checksums

The verifier checks the checksums in `dataset.json` and `sources/manifest.json` against the files in
the repository.
