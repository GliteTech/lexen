# Changelog

All notable dataset and tooling changes are recorded here.

## Unreleased - CSI coarse-sense add-on - 2026-06-16

* Added a second, public coarse-sense layer (**CSI**, Coarse Sense Inventory; Lacerra et al., AAAI
  2020, CC BY-NC-SA 4.0) as an **add-on resource** under `coarsenings/csi/`, alongside the native
  in-record Glite layer, so coarse-sense results are reproducible under a third-party inventory.
* Shipped the per-item CSI block as the sidecar `coarsenings/csi/csi_layer.jsonl` (keyed by
  `item_id`, same shape as `item["glite"]`), plus the forward map, aliases, and coverage summary.
* **Additive only:** the frozen `lexen-v1` artifacts (`data/lexen-v1/items.jsonl`,
  `dataset.json`) and `sources/manifest.json` are unchanged; the release content hash is unchanged
  and `lexen-verify-release --release lexen-v1` still passes. No new dataset version.
* Added `scripts/apply_csi.py` to (re)build the sidecar; it asserts byte-for-value reproduction of
  the existing Glite block before emitting CSI, guaranteeing structural parity.

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
