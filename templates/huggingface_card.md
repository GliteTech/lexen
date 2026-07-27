---
pretty_name: lexEN
license: cc-by-nc-4.0
language:
- en
task_categories:
- token-classification
task_ids:
- word-sense-disambiguation
size_categories:
- 1K<n<10K
multilinguality:
- monolingual
annotations_creators:
- expert-generated
language_creators:
- found
source_datasets:
- extended|other-raganato-2017
- extended|other-maru-2022
tags:
- word-sense-disambiguation
- wsd
- wordnet
- lexical-semantics
- benchmark
- evaluation
- lexicography
- evaluation-only
configs:
- config_name: default
  data_files:
  - split: test
    path: data/items.jsonl
- config_name: reviews
  data_files:
  - split: test
    path: data/reviews.jsonl
---

# lexEN

A conservative, human-adjudicated **correction layer** over the standard English all-words word sense
disambiguation benchmark.

A panel of models flagged **{{REVIEWED_ITEMS}} contested items** in [Maru et al. 2022](https://github.com/SapienzaNLP/wsd-hard-benchmark)'s
ALL_NEW; three professional lexicographers adjudicated those items independently, **changing {{CHANGED_LABELS}} gold
labels and removing {{REMOVED_ITEMS}}**. The other **{{UNREVIEWED_ITEMS}} items carry their source labels unchanged** — they were
never reviewed, and lexEN makes no claim about them.

The complete review record is published alongside the data.

## Key facts

| | |
| --- | --- |
| Task | Word sense disambiguation, all-words, fine-grained |
| Modality | Text |
| Language | English |
| Domain | News, fiction and encyclopaedic prose (Senseval / SemEval source corpora) |
| Examples | {{TOTAL_ITEMS}} polysemous items, across 948 sentences and 23 documents |
| Splits | `test` only — this is an evaluation set, not training data |
| Sense inventory | WordNet 3.0 |
| Annotation | {{REVIEWED_ITEMS}} model-flagged items adjudicated by three professional lexicographers; {{UNREVIEWED_ITEMS}} items inherited unreviewed |
| Agreement | Fleiss κ {{FINE_KAPPA}} fine / {{COARSE_KAPPA}} coarse, over the {{REVIEWED_ITEMS}} reviewed items |
| Licence | **CC BY-NC 4.0** — research and non-commercial evaluation only |
| Version | `{{RELEASE_ID}}` |
| Leaderboard | <https://sense-bench.com> |
| Contact | <https://github.com/GliteTech/lexen/issues> |

## Quick start

```python
from datasets import load_dataset

items = load_dataset("GliteTech/lexen", split="test")
print(items[0])

# The per-item lexicographer record for the {{REVIEWED_ITEMS}} reviewed items
reviews = load_dataset("GliteTech/lexen", "reviews", split="test")
```

Pin a revision for reproducibility:

```python
items = load_dataset("GliteTech/lexen", split="test", revision="{{RELEASE_ID}}")
```

No authentication required. ~13 MB total.

## Dataset summary

lexEN is a conservative, fully traced correction layer over the standard English all-words WSD
evaluation framework — not a new corpus, and not a re-annotation of it. **Only {{REVIEWED_SHARE_PCT}}% of items ({{REVIEWED_ITEMS}} of
{{SOURCE_ITEMS}}) were seen by a human reviewer**; the rest are inherited unchanged.

It starts from [Raganato et al. 2017](http://lcl.uniroma1.it/wsdeval/), as corrected by
[Maru et al. 2022](https://github.com/SapienzaNLP/wsd-hard-benchmark), and adds one further round of
manual review. A panel of models flagged **{{REVIEWED_ITEMS}}** items where automatic predictions disagreed with the
source gold label. Three professional lexicographers then reviewed those items **independently** —
blind to the source label, to which system had flagged the item, and to one another's answers. A
two-of-three majority rule, **fixed before adjudication**, decided each case.

The rule never invents a label; it only ratifies or discards.

| Outcome | Items |
| --- | ---: |
| Retained, unanimous | {{RETAINED_UNANIMOUS}} |
| Retained, two-of-three | {{RETAINED_TWO_OF_THREE}} |
| Removed, two or more cannot-answer | {{REMOVED_CANNOT_ANSWER}} |
| Removed, no sense consensus | {{REMOVED_NO_CONSENSUS}} |
| **Gold labels changed vs source** | **{{CHANGED_LABELS}}** |

The release is those {{RETAINED_TOTAL}} retained items plus {{UNREVIEWED_ITEMS}} unreviewed items carrying their source label
unchanged, for {{TOTAL_ITEMS}} in total.

## Inter-annotator agreement

Computed over the {{REVIEWED_ITEMS}} reviewed items from the three lexicographers' raw choices — not over the
released set, most of which no reviewer saw. This is the number most likely to be useful to other
researchers.

| Granularity | Three-way agreement | Fleiss κ |
| --- | ---: | ---: |
| WordNet fine-grained | {{FINE_AGREEMENT_PCT}}% | **{{FINE_KAPPA}}** |
| Coarse sense grouping | {{COARSE_AGREEMENT_PCT}}% | **{{COARSE_KAPPA}}** |

Three professional lexicographers, one shared brief, the same items — and only moderate agreement at
fine granularity. **{{NON_UNANIMOUS_RESOLVED_PCT}}%** of the items they disagreed on become unanimous once over-specified sense
distinctions are collapsed.

A share of what is normally reported as WSD *system* error is disagreement about the sense inventory
rather than about the word. The per-item choices are in the `reviews` config, so this is auditable
rather than asserted.

## Dataset structure

### Example instance

```json
{
  "item_id": "senseval2.d000.s000.t000",
  "lemma": "art",
  "pos": "NOUN",
  "target_text": "art",
  "sentences": [["The", "art", "of", "change-ringing", "is", "peculiar", "to", "the", "English", "."]],
  "sentence_index": 0,
  "sentence_id": "senseval2.d000.s000",
  "document_id": "senseval2.d000",
  "target_token_index": 1,
  "gold_sense_keys": ["art%1:09:00::"],
  "metadata": {"label_set": "lexen_gold", "dataset_canary": "lexen-canary-v1-..."}
}
```

### Data fields

* `item_id` — stable identifier, unique within this release. Inherited from the source framework, so
  it is comparable across Raganato, Maru and lexEN.
* `lemma` — the lemma of the target word.
* `pos` — part of speech: `NOUN`, `VERB`, `ADJ` or `ADV`.
* `target_text` — the surface form of the target token as it appears in the sentence.
* `sentences` — a context window as a list of token lists. Tokens are pre-tokenised, not raw text.
* `sentence_index` — zero-based index into `sentences` identifying which one contains the target.
* `sentence_id`, `document_id` — provenance within the source corpus.
* `target_token_index` — **zero-based** index of the target token within its sentence.
* `gold_sense_keys` — list of correct WordNet 3.0 sense keys. Usually one; a small number of items
  carry more where the reviewers judged the context genuinely ambiguous.
* `metadata` — label set, adjudication decision, and the contamination canary.

Candidate senses are not stored per item: they are derived from WordNet 3.0 for the given `lemma`
and `pos`, so the candidate set is whatever the installed WordNet returns.

### The `reviews` config

One record per reviewed item ({{REVIEWED_ITEMS}}), carrying each reviewer's choice, any typed cannot-answer flag,
free-text rationale, and the adjudicated consensus.

### Splits

A single `test` split. There is deliberately no train split — lexEN is an evaluation set, and its
source corpora are the standard held-out WSD test sets. Systems are conventionally trained on SemCor,
which is disjoint from these items.

## Additional formats

| Path | What it is |
| --- | --- |
| `data/items.jsonl` | The {{TOTAL_ITEMS}} items. Default config. |
| `data/reviews.jsonl` | Per-item reviewer choices for the {{REVIEWED_ITEMS}} reviewed items. |
| `raganato/{{RELEASE_ID}}.data.xml` | Standard Raganato-format XML, for existing WSD tooling. |
| `raganato/{{RELEASE_ID}}.gold.key.txt` | Standard gold key file. |
| `raganato/{{RELEASE_ID}}.removed.json` | The {{REMOVED_ITEMS}} removed items, each with its removal reason. |
| `DATASHEET.md` | Datasheet for the dataset. |

The Raganato-format files let existing WSD evaluation scripts run against lexEN unchanged.

## Evaluation

`data/items.jsonl` here is byte-identical to the file the [SenseBench](https://sense-bench.com)
leaderboard scores against — SHA-256 `{{ITEMS_SHA256}}`
— so results published there apply to this copy without qualification.

```bash
pip install sensebench
sensebench run --model <model> --prompt p001 --github-handle <you>
sensebench verify runs/<run-id> --dataset lexen-v1 --prompt p001
```

The metric is accuracy over items: a prediction is correct when the predicted sense key is in
`gold_sense_keys`. The leaderboard additionally reports bootstrap confidence intervals, rank ranges
and paired McNemar tests, and scores classic supervised systems (MFS, BEM, ESCHER, ConSeC) on
identical items for reference.

Accuracy on this dataset is meaningful only alongside its sense granularity: the same run can score
around ten points differently under fine and coarse inventories. State the label scheme with any
number you report.

## Contamination

Every item carries a canary string in `metadata.dataset_canary`:

```
{{DATASET_CANARY}}
```

If a model reproduces that string, it was trained on this file. **Please do not strip it when
redistributing, and please exclude lexEN from pretraining corpora.**

The source corpora predate lexEN and are long public, so contamination of the *underlying text* must
be assumed. The {{CHANGED_LABELS}} corrected labels, however, did not exist before this release, which makes them a
usable probe: a model echoing memorised gold would score worse on the changed items than on the
unchanged ones.

## Intended uses

* Evaluating word sense disambiguation in language models and supervised systems
* Studying the granularity of the WordNet sense inventory and its effect on measured accuracy
* Research on annotation quality and inter-annotator disagreement in lexical semantics
* Reproducing results published on the SenseBench leaderboard

## Out-of-scope uses

* **Training.** This is an evaluation set; training on it invalidates it for everyone.
* **Commercial use.** The licence does not permit it — see below.
* Claiming corpus-wide error rates for the source benchmarks (see Limitations).
* Comparing scores across different sense granularities or gold-label schemes as if commensurable.
* Treating the coarse-grained sense mapping as an independent standard — it was developed by the same
  authors.

## Limitations

* **The reviewed subset is model-selected, not random.** Every item a lexicographer saw was flagged
  for disagreeing with the source label. No claim is made about a corpus-wide error rate: the {{CHANGED_LABELS}}
  changed labels are a property of the contested items examined, not an extrapolation to the {{UNREVIEWED_ITEMS}}
  that were not reviewed.
* **Fine WordNet granularity bounds what any of these numbers mean.** Expert agreement is κ {{FINE_KAPPA}}.
  Scores near the top of the leaderboard sit inside the band where lexicographers themselves disagree.
* **Coarse results depend on a sense map we developed**, which ships with
  [SenseBench](https://github.com/GliteTech/sensebench) rather than with this dataset. It is released
  in full, alongside a third-party coarse inventory (CSI), so coarse numbers can be reproduced or
  replaced.
* **English only**, and only the written registers of the Senseval and SemEval source corpora — news,
  fiction and encyclopaedic prose. Nothing here supports claims about conversational speech, learner
  English or social-media varieties.
* **Small.** {{TOTAL_ITEMS}} items over 948 sentences. Differences of a few tenths of a point are unlikely to
  be meaningful; use the paired tests.
* The {{REMOVED_NO_CONSENSUS}} items removed for three-way disagreement are documented rather than silently dropped, and
  are worth reading before treating any WSD gold standard as definitive.

## Personal and sensitive information

lexEN contains no personal or sensitive information beyond what is present in the long-published
Senseval and SemEval source corpora, which are edited news, fiction and encyclopaedic prose. No
personal data was collected for this release. Reviewer identities are published with their consent as
part of the provenance record; no other annotator information is included.

## Licensing

Three levels, which are not the same:

1. **Dataset artifacts — CC BY-NC 4.0.** Inherited from Maru et al. 2022; released for research use
   and non-commercial evaluation only. This is not ours to relicense.
2. **Upstream source content** retains its own terms. The Raganato 2017 framework and the Senseval /
   SemEval corpora carry their original conditions.
3. **Build, verification and evaluation software — Apache-2.0**, in the
   [lexEN](https://github.com/GliteTech/lexen) and
   [SenseBench](https://github.com/GliteTech/sensebench) repositories.

Where a form accepts one licence identifier for the dataset, the answer is `cc-by-nc-4.0`.

## Versioning

Current version: **`{{RELEASE_ID}}`**.

Releases are immutable. Dataset artifacts are pinned by SHA-256 in `sources/manifest.json` and
`data/lexen-v1/dataset.json` in the source repository, and verified in CI. A future `lexen-v2` will
be a separate release rather than an edit to this one, so published scores remain comparable to the
version they were measured on.

## Citation

```bibtex
@misc{lexen2026,
  title  = {lexEN: A Lexicographer-Reviewed English Word Sense Disambiguation Evaluation Set},
  author = {Philippov, Vassili and {Glite Tech Ltd}},
  year   = {2026},
  url    = {https://github.com/GliteTech/lexen}
}
```

Please also cite the work this builds on:

```bibtex
@inproceedings{maru-etal-2022-nibbling,
  title     = {Nibbling at the Hard Core of Word Sense Disambiguation},
  author    = {Maru, Marco and Conia, Simone and Bevilacqua, Michele and Navigli, Roberto},
  booktitle = {Proceedings of the 60th Annual Meeting of the Association for Computational Linguistics},
  year      = {2022}
}

@inproceedings{raganato-etal-2017-word,
  title     = {Word Sense Disambiguation: A Unified Evaluation Framework and Empirical Comparison},
  author    = {Raganato, Alessandro and Camacho-Collados, Jose and Navigli, Roberto},
  booktitle = {Proceedings of EACL},
  year      = {2017}
}
```

## Links

* Source repository, with the full review record: <https://github.com/GliteTech/lexen>
* Leaderboard: <https://sense-bench.com>
* Evaluation harness: <https://github.com/GliteTech/sensebench> — `pip install sensebench`
