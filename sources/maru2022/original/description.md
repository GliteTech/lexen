---
spec_version: "1"
dataset_id: "maru2022-allamended"
source_package_described_at: "2026-03-31"
---

# Maru 2022 ALLamended (ALL_NEW)

## Metadata

* **Name**: Maru 2022 ALLamended (ALL_NEW)
* **Year**: 2022
* **Authors**: Marco Maru, Simone Conia, Michele Bevilacqua,
  Roberto Navigli
* **License**: CC-BY-NC-4.0
* **Access**: public
* **Size**: 4,917 sense-annotated instances across 1,038 sentences from
  4 Raganato datasets with corrected annotations

## Overview

ALLamended (referred to as ALL_NEW in the paper) is a corrected and
amended version of the Raganato ALL concatenation. Maru et al. (2022)
systematically re-annotated the standard evaluation datasets, identifying
and fixing annotation errors in the original gold keys. The re-annotation
found that **72.6%** of instances had unchanged annotations, **9.4%**
had fine-grained sense distinctions updated, **8.0%** had outright sense
errors, **6.8%** had inventory gaps (senses not in WordNet 3.0), **2.9%**
had token/lemma errors, and **0.3%** had POS errors.

A critical difference from the original Raganato ALL: ALLamended excludes
SemEval-2007 (455 instances), which is commonly used as a development
set. This means ALLamended concatenates only Senseval-2, Senseval-3,
SemEval-2013, and SemEval-2015. The exclusion of SE07 and the annotation
corrections mean ALLamended (4,917 instances) is not directly comparable
to the original ALL (7,253 instances).

## Content & Annotation

Each instance is annotated with corrected WordNet 3.0 sense keys in
Raganato XML format. The annotations were produced through a systematic
re-annotation process using six labels: unchanged, fine-grained,
error:token-lemma, error:pos, error:sense, and error:inventory. Instances
with errors were either corrected or removed from the dataset.

POS distribution: **2,921 nouns** (59.4%), **1,130 verbs** (23.0%),
**670 adjectives** (13.6%), **196 adverbs** (4.0%).

## Statistics

| Metric            | Value |
|-------------------|-------|
| Instances         | 4,917 |
| Sentences         | 1,038 |
| Unique lemmas     | 1,701 |
| Unique sense keys | 2,573 |

| POS       | Count | Percentage |
|-----------|-------|------------|
| NOUN      | 2,921 | 59.4%      |
| VERB      | 1,130 | 23.0%      |
| ADJ       | 670   | 13.6%      |
| ADV       | 196   | 4.0%       |

### Source Dataset Composition

ALLamended concatenates 4 of the 5 standard Raganato datasets:

| Source Dataset   | Included |
|------------------|----------|
| Senseval-2       | yes      |
| Senseval-3       | yes      |
| SemEval-2007     | **no** (used as dev set) |
| SemEval-2013     | yes      |
| SemEval-2015     | yes      |

## Usage Notes

The dataset uses the same Raganato XML format as standard evaluation
datasets. Load `files/ALLamended.data.xml` for the corpus and
`files/ALLamended.gold.key.txt` for gold annotations. The filenames match
the upstream Maru repository.

When comparing results against the original Raganato ALL, note two
sources of difference: (1) annotation corrections change the gold
standard, and (2) SemEval-2007 exclusion removes 455 instances.
Published results on "ALL_NEW" or "ALLamended" should not be directly
compared to results on the original "ALL" without accounting for these
differences.

The repository uses "ALLamended" as the folder and file name, while the
paper and subsequent literature refer to this dataset as "ALL_NEW".

## Main Ideas

* Provides a corrected version of the standard Raganato benchmark,
  fixing **~18%** of annotations that were erroneous or needed updating
* Excludes SemEval-2007 (used as dev set), so results are not directly
  comparable to original Raganato ALL
* The annotation correction rates reveal that published benchmark results
  on the original datasets have a noise floor of **~18%** annotation
  uncertainty

## Summary

ALLamended provides 4,917 corrected WSD instances from four Raganato
evaluation datasets (excluding SemEval-2007). It addresses systematic
annotation errors in the original benchmark, with corrections affecting
approximately 18% of instances.

In lexEN, ALLamended serves as the base benchmark. Results on ALLamended are more reliable than on
the original ALL because many annotation errors were corrected by Maru et al. Cross-study comparison
requires care because much prior work reports results on the uncorrected ALL.
