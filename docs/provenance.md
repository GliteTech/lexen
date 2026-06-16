# Provenance

lexEN is built as a traceable correction layer over Maru et al. 2022 ALL_NEW / ALLamended, with the
original Raganato label retained as a separate lineage layer.

## Source Lineage

lexEN v1 follows this chain:

* The base benchmark is Maru 2022 ALL_NEW / ALLamended.
* The original Raganato ALL XML and gold-key files are stored under
  `sources/raganato/original/files/`.
* The original Maru XML and gold-key files are stored under `sources/maru2022/original/files/` in
  upstream format.
* The upstream Maru et al. 2022 paper PDF and BibTeX are copied into `sources/maru2022/papers/`.
* The model-panel prediction files used for selection are stored under `sources/model-panel/`.
* Selection used a model panel of three families: SANDWiCH, GPT-5.5, and a CatBoost ensemble of WSD
  models (ConSeC, ESCHER, BEM, MFS, gpt-5-mini).
* `scripts/build_selection_source.py --verify` recomputes the S1-S6 suspicious-item classes from
  Maru2022 labels and the committed prediction files. This reproduces the 363 reviewed items.
* Those 363 items were loaded into the review website at https://marureview.com/.
* The exact reviewer-facing brief is mirrored in
  `sources/reviews/protocols/marureview-brief-2026-05-26.md`.
* Three professional lexicographers reviewed the items under the same protocol and returned JSON
  verdict files: RF, PW, and PH.
* The three-review agreement report is stored in `reports/rf-pw-ph-2026-06-13/` as HTML, PDF,
  Markdown, metrics JSON, per-item JSONL, and rendered charts.
* The Glite-coarse report metrics and release-level Glite label layer use the mapping subset in
  `sources/glite-coarsening/`.
* The release builder applies the three-annotator label/removal policy and writes canonical JSONL, a
  removed-items sidecar, and Raganato and SenseBench exports.

## Versioned Inputs

The release is derived from these versioned inputs:

* `sources/maru2022/original/`
* `sources/maru2022/papers/`
* `sources/raganato/original/`
* `sources/model-panel/`
* `sources/selection/`
* `sources/reviews/rf-2026-05-26/`
* `sources/reviews/pw-2026-05-29/`
* `sources/reviews/ph-2026-06-13/`
* `sources/glite-coarsening/`

`sources/manifest.json` records package-level provenance, source URLs, licenses, and SHA-256 hashes
for these inputs. `data/lexen-v1/dataset.json` records source, report, and output artifact hashes
for the exact release.

## Label Lineage

Each retained canonical item stores three label layers:

* `labels.raganato_original`: the original Raganato ALL label for the same instance ID.
* `labels.maru2022`: the Maru2022 ALLamended source label.
* `labels.lexen_gold`: the lexEN scoring label after applying the review policy.

Removed reviewed items store the same label lineage in
`exports/raganato/lexen-v1/lexen-v1.removed.json`, with an empty `lexen_gold` label because they are
excluded from scoring.

## Reproducibility Guarantees

lexEN v1 is designed to make the following claims reproducible:

* Maru 2022 is the base dataset.
* Original Raganato labels are preserved for the 4,917 Maru2022 source IDs.
* The selection package contains all 4,917 Maru instances and marks the 363 suspicious items.
* The 363 suspicious items are reproducible from committed model-panel predictions.
* The review evidence contains the same-protocol RF/PW/PH verdicts used for lexEN v1.
* The exact annotator instructions are preserved in the repository.
* `lexen_gold` changes Maru2022 labels only where the three-annotator policy permits it.
* Reviewed items without a usable two-reviewer fine-grained label are removed, not assigned a
  Maru2022 fallback label.
* The benchmark exports contain 4,861 retained items from the 4,917 Maru2022 source items.
