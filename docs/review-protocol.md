# Review Protocol And Label Policy

lexEN v1 uses three same-protocol review files.

## Review Website

The 363 selected items were reviewed through https://marureview.com/. The website presented the
target context, target word, WordNet senses, and controls for selecting sense keys or marking
`cannot_answer`.

The exact reviewer-facing instructions are preserved in `docs/labeling-process.md` and as a source
artifact at `sources/reviews/protocols/marureview-brief-2026-05-26.md`.

The review evidence consists of these same-protocol files:

* `sources/reviews/rf-2026-05-26/maru2022-wsd-verdicts-2026-05-26.json`
* `sources/reviews/pw-2026-05-29/maru2022-wsd-verdicts-2026-05-29.json`
* `sources/reviews/ph-2026-06-13/maru2022-wsd-verdicts-2026-06-13.json`

The normalized review export keeps selected sense keys, `cannot_answer` flags,
`cannot_answer_notes`, and free-text comments.

## Canonical Gold Rule

For each item:

* If the item was not reviewed, `lexen_gold` equals the Maru 2022 label.
* If at least two of RF, PW, and PH selected the same non-empty set of sense keys, `lexen_gold` is
  that set.
* If no non-empty sense-key set has two votes and at least two reviewers selected no sense keys
  while marking `cannot_answer`, the item is removed from lexEN.
* Otherwise, if no fine-grained sense set receives two-reviewer support, the item is removed from
  lexEN.

The decision is stored under `labels.lexen_gold.decision` for retained items and under
`removal.decision` in the removed-items sidecar for removed items.

## Removed Reviewed Items

Removed reviewed items are excluded from:

* `data/lexen-v1/items.jsonl`
* `exports/raganato/lexen-v1/lexen-v1.data.xml` as `<instance>` targets
* `exports/raganato/lexen-v1/lexen-v1.gold.key.txt`
* `exports/sensebench/lexen-v1/items.jsonl`

The removed items remain auditable in `data/lexen-v1/reviews.jsonl` and
`exports/raganato/lexen-v1/lexen-v1.removed.json`. No Maru2022 fallback label is used for removed
items.

## Release Counts

| Decision | Count |
| --- | ---: |
| `unreviewed_kept_maru` | 4,554 |
| `three_way_exact_agreement` | 124 |
| `two_of_three_sense_agreement` | 183 |
| `two_of_three_cannot_answer_removed` | 27 |
| `three_way_no_consensus_removed` | 29 |

lexEN v1 has 4,861 retained benchmark items. It removes 56 reviewed items and has 211 retained
`lexen_gold` labels that differ from Maru2022.
