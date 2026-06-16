---
spec_version: "2"
dataset_id: "lexicographer-review-pw-2026-05-29"
source_package_described_at: "2026-06-13"
---
# Lexicographer Review (Patrick White, 2026-05-29)

## Metadata

* **Name**: Lexicographer Review (Patrick White, 2026-05-29)
* **Year**: 2026
* **Authors**: Patrick White MBA MITI MCIL CL (Director, Wordbox Language and Publishing Services
  Ltd, https://www.wordbox.com)
* **License**: research-only
* **Access**: included in this repository under the research-use terms for this source
* **Size**: 363 verdicts on suspicious ALL_NEW items in a single JSON file
* **Saved at**: 2026-05-29 via the marureview.com tool
* **Protocol brief**: https://marureview.com/brief, mirrored in
  `sources/reviews/protocols/marureview-brief-2026-05-26.md`

## Overview

This dataset is Patrick White's independent expert review of the 363 suspicious Maru2022 ALL_NEW
items selected for lexicographer audit. Patrick is a credentialled professional lexicographer (MBA,
MITI, MCIL CL) and Director of Wordbox Language and Publishing Services Ltd. The review was
completed on 2026-05-29 via the marureview.com tool.

The review used the shared annotator brief preserved in this repository. The brief instructs
reviewers to select one WordNet sense by default, select multiple senses only for genuine textual
ambiguity, and use a typed `cannot_answer` taxonomy when the item cannot be answered as posed.

## Content And Annotation

The dataset is one JSON file with top-level keys `saved_at`, `total_items` (363), `reviewed` (363),
and `verdicts` (a list of 363 records). Each `verdicts[]` element has this schema:

| Field | Type | Description |
| --- | --- | --- |
| `instance_id` | string | Raganato-format instance ID, e.g. `semeval2013.d002.s012.t000` |
| `chosen_sense_keys` | list[string] | WordNet 3.0 percent-form sense keys the reviewer selected |
| `cannot_answer` | list[string] | Typed taxonomy with values `__no_sense_applies__`, `__inventory_inadequate__`, and `__input_defective__` |
| `cannot_answer_notes` | string \| null | Free-text rationale when `cannot_answer` is non-empty |
| `comment` | string \| null | Optional free-text comment for any verdict |

The typed `cannot_answer` taxonomy distinguishes ordinary no-sense-fits cases from WordNet inventory
gaps and defective input contexts. Any non-empty `cannot_answer` means the reviewer judged the item
unanswerable as posed for that reviewer. Under lexEN v1, reviewed items with two independent
cannot-answer judgements are removed from scoring exports.

## Statistics

| Metric | Value |
| --- | ---: |
| Total verdicts | 363 |
| Verdicts with a single chosen sense | 316 |
| Verdicts with multiple chosen senses | 18 |
| Verdicts with a non-empty `cannot_answer` flag | 29 |
| `cannot_answer` = `__no_sense_applies__` | 11 |
| `cannot_answer` = `__inventory_inadequate__` | 12 |
| `cannot_answer` = `__input_defective__` | 6 |
| Verdicts with comments | 33 |
| Verdicts with `cannot_answer_notes` | 29 |

## Usage Notes

Load the JSON file and index `verdicts` by `instance_id`. Sense-key strings use the WordNet 3.0
percent form and are byte-identical to the Maru2022 gold and the other review files. The on-disk
`cannot_answer` values are double-underscore-wrapped and should be matched exactly.

This source is released for research use. When publishing results that use these verdicts, cite
Patrick White MBA MITI MCIL CL (Wordbox Language and Publishing Services Ltd) with the 2026-05-29
saved-at date.
