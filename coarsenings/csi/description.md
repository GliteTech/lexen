---
spec_version: "1"
dataset_id: "csi-coarsening-maru2022-subset"
source_dataset_id: "csi"
source_package_generated_at: "2026-06-16"
date_added_to_lexen: "2026-06-16"
---
# CSI Coarsening Subset (third-party public coarse inventory)

This directory contains a **CSI** coarse-sense layer for lexEN — an independent, third-party
alternative to the Glite coarsening. CSI (Coarse Sense Inventory) is the 45-domain inventory of
Lacerra, Bevilacqua, Pasini & Navigli (AAAI 2020). It is provided so coarse-sense results computed
against lexEN can be reproduced under a public inventory that no lexEN author controls.

This layer is an **add-on resource over the frozen `lexen-v1` release**: it does not modify
`data/lexen-v1/items.jsonl` or the release content hash. Per-item CSI labels are shipped as the
sidecar `data/lexen-v1/csi_layer.jsonl`, keyed by `item_id`, mirroring the in-record `glite` block.

## Included Files

| File | Purpose |
| --- | --- |
| `files/wordnet_sense_key_to_csi_concept.jsonl` | Forward map: WordNet sense key → CSI composite concept id. |
| `files/mapping_coverage.json` | Coverage summary over the lexEN candidate/gold/review inventory. |
| `files/csi_report_aliases.json` | Report-local aliases for legacy/British WordNet sense keys, remapped to their CSI concept. |

## Coarsening Policy

Each WordNet synset that lexEN references is mapped to a single **composite CSI concept**
`csi:<sorted+joined domain labels>`. CSI assigns some synsets more than one domain; we collapse a
synset's full domain set into one composite class. This keeps the layer a clean **partition** that
plugs into the same single-concept coarse-scoring contract as Glite (a coarse hit inherits a fine hit,
else predicted concept ∈ gold concepts). If a sense key is not present in the public CSI map, the
coarsener first checks the alias file; if no alias exists it keeps an explicit `unmapped:<sense_key>`
marker rather than guessing a concept. CSI covers 79.2% of the referenced keys; the remainder are
`unmapped:` and therefore never silently merged.

## Provenance & License

Derived from the released CSI resource (`wn_synset2csi.txt`, WordNet 3.0 synset offsets) at
<https://sapienzanlp.github.io/csi/>. CSI is licensed **CC-BY-NC-SA 4.0**; this derived subset is
distributed under the same terms, with attribution to Lacerra et al. (2020). The only modification is
the join to lexEN's referenced sense keys plus the multi-domain→composite reduction described above
(declared as a change per the ShareAlike terms).
