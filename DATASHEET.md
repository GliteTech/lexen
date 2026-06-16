# Datasheet For lexEN v1

## Motivation

lexEN is a lexicographer-reviewed English Word Sense Disambiguation (WSD) benchmark for evaluating
systems that assign WordNet 3.0 sense keys to ambiguous words in context.

The dataset is built as a targeted verification layer over Maru et al. 2022 ALL_NEW / ALLamended.
Maru2022 is used as the base benchmark. Selection: a model panel of three families - SANDWiCH;
GPT-5.5; and a CatBoost ensemble of WSD models (ConSeC, ESCHER, BEM, MFS, gpt-5-mini) - flagged
363 items for review via an S1-S6 waterfall (S1 55, S2 138, S3 41, S4 75, S5 48, S6 6; not flagged
4,554). Three professional lexicographers independently reviewed those items under a shared
protocol.

The benchmark is intended to support reliable English WSD evaluation, comparison between systems,
error analysis, and research on fine-grained versus coarse-grained sense distinctions.

## Composition

lexEN v1 starts from 4,917 Maru2022 source items. The released scoring benchmark contains 4,861
retained items:

* 4,554 unreviewed items keep their Maru2022 label.
* 307 reviewed items are retained after applying the three-reviewer policy.
* 56 reviewed items are removed from scoring.
* 211 retained labels differ from the Maru2022 label.

Each retained canonical item includes:

* source document, sentence, lemma, POS, target token, and full context;
* the original Raganato ALL label for the same instance ID;
* the Maru2022 ALLamended label;
* the lexEN scoring label;
* reviewer evidence for reviewed items;
* WordNet 3.0 candidate senses;
* Glite coarse-sense mappings for labels, reviewers, and candidate senses.

Removed reviewed items are not scoring targets. They are preserved in the removed-items sidecar for
audit and reproducibility.

## Collection And Review Process

The upstream source files are the original Raganato ALL evaluation files and Maru2022 ALLamended
files. The files are stored in their source formats under `sources/`.

The suspicious-item set was flagged by running the model panel over all 4,917 Maru2022 items. The
selection procedure is deterministic and documented in [`docs/selection.md`](docs/selection.md).
The generated 4,917-row selection package is stored under [`sources/selection/`](sources/selection/).

The 363 selected items were reviewed at [marureview.com](https://marureview.com/). The reviewer
brief is preserved in [`docs/labeling-process.md`](docs/labeling-process.md) and
[`sources/reviews/protocols/marureview-brief-2026-05-26.md`](sources/reviews/protocols/marureview-brief-2026-05-26.md).
Raw reviewer exports are stored under [`sources/reviews/`](sources/reviews/).

The release policy is:

* unreviewed items keep the Maru2022 label;
* reviewed items use a non-empty sense set selected by at least two reviewers;
* reviewed items are removed when at least two reviewers mark them unanswerable;
* reviewed items are removed when no fine-grained sense set receives support from at least two
  reviewers.

## Recommended Uses

lexEN is suitable for:

* intrinsic evaluation of English all-words WSD systems;
* comparisons with Raganato-style WSD evaluation pipelines;
* analysis of high-risk Maru2022 labels and professional reviewer agreement;
* experiments that compare fine-grained WordNet labels with a coarse Glite concept layer.

Use `labels.lexen_gold.sense_keys` as the primary scoring target. Use the Raganato export for
standard WSD scoring tools, or the canonical JSONL artifact for richer analysis.

## Out-Of-Scope Uses

lexEN is not a multilingual WSD benchmark, an entity-linking benchmark, a dictionary-definition
ranking dataset, or a full reannotation of every Raganato item. Only the 363 model-panel-suspicious
Maru2022 items were manually reviewed.

The Glite concept layer is a coarsening view over WordNet senses. It is not the primary fine-grained
scoring label.

## Distribution

The canonical release files are:

* [`data/lexen-v1/items.jsonl`](data/lexen-v1/items.jsonl)
* [`data/lexen-v1/dataset.json`](data/lexen-v1/dataset.json)
* [`data/lexen-v1/reviews.jsonl`](data/lexen-v1/reviews.jsonl)
* [`exports/raganato/lexen-v1/`](exports/raganato/lexen-v1/)
* [`exports/sensebench/lexen-v1/items.jsonl`](exports/sensebench/lexen-v1/items.jsonl)

The source manifest in [`sources/manifest.json`](sources/manifest.json) records source package
metadata, access status, licenses, and SHA-256 hashes.

## Licensing

The repository contains code and dataset artifacts with different terms.

The build, verification, report-generation, and test software is Apache-2.0. Dataset artifacts are
released for research / non-commercial evaluation under the source-package terms recorded in
[`LICENSE`](LICENSE), [`NOTICE`](NOTICE), and [`sources/manifest.json`](sources/manifest.json).

Maru2022 ALLamended is recorded as CC-BY-NC-4.0. The Maru et al. 2022 paper files are recorded as
CC-BY-4.0. WordNet 3.0 notices are included in [`NOTICE`](NOTICE).

## Maintenance

The release is reproducible from committed source artifacts and scripts:

```bash
uv run python scripts/build_selection_source.py --verify
uv run python scripts/build_source_manifest.py
uv run python scripts/build_release.py --release lexen-v1
uv run python scripts/verify_release.py --release lexen-v1
uv run pytest
```

Future releases should preserve source-label lineage, removed-item sidecars, review provenance,
release metadata hashes, and the contamination canary policy documented in the release metadata.

## Ethical And Quality Considerations

The dataset contains naturally occurring English contexts from established WSD benchmark sources.
Those contexts can contain outdated language, culturally specific assumptions, or other source-text
artifacts inherited from the upstream corpora.

Reviewer names and comments are included with consent as audit evidence. Users should treat reviewer
comments as scholarly annotation evidence, not as general-purpose text data for unrelated model
training.

The reviewed subset is intentionally risk-focused. Aggregate performance on lexEN should therefore
be interpreted as performance on a corrected Maru2022-derived benchmark, not as proof that all
remaining Maru2022 labels are error-free.
