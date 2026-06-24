# Coarse-sense add-on layers for lexEN

This directory holds **add-on coarse-sense layers** that map onto the frozen `lexen-v1`
release **without modifying it**. The released dataset (`data/lexen-v1/items.jsonl`,
`data/lexen-v1/dataset.json`) and its source ledger (`sources/manifest.json`) are
unchanged and still pass `lexen-verify-release`; these layers live entirely outside that
verified surface.

Two coarsenings are available for lexEN:

- **Glite** — shipped *in-record* as `item["glite"]` inside `data/lexen-v1/items.jsonl`
  (the dataset's native coarse layer; a learner-dictionary inventory).
- **CSI** — shipped *here* as an add-on (`coarsenings/csi/`), a public third-party
  inventory (Coarse Sense Inventory, Lacerra et al., AAAI 2020) provided so coarse-sense
  results can be reproduced under an inventory no lexEN author controls.

## `coarsenings/csi/`

| Path | Purpose |
| --- | --- |
| `files/wordnet_sense_key_to_csi_concept.jsonl` | Forward map: WordNet sense key → CSI composite concept id. |
| `files/csi_report_aliases.json` | Aliases for legacy/British keys, remapped to their CSI concept. |
| `files/mapping_coverage.json` | Coverage over the lexEN candidate/gold/review inventory (79.2%). |
| `csi_layer.jsonl` | **Per-item sidecar**, one line `{ "item_id", "csi": {…} }`, the `csi` block in the same shape as `item["glite"]`. Join to `items.jsonl` on `item_id`. |
| `details.json`, `description.md` | Package metadata, provenance, and license. |

Regenerate the sidecar with `python scripts/apply_csi.py` (stdlib only). That script also
asserts it reproduces the existing `item["glite"]` block exactly before emitting CSI, so
the CSI block is structurally identical to the native Glite layer.

**License:** CSI is **CC-BY-NC-SA 4.0** (Lacerra et al. 2020); this derived subset is
distributed under the same terms with attribution. See `coarsenings/csi/details.json`.
