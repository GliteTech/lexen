# lexEN

lexEN is a lexicographer-reviewed English Word Sense Disambiguation (WSD) benchmark derived from
[Maru et al. 2022 ALL_NEW / ALLamended](sources/maru2022/original/). It is designed for evaluating
systems that assign WordNet 3.0 sense keys to ambiguous English words in context.

The benchmark keeps the standard [Raganato-style evaluation format](exports/raganato/lexen-v1/)
while adding a richer [canonical JSONL artifact](data/lexen-v1/items.jsonl) with source-label
lineage, professional review evidence, and [Glite coarse-sense mappings](sources/glite-coarsening/).

Current release: [`lexen-v1`](data/lexen-v1/).

## What This Dataset Is For

Use lexEN to evaluate English all-words WSD systems against a benchmark whose highest-risk labels
were manually checked by professional lexicographers.

The primary scoring label is `labels.lexen_gold`. Each [retained item](data/lexen-v1/items.jsonl)
also keeps:

* `labels.raganato_original`: the original Raganato ALL label for the same instance ID.
* `labels.maru2022`: the Maru2022 ALLamended source label.
* `labels.lexen_gold`: the lexEN label after applying the three-reviewer policy.
* `review`: review provenance for audited items.
* `glite`: coarse Glite concept mappings for labels, reviewer selections, and candidate senses,
  using the public Maru2022/lexEN coarsening subset.

## Release Counts

| Count | Value |
| --- | ---: |
| Maru2022 source items | 4,917 |
| Retained lexEN benchmark items | 4,861 |
| Suspicious items reviewed by lexicographers | 363 |
| Unreviewed items kept from Maru2022 | 4,554 |
| Reviewed retained items | 307 |
| Reviewed items removed | 56 |
| Retained labels changed from Maru2022 | 211 |

Reviewed items are removed when at least two reviewers mark the item unanswerable, or when no
fine-grained sense set receives support from at least two reviewers.

## How lexEN Was Built

lexEN starts from Maru et al. 2022 ALL_NEW / ALLamended:

* Paper:
  [Nibbling at the Hard Core of Word Sense Disambiguation](https://aclanthology.org/2022.acl-long.324/)
  ([local PDF](sources/maru2022/papers/maru-etal-2022-nibbling-hard-core-wsd.pdf),
  [BibTeX](sources/maru2022/papers/maru-etal-2022-nibbling-hard-core-wsd.bib))
* Source repository:
  [SapienzaNLP/wsd-hard-benchmark](https://github.com/SapienzaNLP/wsd-hard-benchmark)
* Source files in this repository:
  [`sources/maru2022/original/files/`](sources/maru2022/original/files/)

The original Raganato ALL XML and gold-key files are also preserved under
[`sources/raganato/original/files/`](sources/raganato/original/files/) so every lexEN item can carry
both the original Raganato label and the Maru2022 label.

The construction process is:

1. Take Maru2022 ALLamended as the base benchmark.
2. Run a [WSD prediction panel](sources/model-panel/) over all 4,917 Maru2022 items.
3. Flag 363 suspicious items where the model panel strongly disagrees with the Maru2022 label
   using the [selection procedure](docs/selection.md).
4. Review those 363 items at [marureview.com](https://marureview.com/).
5. Give the same [reviewer brief](https://marureview.com/brief)
   ([repository copy](sources/reviews/protocols/marureview-brief-2026-05-26.md)) to three
   professional lexicographers: [Robert Farren](sources/reviews/rf-2026-05-26/),
   [Patrick White](sources/reviews/pw-2026-05-29/), and
   [Penny Hands](sources/reviews/ph-2026-06-13/).
6. Apply the [three-reviewer policy](docs/review-protocol.md):
   * keep the Maru2022 label for unreviewed items;
   * replace the label when at least two reviewers choose the same non-empty sense set;
   * remove the reviewed item when at least two reviewers mark it unanswerable;
   * remove the reviewed item when no fine-grained sense set receives two-reviewer support.
7. Build the [canonical JSONL artifact](data/lexen-v1/items.jsonl),
   [Raganato-compatible export](exports/raganato/lexen-v1/),
   [SenseBench export](exports/sensebench/lexen-v1/), and
   [removed-items audit sidecar](exports/raganato/lexen-v1/lexen-v1.removed.json).

## Suspicious-Item Selection

Selection: a model panel of three families - SANDWiCH; GPT-5.5; and a CatBoost
ensemble of WSD models (ConSeC, ESCHER, BEM, MFS, gpt-5-mini) - flagged 363
items for review via an S1-S6 waterfall (S1 55, S2 138, S3 41, S4 75, S5 48,
S6 6; not flagged 4,554).

The S1-S6 waterfall classes are recomputed from committed source predictions in
[`sources/model-panel/`](sources/model-panel/). The GPT prediction files keep prompts and normalized
outputs for reproducibility, but omit transport telemetry such as provider request IDs, token
counts, costs, and latency. Operationally, bucket membership is computed from the eight GPT-5.5
variants; SANDWiCH and CatBoost participate in the modal vote, and S1 requires both to agree with
the GPT-5.5 consensus.

Selection source:

* Generated selection package:
  [`sources/selection/lexicographer_review.jsonl.gz`](sources/selection/lexicographer_review.jsonl.gz)
* Selection documentation: [`docs/selection.md`](docs/selection.md)
* Verification script: [`scripts/build_selection_source.py`](scripts/build_selection_source.py)

Selection counts:

| Suspicion Set | Items |
| --- | ---: |
| S1 | 55 |
| S2 | 138 |
| S3 | 41 |
| S4 | 75 |
| S5 | 48 |
| S6 | 6 |
| Total reviewed | 363 |

## Lexicographer Review

The review website is [https://marureview.com/](https://marureview.com/).

The exact reviewer-facing brief is preserved in:

* [`docs/labeling-process.md`](docs/labeling-process.md)
* [`sources/reviews/protocols/marureview-brief-2026-05-26.md`](sources/reviews/protocols/marureview-brief-2026-05-26.md)

Raw review exports are stored in:

* [`sources/reviews/rf-2026-05-26/`](sources/reviews/rf-2026-05-26/)
* [`sources/reviews/pw-2026-05-29/`](sources/reviews/pw-2026-05-29/)
* [`sources/reviews/ph-2026-06-13/`](sources/reviews/ph-2026-06-13/)

The [three-reviewer agreement report](reports/rf-pw-ph-2026-06-13/) is available in:

* HTML:
  [`reports/rf-pw-ph-2026-06-13/lexicographer_agreement_2026_06_13.html`](reports/rf-pw-ph-2026-06-13/lexicographer_agreement_2026_06_13.html)
* PDF:
  [`reports/rf-pw-ph-2026-06-13/lexicographer_agreement_2026_06_13.pdf`](reports/rf-pw-ph-2026-06-13/lexicographer_agreement_2026_06_13.pdf)
* Markdown:
  [`reports/rf-pw-ph-2026-06-13/lexicographer_agreement_2026_06_13.md`](reports/rf-pw-ph-2026-06-13/lexicographer_agreement_2026_06_13.md)
* Metrics JSON:
  [`reports/rf-pw-ph-2026-06-13/metrics.json`](reports/rf-pw-ph-2026-06-13/metrics.json)
* Per-item agreement JSONL:
  [`reports/rf-pw-ph-2026-06-13/per_item_agreement.jsonl`](reports/rf-pw-ph-2026-06-13/per_item_agreement.jsonl)

## Dataset Artifacts

Primary artifact:

* [`data/lexen-v1/items.jsonl`](data/lexen-v1/items.jsonl)

Each line is one retained benchmark item. The schema is documented in
[`docs/schema.md`](docs/schema.md).

Additional release files:

| Path | Purpose |
| --- | --- |
| [`data/lexen-v1/dataset.json`](data/lexen-v1/dataset.json) | Release metadata, counts, source hashes, output hashes, and label policy. |
| [`data/lexen-v1/reviews.jsonl`](data/lexen-v1/reviews.jsonl) | Normalized RF/PW/PH review evidence for all 363 reviewed items. |
| [`exports/raganato/lexen-v1/lexen-v1.data.xml`](exports/raganato/lexen-v1/lexen-v1.data.xml) | Raganato-style XML with removed reviewed targets excluded as scoring instances. |
| [`exports/raganato/lexen-v1/lexen-v1.gold.key.txt`](exports/raganato/lexen-v1/lexen-v1.gold.key.txt) | Raganato-style gold key using `lexen_gold`. |
| [`exports/raganato/lexen-v1/lexen-v1.removed.json`](exports/raganato/lexen-v1/lexen-v1.removed.json) | Audit sidecar for reviewed items removed from scoring. |
| [`exports/sensebench/lexen-v1/items.jsonl`](exports/sensebench/lexen-v1/items.jsonl) | Compact SenseBench-compatible export. |
| [`sources/manifest.json`](sources/manifest.json) | Machine-readable source manifest with package-level provenance and hashes. |

## Loading The Dataset

Read the canonical JSONL artifact:

```python
import json
from pathlib import Path

items_path = Path("data/lexen-v1/items.jsonl")

items = []
with items_path.open(encoding="utf-8") as handle:
    for line in handle:
        items.append(json.loads(line))

print(len(items))
print(items[0]["item_id"], items[0]["labels"]["lexen_gold"]["sense_keys"])
```

Create a simple scoring lookup:

```python
gold_by_id = {
    item["item_id"]: item["labels"]["lexen_gold"]["sense_keys"]
    for item in items
}
```

Use the [Raganato-compatible export](exports/raganato/lexen-v1/) with existing WSD evaluation tools:

```bash
python your_wsd_system.py \
  --input exports/raganato/lexen-v1/lexen-v1.data.xml \
  --output predictions.key.txt

python your_scorer.py \
  --gold exports/raganato/lexen-v1/lexen-v1.gold.key.txt \
  --predictions predictions.key.txt
```

## Example Item

This is an abbreviated retained item from [`data/lexen-v1/items.jsonl`](data/lexen-v1/items.jsonl).
The Maru2022 and original Raganato labels were `field%1:17:00::`; two reviewers selected
`field%1:15:00::`, so lexEN uses that sense as `lexen_gold`.

```json
{
  "schema_version": "lexen.item.v2",
  "item_id": "senseval2.d000.s003.t009",
  "source_dataset": "senseval2",
  "lemma": "field",
  "pos": "NOUN",
  "target": {
    "text": "fields",
    "token_index": 22
  },
  "context": {
    "preceding_sentences": [
      [
        "The", "art", "of", "change-ringing", "is", "peculiar", "to",
        "the", "English", ",", "and", ",", "like", "most", "English",
        "peculiarities", ",", "unintelligible", "to", "the", "rest",
        "of", "the", "world", "."
      ],
      ["Dorothy", "L.", "Sayers", ",", "``", "The", "Nine", "Tailors", "``"],
      ["ASLACTON", ",", "England", "--"]
    ],
    "target_sentence": [
      "Of", "all", "scenes", "that", "evoke", "rural", "England", ",",
      "this", "is", "one", "of", "the", "loveliest", ":", "An", "ancient",
      "stone", "church", "stands", "amid", "the", "fields", ",", "the",
      "sound", "of", "bells", "cascading", "from", "its", "tower", ",",
      "calling", "the", "faithful", "to", "evensong", "."
    ],
    "following_sentences": [
      [
        "The", "parishioners", "of", "St.", "Michael", "and", "All",
        "Angels", "stop", "to", "chat", "at", "the", "church", "door",
        ",", "as", "members", "here", "always", "have", "."
      ],
      [
        "In", "the", "tower", ",", "five", "men", "and", "women", "pull",
        "rhythmically", "on", "ropes", "attached", "to", "the", "same",
        "five", "bells", "that", "first", "sounded", "here", "in", "1614",
        "."
      ]
    ]
  },
  "labels": {
    "raganato_original": {
      "sense_keys": ["field%1:17:00::"]
    },
    "maru2022": {
      "sense_keys": ["field%1:17:00::"]
    },
    "lexen_gold": {
      "decision": "two_of_three_sense_agreement",
      "is_empty": false,
      "sense_keys": ["field%1:15:00::"]
    }
  },
  "review": {
    "status": "reviewed",
    "lexicographer_decision": "two_of_three_sense_agreement",
    "release_disposition": "retained",
    "suspicion_set": "S1"
  },
  "glite": {
    "labels": {
      "raganato_original": {
        "concept_ids": ["ct:ct7f56A4ZLBVYeef5CpmNfield"],
        "unmapped_sense_keys": []
      },
      "maru2022": {
        "concept_ids": ["ct:ct7f56A4ZLBVYeef5CpmNfield"],
        "unmapped_sense_keys": []
      },
      "lexen_gold": {
        "concept_ids": ["ct:ct7f56A4ZLBVYeef5CpmNfield"],
        "unmapped_sense_keys": []
      }
    }
  }
}
```

## Reproducibility

Install dependencies with `uv`, then run the release scripts:

```bash
uv run python scripts/build_selection_source.py --verify
uv run python scripts/build_source_manifest.py
uv run python scripts/build_release.py --release lexen-v1
uv run python scripts/verify_release.py --release lexen-v1
uv run pytest
```

The [release verifier](scripts/verify_release.py) checks:

* source-manifest hashes
* release artifact hashes
* expected counts
* Raganato original label coverage
* Maru2022 source label coverage
* `lexen_gold` policy decisions
* removed-item exclusion from scoring exports
* Raganato XML and gold-key consistency
* SenseBench export consistency
* embedded review evidence
* Glite label and candidate mappings
* contamination-canary placement

## Contamination Canary

Every lexEN release contains a high-entropy canary string for later training-data contamination
audits. In `lexen-v1`, it is stored in [`data/lexen-v1/dataset.json`](data/lexen-v1/dataset.json),
repeated in canonical item and review rows, carried in the SenseBench export metadata, and inserted
into the Raganato XML as an XML comment.

The canary is metadata. It should not be included in WSD prompts or used as model input.

## Scope And Limitations

lexEN is an English WordNet 3.0 WSD benchmark. It is not a replacement for multilingual WSD,
entity-linking, dictionary-definition ranking, or general lexical-semantic evaluation.

Only the 363 [model-panel-suspicious](docs/selection.md) Maru2022 items were manually reviewed. The
remaining 4,554 items keep the Maru2022 label. This is deliberate: lexEN is a targeted correction
and audit layer over Maru2022, not a full reannotation of every Raganato item.

The [Glite layer](sources/glite-coarsening/) is a separate coarse-sense view. The fine-grained
WordNet scoring label remains `labels.lexen_gold.sense_keys`.

## Artifact Guide

Start with the canonical dataset in [`data/lexen-v1/items.jsonl`](data/lexen-v1/items.jsonl). It is
the richest artifact: each retained item includes original Raganato labels, Maru2022 labels, lexEN
labels, review evidence where available, full context, WordNet candidates, and the Glite coarsening
layer. Use [`data/lexen-v1/dataset.json`](data/lexen-v1/dataset.json) for release counts, label
policy, hashes, and provenance pointers.

For standard WSD scoring, use the Raganato export in
[`exports/raganato/lexen-v1/`](exports/raganato/lexen-v1/). It contains the XML input file, the
lexEN gold key, and a removed-items sidecar for audited targets excluded from scoring. For compact
JSONL evaluation pipelines, use the SenseBench export in
[`exports/sensebench/lexen-v1/items.jsonl`](exports/sensebench/lexen-v1/items.jsonl).

To understand how the benchmark was built, read [`docs/provenance.md`](docs/provenance.md),
[`docs/selection.md`](docs/selection.md), and [`docs/review-protocol.md`](docs/review-protocol.md).
The upstream Raganato and Maru2022 source files are preserved under
[`sources/raganato/original/`](sources/raganato/original/) and
[`sources/maru2022/original/`](sources/maru2022/original/). The committed model-panel predictions
and generated suspicious-item package are in [`sources/model-panel/`](sources/model-panel/) and
[`sources/selection/`](sources/selection/).

For audit evidence, use the reviewer brief in
[`sources/reviews/protocols/marureview-brief-2026-05-26.md`](sources/reviews/protocols/marureview-brief-2026-05-26.md),
the raw RF/PW/PH review exports in [`sources/reviews/`](sources/reviews/), the three-reviewer
agreement report in [`reports/rf-pw-ph-2026-06-13/`](reports/rf-pw-ph-2026-06-13/), and the
machine-readable source manifest in [`sources/manifest.json`](sources/manifest.json).

The rebuild and verification entry points are in [`scripts/`](scripts/); the Python package they use
is in [`src/lexen/`](src/lexen/), and release-policy tests are in [`tests/`](tests/).

## Citation

If you use lexEN, cite this repository and the upstream Maru et al. 2022 benchmark:

```bibtex
@inproceedings{maru-etal-2022-nibbling,
  title = {Nibbling at the Hard Core of Word Sense Disambiguation},
  author = {Maru, Marco and Conia, Simone and Bevilacqua, Michele and Navigli, Roberto},
  booktitle = {Proceedings of the 60th Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers)},
  year = {2022},
  pages = {4724--4737}
}
```

Repository citation metadata is provided in [`CITATION.cff`](CITATION.cff).

## License

lexEN separates software licensing from dataset-artifact licensing.

The Python package metadata in [`pyproject.toml`](pyproject.toml) declares Apache-2.0 because the
installable package contains only build, verification, report-generation, and test software. The
software license is [`LICENSE-CODE`](LICENSE-CODE).

The dataset citation metadata in [`CITATION.cff`](CITATION.cff) uses CC-BY-NC-4.0 because the
benchmark artifacts include upstream Maru2022 data and are released for research / non-commercial
evaluation under source-package terms recorded in [`sources/manifest.json`](sources/manifest.json),
[`LICENSE`](LICENSE), and [`NOTICE`](NOTICE).

[Maru2022 ALLamended](sources/maru2022/original/details.json) is recorded as CC-BY-NC-4.0 in the
[source manifest](sources/manifest.json). The [Maru et al. paper files](sources/maru2022/papers/)
are recorded as CC-BY-4.0. Source-package hashes and terms are part of the
[release metadata](data/lexen-v1/dataset.json).

## Additional Documentation

* [`DATASHEET.md`](DATASHEET.md): dataset motivation, composition, collection, use, and maintenance.
* [`docs/provenance.md`](docs/provenance.md): end-to-end dataset lineage.
* [`docs/selection.md`](docs/selection.md): suspicious-item selection logic.
* [`docs/labeling-process.md`](docs/labeling-process.md): reviewer-facing labeling instructions.
* [`docs/review-protocol.md`](docs/review-protocol.md): three-reviewer label and removal policy.
* [`docs/reports.md`](docs/reports.md): agreement report contents.
* [`docs/schema.md`](docs/schema.md): canonical and export schemas.
* [`CHANGELOG.md`](CHANGELOG.md): release history.
* [`CONTRIBUTING.md`](CONTRIBUTING.md): issue and contribution process.
* [`CODE_OF_CONDUCT.md`](CODE_OF_CONDUCT.md): community conduct expectations.
* [`SECURITY.md`](SECURITY.md): sensitive-reporting process.
