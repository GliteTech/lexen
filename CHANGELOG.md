# Changelog

All notable dataset and tooling changes are recorded here.

## lexen-v1 - 2026-06-13

Initial lexEN release.

* Built from Maru et al. 2022 ALL_NEW / ALLamended with original Raganato labels retained as a
  separate lineage layer.
* Reviewed 363 model-panel-suspicious items with three professional lexicographers under a shared
  reviewer brief.
* Released 4,861 retained scoring items and a removed-items audit sidecar for 56 reviewed items
  excluded from scoring.
* Changed 211 retained labels from Maru2022 according to the three-reviewer policy.
* Added canonical JSONL, Raganato-compatible, and SenseBench-compatible exports.
* Added Glite coarse-sense mappings for labels, reviewer selections, and candidate senses using the
  public Maru2022/lexEN mapping subset.
* Added the RF/PW/PH agreement report in HTML, PDF, Markdown, metrics JSON, and per-item JSONL.
* Added release verification scripts, source-manifest generation, and policy tests.

## Forthcoming

* Zenodo DOI metadata after the release archive is minted.
* Additional errata entries if users report verified label or packaging issues.
