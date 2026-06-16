# lexEN v1 Three-Reviewer Agreement Report

Report date: 2026-06-13. Maru2022 labels are source labels under review.

This report audits the 363 Maru2022 validation items flagged by the S1-S6 model-panel waterfall for
lexicographer review. The items were reviewed independently by three professional lexicographers
using the same marureview.com brief. The report is generated from the Maru2022 source copy, the
suspicious-item selection package, the RF/PW/PH review JSON files, and the Glite coarsening map.

## Contents

* [What This Report Includes](#what-this-report-includes)
* [How To Read The Numbers](#how-to-read-the-numbers)
* [Headline Agreement](#headline-agreement)
* [Maru2022 Label Support Split](#maru2022-label-support-split)
* [Pairwise Agreement](#pairwise-agreement)
* [Reviewer Answer Shape](#reviewer-answer-shape)
* [Glite Coarsening Effect](#glite-coarsening-effect)
* [Disagreement Concentration](#disagreement-concentration)
* [Cannot-Answer Reasons](#cannot-answer-reasons)
* [Removed Reviewed Items](#removed-reviewed-items)
* [What The Agreement Shows](#what-the-agreement-shows)
* [Technical Method](#technical-method)
* [Full Item Appendix](#full-item-appendix)
  * [A. All three reviewers selected the Maru2022 sense](#appendix-a)
  * [B. All three reviewers selected the same correction](#appendix-b)
  * [C. All three reviewers judged the item unanswerable](#appendix-c)
  * [D. Two reviewers selected the same sense](#appendix-d)
  * [E. Two reviewers judged the item unanswerable](#appendix-e)
  * [F. All three reviewers disagreed](#appendix-f)

## What This Report Includes

* Fine WordNet agreement among RF, PW, and PH.
* The same agreement analysis after Glite coarsening of WordNet senses.
* Pairwise raw agreement, Cohen's kappa for each reviewer pair, and Fleiss kappa.
* The split of reviewer support for the Maru2022 source label.
* Reviewer-level answer shape: single-sense, multi-sense, cannot-answer, comments, and notes.
* Concentration by part of speech, source dataset, and frequent headword.
* Cannot-answer reason tags and defective-input concentration by document.
* A complete appendix with all 363 reviewed items, reviewer choices, notes, comments, and WordNet
  definitions.

## How To Read The Numbers

Fine WordNet agreement compares the exact WordNet sense-key sets chosen by the reviewers. Glite
agreement first maps those sense keys to Glite coarse concepts, so two different WordNet senses can
agree at the coarse concept level. Maru2022 support counts how many reviewers selected the Maru2022
source label for an item; it does not treat Maru2022 as a privileged adjudication.

## Headline Agreement

| Metric | Fine WordNet | Glite coarse |
| --- | --- | --- |
| All three agree | 129 (35.5%) | 229 (63.1%) |
| Exactly two agree | 205 (56.5%) | 124 (34.2%) |
| All three disagree | 29 (8.0%) | 10 (2.8%) |
| All three agree and match Maru2022 | 40 (11.0%) | 196 (54.0%) |
| Exactly two agree and match Maru2022 | 56 (15.4%) | 54 (14.9%) |
| Fleiss kappa | 0.537 | 0.740 |

Fine-grained agreement is strong for a set that was deliberately selected to be suspicious: all
three reviewers agree on 129 (35.5%) items, and exactly two agree on 205 (56.5%). Coarsening
resolves many apparent sense-key splits: Glite all-three agreement rises to 229 (63.1%).

## Agreement Pattern Relative To Maru2022

| Pattern | Fine WordNet | Glite coarse |
| --- | --- | --- |
| All three agree and match Maru2022 | 40 (11.0%) | 196 (54.0%) |
| All three agree, different from Maru2022 | 89 (24.5%) | 33 (9.1%) |
| Exactly two agree and match Maru2022 | 56 (15.4%) | 54 (14.9%) |
| Exactly two agree, different from Maru2022 | 149 (41.0%) | 70 (19.3%) |
| All three disagree | 29 (8.0%) | 10 (2.8%) |

This table explains why labels changed. At the fine level, 89 (24.5%) items have unanimous reviewer
agreement on a label different from Maru2022, and 149 (41.0%) have a two-reviewer majority different
from Maru2022. Those are the main sources of lexEN corrections. The no-consensus group is removed
from the benchmark because it does not provide enough reviewer agreement to assign a reliable
replacement.

## Maru2022 Label Support Split

| Support | Fine WordNet | Glite coarse |
| --- | --- | --- |
| 3/3 reviewers selected the Maru2022 label | 40 (11.0%) | 196 (54.0%) |
| 2/3 reviewers selected the Maru2022 label | 56 (15.4%) | 54 (14.9%) |
| 1/3 reviewers selected the Maru2022 label | 96 (26.4%) | 47 (12.9%) |
| 0/3 reviewers selected the Maru2022 label | 171 (47.1%) | 66 (18.2%) |

Only 40 (11.0%) fine-grained items received three-reviewer support for the Maru2022 label. At the
Glite level, 196 (54.0%) receive three-reviewer support, showing that many disagreements are between
closely related fine WordNet senses rather than between clearly different coarse meanings.

## Pairwise Agreement

Each 3x3 matrix cell compares the row reviewer with the column reviewer. Raw agreement cells show
the percentage and the matching-item count. Diagonal cells are self-comparisons included only to
keep the reviewer grid explicit.

### Fine Raw Agreement Matrix

| Reviewer | RF | PW | PH |
| --- | --- | --- | --- |
| RF | 100.0% (363/363) | 57.3% (208/363) | 46.8% (170/363) |
| PW | 57.3% (208/363) | 100.0% (363/363) | 59.0% (214/363) |
| PH | 46.8% (170/363) | 59.0% (214/363) | 100.0% (363/363) |

### Glite Raw Agreement Matrix

| Reviewer | RF | PW | PH |
| --- | --- | --- | --- |
| RF | 100.0% (363/363) | 75.5% (274/363) | 68.9% (250/363) |
| PW | 75.5% (274/363) | 100.0% (363/363) | 79.1% (287/363) |
| PH | 68.9% (250/363) | 79.1% (287/363) | 100.0% (363/363) |

### Fine Cohen's Kappa Matrix

| Reviewer | RF | PW | PH |
| --- | --- | --- | --- |
| RF | 1.000 | 0.567 | 0.461 |
| PW | 0.567 | 1.000 | 0.585 |
| PH | 0.461 | 0.585 | 1.000 |

### Glite Cohen's Kappa Matrix

| Reviewer | RF | PW | PH |
| --- | --- | --- | --- |
| RF | 1.000 | 0.751 | 0.683 |
| PW | 0.751 | 1.000 | 0.788 |
| PH | 0.683 | 0.788 | 1.000 |

### Compact Pairwise Summary

| Pair | Fine raw | Fine kappa | Glite raw | Glite kappa |
| --- | --- | --- | --- | --- |
| RF + PW | 57.3% (208/363) | 0.567 | 75.5% (274/363) | 0.751 |
| RF + PH | 46.8% (170/363) | 0.461 | 68.9% (250/363) | 0.683 |
| PW + PH | 59.0% (214/363) | 0.585 | 79.1% (287/363) | 0.788 |

Pairwise coefficients are reported for both granularities. Raw agreement is the direct share of
matching labels. Cohen's kappa corrects for the label distribution in each pair, which matters
because cannot-answer and high-frequency senses are not evenly distributed across the reviewed set.

## Reviewer Answer Shape

| Reviewer | Single | Multi | Cannot | Comments | Notes |
| --- | --- | --- | --- | --- | --- |
| Robert Farren (RF) | 309 | 5 | 49 | 36 | 49 |
| Patrick White (PW) | 316 | 18 | 29 | 33 | 29 |
| Penny Hands (PH) | 312 | 20 | 31 | 171 | 31 |

These counts are behavior diagnostics, not quality rankings. Multi-sense answers capture cases where
a lexicographer judged several WordNet keys acceptable. Cannot-answer tags capture source-text
defects, inventory gaps, and cases where no listed sense applied.

## How Each Reviewer Related To Maru2022

### Fine WordNet

| Relation | Robert Farren | Patrick White | Penny Hands |
| --- | --- | --- | --- |
| Selected exactly the Maru2022 label | 119 (32.8%) | 114 (31.4%) | 95 (26.2%) |
| Selected Maru2022 plus extra sense(s) | 4 (1.1%) | 18 (5.0%) | 19 (5.2%) |
| Selected different sense(s) | 174 (47.9%) | 190 (52.3%) | 205 (56.5%) |
| Partially overlapped Maru2022 | 17 (4.7%) | 12 (3.3%) | 13 (3.6%) |
| Marked cannot answer | 49 (13.5%) | 29 (8.0%) | 31 (8.5%) |

### Glite Coarse

| Relation | Robert Farren | Patrick White | Penny Hands |
| --- | --- | --- | --- |
| Selected exactly the Maru2022 label | 246 (67.8%) | 252 (69.4%) | 245 (67.5%) |
| Selected Maru2022 plus extra sense(s) | 2 (0.6%) | 2 (0.6%) | 2 (0.6%) |
| Selected different sense(s) | 53 (14.6%) | 71 (19.6%) | 74 (20.4%) |
| Partially overlapped Maru2022 | 13 (3.6%) | 9 (2.5%) | 11 (3.0%) |
| Marked cannot answer | 49 (13.5%) | 29 (8.0%) | 31 (8.5%) |

## Glite Coarsening Effect

Glite coarsening resolves 100 (42.7%) of fine-grained non-unanimous cases into all-three agreement.
The report needed 465 distinct WordNet sense keys and mapped 454 of them. Unmapped keys are
preserved as explicit `unmapped:<sense_key>` concepts rather than silently dropped.

## Disagreement Concentration

### Part Of Speech

| POS | Items | Fine all 3 | Fine 2/3 | Fine differ | Glite all 3 | Glite 2/3 | Glite differ |
| --- | --- | --- | --- | --- | --- | --- | --- |
| NOUN | 206 | 76 (36.9%) | 119 (57.8%) | 11 (5.3%) | 129 (62.6%) | 72 (35.0%) | 5 (2.4%) |
| VERB | 91 | 27 (29.7%) | 52 (57.1%) | 12 (13.2%) | 61 (67.0%) | 26 (28.6%) | 4 (4.4%) |
| ADJ | 49 | 16 (32.7%) | 27 (55.1%) | 6 (12.2%) | 27 (55.1%) | 21 (42.9%) | 1 (2.0%) |
| ADV | 17 | 10 (58.8%) | 7 (41.2%) | 0 (0.0%) | 12 (70.6%) | 5 (29.4%) | 0 (0.0%) |

### Source Dataset

| Source | Items | Fine all 3 | Fine 2/3 | Fine differ | Glite all 3 | Glite 2/3 | Glite differ |
| --- | --- | --- | --- | --- | --- | --- | --- |
| senseval2 | 132 | 39 (29.5%) | 82 (62.1%) | 11 (8.3%) | 78 (59.1%) | 51 (38.6%) | 3 (2.3%) |
| senseval3 | 109 | 34 (31.2%) | 65 (59.6%) | 10 (9.2%) | 68 (62.4%) | 39 (35.8%) | 2 (1.8%) |
| semeval2013 | 70 | 32 (45.7%) | 34 (48.6%) | 4 (5.7%) | 45 (64.3%) | 22 (31.4%) | 3 (4.3%) |
| semeval2015 | 52 | 24 (46.2%) | 24 (46.2%) | 4 (7.7%) | 38 (73.1%) | 12 (23.1%) | 2 (3.8%) |

### Frequent Headwords In The Reviewed Set

| Headword | Items | Fine all 3 | Fine 2/3 | Fine differ | Glite all 3 | Glite 2/3 | Glite differ |
| --- | --- | --- | --- | --- | --- | --- | --- |
| say | 17 | 1 (5.9%) | 15 (88.2%) | 1 (5.9%) | 16 (94.1%) | 1 (5.9%) | 0 (0.0%) |
| thing | 7 | 0 (0.0%) | 6 (85.7%) | 1 (14.3%) | 1 (14.3%) | 5 (71.4%) | 1 (14.3%) |
| benefit | 6 | 5 (83.3%) | 1 (16.7%) | 0 (0.0%) | 5 (83.3%) | 1 (16.7%) | 0 (0.0%) |
| growth | 6 | 0 (0.0%) | 6 (100.0%) | 0 (0.0%) | 0 (0.0%) | 6 (100.0%) | 0 (0.0%) |
| level | 6 | 0 (0.0%) | 6 (100.0%) | 0 (0.0%) | 6 (100.0%) | 0 (0.0%) | 0 (0.0%) |
| u.s. | 6 | 5 (83.3%) | 1 (16.7%) | 0 (0.0%) | 5 (83.3%) | 1 (16.7%) | 0 (0.0%) |
| field | 5 | 4 (80.0%) | 1 (20.0%) | 0 (0.0%) | 5 (100.0%) | 0 (0.0%) | 0 (0.0%) |
| state | 5 | 4 (80.0%) | 1 (20.0%) | 0 (0.0%) | 4 (80.0%) | 1 (20.0%) | 0 (0.0%) |
| study | 5 | 2 (40.0%) | 3 (60.0%) | 0 (0.0%) | 2 (40.0%) | 3 (60.0%) | 0 (0.0%) |
| believe | 4 | 1 (25.0%) | 2 (50.0%) | 1 (25.0%) | 2 (50.0%) | 2 (50.0%) | 0 (0.0%) |
| call | 4 | 1 (25.0%) | 3 (75.0%) | 0 (0.0%) | 4 (100.0%) | 0 (0.0%) | 0 (0.0%) |
| function | 4 | 0 (0.0%) | 4 (100.0%) | 0 (0.0%) | 4 (100.0%) | 0 (0.0%) | 0 (0.0%) |
| loss | 4 | 0 (0.0%) | 4 (100.0%) | 0 (0.0%) | 0 (0.0%) | 4 (100.0%) | 0 (0.0%) |
| public | 4 | 0 (0.0%) | 4 (100.0%) | 0 (0.0%) | 2 (50.0%) | 2 (50.0%) | 0 (0.0%) |
| attendance | 3 | 0 (0.0%) | 3 (100.0%) | 0 (0.0%) | 3 (100.0%) | 0 (0.0%) | 0 (0.0%) |
| bell | 3 | 0 (0.0%) | 3 (100.0%) | 0 (0.0%) | 0 (0.0%) | 3 (100.0%) | 0 (0.0%) |
| child | 3 | 0 (0.0%) | 3 (100.0%) | 0 (0.0%) | 3 (100.0%) | 0 (0.0%) | 0 (0.0%) |
| cost | 3 | 1 (33.3%) | 2 (66.7%) | 0 (0.0%) | 1 (33.3%) | 2 (66.7%) | 0 (0.0%) |
| country | 3 | 1 (33.3%) | 2 (66.7%) | 0 (0.0%) | 3 (100.0%) | 0 (0.0%) | 0 (0.0%) |
| development | 3 | 2 (66.7%) | 1 (33.3%) | 0 (0.0%) | 2 (66.7%) | 1 (33.3%) | 0 (0.0%) |

## Cannot-Answer Reasons

At least one reviewer marked 77 items unanswerable. All three reviewers marked 5 items unanswerable.

| Reason | RF | PW | PH |
| --- | --- | --- | --- |
| input defective | 2 | 6 | 2 |
| inventory inadequate | 6 | 12 | 20 |
| no sense applies | 45 | 11 | 10 |

### Cannot-Answer Consensus

| Consensus strength | Items |
| --- | --- |
| Exactly one reviewer marked cannot answer | 50 (13.8%) |
| Exactly two reviewers marked cannot answer | 22 (6.1%) |
| All three reviewers marked cannot answer | 5 (1.4%) |
| At least two reviewers marked cannot answer | 27 (7.4%) |

The strongest unusable-item signal is the at-least-two-reviewer subset: 27 (7.4%) items have at
least two independent cannot-answer judgements. This includes 22 exactly-two cases and 5 all-three
cases. These are not ordinary sense disagreements; they indicate that the item, context, or
available WordNet inventory did not support a reliable fine-grained answer.

| Reason present in at-least-two subset | Items |
| --- | --- |
| input defective | 6 (1.7%) |
| inventory inadequate | 18 (5.0%) |
| no sense applies | 24 (6.6%) |

### Cannot-Answer By Document And Reviewer Support

This table shows document concentration for items where at least two reviewers marked cannot answer,
split into exactly-two and all-three reviewer support.

| Reviewer support | Document | Items |
| --- | --- | --- |
| 2/3 reviewers | semeval2013.d006 | 4 |
| 2/3 reviewers | semeval2013.d009 | 1 |
| 2/3 reviewers | semeval2013.d011 | 1 |
| 2/3 reviewers | semeval2015.d001 | 2 |
| 2/3 reviewers | senseval2.d000 | 1 |
| 2/3 reviewers | senseval2.d002 | 2 |
| 2/3 reviewers | senseval3.d000 | 5 |
| 2/3 reviewers | senseval3.d001 | 2 |
| 2/3 reviewers | senseval3.d002 | 4 |
| 3/3 reviewers | semeval2013.d006 | 1 |
| 3/3 reviewers | semeval2013.d011 | 1 |
| 3/3 reviewers | senseval2.d002 | 2 |
| 3/3 reviewers | senseval3.d000 | 1 |

### Defective Source Text

Input-defective tags identify cases where the sentence, tokenization, target span, or source
material prevents a reliable WSD judgement. This table is split by how many reviewers used the
input-defective reason; it is not limited to unanimous cases.

| Reviewer support | Document | Items |
| --- | --- | --- |
| 1/3 reviewers | semeval2013.d006 | 5 |
| 1/3 reviewers | semeval2015.d001 | 1 |
| 2/3 reviewers | semeval2013.d006 | 1 |
| 2/3 reviewers | semeval2013.d011 | 1 |
| 3/3 reviewers | None | 0 |

## Removed Reviewed Items

lexEN v1 removes reviewed suspicious items when the review evidence does not provide a usable
two-reviewer fine-grained sense label. No Maru2022 fallback label is used for these cases in the
benchmark exports.

| Removal evidence | Items | Benchmark action |
| --- | --- | --- |
| Two or three reviewers marked cannot answer | 27 | Removed from lexEN benchmark |
| No fine-grained sense received two-reviewer support | 29 | Removed from lexEN benchmark |
| Total reviewed items removed | 56 | No Maru2022 fallback label is used |

### No Two-Reviewer Fine Agreement

The 29 no-consensus items are removed because all three reviewers selected different fine-grained
answers. Some become closer after Glite coarsening, but lexEN v1 is a fine-grained WordNet
benchmark, so coarse agreement is not enough to keep a scorable item.

| Group | Items |
| --- | --- |
| Total no-consensus items | 29 |
| POS: ADJ | 6 |
| POS: NOUN | 11 |
| POS: VERB | 12 |
| Source: semeval2013 | 4 |
| Source: semeval2015 | 4 |
| Source: senseval2 | 11 |
| Source: senseval3 | 10 |

| Signal | Items |
| --- | --- |
| Fine Maru2022 support: 0/3 | 9 |
| Fine Maru2022 support: 1/3 | 20 |
| Glite Maru2022 support: 0/3 | 2 |
| Glite Maru2022 support: 1/3 | 8 |
| Glite Maru2022 support: 2/3 | 13 |
| Glite Maru2022 support: 3/3 | 6 |
| Glite reviewer agreement: All three agree | 6 |
| Glite reviewer agreement: All three disagree | 10 |
| Glite reviewer agreement: Exactly two agree | 13 |

| Reviewer evidence | Items |
| --- | --- |
| Cannot-answer votes: 0/3 reviewers | 10 |
| Cannot-answer votes: 1/3 reviewers | 19 |
| Reviewer comments on item: 0 | 7 |
| Reviewer comments on item: 1 | 18 |
| Reviewer comments on item: 2 | 4 |
| Cannot-answer notes on item: 0 | 10 |
| Cannot-answer notes on item: 1 | 19 |

### No-Consensus Item Audit

| Item | Lemma/POS/source | Fine Maru support | Glite level | Glite Maru support | Cannot votes | RF | PW | PH |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| semeval2013.d000.s019.t000 | game / NOUN / semeval2013 | 1/3 | All three disagree | 1/3 | 1 | Cannot answer: no sense applies | game%1:04:00:: | game%1:09:00:: |
| semeval2013.d002.s012.t000 | treasury / NOUN / semeval2013 | 0/3 | All three disagree | 0/3 | 0 | treasury%1:14:01:: | treasury%1:21:01:: | treasury%1:14:00:: |
| semeval2013.d005.s005.t001 | court / NOUN / semeval2013 | 1/3 | All three agree | 3/3 | 0 | court%1:06:05:: | court%1:06:05::, court%1:14:00:: | court%1:14:00:: |
| semeval2013.d009.s022.t000 | conservative / NOUN / semeval2013 | 1/3 | All three disagree | 1/3 | 1 | Cannot answer: no sense applies | conservative%1:18:00:: | conservative%1:18:01:: |
| semeval2015.d001.s009.t007 | input / NOUN / semeval2015 | 1/3 | All three disagree | 1/3 | 1 | input%1:06:00:: | Cannot answer: no sense applies | input%1:10:00:: |
| semeval2015.d002.s011.t008 | organisation / NOUN / semeval2015 | 0/3 | Exactly two agree | 2/3 | 0 | organisation%1:14:01:: | organisation%1:14:00:: | organisation%1:04:01:: |
| semeval2015.d003.s009.t014 | follow / VERB / semeval2015 | 1/3 | All three agree | 3/3 | 0 | follow%2:42:03:: | follow%2:42:01:: | follow%2:42:00:: |
| semeval2015.d003.s012.t002 | act / VERB / semeval2015 | 1/3 | All three disagree | 1/3 | 1 | Cannot answer: no sense applies | act%2:41:06:: | act%2:41:00:: |
| senseval2.d001.s009.t002 | make / VERB / senseval2 | 0/3 | All three disagree | 1/3 | 1 | make%2:36:00:: | make%2:36:01:: | Cannot answer: inventory inadequate |
| senseval2.d001.s013.t004 | believe / VERB / senseval2 | 0/3 | Exactly two agree | 2/3 | 1 | Cannot answer: no sense applies | believe%2:31:04:: | believe%2:31:00:: |
| senseval2.d001.s015.t001 | make / VERB / senseval2 | 0/3 | All three disagree | 1/3 | 1 | make%2:36:00:: | make%2:36:01:: | Cannot answer: inventory inadequate |
| senseval2.d001.s026.t007 | fundamental / ADJ / senseval2 | 0/3 | All three agree | 3/3 | 0 | fundamental%5:00:00:basic:00, fundamental%5:00:00:significant:00 | fundamental%5:00:00:significant:00 | fundamental%5:00:00:basic:00 |
| senseval2.d001.s041.t005 | specific / ADJ / senseval2 | 1/3 | Exactly two agree | 2/3 | 1 | Cannot answer: no sense applies | specific%5:00:00:specified:00 | specific%3:00:00:: |
| senseval2.d001.s057.t002 | attention / NOUN / senseval2 | 1/3 | Exactly two agree | 2/3 | 1 | Cannot answer: no sense applies | attention%1:09:01:: | attention%1:09:00:: |
| senseval2.d001.s086.t008 | think / VERB / senseval2 | 1/3 | Exactly two agree | 2/3 | 1 | Cannot answer: no sense applies | think%2:31:03:: | think%2:31:01:: |
| senseval2.d002.s003.t007 | metaphysical / ADJ / senseval2 | 1/3 | All three disagree | 1/3 | 1 | Cannot answer: no sense applies | metaphysical%3:01:00:: | metaphysical%5:00:00:theoretical:00 |
| senseval2.d002.s004.t002 | dominate / VERB / senseval2 | 1/3 | Exactly two agree | 2/3 | 1 | dominate%2:42:00:: | Cannot answer: inventory inadequate | dominate%2:42:01:: |
| senseval2.d002.s055.t001 | involvement / NOUN / senseval2 | 1/3 | Exactly two agree | 2/3 | 1 | Cannot answer: inventory inadequate | involvement%1:04:00:: | involvement%1:26:01:: |
| senseval2.d002.s076.t004 | large / ADJ / senseval2 | 1/3 | Exactly two agree | 2/3 | 0 | large%5:00:00:comprehensive:00 | large%3:00:00:: | large%5:00:00:significant:00 |
| senseval3.d000.s002.t001 | ready / ADJ / senseval3 | 0/3 | Exactly two agree | 2/3 | 1 | ready%5:00:01:available:00 | ready%5:00:00:prepared:00 | Cannot answer: inventory inadequate |
| senseval3.d000.s011.t004 | occasion / NOUN / senseval3 | 0/3 | Exactly two agree | 2/3 | 0 | occasion%1:16:00:: | occasion%1:11:00:: | occasion%1:28:00:: |
| senseval3.d000.s021.t003 | time / NOUN / senseval3 | 1/3 | Exactly two agree | 2/3 | 1 | time%1:11:00:: | Cannot answer: inventory inadequate | time%1:28:00:: |
| senseval3.d000.s031.t002 | realize / VERB / senseval3 | 1/3 | Exactly two agree | 2/3 | 1 | realize%2:31:00:: | realize%2:31:01:: | Cannot answer: inventory inadequate |
| senseval3.d000.s116.t001 | encourage / VERB / senseval3 | 1/3 | All three disagree | 1/3 | 1 | encourage%2:32:00:: | Cannot answer: inventory inadequate | encourage%2:41:00:: |
| senseval3.d000.s119.t004 | talk / VERB / senseval3 | 1/3 | All three agree | 3/3 | 0 | talk%2:32:03:: | talk%2:32:01:: | talk%2:32:00:: |
| senseval3.d001.s045.t002 | reveal / VERB / senseval3 | 1/3 | Exactly two agree | 2/3 | 1 | reveal%2:39:00:: | reveal%2:32:00:: | Cannot answer: inventory inadequate |
| senseval3.d002.s086.t000 | thing / NOUN / senseval3 | 0/3 | All three disagree | 0/3 | 1 | Cannot answer: no sense applies | thing%1:09:02:: | thing%1:11:00:: |
| senseval3.d002.s093.t000 | say / VERB / senseval3 | 1/3 | All three agree | 3/3 | 0 | say%2:32:01:: | say%2:32:00:: | say%2:32:00::, say%2:32:15:: |
| senseval3.d002.s138.t000 | quiet / ADJ / senseval3 | 1/3 | All three agree | 3/3 | 0 | quiet%3:00:01::, quiet%3:00:02:: | quiet%3:00:02:: | quiet%3:00:01:: |

### Manual Sample Review

A manual review of 20 no-consensus items found no case that was safe to keep by falling back to the
Maru2022 label. The common failure modes were inventory gaps, fixed expressions, figurative uses,
and fine WordNet distinctions that the context does not reliably determine.

| Item | Lemma/POS/source | Recommendation | Rationale |
| --- | --- | --- | --- |
| semeval2013.d000.s019.t000 | game / NOUN / semeval2013 | Remove | WordNet lacks the figurative strategic-manoeuvring sense of game in this context. |
| semeval2013.d009.s022.t000 | conservative / NOUN / semeval2013 | Remove | The US ideological conservative reading is not cleanly captured by the party/member senses. |
| semeval2015.d001.s009.t007 | input / NOUN / semeval2015 | Remove or adjudicate | The computer-input sense is missing or underspecified, and Maru2022 support is weak. |
| semeval2015.d002.s011.t008 | organisation / NOUN / semeval2015 | Remove or adjudicate | The context likely means the way work is organised, while the available labels diverge. |
| semeval2015.d003.s009.t014 | follow / VERB / semeval2015 | Remove from fine scoring | The reviewers differ at fine WordNet level even though Glite coarsening makes them agree. |
| semeval2015.d003.s012.t002 | act / VERB / semeval2015 | Remove | The functional/location use of act in the central nervous system does not map cleanly. |
| senseval2.d001.s015.t001 | make / VERB / senseval2 | Remove | The gene-copy context for make proteins lacks a clean production sense in the inventory. |
| senseval2.d001.s026.t007 | fundamental / ADJ / senseval2 | Remove from fine scoring | The fine-grained distinction is underdetermined even though coarse meaning is closer. |
| senseval2.d001.s041.t005 | specific / ADJ / senseval2 | Remove | Specific genes means particular or individual genes, and reviewers did not converge. |
| senseval2.d001.s057.t002 | attention / NOUN / senseval2 | Remove | Turned his attention to is a fixed research-focus use, not a reliable fine sense. |
| senseval2.d002.s004.t002 | dominate / VERB / senseval2 | Remove or adjudicate | Dominate means strongly influence or prevail over, but the inventory split is unstable. |
| senseval2.d002.s055.t001 | involvement / NOUN / senseval2 | Remove or adjudicate | The intended involvement reading mixes participation and control, producing ambiguity. |
| senseval3.d000.s002.t001 | ready / ADJ / senseval3 | Remove | Ready answer means prompt or available answer; the inventory does not fit cleanly. |
| senseval3.d000.s011.t004 | occasion / NOUN / senseval3 | Remove or adjudicate | All three choices are plausible but different, and Maru2022 has no support. |
| senseval3.d000.s021.t003 | time / NOUN / senseval3 | Remove | At the time is a fixed expression and does not support reliable fine-grained tagging. |
| senseval3.d000.s031.t002 | realize / VERB / senseval3 | Remove or adjudicate | The become-aware nuance exposes a WordNet definition boundary problem. |
| senseval3.d000.s116.t001 | encourage / VERB / senseval3 | Remove | Encourage his company means make more likely or promote, not a clean available sense. |
| senseval3.d001.s045.t002 | reveal / VERB / senseval3 | Remove | Investigation reveals mixes make-known and show evidence; WordNet is too narrow here. |
| senseval3.d002.s086.t000 | thing / NOUN / senseval3 | Remove | Things got rougher uses thing as a general situation marker, not a clean WordNet sense. |
| senseval3.d002.s138.t000 | quiet / ADJ / senseval3 | Remove from fine scoring | Quiet has noise versus activity ambiguity; reviewers agree only after Glite coarsening. |

## What The Agreement Shows

The reviewer evidence supports a conservative benchmark construction policy. Unanimous and
two-reviewer fine-grained agreements provide direct corrections to Maru2022. Cases where two
reviewers mark the item unanswerable and cases with no fine-grained majority are excluded from the
benchmark release but remain visible in this report, so downstream users can audit them.

## Technical Method

The report is generated by `scripts/build_agreement_report.py`. It reads
`data/lexen-v1/reviews.jsonl`, `sources/selection/lexicographer_review.jsonl.gz`, and the Glite
mapping files. The script writes Markdown, HTML, PDF, `metrics.json`, `per_item_agreement.jsonl`,
and chart images under `reports/rf-pw-ph-2026-06-13/`.

## Full Item Appendix

The appendix contains all 363 reviewed items. Items are grouped by the fine-grained three-reviewer
outcome, because this is the level at which lexEN decides whether Maru2022 is retained, corrected,
or removed for lack of usable consensus.

| Group | Outcome | Items |
| --- | --- | --- |
| [A](#appendix-a) | [All three reviewers selected the Maru2022 sense](#appendix-a) | [40 (11.0%)](#appendix-a) |
| [B](#appendix-b) | [All three reviewers selected the same correction](#appendix-b) | [84 (23.1%)](#appendix-b) |
| [C](#appendix-c) | [All three reviewers judged the item unanswerable](#appendix-c) | [5 (1.4%)](#appendix-c) |
| [D](#appendix-d) | [Two reviewers selected the same sense](#appendix-d) | [183 (50.4%)](#appendix-d) |
| [E](#appendix-e) | [Two reviewers judged the item unanswerable](#appendix-e) | [22 (6.1%)](#appendix-e) |
| [F](#appendix-f) | [All three reviewers disagreed](#appendix-f) | [29 (8.0%)](#appendix-f) |

<a id="appendix-a"></a>

## Appendix A. All three reviewers selected the Maru2022 sense

Every reviewer independently chose exactly the same fine-grained WordNet label as the Maru2022
source label. Count: 40.

### A1. semeval2013.d000.s017.t004

**Lemma/POS/source:** `united_states` / `NOUN` / `semeval2013` (`semeval2013.d000`)

**Sentence:** The current battle is as much about saving individual economies as saving the planet,
with China and **[United States]** feuding over their respective obligations while poorer nations
insist that the world's two dozen most influential countries are ignoring the scientific imperative
to take bolder action.

**Maru2022 label**

* united_states%1:14:00:: (united_states_government.n.01) - the executive and legislative and
  judicial branches of the federal government of the United States

**Reviewer verdicts**

* **Robert Farren (RF)**
  * united_states%1:14:00:: (united_states_government.n.01) - the executive and legislative and
    judicial branches of the federal government of the United States
* **Patrick White (PW)**
  * united_states%1:14:00:: (united_states_government.n.01) - the executive and legislative and
    judicial branches of the federal government of the United States
* **Penny Hands (PH)**
  * united_states%1:14:00:: (united_states_government.n.01) - the executive and legislative and
    judicial branches of the federal government of the United States

**Agreement:** Fine: All three agree; Glite: All three agree; Maru2022 fine support: 3/3; Maru2022
Glite support: 3/3.

### A2. semeval2013.d001.s008.t003

**Lemma/POS/source:** `night` / `NOUN` / `semeval2013` (`semeval2013.d001`)

**Sentence:** Teletovic had already begun to stand out as the best on his team with 13 points, even
though Splitter's ``six fewer'' points already signaled that it was n't going to be the best
**[night]** for the Brazilian.

**Maru2022 label**

* night%1:28:03:: (night.n.07) - the time between sunset and midnight Examples: he watched
  television every night

**Reviewer verdicts**

* **Robert Farren (RF)**
  * night%1:28:03:: (night.n.07) - the time between sunset and midnight Examples: he watched
    television every night
* **Patrick White (PW)**
  * night%1:28:03:: (night.n.07) - the time between sunset and midnight Examples: he watched
    television every night
* **Penny Hands (PH)**
  * night%1:28:03:: (night.n.07) - the time between sunset and midnight Examples: he watched
    television every night

**Agreement:** Fine: All three agree; Glite: All three agree; Maru2022 fine support: 3/3; Maru2022
Glite support: 3/3.

### A3. semeval2013.d003.s008.t004

**Lemma/POS/source:** `u.s.` / `NOUN` / `semeval2013` (`semeval2013.d003`)

**Sentence:** Iraq finally opened its doors after six years of war, and instead of **[U.S.]**
companies, you have Asians and Europeans leading the way, said Ruba Husari, the editor of Iraq Oil
Forum, an online news outlet.

**Maru2022 label**

* u.s.%1:15:00:: (united_states.n.01) - North American republic containing 50 states - 48
  conterminous states in North America plus Alaska in northwest North America and the Hawaiian
  Islands in the Pacific Ocean; achieved independence in 1776

**Reviewer verdicts**

* **Robert Farren (RF)**
  * u.s.%1:15:00:: (united_states.n.01) - North American republic containing 50 states - 48
    conterminous states in North America plus Alaska in northwest North America and the Hawaiian
    Islands in the Pacific Ocean; achieved independence in 1776
* **Patrick White (PW)**
  * u.s.%1:15:00:: (united_states.n.01) - North American republic containing 50 states - 48
    conterminous states in North America plus Alaska in northwest North America and the Hawaiian
    Islands in the Pacific Ocean; achieved independence in 1776
* **Penny Hands (PH)**
  * u.s.%1:15:00:: (united_states.n.01) - North American republic containing 50 states - 48
    conterminous states in North America plus Alaska in northwest North America and the Hawaiian
    Islands in the Pacific Ocean; achieved independence in 1776

**Agreement:** Fine: All three agree; Glite: All three agree; Maru2022 fine support: 3/3; Maru2022
Glite support: 3/3.

### A4. semeval2013.d003.s011.t000

**Lemma/POS/source:** `u.s.` / `NOUN` / `semeval2013` (`semeval2013.d003`)

**Sentence:** **[U.S.]** firms were in some cases at a disadvantage because rivals, particularly the
Chinese and other government controlled energy firms, have markedly lower labor costs and are more
prone to take risks because they do n't respond to shareholders.

**Maru2022 label**

* u.s.%1:15:00:: (united_states.n.01) - North American republic containing 50 states - 48
  conterminous states in North America plus Alaska in northwest North America and the Hawaiian
  Islands in the Pacific Ocean; achieved independence in 1776

**Reviewer verdicts**

* **Robert Farren (RF)**
  * u.s.%1:15:00:: (united_states.n.01) - North American republic containing 50 states - 48
    conterminous states in North America plus Alaska in northwest North America and the Hawaiian
    Islands in the Pacific Ocean; achieved independence in 1776
* **Patrick White (PW)**
  * u.s.%1:15:00:: (united_states.n.01) - North American republic containing 50 states - 48
    conterminous states in North America plus Alaska in northwest North America and the Hawaiian
    Islands in the Pacific Ocean; achieved independence in 1776
* **Penny Hands (PH)**
  * u.s.%1:15:00:: (united_states.n.01) - North American republic containing 50 states - 48
    conterminous states in North America plus Alaska in northwest North America and the Hawaiian
    Islands in the Pacific Ocean; achieved independence in 1776

**Agreement:** Fine: All three agree; Glite: All three agree; Maru2022 fine support: 3/3; Maru2022
Glite support: 3/3.

### A5. semeval2013.d003.s013.t000

**Lemma/POS/source:** `u.s.` / `NOUN` / `semeval2013` (`semeval2013.d003`)

**Sentence:** Major **[U.S.]** firms such as Chevron and ConocoPhillips, which have cultivated close
ties with the Iraqi Oil Ministry and have provided technical advice in recent years, walked away
empty-handed.

**Maru2022 label**

* u.s.%1:15:00:: (united_states.n.01) - North American republic containing 50 states - 48
  conterminous states in North America plus Alaska in northwest North America and the Hawaiian
  Islands in the Pacific Ocean; achieved independence in 1776

**Reviewer verdicts**

* **Robert Farren (RF)**
  * u.s.%1:15:00:: (united_states.n.01) - North American republic containing 50 states - 48
    conterminous states in North America plus Alaska in northwest North America and the Hawaiian
    Islands in the Pacific Ocean; achieved independence in 1776
* **Patrick White (PW)**
  * u.s.%1:15:00:: (united_states.n.01) - North American republic containing 50 states - 48
    conterminous states in North America plus Alaska in northwest North America and the Hawaiian
    Islands in the Pacific Ocean; achieved independence in 1776
* **Penny Hands (PH)**
  * u.s.%1:15:00:: (united_states.n.01) - North American republic containing 50 states - 48
    conterminous states in North America plus Alaska in northwest North America and the Hawaiian
    Islands in the Pacific Ocean; achieved independence in 1776

**Agreement:** Fine: All three agree; Glite: All three agree; Maru2022 fine support: 3/3; Maru2022
Glite support: 3/3.

### A6. semeval2013.d009.s023.t001

**Lemma/POS/source:** `administration` / `NOUN` / `semeval2013` (`semeval2013.d009`)

**Sentence:** Kagan served as solicitor general in the Obama **[administration]** when the first
legal challenges to the law were brought at the trial court level.

**Maru2022 label**

* administration%1:28:00:: (presidency.n.01) - the tenure of a president Examples: things were quiet
  during the Eisenhower administration

**Reviewer verdicts**

* **Robert Farren (RF)**
  * administration%1:28:00:: (presidency.n.01) - the tenure of a president Examples: things were
    quiet during the Eisenhower administration
* **Patrick White (PW)**
  * administration%1:28:00:: (presidency.n.01) - the tenure of a president Examples: things were
    quiet during the Eisenhower administration
* **Penny Hands (PH)**
  * administration%1:28:00:: (presidency.n.01) - the tenure of a president Examples: things were
    quiet during the Eisenhower administration

**Agreement:** Fine: All three agree; Glite: All three agree; Maru2022 fine support: 3/3; Maru2022
Glite support: 3/3.

### A7. semeval2013.d011.s020.t006

**Lemma/POS/source:** `proportion` / `NOUN` / `semeval2013` (`semeval2013.d011`)

**Sentence:** And does so without taking into account the fact that the diversity contributed by
immigrants contributes to the creation of ideas and to economic growth (a large **[proportion]** of
naturalised immigrants are among American Nobel prize winners, whilst Google, Intel, Paypal, eBay
and Yahoo were all founded by immigrants).

**Maru2022 label**

* proportion%1:24:01:: (proportion.n.04) - the relation between things (or parts of things) with
  respect to their comparative quantity, magnitude, or degree Examples: an inordinate proportion of
  the book is given over to quotations | a dry martini has a large proportion of gin

**Reviewer verdicts**

* **Robert Farren (RF)**
  * proportion%1:24:01:: (proportion.n.04) - the relation between things (or parts of things) with
    respect to their comparative quantity, magnitude, or degree Examples: an inordinate proportion
    of the book is given over to quotations | a dry martini has a large proportion of gin
  * Comment: Sense 1 is also a good fit, but this use of "proportion" is not really concerned with
    the exact number (quotient) of American Nobel prize winners who are immigrants. It's simply
    saying that they represent a significant subset of the whole. Sense 4 is more in line with this
    sense.
* **Patrick White (PW)**
  * proportion%1:24:01:: (proportion.n.04) - the relation between things (or parts of things) with
    respect to their comparative quantity, magnitude, or degree Examples: an inordinate proportion
    of the book is given over to quotations | a dry martini has a large proportion of gin
* **Penny Hands (PH)**
  * proportion%1:24:01:: (proportion.n.04) - the relation between things (or parts of things) with
    respect to their comparative quantity, magnitude, or degree Examples: an inordinate proportion
    of the book is given over to quotations | a dry martini has a large proportion of gin

**Agreement:** Fine: All three agree; Glite: All three agree; Maru2022 fine support: 3/3; Maru2022
Glite support: 3/3.

### A8. semeval2015.d000.s026.t000

**Lemma/POS/source:** `effect` / `NOUN` / `semeval2015` (`semeval2015.d000`)

**Sentence:** The **[effects]** of Alimta in combination with cisplatin were compared with those of
cisplatin alone.

**Maru2022 label**

* effect%1:26:00:: (effect.n.06) - a symptom caused by an illness or a drug Examples: the effects of
  sleep loss | the effect of the anesthetic

**Reviewer verdicts**

* **Robert Farren (RF)**
  * effect%1:26:00:: (effect.n.06) - a symptom caused by an illness or a drug Examples: the effects
    of sleep loss | the effect of the anesthetic
* **Patrick White (PW)**
  * effect%1:26:00:: (effect.n.06) - a symptom caused by an illness or a drug Examples: the effects
    of sleep loss | the effect of the anesthetic
* **Penny Hands (PH)**
  * effect%1:26:00:: (effect.n.06) - a symptom caused by an illness or a drug Examples: the effects
    of sleep loss | the effect of the anesthetic

**Agreement:** Fine: All three agree; Glite: All three agree; Maru2022 fine support: 3/3; Maru2022
Glite support: 3/3.

### A9. semeval2015.d001.s001.t006

**Lemma/POS/source:** `3d` / `NOUN` / `semeval2015` (`semeval2015.d001`)

**Sentence:** Nowadays it is capable to make simple MathML operations (arithmetic and logical) and
to representate 2D and **[3D]** graphs.

**Maru2022 label**

* 3d%1:09:00:: (three-d.n.02) - having a three-dimensional form or appearance Examples: aren't
  dreams always in 3-D?

**Reviewer verdicts**

* **Robert Farren (RF)**
  * 3d%1:09:00:: (three-d.n.02) - having a three-dimensional form or appearance Examples: aren't
    dreams always in 3-D?
* **Patrick White (PW)**
  * 3d%1:09:00:: (three-d.n.02) - having a three-dimensional form or appearance Examples: aren't
    dreams always in 3-D?
* **Penny Hands (PH)**
  * 3d%1:09:00:: (three-d.n.02) - having a three-dimensional form or appearance Examples: aren't
    dreams always in 3-D?

**Agreement:** Fine: All three agree; Glite: All three agree; Maru2022 fine support: 3/3; Maru2022
Glite support: 3/3.

### A10. semeval2015.d001.s007.t005

**Lemma/POS/source:** `3d` / `NOUN` / `semeval2015` (`semeval2015.d001`)

**Sentence:** kalgebra main window consists in a Console tab, a 2D Graph tab, a **[3D]** Graph tab
and a Dictionary tab.

**Maru2022 label**

* 3d%1:09:00:: (three-d.n.02) - having a three-dimensional form or appearance Examples: aren't
  dreams always in 3-D?

**Reviewer verdicts**

* **Robert Farren (RF)**
  * 3d%1:09:00:: (three-d.n.02) - having a three-dimensional form or appearance Examples: aren't
    dreams always in 3-D?
* **Patrick White (PW)**
  * 3d%1:09:00:: (three-d.n.02) - having a three-dimensional form or appearance Examples: aren't
    dreams always in 3-D?
* **Penny Hands (PH)**
  * 3d%1:09:00:: (three-d.n.02) - having a three-dimensional form or appearance Examples: aren't
    dreams always in 3-D?

**Agreement:** Fine: All three agree; Glite: All three agree; Maru2022 fine support: 3/3; Maru2022
Glite support: 3/3.

### A11. semeval2015.d001.s032.t001

**Lemma/POS/source:** `have` / `VERB` / `semeval2015` (`semeval2015.d001`)

**Sentence:** There you **[have]** a list of the declared variables.

**Maru2022 label**

* have%2:42:12:: (have.v.10) - be confronted with Examples: What do we have here? | Now we have a
  fine mess

**Reviewer verdicts**

* **Robert Farren (RF)**
  * have%2:42:12:: (have.v.10) - be confronted with Examples: What do we have here? | Now we have a
    fine mess
* **Patrick White (PW)**
  * have%2:42:12:: (have.v.10) - be confronted with Examples: What do we have here? | Now we have a
    fine mess
* **Penny Hands (PH)**
  * have%2:42:12:: (have.v.10) - be confronted with Examples: What do we have here? | Now we have a
    fine mess

**Agreement:** Fine: All three agree; Glite: All three agree; Maru2022 fine support: 3/3; Maru2022
Glite support: 3/3.

### A12. semeval2015.d001.s035.t000

**Lemma/POS/source:** `new` / `ADJ` / `semeval2015` (`semeval2015.d001`)

**Sentence:** Ctrl N **[New]** Window

**Maru2022 label**

* new%5:00:00:other:00 (new.s.04) - other than the former one(s); different Examples: they now have
  a new leaders | my new car is four years old but has only 15,000 miles on it

**Reviewer verdicts**

* **Robert Farren (RF)**
  * new%5:00:00:other:00 (new.s.04) - other than the former one(s); different Examples: they now
    have a new leaders | my new car is four years old but has only 15,000 miles on it
* **Patrick White (PW)**
  * new%5:00:00:other:00 (new.s.04) - other than the former one(s); different Examples: they now
    have a new leaders | my new car is four years old but has only 15,000 miles on it
* **Penny Hands (PH)**
  * new%5:00:00:other:00 (new.s.04) - other than the former one(s); different Examples: they now
    have a new leaders | my new car is four years old but has only 15,000 miles on it

**Agreement:** Fine: All three agree; Glite: All three agree; Maru2022 fine support: 3/3; Maru2022
Glite support: 3/3.

### A13. semeval2015.d001.s047.t001

**Lemma/POS/source:** `new` / `ADJ` / `semeval2015` (`semeval2015.d001`)

**Sentence:** To add a **[new]** 2D graph on kalgebra, what you have to do is to go to the 2D Graph
tab and click in the Add tab to add the new function.

**Maru2022 label**

* new%5:00:00:other:00 (new.s.04) - other than the former one(s); different Examples: they now have
  a new leaders | my new car is four years old but has only 15,000 miles on it

**Reviewer verdicts**

* **Robert Farren (RF)**
  * new%5:00:00:other:00 (new.s.04) - other than the former one(s); different Examples: they now
    have a new leaders | my new car is four years old but has only 15,000 miles on it
* **Patrick White (PW)**
  * new%5:00:00:other:00 (new.s.04) - other than the former one(s); different Examples: they now
    have a new leaders | my new car is four years old but has only 15,000 miles on it
* **Penny Hands (PH)**
  * new%5:00:00:other:00 (new.s.04) - other than the former one(s); different Examples: they now
    have a new leaders | my new car is four years old but has only 15,000 miles on it

**Agreement:** Fine: All three agree; Glite: All three agree; Maru2022 fine support: 3/3; Maru2022
Glite support: 3/3.

### A14. semeval2015.d001.s047.t008

**Lemma/POS/source:** `new` / `ADJ` / `semeval2015` (`semeval2015.d001`)

**Sentence:** To add a new 2D graph on kalgebra, what you have to do is to go to the 2D Graph tab
and click in the Add tab to add the **[new]** function.

**Maru2022 label**

* new%5:00:00:other:00 (new.s.04) - other than the former one(s); different Examples: they now have
  a new leaders | my new car is four years old but has only 15,000 miles on it

**Reviewer verdicts**

* **Robert Farren (RF)**
  * new%5:00:00:other:00 (new.s.04) - other than the former one(s); different Examples: they now
    have a new leaders | my new car is four years old but has only 15,000 miles on it
* **Patrick White (PW)**
  * new%5:00:00:other:00 (new.s.04) - other than the former one(s); different Examples: they now
    have a new leaders | my new car is four years old but has only 15,000 miles on it
* **Penny Hands (PH)**
  * new%5:00:00:other:00 (new.s.04) - other than the former one(s); different Examples: they now
    have a new leaders | my new car is four years old but has only 15,000 miles on it

**Agreement:** Fine: All three agree; Glite: All three agree; Maru2022 fine support: 3/3; Maru2022
Glite support: 3/3.

### A15. semeval2015.d001.s049.t005

**Lemma/POS/source:** `specify` / `VERB` / `semeval2015` (`semeval2015.d001`)

**Sentence:** If you want to use a typical f(x) function it is not necessary to **[specify]** it.

**Maru2022 label**

* specify%2:32:02:: (specify.v.02) - decide upon or fix definitely Examples: fix the variables |
  specify the parameters

**Reviewer verdicts**

* **Robert Farren (RF)**
  * specify%2:32:02:: (specify.v.02) - decide upon or fix definitely Examples: fix the variables |
    specify the parameters
* **Patrick White (PW)**
  * specify%2:32:02:: (specify.v.02) - decide upon or fix definitely Examples: fix the variables |
    specify the parameters
* **Penny Hands (PH)**
  * specify%2:32:02:: (specify.v.02) - decide upon or fix definitely Examples: fix the variables |
    specify the parameters
  * Comment: I rejected sense 4 because it seems to be talking about giving more detail. In the
    text, the sentence is saying that you don’t need to say exactly which function you are using
    (sense 2).

**Agreement:** Fine: All three agree; Glite: All three agree; Maru2022 fine support: 3/3; Maru2022
Glite support: 3/3.

### A16. semeval2015.d002.s010.t000

**Lemma/POS/source:** `country` / `NOUN` / `semeval2015` (`semeval2015.d002`)

**Sentence:** For each **[country]**, two or three initiatives have been selected for further in
depth case study.

**Maru2022 label**

* country%1:14:00:: (state.n.04) - a politically organized body of people under a single government
  Examples: the state has elected a new president | African nations

**Reviewer verdicts**

* **Robert Farren (RF)**
  * country%1:14:00:: (state.n.04) - a politically organized body of people under a single
    government Examples: the state has elected a new president | African nations
* **Patrick White (PW)**
  * country%1:14:00:: (state.n.04) - a politically organized body of people under a single
    government Examples: the state has elected a new president | African nations
* **Penny Hands (PH)**
  * country%1:14:00:: (state.n.04) - a politically organized body of people under a single
    government Examples: the state has elected a new president | African nations
  * Comment: Sense 2 is close, but I think the emphasis in the text is on these nations as organised
    political bodies (sense 1) rather than the land they cover.

**Agreement:** Fine: All three agree; Glite: All three agree; Maru2022 fine support: 3/3; Maru2022
Glite support: 3/3.

### A17. semeval2015.d003.s019.t012

**Lemma/POS/source:** `underlying` / `ADJ` / `semeval2015` (`semeval2015.d003`)

**Sentence:** Also, the treatment of vomiting should only be together with other supportive measure
or other veterinary therapy while addressing the **[underlying]** causes of the vomiting.

**Maru2022 label**

* underlying%5:00:00:implicit:00 (implicit_in.s.01) - in the nature of something though not readily
  apparent Examples: shortcomings inherent in our approach | an underlying meaning

**Reviewer verdicts**

* **Robert Farren (RF)**
  * underlying%5:00:00:implicit:00 (implicit_in.s.01) - in the nature of something though not
    readily apparent Examples: shortcomings inherent in our approach | an underlying meaning
* **Patrick White (PW)**
  * underlying%5:00:00:implicit:00 (implicit_in.s.01) - in the nature of something though not
    readily apparent Examples: shortcomings inherent in our approach | an underlying meaning
* **Penny Hands (PH)**
  * underlying%5:00:00:implicit:00 (implicit_in.s.01) - in the nature of something though not
    readily apparent Examples: shortcomings inherent in our approach | an underlying meaning

**Agreement:** Fine: All three agree; Glite: All three agree; Maru2022 fine support: 3/3; Maru2022
Glite support: 3/3.

### A18. semeval2015.d003.s021.t005

**Lemma/POS/source:** `dosage` / `NOUN` / `semeval2015` (`semeval2015.d003`)

**Sentence:** Cerenia was generally well tolerated when administered daily at **[dosages]** up to 5
times the recommended doses for an extended period of time (up to 3 times the recommended maximum
duration of treatment).

**Maru2022 label**

* dosage%1:06:00:: (dose.n.01) - a measured portion of medicine taken at any one time

**Reviewer verdicts**

* **Robert Farren (RF)**
  * dosage%1:06:00:: (dose.n.01) - a measured portion of medicine taken at any one time
* **Patrick White (PW)**
  * dosage%1:06:00:: (dose.n.01) - a measured portion of medicine taken at any one time
* **Penny Hands (PH)**
  * dosage%1:06:00:: (dose.n.01) - a measured portion of medicine taken at any one time

**Agreement:** Fine: All three agree; Glite: All three agree; Maru2022 fine support: 3/3; Maru2022
Glite support: 3/3.

### A19. senseval2.d000.s008.t000

**Lemma/POS/source:** `now` / `ADV` / `senseval2` (`senseval2.d000`)

**Sentence:** **[Now]**, only one local ringer remains: 64-year-old Derek Hammond.

**Maru2022 label**

* now%4:02:04:: (now.r.04) - at the present moment Examples: goods now on sale | the now-aging
  dictator

**Reviewer verdicts**

* **Robert Farren (RF)**
  * now%4:02:04:: (now.r.04) - at the present moment Examples: goods now on sale | the now-aging
    dictator
* **Patrick White (PW)**
  * now%4:02:04:: (now.r.04) - at the present moment Examples: goods now on sale | the now-aging
    dictator
* **Penny Hands (PH)**
  * now%4:02:04:: (now.r.04) - at the present moment Examples: goods now on sale | the now-aging
    dictator

**Agreement:** Fine: All three agree; Glite: All three agree; Maru2022 fine support: 3/3; Maru2022
Glite support: 3/3.

### A20. senseval2.d000.s044.t004

**Lemma/POS/source:** `fault` / `NOUN` / `senseval2` (`senseval2.d000`)

**Sentence:** But C.J.B. Marshall, vicar of a nearby church, feels the **[fault]** is in the stairs
from the bell tower that are located next to the altar.

**Maru2022 label**

* fault%1:07:01:: (fault.n.06) - responsibility for a bad situation or event Examples: it was John's
  fault

**Reviewer verdicts**

* **Robert Farren (RF)**
  * fault%1:07:01:: (fault.n.06) - responsibility for a bad situation or event Examples: it was
    John's fault
* **Patrick White (PW)**
  * fault%1:07:01:: (fault.n.06) - responsibility for a bad situation or event Examples: it was
    John's fault
* **Penny Hands (PH)**
  * fault%1:07:01:: (fault.n.06) - responsibility for a bad situation or event Examples: it was
    John's fault
  * Comment: The stairs are responsible. There are no defects in the stairs.

**Agreement:** Fine: All three agree; Glite: All three agree; Maru2022 fine support: 3/3; Maru2022
Glite support: 3/3.

### A21. senseval2.d001.s007.t005

**Lemma/POS/source:** `initiate` / `VERB` / `senseval2` (`senseval2.d001`)

**Sentence:** Today, we know that the accumulation of several of these altered genes can
**[initiate]** a cancer and, then, propel it into a deadly state. ``

**Maru2022 label**

* initiate%2:36:01:: (originate.v.02) - bring into being Examples: He initiated a new program |
  Start a foundation

**Reviewer verdicts**

* **Robert Farren (RF)**
  * initiate%2:36:01:: (originate.v.02) - bring into being Examples: He initiated a new program |
    Start a foundation
* **Patrick White (PW)**
  * initiate%2:36:01:: (originate.v.02) - bring into being Examples: He initiated a new program |
    Start a foundation
* **Penny Hands (PH)**
  * initiate%2:36:01:: (originate.v.02) - bring into being Examples: He initiated a new program |
    Start a foundation
  * Comment: I rejected sense 5 because it seems to be more about setting an event in motion rather
    than causing something to exist (sense 1).

**Agreement:** Fine: All three agree; Glite: All three agree; Maru2022 fine support: 3/3; Maru2022
Glite support: 3/3.

### A22. senseval2.d001.s020.t001

**Lemma/POS/source:** `carry` / `VERB` / `senseval2` (`senseval2.d001`)

**Sentence:** Mr. Quinlan, 30 years old, knew he **[carried]** a damaged gene, having lost an eye to
the rare tumor when he was only two months old -- after his mother had suffered the same fate when
she was a baby.

**Maru2022 label**

* carry%2:42:13:: (carry.v.18) - have as an inherent or characteristic feature or have as a
  consequence Examples: This new washer carries a two year guarantee | The loan carries a high
  interest rate

**Reviewer verdicts**

* **Robert Farren (RF)**
  * carry%2:42:13:: (carry.v.18) - have as an inherent or characteristic feature or have as a
    consequence Examples: This new washer carries a two year guarantee | The loan carries a high
    interest rate
* **Patrick White (PW)**
  * carry%2:42:13:: (carry.v.18) - have as an inherent or characteristic feature or have as a
    consequence Examples: This new washer carries a two year guarantee | The loan carries a high
    interest rate
* **Penny Hands (PH)**
  * carry%2:42:13:: (carry.v.18) - have as an inherent or characteristic feature or have as a
    consequence Examples: This new washer carries a two year guarantee | The loan carries a high
    interest rate

**Agreement:** Fine: All three agree; Glite: All three agree; Maru2022 fine support: 3/3; Maru2022
Glite support: 3/3.

### A23. senseval2.d001.s033.t005

**Lemma/POS/source:** `u.s.` / `NOUN` / `senseval2` (`senseval2.d001`)

**Sentence:** Right now about a dozen laboratories, in the **[U.S.]**, Canada and Britain, are
racing to unmask other suspected tumor-suppressing genes.

**Maru2022 label**

* u.s.%1:15:00:: (united_states.n.01) - North American republic containing 50 states - 48
  conterminous states in North America plus Alaska in northwest North America and the Hawaiian
  Islands in the Pacific Ocean; achieved independence in 1776

**Reviewer verdicts**

* **Robert Farren (RF)**
  * u.s.%1:15:00:: (united_states.n.01) - North American republic containing 50 states - 48
    conterminous states in North America plus Alaska in northwest North America and the Hawaiian
    Islands in the Pacific Ocean; achieved independence in 1776
* **Patrick White (PW)**
  * u.s.%1:15:00:: (united_states.n.01) - North American republic containing 50 states - 48
    conterminous states in North America plus Alaska in northwest North America and the Hawaiian
    Islands in the Pacific Ocean; achieved independence in 1776
* **Penny Hands (PH)**
  * u.s.%1:15:00:: (united_states.n.01) - North American republic containing 50 states - 48
    conterminous states in North America plus Alaska in northwest North America and the Hawaiian
    Islands in the Pacific Ocean; achieved independence in 1776

**Agreement:** Fine: All three agree; Glite: All three agree; Maru2022 fine support: 3/3; Maru2022
Glite support: 3/3.

### A24. senseval2.d001.s057.t009

**Lemma/POS/source:** `u.s.` / `NOUN` / `senseval2` (`senseval2.d001`)

**Sentence:** Dr. Vogelstein next turned his attention colon cancer, the second biggest cancer
killer in the **[U.S.]** after lung cancer.

**Maru2022 label**

* u.s.%1:15:00:: (united_states.n.01) - North American republic containing 50 states - 48
  conterminous states in North America plus Alaska in northwest North America and the Hawaiian
  Islands in the Pacific Ocean; achieved independence in 1776

**Reviewer verdicts**

* **Robert Farren (RF)**
  * u.s.%1:15:00:: (united_states.n.01) - North American republic containing 50 states - 48
    conterminous states in North America plus Alaska in northwest North America and the Hawaiian
    Islands in the Pacific Ocean; achieved independence in 1776
* **Patrick White (PW)**
  * u.s.%1:15:00:: (united_states.n.01) - North American republic containing 50 states - 48
    conterminous states in North America plus Alaska in northwest North America and the Hawaiian
    Islands in the Pacific Ocean; achieved independence in 1776
* **Penny Hands (PH)**
  * u.s.%1:15:00:: (united_states.n.01) - North American republic containing 50 states - 48
    conterminous states in North America plus Alaska in northwest North America and the Hawaiian
    Islands in the Pacific Ocean; achieved independence in 1776

**Agreement:** Fine: All three agree; Glite: All three agree; Maru2022 fine support: 3/3; Maru2022
Glite support: 3/3.

### A25. senseval2.d001.s067.t002

**Lemma/POS/source:** `need` / `VERB` / `senseval2` (`senseval2.d001`)

**Sentence:**
`It was the confirming evidence we all **[needed]** that gene losses were critical to the development of a common tumor, `says
Ray White at Howard Hughes Medical Institute in Salt Lake City.

**Maru2022 label**

* need%2:42:00:: (necessitate.v.01) - require as useful, just, or proper Examples: It takes nerve to
  do what she did | success usually requires hard work

**Reviewer verdicts**

* **Robert Farren (RF)**
  * need%2:42:00:: (necessitate.v.01) - require as useful, just, or proper Examples: It takes nerve
    to do what she did | success usually requires hard work
* **Patrick White (PW)**
  * need%2:42:00:: (necessitate.v.01) - require as useful, just, or proper Examples: It takes nerve
    to do what she did | success usually requires hard work
* **Penny Hands (PH)**
  * need%2:42:00:: (necessitate.v.01) - require as useful, just, or proper Examples: It takes nerve
    to do what she did | success usually requires hard work
  * Comment: I was tempted to go for sense 3, but concluded that sense 3 refers to personal desires
    ('feel', 'friends', 'money'), whereas the scientific community needed this evidence from a more
    objective point of view.

**Agreement:** Fine: All three agree; Glite: All three agree; Maru2022 fine support: 3/3; Maru2022
Glite support: 3/3.

### A26. senseval2.d001.s083.t003

**Lemma/POS/source:** `yet` / `ADV` / `senseval2` (`senseval2.d001`)

**Sentence:** There also are reports from several labs, as **[yet]** unpublished, of missing p53
genes in tissue taken from kidney, brain and skin cancers.

**Maru2022 label**

* yet%4:02:02:: (yet.r.01) - up to the present time Examples: I have yet to see the results |
  details are yet to be worked out

**Reviewer verdicts**

* **Robert Farren (RF)**
  * yet%4:02:02:: (yet.r.01) - up to the present time Examples: I have yet to see the results |
    details are yet to be worked out
  * Comment: The choice of sense is clear. However, the lexeme is really "as yet", rather than
    "yet".
* **Patrick White (PW)**
  * yet%4:02:02:: (yet.r.01) - up to the present time Examples: I have yet to see the results |
    details are yet to be worked out
  * Comment: Although the fixed phrase "as yet" is used here
* **Penny Hands (PH)**
  * yet%4:02:02:: (yet.r.01) - up to the present time Examples: I have yet to see the results |
    details are yet to be worked out
  * Comment: I hesitated over sense 2, which specifies 'used in a negative statement'. But the exact
    text is 'as yet unpublished', not 'which hasn't been published yet'. It's a close call, though.

**Agreement:** Fine: All three agree; Glite: All three agree; Maru2022 fine support: 3/3; Maru2022
Glite support: 3/3.

### A27. senseval2.d002.s011.t016

**Lemma/POS/source:** `yet` / `ADV` / `senseval2` (`senseval2.d002`)

**Sentence:** The whole notion of `creativity `in education was (and is) part and parcel of a
romantic rebellion against disciplined instruction, which was (and is) regarded as
`authoritarian, `a repression and frustration of the latent talents and the wonderful, if as
**[yet]** undefined, potentialities inherent in the souls of all our children.

**Maru2022 label**

* yet%4:02:02:: (yet.r.01) - up to the present time Examples: I have yet to see the results |
  details are yet to be worked out

**Reviewer verdicts**

* **Robert Farren (RF)**
  * yet%4:02:02:: (yet.r.01) - up to the present time Examples: I have yet to see the results |
    details are yet to be worked out
  * Comment: As stated elsewhere, the sense is clear enough, but the lexeme that has that sense is
    "as yet", rather than just "yet".
* **Patrick White (PW)**
  * yet%4:02:02:: (yet.r.01) - up to the present time Examples: I have yet to see the results |
    details are yet to be worked out
  * Comment: Although the usage here is as part of fixed phrase "as yet"
* **Penny Hands (PH)**
  * yet%4:02:02:: (yet.r.01) - up to the present time Examples: I have yet to see the results |
    details are yet to be worked out
  * Comment: As before, not sense 2 because the text does not technically constitute a negative
    statement.

**Agreement:** Fine: All three agree; Glite: All three agree; Maru2022 fine support: 3/3; Maru2022
Glite support: 3/3.

### A28. senseval2.d002.s040.t006

**Lemma/POS/source:** `same` / `ADJ` / `senseval2` (`senseval2.d002`)

**Sentence:** There are many successful schools scattered throughout this nation, some of them in
the poorest of ghettos, and they are all sending us the **[same]** message.

**Maru2022 label**

* same%3:00:00:: (same.a.02) - closely similar or comparable in kind or quality or quantity or
  degree Examples: curtains the same color as the walls | two girls of the same age

**Reviewer verdicts**

* **Robert Farren (RF)**
  * same%3:00:00:: (same.a.02) - closely similar or comparable in kind or quality or quantity or
    degree Examples: curtains the same color as the walls | two girls of the same age
* **Patrick White (PW)**
  * same%3:00:00:: (same.a.02) - closely similar or comparable in kind or quality or quantity or
    degree Examples: curtains the same color as the walls | two girls of the same age
* **Penny Hands (PH)**
  * same%3:00:00:: (same.a.02) - closely similar or comparable in kind or quality or quantity or
    degree Examples: curtains the same color as the walls | two girls of the same age
  * Comment: Sense 2 because each successful school is sending a message that is comparable in kind
    to those of other schools.

**Agreement:** Fine: All three agree; Glite: All three agree; Maru2022 fine support: 3/3; Maru2022
Glite support: 3/3.

### A29. senseval3.d000.s064.t001

**Lemma/POS/source:** `say` / `VERB` / `senseval3` (`senseval3.d000`)

**Sentence:** `It's my line of work `, he **[said]**

**Maru2022 label**

* say%2:32:15:: (say.v.08) - utter aloud Examples: She said `Hello' to everyone in the office

**Reviewer verdicts**

* **Robert Farren (RF)**
  * say%2:32:15:: (say.v.08) - utter aloud Examples: She said `Hello' to everyone in the office
* **Patrick White (PW)**
  * say%2:32:15:: (say.v.08) - utter aloud Examples: She said `Hello' to everyone in the office
* **Penny Hands (PH)**
  * say%2:32:15:: (say.v.08) - utter aloud Examples: She said `Hello' to everyone in the office
  * Comment: This time, it's clear that he said those words out loud because the wider context shows
    that this is a conversation.

**Agreement:** Fine: All three agree; Glite: All three agree; Maru2022 fine support: 3/3; Maru2022
Glite support: 3/3.

### A30. senseval3.d000.s069.t004

**Lemma/POS/source:** `night` / `NOUN` / `senseval3` (`senseval3.d000`)

**Sentence:** The next day, Sunday, the hangover reminded Haney where he had been the **[night]**
before.

**Maru2022 label**

* night%1:28:03:: (night.n.07) - the time between sunset and midnight Examples: he watched
  television every night

**Reviewer verdicts**

* **Robert Farren (RF)**
  * night%1:28:03:: (night.n.07) - the time between sunset and midnight Examples: he watched
    television every night
* **Patrick White (PW)**
  * night%1:28:03:: (night.n.07) - the time between sunset and midnight Examples: he watched
    television every night
* **Penny Hands (PH)**
  * night%1:28:03:: (night.n.07) - the time between sunset and midnight Examples: he watched
    television every night

**Agreement:** Fine: All three agree; Glite: All three agree; Maru2022 fine support: 3/3; Maru2022
Glite support: 3/3.

### A31. senseval3.d000.s086.t005

**Lemma/POS/source:** `question` / `NOUN` / `senseval3` (`senseval3.d000`)

**Sentence:** After a while he began to feel better about it, especially when no one bothered to ask
any **[questions]**.

**Maru2022 label**

* question%1:10:03:: (question.n.03) - a sentence of inquiry that asks for a reply Examples: he
  asked a direct question | he had trouble phrasing his interrogations

**Reviewer verdicts**

* **Robert Farren (RF)**
  * question%1:10:03:: (question.n.03) - a sentence of inquiry that asks for a reply Examples: he
    asked a direct question | he had trouble phrasing his interrogations
* **Patrick White (PW)**
  * question%1:10:03:: (question.n.03) - a sentence of inquiry that asks for a reply Examples: he
    asked a direct question | he had trouble phrasing his interrogations
* **Penny Hands (PH)**
  * question%1:10:03:: (question.n.03) - a sentence of inquiry that asks for a reply Examples: he
    asked a direct question | he had trouble phrasing his interrogations

**Agreement:** Fine: All three agree; Glite: All three agree; Maru2022 fine support: 3/3; Maru2022
Glite support: 3/3.

### A32. senseval3.d000.s114.t005

**Lemma/POS/source:** `realize` / `VERB` / `senseval3` (`senseval3.d000`)

**Sentence:** He made the mistake of answering in an offhand way, and instantly **[realized]** that
his skepticism must have showed in his face or voice.

**Maru2022 label**

* realize%2:31:00:: (understand.v.02) - perceive (an idea or situation) mentally Examples: Now I
  see! | I just can't see your point

**Reviewer verdicts**

* **Robert Farren (RF)**
  * realize%2:31:00:: (understand.v.02) - perceive (an idea or situation) mentally Examples: Now I
    see! | I just can't see your point
* **Patrick White (PW)**
  * realize%2:31:00:: (understand.v.02) - perceive (an idea or situation) mentally Examples: Now I
    see! | I just can't see your point
* **Penny Hands (PH)**
  * realize%2:31:00:: (understand.v.02) - perceive (an idea or situation) mentally Examples: Now I
    see! | I just can't see your point
  * Comment: Sense 2 is the closest because it gives the idea of *becoming* aware, whereas sense 1
    only talks about *being aware*. However, the sense 2 examples do seem to be more about suddenly
    understanding something after a period of being 'in the dark'. Ideally, there would be a
    definition that read: 'be *or become* fully aware or cognizant of'.

**Agreement:** Fine: All three agree; Glite: All three agree; Maru2022 fine support: 3/3; Maru2022
Glite support: 3/3.

### A33. senseval3.d001.s004.t011

**Lemma/POS/source:** `vote` / `NOUN` / `senseval3` (`senseval3.d001`)

**Sentence:** In every presidential election over the past half century, except for the Goldwater
presidential candidacy, the GOP has captured a greater percentage of the major - party popular
**[vote]** for president than it has of congressional seats or the popular vote for Congress.

**Maru2022 label**

* vote%1:09:00:: (vote.n.05) - the total number of voters who participated Examples: they are
  expecting a large vote

**Reviewer verdicts**

* **Robert Farren (RF)**
  * vote%1:09:00:: (vote.n.05) - the total number of voters who participated Examples: they are
    expecting a large vote
* **Patrick White (PW)**
  * vote%1:09:00:: (vote.n.05) - the total number of voters who participated Examples: they are
    expecting a large vote
* **Penny Hands (PH)**
  * vote%1:09:00:: (vote.n.05) - the total number of voters who participated Examples: they are
    expecting a large vote
  * Comment: The popular vote is the vote of all a country's voters.

**Agreement:** Fine: All three agree; Glite: All three agree; Maru2022 fine support: 3/3; Maru2022
Glite support: 3/3.

### A34. senseval3.d001.s004.t016

**Lemma/POS/source:** `vote` / `NOUN` / `senseval3` (`senseval3.d001`)

**Sentence:** In every presidential election over the past half century, except for the Goldwater
presidential candidacy, the GOP has captured a greater percentage of the major - party popular vote
for president than it has of congressional seats or the popular **[vote]** for Congress.

**Maru2022 label**

* vote%1:09:00:: (vote.n.05) - the total number of voters who participated Examples: they are
  expecting a large vote

**Reviewer verdicts**

* **Robert Farren (RF)**
  * vote%1:09:00:: (vote.n.05) - the total number of voters who participated Examples: they are
    expecting a large vote
* **Patrick White (PW)**
  * vote%1:09:00:: (vote.n.05) - the total number of voters who participated Examples: they are
    expecting a large vote
* **Penny Hands (PH)**
  * vote%1:09:00:: (vote.n.05) - the total number of voters who participated Examples: they are
    expecting a large vote
  * Comment: The popular vote is the vote of all a country's voters.

**Agreement:** Fine: All three agree; Glite: All three agree; Maru2022 fine support: 3/3; Maru2022
Glite support: 3/3.

### A35. senseval3.d001.s020.t017

**Lemma/POS/source:** `cost` / `NOUN` / `senseval3` (`senseval3.d001`)

**Sentence:** Second, it explains why voters hold Congress in disdain but generally love their own
congressional representatives: Any individual legislator's constituents appreciate the specific
benefits that the legislator wins for them but not the overall **[cost]** associated with every
other legislator doing likewise for his own constituency.

**Maru2022 label**

* cost%1:07:01:: (price.n.03) - value measured by what must be given or done or undergone to obtain
  something Examples: the cost in human life was enormous | the price of success is hard work

**Reviewer verdicts**

* **Robert Farren (RF)**
  * cost%1:07:01:: (price.n.03) - value measured by what must be given or done or undergone to
    obtain something Examples: the cost in human life was enormous | the price of success is hard
    work
* **Patrick White (PW)**
  * cost%1:07:01:: (price.n.03) - value measured by what must be given or done or undergone to
    obtain something Examples: the cost in human life was enormous | the price of success is hard
    work
* **Penny Hands (PH)**
  * cost%1:07:01:: (price.n.03) - value measured by what must be given or done or undergone to
    obtain something Examples: the cost in human life was enormous | the price of success is hard
    work

**Agreement:** Fine: All three agree; Glite: All three agree; Maru2022 fine support: 3/3; Maru2022
Glite support: 3/3.

### A36. senseval3.d001.s026.t001

**Lemma/POS/source:** `candidate` / `NOUN` / `senseval3` (`senseval3.d001`)

**Sentence:** Potential **[candidates]** may be discouraged from running less by the congressional
salary than by the prospect of defeat at the hands of a Democratic opponent.

**Maru2022 label**

* candidate%1:18:01:: (campaigner.n.01) - a politician who is running for public office

**Reviewer verdicts**

* **Robert Farren (RF)**
  * candidate%1:18:01:: (campaigner.n.01) - a politician who is running for public office
* **Patrick White (PW)**
  * candidate%1:18:01:: (campaigner.n.01) - a politician who is running for public office
* **Penny Hands (PH)**
  * candidate%1:18:01:: (campaigner.n.01) - a politician who is running for public office

**Agreement:** Fine: All three agree; Glite: All three agree; Maru2022 fine support: 3/3; Maru2022
Glite support: 3/3.

### A37. senseval3.d001.s039.t004

**Lemma/POS/source:** `proportion` / `NOUN` / `senseval3` (`senseval3.d001`)

**Sentence:** Finally, as shown in the table, Democrats allocate a higher **[proportion]** of their
personal staffs to district offices -- where local benefit - seeking duties matter more and national
policy making activities matter less relative to Washington offices.

**Maru2022 label**

* proportion%1:24:01:: (proportion.n.04) - the relation between things (or parts of things) with
  respect to their comparative quantity, magnitude, or degree Examples: an inordinate proportion of
  the book is given over to quotations | a dry martini has a large proportion of gin

**Reviewer verdicts**

* **Robert Farren (RF)**
  * proportion%1:24:01:: (proportion.n.04) - the relation between things (or parts of things) with
    respect to their comparative quantity, magnitude, or degree Examples: an inordinate proportion
    of the book is given over to quotations | a dry martini has a large proportion of gin
* **Patrick White (PW)**
  * proportion%1:24:01:: (proportion.n.04) - the relation between things (or parts of things) with
    respect to their comparative quantity, magnitude, or degree Examples: an inordinate proportion
    of the book is given over to quotations | a dry martini has a large proportion of gin
* **Penny Hands (PH)**
  * proportion%1:24:01:: (proportion.n.04) - the relation between things (or parts of things) with
    respect to their comparative quantity, magnitude, or degree Examples: an inordinate proportion
    of the book is given over to quotations | a dry martini has a large proportion of gin

**Agreement:** Fine: All three agree; Glite: All three agree; Maru2022 fine support: 3/3; Maru2022
Glite support: 3/3.

### A38. senseval3.d001.s041.t009

**Lemma/POS/source:** `regional` / `ADJ` / `senseval3` (`senseval3.d001`)

**Sentence:** An additional piece of evidence from the Senate: Holding other factors constant, such
as incumbency advantages and **[regional]** factors, the difference between popular votes for
Republican presidential and senatorial candidates in states conducting a Senate election turns out
to be a positive function of how onerous the federal government's tax burden is per state -LRB- a
progressive tax rate hits higher - income states harder -RRB-.

**Maru2022 label**

* regional%5:00:00:territorial:00 (regional.s.01) - related or limited to a particular region
  Examples: a regional dialect

**Reviewer verdicts**

* **Robert Farren (RF)**
  * regional%5:00:00:territorial:00 (regional.s.01) - related or limited to a particular region
    Examples: a regional dialect
* **Patrick White (PW)**
  * regional%5:00:00:territorial:00 (regional.s.01) - related or limited to a particular region
    Examples: a regional dialect
* **Penny Hands (PH)**
  * regional%5:00:00:territorial:00 (regional.s.01) - related or limited to a particular region
    Examples: a regional dialect

**Agreement:** Fine: All three agree; Glite: All three agree; Maru2022 fine support: 3/3; Maru2022
Glite support: 3/3.

### A39. senseval3.d001.s045.t011

**Lemma/POS/source:** `vote` / `NOUN` / `senseval3` (`senseval3.d001`)

**Sentence:** A cross-state econometric investigation, furthermore, reveals that, holding other
factors constant, the difference between a state's major - party **[vote]** going to the Republican
gubernatorial candidate and the Republican share of the lower state house is a positive function of
the state tax rate.

**Maru2022 label**

* vote%1:09:00:: (vote.n.05) - the total number of voters who participated Examples: they are
  expecting a large vote

**Reviewer verdicts**

* **Robert Farren (RF)**
  * vote%1:09:00:: (vote.n.05) - the total number of voters who participated Examples: they are
    expecting a large vote
* **Patrick White (PW)**
  * vote%1:09:00:: (vote.n.05) - the total number of voters who participated Examples: they are
    expecting a large vote
* **Penny Hands (PH)**
  * vote%1:09:00:: (vote.n.05) - the total number of voters who participated Examples: they are
    expecting a large vote
  * Comment: The party vote refers to the total number of votes cast.

**Agreement:** Fine: All three agree; Glite: All three agree; Maru2022 fine support: 3/3; Maru2022
Glite support: 3/3.

### A40. senseval3.d002.s106.t005

**Lemma/POS/source:** `drink` / `VERB` / `senseval3` (`senseval3.d002`)

**Sentence:** The Sunset -LCB- District -RCB- was more or less like a pajama party all evening, lots
of people &amp; dogs walking around, **[drinking]** beer.

**Maru2022 label**

* drink%2:34:00:: (drink.v.01) - take in liquids Examples: The patient must drink several liters
  each day | The children like to drink soda

**Reviewer verdicts**

* **Robert Farren (RF)**
  * drink%2:34:00:: (drink.v.01) - take in liquids Examples: The patient must drink several liters
    each day | The children like to drink soda
* **Patrick White (PW)**
  * drink%2:34:00:: (drink.v.01) - take in liquids Examples: The patient must drink several liters
    each day | The children like to drink soda
* **Penny Hands (PH)**
  * drink%2:34:00:: (drink.v.01) - take in liquids Examples: The patient must drink several liters
    each day | The children like to drink soda
  * Comment: Not sense 2 because that seems to be the intransitive sense: 'drinking' without a
    direct object means 'drinking alcohol', whereas in the text, the author is talking about taking
    in a liquid, in this case, beer.

**Agreement:** Fine: All three agree; Glite: All three agree; Maru2022 fine support: 3/3; Maru2022
Glite support: 3/3.

<a id="appendix-b"></a>

## Appendix B. All three reviewers selected the same correction

Every reviewer independently chose the same fine-grained WordNet label, and that label differs from
the Maru2022 source label. Count: 84.

### B1. semeval2013.d000.s007.t001

**Lemma/POS/source:** `negotiation` / `NOUN` / `semeval2013` (`semeval2013.d000`)

**Sentence:** Michael Zammit Cutajar, who drafted the six-page document, boiled down a 180-page
**[negotiation]** text to focus on what the U.N.'s top climate official, Yvo de Boer, described as
``the big picture.''

**Maru2022 label**

* negotiation%1:10:00:: (negotiation.n.01) - a discussion intended to produce an agreement Examples:
  the buyout negotiation lasted several days | they disagreed but kept an open dialogue

**Reviewer verdicts**

* **Robert Farren (RF)**
  * negotiation%1:04:00:: (negotiation.n.02) - the activity or business of negotiating an agreement;
    coming to terms
* **Patrick White (PW)**
  * negotiation%1:04:00:: (negotiation.n.02) - the activity or business of negotiating an agreement;
    coming to terms
* **Penny Hands (PH)**
  * negotiation%1:04:00:: (negotiation.n.02) - the activity or business of negotiating an agreement;
    coming to terms
  * Comment: A 'negotiation text' is a document that is produced as part of the negotiation process,
    describing the state of the negotiations at any point during the process. Sense 2 is more about
    the activity or process of coming to an agreement. The 'negotiation text' is the product of this
    process. I rejected sense 1 because it describes a specific event or set of talks – not the
    process involved.

**Agreement:** Fine: All three agree; Glite: All three agree; Maru2022 fine support: 0/3; Maru2022
Glite support: 3/3.

### B2. semeval2013.d000.s011.t003

**Lemma/POS/source:** `week` / `NOUN` / `semeval2013` (`semeval2013.d000`)

**Sentence:** Still, Friday featured the same sort of verbal fireworks that have dominated the talks
for the past **[week]**.

**Maru2022 label**

* week%1:28:02:: (week.n.03) - a period of seven consecutive days starting on Sunday

**Reviewer verdicts**

* **Robert Farren (RF)**
  * week%1:28:00:: (week.n.01) - any period of seven consecutive days Examples: it rained for a week
* **Patrick White (PW)**
  * week%1:28:00:: (week.n.01) - any period of seven consecutive days Examples: it rained for a week
* **Penny Hands (PH)**
  * week%1:28:00:: (week.n.01) - any period of seven consecutive days Examples: it rained for a week

**Agreement:** Fine: All three agree; Glite: All three agree; Maru2022 fine support: 0/3; Maru2022
Glite support: 3/3.

### B3. semeval2013.d000.s024.t007

**Lemma/POS/source:** `week` / `NOUN` / `semeval2013` (`semeval2013.d000`)

**Sentence:** High-level officials such as Indian environment minister Jairam Ramesh and the Chinese
vice minister stepped off planes and raced through the Bella Center's halls to closed-door meetings
and news conferences so they could stake out claims that will be arbitrated over the next
**[week]**.

**Maru2022 label**

* week%1:28:02:: (week.n.03) - a period of seven consecutive days starting on Sunday

**Reviewer verdicts**

* **Robert Farren (RF)**
  * week%1:28:00:: (week.n.01) - any period of seven consecutive days Examples: it rained for a week
* **Patrick White (PW)**
  * week%1:28:00:: (week.n.01) - any period of seven consecutive days Examples: it rained for a week
* **Penny Hands (PH)**
  * week%1:28:00:: (week.n.01) - any period of seven consecutive days Examples: it rained for a week

**Agreement:** Fine: All three agree; Glite: All three agree; Maru2022 fine support: 0/3; Maru2022
Glite support: 3/3.

### B4. semeval2013.d000.s025.t004

**Lemma/POS/source:** `show` / `NOUN` / `semeval2013` (`semeval2013.d000`)

**Sentence:** The sheer sprawl of the gathering -- where 13,000 people move in and out of the
convention center each day, guitar-playing activists put on nightly **[shows]** mocking the
countries they think are selling out, and draft proposals are passed hand-to-hand on paper rather
than via e-mail -- poses a challenge.

**Maru2022 label**

* show%1:04:00:: (show.n.01) - the act of publicly exhibiting or entertaining Examples: a remarkable
  show of skill

**Reviewer verdicts**

* **Robert Farren (RF)**
  * show%1:10:00:: (show.n.03) - a social event involving a public performance or entertainment
    Examples: they wanted to see some of the shows on Broadway
* **Patrick White (PW)**
  * show%1:10:00:: (show.n.03) - a social event involving a public performance or entertainment
    Examples: they wanted to see some of the shows on Broadway
* **Penny Hands (PH)**
  * show%1:10:00:: (show.n.03) - a social event involving a public performance or entertainment
    Examples: they wanted to see some of the shows on Broadway

**Agreement:** Fine: All three agree; Glite: All three agree; Maru2022 fine support: 0/3; Maru2022
Glite support: 3/3.

### B5. semeval2013.d000.s027.t002

**Lemma/POS/source:** `policy` / `NOUN` / `semeval2013` (`semeval2013.d000`)

**Sentence:** We 're getting into the big leagues, said Carlos Manuel Rodriguez, vice president for
global **[policy]** at Conservation International.

**Maru2022 label**

* policy%1:10:00:: (policy.n.02) - a line of argument rationalizing the course of action of a
  government Examples: they debated the policy or impolicy of the proposed legislation

**Reviewer verdicts**

* **Robert Farren (RF)**
  * policy%1:09:00:: (policy.n.01) - a plan of action adopted by an individual or social group
    Examples: it was a policy of retribution | a politician keeps changing his policies
* **Patrick White (PW)**
  * policy%1:09:00:: (policy.n.01) - a plan of action adopted by an individual or social group
    Examples: it was a policy of retribution | a politician keeps changing his policies
* **Penny Hands (PH)**
  * policy%1:09:00:: (policy.n.01) - a plan of action adopted by an individual or social group
    Examples: it was a policy of retribution | a politician keeps changing his policies
  * Comment: Sense 2 seems to be more about justification or reasoning behind decisions. I did
    hesitate about sense 1 because it only seems to define the countable sense, whereas the text
    demonstrates the uncountable use of 'policy'. Most dictionaries would give the same definition
    as here, but give the label (C, U) to cover both uses.

**Agreement:** Fine: All three agree; Glite: All three agree; Maru2022 fine support: 0/3; Maru2022
Glite support: 3/3.

### B6. semeval2013.d003.s003.t002

**Lemma/POS/source:** `field` / `NOUN` / `semeval2013` (`semeval2013.d003`)

**Sentence:** American companies walked away with stakes in just two of the 10 auctioned
**[fields]**.

**Maru2022 label**

* field%1:15:00:: (field.n.01) - a piece of land cleared of trees and usually enclosed Examples: he
  planted a field of wheat

**Reviewer verdicts**

* **Robert Farren (RF)**
  * field%1:15:05:: (field.n.14) - a geographic region (land or sea) under which something valuable
    is found Examples: the diamond fields of South Africa
* **Patrick White (PW)**
  * field%1:15:05:: (field.n.14) - a geographic region (land or sea) under which something valuable
    is found Examples: the diamond fields of South Africa
* **Penny Hands (PH)**
  * field%1:15:05:: (field.n.14) - a geographic region (land or sea) under which something valuable
    is found Examples: the diamond fields of South Africa

**Agreement:** Fine: All three agree; Glite: All three agree; Maru2022 fine support: 0/3; Maru2022
Glite support: 0/3.

### B7. semeval2013.d003.s006.t002

**Lemma/POS/source:** `field` / `NOUN` / `semeval2013` (`semeval2013.d003`)

**Sentence:** Two American companies reached deals for **[fields]** auctioned in June.

**Maru2022 label**

* field%1:15:00:: (field.n.01) - a piece of land cleared of trees and usually enclosed Examples: he
  planted a field of wheat

**Reviewer verdicts**

* **Robert Farren (RF)**
  * field%1:15:05:: (field.n.14) - a geographic region (land or sea) under which something valuable
    is found Examples: the diamond fields of South Africa
* **Patrick White (PW)**
  * field%1:15:05:: (field.n.14) - a geographic region (land or sea) under which something valuable
    is found Examples: the diamond fields of South Africa
* **Penny Hands (PH)**
  * field%1:15:05:: (field.n.14) - a geographic region (land or sea) under which something valuable
    is found Examples: the diamond fields of South Africa

**Agreement:** Fine: All three agree; Glite: All three agree; Maru2022 fine support: 0/3; Maru2022
Glite support: 0/3.

### B8. semeval2013.d003.s015.t005

**Lemma/POS/source:** `field` / `NOUN` / `semeval2013` (`semeval2013.d003`)

**Sentence:** State-owned China National Petroleum Corporation bid on more contracts than any other
company and walked away with large stakes in contracts for two major **[fields]**.

**Maru2022 label**

* field%1:15:00:: (field.n.01) - a piece of land cleared of trees and usually enclosed Examples: he
  planted a field of wheat

**Reviewer verdicts**

* **Robert Farren (RF)**
  * field%1:15:05:: (field.n.14) - a geographic region (land or sea) under which something valuable
    is found Examples: the diamond fields of South Africa
* **Patrick White (PW)**
  * field%1:15:05:: (field.n.14) - a geographic region (land or sea) under which something valuable
    is found Examples: the diamond fields of South Africa
* **Penny Hands (PH)**
  * field%1:15:05:: (field.n.14) - a geographic region (land or sea) under which something valuable
    is found Examples: the diamond fields of South Africa

**Agreement:** Fine: All three agree; Glite: All three agree; Maru2022 fine support: 0/3; Maru2022
Glite support: 0/3.

### B9. semeval2013.d003.s018.t008

**Lemma/POS/source:** `field` / `NOUN` / `semeval2013` (`semeval2013.d003`)

**Sentence:** Companies pre-selected to submit bids made offers that were then compared to the per
barrel fee the ministry was willing to pay for boosting output above current levels at each
**[field]**.

**Maru2022 label**

* field%1:15:00:: (field.n.01) - a piece of land cleared of trees and usually enclosed Examples: he
  planted a field of wheat

**Reviewer verdicts**

* **Robert Farren (RF)**
  * field%1:15:05:: (field.n.14) - a geographic region (land or sea) under which something valuable
    is found Examples: the diamond fields of South Africa
* **Patrick White (PW)**
  * field%1:15:05:: (field.n.14) - a geographic region (land or sea) under which something valuable
    is found Examples: the diamond fields of South Africa
* **Penny Hands (PH)**
  * field%1:15:05:: (field.n.14) - a geographic region (land or sea) under which something valuable
    is found Examples: the diamond fields of South Africa

**Agreement:** Fine: All three agree; Glite: All three agree; Maru2022 fine support: 0/3; Maru2022
Glite support: 0/3.

### B10. semeval2013.d004.s004.t002

**Lemma/POS/source:** `acceptance` / `NOUN` / `semeval2013` (`semeval2013.d004`)

**Sentence:** The institutions thereby want to wiggle themselves free from the restrictions going
hand-in-hand with the **[acceptance]** of the money, such as the limits on manager bonuses and the
paying of high charges.

**Maru2022 label**

* acceptance%1:04:00:: (adoption.n.01) - the act of accepting with approval; favorable reception
  Examples: its adoption by society | the proposal found wide acceptance

**Reviewer verdicts**

* **Robert Farren (RF)**
  * acceptance%1:04:03:: (acceptance.n.07) - the act of taking something that is offered Examples:
    her acceptance of the gift encouraged him | he anticipated their acceptance of his offer
* **Patrick White (PW)**
  * acceptance%1:04:03:: (acceptance.n.07) - the act of taking something that is offered Examples:
    her acceptance of the gift encouraged him | he anticipated their acceptance of his offer
* **Penny Hands (PH)**
  * acceptance%1:04:03:: (acceptance.n.07) - the act of taking something that is offered Examples:
    her acceptance of the gift encouraged him | he anticipated their acceptance of his offer

**Agreement:** Fine: All three agree; Glite: All three agree; Maru2022 fine support: 0/3; Maru2022
Glite support: 3/3.

### B11. semeval2013.d005.s010.t001

**Lemma/POS/source:** `issue` / `NOUN` / `semeval2013` (`semeval2013.d005`)

**Sentence:** But that is not likely to be the last word on the **[issue]**.

**Maru2022 label**

* issue%1:09:00:: (topic.n.02) - some situation or event that is thought about Examples: he kept
  drifting off the topic | he had been thinking about the subject for several years

**Reviewer verdicts**

* **Robert Farren (RF)**
  * issue%1:09:01:: (issue.n.01) - an important question that is in dispute and must be settled
    Examples: the issue could be settled by requiring public education for everyone | politicians
    never discuss the real issues
  * Comment: Without the five sentences that precede it, this sentence's use of the word "issue" is
    so wide open that almost all the senses are at least possible. Seen in the light of the
    preceding context, it's immediately clear that what's meant is a matter under discussion. Sense
    1 is probably the most accurate answer. But sense 3, which is more general, also seems to cover
    the sense intended in the text quite comfortably.
* **Patrick White (PW)**
  * issue%1:09:01:: (issue.n.01) - an important question that is in dispute and must be settled
    Examples: the issue could be settled by requiring public education for everyone | politicians
    never discuss the real issues
* **Penny Hands (PH)**
  * issue%1:09:01:: (issue.n.01) - an important question that is in dispute and must be settled
    Examples: the issue could be settled by requiring public education for everyone | politicians
    never discuss the real issues

**Agreement:** Fine: All three agree; Glite: All three agree; Maru2022 fine support: 0/3; Maru2022
Glite support: 3/3.

### B12. semeval2013.d005.s011.t004

**Lemma/POS/source:** `question` / `NOUN` / `semeval2013` (`semeval2013.d005`)

**Sentence:** For decades, appeals courts have recognized that coverage of notorious cases can raise
**[questions]** about a trial's fairness.

**Maru2022 label**

* question%1:10:00:: (question.n.01) - an instance of questioning Examples: there was a question
  about my training | we made inquiries of all those who were present
* question%1:10:01:: (question.n.02) - the subject matter at issue Examples: the question of disease
  merits serious discussion | under the head of minor Roman poets

**Reviewer verdicts**

* **Robert Farren (RF)**
  * question%1:07:00:: (doubt.n.02) - uncertainty about the truth or factuality or existence of
    something Examples: the dubiousness of his claim | there is no question about the validity of
    the enterprise
* **Patrick White (PW)**
  * question%1:07:00:: (doubt.n.02) - uncertainty about the truth or factuality or existence of
    something Examples: the dubiousness of his claim | there is no question about the validity of
    the enterprise
* **Penny Hands (PH)**
  * question%1:07:00:: (doubt.n.02) - uncertainty about the truth or factuality or existence of
    something Examples: the dubiousness of his claim | there is no question about the validity of
    the enterprise

**Agreement:** Fine: All three agree; Glite: All three agree; Maru2022 fine support: 0/3; Maru2022
Glite support: 0/3.

### B13. semeval2013.d005.s027.t007

**Lemma/POS/source:** `policy` / `NOUN` / `semeval2013` (`semeval2013.d005`)

**Sentence:** In interviews, some journalists said the claim that instant news was more incendiary
than reports delivered more slowly was a Luddite view that would make poor court **[policy]**
governing coverage of future trials.

**Maru2022 label**

* policy%1:10:00:: (policy.n.02) - a line of argument rationalizing the course of action of a
  government Examples: they debated the policy or impolicy of the proposed legislation

**Reviewer verdicts**

* **Robert Farren (RF)**
  * policy%1:09:00:: (policy.n.01) - a plan of action adopted by an individual or social group
    Examples: it was a policy of retribution | a politician keeps changing his policies
* **Patrick White (PW)**
  * policy%1:09:00:: (policy.n.01) - a plan of action adopted by an individual or social group
    Examples: it was a policy of retribution | a politician keeps changing his policies
* **Penny Hands (PH)**
  * policy%1:09:00:: (policy.n.01) - a plan of action adopted by an individual or social group
    Examples: it was a policy of retribution | a politician keeps changing his policies

**Agreement:** Fine: All three agree; Glite: All three agree; Maru2022 fine support: 0/3; Maru2022
Glite support: 3/3.

### B14. semeval2013.d006.s021.t005

**Lemma/POS/source:** `rule` / `NOUN` / `semeval2013` (`semeval2013.d006`)

**Sentence:** Those actions are really against the sporting spirit, which is part of the strategic
decisions that favor taking advantages allowed by the **[rules]**.

**Maru2022 label**

* rule%1:10:00:: (rule.n.03) - prescribed guide for conduct or action

**Reviewer verdicts**

* **Robert Farren (RF)**
  * rule%1:10:02:: (rule.n.08) - directions that define the way a game or sport is to be conducted
    Examples: he knew the rules of chess
* **Patrick White (PW)**
  * rule%1:10:02:: (rule.n.08) - directions that define the way a game or sport is to be conducted
    Examples: he knew the rules of chess
* **Penny Hands (PH)**
  * rule%1:10:02:: (rule.n.08) - directions that define the way a game or sport is to be conducted
    Examples: he knew the rules of chess
  * Comment: Even though I have (reasonably confidently) made a selection, I believe that this text
    is unlikely to have been written by someone with proficiency in English.

**Agreement:** Fine: All three agree; Glite: All three agree; Maru2022 fine support: 0/3; Maru2022
Glite support: 3/3.

### B15. semeval2013.d007.s010.t000

**Lemma/POS/source:** `study` / `NOUN` / `semeval2013` (`semeval2013.d007`)

**Sentence:** The **[study]** focuses on a microbe found on Earth.

**Maru2022 label**

* study%1:04:00:: (survey.n.01) - a detailed critical inspection

**Reviewer verdicts**

* **Robert Farren (RF)**
  * study%1:10:00:: (report.n.01) - a written document describing the findings of some individual or
    group Examples: this accords with the recent study by Hill and Dale
* **Patrick White (PW)**
  * study%1:10:00:: (report.n.01) - a written document describing the findings of some individual or
    group Examples: this accords with the recent study by Hill and Dale
* **Penny Hands (PH)**
  * study%1:10:00:: (report.n.01) - a written document describing the findings of some individual or
    group Examples: this accords with the recent study by Hill and Dale
  * Comment: The passage talks about the researchers' findings, a co-author and the report, so this
    is more about the paper itself and less about the process of investigating.

**Agreement:** Fine: All three agree; Glite: All three agree; Maru2022 fine support: 0/3; Maru2022
Glite support: 0/3.

### B16. semeval2013.d007.s011.t007

**Lemma/POS/source:** `discovery` / `NOUN` / `semeval2013` (`semeval2013.d007`)

**Sentence:** However, the announcement of a news conference to discuss it, which did not disclose
details of the find, generated widespread speculation on the Internet that the report would disclose
the **[discovery]** of extraterrestrial life.

**Maru2022 label**

* discovery%1:10:00:: (discovery.n.02) - something that is discovered

**Reviewer verdicts**

* **Robert Farren (RF)**
  * discovery%1:04:00:: (discovery.n.01) - the act of discovering something
* **Patrick White (PW)**
  * discovery%1:04:00:: (discovery.n.01) - the act of discovering something
* **Penny Hands (PH)**
  * discovery%1:04:00:: (discovery.n.01) - the act of discovering something

**Agreement:** Fine: All three agree; Glite: All three agree; Maru2022 fine support: 0/3; Maru2022
Glite support: 0/3.

### B17. semeval2013.d011.s001.t002

**Lemma/POS/source:** `aspect` / `NOUN` / `semeval2013` (`semeval2013.d011`)

**Sentence:** Immigration policy under Nicolas Sarkozy was criticised from various **[aspects]** a
congestion of police, legal and administrative services subjected to a policy of numbers and the
compatibility of that policy with the self-proclaimed status of the country as the country of French
human rights.

**Maru2022 label**

* aspect%1:07:02:: (aspect.n.02) - a characteristic to be considered

**Reviewer verdicts**

* **Robert Farren (RF)**
  * aspect%1:09:00:: (aspect.n.01) - a distinct feature or element in a problem Examples: he studied
    every facet of the question
* **Patrick White (PW)**
  * aspect%1:09:00:: (aspect.n.01) - a distinct feature or element in a problem Examples: he studied
    every facet of the question
* **Penny Hands (PH)**
  * aspect%1:09:00:: (aspect.n.01) - a distinct feature or element in a problem Examples: he studied
    every facet of the question
  * Comment: Sense 1 is definitely the best fit; however, the use of 'from' in the text ('from
    various aspects') suggests that that author means 'from various perspectives' or 'from the point
    of view of various groups who were involved'. Maybe this is an 'Inventory inadequate' answer,
    but I don't think any dictionary would include that sense at the entry for 'aspect'.

**Agreement:** Fine: All three agree; Glite: All three agree; Maru2022 fine support: 0/3; Maru2022
Glite support: 3/3.

### B18. semeval2013.d011.s015.t006

**Lemma/POS/source:** `shortage` / `NOUN` / `semeval2013` (`semeval2013.d011`)

**Sentence:** But experience shows that in reality immigrants are much more complementary to, rather
than replacements of, local labor, exercising trades in which there is a **[shortage]** of local
labor.

**Maru2022 label**

* shortage%1:07:00:: (deficit.n.01) - the property of being an amount by which something is less
  than expected or required Examples: new blood vessels bud out from the already dilated vascular
  bed to make up the nutritional deficit

**Reviewer verdicts**

* **Robert Farren (RF)**
  * shortage%1:26:00:: (dearth.n.01) - an acute insufficiency
* **Patrick White (PW)**
  * shortage%1:26:00:: (dearth.n.01) - an acute insufficiency
* **Penny Hands (PH)**
  * shortage%1:26:00:: (dearth.n.01) - an acute insufficiency

**Agreement:** Fine: All three agree; Glite: All three agree; Maru2022 fine support: 0/3; Maru2022
Glite support: 3/3.

### B19. semeval2013.d011.s018.t003

**Lemma/POS/source:** `shortage` / `NOUN` / `semeval2013` (`semeval2013.d011`)

**Sentence:** In the same way as a surgeon would find it difficult to work in a country with a
**[shortage]** of anaesthetists, the complementarities existing between locals and immigrants bring
it about that the arrival of immigrants has a positive effect on the pay of locals.

**Maru2022 label**

* shortage%1:07:00:: (deficit.n.01) - the property of being an amount by which something is less
  than expected or required Examples: new blood vessels bud out from the already dilated vascular
  bed to make up the nutritional deficit

**Reviewer verdicts**

* **Robert Farren (RF)**
  * shortage%1:26:00:: (dearth.n.01) - an acute insufficiency
* **Patrick White (PW)**
  * shortage%1:26:00:: (dearth.n.01) - an acute insufficiency
* **Penny Hands (PH)**
  * shortage%1:26:00:: (dearth.n.01) - an acute insufficiency

**Agreement:** Fine: All three agree; Glite: All three agree; Maru2022 fine support: 0/3; Maru2022
Glite support: 3/3.

### B20. semeval2013.d011.s020.t003

**Lemma/POS/source:** `creation` / `NOUN` / `semeval2013` (`semeval2013.d011`)

**Sentence:** And does so without taking into account the fact that the diversity contributed by
immigrants contributes to the **[creation]** of ideas and to economic growth (a large proportion of
naturalised immigrants are among American Nobel prize winners, whilst Google, Intel, Paypal, eBay
and Yahoo were all founded by immigrants).

**Maru2022 label**

* creation%1:04:01:: (initiation.n.02) - the act of starting something for the first time;
  introducing something new Examples: she looked forward to her initiation as an adult | the
  foundation of a new scientific society

**Reviewer verdicts**

* **Robert Farren (RF)**
  * creation%1:04:00:: (creation.n.01) - the human act of creating
* **Patrick White (PW)**
  * creation%1:04:00:: (creation.n.01) - the human act of creating
* **Penny Hands (PH)**
  * creation%1:04:00:: (creation.n.01) - the human act of creating

**Agreement:** Fine: All three agree; Glite: All three agree; Maru2022 fine support: 0/3; Maru2022
Glite support: 3/3.

### B21. semeval2013.d011.s022.t006

**Lemma/POS/source:** `age` / `NOUN` / `semeval2013` (`semeval2013.d011`)

**Sentence:** The World Labor Organisation estimates that for example in Germany, an immigrant
arriving at the **[age]** of 30, will make a net contribution (receipts less expenditure) of an
average of 150,000 Euros to public budgets during his lifetime.

**Maru2022 label**

* age%1:07:00:: (age.n.01) - how long something has existed Examples: it was replaced because of its
  age

**Reviewer verdicts**

* **Robert Farren (RF)**
  * age%1:28:00:: (age.n.03) - a time of life (usually defined in years) at which some particular
    qualification or power arises Examples: she was now of school age | tall for his eld
* **Patrick White (PW)**
  * age%1:28:00:: (age.n.03) - a time of life (usually defined in years) at which some particular
    qualification or power arises Examples: she was now of school age | tall for his eld
* **Penny Hands (PH)**
  * age%1:28:00:: (age.n.03) - a time of life (usually defined in years) at which some particular
    qualification or power arises Examples: she was now of school age | tall for his eld
  * Comment: The mention of 'qualification or power' in the definition for sense 3 seems a bit over
    the top/superfluous, but I opted for sense 3 because of the wording: 'a time of life (usually
    defined in years)', which is what we have in the text.

**Agreement:** Fine: All three agree; Glite: All three agree; Maru2022 fine support: 0/3; Maru2022
Glite support: 0/3.

### B22. semeval2013.d012.s002.t002

**Lemma/POS/source:** `industry` / `NOUN` / `semeval2013` (`semeval2013.d012`)

**Sentence:** As if the problems at home were not already enough for Deutsche Bank, the
**[industry]** giant's past in the USA is now also catching up with it. Frankfurt-based Deutsche
Bank will pay 145 million dollars (106 million Euros) to settle disputes arising from the bankruptcy
of five major credit unions during the financial crisis.

**Maru2022 label**

* industry%1:04:00:: (industry.n.02) - the organized action of making of goods and services for sale
  Examples: American industry is making increased use of computers to control production

**Reviewer verdicts**

* **Robert Farren (RF)**
  * industry%1:14:00:: (industry.n.01) - the people or companies engaged in a particular kind of
    commercial enterprise Examples: each industry has its own trade publications
* **Patrick White (PW)**
  * industry%1:14:00:: (industry.n.01) - the people or companies engaged in a particular kind of
    commercial enterprise Examples: each industry has its own trade publications
* **Penny Hands (PH)**
  * industry%1:14:00:: (industry.n.01) - the people or companies engaged in a particular kind of
    commercial enterprise Examples: each industry has its own trade publications

**Agreement:** Fine: All three agree; Glite: All three agree; Maru2022 fine support: 0/3; Maru2022
Glite support: 3/3.

### B23. semeval2013.d012.s003.t001

**Lemma/POS/source:** `sale` / `NOUN` / `semeval2013` (`semeval2013.d012`)

**Sentence:** The issue centres on the **[sale]** of mortgage securities.

**Maru2022 label**

* sale%1:04:00:: (sale.n.01) - a particular instance of selling Examples: he has just made his first
  sale | they had to complete the sale before the banks closed

**Reviewer verdicts**

* **Robert Farren (RF)**
  * sale%1:04:02:: (sale.n.02) - the general activity of selling Examples: they tried to boost sales
    | laws limit the sale of handguns
* **Patrick White (PW)**
  * sale%1:04:02:: (sale.n.02) - the general activity of selling Examples: they tried to boost sales
    | laws limit the sale of handguns
* **Penny Hands (PH)**
  * sale%1:04:02:: (sale.n.02) - the general activity of selling Examples: they tried to boost sales
    | laws limit the sale of handguns

**Agreement:** Fine: All three agree; Glite: All three agree; Maru2022 fine support: 0/3; Maru2022
Glite support: 3/3.

### B24. semeval2015.d000.s000.t004

**Lemma/POS/source:** `assessment` / `NOUN` / `semeval2015` (`semeval2015.d000`)

**Sentence:** This document is a summary of the European Public **[Assessment]** Report (EPAR).

**Maru2022 label**

* assessment%1:09:00:: (appraisal.n.01) - the classification of someone or something with respect to
  its worth

**Reviewer verdicts**

* **Robert Farren (RF)**
  * assessment%1:04:00:: (judgment.n.02) - the act of judging or assessing a person or situation or
    event Examples: they criticized my judgment of the contestants
* **Patrick White (PW)**
  * assessment%1:04:00:: (judgment.n.02) - the act of judging or assessing a person or situation or
    event Examples: they criticized my judgment of the contestants
* **Penny Hands (PH)**
  * assessment%1:04:00:: (judgment.n.02) - the act of judging or assessing a person or situation or
    event Examples: they criticized my judgment of the contestants
  * Comment: The difference between senses 1 and 4 is subtle. Sense 1 seems to refer to ranking
    people or things by worth, whereas sense 4 refers to the act or process of reasoning and forming
    an opinion (i.e. considering studies and making judgements about how the medicines should be
    used). Since the latter is what the EPAR report does, I selected sense 4.

**Agreement:** Fine: All three agree; Glite: All three agree; Maru2022 fine support: 0/3; Maru2022
Glite support: 3/3.

### B25. semeval2015.d000.s018.t002

**Lemma/POS/source:** `discontinue` / `VERB` / `semeval2015` (`semeval2015.d000`)

**Sentence:** Treatment should be delayed or **[discontinued]**, or the dose reduced, in patients
whose blood counts are abnormal or who have certain other side effects.

**Maru2022 label**

* discontinue%2:30:00:: (break.v.10) - prevent completion Examples: stop the project | break off the
  negotiations

**Reviewer verdicts**

* **Robert Farren (RF)**
  * discontinue%2:42:00:: (discontinue.v.01) - put an end to a state or an activity Examples: Quit
    teasing your little brother
* **Patrick White (PW)**
  * discontinue%2:42:00:: (discontinue.v.01) - put an end to a state or an activity Examples: Quit
    teasing your little brother
* **Penny Hands (PH)**
  * discontinue%2:42:00:: (discontinue.v.01) - put an end to a state or an activity Examples: Quit
    teasing your little brother
  * Comment: Senses 1 and 3 are close but I went for 1 because of the word 'prevent' in sense 3.
    There is no need to *prevent* something from being completed; doctors simply have to stop
    administering it.

**Agreement:** Fine: All three agree; Glite: All three agree; Maru2022 fine support: 0/3; Maru2022
Glite support: 0/3.

### B26. semeval2015.d000.s018.t007

**Lemma/POS/source:** `abnormal` / `ADJ` / `semeval2015` (`semeval2015.d000`)

**Sentence:** Treatment should be delayed or discontinued, or the dose reduced, in patients whose
blood counts are **[abnormal]** or who have certain other side effects.

**Maru2022 label**

* abnormal%5:00:00:immoderate:00 (abnormal.s.01) - much greater than the normal Examples: abnormal
  profits | abnormal ambition

**Reviewer verdicts**

* **Robert Farren (RF)**
  * abnormal%3:00:00:: (abnormal.a.01) - not normal; not typical or usual or regular or conforming
    to a norm Examples: abnormal powers of concentration | abnormal amounts of rain
* **Patrick White (PW)**
  * abnormal%3:00:00:: (abnormal.a.01) - not normal; not typical or usual or regular or conforming
    to a norm Examples: abnormal powers of concentration | abnormal amounts of rain
* **Penny Hands (PH)**
  * abnormal%3:00:00:: (abnormal.a.01) - not normal; not typical or usual or regular or conforming
    to a norm Examples: abnormal powers of concentration | abnormal amounts of rain

**Agreement:** Fine: All three agree; Glite: All three agree; Maru2022 fine support: 0/3; Maru2022
Glite support: 3/3.

### B27. semeval2015.d000.s036.t000

**Lemma/POS/source:** `however` / `ADV` / `semeval2015` (`semeval2015.d000`)

**Sentence:** **[However]**, in both studies, patients whose cancer was not affecting squamous cells
had longer survival times if they received Alimta than if they received the comparator.

**Maru2022 label**

* however%4:02:00:: (however.r.01) - despite anything to the contrary (usually following a
  concession) Examples: although I'm a little afraid, however I'd like to try it | while we disliked
  each other, nevertheless we agreed

**Reviewer verdicts**

* **Robert Farren (RF)**
  * however%4:02:04:: (however.r.02) - by contrast; on the other hand Examples: the first part was
    easy; the second, however, took hours
* **Patrick White (PW)**
  * however%4:02:04:: (however.r.02) - by contrast; on the other hand Examples: the first part was
    easy; the second, however, took hours
* **Penny Hands (PH)**
  * however%4:02:04:: (however.r.02) - by contrast; on the other hand Examples: the first part was
    easy; the second, however, took hours
  * Comment: Sense 1's '(usually following a concession)', together with the examples that mostly
    show concession, led me to feel that sense 2 was more suited to the use demonstrated in the
    text.

**Agreement:** Fine: All three agree; Glite: All three agree; Maru2022 fine support: 0/3; Maru2022
Glite support: 3/3.

### B28. semeval2015.d001.s026.t001

**Lemma/POS/source:** `useful` / `ADJ` / `semeval2015` (`semeval2015.d001`)

**Sentence:** Mainly **[useful]** for working with piecewise.

**Maru2022 label**

* useful%5:00:00:functional:00 (utilitarian.s.01) - having a useful function Examples: utilitarian
  steel tables

**Reviewer verdicts**

* **Robert Farren (RF)**
  * useful%3:00:00:: (useful.a.01) - being of use or service Examples: the girl felt motherly and
    useful | a useful job
* **Patrick White (PW)**
  * useful%3:00:00:: (useful.a.01) - being of use or service Examples: the girl felt motherly and
    useful | a useful job
* **Penny Hands (PH)**
  * useful%3:00:00:: (useful.a.01) - being of use or service Examples: the girl felt motherly and
    useful | a useful job

**Agreement:** Fine: All three agree; Glite: All three agree; Maru2022 fine support: 0/3; Maru2022
Glite support: 0/3.

### B29. semeval2015.d001.s027.t000

**Lemma/POS/source:** `now` / `ADV` / `semeval2015` (`semeval2015.d001`)

**Sentence:** **[Now]** you could ask me, why should the user mind about MathML?

**Maru2022 label**

* now%4:02:04:: (now.r.04) - at the present moment Examples: goods now on sale | the now-aging
  dictator

**Reviewer verdicts**

* **Robert Farren (RF)**
  * now%4:02:07:: (now.r.06) - (prefatory or transitional) indicates a change of subject or activity
    Examples: Now the next problem is...
* **Patrick White (PW)**
  * now%4:02:07:: (now.r.06) - (prefatory or transitional) indicates a change of subject or activity
    Examples: Now the next problem is...
* **Penny Hands (PH)**
  * now%4:02:07:: (now.r.06) - (prefatory or transitional) indicates a change of subject or activity
    Examples: Now the next problem is...

**Agreement:** Fine: All three agree; Glite: All three agree; Maru2022 fine support: 0/3; Maru2022
Glite support: 0/3.

### B30. semeval2015.d002.s006.t000

**Lemma/POS/source:** `study` / `NOUN` / `semeval2015` (`semeval2015.d002`)

**Sentence:** The **[study]** is based on 195 personal interviews with senior officials of the
social partners as representatives of national level peak organisations in fifteen European
countries.

**Maru2022 label**

* study%1:04:00:: (survey.n.01) - a detailed critical inspection

**Reviewer verdicts**

* **Robert Farren (RF)**
  * study%1:10:00:: (report.n.01) - a written document describing the findings of some individual or
    group Examples: this accords with the recent study by Hill and Dale
* **Patrick White (PW)**
  * study%1:10:00:: (report.n.01) - a written document describing the findings of some individual or
    group Examples: this accords with the recent study by Hill and Dale
* **Penny Hands (PH)**
  * study%1:10:00:: (report.n.01) - a written document describing the findings of some individual or
    group Examples: this accords with the recent study by Hill and Dale

**Agreement:** Fine: All three agree; Glite: All three agree; Maru2022 fine support: 0/3; Maru2022
Glite support: 0/3.

### B31. semeval2015.d002.s007.t004

**Lemma/POS/source:** `industry` / `NOUN` / `semeval2015` (`semeval2015.d002`)

**Sentence:** As important industrial sectors, the metal **[industry]** and the banking sector were
also included.

**Maru2022 label**

* industry%1:04:00:: (industry.n.02) - the organized action of making of goods and services for sale
  Examples: American industry is making increased use of computers to control production

**Reviewer verdicts**

* **Robert Farren (RF)**
  * industry%1:14:00:: (industry.n.01) - the people or companies engaged in a particular kind of
    commercial enterprise Examples: each industry has its own trade publications
* **Patrick White (PW)**
  * industry%1:14:00:: (industry.n.01) - the people or companies engaged in a particular kind of
    commercial enterprise Examples: each industry has its own trade publications
* **Penny Hands (PH)**
  * industry%1:14:00:: (industry.n.01) - the people or companies engaged in a particular kind of
    commercial enterprise Examples: each industry has its own trade publications

**Agreement:** Fine: All three agree; Glite: All three agree; Maru2022 fine support: 0/3; Maru2022
Glite support: 3/3.

### B32. semeval2015.d003.s000.t004

**Lemma/POS/source:** `assessment` / `NOUN` / `semeval2015` (`semeval2015.d003`)

**Sentence:** This document is a summary of the European Public **[Assessment]** Report.

**Maru2022 label**

* assessment%1:09:00:: (appraisal.n.01) - the classification of someone or something with respect to
  its worth

**Reviewer verdicts**

* **Robert Farren (RF)**
  * assessment%1:04:00:: (judgment.n.02) - the act of judging or assessing a person or situation or
    event Examples: they criticized my judgment of the contestants
* **Patrick White (PW)**
  * assessment%1:04:00:: (judgment.n.02) - the act of judging or assessing a person or situation or
    event Examples: they criticized my judgment of the contestants
* **Penny Hands (PH)**
  * assessment%1:04:00:: (judgment.n.02) - the act of judging or assessing a person or situation or
    event Examples: they criticized my judgment of the contestants

**Agreement:** Fine: All three agree; Glite: All three agree; Maru2022 fine support: 0/3; Maru2022
Glite support: 3/3.

### B33. semeval2015.d003.s001.t003

**Lemma/POS/source:** `product` / `NOUN` / `semeval2015` (`semeval2015.d003`)

**Sentence:** It explains how the Committee for Medicinal **[Products]** for Veterinary Use (CVMP)
assessed the studies performed, to reach their recommendations on how to use the medicine.

**Maru2022 label**

* product%1:06:00:: (product.n.02) - an artifact that has been created by someone or some process
  Examples: they improve their product every year | they export most of their agricultural
  production

**Reviewer verdicts**

* **Robert Farren (RF)**
  * product%1:06:01:: (merchandise.n.01) - commodities offered for sale Examples: good business
    depends on having good merchandise | that store offers a variety of products
* **Patrick White (PW)**
  * product%1:06:01:: (merchandise.n.01) - commodities offered for sale Examples: good business
    depends on having good merchandise | that store offers a variety of products
* **Penny Hands (PH)**
  * product%1:06:01:: (merchandise.n.01) - commodities offered for sale Examples: good business
    depends on having good merchandise | that store offers a variety of products

**Agreement:** Fine: All three agree; Glite: All three agree; Maru2022 fine support: 0/3; Maru2022
Glite support: 3/3.

### B34. semeval2015.d003.s007.t002

**Lemma/POS/source:** `stop` / `VERB` / `semeval2015` (`semeval2015.d003`)

**Sentence:** Cerenia is an anti-emetic, this means that it **[stops]** vomiting.

**Maru2022 label**

* stop%2:42:00:: (discontinue.v.01) - put an end to a state or an activity Examples: Quit teasing
  your little brother

**Reviewer verdicts**

* **Robert Farren (RF)**
  * stop%2:41:00:: (stop.v.03) - stop from happening or developing Examples: Block his election |
    Halt the process
* **Patrick White (PW)**
  * stop%2:41:00:: (stop.v.03) - stop from happening or developing Examples: Block his election |
    Halt the process
* **Penny Hands (PH)**
  * stop%2:41:00:: (stop.v.03) - stop from happening or developing Examples: Block his election |
    Halt the process
  * Comment: Sense 2 seems to be more about telling someone to stop doing something, according to
    the example and the suggested synonyms.

**Agreement:** Fine: All three agree; Glite: All three agree; Maru2022 fine support: 0/3; Maru2022
Glite support: 3/3.

### B35. semeval2015.d003.s010.t000

**Lemma/POS/source:** `purpose` / `NOUN` / `semeval2015` (`semeval2015.d003`)

**Sentence:** For these **[purposes]**, Cerenia can be given for up to five days

**Maru2022 label**

* purpose%1:09:00:: (purpose.n.01) - an anticipated outcome that is intended or that guides your
  planned actions Examples: his intent was to provide a new translation | good intentions are not
  enough

**Reviewer verdicts**

* **Robert Farren (RF)**
  * purpose%1:07:00:: (function.n.02) - what something is used for Examples: the function of an
    auger is to bore holes | ballet is beautiful but what use is it?
* **Patrick White (PW)**
  * purpose%1:07:00:: (function.n.02) - what something is used for Examples: the function of an
    auger is to bore holes | ballet is beautiful but what use is it?
* **Penny Hands (PH)**
  * purpose%1:07:00:: (function.n.02) - what something is used for Examples: the function of an
    auger is to bore holes | ballet is beautiful but what use is it?

**Agreement:** Fine: All three agree; Glite: All three agree; Maru2022 fine support: 0/3; Maru2022
Glite support: 3/3.

### B36. semeval2015.d003.s016.t008

**Lemma/POS/source:** `see` / `VERB` / `semeval2015` (`semeval2015.d003`)

**Sentence:** The results of the studies showed that Cerenia was more effective than the placebo:
less vomiting was **[seen]** in dogs that received the medicine than in dogs that received a
placebo, both in the treatment or in the prevention of vomiting.

**Maru2022 label**

* see%2:31:03:: (see.v.10) - be careful or certain to do something; make certain of something
  Examples: He verified that the valves were closed | See that the curtains are closed

**Reviewer verdicts**

* **Robert Farren (RF)**
  * see%2:39:02:: (witness.v.02) - perceive or be contemporaneous with Examples: We found
    Republicans winning the offices | You'll see a lot of cheating in this school
* **Patrick White (PW)**
  * see%2:39:02:: (witness.v.02) - perceive or be contemporaneous with Examples: We found
    Republicans winning the offices | You'll see a lot of cheating in this school
* **Penny Hands (PH)**
  * see%2:39:02:: (witness.v.02) - perceive or be contemporaneous with Examples: We found
    Republicans winning the offices | You'll see a lot of cheating in this school

**Agreement:** Fine: All three agree; Glite: All three agree; Maru2022 fine support: 0/3; Maru2022
Glite support: 0/3.

### B37. senseval2.d000.s003.t014

**Lemma/POS/source:** `call` / `VERB` / `senseval2` (`senseval2.d000`)

**Sentence:** Of all scenes that evoke rural England, this is one of the loveliest: An ancient stone
church stands amid the fields, the sound of bells cascading from its tower, **[calling]** the
faithful to evensong.

**Maru2022 label**

* call%2:41:04:: (call.v.07) - call a meeting; invite or command to meet Examples: The Wannsee
  Conference was called to discuss the `Final Solution' | The new dean calls meetings every week

**Reviewer verdicts**

* **Robert Farren (RF)**
  * call%2:32:05:: (call.v.05) - order, request, or command to come Examples: She was called into
    the director's office | Call the police!
* **Patrick White (PW)**
  * call%2:32:05:: (call.v.05) - order, request, or command to come Examples: She was called into
    the director's office | Call the police!
* **Penny Hands (PH)**
  * call%2:32:05:: (call.v.05) - order, request, or command to come Examples: She was called into
    the director's office | Call the police!
  * Comment: I selected sense 5 because it takes a human object, whereas in sense 7, it's the
    meeting or conference that is called. Sense 24 (summon or request) feels too formal and
    civic-duty-related.

**Agreement:** Fine: All three agree; Glite: All three agree; Maru2022 fine support: 0/3; Maru2022
Glite support: 3/3.

### B38. senseval2.d000.s008.t004

**Lemma/POS/source:** `remain` / `VERB` / `senseval2` (`senseval2.d000`)

**Sentence:** Now, only one local ringer **[remains]**: 64-year-old Derek Hammond.

**Maru2022 label**

* remain%2:42:03:: (stay.v.04) - continue in a place, position, or situation Examples: After
  graduation, she stayed on in Cambridge as a student adviser | Stay with me, please

**Reviewer verdicts**

* **Robert Farren (RF)**
  * remain%2:42:05:: (remain.v.03) - be left; of persons, questions, problems, results, evidence,
    etc. Examples: There remains the question of who pulled the trigger | Carter remains the only
    President in recent history under whose Presidency the U.S. did not fight a war
* **Patrick White (PW)**
  * remain%2:42:05:: (remain.v.03) - be left; of persons, questions, problems, results, evidence,
    etc. Examples: There remains the question of who pulled the trigger | Carter remains the only
    President in recent history under whose Presidency the U.S. did not fight a war
* **Penny Hands (PH)**
  * remain%2:42:05:: (remain.v.03) - be left; of persons, questions, problems, results, evidence,
    etc. Examples: There remains the question of who pulled the trigger | Carter remains the only
    President in recent history under whose Presidency the U.S. did not fight a war
  * Comment: The examples don't help much to distinguish between sense 2 and 3 because they show
    'remain' followed by a complement. I chose sense 3 because the definition 'be left' is
    substitutable for 'remain' in the text.

**Agreement:** Fine: All three agree; Glite: All three agree; Maru2022 fine support: 0/3; Maru2022
Glite support: 3/3.

### B39. senseval2.d000.s025.t001

**Lemma/POS/source:** `stand` / `VERB` / `senseval2` (`senseval2.d000`)

**Sentence:** Ten shirt-sleeved ringers **[stand]** in a circle, one foot ahead of the other in a
prize-fighter's stance, each pulling a rope that disappears through a small hole in the high ceiling
of the ringing chamber.

**Maru2022 label**

* stand%2:42:03:: (stand.v.03) - occupy a place or location, also metaphorically Examples: We stand
  on common ground

**Reviewer verdicts**

* **Robert Farren (RF)**
  * stand%2:35:00:: (stand.v.01) - be standing; be upright Examples: We had to stand for the entire
    performance!
* **Patrick White (PW)**
  * stand%2:35:00:: (stand.v.01) - be standing; be upright Examples: We had to stand for the entire
    performance!
* **Penny Hands (PH)**
  * stand%2:35:00:: (stand.v.01) - be standing; be upright Examples: We had to stand for the entire
    performance!

**Agreement:** Fine: All three agree; Glite: All three agree; Maru2022 fine support: 0/3; Maru2022
Glite support: 3/3.

### B40. senseval2.d000.s026.t006

**Lemma/POS/source:** `sound` / `NOUN` / `senseval2` (`senseval2.d000`)

**Sentence:** No one speaks, and the snaking of the ropes seems to make as much **[sound]** as the
bells themselves, muffled by the ceiling.

**Maru2022 label**

* sound%1:19:00:: (sound.n.03) - mechanical vibrations transmitted by an elastic medium Examples:
  falling trees make a sound in the forest even when no one is there to hear them

**Reviewer verdicts**

* **Robert Farren (RF)**
  * sound%1:07:00:: (sound.n.01) - the particular auditory effect produced by a given cause
    Examples: the sound of rain on the roof | the beautiful sound of music
* **Patrick White (PW)**
  * sound%1:07:00:: (sound.n.01) - the particular auditory effect produced by a given cause
    Examples: the sound of rain on the roof | the beautiful sound of music
* **Penny Hands (PH)**
  * sound%1:07:00:: (sound.n.01) - the particular auditory effect produced by a given cause
    Examples: the sound of rain on the roof | the beautiful sound of music

**Agreement:** Fine: All three agree; Glite: All three agree; Maru2022 fine support: 0/3; Maru2022
Glite support: 3/3.

### B41. senseval2.d000.s031.t003

**Lemma/POS/source:** `solemn` / `ADJ` / `senseval2` (`senseval2.d000`)

**Sentence:** Ringers, she added, are
``filled with the **[solemn]** intoxication that comes of intricate ritual faultlessly performed. ````

**Maru2022 label**

* solemn%5:00:01:serious:00 (earnest.s.01) - characterized by a firm and humorless belief in the
  validity of your opinions Examples: both sides were deeply in earnest, even passionate | an
  entirely sincere and cruel tyrant

**Reviewer verdicts**

* **Robert Farren (RF)**
  * solemn%5:00:00:serious:00 (grave.s.01) - dignified and somber in manner or character and
    committed to keeping promises Examples: a grave God-fearing man | a quiet sedate nature
* **Patrick White (PW)**
  * solemn%5:00:00:serious:00 (grave.s.01) - dignified and somber in manner or character and
    committed to keeping promises Examples: a grave God-fearing man | a quiet sedate nature
* **Penny Hands (PH)**
  * solemn%5:00:00:serious:00 (grave.s.01) - dignified and somber in manner or character and
    committed to keeping promises Examples: a grave God-fearing man | a quiet sedate nature

**Agreement:** Fine: All three agree; Glite: All three agree; Maru2022 fine support: 0/3; Maru2022
Glite support: 3/3.

### B42. senseval2.d000.s038.t004

**Lemma/POS/source:** `so` / `ADV` / `senseval2` (`senseval2.d000`)

**Sentence:** Two years ago, the Rev. Jeremy Hummerstone, vicar of Great Torrington, Devon, got
**[so]** fed up with ringers who did n't attend service he sacked the entire band; the ringers
promptly set up a picket line in protest.

**Maru2022 label**

* so%4:02:02:: (so.r.01) - to a very great extent or degree Examples: the idea is so obvious | never
  been so happy

**Reviewer verdicts**

* **Robert Farren (RF)**
  * so%4:02:03:: (so.r.07) - (usually followed by `that') to an extent or degree as expressed
    Examples: he was so tired he could hardly stand | so dirty that it smells
* **Patrick White (PW)**
  * so%4:02:03:: (so.r.07) - (usually followed by `that') to an extent or degree as expressed
    Examples: he was so tired he could hardly stand | so dirty that it smells
* **Penny Hands (PH)**
  * so%4:02:03:: (so.r.07) - (usually followed by `that') to an extent or degree as expressed
    Examples: he was so tired he could hardly stand | so dirty that it smells

**Agreement:** Fine: All three agree; Glite: All three agree; Maru2022 fine support: 0/3; Maru2022
Glite support: 3/3.

### B43. senseval2.d000.s048.t003

**Lemma/POS/source:** `draw` / `VERB` / `senseval2` (`senseval2.d000`)

**Sentence:**
`I live in hopes that the ringers themselves will be **[drawn]** into that fuller life. `

**Maru2022 label**

* draw%2:35:06:: (attract.v.01) - direct toward itself or oneself by means of some psychological
  power or physical attributes Examples: Her good looks attract the stares of many men | The ad
  pulled in many potential customers

**Reviewer verdicts**

* **Robert Farren (RF)**
  * draw%2:30:14:: (draw.v.16) - bring or lead someone to a certain action or condition Examples:
    She was drawn to despair | The President refused to be drawn into delivering an ultimatum
* **Patrick White (PW)**
  * draw%2:30:14:: (draw.v.16) - bring or lead someone to a certain action or condition Examples:
    She was drawn to despair | The President refused to be drawn into delivering an ultimatum
* **Penny Hands (PH)**
  * draw%2:30:14:: (draw.v.16) - bring or lead someone to a certain action or condition Examples:
    She was drawn to despair | The President refused to be drawn into delivering an ultimatum

**Agreement:** Fine: All three agree; Glite: All three agree; Maru2022 fine support: 0/3; Maru2022
Glite support: 0/3.

### B44. senseval2.d000.s051.t005

**Lemma/POS/source:** `high` / `ADJ` / `senseval2` (`senseval2.d000`)

**Sentence:** Says Mr. Baldwin,
`We recognize that we may no longer have as **[high]** a priority in church life and experience. `

**Maru2022 label**

* high%5:00:00:superior:01 (eminent.s.01) - standing above others in quality or position Examples:
  people in high places | the high priest

**Reviewer verdicts**

* **Robert Farren (RF)**
  * high%3:00:02:: (high.a.01) - greater than normal in degree or intensity or amount Examples: a
    high temperature | a high price
* **Patrick White (PW)**
  * high%3:00:02:: (high.a.01) - greater than normal in degree or intensity or amount Examples: a
    high temperature | a high price
* **Penny Hands (PH)**
  * high%3:00:02:: (high.a.01) - greater than normal in degree or intensity or amount Examples: a
    high temperature | a high price

**Agreement:** Fine: All three agree; Glite: All three agree; Maru2022 fine support: 0/3; Maru2022
Glite support: 0/3.

### B45. senseval2.d000.s054.t002

**Lemma/POS/source:** `always` / `ADV` / `senseval2` (`senseval2.d000`)

**Sentence:** Also, ringers do not **[always]** live where the bells need to be rung -- like in
small, rural parishes and inner-city churches.

**Maru2022 label**

* always%4:02:00:: (always.r.01) - at all times; all the time and on every occasion Examples: I will
  always be there to help you | always arrives on time

**Reviewer verdicts**

* **Robert Farren (RF)**
  * always%4:02:04:: (constantly.r.01) - without variation or change, in every case Examples:
    constantly kind and gracious | he always arrives on time
* **Patrick White (PW)**
  * always%4:02:04:: (constantly.r.01) - without variation or change, in every case Examples:
    constantly kind and gracious | he always arrives on time
* **Penny Hands (PH)**
  * always%4:02:04:: (constantly.r.01) - without variation or change, in every case Examples:
    constantly kind and gracious | he always arrives on time

**Agreement:** Fine: All three agree; Glite: All three agree; Maru2022 fine support: 0/3; Maru2022
Glite support: 3/3.

### B46. senseval2.d000.s063.t005

**Lemma/POS/source:** `know` / `VERB` / `senseval2` (`senseval2.d000`)

**Sentence:** Another women wrote from Sheffield to say that in her 60 years of ringing, ``I have
never **[known]** a lady to faint in the belfry.

**Maru2022 label**

* know%2:31:00:: (know.v.04) - be familiar or acquainted with a person or an object Examples: She
  doesn't know this composer | Do you know my sister?

**Reviewer verdicts**

* **Robert Farren (RF)**
  * know%2:31:04:: (know.v.05) - have firsthand knowledge of states, situations, emotions, or
    sensations Examples: I know the feeling! | have you ever known hunger?
* **Patrick White (PW)**
  * know%2:31:04:: (know.v.05) - have firsthand knowledge of states, situations, emotions, or
    sensations Examples: I know the feeling! | have you ever known hunger?
* **Penny Hands (PH)**
  * know%2:31:04:: (know.v.05) - have firsthand knowledge of states, situations, emotions, or
    sensations Examples: I know the feeling! | have you ever known hunger?

**Agreement:** Fine: All three agree; Glite: All three agree; Maru2022 fine support: 0/3; Maru2022
Glite support: 3/3.

### B47. senseval2.d001.s019.t015

**Lemma/POS/source:** `birth` / `NOUN` / `senseval2` (`senseval2.d001`)

**Sentence:** The Dedham, Mass., couple knew even before Bonnie became pregnant in 1987 that any
child of theirs had a 50% chance of being at risk for retinoblastoma, an eye cancer that occurs
about once every 20,000 **[births]**.

**Maru2022 label**

* birth%1:11:00:: (birth.n.02) - the event of being born Examples: they celebrated the birth of
  their first child

**Reviewer verdicts**

* **Robert Farren (RF)**
  * birth%1:18:00:: (birth.n.05) - a baby born; an offspring Examples: the overall rate of incidence
    of Down's syndrome is one in every 800 births
* **Patrick White (PW)**
  * birth%1:18:00:: (birth.n.05) - a baby born; an offspring Examples: the overall rate of incidence
    of Down's syndrome is one in every 800 births
* **Penny Hands (PH)**
  * birth%1:18:00:: (birth.n.05) - a baby born; an offspring Examples: the overall rate of incidence
    of Down's syndrome is one in every 800 births

**Agreement:** Fine: All three agree; Glite: All three agree; Maru2022 fine support: 0/3; Maru2022
Glite support: 3/3.

### B48. senseval2.d001.s041.t009

**Lemma/POS/source:** `pair` / `NOUN` / `senseval2` (`senseval2.d001`)

**Sentence:** Back then, scientists had no way of ferreting out specific genes, but under a
microscope they could see the 23 **[pairs]** of chromosomes in the cells that contain the genes.

**Maru2022 label**

* pair%1:23:00:: (couple.n.04) - two items of the same kind

**Reviewer verdicts**

* **Robert Farren (RF)**
  * pair%1:14:01:: (pair.n.01) - a set of two similar things considered as a unit
* **Patrick White (PW)**
  * pair%1:14:01:: (pair.n.01) - a set of two similar things considered as a unit
* **Penny Hands (PH)**
  * pair%1:14:01:: (pair.n.01) - a set of two similar things considered as a unit

**Agreement:** Fine: All three agree; Glite: All three agree; Maru2022 fine support: 0/3; Maru2022
Glite support: 3/3.

### B49. senseval2.d001.s045.t003

**Lemma/POS/source:** `contain` / `VERB` / `senseval2` (`senseval2.d001`)

**Sentence:** He assumed the missing piece **[contained]** a gene or genes whose loss had a critical
role in setting off the cancer.

**Maru2022 label**

* contain%2:42:13:: (hold.v.11) - contain or hold; have within Examples: The jar carries wine | The
  canteen holds fresh water

**Reviewer verdicts**

* **Robert Farren (RF)**
  * contain%2:42:00:: (incorporate.v.02) - include or contain; have as a component Examples: A
    totally new idea is comprised in this paper | The record contains many old songs from the 1930's
* **Patrick White (PW)**
  * contain%2:42:00:: (incorporate.v.02) - include or contain; have as a component Examples: A
    totally new idea is comprised in this paper | The record contains many old songs from the 1930's
* **Penny Hands (PH)**
  * contain%2:42:00:: (incorporate.v.02) - include or contain; have as a component Examples: A
    totally new idea is comprised in this paper | The record contains many old songs from the 1930's

**Agreement:** Fine: All three agree; Glite: All three agree; Maru2022 fine support: 0/3; Maru2022
Glite support: 3/3.

### B50. senseval2.d001.s060.t002

**Lemma/POS/source:** `begin` / `VERB` / `senseval2` (`senseval2.d001`)

**Sentence:** Dr. Vogelstein and a doctoral student, Eric Fearon, **[began]** months of tedious and
often frustrating probing of the chromosomes searching for signs of genetic damage.

**Maru2022 label**

* begin%2:30:01:: (begin.v.03) - set in motion, cause to start Examples: The U.S. started a war in
  the Middle East | The Iraqis began hostilities

**Reviewer verdicts**

* **Robert Farren (RF)**
  * begin%2:30:00:: (get_down.v.07) - take the first step or steps in carrying out an action
    Examples: We began working at dawn | Who will start?
* **Patrick White (PW)**
  * begin%2:30:00:: (get_down.v.07) - take the first step or steps in carrying out an action
    Examples: We began working at dawn | Who will start?
* **Penny Hands (PH)**
  * begin%2:30:00:: (get_down.v.07) - take the first step or steps in carrying out an action
    Examples: We began working at dawn | Who will start?
  * Comment: Sense 3 is also close, but sense 3's combination of definition and examples seem to be
    emphasising triggering something that then gets bigger and develops a life of its own.

**Agreement:** Fine: All three agree; Glite: All three agree; Maru2022 fine support: 0/3; Maru2022
Glite support: 3/3.

### B51. senseval2.d001.s062.t004

**Lemma/POS/source:** `development` / `NOUN` / `senseval2` (`senseval2.d001`)

**Sentence:** Gradually, a coherent picture of cancer **[development]** emerged.

**Maru2022 label**

* development%1:22:01:: (growth.n.01) - (biology) the process of an individual organism growing
  organically; a purely biological unfolding of events involved in an organism changing gradually
  from a simple to a more complex level Examples: he proposed an indicator of osseous development in
  children

**Reviewer verdicts**

* **Robert Farren (RF)**
  * development%1:22:02:: (development.n.02) - a process in which something passes by degrees to a
    different stage (especially a more advanced or mature stage) Examples: the development of his
    ideas took many years | the evolution of Greek civilization
* **Patrick White (PW)**
  * development%1:22:02:: (development.n.02) - a process in which something passes by degrees to a
    different stage (especially a more advanced or mature stage) Examples: the development of his
    ideas took many years | the evolution of Greek civilization
* **Penny Hands (PH)**
  * development%1:22:02:: (development.n.02) - a process in which something passes by degrees to a
    different stage (especially a more advanced or mature stage) Examples: the development of his
    ideas took many years | the evolution of Greek civilization
  * Comment: Sense 2 works better for talking about the progression of the disease. Sense 3 is more
    about natural development, e.g. of a foetus, or from a child to an adult.

**Agreement:** Fine: All three agree; Glite: All three agree; Maru2022 fine support: 0/3; Maru2022
Glite support: 0/3.

### B52. senseval2.d001.s067.t006

**Lemma/POS/source:** `development` / `NOUN` / `senseval2` (`senseval2.d001`)

**Sentence:**
`It was the confirming evidence we all needed that gene losses were critical to the **[development]** of a common tumor, `says
Ray White at Howard Hughes Medical Institute in Salt Lake City.

**Maru2022 label**

* development%1:22:01:: (growth.n.01) - (biology) the process of an individual organism growing
  organically; a purely biological unfolding of events involved in an organism changing gradually
  from a simple to a more complex level Examples: he proposed an indicator of osseous development in
  children

**Reviewer verdicts**

* **Robert Farren (RF)**
  * development%1:22:02:: (development.n.02) - a process in which something passes by degrees to a
    different stage (especially a more advanced or mature stage) Examples: the development of his
    ideas took many years | the evolution of Greek civilization
* **Patrick White (PW)**
  * development%1:22:02:: (development.n.02) - a process in which something passes by degrees to a
    different stage (especially a more advanced or mature stage) Examples: the development of his
    ideas took many years | the evolution of Greek civilization
* **Penny Hands (PH)**
  * development%1:22:02:: (development.n.02) - a process in which something passes by degrees to a
    different stage (especially a more advanced or mature stage) Examples: the development of his
    ideas took many years | the evolution of Greek civilization
  * Comment: I think sense 3 is about a natural developmental process, e.g. a child into an adult.

**Agreement:** Fine: All three agree; Glite: All three agree; Maru2022 fine support: 0/3; Maru2022
Glite support: 0/3.

### B53. senseval2.d001.s082.t011

**Lemma/POS/source:** `test` / `VERB` / `senseval2` (`senseval2.d001`)

**Sentence:** In a report out last week, John Minna and colleagues at the National Cancer Institute
say that about half the cells taken from lung cancer tissue they **[tested]** are missing this gene.

**Maru2022 label**

* test%2:41:01:: (screen.v.01) - test or examine for the presence of disease or infection Examples:
  screen the blood for the HIV virus

**Reviewer verdicts**

* **Robert Farren (RF)**
  * test%2:32:08:: (test.v.06) - determine the presence or properties of (a substance)
* **Patrick White (PW)**
  * test%2:32:08:: (test.v.06) - determine the presence or properties of (a substance)
* **Penny Hands (PH)**
  * test%2:32:08:: (test.v.06) - determine the presence or properties of (a substance)
  * Comment: Not sense 2 because they weren't testing the tissue for disease; they were trying to
    determine the presence of a particular gene.

**Agreement:** Fine: All three agree; Glite: All three agree; Maru2022 fine support: 0/3; Maru2022
Glite support: 3/3.

### B54. senseval2.d002.s003.t005

**Lemma/POS/source:** `relinquish` / `VERB` / `senseval2` (`senseval2.d002`)

**Sentence:** And the reason we do not want to is that effective education would require us to
**[relinquish]** some cherished metaphysical beliefs about human nature in general and the human
nature of young people in particular, well as to violate some cherished vested interests.

**Maru2022 label**

* relinquish%2:40:00:: (foreswear.v.02) - turn away from; give up Examples: I am foreswearing women
  forever

**Reviewer verdicts**

* **Robert Farren (RF)**
  * relinquish%2:41:00:: (waive.v.01) - do without or cease to hold or adhere to Examples: We are
    dispensing with formalities | relinquish the old ideas
* **Patrick White (PW)**
  * relinquish%2:41:00:: (waive.v.01) - do without or cease to hold or adhere to Examples: We are
    dispensing with formalities | relinquish the old ideas
* **Penny Hands (PH)**
  * relinquish%2:41:00:: (waive.v.01) - do without or cease to hold or adhere to Examples: We are
    dispensing with formalities | relinquish the old ideas
  * Comment: Sense 3 is more about deliberate rejection. Sense 2 (my choice) suggests letting go.
    Not sense 1 because a belief is not a possession or right.

**Agreement:** Fine: All three agree; Glite: All three agree; Maru2022 fine support: 0/3; Maru2022
Glite support: 3/3.

### B55. senseval2.d002.s004.t001

**Lemma/POS/source:** `so` / `ADV` / `senseval2` (`senseval2.d002`)

**Sentence:** These beliefs **[so]** dominate our educational establishment, our media, our
politicians, and even our parents that it seems almost blasphemous to challenge them.

**Maru2022 label**

* so%4:02:02:: (so.r.01) - to a very great extent or degree Examples: the idea is so obvious | never
  been so happy

**Reviewer verdicts**

* **Robert Farren (RF)**
  * so%4:02:03:: (so.r.07) - (usually followed by `that') to an extent or degree as expressed
    Examples: he was so tired he could hardly stand | so dirty that it smells
* **Patrick White (PW)**
  * so%4:02:03:: (so.r.07) - (usually followed by `that') to an extent or degree as expressed
    Examples: he was so tired he could hardly stand | so dirty that it smells
* **Penny Hands (PH)**
  * so%4:02:03:: (so.r.07) - (usually followed by `that') to an extent or degree as expressed
    Examples: he was so tired he could hardly stand | so dirty that it smells

**Agreement:** Fine: All three agree; Glite: All three agree; Maru2022 fine support: 0/3; Maru2022
Glite support: 3/3.

### B56. senseval2.d002.s011.t009

**Lemma/POS/source:** `authoritarian` / `ADJ` / `senseval2` (`senseval2.d002`)

**Sentence:** The whole notion of `creativity `in education was (and is) part and parcel of a
romantic rebellion against disciplined instruction, which was (and is) regarded as
`**[authoritarian]**, `a repression and frustration of the latent talents and the wonderful, if as
yet undefined, potentialities inherent in the souls of all our children.

**Maru2022 label**

* authoritarian%5:00:00:undemocratic:00 (authoritarian.s.01) - characteristic of an absolute ruler
  or absolute rule; having absolute sovereignty Examples: an authoritarian regime | autocratic
  government

**Reviewer verdicts**

* **Robert Farren (RF)**
  * authoritarian%5:00:00:domineering:00 (authoritarian.s.02) - expecting unquestioning obedience
    Examples: the timid child of authoritarian parents | insufferably overbearing behavior toward
    the waiter
* **Patrick White (PW)**
  * authoritarian%5:00:00:domineering:00 (authoritarian.s.02) - expecting unquestioning obedience
    Examples: the timid child of authoritarian parents | insufferably overbearing behavior toward
    the waiter
* **Penny Hands (PH)**
  * authoritarian%5:00:00:domineering:00 (authoritarian.s.02) - expecting unquestioning obedience
    Examples: the timid child of authoritarian parents | insufferably overbearing behavior toward
    the waiter

**Agreement:** Fine: All three agree; Glite: All three agree; Maru2022 fine support: 0/3; Maru2022
Glite support: 3/3.

### B57. senseval2.d002.s011.t019

**Lemma/POS/source:** `inherent` / `ADJ` / `senseval2` (`senseval2.d002`)

**Sentence:** The whole notion of `creativity `in education was (and is) part and parcel of a
romantic rebellion against disciplined instruction, which was (and is) regarded as
`authoritarian, `a repression and frustration of the latent talents and the wonderful, if as yet
undefined, potentialities **[inherent]** in the souls of all our children.

**Maru2022 label**

* inherent%5:00:00:implicit:00 (implicit_in.s.01) - in the nature of something though not readily
  apparent Examples: shortcomings inherent in our approach | an underlying meaning

**Reviewer verdicts**

* **Robert Farren (RF)**
  * inherent%5:00:00:intrinsic:00 (built-in.s.01) - existing as an essential constituent or
    characteristic Examples: the Ptolemaic system with its built-in concept of periodicity | a
    constitutional inability to tell the truth
* **Patrick White (PW)**
  * inherent%5:00:00:intrinsic:00 (built-in.s.01) - existing as an essential constituent or
    characteristic Examples: the Ptolemaic system with its built-in concept of periodicity | a
    constitutional inability to tell the truth
* **Penny Hands (PH)**
  * inherent%5:00:00:intrinsic:00 (built-in.s.01) - existing as an essential constituent or
    characteristic Examples: the Ptolemaic system with its built-in concept of periodicity | a
    constitutional inability to tell the truth
  * Comment: According to the author, these characteristics are essential constituents of what these
    children are – they are naturally present in them (Sense 1). However, they are also qualities
    that exist within children by their nature — and they are not immediately visible, or readily
    apparent (sense 2). So senses 1 and 2 both work for this one. I opted for sense 1 because the
    author's aim does not seem to be to emphasise the fact that these characteristics are invisible.

**Agreement:** Fine: All three agree; Glite: All three agree; Maru2022 fine support: 0/3; Maru2022
Glite support: 3/3.

### B58. senseval2.d002.s042.t000

**Lemma/POS/source:** `really` / `ADV` / `senseval2` (`senseval2.d002`)

**Sentence:** We **[really]** do know all we need to know, if only we could assimilate this
knowledge into our thinking.

**Maru2022 label**

* really%4:02:03:: (truly.r.01) - in accordance with truth or fact or reality Examples: she was now
  truly American | a genuinely open society

**Reviewer verdicts**

* **Robert Farren (RF)**
  * really%4:02:02:: (in_truth.r.01) - in fact (used as intensifiers or sentence modifiers)
    Examples: in truth, moral decay hastened the decline of the Roman Empire | really, you shouldn't
    have done it
* **Patrick White (PW)**
  * really%4:02:02:: (in_truth.r.01) - in fact (used as intensifiers or sentence modifiers)
    Examples: in truth, moral decay hastened the decline of the Roman Empire | really, you shouldn't
    have done it
* **Penny Hands (PH)**
  * really%4:02:02:: (in_truth.r.01) - in fact (used as intensifiers or sentence modifiers)
    Examples: in truth, moral decay hastened the decline of the Roman Empire | really, you shouldn't
    have done it
  * Comment: Sense 3 describes 'really' as an intensifier, insisting on a fact that is already
    understood or accepted. Sense 2 is more about disabusing people of a misunderstanding, and sense
    1 is about emphasising that a description (American, open society) is accurate.

**Agreement:** Fine: All three agree; Glite: All three agree; Maru2022 fine support: 0/3; Maru2022
Glite support: 3/3.

### B59. senseval2.d002.s042.t002

**Lemma/POS/source:** `need` / `VERB` / `senseval2` (`senseval2.d002`)

**Sentence:** We really do know all we **[need]** to know, if only we could assimilate this
knowledge into our thinking.

**Maru2022 label**

* need%2:34:01:: (need.v.03) - have or feel a need for Examples: always needing friends and money

**Reviewer verdicts**

* **Robert Farren (RF)**
  * need%2:42:00:: (necessitate.v.01) - require as useful, just, or proper Examples: It takes nerve
    to do what she did | success usually requires hard work
* **Patrick White (PW)**
  * need%2:42:00:: (necessitate.v.01) - require as useful, just, or proper Examples: It takes nerve
    to do what she did | success usually requires hard work
* **Penny Hands (PH)**
  * need%2:42:00:: (necessitate.v.01) - require as useful, just, or proper Examples: It takes nerve
    to do what she did | success usually requires hard work

**Agreement:** Fine: All three agree; Glite: All three agree; Maru2022 fine support: 0/3; Maru2022
Glite support: 3/3.

### B60. senseval2.d002.s058.t002

**Lemma/POS/source:** `system` / `NOUN` / `senseval2` (`senseval2.d002`)

**Sentence:** New York is in the process of trying to disengage itself from a 20-year-old commitment
to this **[system]** of school governance, even as Chicago and other cities are moving to institute
it.

**Maru2022 label**

* system%1:14:00:: (system.n.02) - a group of independent but interrelated elements comprising a
  unified whole Examples: a vast system of production and distribution and consumption keep the
  country going

**Reviewer verdicts**

* **Robert Farren (RF)**
  * system%1:09:00:: (system.n.04) - a complex of methods or rules governing behavior Examples: they
    have to operate under a system they oppose | that language has a complex system for indicating
    gender
* **Patrick White (PW)**
  * system%1:09:00:: (system.n.04) - a complex of methods or rules governing behavior Examples: they
    have to operate under a system they oppose | that language has a complex system for indicating
    gender
* **Penny Hands (PH)**
  * system%1:09:00:: (system.n.04) - a complex of methods or rules governing behavior Examples: they
    have to operate under a system they oppose | that language has a complex system for indicating
    gender
  * Comment: School governance is specifically about rules and hierarchies. Sense 2 seems to be more
    general (e.g. how an economy works, or an ecosystem, for example).

**Agreement:** Fine: All three agree; Glite: All three agree; Maru2022 fine support: 0/3; Maru2022
Glite support: 0/3.

### B61. senseval2.d002.s070.t001

**Lemma/POS/source:** `believe` / `VERB` / `senseval2` (`senseval2.d002`)

**Sentence:** No one in his right mind actually **[believes]** that we all have an equal academic
potential.

**Maru2022 label**

* believe%2:31:03:: (believe.v.03) - be confident about something Examples: I believe that he will
  come back from the war

**Reviewer verdicts**

* **Robert Farren (RF)**
  * believe%2:31:00:: (believe.v.01) - accept as true; take to be true Examples: I believed his
    report | We didn't believe his stories from the War
* **Patrick White (PW)**
  * believe%2:31:00:: (believe.v.01) - accept as true; take to be true Examples: I believed his
    report | We didn't believe his stories from the War
* **Penny Hands (PH)**
  * believe%2:31:00:: (believe.v.01) - accept as true; take to be true Examples: I believed his
    report | We didn't believe his stories from the War

**Agreement:** Fine: All three agree; Glite: All three agree; Maru2022 fine support: 0/3; Maru2022
Glite support: 3/3.

### B62. senseval2.d002.s080.t000

**Lemma/POS/source:** `fact` / `NOUN` / `senseval2` (`senseval2.d002`)

**Sentence:** This is a **[fact]** -- though, in view of all the feathers that are ruffled by this
fact, it is not surprising that one hears so little about it.

**Maru2022 label**

* fact%1:09:01:: (fact.n.01) - a piece of information about circumstances that exist or events that
  have occurred Examples: first you must collect all the facts of the case

**Reviewer verdicts**

* **Robert Farren (RF)**
  * fact%1:10:01:: (fact.n.02) - a statement or assertion of verified information about something
    that is the case or has happened Examples: he supported his argument with an impressive array of
    facts
  * Comment: Arguably, sense 4 is even more apt, since in using the word "fact" the writer is trying
    to invest his narrative as objectively, inherently true; presenting a statement of opinion
    (which may well be demonstrable with data) as a "fact".
* **Patrick White (PW)**
  * fact%1:10:01:: (fact.n.02) - a statement or assertion of verified information about something
    that is the case or has happened Examples: he supported his argument with an impressive array of
    facts
* **Penny Hands (PH)**
  * fact%1:10:01:: (fact.n.02) - a statement or assertion of verified information about something
    that is the case or has happened Examples: he supported his argument with an impressive array of
    facts

**Agreement:** Fine: All three agree; Glite: All three agree; Maru2022 fine support: 0/3; Maru2022
Glite support: 3/3.

### B63. senseval2.d002.s080.t002

**Lemma/POS/source:** `fact` / `NOUN` / `senseval2` (`senseval2.d002`)

**Sentence:** This is a fact -- though, in view of all the feathers that are ruffled by this
**[fact]**, it is not surprising that one hears so little about it.

**Maru2022 label**

* fact%1:09:01:: (fact.n.01) - a piece of information about circumstances that exist or events that
  have occurred Examples: first you must collect all the facts of the case

**Reviewer verdicts**

* **Robert Farren (RF)**
  * fact%1:10:01:: (fact.n.02) - a statement or assertion of verified information about something
    that is the case or has happened Examples: he supported his argument with an impressive array of
    facts
* **Patrick White (PW)**
  * fact%1:10:01:: (fact.n.02) - a statement or assertion of verified information about something
    that is the case or has happened Examples: he supported his argument with an impressive array of
    facts
* **Penny Hands (PH)**
  * fact%1:10:01:: (fact.n.02) - a statement or assertion of verified information about something
    that is the case or has happened Examples: he supported his argument with an impressive array of
    facts
  * Comment: Sense 2 mentions a statement or assertion, which is what we have in the text.

**Agreement:** Fine: All three agree; Glite: All three agree; Maru2022 fine support: 0/3; Maru2022
Glite support: 3/3.

### B64. senseval3.d000.s006.t005

**Lemma/POS/source:** `cold` / `ADJ` / `senseval3` (`senseval3.d000`)

**Sentence:** Eyes that were clear, but also bright with a strange intensity, a sort of **[cold]**
fire burning behind them.

**Maru2022 label**

* cold%3:00:01:: (cold.a.01) - having a low or inadequate temperature or feeling a sensation of
  coldness or having been made cold by e.g. ice or refrigeration Examples: a cold climate | a cold
  room

**Reviewer verdicts**

* **Robert Farren (RF)**
  * cold%3:00:02:: (cold.a.02) - extended meanings; especially of psychological coldness; without
    human warmth or emotion Examples: a cold unfriendly nod | a cold and unaffectionate person
* **Patrick White (PW)**
  * cold%3:00:02:: (cold.a.02) - extended meanings; especially of psychological coldness; without
    human warmth or emotion Examples: a cold unfriendly nod | a cold and unaffectionate person
  * Comment: Poetic/figurative usage makes it hard to be precise in sense attribution
* **Penny Hands (PH)**
  * cold%3:00:02:: (cold.a.02) - extended meanings; especially of psychological coldness; without
    human warmth or emotion Examples: a cold unfriendly nod | a cold and unaffectionate person

**Agreement:** Fine: All three agree; Glite: All three agree; Maru2022 fine support: 0/3; Maru2022
Glite support: 0/3.

### B65. senseval3.d000.s030.t004

**Lemma/POS/source:** `uneasy` / `ADJ` / `senseval3` (`senseval3.d000`)

**Sentence:** He really did n't take the offer seriously, but he began to feel **[uneasy]**.

**Maru2022 label**

* uneasy%5:00:00:uncomfortable:01 (awkward.s.05) - socially uncomfortable; unsure and constrained in
  manner Examples: awkward and reserved at parties | ill at ease among eddies of people he didn't
  know

**Reviewer verdicts**

* **Robert Farren (RF)**
  * uneasy%3:00:00:: (uneasy.a.01) - lacking a sense of security or affording no ease or reassurance
    Examples: farmers were uneasy until rain finally came | uneasy about his health
* **Patrick White (PW)**
  * uneasy%3:00:00:: (uneasy.a.01) - lacking a sense of security or affording no ease or reassurance
    Examples: farmers were uneasy until rain finally came | uneasy about his health
* **Penny Hands (PH)**
  * uneasy%3:00:00:: (uneasy.a.01) - lacking a sense of security or affording no ease or reassurance
    Examples: farmers were uneasy until rain finally came | uneasy about his health

**Agreement:** Fine: All three agree; Glite: All three agree; Maru2022 fine support: 0/3; Maru2022
Glite support: 3/3.

### B66. senseval3.d000.s135.t000

**Lemma/POS/source:** `do` / `VERB` / `senseval3` (`senseval3.d000`)

**Sentence:** That's why I -- why I **[do]** a free job now and then.

**Maru2022 label**

* do%2:41:01:: (make.v.01) - engage in Examples: make love, not war | make an effort

**Reviewer verdicts**

* **Robert Farren (RF)**
  * do%2:36:01:: (perform.v.01) - carry out or perform an action Examples: John did the painting,
    the weeding, and he cleaned out the gutters | the skater executed a triple pirouette
* **Patrick White (PW)**
  * do%2:36:01:: (perform.v.01) - carry out or perform an action Examples: John did the painting,
    the weeding, and he cleaned out the gutters | the skater executed a triple pirouette
* **Penny Hands (PH)**
  * do%2:36:01:: (perform.v.01) - carry out or perform an action Examples: John did the painting,
    the weeding, and he cleaned out the gutters | the skater executed a triple pirouette

**Agreement:** Fine: All three agree; Glite: All three agree; Maru2022 fine support: 0/3; Maru2022
Glite support: 3/3.

### B67. senseval3.d000.s138.t000

**Lemma/POS/source:** `wild` / `ADJ` / `senseval3` (`senseval3.d000`)

**Sentence:** Then a **[wild]** thought ran circles through his clouded brain.

**Maru2022 label**

* wild%3:00:02:: (wild.a.01) - marked by extreme lack of restraint or control Examples: wild talk |
  wild parties

**Reviewer verdicts**

* **Robert Farren (RF)**
  * wild%5:00:00:unrealistic:00 (fantastic.s.03) - fanciful and unrealistic; foolish Examples: a
    fantastic idea of his own importance
* **Patrick White (PW)**
  * wild%5:00:00:unrealistic:00 (fantastic.s.03) - fanciful and unrealistic; foolish Examples: a
    fantastic idea of his own importance
* **Penny Hands (PH)**
  * wild%5:00:00:unrealistic:00 (fantastic.s.03) - fanciful and unrealistic; foolish Examples: a
    fantastic idea of his own importance
  * Comment: Because it 'ran circles' around his brain, it could also be sense 1; however, sense 9
    is specifically about fanciful thoughts, so I opted for that.

**Agreement:** Fine: All three agree; Glite: All three agree; Maru2022 fine support: 0/3; Maru2022
Glite support: 0/3.

### B68. senseval3.d001.s013.t004

**Lemma/POS/source:** `benefit` / `NOUN` / `senseval3` (`senseval3.d001`)

**Sentence:** If they put a Republican into office, not only will they acquire less in terms of
local **[benefits]** but their selected legislator will be relatively powerless to prevent other
legislators from `bringing home the bacon `to their respective constituencies.

**Maru2022 label**

* benefit%1:21:00:: (benefit.n.01) - financial assistance in time of need

**Reviewer verdicts**

* **Robert Farren (RF)**
  * benefit%1:07:00:: (benefit.n.02) - something that aids or promotes well-being Examples: for the
    benefit of all
* **Patrick White (PW)**
  * benefit%1:07:00:: (benefit.n.02) - something that aids or promotes well-being Examples: for the
    benefit of all
* **Penny Hands (PH)**
  * benefit%1:07:00:: (benefit.n.02) - something that aids or promotes well-being Examples: for the
    benefit of all
  * Comment: It may well involve money (sense 1), but it could be other things, such as better
    working conditions.

**Agreement:** Fine: All three agree; Glite: All three agree; Maru2022 fine support: 0/3; Maru2022
Glite support: 0/3.

### B69. senseval3.d001.s016.t003

**Lemma/POS/source:** `benefit` / `NOUN` / `senseval3` (`senseval3.d001`)

**Sentence:** Although a GOP president may limit local **[benefits]** to the voter's particular
district/state, such a president is also likely to be more effective at preventing other
districts/states and their legislators from bringing home the local benefits.

**Maru2022 label**

* benefit%1:21:00:: (benefit.n.01) - financial assistance in time of need

**Reviewer verdicts**

* **Robert Farren (RF)**
  * benefit%1:07:00:: (benefit.n.02) - something that aids or promotes well-being Examples: for the
    benefit of all
* **Patrick White (PW)**
  * benefit%1:07:00:: (benefit.n.02) - something that aids or promotes well-being Examples: for the
    benefit of all
* **Penny Hands (PH)**
  * benefit%1:07:00:: (benefit.n.02) - something that aids or promotes well-being Examples: for the
    benefit of all

**Agreement:** Fine: All three agree; Glite: All three agree; Maru2022 fine support: 0/3; Maru2022
Glite support: 0/3.

### B70. senseval3.d001.s016.t017

**Lemma/POS/source:** `benefit` / `NOUN` / `senseval3` (`senseval3.d001`)

**Sentence:** Although a GOP president may limit local benefits to the voter's particular
district/state, such a president is also likely to be more effective at preventing other
districts/states and their legislators from bringing home the local **[benefits]**.

**Maru2022 label**

* benefit%1:21:00:: (benefit.n.01) - financial assistance in time of need

**Reviewer verdicts**

* **Robert Farren (RF)**
  * benefit%1:07:00:: (benefit.n.02) - something that aids or promotes well-being Examples: for the
    benefit of all
* **Patrick White (PW)**
  * benefit%1:07:00:: (benefit.n.02) - something that aids or promotes well-being Examples: for the
    benefit of all
* **Penny Hands (PH)**
  * benefit%1:07:00:: (benefit.n.02) - something that aids or promotes well-being Examples: for the
    benefit of all

**Agreement:** Fine: All three agree; Glite: All three agree; Maru2022 fine support: 0/3; Maru2022
Glite support: 0/3.

### B71. senseval3.d001.s018.t002

**Lemma/POS/source:** `appear` / `VERB` / `senseval3` (`senseval3.d001`)

**Sentence:** While this theory is exceedingly simple, it **[appears]** to explain several things.

**Maru2022 label**

* appear%2:39:01:: (appear.v.04) - seem to be true, probable, or apparent Examples: It seems that he
  is very gifted | It appears that the weather in California is very bad

**Reviewer verdicts**

* **Robert Farren (RF)**
  * appear%2:39:00:: (look.v.02) - give a certain impression or have a certain outward aspect
    Examples: She seems to be sleeping | This appears to be a very difficult problem
* **Patrick White (PW)**
  * appear%2:39:00:: (look.v.02) - give a certain impression or have a certain outward aspect
    Examples: She seems to be sleeping | This appears to be a very difficult problem
* **Penny Hands (PH)**
  * appear%2:39:00:: (look.v.02) - give a certain impression or have a certain outward aspect
    Examples: She seems to be sleeping | This appears to be a very difficult problem

**Agreement:** Fine: All three agree; Glite: All three agree; Maru2022 fine support: 0/3; Maru2022
Glite support: 3/3.

### B72. senseval3.d001.s020.t013

**Lemma/POS/source:** `benefit` / `NOUN` / `senseval3` (`senseval3.d001`)

**Sentence:** Second, it explains why voters hold Congress in disdain but generally love their own
congressional representatives: Any individual legislator's constituents appreciate the specific
**[benefits]** that the legislator wins for them but not the overall cost associated with every
other legislator doing likewise for his own constituency.

**Maru2022 label**

* benefit%1:21:00:: (benefit.n.01) - financial assistance in time of need

**Reviewer verdicts**

* **Robert Farren (RF)**
  * benefit%1:07:00:: (benefit.n.02) - something that aids or promotes well-being Examples: for the
    benefit of all
* **Patrick White (PW)**
  * benefit%1:07:00:: (benefit.n.02) - something that aids or promotes well-being Examples: for the
    benefit of all
* **Penny Hands (PH)**
  * benefit%1:07:00:: (benefit.n.02) - something that aids or promotes well-being Examples: for the
    benefit of all

**Agreement:** Fine: All three agree; Glite: All three agree; Maru2022 fine support: 0/3; Maru2022
Glite support: 0/3.

### B73. senseval3.d001.s029.t011

**Lemma/POS/source:** `benefit` / `NOUN` / `senseval3` (`senseval3.d001`)

**Sentence:** To the extent that Democratic legislators from the South have held a disproportionate
share of power in Congress since 1932 and have been able to translate such clout into relatively
more local **[benefits]** for their respective constituencies, voters in the South have had an
especially strong incentive to keep such Democrats in office.

**Maru2022 label**

* benefit%1:21:00:: (benefit.n.01) - financial assistance in time of need

**Reviewer verdicts**

* **Robert Farren (RF)**
  * benefit%1:07:00:: (benefit.n.02) - something that aids or promotes well-being Examples: for the
    benefit of all
* **Patrick White (PW)**
  * benefit%1:07:00:: (benefit.n.02) - something that aids or promotes well-being Examples: for the
    benefit of all
* **Penny Hands (PH)**
  * benefit%1:07:00:: (benefit.n.02) - something that aids or promotes well-being Examples: for the
    benefit of all

**Agreement:** Fine: All three agree; Glite: All three agree; Maru2022 fine support: 0/3; Maru2022
Glite support: 0/3.

### B74. senseval3.d001.s036.t007

**Lemma/POS/source:** `rate` / `NOUN` / `senseval3` (`senseval3.d001`)

**Sentence:** Second, if the key assumption is valid, Democrats should have lower attendance
**[rates]** on roll-call votes than Republicans do to the extent that such votes reflect national
policy making and that participating in such votes takes away from the time a legislator could
otherwise devote to local benefit - seeking.

**Maru2022 label**

* rate%1:28:00:: (rate.n.01) - a magnitude or frequency relative to a time unit Examples: they
  traveled at a rate of 55 miles per hour | the rate of change was faster than expected

**Reviewer verdicts**

* **Robert Farren (RF)**
  * rate%1:24:00:: (rate.n.04) - a quantity or amount or measure considered as a proportion of
    another quantity or amount or measure Examples: the literacy rate | the retention rate
* **Patrick White (PW)**
  * rate%1:24:00:: (rate.n.04) - a quantity or amount or measure considered as a proportion of
    another quantity or amount or measure Examples: the literacy rate | the retention rate
* **Penny Hands (PH)**
  * rate%1:24:00:: (rate.n.04) - a quantity or amount or measure considered as a proportion of
    another quantity or amount or measure Examples: the literacy rate | the retention rate
  * Comment: I rejected sense 1 because the attendance rate is not measured by time unit; it's
    measured as a proportion of votes attended (sense 4).

**Agreement:** Fine: All three agree; Glite: All three agree; Maru2022 fine support: 0/3; Maru2022
Glite support: 3/3.

### B75. senseval3.d001.s036.t023

**Lemma/POS/source:** `devote` / `VERB` / `senseval3` (`senseval3.d001`)

**Sentence:** Second, if the key assumption is valid, Democrats should have lower attendance rates
on roll-call votes than Republicans do to the extent that such votes reflect national policy making
and that participating in such votes takes away from the time a legislator could otherwise
**[devote]** to local benefit - seeking.

**Maru2022 label**

* devote%2:32:00:: (give.v.18) - give entirely to a specific person, activity, or cause Examples:
  She committed herself to the work of God | give one's talents to a good cause

**Reviewer verdicts**

* **Robert Farren (RF)**
  * devote%2:40:00:: (devote.v.03) - set aside or apart for a specific purpose or use Examples: this
    land was devoted to mining
  * Comment: Pretty strange definitions. The Concise Oxford defines this sense as "give time or
    resources to (a person or activity)", which seems much clearer.
* **Patrick White (PW)**
  * devote%2:40:00:: (devote.v.03) - set aside or apart for a specific purpose or use Examples: this
    land was devoted to mining
* **Penny Hands (PH)**
  * devote%2:40:00:: (devote.v.03) - set aside or apart for a specific purpose or use Examples: this
    land was devoted to mining
  * Comment: Sense 1 feels more moral or spiritual, involving giving oneself up entirely to
    something. Sense 2 is close, but seems to be more about paying attention to things rather than
    actually doing anything. Sense 3 is best because it suggests setting aside resources: time
    (mentioned in the text) is a resource.

**Agreement:** Fine: All three agree; Glite: All three agree; Maru2022 fine support: 0/3; Maru2022
Glite support: 3/3.

### B76. senseval3.d001.s038.t002

**Lemma/POS/source:** `rate` / `NOUN` / `senseval3` (`senseval3.d001`)

**Sentence:** The Democratic House attendance **[rate]** has not exceeded the Republican House
attendance rate since 1959.

**Maru2022 label**

* rate%1:28:00:: (rate.n.01) - a magnitude or frequency relative to a time unit Examples: they
  traveled at a rate of 55 miles per hour | the rate of change was faster than expected

**Reviewer verdicts**

* **Robert Farren (RF)**
  * rate%1:24:00:: (rate.n.04) - a quantity or amount or measure considered as a proportion of
    another quantity or amount or measure Examples: the literacy rate | the retention rate
* **Patrick White (PW)**
  * rate%1:24:00:: (rate.n.04) - a quantity or amount or measure considered as a proportion of
    another quantity or amount or measure Examples: the literacy rate | the retention rate
* **Penny Hands (PH)**
  * rate%1:24:00:: (rate.n.04) - a quantity or amount or measure considered as a proportion of
    another quantity or amount or measure Examples: the literacy rate | the retention rate
  * Comment: See reasoning at previous instance.

**Agreement:** Fine: All three agree; Glite: All three agree; Maru2022 fine support: 0/3; Maru2022
Glite support: 3/3.

### B77. senseval3.d001.s038.t006

**Lemma/POS/source:** `rate` / `NOUN` / `senseval3` (`senseval3.d001`)

**Sentence:** The Democratic House attendance rate has not exceeded the Republican House attendance
**[rate]** since 1959.

**Maru2022 label**

* rate%1:28:00:: (rate.n.01) - a magnitude or frequency relative to a time unit Examples: they
  traveled at a rate of 55 miles per hour | the rate of change was faster than expected

**Reviewer verdicts**

* **Robert Farren (RF)**
  * rate%1:24:00:: (rate.n.04) - a quantity or amount or measure considered as a proportion of
    another quantity or amount or measure Examples: the literacy rate | the retention rate
* **Patrick White (PW)**
  * rate%1:24:00:: (rate.n.04) - a quantity or amount or measure considered as a proportion of
    another quantity or amount or measure Examples: the literacy rate | the retention rate
* **Penny Hands (PH)**
  * rate%1:24:00:: (rate.n.04) - a quantity or amount or measure considered as a proportion of
    another quantity or amount or measure Examples: the literacy rate | the retention rate
  * Comment: See reasoning at previous instance.

**Agreement:** Fine: All three agree; Glite: All three agree; Maru2022 fine support: 0/3; Maru2022
Glite support: 3/3.

### B78. senseval3.d001.s041.t011

**Lemma/POS/source:** `difference` / `NOUN` / `senseval3` (`senseval3.d001`)

**Sentence:** An additional piece of evidence from the Senate: Holding other factors constant, such
as incumbency advantages and regional factors, the **[difference]** between popular votes for
Republican presidential and senatorial candidates in states conducting a Senate election turns out
to be a positive function of how onerous the federal government's tax burden is per state -LRB- a
progressive tax rate hits higher - income states harder -RRB-.

**Maru2022 label**

* difference%1:07:00:: (difference.n.01) - the quality of being unlike or dissimilar Examples: there
  are many differences between jazz and rock

**Reviewer verdicts**

* **Robert Farren (RF)**
  * difference%1:23:00:: (remainder.n.03) - the number that remains after subtraction; the number
    that when added to the subtrahend gives the minuend
* **Patrick White (PW)**
  * difference%1:23:00:: (remainder.n.03) - the number that remains after subtraction; the number
    that when added to the subtrahend gives the minuend
* **Penny Hands (PH)**
  * difference%1:23:00:: (remainder.n.03) - the number that remains after subtraction; the number
    that when added to the subtrahend gives the minuend

**Agreement:** Fine: All three agree; Glite: All three agree; Maru2022 fine support: 0/3; Maru2022
Glite support: 3/3.

### B79. senseval3.d001.s041.t028

**Lemma/POS/source:** `state` / `NOUN` / `senseval3` (`senseval3.d001`)

**Sentence:** An additional piece of evidence from the Senate: Holding other factors constant, such
as incumbency advantages and regional factors, the difference between popular votes for Republican
presidential and senatorial candidates in states conducting a Senate election turns out to be a
positive function of how onerous the federal government's tax burden is per **[state]** -LRB- a
progressive tax rate hits higher - income states harder -RRB-.

**Maru2022 label**

* state%1:14:00:: (state.n.04) - a politically organized body of people under a single government
  Examples: the state has elected a new president | African nations

**Reviewer verdicts**

* **Robert Farren (RF)**
  * state%1:15:01:: (state.n.01) - the territory occupied by one of the constituent administrative
    districts of a nation Examples: his state is in the deep south
* **Patrick White (PW)**
  * state%1:15:01:: (state.n.01) - the territory occupied by one of the constituent administrative
    districts of a nation Examples: his state is in the deep south
* **Penny Hands (PH)**
  * state%1:15:01:: (state.n.01) - the territory occupied by one of the constituent administrative
    districts of a nation Examples: his state is in the deep south

**Agreement:** Fine: All three agree; Glite: All three agree; Maru2022 fine support: 0/3; Maru2022
Glite support: 3/3.

### B80. senseval3.d001.s041.t034

**Lemma/POS/source:** `state` / `NOUN` / `senseval3` (`senseval3.d001`)

**Sentence:** An additional piece of evidence from the Senate: Holding other factors constant, such
as incumbency advantages and regional factors, the difference between popular votes for Republican
presidential and senatorial candidates in states conducting a Senate election turns out to be a
positive function of how onerous the federal government's tax burden is per state -LRB- a
progressive tax rate hits higher - income **[states]** harder -RRB-.

**Maru2022 label**

* state%1:14:00:: (state.n.04) - a politically organized body of people under a single government
  Examples: the state has elected a new president | African nations

**Reviewer verdicts**

* **Robert Farren (RF)**
  * state%1:15:01:: (state.n.01) - the territory occupied by one of the constituent administrative
    districts of a nation Examples: his state is in the deep south
* **Patrick White (PW)**
  * state%1:15:01:: (state.n.01) - the territory occupied by one of the constituent administrative
    districts of a nation Examples: his state is in the deep south
* **Penny Hands (PH)**
  * state%1:15:01:: (state.n.01) - the territory occupied by one of the constituent administrative
    districts of a nation Examples: his state is in the deep south

**Agreement:** Fine: All three agree; Glite: All three agree; Maru2022 fine support: 0/3; Maru2022
Glite support: 3/3.

### B81. senseval3.d001.s045.t007

**Lemma/POS/source:** `difference` / `NOUN` / `senseval3` (`senseval3.d001`)

**Sentence:** A cross-state econometric investigation, furthermore, reveals that, holding other
factors constant, the **[difference]** between a state's major - party vote going to the Republican
gubernatorial candidate and the Republican share of the lower state house is a positive function of
the state tax rate.

**Maru2022 label**

* difference%1:07:00:: (difference.n.01) - the quality of being unlike or dissimilar Examples: there
  are many differences between jazz and rock

**Reviewer verdicts**

* **Robert Farren (RF)**
  * difference%1:23:00:: (remainder.n.03) - the number that remains after subtraction; the number
    that when added to the subtrahend gives the minuend
* **Patrick White (PW)**
  * difference%1:23:00:: (remainder.n.03) - the number that remains after subtraction; the number
    that when added to the subtrahend gives the minuend
* **Penny Hands (PH)**
  * difference%1:23:00:: (remainder.n.03) - the number that remains after subtraction; the number
    that when added to the subtrahend gives the minuend
  * Comment: Even though sense 5 is written in mathematical terms, this is the best definition of
    what is described in the text.

**Agreement:** Fine: All three agree; Glite: All three agree; Maru2022 fine support: 0/3; Maru2022
Glite support: 3/3.

### B82. senseval3.d001.s045.t008

**Lemma/POS/source:** `state` / `NOUN` / `senseval3` (`senseval3.d001`)

**Sentence:** A cross-state econometric investigation, furthermore, reveals that, holding other
factors constant, the difference between a **[state]**'s major - party vote going to the Republican
gubernatorial candidate and the Republican share of the lower state house is a positive function of
the state tax rate.

**Maru2022 label**

* state%1:14:00:: (state.n.04) - a politically organized body of people under a single government
  Examples: the state has elected a new president | African nations

**Reviewer verdicts**

* **Robert Farren (RF)**
  * state%1:15:01:: (state.n.01) - the territory occupied by one of the constituent administrative
    districts of a nation Examples: his state is in the deep south
* **Patrick White (PW)**
  * state%1:15:01:: (state.n.01) - the territory occupied by one of the constituent administrative
    districts of a nation Examples: his state is in the deep south
* **Penny Hands (PH)**
  * state%1:15:01:: (state.n.01) - the territory occupied by one of the constituent administrative
    districts of a nation Examples: his state is in the deep south

**Agreement:** Fine: All three agree; Glite: All three agree; Maru2022 fine support: 0/3; Maru2022
Glite support: 3/3.

### B83. senseval3.d001.s045.t022

**Lemma/POS/source:** `state` / `NOUN` / `senseval3` (`senseval3.d001`)

**Sentence:** A cross-state econometric investigation, furthermore, reveals that, holding other
factors constant, the difference between a state's major - party vote going to the Republican
gubernatorial candidate and the Republican share of the lower state house is a positive function of
the **[state]** tax rate.

**Maru2022 label**

* state%1:14:00:: (state.n.04) - a politically organized body of people under a single government
  Examples: the state has elected a new president | African nations
* state%1:14:01:: (state.n.03) - the group of people comprising the government of a sovereign state
  Examples: the state has lowered its income tax

**Reviewer verdicts**

* **Robert Farren (RF)**
  * state%1:15:01:: (state.n.01) - the territory occupied by one of the constituent administrative
    districts of a nation Examples: his state is in the deep south
* **Patrick White (PW)**
  * state%1:15:01:: (state.n.01) - the territory occupied by one of the constituent administrative
    districts of a nation Examples: his state is in the deep south
* **Penny Hands (PH)**
  * state%1:15:01:: (state.n.01) - the territory occupied by one of the constituent administrative
    districts of a nation Examples: his state is in the deep south

**Agreement:** Fine: All three agree; Glite: All three agree; Maru2022 fine support: 0/3; Maru2022
Glite support: 0/3.

### B84. senseval3.d002.s091.t004

**Lemma/POS/source:** `do` / `VERB` / `senseval3` (`senseval3.d002`)

**Sentence:** Power is back on, and UCSF -LCB- medical center -RCB- seems to have quieted down for
the night -LRB- they were **[doing]** triage out in the parking lot from the sound and lights of it
-RRB-.

**Maru2022 label**

* do%2:41:01:: (make.v.01) - engage in Examples: make love, not war | make an effort

**Reviewer verdicts**

* **Robert Farren (RF)**
  * do%2:36:01:: (perform.v.01) - carry out or perform an action Examples: John did the painting,
    the weeding, and he cleaned out the gutters | the skater executed a triple pirouette
* **Patrick White (PW)**
  * do%2:36:01:: (perform.v.01) - carry out or perform an action Examples: John did the painting,
    the weeding, and he cleaned out the gutters | the skater executed a triple pirouette
* **Penny Hands (PH)**
  * do%2:36:01:: (perform.v.01) - carry out or perform an action Examples: John did the painting,
    the weeding, and he cleaned out the gutters | the skater executed a triple pirouette
  * Comment: I chose sense 2 because it seems to be more specific, involving performing a particular
    task. However, I did wonder if sense 2 was meant to define 'do' in the sense of completing or
    accomplishing a specific task, since all the examples seem to suggest this. If the definition of
    sense 2 had mentioned the idea of completion, I would have gone for sense 1.

**Agreement:** Fine: All three agree; Glite: All three agree; Maru2022 fine support: 0/3; Maru2022
Glite support: 3/3.

<a id="appendix-c"></a>

## Appendix C. All three reviewers judged the item unanswerable

All reviewers used a cannot-answer judgement rather than choosing a WordNet sense. These items are
removed from the lexEN benchmark. Count: 5.

### C1. semeval2013.d006.s021.t001

**Lemma/POS/source:** `spirit` / `NOUN` / `semeval2013` (`semeval2013.d006`)

**Sentence:** Those actions are really against the sporting **[spirit]**, which is part of the
strategic decisions that favor taking advantages allowed by the rules.

**Maru2022 label**

* spirit%1:26:00:: (spirit.n.02) - the general atmosphere of a place or situation and the effect
  that it has on people Examples: the feel of the city excited him | a clergyman improved the tone
  of the meeting

**Reviewer verdicts**

* **Robert Farren (RF)**
  * Cannot answer: no sense applies
  * Note: From the Concise Oxford: "the prevailing or typical quality or mood". None of the senses
    listed above really works for the sentence, though sense 2 is the closest.
* **Patrick White (PW)**
  * Cannot answer: input defective
  * Note: Input text is non-natural English.
* **Penny Hands (PH)**
  * Cannot answer: inventory inadequate
  * Note: Sense 3 is close to the correct sense, but it only seems to refer to a person's character
    ('... determining one's character'). In the text, the author is referring to how we expect
    people to think and behave when playing sports. The definition should be something like 'the
    values and principles that determine how someone approaches something'.

**Agreement:** Fine: All three agree; Glite: All three agree; Maru2022 fine support: 0/3; Maru2022
Glite support: 0/3.

### C2. semeval2013.d011.s022.t008

**Lemma/POS/source:** `receipt` / `NOUN` / `semeval2013` (`semeval2013.d011`)

**Sentence:** The World Labor Organisation estimates that for example in Germany, an immigrant
arriving at the age of 30, will make a net contribution (**[receipts]** less expenditure) of an
average of 150,000 Euros to public budgets during his lifetime.

**Maru2022 label**

* receipt%1:10:00:: (receipt.n.02) - an acknowledgment (usually tangible) that payment has been made

**Reviewer verdicts**

* **Robert Farren (RF)**
  * Cannot answer: no sense applies
  * Note: This sense is usually or always plural, and means "the amount of money received", in this
    case by the public exchequer.
* **Patrick White (PW)**
  * Cannot answer: no sense applies
  * Note: Sense is money received
* **Penny Hands (PH)**
  * Cannot answer: no sense applies
  * Note: The correct sense would be '[plural] money that a business or person receives'.

**Agreement:** Fine: All three agree; Glite: All three agree; Maru2022 fine support: 0/3; Maru2022
Glite support: 0/3.

### C3. senseval2.d002.s043.t004

**Lemma/POS/source:** `mute` / `ADJ` / `senseval2` (`senseval2.d002`)

**Sentence:** In this respect, it would be helpful if our political leaders were **[mute]**, rather
than eloquently `concerned. `

**Maru2022 label**

* mute%5:00:01:inarticulate:00 (dumb.s.04) - unable to speak because of hereditary deafness

**Reviewer verdicts**

* **Robert Farren (RF)**
  * Cannot answer: no sense applies
  * Note: Figurative sense of "mute", meaning "silent, not saying anything", though out of choice
    rather than inability. Of a person rather than a communication or a feeling (or an animal).
* **Patrick White (PW)**
  * Cannot answer: no sense applies
  * Note: (of a person) choosing to be silent
* **Penny Hands (PH)**
  * Cannot answer: inventory inadequate
  * Note: Sense 1 omits to mention that a *person* may choose not to express themselves through
    speech. There are no examples with a human noun.

**Agreement:** Fine: All three agree; Glite: All three agree; Maru2022 fine support: 0/3; Maru2022
Glite support: 0/3.

### C4. senseval2.d002.s058.t005

**Lemma/POS/source:** `even` / `ADV` / `senseval2` (`senseval2.d002`)

**Sentence:** New York is in the process of trying to disengage itself from a 20-year-old commitment
to this system of school governance, **[even]** as Chicago and other cities are moving to institute
it.

**Maru2022 label**

* even%4:02:03:: (even.r.02) - in spite of; notwithstanding Examples: even when he is sick, he works
  | even with his head start she caught up with him

**Reviewer verdicts**

* **Robert Farren (RF)**
  * Cannot answer: no sense applies
  * Note: In this sentence, "even" is part of the phrase "even as", meaning "at the very same time
    as" (Concise Oxford). None of the senses listed come close to this.
* **Patrick White (PW)**
  * Cannot answer: inventory inadequate
  * Note: "evan as" is a fixed phrase meaning "at the same time as"
* **Penny Hands (PH)**
  * Cannot answer: no sense applies
  * Note: 'Even as' is a phrase which means 'just at the same time as something else happens', which
    is not covered in the inventory.

**Agreement:** Fine: All three agree; Glite: All three agree; Maru2022 fine support: 0/3; Maru2022
Glite support: 0/3.

### C5. senseval3.d000.s106.t007

**Lemma/POS/source:** `smile` / `VERB` / `senseval3` (`senseval3.d000`)

**Sentence:** He looked up with bloodshot eyes and beheld the stranger sitting across the table,
**[smiling]** a secret smile at him, as if they were fellow conspirators.

**Maru2022 label**

* smile%2:32:00:: (smile.v.02) - express with a smile Examples: She smiled her thanks

**Reviewer verdicts**

* **Robert Farren (RF)**
  * Cannot answer: no sense applies
  * Note: The stative sense "to be smiling, to have a smile on one's face" is missing. Sense 1
    specifies "change one's facial expression..." etc., so it's not stative. This usage in this
    particular sentence, "smiling a smile", obviously contains a redundancy, but it appears to
    underlyingly be about the stative sense that I've just described. Probably with an additional
    suggestion of intentionality.
* **Patrick White (PW)**
  * Cannot answer: inventory inadequate
  * Note: tautologous usage for stylistic effect. Neither of the WordNet senses allows for the noun
    "smile" as the object of the verb "smile"
* **Penny Hands (PH)**
  * Cannot answer: inventory inadequate
  * Note: Sense 1 seems to be about the intransitive sense of 'smile'. Sense 2 is very close because
    it covers the transitive sense of 'smile'. However, you don't 'express *a smile* with a smile'
    so it doesn't quite fit.

This use should be defined as 'to give a smile of a particular type'.

**Agreement:** Fine: All three agree; Glite: All three agree; Maru2022 fine support: 0/3; Maru2022
Glite support: 0/3.

<a id="appendix-d"></a>

## Appendix D. Two reviewers selected the same sense

Exactly two reviewers agreed on a fine-grained WordNet label and the third reviewer gave a different
answer. Count: 183.

### D1. semeval2013.d000.s006.t003

**Lemma/POS/source:** `washington` / `NOUN` / `semeval2013` (`semeval2013.d000`)

**Sentence:** It gives a lot of flexibility to the process, said John Coequyt, senior
**[Washington]** representative for the Sierra Club.

**Maru2022 label**

* washington%1:14:00:: (capital.n.06) - the federal government of the United States

**Reviewer verdicts**

* **Robert Farren (RF)**
  * washington%1:15:01:: (washington.n.01) - the capital of the United States in the District of
    Columbia and a tourist mecca; George Washington commissioned Charles L'Enfant to lay out the
    city in 1791
* **Patrick White (PW)**
  * washington%1:15:01:: (washington.n.01) - the capital of the United States in the District of
    Columbia and a tourist mecca; George Washington commissioned Charles L'Enfant to lay out the
    city in 1791
* **Penny Hands (PH)**
  * washington%1:14:00:: (capital.n.06) - the federal government of the United States

**Agreement:** Fine: Exactly two agree; Glite: Exactly two agree; Maru2022 fine support: 1/3;
Maru2022 Glite support: 1/3.

### D2. semeval2013.d001.s001.t003

**Lemma/POS/source:** `loss` / `NOUN` / `semeval2013` (`semeval2013.d001`)

**Sentence:** Caja Laboral achieved a stunning 82-91 victory on their visit to the Maccabee Electra
court despite Dusko Ivanovic's team's heavy **[losses]**, and after the great performance by Mizra
Teltovic, who was the best on his team with eight three-pointers scored (29 points), they now at the
top of their group.

**Maru2022 label**

* loss%1:04:00:: (loss.n.03) - the act of losing someone or something Examples: everyone expected
  him to win so his loss was a shock

**Reviewer verdicts**

* **Robert Farren (RF)**
  * loss%1:04:00:: (loss.n.03) - the act of losing someone or something Examples: everyone expected
    him to win so his loss was a shock
* **Patrick White (PW)**
  * loss%1:04:00:: (loss.n.03) - the act of losing someone or something Examples: everyone expected
    him to win so his loss was a shock
  * Comment: This text reads like it was written by a non-native. "Losses" here refers to players
    who were unable to play in the team, as is clear from the following paragraph. It's not natural
    English.
* **Penny Hands (PH)**
  * Cannot answer: no sense applies
  * Note: The sense demonstrated in the text is 'a failure to win a contest', which is not covered
    by the WordNet inventory.

**Agreement:** Fine: Exactly two agree; Glite: Exactly two agree; Maru2022 fine support: 2/3;
Maru2022 Glite support: 2/3.

### D3. semeval2013.d003.s010.t005

**Lemma/POS/source:** `u.s.` / `NOUN` / `semeval2013` (`semeval2013.d003`)

**Sentence:** Concerns over security, underscored by massive coordinated bombings Tuesday, and
political instability as the **[U.S.]** military withdraws, likely kept American oil companies from
venturing more forcefully in Iraq, which has the world's third-largest proven crude reserves,
analysts said.

**Maru2022 label**

* u.s.%1:15:00:: (united_states.n.01) - North American republic containing 50 states - 48
  conterminous states in North America plus Alaska in northwest North America and the Hawaiian
  Islands in the Pacific Ocean; achieved independence in 1776

**Reviewer verdicts**

* **Robert Farren (RF)**
  * u.s.%1:14:00:: (united_states_government.n.01) - the executive and legislative and judicial
    branches of the federal government of the United States
  * Comment: I feel that sense 1 is closer. The "US military" doesn't mean the "military from the
    United States". The adjunct has the same role in "US military" as in "US president", "US
    Senate", "US Supreme Court", etc.
* **Patrick White (PW)**
  * u.s.%1:14:00:: (united_states_government.n.01) - the executive and legislative and judicial
    branches of the federal government of the United States
* **Penny Hands (PH)**
  * u.s.%1:15:00:: (united_states.n.01) - North American republic containing 50 states - 48
    conterminous states in North America plus Alaska in northwest North America and the Hawaiian
    Islands in the Pacific Ocean; achieved independence in 1776
  * Comment: Sense 1 is close because the military belongs to the US government. But I think the
    text refers to the military as part of the country as a whole.

**Agreement:** Fine: Exactly two agree; Glite: Exactly two agree; Maru2022 fine support: 1/3;
Maru2022 Glite support: 1/3.

### D4. semeval2013.d004.s010.t003

**Lemma/POS/source:** `capital` / `NOUN` / `semeval2013` (`semeval2013.d004`)

**Sentence:** Already on Thursday, the US bank was able to announce a **[capital]** increase of some
USD 20 billion, reported CNBC with reference to circles.

**Maru2022 label**

* capital%1:21:01:: (capital.n.01) - assets available for use in the production of further assets

**Reviewer verdicts**

* **Robert Farren (RF)**
  * capital%1:21:01:: (capital.n.01) - assets available for use in the production of further assets
* **Patrick White (PW)**
  * capital%1:21:00:: (capital.n.02) - wealth in the form of money or property owned by a person or
    business and human resources of economic value
* **Penny Hands (PH)**
  * capital%1:21:00:: (capital.n.02) - wealth in the form of money or property owned by a person or
    business and human resources of economic value

**Agreement:** Fine: Exactly two agree; Glite: All three agree; Maru2022 fine support: 1/3; Maru2022
Glite support: 3/3.

### D5. semeval2013.d005.s004.t003

**Lemma/POS/source:** `family` / `NOUN` / `semeval2013` (`semeval2013.d005`)

**Sentence:** On Thursday, the widely followed trial of Steven J. Hayes, who was convicted of
killing three members of a Cheshire, Conn., **[family]**, is set to come to an official end with the
judge's imposition of the death sentence voted for by the jury.

**Maru2022 label**

* family%1:14:02:: (family.n.01) - a social unit living together Examples: he moved his family to
  Virginia | It was a good Christian household

**Reviewer verdicts**

* **Robert Farren (RF)**
  * family%1:14:00:: (family.n.02) - primary social group; parents and children Examples: he wanted
    to have a good job before starting a family
  * family%1:14:02:: (family.n.01) - a social unit living together Examples: he moved his family to
    Virginia | It was a good Christian household
  * Comment: The text doesn't give enough information to disambiguate between the two senses chosen
    (further research shows that both senses are in fact equally applicable).
* **Patrick White (PW)**
  * family%1:14:00:: (family.n.02) - primary social group; parents and children Examples: he wanted
    to have a good job before starting a family
  * family%1:14:02:: (family.n.01) - a social unit living together Examples: he moved his family to
    Virginia | It was a good Christian household
  * Comment: Ambiguous as to whether group living together, or parents/children, or indeed extended
    family members
* **Penny Hands (PH)**
  * Cannot answer: inventory inadequate
  * Note: Sense 2 is the closest but it's too restrictive – the family in the text was not
    necessarily just parents and children – it might have included aunts, uncles, cousins or
    grandparents. The definition at sense 2 should read 'primary social group; parents, children and
    close relations'.

**Agreement:** Fine: Exactly two agree; Glite: Exactly two agree; Maru2022 fine support: 0/3;
Maru2022 Glite support: 2/3.

### D6. semeval2013.d005.s005.t004

**Lemma/POS/source:** `argument` / `NOUN` / `semeval2013` (`semeval2013.d005`)

**Sentence:** But lawyers for Mr. Hayes have already made court filings that sketch out appeals
**[arguments]** that are likely to occupy the courts for years.

**Maru2022 label**

* argument%1:10:02:: (argument.n.01) - a fact or assertion offered as evidence that something is
  true Examples: it was a strong argument that his hypothesis was true

**Reviewer verdicts**

* **Robert Farren (RF)**
  * argument%1:10:02:: (argument.n.01) - a fact or assertion offered as evidence that something is
    true Examples: it was a strong argument that his hypothesis was true
* **Patrick White (PW)**
  * argument%1:10:02:: (argument.n.01) - a fact or assertion offered as evidence that something is
    true Examples: it was a strong argument that his hypothesis was true
* **Penny Hands (PH)**
  * argument%1:09:01:: (argumentation.n.02) - a course of reasoning aimed at demonstrating a truth
    or falsehood; the methodical process of logical reasoning Examples: I can't follow your line of
    reasoning
  * Comment: The use of 'sketch out' in the text suggests that they explained their line of
    reasoning and didn't simply list assertions.

**Agreement:** Fine: Exactly two agree; Glite: All three agree; Maru2022 fine support: 2/3; Maru2022
Glite support: 3/3.

### D7. semeval2013.d005.s009.t007

**Lemma/POS/source:** `evidence` / `NOUN` / `semeval2013` (`semeval2013.d005`)

**Sentence:** The trial judge, Jon C. Blue of State Superior Court, tersely rejected the claims in a
ruling last week, saying that the news media were ``carefully controlled'' and that there was no
**[evidence]** the jury was driven by passion.

**Maru2022 label**

* evidence%1:10:00:: (evidence.n.03) - (law) all the means by which any alleged matter of fact whose
  truth is investigated at judicial trial is established or disproved

**Reviewer verdicts**

* **Robert Farren (RF)**
  * evidence%1:09:00:: (evidence.n.01) - your basis for belief or disbelief; knowledge on which to
    base belief Examples: the evidence that smoking causes lung cancer is very compelling
  * Comment: Despite the fact that this use of the word "evidence" is used by a judge in a ruling,
    the intended sense is not the legal one (sense 3). What's under discussion is not evidence
    presented as part of a trial with a view to securing a verdict.
* **Patrick White (PW)**
  * evidence%1:09:00:: (evidence.n.01) - your basis for belief or disbelief; knowledge on which to
    base belief Examples: the evidence that smoking causes lung cancer is very compelling
* **Penny Hands (PH)**
  * evidence%1:10:00:: (evidence.n.03) - (law) all the means by which any alleged matter of fact
    whose truth is investigated at judicial trial is established or disproved
  * Comment: Sense 1 would have worked too, but the context is a court ruling with a judge, so I've
    opted for the more specific sense (3).

**Agreement:** Fine: Exactly two agree; Glite: All three agree; Maru2022 fine support: 1/3; Maru2022
Glite support: 3/3.

### D8. semeval2013.d006.s000.t002

**Lemma/POS/source:** `law` / `NOUN` / `semeval2013` (`semeval2013.d006`)

**Sentence:** Sport and fraud **[law]**

**Maru2022 label**

* law%1:10:00:: (law.n.02) - legal document setting forth rules governing a particular kind of
  activity Examples: there is a law against kidnapping

**Reviewer verdicts**

* **Robert Farren (RF)**
  * Cannot answer: no sense applies
  * Note: This sense of "law", modified by an adjective or a noun adjunct, normally means the
    ensemble of legislation relevant to a specific field. As in company law, planning law, family
    law, etc.
* **Patrick White (PW)**
  * law%1:14:00:: (law.n.01) - the collection of rules imposed by authority Examples: civilization
    presupposes respect for the law | the great problem for jurisprudence to allow freedom while
    enforcing order
  * Comment: But input text is non-natural English.
* **Penny Hands (PH)**
  * law%1:14:00:: (law.n.01) - the collection of rules imposed by authority Examples: civilization
    presupposes respect for the law | the great problem for jurisprudence to allow freedom while
    enforcing order

**Agreement:** Fine: Exactly two agree; Glite: Exactly two agree; Maru2022 fine support: 0/3;
Maru2022 Glite support: 2/3.

### D9. semeval2013.d006.s006.t004

**Lemma/POS/source:** `world` / `NOUN` / `semeval2013` (`semeval2013.d006`)

**Sentence:** The provocation of a yellow card in similar circumstances as this one is not a new
practice, but rather frequent in the **[world]** of football.

**Maru2022 label**

* world%1:17:02:: (world.n.06) - a part of the earth that can be considered separately Examples: the
  outdoor world | the world of insects

**Reviewer verdicts**

* **Robert Farren (RF)**
  * Cannot answer: no sense applies
  * Note: "The world of football" is a particular milieu, like the "world of finance", etc. The term
    doesn't refer only to people, but to organizations, clubs that are run like businesses, a
    system, a complex body of rules and conventions. There's no sense given here that comes close to
    this.
* **Patrick White (PW)**
  * world%1:14:01:: (world.n.02) - people in general; especially a distinctive group of people with
    some shared interest Examples: the Western world
* **Penny Hands (PH)**
  * world%1:14:01:: (world.n.02) - people in general; especially a distinctive group of people with
    some shared interest Examples: the Western world
  * Comment: I opted for sense 2 because the world of football does refer to a group of people with
    a shared interest. However, the example at sense 2 ('the Western world') muddies the waters – it
    should be at sense 6, which refers to 'a part of the earth that can be considered separately'.
    The sense 6 example, 'the world of insects', mirrors 'the world of football', which caused me to
    hover over sense 6; however, the definition at sense 6 doesn't work at all for 'the world of
    football'. It would be better if the sense 2 definition were reworded as 'the people or things
    belonging to a particular group or connected with a particular interest'. Then 'the world of
    insects' and 'the world of football' would be examples for that sense.

**Agreement:** Fine: Exactly two agree; Glite: Exactly two agree; Maru2022 fine support: 0/3;
Maru2022 Glite support: 2/3.

### D10. semeval2013.d006.s007.t001

**Lemma/POS/source:** `rule` / `NOUN` / `semeval2013` (`semeval2013.d006`)

**Sentence:** It is so extended that it part of the ethos, of the unwritten **[rules]**, but
followed nonetheless by this sport.

**Maru2022 label**

* rule%1:10:02:: (rule.n.08) - directions that define the way a game or sport is to be conducted
  Examples: he knew the rules of chess

**Reviewer verdicts**

* **Robert Farren (RF)**
  * rule%1:09:00:: (rule.n.01) - a principle or condition that customarily governs behavior
    Examples: it was his rule to take a walk before breakfast | short haircuts were the regulation
  * Comment: I've chosen a single sense (sense 1), but really the intended meaning is not just the
    meaning of "rules", but that of the collocation "unwritten rules". If I considered "rules"
    strictly in isolation, totally ignoring the collocation and therefore the word's meaning in the
    sentence, then sense 8 would have been the best match.
* **Patrick White (PW)**
  * rule%1:10:02:: (rule.n.08) - directions that define the way a game or sport is to be conducted
    Examples: he knew the rules of chess
* **Penny Hands (PH)**
  * rule%1:10:02:: (rule.n.08) - directions that define the way a game or sport is to be conducted
    Examples: he knew the rules of chess
  * Comment: The adjective 'unwritten' makes me slightly less confident of this selection – because
    we don't expect the rules of any sport to be 'unwritten'. However, that seems to be the case
    here, and we are talking about the rules of a sport, so I think sense 8 is the most logical.

**Agreement:** Fine: Exactly two agree; Glite: All three agree; Maru2022 fine support: 2/3; Maru2022
Glite support: 3/3.

### D11. semeval2013.d006.s009.t003

**Lemma/POS/source:** `principle` / `NOUN` / `semeval2013` (`semeval2013.d006`)

**Sentence:** Anyway, the debate deals with if that type of behavior not prohibited specifically by
the regulation contradicts the **[principles]** of the sport, that is to say, if with these actions
fraud is committed; then, indeed, they are respectful actions with the sport regulation, but they
seem to elude its sense.

**Maru2022 label**

* principle%1:09:00:: (principle.n.03) - a basic truth or law or assumption Examples: the principles
  of democracy

**Reviewer verdicts**

* **Robert Farren (RF)**
  * principle%1:09:01:: (principle.n.02) - a rule or standard especially of good behavior Examples:
    a man of principle | he will not violate his principles
* **Patrick White (PW)**
  * principle%1:09:01:: (principle.n.02) - a rule or standard especially of good behavior Examples:
    a man of principle | he will not violate his principles
* **Penny Hands (PH)**
  * principle%1:09:00:: (principle.n.03) - a basic truth or law or assumption Examples: the
    principles of democracy

**Agreement:** Fine: Exactly two agree; Glite: Exactly two agree; Maru2022 fine support: 1/3;
Maru2022 Glite support: 1/3.

### D12. semeval2013.d006.s013.t005

**Lemma/POS/source:** `rule` / `NOUN` / `semeval2013` (`semeval2013.d006`)

**Sentence:** However, the paradoxical thing about the action of the players of Real Madrid is that
it did not comply to what we normally characterize as legal fraud, because the violation of the
**[rules]** was not made secretly as to try to avoid the sanction, but their action was most evident
and thus they received punishment from the referee.

**Maru2022 label**

* rule%1:10:00:: (rule.n.03) - prescribed guide for conduct or action

**Reviewer verdicts**

* **Robert Farren (RF)**
  * rule%1:10:00:: (rule.n.03) - prescribed guide for conduct or action
  * Comment: Even though the "rules" in question concern how players behave during a game, sense 3
    is still more apt than the explicitly game-related sense 8, because this isn't about the central
    definitions that determine how a game functions, but about player conduct.
* **Patrick White (PW)**
  * rule%1:10:02:: (rule.n.08) - directions that define the way a game or sport is to be conducted
    Examples: he knew the rules of chess
* **Penny Hands (PH)**
  * rule%1:10:02:: (rule.n.08) - directions that define the way a game or sport is to be conducted
    Examples: he knew the rules of chess

**Agreement:** Fine: Exactly two agree; Glite: All three agree; Maru2022 fine support: 1/3; Maru2022
Glite support: 3/3.

### D13. semeval2013.d006.s021.t003

**Lemma/POS/source:** `decision` / `NOUN` / `semeval2013` (`semeval2013.d006`)

**Sentence:** Those actions are really against the sporting spirit, which is part of the strategic
**[decisions]** that favor taking advantages allowed by the rules.

**Maru2022 label**

* decision%1:09:00:: (decision.n.02) - a position or opinion or judgment reached after consideration
  Examples: a decision unfavorable to the opposition | his conclusion took the evidence into account

**Reviewer verdicts**

* **Robert Farren (RF)**
  * decision%1:04:00:: (decision.n.01) - the act of making up your mind about something Examples:
    the burden of decision was his | he drew his conclusions quickly
* **Patrick White (PW)**
  * decision%1:04:00:: (decision.n.01) - the act of making up your mind about something Examples:
    the burden of decision was his | he drew his conclusions quickly
* **Penny Hands (PH)**
  * Cannot answer: input defective
  * Note: This text seems to be machine-translated or written by someone who has low proficiency in
    English.

**Agreement:** Fine: Exactly two agree; Glite: Exactly two agree; Maru2022 fine support: 0/3;
Maru2022 Glite support: 2/3.

### D14. semeval2013.d007.s001.t003

**Lemma/POS/source:** `nutrient` / `NOUN` / `semeval2013` (`semeval2013.d007`)

**Sentence:** The discovery of a strange bacteria that can use arsenic as one of its **[nutrients]**
widens the scope for finding new forms of life on Earth and possibly beyond.

**Maru2022 label**

* nutrient%1:03:00:: (food.n.01) - any substance that can be metabolized by an animal to give energy
  and build tissue

**Reviewer verdicts**

* **Robert Farren (RF)**
  * nutrient%1:03:00:: (food.n.01) - any substance that can be metabolized by an animal to give
    energy and build tissue
* **Patrick White (PW)**
  * nutrient%1:03:00:: (food.n.01) - any substance that can be metabolized by an animal to give
    energy and build tissue
* **Penny Hands (PH)**
  * Cannot answer: inventory inadequate
  * Note: Both senses are close but they only cover animals and plants, not bacteria. It would be
    better to replace them both with one definition that refers to any substance that is needed to
    keep 'a living thing' alive, help it grow, etc.

**Agreement:** Fine: Exactly two agree; Glite: Exactly two agree; Maru2022 fine support: 2/3;
Maru2022 Glite support: 2/3.

### D15. semeval2013.d007.s002.t004

**Lemma/POS/source:** `possibility` / `NOUN` / `semeval2013` (`semeval2013.d007`)

**Sentence:** While researchers discovered the unusual bacteria here in Earth, they say it shows
that life has **[possibilities]** beyond the major elements that have been considered essential.

**Maru2022 label**

* possibility%1:26:00:: (possibility.n.02) - capability of existing or happening or being true
  Examples: there is a possibility that his sense of smell has been impaired

**Reviewer verdicts**

* **Robert Farren (RF)**
  * possibility%1:26:00:: (possibility.n.02) - capability of existing or happening or being true
    Examples: there is a possibility that his sense of smell has been impaired
* **Patrick White (PW)**
  * possibility%1:09:03:: (possibility.n.01) - a future prospect or potential Examples: this room
    has great possibilities
* **Penny Hands (PH)**
  * possibility%1:09:03:: (possibility.n.01) - a future prospect or potential Examples: this room
    has great possibilities

**Agreement:** Fine: Exactly two agree; Glite: All three agree; Maru2022 fine support: 1/3; Maru2022
Glite support: 3/3.

### D16. semeval2013.d007.s003.t001

**Lemma/POS/source:** `capability` / `NOUN` / `semeval2013` (`semeval2013.d007`)

**Sentence:** ``This organism has dual **[capability]**.''

**Maru2022 label**

* capability%1:26:00:: (capability.n.02) - the susceptibility of something to a particular treatment
  Examples: the capability of a metal to be fused

**Reviewer verdicts**

* **Robert Farren (RF)**
  * capability%1:26:00:: (capability.n.02) - the susceptibility of something to a particular
    treatment Examples: the capability of a metal to be fused
* **Patrick White (PW)**
  * capability%1:07:00:: (capability.n.01) - the quality of being capable -- physically or
    intellectually or legally Examples: he worked to the limits of his capability
* **Penny Hands (PH)**
  * capability%1:07:00:: (capability.n.01) - the quality of being capable -- physically or
    intellectually or legally Examples: he worked to the limits of his capability

**Agreement:** Fine: Exactly two agree; Glite: Exactly two agree; Maru2022 fine support: 1/3;
Maru2022 Glite support: 1/3.

### D17. semeval2013.d007.s005.t001

**Lemma/POS/source:** `life` / `NOUN` / `semeval2013` (`semeval2013.d007`)

**Sentence:** ``That makes it very peculiar, though it falls short of being some form of truly `
alien ' **[life]**,'' commented Paul C. W. Davies of Arizona State University, a co-author of the
report appearing in Thursday's online edition of the journal Science.

**Maru2022 label**

* life%1:19:00:: (life.n.11) - the organic phenomenon that distinguishes living organisms from
  nonliving ones Examples: there is no life on the moon

**Reviewer verdicts**

* **Robert Farren (RF)**
  * life%1:03:00:: (life.n.10) - living things collectively Examples: the oceans are teeming with
    life
* **Patrick White (PW)**
  * life%1:19:00:: (life.n.11) - the organic phenomenon that distinguishes living organisms from
    nonliving ones Examples: there is no life on the moon
* **Penny Hands (PH)**
  * life%1:19:00:: (life.n.11) - the organic phenomenon that distinguishes living organisms from
    nonliving ones Examples: there is no life on the moon
  * Comment: Davies explains that it has certain features that prove that it is an organic
    phenomenon – and this proves that it is a living organism (sense 11).

**Agreement:** Fine: Exactly two agree; Glite: All three agree; Maru2022 fine support: 2/3; Maru2022
Glite support: 3/3.

### D18. semeval2013.d007.s013.t001

**Lemma/POS/source:** `environment` / `NOUN` / `semeval2013` (`semeval2013.d007`)

**Sentence:** The discovery
``does show that in other planetary **[environments]** organisms might be able to use other elements to drive biochemistry and that the `
standard ' set of elements we think are absolutely necessary for life might not be so fixed,''
commented Charles Cockell, professor at Planetary and Space Sciences Research Institute, Open
University, in Milton Keynes, United Kingdom.

**Maru2022 label**

* environment%1:15:00:: (environment.n.02) - the area in which something exists or lives Examples:
  the country--the flat agricultural surround

**Reviewer verdicts**

* **Robert Farren (RF)**
  * environment%1:26:00:: (environment.n.01) - the totality of surrounding conditions Examples: he
    longed for the comfortable environment of his living room
* **Patrick White (PW)**
  * environment%1:15:00:: (environment.n.02) - the area in which something exists or lives Examples:
    the country--the flat agricultural surround
* **Penny Hands (PH)**
  * environment%1:26:00:: (environment.n.01) - the totality of surrounding conditions Examples: he
    longed for the comfortable environment of his living room

**Agreement:** Fine: Exactly two agree; Glite: All three agree; Maru2022 fine support: 1/3; Maru2022
Glite support: 3/3.

### D19. semeval2013.d008.s006.t000

**Lemma/POS/source:** `thing` / `NOUN` / `semeval2013` (`semeval2013.d008`)

**Sentence:** Two related **[things]** stand out in the results of this year's poll, taken in
September and early October.

**Maru2022 label**

* thing%1:03:00:: (thing.n.12) - a separate and self-contained entity

**Reviewer verdicts**

* **Robert Farren (RF)**
  * thing%1:26:00:: (thing.n.01) - a special situation Examples: this thing has got to end | it is a
    remarkable thing
* **Patrick White (PW)**
  * thing%1:09:02:: (matter.n.01) - a vaguely specified concern Examples: several matters to attend
    to | it is none of your affair
* **Penny Hands (PH)**
  * thing%1:09:02:: (matter.n.01) - a vaguely specified concern Examples: several matters to attend
    to | it is none of your affair

**Agreement:** Fine: Exactly two agree; Glite: Exactly two agree; Maru2022 fine support: 0/3;
Maru2022 Glite support: 2/3.

### D20. semeval2013.d008.s008.t004

**Lemma/POS/source:** `institution` / `NOUN` / `semeval2013` (`semeval2013.d008`)

**Sentence:** The second is the increasing stability of attitudes towards democracy and its core
**[institutions]**.

**Maru2022 label**

* institution%1:09:00:: (institution.n.03) - a custom that for a long time has been an important
  feature of some group or society Examples: the institution of marriage | the institution of
  slavery

**Reviewer verdicts**

* **Robert Farren (RF)**
  * institution%1:09:00:: (institution.n.03) - a custom that for a long time has been an important
    feature of some group or society Examples: the institution of marriage | the institution of
    slavery
* **Patrick White (PW)**
  * institution%1:09:00:: (institution.n.03) - a custom that for a long time has been an important
    feature of some group or society Examples: the institution of marriage | the institution of
    slavery
* **Penny Hands (PH)**
  * institution%1:14:00:: (institution.n.01) - an organization founded and united for a specific
    purpose
  * Comment: When selecting Sense 1, I'm thinking about formal organizations such as parliament, the
    judiciary, etc.).

**Agreement:** Fine: Exactly two agree; Glite: Exactly two agree; Maru2022 fine support: 2/3;
Maru2022 Glite support: 2/3.

### D21. semeval2013.d008.s019.t001

**Lemma/POS/source:** `country` / `NOUN` / `semeval2013` (`semeval2013.d008`)

**Sentence:** But the mood varies widely from **[country]** to country (see chart 4).

**Maru2022 label**

* country%1:14:00:: (state.n.04) - a politically organized body of people under a single government
  Examples: the state has elected a new president | African nations

**Reviewer verdicts**

* **Robert Farren (RF)**
  * country%1:15:00:: (country.n.02) - the territory occupied by a nation Examples: he returned to
    the land of his birth | he visited several European countries
* **Patrick White (PW)**
  * country%1:15:00:: (country.n.02) - the territory occupied by a nation Examples: he returned to
    the land of his birth | he visited several European countries
* **Penny Hands (PH)**
  * country%1:14:00:: (state.n.04) - a politically organized body of people under a single
    government Examples: the state has elected a new president | African nations
  * Comment: Sense 2 is also possible, but I would be more inclined to select sense 2 if the context
    were something like 'in different parts of the country'.

**Agreement:** Fine: Exactly two agree; Glite: All three agree; Maru2022 fine support: 1/3; Maru2022
Glite support: 3/3.

### D22. semeval2013.d008.s019.t002

**Lemma/POS/source:** `country` / `NOUN` / `semeval2013` (`semeval2013.d008`)

**Sentence:** But the mood varies widely from country to **[country]** (see chart 4).

**Maru2022 label**

* country%1:14:00:: (state.n.04) - a politically organized body of people under a single government
  Examples: the state has elected a new president | African nations

**Reviewer verdicts**

* **Robert Farren (RF)**
  * country%1:15:00:: (country.n.02) - the territory occupied by a nation Examples: he returned to
    the land of his birth | he visited several European countries
* **Patrick White (PW)**
  * country%1:15:00:: (country.n.02) - the territory occupied by a nation Examples: he returned to
    the land of his birth | he visited several European countries
* **Penny Hands (PH)**
  * country%1:14:00:: (state.n.04) - a politically organized body of people under a single
    government Examples: the state has elected a new president | African nations
  * Comment: Sense 2 is also possible, but I would be more inclined to select sense 2 if the context
    were something like 'in different parts of the country'.

**Agreement:** Fine: Exactly two agree; Glite: All three agree; Maru2022 fine support: 1/3; Maru2022
Glite support: 3/3.

### D23. semeval2013.d008.s028.t006

**Lemma/POS/source:** `distinction` / `NOUN` / `semeval2013` (`semeval2013.d008`)

**Sentence:** But the United States is seen as the most influential country by respondents in Mexico
and much of Central America, whereas Venezuela enjoys that **[distinction]** in Ecuador, the
Dominican Republic and Nicaragua.

**Maru2022 label**

* distinction%1:26:00:: (eminence.n.01) - high status importance owing to marked superiority
  Examples: a scholar of great eminence

**Reviewer verdicts**

* **Robert Farren (RF)**
  * distinction%1:07:01:: (distinction.n.03) - a distinguishing quality Examples: it has the
    distinction of being the cheapest restaurant in town
* **Patrick White (PW)**
  * distinction%1:07:01:: (distinction.n.03) - a distinguishing quality Examples: it has the
    distinction of being the cheapest restaurant in town
* **Penny Hands (PH)**
  * distinction%1:26:00:: (eminence.n.01) - high status importance owing to marked superiority
    Examples: a scholar of great eminence

**Agreement:** Fine: Exactly two agree; Glite: Exactly two agree; Maru2022 fine support: 1/3;
Maru2022 Glite support: 1/3.

### D24. semeval2013.d009.s003.t003

**Lemma/POS/source:** `state` / `NOUN` / `semeval2013` (`semeval2013.d009`)

**Sentence:** One of the cases at issue was a suit brought by 26 **[states]** challenging the
sweeping healthcare overhaul passed by Congress last year, a law that has been a rallying cry for
conservative activists nationwide.

**Maru2022 label**

* state%1:14:00:: (state.n.04) - a politically organized body of people under a single government
  Examples: the state has elected a new president | African nations

**Reviewer verdicts**

* **Robert Farren (RF)**
  * state%1:15:01:: (state.n.01) - the territory occupied by one of the constituent administrative
    districts of a nation Examples: his state is in the deep south
* **Patrick White (PW)**
  * state%1:15:01:: (state.n.01) - the territory occupied by one of the constituent administrative
    districts of a nation Examples: his state is in the deep south
* **Penny Hands (PH)**
  * state%1:14:01:: (state.n.03) - the group of people comprising the government of a sovereign
    state Examples: the state has lowered its income tax

**Agreement:** Fine: Exactly two agree; Glite: Exactly two agree; Maru2022 fine support: 0/3;
Maru2022 Glite support: 2/3.

### D25. semeval2013.d009.s023.t005

**Lemma/POS/source:** `level` / `NOUN` / `semeval2013` (`semeval2013.d009`)

**Sentence:** Kagan served as solicitor general in the Obama administration when the first legal
challenges to the law were brought at the trial court **[level]**.

**Maru2022 label**

* level%1:09:00:: (level.n.07) - an abstract place usually conceived as having depth Examples: a
  good actor communicates on several levels | a simile has at least two layers of meaning

**Reviewer verdicts**

* **Robert Farren (RF)**
  * level%1:26:01:: (grade.n.02) - a relative position or degree of value in a graded group
    Examples: lumber of the highest grade
* **Patrick White (PW)**
  * level%1:09:00:: (level.n.07) - an abstract place usually conceived as having depth Examples: a
    good actor communicates on several levels | a simile has at least two layers of meaning
* **Penny Hands (PH)**
  * level%1:26:01:: (grade.n.02) - a relative position or degree of value in a graded group
    Examples: lumber of the highest grade

**Agreement:** Fine: Exactly two agree; Glite: All three agree; Maru2022 fine support: 1/3; Maru2022
Glite support: 3/3.

### D26. semeval2013.d010.s008.t002

**Lemma/POS/source:** `area` / `NOUN` / `semeval2013` (`semeval2013.d010`)

**Sentence:** The Ticos players, however, have a limited international experience in an **[area]**
such as CONCACAF, which is considered the lowest level within FIFA

**Maru2022 label**

* area%1:26:00:: (sphere.n.01) - a particular environment or walk of life Examples: his social
  sphere is limited | it was a closed area of employment

**Reviewer verdicts**

* **Robert Farren (RF)**
  * area%1:15:01:: (area.n.01) - a particular geographical region of indefinite boundary (usually
    serving some special purpose or distinguished by its people or culture or geography) Examples:
    it was a mountainous area | Bible country
  * Comment: This is a case where the input is arguably defective. Seen in context, the sentence
    seems to be referring to the geographical area for which CONCACAF, one of FIFA's continental
    governing bodies, is responsible. If so, then sense 1 is the best choice. If not, then this
    sense of "area" is like "field of activity", which is a figurative sense not represented here.
* **Patrick White (PW)**
  * area%1:15:01:: (area.n.01) - a particular geographical region of indefinite boundary (usually
    serving some special purpose or distinguished by its people or culture or geography) Examples:
    it was a mountainous area | Bible country
  * Comment: This text appears to be written by a non-native English speaker but this is the sense
    that I think is intended.
* **Penny Hands (PH)**
  * area%1:26:00:: (sphere.n.01) - a particular environment or walk of life Examples: his social
    sphere is limited | it was a closed area of employment
  * Comment: CONCACAF is an organisation, not a geographical area in itself. The synonyms at sense 4
    (domain, sphere, arena) help to pin things down.

**Agreement:** Fine: Exactly two agree; Glite: Exactly two agree; Maru2022 fine support: 1/3;
Maru2022 Glite support: 1/3.

### D27. semeval2013.d010.s013.t000

**Lemma/POS/source:** `number` / `NOUN` / `semeval2013` (`semeval2013.d010`)

**Sentence:** Almost near the centennial **[number]** is Carles Puyol, with 97 games.

**Maru2022 label**

* number%1:07:00:: (number.n.01) - the property possessed by a sum or total or indefinite quantity
  of units or individuals Examples: he had a number of chores to do | the number of parameters is
  small

**Reviewer verdicts**

* **Robert Farren (RF)**
  * number%1:23:00:: (number.n.02) - a concept of quantity involving zero and units Examples: every
    number has a unique position in the sequence
* **Patrick White (PW)**
  * number%1:07:00:: (number.n.01) - the property possessed by a sum or total or indefinite quantity
    of units or individuals Examples: he had a number of chores to do | the number of parameters is
    small
  * Comment: NB this text not written by a non-native English speaker: "centennial number" is not an
    English expression.
* **Penny Hands (PH)**
  * number%1:07:00:: (number.n.01) - the property possessed by a sum or total or indefinite quantity
    of units or individuals Examples: he had a number of chores to do | the number of parameters is
    small
  * Comment: The text is about a *quantity* of games. Sense 2 is close if you focus on the figures
    themselves (97 and 100), but the reality is that we're talking about a quantity or amount.

**Agreement:** Fine: Exactly two agree; Glite: Exactly two agree; Maru2022 fine support: 2/3;
Maru2022 Glite support: 2/3.

### D28. semeval2013.d011.s005.t001

**Lemma/POS/source:** `tone` / `NOUN` / `semeval2013` (`semeval2013.d011`)

**Sentence:** On the Right, the **[tone]** was set by Jacques Chirac, who declared in 1976 that
`900,000 unemployed would not become a problem in a country with 2 million of foreign workers,'' and on the Left by Michel Rocard explaining in 1990 that France `can
not accommodate all the world's misery.''

**Maru2022 label**

* tone%1:26:01:: (spirit.n.02) - the general atmosphere of a place or situation and the effect that
  it has on people Examples: the feel of the city excited him | a clergyman improved the tone of the
  meeting

**Reviewer verdicts**

* **Robert Farren (RF)**
  * tone%1:07:03:: (tone.n.10) - the quality of something (an act or a piece of writing) that
    reveals the attitudes and presuppositions of the author Examples: the general tone of articles
    appearing in the newspapers is that the government should withdraw | from the tone of her
    behavior I gathered that I had outstayed my welcome
* **Patrick White (PW)**
  * tone%1:26:01:: (spirit.n.02) - the general atmosphere of a place or situation and the effect
    that it has on people Examples: the feel of the city excited him | a clergyman improved the tone
    of the meeting
* **Penny Hands (PH)**
  * tone%1:07:03:: (tone.n.10) - the quality of something (an act or a piece of writing) that
    reveals the attitudes and presuppositions of the author Examples: the general tone of articles
    appearing in the newspapers is that the government should withdraw | from the tone of her
    behavior I gathered that I had outstayed my welcome
  * Comment: Sense 4 is more about atmosphere; sense 10 is about revealing attitudes and opinions
    (as in the text).

**Agreement:** Fine: Exactly two agree; Glite: All three agree; Maru2022 fine support: 1/3; Maru2022
Glite support: 3/3.

### D29. semeval2015.d000.s001.t003

**Lemma/POS/source:** `product` / `NOUN` / `semeval2015` (`semeval2015.d000`)

**Sentence:** It explains how the Committee for Medicinal **[Products]** for Human Use (CHMP)
assessed the studies performed, to reach their recommendations on how to use the medicine.

**Maru2022 label**

* product%1:06:00:: (product.n.02) - an artifact that has been created by someone or some process
  Examples: they improve their product every year | they export most of their agricultural
  production

**Reviewer verdicts**

* **Robert Farren (RF)**
  * product%1:06:01:: (merchandise.n.01) - commodities offered for sale Examples: good business
    depends on having good merchandise | that store offers a variety of products
* **Patrick White (PW)**
  * product%1:06:00:: (product.n.02) - an artifact that has been created by someone or some process
    Examples: they improve their product every year | they export most of their agricultural
    production
* **Penny Hands (PH)**
  * product%1:06:01:: (merchandise.n.01) - commodities offered for sale Examples: good business
    depends on having good merchandise | that store offers a variety of products

**Agreement:** Fine: Exactly two agree; Glite: All three agree; Maru2022 fine support: 1/3; Maru2022
Glite support: 3/3.

### D30. semeval2015.d000.s002.t002

**Lemma/POS/source:** `information` / `NOUN` / `semeval2015` (`semeval2015.d000`)

**Sentence:** If you need more **[information]** about your medical condition or your treatment,
read the Package Leaflet (also part of the EPAR) or contact your doctor or pharmacist.

**Maru2022 label**

* information%1:09:00:: (information.n.02) - knowledge acquired through study or experience or
  instruction
* information%1:14:00:: (data.n.01) - a collection of facts from which conclusions may be drawn
  Examples: statistical data

**Reviewer verdicts**

* **Robert Farren (RF)**
  * information%1:09:00:: (information.n.02) - knowledge acquired through study or experience or
    instruction
* **Patrick White (PW)**
  * information%1:14:00:: (data.n.01) - a collection of facts from which conclusions may be drawn
    Examples: statistical data
* **Penny Hands (PH)**
  * information%1:09:00:: (information.n.02) - knowledge acquired through study or experience or
    instruction

**Agreement:** Fine: Exactly two agree; Glite: All three agree; Maru2022 fine support: 0/3; Maru2022
Glite support: 3/3.

### D31. semeval2015.d000.s011.t001

**Lemma/POS/source:** `only` / `ADV` / `semeval2015` (`semeval2015.d000`)

**Sentence:** The medicine can **[only]** be obtained with a prescription.

**Maru2022 label**

* only%4:02:03:: (only.r.06) - never except when Examples: call me only if your cold gets worse

**Reviewer verdicts**

* **Robert Farren (RF)**
  * only%4:02:03:: (only.r.06) - never except when Examples: call me only if your cold gets worse
* **Patrick White (PW)**
  * only%4:02:01:: (entirely.r.02) - without any others being included or involved Examples: was
    entirely to blame | a school devoted entirely to the needs of problem children
* **Penny Hands (PH)**
  * only%4:02:01:: (entirely.r.02) - without any others being included or involved Examples: was
    entirely to blame | a school devoted entirely to the needs of problem children
  * Comment: Sense 2 suggests 'exclusively', as in 'there are no other options', or 'there are no
    other ways to get it'. Sense 6 would work if the sentence were rephrased as: 'You can get this
    medicine only if you have a prescription.' I think the grammar is important there, judging by
    the synonyms, so I've opted for sense 2.

**Agreement:** Fine: Exactly two agree; Glite: Exactly two agree; Maru2022 fine support: 1/3;
Maru2022 Glite support: 1/3.

### D32. semeval2015.d000.s020.t001

**Lemma/POS/source:** `information` / `NOUN` / `semeval2015` (`semeval2015.d000`)

**Sentence:** For more **[information]**, see the Summary of Product Characteristics (also part of
the EPAR).

**Maru2022 label**

* information%1:09:00:: (information.n.02) - knowledge acquired through study or experience or
  instruction
* information%1:14:00:: (data.n.01) - a collection of facts from which conclusions may be drawn
  Examples: statistical data

**Reviewer verdicts**

* **Robert Farren (RF)**
  * information%1:09:00:: (information.n.02) - knowledge acquired through study or experience or
    instruction
* **Patrick White (PW)**
  * information%1:14:00:: (data.n.01) - a collection of facts from which conclusions may be drawn
    Examples: statistical data
* **Penny Hands (PH)**
  * information%1:09:00:: (information.n.02) - knowledge acquired through study or experience or
    instruction

**Agreement:** Fine: Exactly two agree; Glite: All three agree; Maru2022 fine support: 0/3; Maru2022
Glite support: 3/3.

### D33. semeval2015.d000.s020.t004

**Lemma/POS/source:** `product` / `NOUN` / `semeval2015` (`semeval2015.d000`)

**Sentence:** For more information, see the Summary of **[Product]** Characteristics (also part of
the EPAR).

**Maru2022 label**

* product%1:06:00:: (product.n.02) - an artifact that has been created by someone or some process
  Examples: they improve their product every year | they export most of their agricultural
  production

**Reviewer verdicts**

* **Robert Farren (RF)**
  * product%1:06:01:: (merchandise.n.01) - commodities offered for sale Examples: good business
    depends on having good merchandise | that store offers a variety of products
* **Patrick White (PW)**
  * product%1:06:00:: (product.n.02) - an artifact that has been created by someone or some process
    Examples: they improve their product every year | they export most of their agricultural
    production
* **Penny Hands (PH)**
  * product%1:06:01:: (merchandise.n.01) - commodities offered for sale Examples: good business
    depends on having good merchandise | that store offers a variety of products
  * Comment: The emphasis here seems to be more on a commodity offered for sale than just 'something
    produced'.

**Agreement:** Fine: Exactly two agree; Glite: All three agree; Maru2022 fine support: 1/3; Maru2022
Glite support: 3/3.

### D34. semeval2015.d001.s002.t003

**Lemma/POS/source:** `know` / `VERB` / `semeval2015` (`semeval2015.d001`)

**Sentence:** It is actually not necessary to **[know]** MathML to use kalgebra.

**Maru2022 label**

* know%2:31:03:: (know.v.02) - know how to do or perform something Examples: She knows how to knit |
  Does your husband know how to cook?

**Reviewer verdicts**

* **Robert Farren (RF)**
  * know%2:31:15:: (know.v.07) - have fixed in the mind Examples: I know Latin | This student knows
    her irregular verbs
* **Patrick White (PW)**
  * know%2:31:15:: (know.v.07) - have fixed in the mind Examples: I know Latin | This student knows
    her irregular verbs
* **Penny Hands (PH)**
  * know%2:31:03:: (know.v.02) - know how to do or perform something Examples: She knows how to knit
    | Does your husband know how to cook?
  * know%2:31:15:: (know.v.07) - have fixed in the mind Examples: I know Latin | This student knows
    her irregular verbs
  * Comment: It's not possible to know from the text whether the author is talking about just being
    able to read MathML (i.e. having it in one's mind) (sense 7), or also knowing how to
    write/create' the code (sense 2).

**Agreement:** Fine: Exactly two agree; Glite: Exactly two agree; Maru2022 fine support: 0/3;
Maru2022 Glite support: 0/3.

### D35. semeval2015.d001.s009.t003

**Lemma/POS/source:** `best` / `ADJ` / `semeval2015` (`semeval2015.d001`)

**Sentence:** If we want to understand how it works, the **[best]** thing we can do is to realize
that our input is being converted into MathML although it is not necessary to know MathML.

**Maru2022 label**

* best%3:00:00:: (best.a.01) - (superlative of `good') having the most positive qualities Examples:
  the best film of the year | the best solution

**Reviewer verdicts**

* **Robert Farren (RF)**
  * best%5:00:00:advisable:00 (better.s.01) - (comparative and superlative of `well') wiser or more
    advantageous and hence advisable Examples: it would be better to speak to him | the White House
    thought it best not to respond
* **Patrick White (PW)**
  * best%5:00:00:advisable:00 (better.s.01) - (comparative and superlative of `well') wiser or more
    advantageous and hence advisable Examples: it would be better to speak to him | the White House
    thought it best not to respond
* **Penny Hands (PH)**
  * best%3:00:00:: (best.a.01) - (superlative of `good') having the most positive qualities
    Examples: the best film of the year | the best solution
  * Comment: While the sense 2 definition 'wiser or more advantageous and hence advisable' sounds
    like it would fit best, the examples suggest that this sense is restricted to such expressions
    as 'It would be better (not) to ...' or 'It would be best not to ...'. There are no examples of
    attributive position. The example of 'best solution' in sense 1 influenced me in deciding that
    the 'best thing' is simply the thing that has the most positive qualities.

**Agreement:** Fine: Exactly two agree; Glite: All three agree; Maru2022 fine support: 1/3; Maru2022
Glite support: 3/3.

### D36. semeval2015.d001.s009.t011

**Lemma/POS/source:** `know` / `VERB` / `semeval2015` (`semeval2015.d001`)

**Sentence:** If we want to understand how it works, the best thing we can do is to realize that our
input is being converted into MathML although it is not necessary to **[know]** MathML.

**Maru2022 label**

* know%2:31:03:: (know.v.02) - know how to do or perform something Examples: She knows how to knit |
  Does your husband know how to cook?

**Reviewer verdicts**

* **Robert Farren (RF)**
  * know%2:31:15:: (know.v.07) - have fixed in the mind Examples: I know Latin | This student knows
    her irregular verbs
* **Patrick White (PW)**
  * know%2:31:15:: (know.v.07) - have fixed in the mind Examples: I know Latin | This student knows
    her irregular verbs
* **Penny Hands (PH)**
  * know%2:31:03:: (know.v.02) - know how to do or perform something Examples: She knows how to knit
    | Does your husband know how to cook?
  * know%2:31:15:: (know.v.07) - have fixed in the mind Examples: I know Latin | This student knows
    her irregular verbs
  * Comment: It's not possible to tell from the text whether the author means that it's not
    necessary to know how to code in MathML or just to be able to understand it.

**Agreement:** Fine: Exactly two agree; Glite: Exactly two agree; Maru2022 fine support: 0/3;
Maru2022 Glite support: 0/3.

### D37. semeval2015.d001.s018.t002

**Lemma/POS/source:** `function` / `NOUN` / `semeval2015` (`semeval2015.d001`)

**Sentence:** abc(params): When the parser finds a **[function]**, it checks if abc is an operator.

**Maru2022 label**

* function%1:24:00:: (function.n.01) - (mathematics) a mathematical relation such that each element
  of a given set (the domain of the function) is associated with an element of another set (the
  range of the function)

**Reviewer verdicts**

* **Robert Farren (RF)**
  * function%1:24:00:: (function.n.01) - (mathematics) a mathematical relation such that each
    element of a given set (the domain of the function) is associated with an element of another set
    (the range of the function)
* **Patrick White (PW)**
  * function%1:24:00:: (function.n.01) - (mathematics) a mathematical relation such that each
    element of a given set (the domain of the function) is associated with an element of another set
    (the range of the function)
* **Penny Hands (PH)**
  * function%1:10:00:: (routine.n.03) - a set sequence of steps, part of larger computer program

**Agreement:** Fine: Exactly two agree; Glite: All three agree; Maru2022 fine support: 2/3; Maru2022
Glite support: 3/3.

### D38. semeval2015.d001.s019.t005

**Lemma/POS/source:** `function` / `NOUN` / `semeval2015` (`semeval2015.d001`)

**Sentence:** If it is, it will be treated as an operator, if it is not, it will be treated as a
user **[function]**.

**Maru2022 label**

* function%1:24:00:: (function.n.01) - (mathematics) a mathematical relation such that each element
  of a given set (the domain of the function) is associated with an element of another set (the
  range of the function)

**Reviewer verdicts**

* **Robert Farren (RF)**
  * function%1:24:00:: (function.n.01) - (mathematics) a mathematical relation such that each
    element of a given set (the domain of the function) is associated with an element of another set
    (the range of the function)
* **Patrick White (PW)**
  * function%1:24:00:: (function.n.01) - (mathematics) a mathematical relation such that each
    element of a given set (the domain of the function) is associated with an element of another set
    (the range of the function)
* **Penny Hands (PH)**
  * function%1:10:00:: (routine.n.03) - a set sequence of steps, part of larger computer program

**Agreement:** Fine: Exactly two agree; Glite: All three agree; Maru2022 fine support: 2/3; Maru2022
Glite support: 3/3.

### D39. semeval2015.d001.s031.t000

**Lemma/POS/source:** `useful` / `ADJ` / `semeval2015` (`semeval2015.d001`)

**Sentence:** kalgebra's console is **[useful]** as a calculator.

**Maru2022 label**

* useful%5:00:00:functional:00 (utilitarian.s.01) - having a useful function Examples: utilitarian
  steel tables

**Reviewer verdicts**

* **Robert Farren (RF)**
  * Cannot answer: input defective
  * Note: Sense 2 is closer than sense 1, but the sentence is odd: it feels like "useful" is
    intended to mean "can be used". It's debatable whether this is a correct usage. Maybe the writer
    should have chosen "usable", or written "...can be used as a calculator"?
* **Patrick White (PW)**
  * useful%3:00:00:: (useful.a.01) - being of use or service Examples: the girl felt motherly and
    useful | a useful job
* **Penny Hands (PH)**
  * useful%3:00:00:: (useful.a.01) - being of use or service Examples: the girl felt motherly and
    useful | a useful job
  * Comment: Sense 2 seems to be more about functional style or design.

**Agreement:** Fine: Exactly two agree; Glite: Exactly two agree; Maru2022 fine support: 0/3;
Maru2022 Glite support: 0/3.

### D40. semeval2015.d002.s000.t005

**Lemma/POS/source:** `deal` / `VERB` / `semeval2015` (`semeval2015.d002`)

**Sentence:** The Foundation has recently been involved in organising a conference which **[dealt]**
with this critical challenge.

**Maru2022 label**

* deal%2:41:09:: (deal.v.03) - take action with respect to (someone or something) Examples: How are
  we going to deal with this problem? | The teacher knew how to deal with these lazy students
* deal%2:41:13:: (manage.v.02) - be in charge of, act on, or dispose of Examples: I can deal with
  this crew of workers | This blender can't handle nuts

**Reviewer verdicts**

* **Robert Farren (RF)**
  * deal%2:32:08:: (cover.v.05) - act on verbally or in some form of artistic expression Examples:
    This book deals with incest | The course covered all of Western Civilization
* **Patrick White (PW)**
  * Cannot answer: inventory inadequate
  * Note: Sense of phrasal verb usage, deal with, is to be about something.
* **Penny Hands (PH)**
  * deal%2:32:08:: (cover.v.05) - act on verbally or in some form of artistic expression Examples:
    This book deals with incest | The course covered all of Western Civilization

**Agreement:** Fine: Exactly two agree; Glite: Exactly two agree; Maru2022 fine support: 0/3;
Maru2022 Glite support: 2/3.

### D41. semeval2015.d002.s001.t004

**Lemma/POS/source:** `debate` / `VERB` / `semeval2015` (`semeval2015.d002`)

**Sentence:** Over 100 participants from the main interest groups attended and **[debated]** issues
such as the role of key actors including public authorities, social partners, voluntary and
community organisations as well as service users.

**Maru2022 label**

* debate%2:31:00:: (debate.v.01) - argue with one another Examples: We debated the question of
  abortion | John debated Mary

**Reviewer verdicts**

* **Robert Farren (RF)**
  * debate%2:32:00:: (debate.v.03) - discuss the pros and cons of an issue
* **Patrick White (PW)**
  * debate%2:32:00:: (debate.v.03) - discuss the pros and cons of an issue
* **Penny Hands (PH)**
  * debate%2:31:00:: (debate.v.01) - argue with one another Examples: We debated the question of
    abortion | John debated Mary
  * Comment: I think sense 3 is referring to the intransitive sense of 'debate' (as in 'We debated
    long into the night'). The first example in sense 1 suggests that this is the transitive sense:
    'debate an issue/question/topic/proposal'.

**Agreement:** Fine: Exactly two agree; Glite: All three agree; Maru2022 fine support: 1/3; Maru2022
Glite support: 3/3.

### D42. semeval2015.d002.s002.t009

**Lemma/POS/source:** `involvement` / `NOUN` / `semeval2015` (`semeval2015.d002`)

**Sentence:** There were relatively few cases reported of attempts to involve users in service
planning but their **[involvement]** in service provision was found to be more common.

**Maru2022 label**

* involvement%1:26:01:: (participation.n.02) - the condition of sharing in common with others (as
  fellows or partners etc.)

**Reviewer verdicts**

* **Robert Farren (RF)**
  * involvement%1:04:00:: (engagement.n.07) - the act of sharing in the activities of a group
    Examples: the teacher tried to increase his students' engagement in class activities
* **Patrick White (PW)**
  * involvement%1:04:00:: (engagement.n.07) - the act of sharing in the activities of a group
    Examples: the teacher tried to increase his students' engagement in class activities
* **Penny Hands (PH)**
  * involvement%1:04:00:: (engagement.n.07) - the act of sharing in the activities of a group
    Examples: the teacher tried to increase his students' engagement in class activities
  * involvement%1:26:01:: (participation.n.02) - the condition of sharing in common with others (as
    fellows or partners etc.)
  * Comment: Sense 1 focuses on participating in activities.; sense 5 focuses on the state of being
    associated. I can't make the call here.

**Agreement:** Fine: Exactly two agree; Glite: All three agree; Maru2022 fine support: 0/3; Maru2022
Glite support: 3/3.

### D43. semeval2015.d002.s003.t006

**Lemma/POS/source:** `public` / `ADJ` / `semeval2015` (`semeval2015.d002`)

**Sentence:** Note was also taken of the variety of different roles played by **[public]** welfare

**Maru2022 label**

* public%5:00:00:common:02 (public.s.01) - affecting the people or community as a whole Examples:
  community leaders | community interests

**Reviewer verdicts**

* **Robert Farren (RF)**
  * public%3:00:00:: (public.a.01) - not private; open to or concerning the people as a whole
    Examples: the public good | public libraries
  * Comment: The meaning of "roles played by public welfare" in this particular sentence is very
    unclear, and it's worth noting that the sentence is unfinished. However, the next paragraph
    refers to "public welfare services", and on the balance of probabilities this is what the term
    refers to in both cases.
* **Patrick White (PW)**
  * public%5:00:00:common:02 (public.s.01) - affecting the people or community as a whole Examples:
    community leaders | community interests
* **Penny Hands (PH)**
  * public%5:00:00:common:02 (public.s.01) - affecting the people or community as a whole Examples:
    community leaders | community interests

**Agreement:** Fine: Exactly two agree; Glite: All three agree; Maru2022 fine support: 2/3; Maru2022
Glite support: 3/3.

### D44. semeval2015.d002.s004.t006

**Lemma/POS/source:** `affairs` / `NOUN` / `semeval2015` (`semeval2015.d002`)

**Sentence:** The Foundation organised, together with the European Commission, the Spanish Ministry
of Social **[Affairs]** and the Galician regional government, a European conference on social
exclusion: a major challenge for public welfare services.

**Maru2022 label**

* affairs%1:09:00:: (personal_business.n.01) - matters of personal concern Examples: get his affairs
  in order

**Reviewer verdicts**

* **Robert Farren (RF)**
  * Cannot answer: inventory inadequate, no sense applies
  * Note: This sense of "affairs", which is always a plural, falls somewhere between sense 1 and
    sense 2 above. The problem is that sense 2 is too specific, or indeed is poorly formulated. The
    sense here is "matters of public or state interest".
* **Patrick White (PW)**
  * affairs%1:04:00:: (affairs.n.02) - transactions of professional or public interest Examples:
    news of current affairs | great affairs of state
* **Penny Hands (PH)**
  * affairs%1:04:00:: (affairs.n.02) - transactions of professional or public interest Examples:
    news of current affairs | great affairs of state

**Agreement:** Fine: Exactly two agree; Glite: Exactly two agree; Maru2022 fine support: 0/3;
Maru2022 Glite support: 0/3.

### D45. semeval2015.d002.s004.t015

**Lemma/POS/source:** `public` / `ADJ` / `semeval2015` (`semeval2015.d002`)

**Sentence:** The Foundation organised, together with the European Commission, the Spanish Ministry
of Social Affairs and the Galician regional government, a European conference on social exclusion: a
major challenge for **[public]** welfare services.

**Maru2022 label**

* public%5:00:00:common:02 (public.s.01) - affecting the people or community as a whole Examples:
  community leaders | community interests

**Reviewer verdicts**

* **Robert Farren (RF)**
  * public%3:00:00:: (public.a.01) - not private; open to or concerning the people as a whole
    Examples: the public good | public libraries
* **Patrick White (PW)**
  * public%5:00:00:common:02 (public.s.01) - affecting the people or community as a whole Examples:
    community leaders | community interests
* **Penny Hands (PH)**
  * public%5:00:00:common:02 (public.s.01) - affecting the people or community as a whole Examples:
    community leaders | community interests

**Agreement:** Fine: Exactly two agree; Glite: All three agree; Maru2022 fine support: 2/3; Maru2022
Glite support: 3/3.

### D46. semeval2015.d002.s006.t009

**Lemma/POS/source:** `level` / `NOUN` / `semeval2015` (`semeval2015.d002`)

**Sentence:** The study is based on 195 personal interviews with senior officials of the social
partners as representatives of national **[level]** peak organisations in fifteen European
countries.

**Maru2022 label**

* level%1:09:00:: (level.n.07) - an abstract place usually conceived as having depth Examples: a
  good actor communicates on several levels | a simile has at least two layers of meaning

**Reviewer verdicts**

* **Robert Farren (RF)**
  * level%1:26:01:: (grade.n.02) - a relative position or degree of value in a graded group
    Examples: lumber of the highest grade
* **Patrick White (PW)**
  * level%1:09:00:: (level.n.07) - an abstract place usually conceived as having depth Examples: a
    good actor communicates on several levels | a simile has at least two layers of meaning
* **Penny Hands (PH)**
  * level%1:26:01:: (grade.n.02) - a relative position or degree of value in a graded group
    Examples: lumber of the highest grade

**Agreement:** Fine: Exactly two agree; Glite: All three agree; Maru2022 fine support: 1/3; Maru2022
Glite support: 3/3.

### D47. semeval2015.d002.s013.t001

**Lemma/POS/source:** `study` / `NOUN` / `semeval2015` (`semeval2015.d002`)

**Sentence:** These national **[studies]** will form the basis of a European report which
synthesises overall practices.

**Maru2022 label**

* study%1:04:00:: (survey.n.01) - a detailed critical inspection

**Reviewer verdicts**

* **Robert Farren (RF)**
  * study%1:04:00:: (survey.n.01) - a detailed critical inspection
* **Patrick White (PW)**
  * study%1:10:00:: (report.n.01) - a written document describing the findings of some individual or
    group Examples: this accords with the recent study by Hill and Dale
* **Penny Hands (PH)**
  * study%1:10:00:: (report.n.01) - a written document describing the findings of some individual or
    group Examples: this accords with the recent study by Hill and Dale
  * Comment: As I see it, sense 1 refers to the investigation itself and sense 3 is about the
    findings. It is the findings that will form the basis of a European report.

**Agreement:** Fine: Exactly two agree; Glite: Exactly two agree; Maru2022 fine support: 1/3;
Maru2022 Glite support: 1/3.

### D48. semeval2015.d002.s013.t003

**Lemma/POS/source:** `basis` / `NOUN` / `semeval2015` (`semeval2015.d002`)

**Sentence:** These national studies will form the **[basis]** of a European report which
synthesises overall practices.

**Maru2022 label**

* basis%1:24:01:: (basis.n.03) - the most important or necessary part of something Examples: the
  basis of this drink is orange juice

**Reviewer verdicts**

* **Robert Farren (RF)**
  * Cannot answer: no sense applies
  * Note: Sense 3 is close, but "most important or necessary part" is too specific. This sense of
    "basis" is more like the material the study builds on, or takes as a starting point. So:
    "starting point", with synonyms like "foundation, support, base, ground" (from
    collinsdictionary.com).
* **Patrick White (PW)**
  * basis%1:09:00:: (basis.n.02) - the fundamental assumptions from which something is begun or
    developed or calculated or explained Examples: the whole argument rested on a basis of
    conjecture
* **Penny Hands (PH)**
  * basis%1:09:00:: (basis.n.02) - the fundamental assumptions from which something is begun or
    developed or calculated or explained Examples: the whole argument rested on a basis of
    conjecture

**Agreement:** Fine: Exactly two agree; Glite: Exactly two agree; Maru2022 fine support: 0/3;
Maru2022 Glite support: 2/3.

### D49. semeval2015.d002.s013.t007

**Lemma/POS/source:** `overall` / `ADJ` / `semeval2015` (`semeval2015.d002`)

**Sentence:** These national studies will form the basis of a European report which synthesises
**[overall]** practices.

**Maru2022 label**

* overall%5:00:00:gross:00 (overall.s.02) - including everything Examples: the overall cost

**Reviewer verdicts**

* **Robert Farren (RF)**
  * overall%5:00:00:general:00 (overall.s.01) - involving only main features Examples: the overall
    pattern of his life
  * Comment: It's debatable which sense is intended here, but on the balance of probability sense 1
    is the better choice.
* **Patrick White (PW)**
  * overall%5:00:00:general:00 (overall.s.01) - involving only main features Examples: the overall
    pattern of his life
* **Penny Hands (PH)**
  * overall%5:00:00:gross:00 (overall.s.02) - including everything Examples: the overall cost
  * Comment: Sense 2 because I think the author is saying that the national studies will take
    everything into account, rather than giving a broad outline of general patterns.

**Agreement:** Fine: Exactly two agree; Glite: All three agree; Maru2022 fine support: 1/3; Maru2022
Glite support: 3/3.

### D50. semeval2015.d002.s020.t002

**Lemma/POS/source:** `consider` / `VERB` / `semeval2015` (`semeval2015.d002`)

**Sentence:** The project also **[considers]** initiatives to combat age discrimination in rural
areas and in small and medium sized enterprises.

**Maru2022 label**

* consider%2:32:00:: (consider.v.04) - show consideration for; take into account Examples: You must
  consider her age | The judge considered the offender's youth and was lenient

**Reviewer verdicts**

* **Robert Farren (RF)**
  * consider%2:31:01:: (consider.v.03) - take into consideration for exemplifying purposes Examples:
    Take the case of China | Consider the following case
  * Comment: "Consider" is being used as a synonym of other verbs in the text (examine, assess).
    Sense 3 is closest to the intended meaning.
* **Patrick White (PW)**
  * consider%2:39:00:: (study.v.03) - give careful consideration to Examples: consider the
    possibility of moving
* **Penny Hands (PH)**
  * consider%2:39:00:: (study.v.03) - give careful consideration to Examples: consider the
    possibility of moving

**Agreement:** Fine: Exactly two agree; Glite: Exactly two agree; Maru2022 fine support: 0/3;
Maru2022 Glite support: 2/3.

### D51. senseval2.d000.s003.t009

**Lemma/POS/source:** `field` / `NOUN` / `senseval2` (`senseval2.d000`)

**Sentence:** Of all scenes that evoke rural England, this is one of the loveliest: An ancient stone
church stands amid the **[fields]**, the sound of bells cascading from its tower, calling the
faithful to evensong.

**Maru2022 label**

* field%1:17:00:: (plain.n.01) - extensive tract of level open land Examples: they emerged from the
  woods onto a vast open plain | he longed for the fields of his youth

**Reviewer verdicts**

* **Robert Farren (RF)**
  * field%1:15:00:: (field.n.01) - a piece of land cleared of trees and usually enclosed Examples:
    he planted a field of wheat
* **Patrick White (PW)**
  * field%1:15:00:: (field.n.01) - a piece of land cleared of trees and usually enclosed Examples:
    he planted a field of wheat
* **Penny Hands (PH)**
  * field%1:15:00:: (field.n.01) - a piece of land cleared of trees and usually enclosed Examples:
    he planted a field of wheat
  * field%1:17:00:: (plain.n.01) - extensive tract of level open land Examples: they emerged from
    the woods onto a vast open plain | he longed for the fields of his youth
  * Comment: I originally selected sense 9 only because the author is thinking more generally about
    open land that could be planted or not, whereas sense 1 is more specifically agricultural. On
    reflection, I decided that this is specifically set in England, where fields are reasonably
    small and enclosed, and most commonly used as farmland; in addition, there are few vast plains,
    so I ended up selecting both.

**Agreement:** Fine: Exactly two agree; Glite: All three agree; Maru2022 fine support: 0/3; Maru2022
Glite support: 3/3.

### D52. senseval2.d000.s006.t007

**Lemma/POS/source:** `bell` / `NOUN` / `senseval2` (`senseval2.d000`)

**Sentence:** But there is also a discordant, modern note in Aslacton, though it can not be heard by
the church-goers enjoying the peal of **[bells]** this cool autumn evening.

**Maru2022 label**

* bell%1:06:00:: (bell.n.01) - a hollow device made of metal that makes a ringing sound when struck

**Reviewer verdicts**

* **Robert Farren (RF)**
  * bell%1:06:00:: (bell.n.01) - a hollow device made of metal that makes a ringing sound when
    struck
* **Patrick White (PW)**
  * bell%1:06:00:: (bell.n.01) - a hollow device made of metal that makes a ringing sound when
    struck
* **Penny Hands (PH)**
  * bell%1:11:00:: (bell.n.03) - the sound of a bell being struck Examples: saved by the bell | she
    heard the distant toll of church bells

**Agreement:** Fine: Exactly two agree; Glite: Exactly two agree; Maru2022 fine support: 2/3;
Maru2022 Glite support: 2/3.

### D53. senseval2.d000.s011.t004

**Lemma/POS/source:** `say` / `VERB` / `senseval2` (`senseval2.d000`)

**Sentence:** `To ring for even one service at this tower, we have to scrape, `**[says]** Mr.
Hammond, a retired water-authority worker. ``

**Maru2022 label**

* say%2:32:15:: (say.v.08) - utter aloud Examples: She said `Hello' to everyone in the office

**Reviewer verdicts**

* **Robert Farren (RF)**
  * say%2:32:15:: (say.v.08) - utter aloud Examples: She said `Hello' to everyone in the office
* **Patrick White (PW)**
  * say%2:32:00:: (state.v.01) - express in words Examples: He said that he wanted to marry her |
    tell me what is bothering you
  * say%2:32:15:: (say.v.08) - utter aloud Examples: She said `Hello' to everyone in the office
  * Comment: Unclear if reported speech or quote from something written
* **Penny Hands (PH)**
  * say%2:32:00:: (state.v.01) - express in words Examples: He said that he wanted to marry her |
    tell me what is bothering you
  * say%2:32:15:: (say.v.08) - utter aloud Examples: She said `Hello' to everyone in the office
  * Comment: Sense 8 seems to be about direct speech, i.e. a quote + a reporting verb (say). But
    there is no proof that he uttered this statement aloud; it could have been a written statement.
    That's why I also selected sense 1.

**Agreement:** Fine: Exactly two agree; Glite: All three agree; Maru2022 fine support: 1/3; Maru2022
Glite support: 3/3.

### D54. senseval2.d000.s014.t000

**Lemma/POS/source:** `history` / `NOUN` / `senseval2` (`senseval2.d000`)

**Sentence:** **[History]**, after all, is not on his side.

**Maru2022 label**

* history%1:28:00:: (history.n.01) - the aggregate of past events Examples: a critical time in the
  school's history

**Reviewer verdicts**

* **Robert Farren (RF)**
  * history%1:28:02:: (history.n.04) - the continuum of events occurring in succession leading from
    the past to the present and even into the future Examples: all of human history
* **Patrick White (PW)**
  * history%1:28:00:: (history.n.01) - the aggregate of past events Examples: a critical time in the
    school's history
* **Penny Hands (PH)**
  * history%1:28:00:: (history.n.01) - the aggregate of past events Examples: a critical time in the
    school's history

**Agreement:** Fine: Exactly two agree; Glite: All three agree; Maru2022 fine support: 2/3; Maru2022
Glite support: 3/3.

### D55. senseval2.d000.s021.t000

**Lemma/POS/source:** `variation` / `NOUN` / `senseval2` (`senseval2.d000`)

**Sentence:** Each **[variation]**, or change, can occur only once, the rules state.

**Maru2022 label**

* variation%1:09:01:: (version.n.02) - something a little different from others of the same type
  Examples: an experimental version of the night fighter | a variant of the same word
* variation%1:10:00:: (variation.n.03) - a repetition of a musical theme in which it is modified or
  embellished

**Reviewer verdicts**

* **Robert Farren (RF)**
  * variation%1:10:00:: (variation.n.03) - a repetition of a musical theme in which it is modified
    or embellished
* **Patrick White (PW)**
  * variation%1:11:01:: (variation.n.01) - an instance of change; the rate or magnitude of change
* **Penny Hands (PH)**
  * variation%1:10:00:: (variation.n.03) - a repetition of a musical theme in which it is modified
    or embellished

**Agreement:** Fine: Exactly two agree; Glite: Exactly two agree; Maru2022 fine support: 0/3;
Maru2022 Glite support: 0/3.

### D56. senseval2.d000.s027.t004

**Lemma/POS/source:** `straight` / `ADV` / `senseval2` (`senseval2.d000`)

**Sentence:** Totally absorbed, the ringers stare **[straight]** ahead, using peripheral vision
(they call it `rope-sight `) to watch the other ropes and thus time their pulls.

**Maru2022 label**

* straight%4:02:00:: (straight.r.03) - in a straight line; in a direct course Examples: the road
  runs straight

**Reviewer verdicts**

* **Robert Farren (RF)**
  * straight%4:02:05:: (directly.r.01) - without deviation Examples: the path leads directly to the
    lake | went direct to the office
  * Comment: The word "straight" in the phrase "straight ahead" serves as an intensifier and is
    essentially redundant. "Straight ahead" simply means "ahead", neither to left or right. Sense 1
    is probably close enough, but it's not entirely accurate.
* **Patrick White (PW)**
  * straight%4:02:05:: (directly.r.01) - without deviation Examples: the path leads directly to the
    lake | went direct to the office
* **Penny Hands (PH)**
  * straight%4:02:00:: (straight.r.03) - in a straight line; in a direct course Examples: the road
    runs straight

**Agreement:** Fine: Exactly two agree; Glite: All three agree; Maru2022 fine support: 1/3; Maru2022
Glite support: 3/3.

### D57. senseval2.d000.s027.t008

**Lemma/POS/source:** `call` / `VERB` / `senseval2` (`senseval2.d000`)

**Sentence:** Totally absorbed, the ringers stare straight ahead, using peripheral vision (they
**[call]** it `rope-sight `) to watch the other ropes and thus time their pulls.

**Maru2022 label**

* call%2:32:00:: (call.v.02) - ascribe a quality to or give a name of a common noun that reflects a
  quality Examples: He called me a bastard | She called her children lazy and ungrateful

**Reviewer verdicts**

* **Robert Farren (RF)**
  * call%2:32:02:: (name.v.01) - assign a specified (usually proper) proper name to Examples: They
    named their son David | The new school was named after the famous Civil Rights leader
* **Patrick White (PW)**
  * call%2:32:02:: (name.v.01) - assign a specified (usually proper) proper name to Examples: They
    named their son David | The new school was named after the famous Civil Rights leader
* **Penny Hands (PH)**
  * call%2:32:00:: (call.v.02) - ascribe a quality to or give a name of a common noun that reflects
    a quality Examples: He called me a bastard | She called her children lazy and ungrateful

**Agreement:** Fine: Exactly two agree; Glite: All three agree; Maru2022 fine support: 1/3; Maru2022
Glite support: 3/3.

### D58. senseval2.d000.s027.t012

**Lemma/POS/source:** `thus` / `ADV` / `senseval2` (`senseval2.d000`)

**Sentence:** Totally absorbed, the ringers stare straight ahead, using peripheral vision (they call
it `rope-sight `) to watch the other ropes and **[thus]** time their pulls.

**Maru2022 label**

* thus%4:02:00:: (therefore.r.01) - (used to introduce a logical conclusion) from that fact or
  reason or as a result Examples: therefore X must be true | the eggs were fresh and hence
  satisfactory

**Reviewer verdicts**

* **Robert Farren (RF)**
  * thus%4:02:00:: (therefore.r.01) - (used to introduce a logical conclusion) from that fact or
    reason or as a result Examples: therefore X must be true | the eggs were fresh and hence
    satisfactory
* **Patrick White (PW)**
  * thus%4:02:00:: (therefore.r.01) - (used to introduce a logical conclusion) from that fact or
    reason or as a result Examples: therefore X must be true | the eggs were fresh and hence
    satisfactory
* **Penny Hands (PH)**
  * Cannot answer: inventory inadequate
  * Note: Sense 2 is closest, but to cover the meaning exactly, it would have to say 'in the way
    indicated *or described*.

**Agreement:** Fine: Exactly two agree; Glite: Exactly two agree; Maru2022 fine support: 2/3;
Maru2022 Glite support: 2/3.

### D59. senseval2.d000.s028.t009

**Lemma/POS/source:** `madly` / `ADV` / `senseval2` (`senseval2.d000`)

**Sentence:** Far above in the belfry, the huge bronze bells, mounted on wheels, swing **[madly]**
through a full 360 degrees, starting and ending, surprisingly, in the inverted, or mouth-up
position.

**Maru2022 label**

* madly%4:02:00:: (madly.r.03) - (used as intensives) extremely Examples: she was madly in love |
  deadly dull

**Reviewer verdicts**

* **Robert Farren (RF)**
  * Cannot answer: no sense applies
  * Note: The desired effect of "madly" in this sentence seems to be to give an impression of great
    kinetic force. The author is seeking effect by using a term that would usually be applied to an
    animate referent. The sense is figurative and means "powerfully, forcefully".
* **Patrick White (PW)**
  * madly%4:02:02:: (madly.r.01) - in an uncontrolled manner Examples: she fought back madly
* **Penny Hands (PH)**
  * madly%4:02:02:: (madly.r.01) - in an uncontrolled manner Examples: she fought back madly

**Agreement:** Fine: Exactly two agree; Glite: Exactly two agree; Maru2022 fine support: 0/3;
Maru2022 Glite support: 2/3.

### D60. senseval2.d000.s029.t006

**Lemma/POS/source:** `swing` / `NOUN` / `senseval2` (`senseval2.d000`)

**Sentence:** Skilled ringers use their wrists to advance or retard the next **[swing]**, so that
one bell can swap places with another in the following change.

**Maru2022 label**

* swing%1:04:06:: (swing.n.03) - a sweeping blow or stroke Examples: he took a wild swing at my head

**Reviewer verdicts**

* **Robert Farren (RF)**
  * swing%1:04:00:: (swing.n.04) - changing location by moving back and forth
* **Patrick White (PW)**
  * swing%1:04:06:: (swing.n.03) - a sweeping blow or stroke Examples: he took a wild swing at my
    head
* **Penny Hands (PH)**
  * swing%1:04:00:: (swing.n.04) - changing location by moving back and forth
  * Comment: I've chosen sense 4, but the grammar is odd. It seems to be defining the noun 'swing'
    as if it were an adjective (e.g. 'swinging bells'). It should be worded as something like 'a
    back-and-forth movement'. I suppose it's seen as a gerund, but still, it seems a bit misleading
    and it's not usual to do this.

**Agreement:** Fine: Exactly two agree; Glite: Exactly two agree; Maru2022 fine support: 1/3;
Maru2022 Glite support: 1/3.

### D61. senseval2.d000.s029.t008

**Lemma/POS/source:** `bell` / `NOUN` / `senseval2` (`senseval2.d000`)

**Sentence:** Skilled ringers use their wrists to advance or retard the next swing, so that one
**[bell]** can swap places with another in the following change.

**Maru2022 label**

* bell%1:11:00:: (bell.n.03) - the sound of a bell being struck Examples: saved by the bell | she
  heard the distant toll of church bells

**Reviewer verdicts**

* **Robert Farren (RF)**
  * bell%1:06:00:: (bell.n.01) - a hollow device made of metal that makes a ringing sound when
    struck
* **Patrick White (PW)**
  * bell%1:06:00:: (bell.n.01) - a hollow device made of metal that makes a ringing sound when
    struck
* **Penny Hands (PH)**
  * bell%1:11:00:: (bell.n.03) - the sound of a bell being struck Examples: saved by the bell | she
    heard the distant toll of church bells
  * Comment: The focus is the pattern of sounds.

**Agreement:** Fine: Exactly two agree; Glite: Exactly two agree; Maru2022 fine support: 1/3;
Maru2022 Glite support: 1/3.

### D62. senseval2.d000.s030.t011

**Lemma/POS/source:** `mathematical` / `ADJ` / `senseval2` (`senseval2.d000`)

**Sentence:** In a well-known detective-story involving church bells, English novelist Dorothy L.
Sayers described ringing as a
`passion that finds its satisfaction in **[mathematical]** completeness and mechanical perfection. `

**Maru2022 label**

* mathematical%5:00:00:exact:00 (mathematical.s.03) - characterized by the exactness or precision of
  mathematics Examples: mathematical precision

**Reviewer verdicts**

* **Robert Farren (RF)**
  * Cannot answer: no sense applies
  * Note: In my opinion this sense of "mathematical" is figurative, and is intended to evoke the
    full logical development and expression from start to finish of a pattern, which can then be
    repeated. It's not only about "exactness or precision" (sense 5), but completeness within a
    cycle, as if the modifier has been chosen only to give more force to the head noun
    "completeness".
* **Patrick White (PW)**
  * mathematical%5:00:00:exact:00 (mathematical.s.03) - characterized by the exactness or precision
    of mathematics Examples: mathematical precision
* **Penny Hands (PH)**
  * mathematical%5:00:00:exact:00 (mathematical.s.03) - characterized by the exactness or precision
    of mathematics Examples: mathematical precision

**Agreement:** Fine: Exactly two agree; Glite: Exactly two agree; Maru2022 fine support: 2/3;
Maru2022 Glite support: 2/3.

### D63. senseval2.d000.s031.t004

**Lemma/POS/source:** `come` / `VERB` / `senseval2` (`senseval2.d000`)

**Sentence:** Ringers, she added, are
``filled with the solemn intoxication that **[comes]** of intricate ritual faultlessly performed. ````

**Maru2022 label**

* come%2:42:04:: (come.v.05) - to be the product or result Examples: Melons come from a vine |
  Understanding comes from experience

**Reviewer verdicts**

* **Robert Farren (RF)**
  * come%2:42:04:: (come.v.05) - to be the product or result Examples: Melons come from a vine |
    Understanding comes from experience
* **Patrick White (PW)**
  * come%2:30:13:: (come.v.13) - happen as a result Examples: Nothing good will come of this
* **Penny Hands (PH)**
  * come%2:30:13:: (come.v.13) - happen as a result Examples: Nothing good will come of this
  * Comment: Sense 13 because it's a kind of phrasal verb: 'to come of something' and sense 13 is
    the only sense that demonstrates that. However, it could be said the 'come of sth' (sense 13)and
    come from sth' (sense 5) are simply variants of the same phrasal verb, which means 'to be the
    result of something'.

**Agreement:** Fine: Exactly two agree; Glite: Exactly two agree; Maru2022 fine support: 1/3;
Maru2022 Glite support: 1/3.

### D64. senseval2.d000.s035.t009

**Lemma/POS/source:** `leave` / `VERB` / `senseval2` (`senseval2.d000`)

**Sentence:** When their changes are completed, and after they have worked up a sweat, ringers often
skip off to the local pub, **[leaving]** worship for others below.

**Maru2022 label**

* leave%2:31:05:: (leave.v.02) - go and leave behind, either intentionally or by neglect or
  forgetfulness Examples: She left a mess when she moved out | His good luck finally left him

**Reviewer verdicts**

* **Robert Farren (RF)**
  * leave%2:40:06:: (entrust.v.02) - put into the care or protection of someone Examples: He left
    the decision to his deputy | leave your child the nurse's care
* **Patrick White (PW)**
  * leave%2:40:06:: (entrust.v.02) - put into the care or protection of someone Examples: He left
    the decision to his deputy | leave your child the nurse's care
* **Penny Hands (PH)**
  * leave%2:31:05:: (leave.v.02) - go and leave behind, either intentionally or by neglect or
    forgetfulness Examples: She left a mess when she moved out | His good luck finally left him
  * Comment: Not sense 9 because they are not leaving worship *in the care of* the others below.

**Agreement:** Fine: Exactly two agree; Glite: Exactly two agree; Maru2022 fine support: 1/3;
Maru2022 Glite support: 1/3.

### D65. senseval2.d000.s035.t011

**Lemma/POS/source:** `below` / `ADV` / `senseval2` (`senseval2.d000`)

**Sentence:** When their changes are completed, and after they have worked up a sweat, ringers often
skip off to the local pub, leaving worship for others **[below]**.

**Maru2022 label**

* below%4:02:06:: (downstairs.r.01) - on a floor below Examples: the tenants live downstairs

**Reviewer verdicts**

* **Robert Farren (RF)**
  * below%4:02:01:: (below.r.01) - in or to a place that is lower
* **Patrick White (PW)**
  * below%4:02:06:: (downstairs.r.01) - on a floor below Examples: the tenants live downstairs
* **Penny Hands (PH)**
  * below%4:02:06:: (downstairs.r.01) - on a floor below Examples: the tenants live downstairs

**Agreement:** Fine: Exactly two agree; Glite: All three agree; Maru2022 fine support: 2/3; Maru2022
Glite support: 3/3.

### D66. senseval2.d000.s039.t006

**Lemma/POS/source:** `say` / `VERB` / `senseval2` (`senseval2.d000`)

**Sentence:**
`They were a self-perpetuating club that treated the tower as sort of a separate premises, `the
Vicar Hummerstone **[says]**.

**Maru2022 label**

* say%2:32:15:: (say.v.08) - utter aloud Examples: She said `Hello' to everyone in the office

**Reviewer verdicts**

* **Robert Farren (RF)**
  * say%2:32:13:: (say.v.09) - state as one's opinion or judgement; declare Examples: I say let's
    forget this whole business
  * Comment: I can see good reasons to include both sense 8 and sense 9. But since we're opting for
    one meaning where possible, sense 9 is the better choice.
* **Patrick White (PW)**
  * say%2:32:00:: (state.v.01) - express in words Examples: He said that he wanted to marry her |
    tell me what is bothering you
  * say%2:32:15:: (say.v.08) - utter aloud Examples: She said `Hello' to everyone in the office
  * Comment: Unclear if reported speech or quote from something written
* **Penny Hands (PH)**
  * say%2:32:00:: (state.v.01) - express in words Examples: He said that he wanted to marry her |
    tell me what is bothering you
  * say%2:32:15:: (say.v.08) - utter aloud Examples: She said `Hello' to everyone in the office
  * Comment: Sense 8 seems to be about direct speech, i.e. a quote + a reporting verb (say). But
    there is no proof that he uttered this statement aloud; it could have been a written statement.
    That's why I also selected sense 1.

**Agreement:** Fine: Exactly two agree; Glite: All three agree; Maru2022 fine support: 0/3; Maru2022
Glite support: 3/3.

### D67. senseval2.d000.s043.t003

**Lemma/POS/source:** `say` / `VERB` / `senseval2` (`senseval2.d000`)

**Sentence:** The vicar, W.D. Jones, refuses to talk about it, **[saying]** it would
`reopen the wound. `

**Maru2022 label**

* say%2:32:15:: (say.v.08) - utter aloud Examples: She said `Hello' to everyone in the office

**Reviewer verdicts**

* **Robert Farren (RF)**
  * say%2:32:13:: (say.v.09) - state as one's opinion or judgement; declare Examples: I say let's
    forget this whole business
  * Comment: The fact that part of this complement clause is a direct quotation does not justify
    choosing sense 8 over sense 9.
* **Patrick White (PW)**
  * say%2:32:00:: (state.v.01) - express in words Examples: He said that he wanted to marry her |
    tell me what is bothering you
  * say%2:32:15:: (say.v.08) - utter aloud Examples: She said `Hello' to everyone in the office
  * Comment: Unclear if reported speech or quote from something written
* **Penny Hands (PH)**
  * say%2:32:00:: (state.v.01) - express in words Examples: He said that he wanted to marry her |
    tell me what is bothering you
  * say%2:32:15:: (say.v.08) - utter aloud Examples: She said `Hello' to everyone in the office
  * Comment: Sense 8 seems to be about direct speech, i.e. a quote + a reporting verb (say). But
    there is no proof that he uttered this statement aloud; it could have been a written statement.
    That's why I also selected sense 1.

**Agreement:** Fine: Exactly two agree; Glite: All three agree; Maru2022 fine support: 0/3; Maru2022
Glite support: 3/3.

### D68. senseval2.d000.s045.t000

**Lemma/POS/source:** `so` / `ADV` / `senseval2` (`senseval2.d000`)

**Sentence:**
`**[So]** crunch, crunch, crunch, bang, bang, bang -- here come the ringers from above, making a very obvious exit while the congregation is at prayer, `he
says.

**Maru2022 label**

* so%4:02:09:: (then.r.01) - subsequently or soon afterward (often used as sentence connectors)
  Examples: then he left | go left first, then right

**Reviewer verdicts**

* **Robert Farren (RF)**
  * so%4:02:10:: (therefore.r.01) - (used to introduce a logical conclusion) from that fact or
    reason or as a result Examples: therefore X must be true | the eggs were fresh and hence
    satisfactory
* **Patrick White (PW)**
  * so%4:02:10:: (therefore.r.01) - (used to introduce a logical conclusion) from that fact or
    reason or as a result Examples: therefore X must be true | the eggs were fresh and hence
    satisfactory
* **Penny Hands (PH)**
  * Cannot answer: no sense applies
  * Note: There's a (sentence adverb) sense missing – 'used to introduce the next part of a story or
    description', e.g. 'So, the next thing I know, she's left the room in tears!' 'So, once they've
    finished, the bellringers come down the back stairs, chatting and laughing for all to hear.'

**Agreement:** Fine: Exactly two agree; Glite: Exactly two agree; Maru2022 fine support: 0/3;
Maru2022 Glite support: 2/3.

### D69. senseval2.d000.s045.t017

**Lemma/POS/source:** `say` / `VERB` / `senseval2` (`senseval2.d000`)

**Sentence:**
`So crunch, crunch, crunch, bang, bang, bang -- here come the ringers from above, making a very obvious exit while the congregation is at prayer, `he
**[says]**.

**Maru2022 label**

* say%2:32:15:: (say.v.08) - utter aloud Examples: She said `Hello' to everyone in the office

**Reviewer verdicts**

* **Robert Farren (RF)**
  * say%2:32:15:: (say.v.08) - utter aloud Examples: She said `Hello' to everyone in the office
* **Patrick White (PW)**
  * say%2:32:00:: (state.v.01) - express in words Examples: He said that he wanted to marry her |
    tell me what is bothering you
  * say%2:32:15:: (say.v.08) - utter aloud Examples: She said `Hello' to everyone in the office
  * Comment: Unclear if reported speech or quote from something written
* **Penny Hands (PH)**
  * say%2:32:00:: (state.v.01) - express in words Examples: He said that he wanted to marry her |
    tell me what is bothering you
  * say%2:32:15:: (say.v.08) - utter aloud Examples: She said `Hello' to everyone in the office
  * Comment: Sense 8 seems to be about direct speech, i.e. a quote + a reporting verb (say). But
    there is no proof that he uttered this statement aloud; it could have been a written statement.
    That's why I also selected sense 1.

**Agreement:** Fine: Exactly two agree; Glite: All three agree; Maru2022 fine support: 1/3; Maru2022
Glite support: 3/3.

### D70. senseval2.d000.s047.t001

**Lemma/POS/source:** `bell` / `NOUN` / `senseval2` (`senseval2.d000`)

**Sentence:** `The sound of **[bells]** is a net to draw people into the church, `he says.

**Maru2022 label**

* bell%1:06:00:: (bell.n.01) - a hollow device made of metal that makes a ringing sound when struck

**Reviewer verdicts**

* **Robert Farren (RF)**
  * bell%1:06:00:: (bell.n.01) - a hollow device made of metal that makes a ringing sound when
    struck
* **Patrick White (PW)**
  * bell%1:06:00:: (bell.n.01) - a hollow device made of metal that makes a ringing sound when
    struck
* **Penny Hands (PH)**
  * bell%1:11:00:: (bell.n.03) - the sound of a bell being struck Examples: saved by the bell | she
    heard the distant toll of church bells

**Agreement:** Fine: Exactly two agree; Glite: Exactly two agree; Maru2022 fine support: 2/3;
Maru2022 Glite support: 2/3.

### D71. senseval2.d000.s047.t005

**Lemma/POS/source:** `say` / `VERB` / `senseval2` (`senseval2.d000`)

**Sentence:** `The sound of bells is a net to draw people into the church, `he **[says]**.

**Maru2022 label**

* say%2:32:15:: (say.v.08) - utter aloud Examples: She said `Hello' to everyone in the office

**Reviewer verdicts**

* **Robert Farren (RF)**
  * say%2:32:15:: (say.v.08) - utter aloud Examples: She said `Hello' to everyone in the office
* **Patrick White (PW)**
  * say%2:32:00:: (state.v.01) - express in words Examples: He said that he wanted to marry her |
    tell me what is bothering you
  * say%2:32:15:: (say.v.08) - utter aloud Examples: She said `Hello' to everyone in the office
  * Comment: Unclear if reported speech or quote from something written
* **Penny Hands (PH)**
  * say%2:32:00:: (state.v.01) - express in words Examples: He said that he wanted to marry her |
    tell me what is bothering you
  * say%2:32:15:: (say.v.08) - utter aloud Examples: She said `Hello' to everyone in the office
  * Comment: Sense 8 seems to be about direct speech, i.e. a quote + a reporting verb (say). But
    there is no proof that he uttered this statement aloud; it could have been a written statement.
    That's why I also selected sense 1.

**Agreement:** Fine: Exactly two agree; Glite: All three agree; Maru2022 fine support: 1/3; Maru2022
Glite support: 3/3.

### D72. senseval2.d000.s048.t004

**Lemma/POS/source:** `full` / `ADJ` / `senseval2` (`senseval2.d000`)

**Sentence:**
`I live in hopes that the ringers themselves will be drawn into that **[fuller]** life. `

**Maru2022 label**

* full%3:00:00:: (full.a.01) - containing as much or as many as is possible or normal Examples: a
  full glass | a sky full of stars

**Reviewer verdicts**

* **Robert Farren (RF)**
  * full%3:00:00:: (full.a.01) - containing as much or as many as is possible or normal Examples: a
    full glass | a sky full of stars
* **Patrick White (PW)**
  * full%3:00:00:: (full.a.01) - containing as much or as many as is possible or normal Examples: a
    full glass | a sky full of stars
* **Penny Hands (PH)**
  * Cannot answer: no sense applies
  * Note: The sense missing is 'fulfilling, involving lots of interesting things'.

**Agreement:** Fine: Exactly two agree; Glite: Exactly two agree; Maru2022 fine support: 2/3;
Maru2022 Glite support: 2/3.

### D73. senseval2.d000.s048.t005

**Lemma/POS/source:** `life` / `NOUN` / `senseval2` (`senseval2.d000`)

**Sentence:**
`I live in hopes that the ringers themselves will be drawn into that fuller **[life]**. `

**Maru2022 label**

* life%1:26:02:: (life.n.03) - the course of existence of an individual; the actions and events that
  occur in living Examples: he hoped for a new life in Australia | he wanted to live his own life
  without interference from others

**Reviewer verdicts**

* **Robert Farren (RF)**
  * life%1:26:01:: (life.n.01) - a characteristic state or mode of living Examples: social life |
    city life
* **Patrick White (PW)**
  * life%1:26:02:: (life.n.03) - the course of existence of an individual; the actions and events
    that occur in living Examples: he hoped for a new life in Australia | he wanted to live his own
    life without interference from others
* **Penny Hands (PH)**
  * life%1:26:01:: (life.n.01) - a characteristic state or mode of living Examples: social life |
    city life

**Agreement:** Fine: Exactly two agree; Glite: Exactly two agree; Maru2022 fine support: 1/3;
Maru2022 Glite support: 1/3.

### D74. senseval2.d000.s050.t001

**Lemma/POS/source:** `speak` / `VERB` / `senseval2` (`senseval2.d000`)

**Sentence:** It hopes to **[speak]** to students at theological colleges about the joys of bell
ringing and will shortly publish a booklet for every vicar in the country entitled,
`The Bells in Your Care. `

**Maru2022 label**

* speak%2:32:01:: (talk.v.01) - exchange thoughts; talk with Examples: We often talk business |
  Actions talk louder than words

**Reviewer verdicts**

* **Robert Farren (RF)**
  * speak%2:32:01:: (talk.v.01) - exchange thoughts; talk with Examples: We often talk business |
    Actions talk louder than words
  * speak%2:32:03:: (address.v.02) - give a speech to Examples: The chairman addressed the board of
    trustees
  * Comment: Both of the sense I've chosen seem equally plausible, and the context doesn't give any
    indication which one is meant. In practice, probably both.
* **Patrick White (PW)**
  * speak%2:32:01:: (talk.v.01) - exchange thoughts; talk with Examples: We often talk business |
    Actions talk louder than words
  * speak%2:32:03:: (address.v.02) - give a speech to Examples: The chairman addressed the board of
    trustees
  * Comment: It is unclear whether the Council will give a formal talk to the students or just
    conduct informal conversations.
* **Penny Hands (PH)**
  * speak%2:32:03:: (address.v.02) - give a speech to Examples: The chairman addressed the board of
    trustees
  * Comment: Based on the context, I think it's very likely to be sense 4 and not 2, although I'm
    sure they would also be happy to exchange thoughts and talk with the students. Another thing
    that put me off sense 2 were the examples, none of which illustrate the most common use: 'speak
    to someone about something'.

**Agreement:** Fine: Exactly two agree; Glite: Exactly two agree; Maru2022 fine support: 0/3;
Maru2022 Glite support: 0/3.

### D75. senseval2.d000.s051.t000

**Lemma/POS/source:** `say` / `VERB` / `senseval2` (`senseval2.d000`)

**Sentence:** **[Says]** Mr. Baldwin,
`We recognize that we may no longer have as high a priority in church life and experience. `

**Maru2022 label**

* say%2:32:15:: (say.v.08) - utter aloud Examples: She said `Hello' to everyone in the office

**Reviewer verdicts**

* **Robert Farren (RF)**
  * say%2:32:13:: (say.v.09) - state as one's opinion or judgement; declare Examples: I say let's
    forget this whole business
  * Comment: I can see good reasons to include both sense 8 and sense 9. But since we're opting for
    one meaning where possible, sense 9 is the better choice.
* **Patrick White (PW)**
  * say%2:32:00:: (state.v.01) - express in words Examples: He said that he wanted to marry her |
    tell me what is bothering you
  * say%2:32:15:: (say.v.08) - utter aloud Examples: She said `Hello' to everyone in the office
  * Comment: Unclear if reported speech or quote from something written
* **Penny Hands (PH)**
  * say%2:32:00:: (state.v.01) - express in words Examples: He said that he wanted to marry her |
    tell me what is bothering you
  * say%2:32:15:: (say.v.08) - utter aloud Examples: She said `Hello' to everyone in the office
  * Comment: Sense 8 seems to be about direct speech, i.e. a quote + a reporting verb (say). But
    there is no proof that he uttered this statement aloud; it could have been a written statement.
    That's why I also selected sense 1.

**Agreement:** Fine: Exactly two agree; Glite: All three agree; Maru2022 fine support: 0/3; Maru2022
Glite support: 3/3.

### D76. senseval2.d000.s054.t007

**Lemma/POS/source:** `small` / `ADJ` / `senseval2` (`senseval2.d000`)

**Sentence:** Also, ringers do not always live where the bells need to be rung -- like in
**[small]**, rural parishes and inner-city churches.

**Maru2022 label**

* small%5:00:00:limited:00 (minor.s.03) - limited in size or scope Examples: a small business | a
  newspaper with a modest circulation

**Reviewer verdicts**

* **Robert Farren (RF)**
  * small%3:00:00:: (small.a.01) - limited or below average in number or quantity or magnitude or
    extent Examples: a little dining room | a little house
* **Patrick White (PW)**
  * small%5:00:00:limited:00 (minor.s.03) - limited in size or scope Examples: a small business | a
    newspaper with a modest circulation
* **Penny Hands (PH)**
  * small%3:00:00:: (small.a.01) - limited or below average in number or quantity or magnitude or
    extent Examples: a little dining room | a little house

**Agreement:** Fine: Exactly two agree; Glite: All three agree; Maru2022 fine support: 1/3; Maru2022
Glite support: 3/3.

### D77. senseval2.d000.s055.t001

**Lemma/POS/source:** `program` / `NOUN` / `senseval2` (`senseval2.d000`)

**Sentence:** But the council's **[program]** to attract and train ringers is only partly
successful, says Mr. Baldwin.

**Maru2022 label**

* program%1:09:00:: (plan.n.01) - a series of steps to be carried out or goals to be accomplished
  Examples: they drew up a six-step plan | they discussed plans for a new bond issue

**Reviewer verdicts**

* **Robert Farren (RF)**
  * program%1:09:00:: (plan.n.01) - a series of steps to be carried out or goals to be accomplished
    Examples: they drew up a six-step plan | they discussed plans for a new bond issue
* **Patrick White (PW)**
  * program%1:09:01:: (program.n.02) - a system of projects or services intended to meet a public
    need Examples: he proposed an elaborate program of public works | working mothers rely on the
    day care program
* **Penny Hands (PH)**
  * program%1:09:01:: (program.n.02) - a system of projects or services intended to meet a public
    need Examples: he proposed an elaborate program of public works | working mothers rely on the
    day care program

**Agreement:** Fine: Exactly two agree; Glite: All three agree; Maru2022 fine support: 1/3; Maru2022
Glite support: 3/3.

### D78. senseval2.d000.s063.t002

**Lemma/POS/source:** `say` / `VERB` / `senseval2` (`senseval2.d000`)

**Sentence:** Another women wrote from Sheffield to **[say]** that in her 60 years of ringing, ``I
have never known a lady to faint in the belfry.

**Maru2022 label**

* say%2:32:01:: (allege.v.01) - report or maintain Examples: He alleged that he was the victim of a
  crime | He said it was too late to intervene in the war

**Reviewer verdicts**

* **Robert Farren (RF)**
  * say%2:32:01:: (allege.v.01) - report or maintain Examples: He alleged that he was the victim of
    a crime | He said it was too late to intervene in the war
* **Patrick White (PW)**
  * say%2:32:00:: (state.v.01) - express in words Examples: He said that he wanted to marry her |
    tell me what is bothering you
* **Penny Hands (PH)**
  * say%2:32:00:: (state.v.01) - express in words Examples: He said that he wanted to marry her |
    tell me what is bothering you
  * Comment: Not sense 8 this time because it is specified that his was in writing.

**Agreement:** Fine: Exactly two agree; Glite: All three agree; Maru2022 fine support: 1/3; Maru2022
Glite support: 3/3.

### D79. senseval2.d001.s000.t008

**Lemma/POS/source:** `growth` / `NOUN` / `senseval2` (`senseval2.d001`)

**Sentence:** Medical scientists are starting to uncover a handful of genes which, if damaged,
unleash the chaotic **[growth]** of cells that characterizes cancer.

**Maru2022 label**

* growth%1:17:00:: (growth.n.07) - something grown or growing Examples: a growth of hair
* growth%1:22:00:: (growth.n.01) - (biology) the process of an individual organism growing
  organically; a purely biological unfolding of events involved in an organism changing gradually
  from a simple to a more complex level Examples: he proposed an indicator of osseous development in
  children

**Reviewer verdicts**

* **Robert Farren (RF)**
  * growth%1:22:00:: (growth.n.01) - (biology) the process of an individual organism growing
    organically; a purely biological unfolding of events involved in an organism changing gradually
    from a simple to a more complex level Examples: he proposed an indicator of osseous development
    in children
* **Patrick White (PW)**
  * growth%1:22:02:: (increase.n.03) - a process of becoming larger or longer or more numerous or
    more important Examples: the increase in unemployment | the growth of population
* **Penny Hands (PH)**
  * growth%1:22:02:: (increase.n.03) - a process of becoming larger or longer or more numerous or
    more important Examples: the increase in unemployment | the growth of population

**Agreement:** Fine: Exactly two agree; Glite: Exactly two agree; Maru2022 fine support: 0/3;
Maru2022 Glite support: 0/3.

### D80. senseval2.d001.s005.t002

**Lemma/POS/source:** `say` / `VERB` / `senseval2` (`senseval2.d001`)

**Sentence:** `It's a super-exciting set of discoveries, `**[says]** Bert Vogelstein, a Johns
Hopkins University researcher who has just found a gene pivotal to the triggering of colon cancer.

**Maru2022 label**

* say%2:32:15:: (say.v.08) - utter aloud Examples: She said `Hello' to everyone in the office

**Reviewer verdicts**

* **Robert Farren (RF)**
  * say%2:32:15:: (say.v.08) - utter aloud Examples: She said `Hello' to everyone in the office
* **Patrick White (PW)**
  * say%2:32:00:: (state.v.01) - express in words Examples: He said that he wanted to marry her |
    tell me what is bothering you
  * say%2:32:15:: (say.v.08) - utter aloud Examples: She said `Hello' to everyone in the office
  * Comment: Unclear if reported speech or quote from something written
* **Penny Hands (PH)**
  * say%2:32:00:: (state.v.01) - express in words Examples: He said that he wanted to marry her |
    tell me what is bothering you
  * say%2:32:15:: (say.v.08) - utter aloud Examples: She said `Hello' to everyone in the office
  * Comment: Sense 8 seems to be about direct speech, i.e. a quote + a reporting verb (say). But
    there is no proof that he uttered this statement aloud; it could have been a written statement.
    That's why I also selected sense 1.

**Agreement:** Fine: Exactly two agree; Glite: All three agree; Maru2022 fine support: 1/3; Maru2022
Glite support: 3/3.

### D81. senseval2.d001.s008.t001

**Lemma/POS/source:** `call` / `VERB` / `senseval2` (`senseval2.d001`)

**Sentence:** Scientists **[call]** the new class of genes tumor-suppressors, or simply anti-cancer
genes.

**Maru2022 label**

* call%2:32:02:: (name.v.01) - assign a specified (usually proper) proper name to Examples: They
  named their son David | The new school was named after the famous Civil Rights leader

**Reviewer verdicts**

* **Robert Farren (RF)**
  * call%2:32:00:: (call.v.02) - ascribe a quality to or give a name of a common noun that reflects
    a quality Examples: He called me a bastard | She called her children lazy and ungrateful
* **Patrick White (PW)**
  * call%2:32:02:: (name.v.01) - assign a specified (usually proper) proper name to Examples: They
    named their son David | The new school was named after the famous Civil Rights leader
* **Penny Hands (PH)**
  * call%2:32:00:: (call.v.02) - ascribe a quality to or give a name of a common noun that reflects
    a quality Examples: He called me a bastard | She called her children lazy and ungrateful

**Agreement:** Fine: Exactly two agree; Glite: All three agree; Maru2022 fine support: 1/3; Maru2022
Glite support: 3/3.

### D82. senseval2.d001.s008.t005

**Lemma/POS/source:** `simply` / `ADV` / `senseval2` (`senseval2.d001`)

**Sentence:** Scientists call the new class of genes tumor-suppressors, or **[simply]** anti-cancer
genes.

**Maru2022 label**

* simply%4:02:01:: (plainly.r.02) - in a simple manner; without extravagance or embellishment
  Examples: she was dressed plainly | they lived very simply

**Reviewer verdicts**

* **Robert Farren (RF)**
  * simply%4:02:01:: (plainly.r.02) - in a simple manner; without extravagance or embellishment
    Examples: she was dressed plainly | they lived very simply
* **Patrick White (PW)**
  * simply%4:02:01:: (plainly.r.02) - in a simple manner; without extravagance or embellishment
    Examples: she was dressed plainly | they lived very simply
* **Penny Hands (PH)**
  * simply%4:02:00:: (merely.r.01) - and nothing more Examples: I was merely asking | it is simply a
    matter of time

**Agreement:** Fine: Exactly two agree; Glite: Exactly two agree; Maru2022 fine support: 2/3;
Maru2022 Glite support: 2/3.

### D83. senseval2.d001.s009.t004

**Lemma/POS/source:** `hold` / `VERB` / `senseval2` (`senseval2.d001`)

**Sentence:** When functioning normally, they make proteins that **[hold]** a cell's growth in
check.

**Maru2022 label**

* hold%2:42:00:: (keep.v.01) - keep in a certain state, position, or activity; e.g., Examples: keep
  clean | hold in place

**Reviewer verdicts**

* **Robert Farren (RF)**
  * hold%2:41:15:: (control.v.02) - lessen the intensity of; temper; hold in restraint; hold or keep
    within limits Examples: moderate your alcohol intake | hold your tongue
  * Comment: I chose a sense which is very close to the intended meaning. However, the verb in this
    sentence is actually the phrasal verb "hold in check", rather than just "hold".
* **Patrick White (PW)**
  * hold%2:42:00:: (keep.v.01) - keep in a certain state, position, or activity; e.g., Examples:
    keep clean | hold in place
* **Penny Hands (PH)**
  * hold%2:41:15:: (control.v.02) - lessen the intensity of; temper; hold in restraint; hold or keep
    within limits Examples: moderate your alcohol intake | hold your tongue

**Agreement:** Fine: Exactly two agree; Glite: Exactly two agree; Maru2022 fine support: 1/3;
Maru2022 Glite support: 1/3.

### D84. senseval2.d001.s009.t006

**Lemma/POS/source:** `growth` / `NOUN` / `senseval2` (`senseval2.d001`)

**Sentence:** When functioning normally, they make proteins that hold a cell's **[growth]** in
check.

**Maru2022 label**

* growth%1:22:00:: (growth.n.01) - (biology) the process of an individual organism growing
  organically; a purely biological unfolding of events involved in an organism changing gradually
  from a simple to a more complex level Examples: he proposed an indicator of osseous development in
  children

**Reviewer verdicts**

* **Robert Farren (RF)**
  * growth%1:22:00:: (growth.n.01) - (biology) the process of an individual organism growing
    organically; a purely biological unfolding of events involved in an organism changing gradually
    from a simple to a more complex level Examples: he proposed an indicator of osseous development
    in children
* **Patrick White (PW)**
  * growth%1:22:02:: (increase.n.03) - a process of becoming larger or longer or more numerous or
    more important Examples: the increase in unemployment | the growth of population
* **Penny Hands (PH)**
  * growth%1:22:02:: (increase.n.03) - a process of becoming larger or longer or more numerous or
    more important Examples: the increase in unemployment | the growth of population
  * Comment: While sense 1 appears to be the correct one at first glance, I think it is more about
    natural development, e.g. from a child to and adult.

**Agreement:** Fine: Exactly two agree; Glite: Exactly two agree; Maru2022 fine support: 1/3;
Maru2022 Glite support: 1/3.

### D85. senseval2.d001.s015.t006

**Lemma/POS/source:** `growth` / `NOUN` / `senseval2` (`senseval2.d001`)

**Sentence:** Either copy can make the proteins needed to control cell **[growth]**, so for cancer
to arise, both copies must be impaired.

**Maru2022 label**

* growth%1:22:00:: (growth.n.01) - (biology) the process of an individual organism growing
  organically; a purely biological unfolding of events involved in an organism changing gradually
  from a simple to a more complex level Examples: he proposed an indicator of osseous development in
  children

**Reviewer verdicts**

* **Robert Farren (RF)**
  * growth%1:22:00:: (growth.n.01) - (biology) the process of an individual organism growing
    organically; a purely biological unfolding of events involved in an organism changing gradually
    from a simple to a more complex level Examples: he proposed an indicator of osseous development
    in children
* **Patrick White (PW)**
  * growth%1:22:02:: (increase.n.03) - a process of becoming larger or longer or more numerous or
    more important Examples: the increase in unemployment | the growth of population
* **Penny Hands (PH)**
  * growth%1:22:02:: (increase.n.03) - a process of becoming larger or longer or more numerous or
    more important Examples: the increase in unemployment | the growth of population
  * Comment: I rejected sense 1 because I think that's more to do with natural developments, e.g. of
    a foetus, or of a child growing into an adult.

**Agreement:** Fine: Exactly two agree; Glite: Exactly two agree; Maru2022 fine support: 1/3;
Maru2022 Glite support: 1/3.

### D86. senseval2.d001.s017.t001

**Lemma/POS/source:** `genetic` / `ADJ` / `senseval2` (`senseval2.d001`)

**Sentence:** Emerging **[genetic]** tests will be able to spot such cancer-susceptible individuals,
ushering in what some scientists believe is a new age of predictive cancer diagnosis.

**Maru2022 label**

* genetic%3:01:00:: (genetic.a.04) - of or relating to the science of genetics Examples: genetic
  research

**Reviewer verdicts**

* **Robert Farren (RF)**
  * genetic%3:01:00:: (genetic.a.04) - of or relating to the science of genetics Examples: genetic
    research
* **Patrick White (PW)**
  * genetic%3:01:00:: (genetic.a.04) - of or relating to the science of genetics Examples: genetic
    research
* **Penny Hands (PH)**
  * genetic%3:01:02:: (genic.a.01) - of or relating to or produced by or being a gene Examples:
    genic combinations | genetic code

**Agreement:** Fine: Exactly two agree; Glite: All three agree; Maru2022 fine support: 2/3; Maru2022
Glite support: 3/3.

### D87. senseval2.d001.s023.t002

**Lemma/POS/source:** `say` / `VERB` / `senseval2` (`senseval2.d001`)

**Sentence:** `It made our New Year, `**[says]** Mr. Quinlan.

**Maru2022 label**

* say%2:32:15:: (say.v.08) - utter aloud Examples: She said `Hello' to everyone in the office

**Reviewer verdicts**

* **Robert Farren (RF)**
  * say%2:32:15:: (say.v.08) - utter aloud Examples: She said `Hello' to everyone in the office
* **Patrick White (PW)**
  * say%2:32:00:: (state.v.01) - express in words Examples: He said that he wanted to marry her |
    tell me what is bothering you
  * say%2:32:15:: (say.v.08) - utter aloud Examples: She said `Hello' to everyone in the office
  * Comment: Unclear if reported speech or quote from something written
* **Penny Hands (PH)**
  * say%2:32:00:: (state.v.01) - express in words Examples: He said that he wanted to marry her |
    tell me what is bothering you
  * say%2:32:15:: (say.v.08) - utter aloud Examples: She said `Hello' to everyone in the office
  * Comment: Sense 8 seems to be about direct speech, i.e. a quote + a reporting verb (say). But
    there is no proof that he uttered this statement aloud; it could have been a written statement.
    That's why I also selected sense 1.

**Agreement:** Fine: Exactly two agree; Glite: All three agree; Maru2022 fine support: 1/3; Maru2022
Glite support: 3/3.

### D88. senseval2.d001.s025.t008

**Lemma/POS/source:** `growth` / `NOUN` / `senseval2` (`senseval2.d001`)

**Sentence:** Equally important, the initial discovery of the gene that controls retinal cell
**[growth]**, made by a Boston doctor named Thaddeus Dryja, has opened a field of cancer study,
which in recent months has exploded.

**Maru2022 label**

* growth%1:22:00:: (growth.n.01) - (biology) the process of an individual organism growing
  organically; a purely biological unfolding of events involved in an organism changing gradually
  from a simple to a more complex level Examples: he proposed an indicator of osseous development in
  children

**Reviewer verdicts**

* **Robert Farren (RF)**
  * growth%1:22:00:: (growth.n.01) - (biology) the process of an individual organism growing
    organically; a purely biological unfolding of events involved in an organism changing gradually
    from a simple to a more complex level Examples: he proposed an indicator of osseous development
    in children
* **Patrick White (PW)**
  * growth%1:22:00:: (growth.n.01) - (biology) the process of an individual organism growing
    organically; a purely biological unfolding of events involved in an organism changing gradually
    from a simple to a more complex level Examples: he proposed an indicator of osseous development
    in children
* **Penny Hands (PH)**
  * growth%1:22:02:: (increase.n.03) - a process of becoming larger or longer or more numerous or
    more important Examples: the increase in unemployment | the growth of population
  * Comment: Sense 1 refers to the natural biological process whereby, for example, a child becomes
    an adult. Retinal cell growth is abnormal, so I've opted for sense 3.

**Agreement:** Fine: Exactly two agree; Glite: Exactly two agree; Maru2022 fine support: 2/3;
Maru2022 Glite support: 2/3.

### D89. senseval2.d001.s026.t011

**Lemma/POS/source:** `say` / `VERB` / `senseval2` (`senseval2.d001`)

**Sentence:**
`It turns out that studying a tragic but uncommon tumor made possible some fundamental insights about the most basic workings of cancer, `**[says]**
Samuel Broder, director of the National Cancer Institute.

**Maru2022 label**

* say%2:32:15:: (say.v.08) - utter aloud Examples: She said `Hello' to everyone in the office

**Reviewer verdicts**

* **Robert Farren (RF)**
  * say%2:32:13:: (say.v.09) - state as one's opinion or judgement; declare Examples: I say let's
    forget this whole business
* **Patrick White (PW)**
  * say%2:32:00:: (state.v.01) - express in words Examples: He said that he wanted to marry her |
    tell me what is bothering you
  * say%2:32:15:: (say.v.08) - utter aloud Examples: She said `Hello' to everyone in the office
  * Comment: Unclear if reported speech or quote from something written
* **Penny Hands (PH)**
  * say%2:32:00:: (state.v.01) - express in words Examples: He said that he wanted to marry her |
    tell me what is bothering you
  * say%2:32:15:: (say.v.08) - utter aloud Examples: She said `Hello' to everyone in the office
  * Comment: Sense 8 seems to be about direct speech, i.e. a quote + a reporting verb (say). But
    there is no proof that he uttered this statement aloud; it could have been a written statement.
    That's why I also selected sense 1.

**Agreement:** Fine: Exactly two agree; Glite: All three agree; Maru2022 fine support: 0/3; Maru2022
Glite support: 3/3.

### D90. senseval2.d001.s031.t006

**Lemma/POS/source:** `same` / `ADJ` / `senseval2` (`senseval2.d001`)

**Sentence:** Soon after that report, two other research teams uncovered evidence that the
**[same]** damaged p53 gene is present in tissue from lung and breast cancers.

**Maru2022 label**

* same%3:00:00:: (same.a.02) - closely similar or comparable in kind or quality or quantity or
  degree Examples: curtains the same color as the walls | two girls of the same age

**Reviewer verdicts**

* **Robert Farren (RF)**
  * same%3:00:00:: (same.a.02) - closely similar or comparable in kind or quality or quantity or
    degree Examples: curtains the same color as the walls | two girls of the same age
* **Patrick White (PW)**
  * same%3:00:02:: (same.a.01) - same in identity Examples: the same man I saw yesterday | never
    wore the same dress twice
* **Penny Hands (PH)**
  * same%3:00:00:: (same.a.02) - closely similar or comparable in kind or quality or quantity or
    degree Examples: curtains the same color as the walls | two girls of the same age

**Agreement:** Fine: Exactly two agree; Glite: Exactly two agree; Maru2022 fine support: 2/3;
Maru2022 Glite support: 2/3.

### D91. senseval2.d001.s035.t007

**Lemma/POS/source:** `development` / `NOUN` / `senseval2` (`senseval2.d001`)

**Sentence:** Researchers say the inactivation of tumor-suppressor genes, alone or in combination,
appears crucial to the **[development]** of such scourges as cancer of the brain, the skin, kidney,
prostate, and cervix.

**Maru2022 label**

* development%1:22:01:: (growth.n.01) - (biology) the process of an individual organism growing
  organically; a purely biological unfolding of events involved in an organism changing gradually
  from a simple to a more complex level Examples: he proposed an indicator of osseous development in
  children

**Reviewer verdicts**

* **Robert Farren (RF)**
  * development%1:22:02:: (development.n.02) - a process in which something passes by degrees to a
    different stage (especially a more advanced or mature stage) Examples: the development of his
    ideas took many years | the evolution of Greek civilization
* **Patrick White (PW)**
  * development%1:22:01:: (growth.n.01) - (biology) the process of an individual organism growing
    organically; a purely biological unfolding of events involved in an organism changing gradually
    from a simple to a more complex level Examples: he proposed an indicator of osseous development
    in children
* **Penny Hands (PH)**
  * development%1:22:02:: (development.n.02) - a process in which something passes by degrees to a
    different stage (especially a more advanced or mature stage) Examples: the development of his
    ideas took many years | the evolution of Greek civilization
  * Comment: Sense 3 seems to be more about natural development, e.g. as a children becomes an
    adult.

**Agreement:** Fine: Exactly two agree; Glite: Exactly two agree; Maru2022 fine support: 1/3;
Maru2022 Glite support: 1/3.

### D92. senseval2.d001.s049.t012

**Lemma/POS/source:** `first` / `ADJ` / `senseval2` (`senseval2.d001`)

**Sentence:** By analyzing cells extracted from eye tumors, they found defects in the second copy of
chromosome 13 in the exact area as in the **[first]** copy of the chromosome.

**Maru2022 label**

* first%3:00:00:: (first.a.01) - preceding all others in time or space or degree Examples: the first
  house on the right | the first day of spring

**Reviewer verdicts**

* **Robert Farren (RF)**
  * first%3:00:00:: (first.a.01) - preceding all others in time or space or degree Examples: the
    first house on the right | the first day of spring
* **Patrick White (PW)**
  * first%5:00:00:ordinal:00 (first.s.01) - indicating the beginning unit in a series
* **Penny Hands (PH)**
  * first%5:00:00:ordinal:00 (first.s.01) - indicating the beginning unit in a series

**Agreement:** Fine: Exactly two agree; Glite: Exactly two agree; Maru2022 fine support: 1/3;
Maru2022 Glite support: 1/3.

### D93. senseval2.d001.s051.t003

**Lemma/POS/source:** `loss` / `NOUN` / `senseval2` (`senseval2.d001`)

**Sentence:** It was the first time anyone had showed that the **[loss]** of both copies of the same
gene could lead to the eruption of a cancer.

**Maru2022 label**

* loss%1:07:00:: (loss.n.04) - the disadvantage that results from losing something Examples: his
  loss of credibility led to his resignation | losing him is no great deprivation
* loss%1:21:01:: (loss.n.01) - something that is lost Examples: the car was a total loss | loss of
  livestock left the rancher bankrupt

**Reviewer verdicts**

* **Robert Farren (RF)**
  * loss%1:04:00:: (loss.n.03) - the act of losing someone or something Examples: everyone expected
    him to win so his loss was a shock
* **Patrick White (PW)**
  * loss%1:04:00:: (loss.n.03) - the act of losing someone or something Examples: everyone expected
    him to win so his loss was a shock
* **Penny Hands (PH)**
  * loss%1:21:01:: (loss.n.01) - something that is lost Examples: the car was a total loss | loss of
    livestock left the rancher bankrupt
  * Comment: The second example in sense 1 mirrors the example in the text. I rejected sense 3
    because it's not the act of losing both copies of the gene that leads to the eruption of a
    cancer, and sense 4 because it's not the disadvantage that results in the eruption of the
    cancer.

**Agreement:** Fine: Exactly two agree; Glite: Exactly two agree; Maru2022 fine support: 0/3;
Maru2022 Glite support: 0/3.

### D94. senseval2.d001.s052.t002

**Lemma/POS/source:** `say` / `VERB` / `senseval2` (`senseval2.d001`)

**Sentence:** `It was extraordinarily satisfying, `**[says]** Dr. Knudson, now at Fox Chase Cancer
Research Center in Philadelphia.

**Maru2022 label**

* say%2:32:15:: (say.v.08) - utter aloud Examples: She said `Hello' to everyone in the office

**Reviewer verdicts**

* **Robert Farren (RF)**
  * say%2:32:15:: (say.v.08) - utter aloud Examples: She said `Hello' to everyone in the office
* **Patrick White (PW)**
  * say%2:32:00:: (state.v.01) - express in words Examples: He said that he wanted to marry her |
    tell me what is bothering you
  * say%2:32:15:: (say.v.08) - utter aloud Examples: She said `Hello' to everyone in the office
  * Comment: Unclear if reported speech or quote from something written
* **Penny Hands (PH)**
  * say%2:32:00:: (state.v.01) - express in words Examples: He said that he wanted to marry her |
    tell me what is bothering you
  * say%2:32:15:: (say.v.08) - utter aloud Examples: She said `Hello' to everyone in the office
  * Comment: Sense 8 seems to be about direct speech, i.e. a quote + a reporting verb (say). But
    there is no proof that he uttered this statement aloud; it could have been a written statement.
    That's why I also selected sense 1.

**Agreement:** Fine: Exactly two agree; Glite: All three agree; Maru2022 fine support: 1/3; Maru2022
Glite support: 3/3.

### D95. senseval2.d001.s055.t003

**Lemma/POS/source:** `believe` / `VERB` / `senseval2` (`senseval2.d001`)

**Sentence:** But in Baltimore, Dr. Vogelstein, a young molecular biologist at Johns Hopkins Medical
School, **[believed]** Dr. Knudson was right, and set out to repeat the Cavenee experiment in cells
from other cancers.

**Maru2022 label**

* believe%2:31:03:: (believe.v.03) - be confident about something Examples: I believe that he will
  come back from the war

**Reviewer verdicts**

* **Robert Farren (RF)**
  * believe%2:31:04:: (think.v.01) - judge or regard; look upon; judge Examples: I think he is very
    smart | I believe her to be very smart
* **Patrick White (PW)**
  * believe%2:31:03:: (believe.v.03) - be confident about something Examples: I believe that he will
    come back from the war
* **Penny Hands (PH)**
  * believe%2:31:04:: (think.v.01) - judge or regard; look upon; judge Examples: I think he is very
    smart | I believe her to be very smart
  * Comment: I rejected sense 1 because that seems to be more about being sure that someone is not
    lying (and the examples show a direct object: 'believe someone or something'. Sense 3 is
    tempting, but I think that is more about believing that things will work out, like trusting in
    fate. Sense 3 is substitutable: I believe he's right = I think he's right / I judge him to be
    right.

**Agreement:** Fine: Exactly two agree; Glite: All three agree; Maru2022 fine support: 1/3; Maru2022
Glite support: 3/3.

### D96. senseval2.d001.s056.t005

**Lemma/POS/source:** `loss` / `NOUN` / `senseval2` (`senseval2.d001`)

**Sentence:** His was one of two research teams in 1984 to report dual chromosome **[losses]** for a
rare childhood cancer of the kidney called Wilm's tumor.

**Maru2022 label**

* loss%1:07:00:: (loss.n.04) - the disadvantage that results from losing something Examples: his
  loss of credibility led to his resignation | losing him is no great deprivation
* loss%1:21:01:: (loss.n.01) - something that is lost Examples: the car was a total loss | loss of
  livestock left the rancher bankrupt

**Reviewer verdicts**

* **Robert Farren (RF)**
  * loss%1:04:00:: (loss.n.03) - the act of losing someone or something Examples: everyone expected
    him to win so his loss was a shock
* **Patrick White (PW)**
  * loss%1:04:00:: (loss.n.03) - the act of losing someone or something Examples: everyone expected
    him to win so his loss was a shock
* **Penny Hands (PH)**
  * loss%1:21:01:: (loss.n.01) - something that is lost Examples: the car was a total loss | loss of
    livestock left the rancher bankrupt

**Agreement:** Fine: Exactly two agree; Glite: Exactly two agree; Maru2022 fine support: 0/3;
Maru2022 Glite support: 0/3.

### D97. senseval2.d001.s060.t010

**Lemma/POS/source:** `sign` / `NOUN` / `senseval2` (`senseval2.d001`)

**Sentence:** Dr. Vogelstein and a doctoral student, Eric Fearon, began months of tedious and often
frustrating probing of the chromosomes searching for **[signs]** of genetic damage.

**Maru2022 label**

* sign%1:26:00:: (sign.n.06) - (medicine) any objective evidence of the presence of a disorder or
  disease Examples: there were no signs of asphyxiation

**Reviewer verdicts**

* **Robert Farren (RF)**
  * sign%1:26:00:: (sign.n.06) - (medicine) any objective evidence of the presence of a disorder or
    disease Examples: there were no signs of asphyxiation
* **Patrick White (PW)**
  * sign%1:10:05:: (sign.n.01) - a perceptible indication of something not immediately apparent (as
    a visible clue that something has happened) Examples: he showed signs of strain | they welcomed
    the signs of spring
* **Penny Hands (PH)**
  * sign%1:26:00:: (sign.n.06) - (medicine) any objective evidence of the presence of a disorder or
    disease Examples: there were no signs of asphyxiation
  * Comment: I'm concerned that sense 6 is referring to the language used by doctors when diagnosing
    a patient, rather than researchers discussing findings. My question is, does gene damage
    constitute a disorder? Whether it is a disorder or not, I've gone for sense 6 because I think
    it's close enough to be acceptable. If not, I would opt for the more general, but accurate,
    sense 1.

**Agreement:** Fine: Exactly two agree; Glite: Exactly two agree; Maru2022 fine support: 2/3;
Maru2022 Glite support: 2/3.

### D98. senseval2.d001.s062.t002

**Lemma/POS/source:** `picture` / `NOUN` / `senseval2` (`senseval2.d001`)

**Sentence:** Gradually, a coherent **[picture]** of cancer development emerged.

**Maru2022 label**

* picture%1:26:00:: (picture.n.04) - a situation treated as an observable object Examples: the
  political picture is favorable | the religious scene in England has changed in the last century

**Reviewer verdicts**

* **Robert Farren (RF)**
  * Cannot answer: no sense applies
  * Note: This is a figurative sense of "picture" which implies no visual or pictorial element
    whatsoever. It suggests "a comprehensive overview, description, explanation or understanding" of
    some event or situation or process.
* **Patrick White (PW)**
  * picture%1:26:00:: (picture.n.04) - a situation treated as an observable object Examples: the
    political picture is favorable | the religious scene in England has changed in the last century
* **Penny Hands (PH)**
  * picture%1:26:00:: (picture.n.04) - a situation treated as an observable object Examples: the
    political picture is favorable | the religious scene in England has changed in the last century
  * Comment: Sense 3 seems to refer more to a subjective image in someone's mind.

**Agreement:** Fine: Exactly two agree; Glite: Exactly two agree; Maru2022 fine support: 2/3;
Maru2022 Glite support: 2/3.

### D99. senseval2.d001.s067.t004

**Lemma/POS/source:** `loss` / `NOUN` / `senseval2` (`senseval2.d001`)

**Sentence:**
`It was the confirming evidence we all needed that gene **[losses]** were critical to the development of a common tumor, `says
Ray White at Howard Hughes Medical Institute in Salt Lake City.

**Maru2022 label**

* loss%1:07:00:: (loss.n.04) - the disadvantage that results from losing something Examples: his
  loss of credibility led to his resignation | losing him is no great deprivation
* loss%1:21:01:: (loss.n.01) - something that is lost Examples: the car was a total loss | loss of
  livestock left the rancher bankrupt

**Reviewer verdicts**

* **Robert Farren (RF)**
  * loss%1:04:00:: (loss.n.03) - the act of losing someone or something Examples: everyone expected
    him to win so his loss was a shock
* **Patrick White (PW)**
  * loss%1:04:00:: (loss.n.03) - the act of losing someone or something Examples: everyone expected
    him to win so his loss was a shock
* **Penny Hands (PH)**
  * loss%1:21:01:: (loss.n.01) - something that is lost Examples: the car was a total loss | loss of
    livestock left the rancher bankrupt
  * Comment: The plural form 'losses' suggests sense 1 – a thing that is lost rather than an act or
    process. It equates to the use demonstrated in the second example: 'loss of livestock', which
    could be rephrased as 'livestock losses'.

**Agreement:** Fine: Exactly two agree; Glite: Exactly two agree; Maru2022 fine support: 0/3;
Maru2022 Glite support: 0/3.

### D100. senseval2.d001.s067.t009

**Lemma/POS/source:** `say` / `VERB` / `senseval2` (`senseval2.d001`)

**Sentence:**
`It was the confirming evidence we all needed that gene losses were critical to the development of a common tumor, `**[says]**
Ray White at Howard Hughes Medical Institute in Salt Lake City.

**Maru2022 label**

* say%2:32:15:: (say.v.08) - utter aloud Examples: She said `Hello' to everyone in the office

**Reviewer verdicts**

* **Robert Farren (RF)**
  * say%2:32:13:: (say.v.09) - state as one's opinion or judgement; declare Examples: I say let's
    forget this whole business
* **Patrick White (PW)**
  * say%2:32:00:: (state.v.01) - express in words Examples: He said that he wanted to marry her |
    tell me what is bothering you
  * say%2:32:15:: (say.v.08) - utter aloud Examples: She said `Hello' to everyone in the office
  * Comment: Unclear if reported speech or quote from something written
* **Penny Hands (PH)**
  * say%2:32:00:: (state.v.01) - express in words Examples: He said that he wanted to marry her |
    tell me what is bothering you
  * say%2:32:15:: (say.v.08) - utter aloud Examples: She said `Hello' to everyone in the office
  * Comment: Sense 8 seems to be about direct speech, i.e. a quote + a reporting verb (say). But
    there is no proof that he uttered this statement aloud; it could have been a written statement.
    That's why I also selected sense 1.

**Agreement:** Fine: Exactly two agree; Glite: All three agree; Maru2022 fine support: 0/3; Maru2022
Glite support: 3/3.

### D101. senseval2.d001.s072.t000

**Lemma/POS/source:** `find` / `VERB` / `senseval2` (`senseval2.d001`)

**Sentence:** When they **[found]** it last winter, Dr. Vogelstein was dubious that the search was
over.

**Maru2022 label**

* find%2:31:09:: (discover.v.04) - make a discovery Examples: She found that he had lied to her |
  The story is false, so far as I can discover
* find%2:32:00:: (determine.v.01) - establish after a calculation, investigation, experiment,
  survey, or study Examples: find the product of two numbers | The physicist who found the elusive
  particle won the Nobel Prize
* find%2:36:00:: (discover.v.03) - make a discovery, make a new finding Examples: Roentgen
  discovered X-rays | Physicists believe they found a new elementary particle
* find%2:39:02:: (detect.v.01) - discover or determine the existence, presence, or fact of Examples:
  She detected high levels of lead in her drinking water | We found traces of lead in the paint

**Reviewer verdicts**

* **Robert Farren (RF)**
  * find%2:39:02:: (detect.v.01) - discover or determine the existence, presence, or fact of
    Examples: She detected high levels of lead in her drinking water | We found traces of lead in
    the paint
* **Patrick White (PW)**
  * find%2:32:00:: (determine.v.01) - establish after a calculation, investigation, experiment,
    survey, or study Examples: find the product of two numbers | The physicist who found the elusive
    particle won the Nobel Prize
* **Penny Hands (PH)**
  * find%2:39:02:: (detect.v.01) - discover or determine the existence, presence, or fact of
    Examples: She detected high levels of lead in her drinking water | We found traces of lead in
    the paint

**Agreement:** Fine: Exactly two agree; Glite: All three agree; Maru2022 fine support: 0/3; Maru2022
Glite support: 0/3.

### D102. senseval2.d001.s073.t000

**Lemma/POS/source:** `doubt` / `NOUN` / `senseval2` (`senseval2.d001`)

**Sentence:** His **[doubts]** stemmed from the fact that several years earlier a Princeton
University researcher, Arnold Levine, had found in experiments with mice that a gene called p53
could transform normal cells into cancerous ones.

**Maru2022 label**

* doubt%1:07:00:: (doubt.n.02) - uncertainty about the truth or factuality or existence of something
  Examples: the dubiousness of his claim | there is no question about the validity of the enterprise

**Reviewer verdicts**

* **Robert Farren (RF)**
  * doubt%1:07:00:: (doubt.n.02) - uncertainty about the truth or factuality or existence of
    something Examples: the dubiousness of his claim | there is no question about the validity of
    the enterprise
* **Patrick White (PW)**
  * doubt%1:07:00:: (doubt.n.02) - uncertainty about the truth or factuality or existence of
    something Examples: the dubiousness of his claim | there is no question about the validity of
    the enterprise
* **Penny Hands (PH)**
  * Cannot answer: inventory inadequate
  * Note: Neither of the senses seem to cover the countable sense of 'doubt' that is demonstrated in
    the text – a *feeling* of uncertainty about something.

**Agreement:** Fine: Exactly two agree; Glite: Exactly two agree; Maru2022 fine support: 2/3;
Maru2022 Glite support: 2/3.

### D103. senseval2.d001.s074.t002

**Lemma/POS/source:** `same` / `ADJ` / `senseval2` (`senseval2.d001`)

**Sentence:** The deletion Dr. Vogelstein found was in exactly the **[same]** spot as p53.

**Maru2022 label**

* same%3:00:00:: (same.a.02) - closely similar or comparable in kind or quality or quantity or
  degree Examples: curtains the same color as the walls | two girls of the same age

**Reviewer verdicts**

* **Robert Farren (RF)**
  * same%3:00:00:: (same.a.02) - closely similar or comparable in kind or quality or quantity or
    degree Examples: curtains the same color as the walls | two girls of the same age
* **Patrick White (PW)**
  * same%3:00:02:: (same.a.01) - same in identity Examples: the same man I saw yesterday | never
    wore the same dress twice
* **Penny Hands (PH)**
  * same%3:00:00:: (same.a.02) - closely similar or comparable in kind or quality or quantity or
    degree Examples: curtains the same color as the walls | two girls of the same age
  * Comment: The use of the word 'exactly the same' initially suggests sense 1, but the author is
    talking about the *equivalent* spot in a different organism, so I've opted for sense 2. Dr
    Vogelstein's finding was in a spot that was *comparable in kind* to the spot where Arnold Levine
    found it. It wasn't the very same one because they were working with different materials.

**Agreement:** Fine: Exactly two agree; Glite: Exactly two agree; Maru2022 fine support: 2/3;
Maru2022 Glite support: 2/3.

### D104. senseval2.d001.s075.t005

**Lemma/POS/source:** `growth` / `NOUN` / `senseval2` (`senseval2.d001`)

**Sentence:** But Mr. Levine had said the p53 gene caused cancer by promoting **[growth]**, whereas
the Johns Hopkins scientists were looking for a gene that suppressed growth.

**Maru2022 label**

* growth%1:22:00:: (growth.n.01) - (biology) the process of an individual organism growing
  organically; a purely biological unfolding of events involved in an organism changing gradually
  from a simple to a more complex level Examples: he proposed an indicator of osseous development in
  children
* growth%1:26:00:: (growth.n.06) - (pathology) an abnormal proliferation of tissue (as in a tumor)

**Reviewer verdicts**

* **Robert Farren (RF)**
  * growth%1:22:00:: (growth.n.01) - (biology) the process of an individual organism growing
    organically; a purely biological unfolding of events involved in an organism changing gradually
    from a simple to a more complex level Examples: he proposed an indicator of osseous development
    in children
* **Patrick White (PW)**
  * growth%1:22:02:: (increase.n.03) - a process of becoming larger or longer or more numerous or
    more important Examples: the increase in unemployment | the growth of population
* **Penny Hands (PH)**
  * growth%1:22:02:: (increase.n.03) - a process of becoming larger or longer or more numerous or
    more important Examples: the increase in unemployment | the growth of population

**Agreement:** Fine: Exactly two agree; Glite: Exactly two agree; Maru2022 fine support: 0/3;
Maru2022 Glite support: 0/3.

### D105. senseval2.d001.s075.t010

**Lemma/POS/source:** `growth` / `NOUN` / `senseval2` (`senseval2.d001`)

**Sentence:** But Mr. Levine had said the p53 gene caused cancer by promoting growth, whereas the
Johns Hopkins scientists were looking for a gene that suppressed **[growth]**.

**Maru2022 label**

* growth%1:22:00:: (growth.n.01) - (biology) the process of an individual organism growing
  organically; a purely biological unfolding of events involved in an organism changing gradually
  from a simple to a more complex level Examples: he proposed an indicator of osseous development in
  children
* growth%1:26:00:: (growth.n.06) - (pathology) an abnormal proliferation of tissue (as in a tumor)

**Reviewer verdicts**

* **Robert Farren (RF)**
  * growth%1:22:00:: (growth.n.01) - (biology) the process of an individual organism growing
    organically; a purely biological unfolding of events involved in an organism changing gradually
    from a simple to a more complex level Examples: he proposed an indicator of osseous development
    in children
* **Patrick White (PW)**
  * growth%1:22:02:: (increase.n.03) - a process of becoming larger or longer or more numerous or
    more important Examples: the increase in unemployment | the growth of population
* **Penny Hands (PH)**
  * growth%1:22:02:: (increase.n.03) - a process of becoming larger or longer or more numerous or
    more important Examples: the increase in unemployment | the growth of population

**Agreement:** Fine: Exactly two agree; Glite: Exactly two agree; Maru2022 fine support: 0/3;
Maru2022 Glite support: 0/3.

### D106. senseval2.d001.s076.t014

**Lemma/POS/source:** `observe` / `VERB` / `senseval2` (`senseval2.d001`)

**Sentence:** Despite that, when the Johns Hopkins scientists compared the gene they had found in
the human cancer cells with the Mr. Levine's p53 gene they found the two were identical; it turned
out that in Mr. Levine's cancer studies, he had unknowingly been **[observing]** a damaged form of
p53 -- a cancer-suppressing gene.

**Maru2022 label**

* observe%2:39:01:: (note.v.03) - observe with care or pay close attention to Examples: Take note of
  this chemical reaction

**Reviewer verdicts**

* **Robert Farren (RF)**
  * observe%2:39:00:: (observe.v.04) - watch attentively Examples: Please observe the reaction of
    these two chemicals
* **Patrick White (PW)**
  * observe%2:39:01:: (note.v.03) - observe with care or pay close attention to Examples: Take note
    of this chemical reaction
* **Penny Hands (PH)**
  * observe%2:39:00:: (observe.v.04) - watch attentively Examples: Please observe the reaction of
    these two chemicals
  * Comment: I went by the examples as the definitions for senses 3 and 4 mean pretty much the same.

**Agreement:** Fine: Exactly two agree; Glite: All three agree; Maru2022 fine support: 1/3; Maru2022
Glite support: 3/3.

### D107. senseval2.d001.s077.t008

**Lemma/POS/source:** `say` / `VERB` / `senseval2` (`senseval2.d001`)

**Sentence:** The discovery
`suddenly puts an obscure gene right in the cockpit of cancer formation, `**[says]** Robert
Weinberg, a leader in cancer-gene research at Whitehead Institute in Cambridge, Mass.

**Maru2022 label**

* say%2:32:15:: (say.v.08) - utter aloud Examples: She said `Hello' to everyone in the office

**Reviewer verdicts**

* **Robert Farren (RF)**
  * say%2:32:13:: (say.v.09) - state as one's opinion or judgement; declare Examples: I say let's
    forget this whole business
* **Patrick White (PW)**
  * say%2:32:00:: (state.v.01) - express in words Examples: He said that he wanted to marry her |
    tell me what is bothering you
  * say%2:32:15:: (say.v.08) - utter aloud Examples: She said `Hello' to everyone in the office
  * Comment: Unclear if reported speech or quote from something written
* **Penny Hands (PH)**
  * say%2:32:00:: (state.v.01) - express in words Examples: He said that he wanted to marry her |
    tell me what is bothering you
  * say%2:32:15:: (say.v.08) - utter aloud Examples: She said `Hello' to everyone in the office
  * Comment: Sense 8 seems to be about direct speech, i.e. a quote + a reporting verb (say). But
    there is no proof that he uttered this statement aloud; it could have been a written statement.
    That's why I also selected sense 1.

**Agreement:** Fine: Exactly two agree; Glite: All three agree; Maru2022 fine support: 0/3; Maru2022
Glite support: 3/3.

### D108. senseval2.d001.s081.t002

**Lemma/POS/source:** `implicate` / `VERB` / `senseval2` (`senseval2.d001`)

**Sentence:** The p53 gene has just been **[implicated]** in lung cancer.

**Maru2022 label**

* implicate%2:42:00:: (entail.v.02) - impose, involve, or imply as a necessary accompaniment or
  result Examples: What does this move entail?

**Reviewer verdicts**

* **Robert Farren (RF)**
  * implicate%2:42:01:: (implicate.v.01) - bring into intimate and incriminating connection
    Examples: He is implicated in the scheme to defraud the government
* **Patrick White (PW)**
  * implicate%2:42:01:: (implicate.v.01) - bring into intimate and incriminating connection
    Examples: He is implicated in the scheme to defraud the government
* **Penny Hands (PH)**
  * implicate%2:42:00:: (entail.v.02) - impose, involve, or imply as a necessary accompaniment or
    result Examples: What does this move entail?
  * Comment: There is a hint of sense 1 in the author's use of 'implicate' because of the negative
    nature of lung cancer; we might see the p53 gene as the 'baddie' here.

**Agreement:** Fine: Exactly two agree; Glite: Exactly two agree; Maru2022 fine support: 1/3;
Maru2022 Glite support: 1/3.

### D109. senseval2.d001.s087.t000

**Lemma/POS/source:** `believe` / `VERB` / `senseval2` (`senseval2.d001`)

**Sentence:** Dr. Minna **[believes]** people who inherit a defective gene somewhere on one of their
two copies of chromosome 3 are especially prone to lung cancer.

**Maru2022 label**

* believe%2:31:03:: (believe.v.03) - be confident about something Examples: I believe that he will
  come back from the war

**Reviewer verdicts**

* **Robert Farren (RF)**
  * Cannot answer: no sense applies
  * Note: This sense of "believe", in a context involving researchers, can be described as "consider
    that a hypothesis not yet proven to be true, is probably true". This is distinct from sense 1
    because it's specific to scientific hypotheses.
* **Patrick White (PW)**
  * believe%2:31:04:: (think.v.01) - judge or regard; look upon; judge Examples: I think he is very
    smart | I believe her to be very smart
* **Penny Hands (PH)**
  * believe%2:31:04:: (think.v.01) - judge or regard; look upon; judge Examples: I think he is very
    smart | I believe her to be very smart
  * Comment: As mentioned before, I think sense 3 relates to believing in fate, or believing that
    things will somehow work out.

**Agreement:** Fine: Exactly two agree; Glite: Exactly two agree; Maru2022 fine support: 0/3;
Maru2022 Glite support: 2/3.

### D110. senseval2.d001.s090.t010

**Lemma/POS/source:** `discovery` / `NOUN` / `senseval2` (`senseval2.d001`)

**Sentence:** Already two major pharmaceutical companies, the Squibb unit of Bristol-Myers Squibb
Co. and Hoffmann-La Roche Inc., are collaborating with gene hunters to turn the anticipated cascade
of **[discoveries]** into predictive tests and, maybe, new therapies.

**Maru2022 label**

* discovery%1:04:00:: (discovery.n.01) - the act of discovering something

**Reviewer verdicts**

* **Robert Farren (RF)**
  * discovery%1:09:00:: (discovery.n.03) - a productive insight
* **Patrick White (PW)**
  * discovery%1:10:00:: (discovery.n.02) - something that is discovered
* **Penny Hands (PH)**
  * discovery%1:10:00:: (discovery.n.02) - something that is discovered
  * Comment: I think the emphasis in the text is on *what* scientists will find rather than the act
    or process of finding. (In addition, pharmaceutical companies can't turn *the act of discovery*
    into predictive tests.) Sense 3 refers to 'insights', whereas here, scientists are referring to
    hunting for and finding specific genes.

**Agreement:** Fine: Exactly two agree; Glite: Exactly two agree; Maru2022 fine support: 0/3;
Maru2022 Glite support: 1/3.

### D111. senseval2.d001.s094.t001

**Lemma/POS/source:** `say` / `VERB` / `senseval2` (`senseval2.d001`)

**Sentence:** In any case, **[says]** Dr. Minna of the National Cancer Institute, ``We 're
witnessing the discovery of one of the most important steps in the genesis of cancer.

**Maru2022 label**

* say%2:32:15:: (say.v.08) - utter aloud Examples: She said `Hello' to everyone in the office

**Reviewer verdicts**

* **Robert Farren (RF)**
  * say%2:32:13:: (say.v.09) - state as one's opinion or judgement; declare Examples: I say let's
    forget this whole business
* **Patrick White (PW)**
  * say%2:32:00:: (state.v.01) - express in words Examples: He said that he wanted to marry her |
    tell me what is bothering you
  * say%2:32:15:: (say.v.08) - utter aloud Examples: She said `Hello' to everyone in the office
  * Comment: Unclear if reported speech or quote from something written
* **Penny Hands (PH)**
  * say%2:32:00:: (state.v.01) - express in words Examples: He said that he wanted to marry her |
    tell me what is bothering you
  * say%2:32:15:: (say.v.08) - utter aloud Examples: She said `Hello' to everyone in the office
  * Comment: Sense 8 seems to be about direct speech, i.e. a quote + a reporting verb (say). But
    there is no proof that he uttered this statement aloud; it could have been a written statement.
    That's why I also selected sense 1.

**Agreement:** Fine: Exactly two agree; Glite: All three agree; Maru2022 fine support: 0/3; Maru2022
Glite support: 3/3.

### D112. senseval2.d002.s000.t001

**Lemma/POS/source:** `child` / `NOUN` / `senseval2` (`senseval2.d002`)

**Sentence:** Why ca not we teach our **[children]** to read, write and reckon?

**Maru2022 label**

* child%1:18:01:: (child.n.02) - a human offspring (son or daughter) of any age Examples: they had
  three children | they were able to send their kids to college

**Reviewer verdicts**

* **Robert Farren (RF)**
  * child%1:18:00:: (child.n.01) - a young person of either sex Examples: she writes books for
    children | they're just kids
* **Patrick White (PW)**
  * child%1:18:00:: (child.n.01) - a young person of either sex Examples: she writes books for
    children | they're just kids
* **Penny Hands (PH)**
  * child%1:18:01:: (child.n.02) - a human offspring (son or daughter) of any age Examples: they had
    three children | they were able to send their kids to college
  * Comment: I'm presuming the text is talking about parents teaching their own children because as
    a society, we can and do teach our children to read, write, and reckon.

**Agreement:** Fine: Exactly two agree; Glite: All three agree; Maru2022 fine support: 1/3; Maru2022
Glite support: 3/3.

### D113. senseval2.d002.s003.t004

**Lemma/POS/source:** `require` / `VERB` / `senseval2` (`senseval2.d002`)

**Sentence:** And the reason we do not want to is that effective education would **[require]** us to
relinquish some cherished metaphysical beliefs about human nature in general and the human nature of
young people in particular, well as to violate some cherished vested interests.

**Maru2022 label**

* require%2:32:00:: (command.v.02) - make someone do something
* require%2:32:01:: (ask.v.04) - consider obligatory; request and expect Examples: We require our
  secretary to be on time | Aren't we asking too much of these children?

**Reviewer verdicts**

* **Robert Farren (RF)**
  * require%2:42:00:: (necessitate.v.01) - require as useful, just, or proper Examples: It takes
    nerve to do what she did | success usually requires hard work
  * Comment: I've decided to choose sense 1, though with reservations, because the example sentences
    fit but the definition doesn't. This is a particular sense of "require" that is always
    impersonal: there's no sentient being that "would require us to relinquish", etc, in the above
    sentence. The sense is close to "necessitate".
* **Patrick White (PW)**
  * require%2:32:01:: (ask.v.04) - consider obligatory; request and expect Examples: We require our
    secretary to be on time | Aren't we asking too much of these children?
* **Penny Hands (PH)**
  * require%2:42:00:: (necessitate.v.01) - require as useful, just, or proper Examples: It takes
    nerve to do what she did | success usually requires hard work

**Agreement:** Fine: Exactly two agree; Glite: All three agree; Maru2022 fine support: 0/3; Maru2022
Glite support: 3/3.

### D114. senseval2.d002.s003.t016

**Lemma/POS/source:** `violate` / `VERB` / `senseval2` (`senseval2.d002`)

**Sentence:** And the reason we do not want to is that effective education would require us to
relinquish some cherished metaphysical beliefs about human nature in general and the human nature of
young people in particular, well as to **[violate]** some cherished vested interests.

**Maru2022 label**

* violate%2:42:00:: (violate.v.01) - fail to agree with; be in violation of; as of rules or patterns
  Examples: This sentence violates the rules of syntax

**Reviewer verdicts**

* **Robert Farren (RF)**
  * violate%2:42:00:: (violate.v.01) - fail to agree with; be in violation of; as of rules or
    patterns Examples: This sentence violates the rules of syntax
* **Patrick White (PW)**
  * violate%2:41:00:: (transgress.v.01) - act in disregard of laws, rules, contracts, or promises
    Examples: offend all laws of humanity | violate the basic laws or human civilization
  * Comment: A tentative assignment of sense as this collocation is not a typical one.
* **Penny Hands (PH)**
  * violate%2:41:00:: (transgress.v.01) - act in disregard of laws, rules, contracts, or promises
    Examples: offend all laws of humanity | violate the basic laws or human civilization
  * Comment: To 'violate vested interests' means to disregard or undermine them. I think 'laws,
    contracts or promises' are similar to vested interests, so have opted for sense 2.

**Agreement:** Fine: Exactly two agree; Glite: All three agree; Maru2022 fine support: 1/3; Maru2022
Glite support: 3/3.

### D115. senseval2.d002.s011.t021

**Lemma/POS/source:** `child` / `NOUN` / `senseval2` (`senseval2.d002`)

**Sentence:** The whole notion of `creativity `in education was (and is) part and parcel of a
romantic rebellion against disciplined instruction, which was (and is) regarded as
`authoritarian, `a repression and frustration of the latent talents and the wonderful, if as yet
undefined, potentialities inherent in the souls of all our **[children]**.

**Maru2022 label**

* child%1:18:01:: (child.n.02) - a human offspring (son or daughter) of any age Examples: they had
  three children | they were able to send their kids to college

**Reviewer verdicts**

* **Robert Farren (RF)**
  * child%1:18:00:: (child.n.01) - a young person of either sex Examples: she writes books for
    children | they're just kids
* **Patrick White (PW)**
  * child%1:18:00:: (child.n.01) - a young person of either sex Examples: she writes books for
    children | they're just kids
* **Penny Hands (PH)**
  * child%1:18:00:: (child.n.01) - a young person of either sex Examples: she writes books for
    children | they're just kids
  * child%1:18:01:: (child.n.02) - a human offspring (son or daughter) of any age Examples: they had
    three children | they were able to send their kids to college
  * Comment: It's not clear this time whether the author is talking about our offspring or all the
    young people in a society.

**Agreement:** Fine: Exactly two agree; Glite: All three agree; Maru2022 fine support: 0/3; Maru2022
Glite support: 3/3.

### D116. senseval2.d002.s013.t007

**Lemma/POS/source:** `education` / `NOUN` / `senseval2` (`senseval2.d002`)

**Sentence:** Fortunately, these same parents do want their children to get a decent **[education]**
as traditionally understood, and they have enough common sense to know what that demands.

**Maru2022 label**

* education%1:09:00:: (education.n.02) - knowledge acquired by learning and instruction Examples: it
  was clear that he had a very broad education

**Reviewer verdicts**

* **Robert Farren (RF)**
  * education%1:09:00:: (education.n.02) - knowledge acquired by learning and instruction Examples:
    it was clear that he had a very broad education
* **Patrick White (PW)**
  * education%1:04:00:: (education.n.01) - the activities of educating or instructing; activities
    that impart knowledge or skill Examples: he received no formal education | our instruction was
    carefully programmed
* **Penny Hands (PH)**
  * education%1:04:00:: (education.n.01) - the activities of educating or instructing; activities
    that impart knowledge or skill Examples: he received no formal education | our instruction was
    carefully programmed
  * Comment: Sense 2 (not chosen) focuses on the end product, whereas sense 1 (chosen) is more about
    the process of schooling.

**Agreement:** Fine: Exactly two agree; Glite: All three agree; Maru2022 fine support: 1/3; Maru2022
Glite support: 3/3.

### D117. senseval2.d002.s018.t003

**Lemma/POS/source:** `call` / `VERB` / `senseval2` (`senseval2.d002`)

**Sentence:** `Progressive education `(as it was once **[called]**) is far more interesting and
agreeable to teachers than is disciplined instruction.

**Maru2022 label**

* call%2:32:00:: (call.v.02) - ascribe a quality to or give a name of a common noun that reflects a
  quality Examples: He called me a bastard | She called her children lazy and ungrateful

**Reviewer verdicts**

* **Robert Farren (RF)**
  * call%2:32:02:: (name.v.01) - assign a specified (usually proper) proper name to Examples: They
    named their son David | The new school was named after the famous Civil Rights leader
* **Patrick White (PW)**
  * call%2:32:02:: (name.v.01) - assign a specified (usually proper) proper name to Examples: They
    named their son David | The new school was named after the famous Civil Rights leader
* **Penny Hands (PH)**
  * call%2:32:00:: (call.v.02) - ascribe a quality to or give a name of a common noun that reflects
    a quality Examples: He called me a bastard | She called her children lazy and ungrateful

**Agreement:** Fine: Exactly two agree; Glite: All three agree; Maru2022 fine support: 1/3; Maru2022
Glite support: 3/3.

### D118. senseval2.d002.s019.t002

**Lemma/POS/source:** `think` / `VERB` / `senseval2` (`senseval2.d002`)

**Sentence:** It is nice for teachers to **[think]** they are engaged in
`personality development `and even nicer to minimize those irksome tests with often disappointing
results.

**Maru2022 label**

* think%2:31:03:: (think.v.02) - expect, believe, or suppose Examples: I imagine she earned a lot of
  money with her new novel | I thought to find her in a bad state

**Reviewer verdicts**

* **Robert Farren (RF)**
  * think%2:31:03:: (think.v.02) - expect, believe, or suppose Examples: I imagine she earned a lot
    of money with her new novel | I thought to find her in a bad state
* **Patrick White (PW)**
  * think%2:31:03:: (think.v.02) - expect, believe, or suppose Examples: I imagine she earned a lot
    of money with her new novel | I thought to find her in a bad state
* **Penny Hands (PH)**
  * think%2:31:01:: (think.v.01) - judge or regard; look upon; judge Examples: I think he is very
    smart | I believe her to be very smart
  * Comment: Despite having the word 'believe' in its definition, which would appear to be
    substitutable in the text, sense 2 seems to be more about speculating or making a guess.

**Agreement:** Fine: Exactly two agree; Glite: All three agree; Maru2022 fine support: 2/3; Maru2022
Glite support: 3/3.

### D119. senseval2.d002.s033.t000

**Lemma/POS/source:** `problem` / `NOUN` / `senseval2` (`senseval2.d002`)

**Sentence:** Whether they are or are not underpaid is a **[problem]** of equity; it is not an
educational problem.

**Maru2022 label**

* problem%1:09:00:: (trouble.n.01) - a source of difficulty Examples: one trouble after another
  delayed the job | what's the problem?
* problem%1:26:00:: (problem.n.01) - a state of difficulty that needs to be resolved Examples: she
  and her husband are having problems | it is always a job to contact him

**Reviewer verdicts**

* **Robert Farren (RF)**
  * problem%1:26:00:: (problem.n.01) - a state of difficulty that needs to be resolved Examples: she
    and her husband are having problems | it is always a job to contact him
* **Patrick White (PW)**
  * problem%1:26:00:: (problem.n.01) - a state of difficulty that needs to be resolved Examples: she
    and her husband are having problems | it is always a job to contact him
* **Penny Hands (PH)**
  * problem%1:10:00:: (problem.n.02) - a question raised for consideration or solution Examples: our
    homework consisted of ten problems to solve

**Agreement:** Fine: Exactly two agree; Glite: Exactly two agree; Maru2022 fine support: 0/3;
Maru2022 Glite support: 2/3.

### D120. senseval2.d002.s034.t005

**Lemma/POS/source:** `child` / `NOUN` / `senseval2` (`senseval2.d002`)

**Sentence:** It is silly libel on our teachers to think they would educate our **[children]**
better if only they got a few thousand dollars a year more.

**Maru2022 label**

* child%1:18:01:: (child.n.02) - a human offspring (son or daughter) of any age Examples: they had
  three children | they were able to send their kids to college

**Reviewer verdicts**

* **Robert Farren (RF)**
  * child%1:18:00:: (child.n.01) - a young person of either sex Examples: she writes books for
    children | they're just kids
* **Patrick White (PW)**
  * child%1:18:00:: (child.n.01) - a young person of either sex Examples: she writes books for
    children | they're just kids
* **Penny Hands (PH)**
  * child%1:18:00:: (child.n.01) - a young person of either sex Examples: she writes books for
    children | they're just kids
  * child%1:18:01:: (child.n.02) - a human offspring (son or daughter) of any age Examples: they had
    three children | they were able to send their kids to college
  * Comment: Again, it is not clear from the text whether the author is referring to the offspring
    of the parents who are reading the article or young people considered as part of our society.

**Agreement:** Fine: Exactly two agree; Glite: All three agree; Maru2022 fine support: 0/3; Maru2022
Glite support: 3/3.

### D121. senseval2.d002.s037.t003

**Lemma/POS/source:** `thing` / `NOUN` / `senseval2` (`senseval2.d002`)

**Sentence:** But there is not one shred of evidence that, other **[things]** being equal, salary
differentials result in educational differentials.

**Maru2022 label**

* thing%1:09:02:: (matter.n.01) - a vaguely specified concern Examples: several matters to attend to
  | it is none of your affair

**Reviewer verdicts**

* **Robert Farren (RF)**
  * thing%1:07:00:: (thing.n.09) - any attribute or quality considered as having its own existence
    Examples: the thing I like about her is ...
  * Comment: The meaning of "things" in the phrase "other things being equal" is close to "factors"
    or "considerations". None of the senses given above is a good match, but sense 9 seems less
    wrong than the others.
* **Patrick White (PW)**
  * thing%1:09:02:: (matter.n.01) - a vaguely specified concern Examples: several matters to attend
    to | it is none of your affair
* **Penny Hands (PH)**
  * thing%1:09:02:: (matter.n.01) - a vaguely specified concern Examples: several matters to attend
    to | it is none of your affair

**Agreement:** Fine: Exactly two agree; Glite: Exactly two agree; Maru2022 fine support: 2/3;
Maru2022 Glite support: 2/3.

### D122. senseval2.d002.s041.t007

**Lemma/POS/source:** `reform` / `NOUN` / `senseval2` (`senseval2.d002`)

**Sentence:** Conversely, there are the majority of unsuccessful schools, and we know which efforts
at educational **[reform]** are doomed beforehand.

**Maru2022 label**

* reform%1:04:00:: (reform.n.01) - a change for the better as a result of correcting abuses
  Examples: justice was for sale before the reform of the law courts

**Reviewer verdicts**

* **Robert Farren (RF)**
  * reform%1:04:00:: (reform.n.01) - a change for the better as a result of correcting abuses
    Examples: justice was for sale before the reform of the law courts
  * Comment: These senses are not very well formulated. Sense 1 is the most relevant in this case,
    though it's not perfect.
* **Patrick White (PW)**
  * reform%1:04:00:: (reform.n.01) - a change for the better as a result of correcting abuses
    Examples: justice was for sale before the reform of the law courts
* **Penny Hands (PH)**
  * reform%1:04:01:: (reform.n.02) - a campaign aimed to correct abuses or malpractices Examples:
    the reforms he proposed were too radical for the politicians
  * Comment: Sense 2 focuses on the process, which is what the author seems to be talking about.
    Sense 1 is about changes that have already been made. However, there is an argument for
    selecting sense 1: the efforts are being made to attain *changes to the education system* (sense
    1). The question is whether the efforts are directed at *the process* or at *obtaining changes*.
    The difference between the two is very subtle, but I'm opting for sense 2 because the efforts
    being made are ongoing, and changes have not yet come about.

**Agreement:** Fine: Exactly two agree; Glite: All three agree; Maru2022 fine support: 2/3; Maru2022
Glite support: 3/3.

### D123. senseval2.d002.s050.t004

**Lemma/POS/source:** `reform` / `NOUN` / `senseval2` (`senseval2.d002`)

**Sentence:** Let us sum up what we do know about education and about those education **[reforms]**
that do work and do not work: -- `Parental involvement `is a bad idea.

**Maru2022 label**

* reform%1:04:00:: (reform.n.01) - a change for the better as a result of correcting abuses
  Examples: justice was for sale before the reform of the law courts

**Reviewer verdicts**

* **Robert Farren (RF)**
  * reform%1:04:00:: (reform.n.01) - a change for the better as a result of correcting abuses
    Examples: justice was for sale before the reform of the law courts
* **Patrick White (PW)**
  * reform%1:04:01:: (reform.n.02) - a campaign aimed to correct abuses or malpractices Examples:
    the reforms he proposed were too radical for the politicians
* **Penny Hands (PH)**
  * reform%1:04:00:: (reform.n.01) - a change for the better as a result of correcting abuses
    Examples: justice was for sale before the reform of the law courts
  * Comment: In this case, we are discussing reforms that have already been made, and whether they
    have had a positive effect on children's education or not.

**Agreement:** Fine: Exactly two agree; Glite: All three agree; Maru2022 fine support: 2/3; Maru2022
Glite support: 3/3.

### D124. senseval2.d002.s050.t008

**Lemma/POS/source:** `involvement` / `NOUN` / `senseval2` (`senseval2.d002`)

**Sentence:** Let us sum up what we do know about education and about those education reforms that
do work and do not work: -- `Parental **[involvement]** `is a bad idea.

**Maru2022 label**

* involvement%1:26:01:: (participation.n.02) - the condition of sharing in common with others (as
  fellows or partners etc.)

**Reviewer verdicts**

* **Robert Farren (RF)**
  * Cannot answer: no sense applies
  * Note: This sense of "involvement" includes the idea of participating, not only in an activity,
    but also in control or decision-making. It's about sharing power, having a say in how things are
    done, as well as taking an active part in doing them. So it's close to sense 5 above, but more
    specific.
* **Patrick White (PW)**
  * involvement%1:04:00:: (engagement.n.07) - the act of sharing in the activities of a group
    Examples: the teacher tried to increase his students' engagement in class activities
* **Penny Hands (PH)**
  * involvement%1:04:00:: (engagement.n.07) - the act of sharing in the activities of a group
    Examples: the teacher tried to increase his students' engagement in class activities
  * Comment: Sense 1 is more about active participation.

**Agreement:** Fine: Exactly two agree; Glite: Exactly two agree; Maru2022 fine support: 0/3;
Maru2022 Glite support: 2/3.

### D125. senseval2.d002.s058.t007

**Lemma/POS/source:** `city` / `NOUN` / `senseval2` (`senseval2.d002`)

**Sentence:** New York is in the process of trying to disengage itself from a 20-year-old commitment
to this system of school governance, even as Chicago and other **[cities]** are moving to institute
it.

**Maru2022 label**

* city%1:15:00:: (city.n.01) - a large and densely populated urban area; may include several
  independent administrative districts Examples: Ancient Troy was a great city

**Reviewer verdicts**

* **Robert Farren (RF)**
  * city%1:15:01:: (city.n.02) - an incorporated administrative district established by state
    charter Examples: the city raised the tax rate
* **Patrick White (PW)**
  * city%1:15:00:: (city.n.01) - a large and densely populated urban area; may include several
    independent administrative districts Examples: Ancient Troy was a great city
* **Penny Hands (PH)**
  * city%1:15:01:: (city.n.02) - an incorporated administrative district established by state
    charter Examples: the city raised the tax rate
  * Comment: Sense 2's example shows that this sense is about decision-making bodies within a city.

**Agreement:** Fine: Exactly two agree; Glite: All three agree; Maru2022 fine support: 1/3; Maru2022
Glite support: 3/3.

### D126. senseval2.d002.s059.t008

**Lemma/POS/source:** `thing` / `NOUN` / `senseval2` (`senseval2.d002`)

**Sentence:** -- In most states, increasing expenditures on education, in our current circumstances,
will probably make **[things]** worse, not better.

**Maru2022 label**

* thing%1:09:02:: (matter.n.01) - a vaguely specified concern Examples: several matters to attend to
  | it is none of your affair

**Reviewer verdicts**

* **Robert Farren (RF)**
  * Cannot answer: no sense applies
  * Note: "Things" in this context means "the general situation", at its broadest and vaguest. It's
    not a sense of the noun "thing" properly speaking, since it's always plural and uncountable.
* **Patrick White (PW)**
  * thing%1:09:02:: (matter.n.01) - a vaguely specified concern Examples: several matters to attend
    to | it is none of your affair
* **Penny Hands (PH)**
  * thing%1:09:02:: (matter.n.01) - a vaguely specified concern Examples: several matters to attend
    to | it is none of your affair

**Agreement:** Fine: Exactly two agree; Glite: Exactly two agree; Maru2022 fine support: 2/3;
Maru2022 Glite support: 2/3.

### D127. senseval2.d002.s063.t002

**Lemma/POS/source:** `fact` / `NOUN` / `senseval2` (`senseval2.d002`)

**Sentence:** There is neither mystery nor paradox in the **[fact]** that as educational
expenditures (in real terms) have increased sharply in the past quarter-of-a-century -- we now spend
more per pupil than any other country in the world -- educational performance has declined.

**Maru2022 label**

* fact%1:09:01:: (fact.n.01) - a piece of information about circumstances that exist or events that
  have occurred Examples: first you must collect all the facts of the case

**Reviewer verdicts**

* **Robert Farren (RF)**
  * fact%1:26:01:: (fact.n.03) - an event known to have happened or something known to have existed
    Examples: your fears have no basis in fact | how much of the story is fact and how much fiction
    is hard to tell
* **Patrick White (PW)**
  * fact%1:09:01:: (fact.n.01) - a piece of information about circumstances that exist or events
    that have occurred Examples: first you must collect all the facts of the case
* **Penny Hands (PH)**
  * fact%1:09:01:: (fact.n.01) - a piece of information about circumstances that exist or events
    that have occurred Examples: first you must collect all the facts of the case
  * Comment: I've picked sense 1 because it's close enough; however, 'the fact that ...' is a phrase
    that is used to refer to a particular situation that exists, and ideally, the inventory would
    include that as a sense in its own right. It's not the same as when you say 'Collect all the
    facts' (i.e. things that are true and can be proved); rather it's a way of talking about a
    situation.

**Agreement:** Fine: Exactly two agree; Glite: All three agree; Maru2022 fine support: 2/3; Maru2022
Glite support: 3/3.

### D128. senseval2.d002.s077.t000

**Lemma/POS/source:** `study` / `NOUN` / `senseval2` (`senseval2.d002`)

**Sentence:** **[Study]** after study -- the most recent from the Brookings Institution -- tells us
that the best schools are those that are free of outside interference and are governed by a powerful
head.

**Maru2022 label**

* study%1:04:00:: (survey.n.01) - a detailed critical inspection

**Reviewer verdicts**

* **Robert Farren (RF)**
  * study%1:04:00:: (survey.n.01) - a detailed critical inspection
* **Patrick White (PW)**
  * study%1:10:00:: (report.n.01) - a written document describing the findings of some individual or
    group Examples: this accords with the recent study by Hill and Dale
* **Penny Hands (PH)**
  * study%1:10:00:: (report.n.01) - a written document describing the findings of some individual or
    group Examples: this accords with the recent study by Hill and Dale
  * Comment: The text is talking about the findings, not the process.

**Agreement:** Fine: Exactly two agree; Glite: Exactly two agree; Maru2022 fine support: 1/3;
Maru2022 Glite support: 1/3.

### D129. senseval2.d002.s077.t001

**Lemma/POS/source:** `study` / `NOUN` / `senseval2` (`senseval2.d002`)

**Sentence:** Study after **[study]** -- the most recent from the Brookings Institution -- tells us
that the best schools are those that are free of outside interference and are governed by a powerful
head.

**Maru2022 label**

* study%1:04:00:: (survey.n.01) - a detailed critical inspection

**Reviewer verdicts**

* **Robert Farren (RF)**
  * study%1:04:00:: (survey.n.01) - a detailed critical inspection
* **Patrick White (PW)**
  * study%1:10:00:: (report.n.01) - a written document describing the findings of some individual or
    group Examples: this accords with the recent study by Hill and Dale
* **Penny Hands (PH)**
  * study%1:10:00:: (report.n.01) - a written document describing the findings of some individual or
    group Examples: this accords with the recent study by Hill and Dale
  * Comment: The text is talking about the findings, not the process.

**Agreement:** Fine: Exactly two agree; Glite: Exactly two agree; Maru2022 fine support: 1/3;
Maru2022 Glite support: 1/3.

### D130. senseval3.d000.s006.t002

**Lemma/POS/source:** `bright` / `ADJ` / `senseval3` (`senseval3.d000`)

**Sentence:** Eyes that were clear, but also **[bright]** with a strange intensity, a sort of cold
fire burning behind them.

**Maru2022 label**

* bright%5:00:00:happy:00 (bright.s.07) - characterized by happiness or gladness Examples: bright
  faces | all the world seems bright and gay

**Reviewer verdicts**

* **Robert Farren (RF)**
  * Cannot answer: no sense applies
  * Note: This is another sense of "bright", wholly figurative. Although the analogy is with light,
    it's not saying that the person's eyes are emitting or reflecting light, but that they convey
    something - emotion, or intelligence, or attention - with a certain degree of intensity.
* **Patrick White (PW)**
  * bright%3:00:00:: (bright.a.01) - emitting or reflecting light readily or in large amounts
    Examples: the sun was bright and hot | a bright sunlit room
* **Penny Hands (PH)**
  * bright%3:00:00:: (bright.a.01) - emitting or reflecting light readily or in large amounts
    Examples: the sun was bright and hot | a bright sunlit room

**Agreement:** Fine: Exactly two agree; Glite: Exactly two agree; Maru2022 fine support: 0/3;
Maru2022 Glite support: 0/3.

### D131. senseval3.d000.s006.t006

**Lemma/POS/source:** `fire` / `NOUN` / `senseval3` (`senseval3.d000`)

**Sentence:** Eyes that were clear, but also bright with a strange intensity, a sort of cold
**[fire]** burning behind them.

**Maru2022 label**

* fire%1:22:00:: (fire.n.03) - the process of combustion of inflammable materials producing heat and
  light and (often) smoke Examples: fire was one of our ancestors' first discoveries

**Reviewer verdicts**

* **Robert Farren (RF)**
  * Cannot answer: no sense applies
  * Note: "Fire" in this figurative sense is not a feeling but a manifestation of spirit, of
    intensity.
* **Patrick White (PW)**
  * fire%1:12:00:: (ardor.n.03) - feelings of great warmth and intensity Examples: he spoke with
    great ardor
* **Penny Hands (PH)**
  * fire%1:12:00:: (ardor.n.03) - feelings of great warmth and intensity Examples: he spoke with
    great ardor
  * Comment: Even though sense 6 mentions warmth, the author uses the word modified by 'cold' in
    order to be deliberately contradictory.

**Agreement:** Fine: Exactly two agree; Glite: Exactly two agree; Maru2022 fine support: 0/3;
Maru2022 Glite support: 0/3.

### D132. senseval3.d000.s031.t010

**Lemma/POS/source:** `stare` / `VERB` / `senseval3` (`senseval3.d000`)

**Sentence:** When he finally got the coughing under control, he realized that Pete -LRB- all he
gave was his first name -RRB- was still waiting for an answer -- he did n't even seem to wink as he
continued to **[stare]**.

**Maru2022 label**

* stare%2:29:00:: (stare.v.02) - fixate one's eyes Examples: The ancestor in the painting is staring
  down menacingly

**Reviewer verdicts**

* **Robert Farren (RF)**
  * stare%2:39:00:: (gaze.v.01) - look at with fixed eyes Examples: The students stared at the
    teacher with amazement
* **Patrick White (PW)**
  * stare%2:39:00:: (gaze.v.01) - look at with fixed eyes Examples: The students stared at the
    teacher with amazement
* **Penny Hands (PH)**
  * stare%2:29:00:: (stare.v.02) - fixate one's eyes Examples: The ancestor in the painting is
    staring down menacingly
  * Comment: I picked sense 2 because I think that is referring to the use that is not followed by
    an object, which is the use demonstrated in the text.

**Agreement:** Fine: Exactly two agree; Glite: All three agree; Maru2022 fine support: 1/3; Maru2022
Glite support: 3/3.

### D133. senseval3.d000.s055.t001

**Lemma/POS/source:** `address` / `NOUN` / `senseval3` (`senseval3.d000`)

**Sentence:** Give me your **[address]**.

**Maru2022 label**

* address%1:10:02:: (address.n.06) - written directions for finding some location; written on
  letters or packages that are to be delivered to that location

**Reviewer verdicts**

* **Robert Farren (RF)**
  * address%1:15:00:: (address.n.02) - the place where a person or organization can be found or
    communicated with
* **Patrick White (PW)**
  * address%1:10:02:: (address.n.06) - written directions for finding some location; written on
    letters or packages that are to be delivered to that location
* **Penny Hands (PH)**
  * address%1:15:00:: (address.n.02) - the place where a person or organization can be found or
    communicated with
  * Comment: Sense 6 seems to be specifically about what is written on envelopes and packages. In
    the text, the man wants to know the details of where the other man lives. That's why I opted for
    sense 2 – he simply wants to know where he can find him. But it's a close thing, because he will
    probably write his address down on a piece of paper.

**Agreement:** Fine: Exactly two agree; Glite: All three agree; Maru2022 fine support: 1/3; Maru2022
Glite support: 3/3.

### D134. senseval3.d000.s071.t002

**Lemma/POS/source:** `day` / `NOUN` / `senseval3` (`senseval3.d000`)

**Sentence:** He went for more aspirin later in the **[day]**, and passed the surly landlord on the
way -- he was still alive and scowling as usual, as if tenants were a burden in his life.

**Maru2022 label**

* day%1:28:04:: (day.n.05) - the recurring hours when you are not sleeping (especially those when
  you are working) Examples: my day began early this morning | it was a busy day on the stock
  exchange

**Reviewer verdicts**

* **Robert Farren (RF)**
  * day%1:28:02:: (day.n.04) - the time after sunrise and before sunset while it is light outside
    Examples: the dawn turned night into day | it is easier to make the repairs in the daytime
* **Patrick White (PW)**
  * day%1:28:04:: (day.n.05) - the recurring hours when you are not sleeping (especially those when
    you are working) Examples: my day began early this morning | it was a busy day on the stock
    exchange
* **Penny Hands (PH)**
  * day%1:28:04:: (day.n.05) - the recurring hours when you are not sleeping (especially those when
    you are working) Examples: my day began early this morning | it was a busy day on the stock
    exchange
  * Comment: Not sense 4 because it's not relevant whether it's light or not – it's the time when
    you are awake.

**Agreement:** Fine: Exactly two agree; Glite: Exactly two agree; Maru2022 fine support: 2/3;
Maru2022 Glite support: 2/3.

### D135. senseval3.d000.s076.t000

**Lemma/POS/source:** `come` / `VERB` / `senseval3` (`senseval3.d000`)

**Sentence:** **[Coming]** home from work, he was startled to see a police car parked in front of
the apartment building.

**Maru2022 label**

* come%2:38:00:: (come.v.01) - move toward, travel toward something or somebody or approach
  something or somebody Examples: He came singing down the road | Come with me to the Casbah

**Reviewer verdicts**

* **Robert Farren (RF)**
  * come%2:38:00:: (come.v.01) - move toward, travel toward something or somebody or approach
    something or somebody Examples: He came singing down the road | Come with me to the Casbah
* **Patrick White (PW)**
  * come%2:38:04:: (arrive.v.01) - reach a destination; arrive by movement or progress Examples: She
    arrived home at 7 o'clock | She didn't get to Chicago until after midnight
* **Penny Hands (PH)**
  * come%2:38:04:: (arrive.v.01) - reach a destination; arrive by movement or progress Examples: She
    arrived home at 7 o'clock | She didn't get to Chicago until after midnight

**Agreement:** Fine: Exactly two agree; Glite: All three agree; Maru2022 fine support: 1/3; Maru2022
Glite support: 3/3.

### D136. senseval3.d000.s084.t003

**Lemma/POS/source:** `deliberate` / `ADJ` / `senseval3` (`senseval3.d000`)

**Sentence:** He muttered something about how terrible it was, and walked with **[deliberate]**
slowness to the elevator.

**Maru2022 label**

* deliberate%5:00:00:intended:00 (deliberate.s.01) - carefully thought out in advance Examples: a
  calculated insult | with measured irony

**Reviewer verdicts**

* **Robert Farren (RF)**
  * deliberate%5:00:00:intended:00 (deliberate.s.01) - carefully thought out in advance Examples: a
    calculated insult | with measured irony
  * deliberate%5:00:00:unhurried:00 (careful.s.02) - unhurried and with care and dignity Examples:
    walking at the same measured pace | with all deliberate speed
  * Comment: Given the context, I believe the intended meaning knowingly evokes both of these
    senses. An unhurried and dignified walk that's done consciously and for a tactical purpose.
* **Patrick White (PW)**
  * deliberate%5:00:00:unhurried:00 (careful.s.02) - unhurried and with care and dignity Examples:
    walking at the same measured pace | with all deliberate speed
* **Penny Hands (PH)**
  * deliberate%5:00:00:unhurried:00 (careful.s.02) - unhurried and with care and dignity Examples:
    walking at the same measured pace | with all deliberate speed

**Agreement:** Fine: Exactly two agree; Glite: Exactly two agree; Maru2022 fine support: 0/3;
Maru2022 Glite support: 0/3.

### D137. senseval3.d000.s092.t000

**Lemma/POS/source:** `say` / `VERB` / `senseval3` (`senseval3.d000`)

**Sentence:** Really, he **[said]** to himself, nobody kills a man just as a favor!!

**Maru2022 label**

* say%2:32:13:: (say.v.09) - state as one's opinion or judgement; declare Examples: I say let's
  forget this whole business

**Reviewer verdicts**

* **Robert Farren (RF)**
  * Cannot answer: no sense applies
  * Note: The sense is specific to the reflexive form "say to oneself". Here it means "to muse, to
    reflect".
* **Patrick White (PW)**
  * say%2:32:00:: (state.v.01) - express in words Examples: He said that he wanted to marry her |
    tell me what is bothering you
* **Penny Hands (PH)**
  * say%2:32:00:: (state.v.01) - express in words Examples: He said that he wanted to marry her |
    tell me what is bothering you
  * Comment: This time, it's clear that he didn't say the words out loud. In fact, he said these
    words 'to himself', which means that he just thought them. I've opted for sense 1, because even
    though he didn't say or write the words, he did express them in his mind.

**Agreement:** Fine: Exactly two agree; Glite: Exactly two agree; Maru2022 fine support: 0/3;
Maru2022 Glite support: 2/3.

### D138. senseval3.d000.s101.t001

**Lemma/POS/source:** `grievance` / `NOUN` / `senseval3` (`senseval3.d000`)

**Sentence:** This favorite **[grievance]** was not the landlord.

**Maru2022 label**

* grievance%1:12:00:: (grudge.n.01) - a resentment strong enough to justify retaliation Examples:
  holding a grudge | settling a score

**Reviewer verdicts**

* **Robert Farren (RF)**
  * grievance%1:12:00:: (grudge.n.01) - a resentment strong enough to justify retaliation Examples:
    holding a grudge | settling a score
* **Patrick White (PW)**
  * grievance%1:12:00:: (grudge.n.01) - a resentment strong enough to justify retaliation Examples:
    holding a grudge | settling a score
* **Penny Hands (PH)**
  * grievance%1:10:00:: (grievance.n.03) - a complaint about a (real or imaginary) wrong that causes
    resentment and is grounds for action

**Agreement:** Fine: Exactly two agree; Glite: All three agree; Maru2022 fine support: 2/3; Maru2022
Glite support: 3/3.

### D139. senseval3.d000.s105.t000

**Lemma/POS/source:** `end` / `NOUN` / `senseval3` (`senseval3.d000`)

**Sentence:** Toward the **[end]** of his fourth hairy highball, while he was moodily making wet
rings on the table-top with the bottom of the glass, he became aware that he was not alone.

**Maru2022 label**

* end%1:09:00:: (end.n.05) - a final part or section Examples: we have given it at the end of the
  section since it involves the calculus | Start at the beginning and go on until you come to the
  end
* end%1:28:00:: (end.n.02) - the point in time at which something ends Examples: the end of the year
  | the ending of warranty period

**Reviewer verdicts**

* **Robert Farren (RF)**
  * end%1:09:00:: (end.n.05) - a final part or section Examples: we have given it at the end of the
    section since it involves the calculus | Start at the beginning and go on until you come to the
    end
* **Patrick White (PW)**
  * end%1:28:00:: (end.n.02) - the point in time at which something ends Examples: the end of the
    year | the ending of warranty period
* **Penny Hands (PH)**
  * end%1:28:00:: (end.n.02) - the point in time at which something ends Examples: the end of the
    year | the ending of warranty period
  * Comment: I opted for sense 2 because in the text, 'end' refers to the later part of the time
    period when he was drinking his fourth highball. Sense 3 seems to be more about events that are
    structured to have a beginning, middle and end, and sense 5 seems to be about specific texts,
    such as a chapter or section.

**Agreement:** Fine: Exactly two agree; Glite: All three agree; Maru2022 fine support: 0/3; Maru2022
Glite support: 3/3.

### D140. senseval3.d000.s120.t012

**Lemma/POS/source:** `bright` / `ADJ` / `senseval3` (`senseval3.d000`)

**Sentence:** In time, and two drinks later, he was complaining bitterly about his wife, He was on
the subject for ten minutes or so when he noticed the renewed interest in his listener -- it showed
in the alert face and the suddenly **[bright]** eyes.

**Maru2022 label**

* bright%5:00:00:happy:00 (bright.s.07) - characterized by happiness or gladness Examples: bright
  faces | all the world seems bright and gay

**Reviewer verdicts**

* **Robert Farren (RF)**
  * Cannot answer: no sense applies
  * Note: This is another sense of "bright", wholly figurative. Although the analogy is with light,
    it's not saying that the person's eyes are emitting or reflecting light, but that they convey
    something - emotion, or intelligence, or attention - with a certain degree of intensity.
* **Patrick White (PW)**
  * bright%5:00:00:happy:00 (bright.s.07) - characterized by happiness or gladness Examples: bright
    faces | all the world seems bright and gay
  * Comment: Although it's more "interest" than "happiness"
* **Penny Hands (PH)**
  * bright%5:00:00:happy:00 (bright.s.07) - characterized by happiness or gladness Examples: bright
    faces | all the world seems bright and gay
  * Comment: 'Renewed interest' suggests that the listener's 'bright eyes' related to a positive
    feeling (although we cannot be sure without more context).

**Agreement:** Fine: Exactly two agree; Glite: Exactly two agree; Maru2022 fine support: 2/3;
Maru2022 Glite support: 2/3.

### D141. senseval3.d000.s135.t002

**Lemma/POS/source:** `job` / `NOUN` / `senseval3` (`senseval3.d000`)

**Sentence:** That's why I -- why I do a free **[job]** now and then.

**Maru2022 label**

* job%1:04:02:: (caper.n.03) - a crime (especially a robbery) Examples: the gang pulled off a bank
  job in St. Louis

**Reviewer verdicts**

* **Robert Farren (RF)**
  * job%1:04:01:: (job.n.02) - a specific piece of work required to be done as a duty or for a
    specific fee Examples: estimates of the city's loss on that job ranged as high as a million
    dollars | the job of repairing the engine took several hours
  * Comment: The text really does evoke both sense 2 and sense 13. But there's a sort of comic irony
    in the casual way that the assassin uses this term as sense 2 only, as if he was a plumber
    offering to fix someone's tap for free.
* **Patrick White (PW)**
  * job%1:04:01:: (job.n.02) - a specific piece of work required to be done as a duty or for a
    specific fee Examples: estimates of the city's loss on that job ranged as high as a million
    dollars | the job of repairing the engine took several hours
  * job%1:04:02:: (caper.n.03) - a crime (especially a robbery) Examples: the gang pulled off a bank
    job in St. Louis
  * Comment: It's unclear from the input text whether this is a crime or a legal piece of work
* **Penny Hands (PH)**
  * job%1:04:01:: (job.n.02) - a specific piece of work required to be done as a duty or for a
    specific fee Examples: estimates of the city's loss on that job ranged as high as a million
    dollars | the job of repairing the engine took several hours

**Agreement:** Fine: Exactly two agree; Glite: Exactly two agree; Maru2022 fine support: 0/3;
Maru2022 Glite support: 0/3.

### D142. senseval3.d001.s000.t010

**Lemma/POS/source:** `level` / `NOUN` / `senseval3` (`senseval3.d001`)

**Sentence:** Tuesday's rout of a GOP congressional hopeful in a Mississippi district that has n't
backed a Democratic presidential candidate since Adlai Stevenson is another reminder that, at least
at the federal **[level]**, political `ticket splitting `has been on the rise over the past half
century.

**Maru2022 label**

* level%1:09:00:: (level.n.07) - an abstract place usually conceived as having depth Examples: a
  good actor communicates on several levels | a simile has at least two layers of meaning

**Reviewer verdicts**

* **Robert Farren (RF)**
  * level%1:26:01:: (grade.n.02) - a relative position or degree of value in a graded group
    Examples: lumber of the highest grade
* **Patrick White (PW)**
  * level%1:09:00:: (level.n.07) - an abstract place usually conceived as having depth Examples: a
    good actor communicates on several levels | a simile has at least two layers of meaning
* **Penny Hands (PH)**
  * level%1:26:01:: (grade.n.02) - a relative position or degree of value in a graded group
    Examples: lumber of the highest grade

**Agreement:** Fine: Exactly two agree; Glite: All three agree; Maru2022 fine support: 1/3; Maru2022
Glite support: 3/3.

### D143. senseval3.d001.s009.t015

**Lemma/POS/source:** `public` / `ADJ` / `senseval3` (`senseval3.d001`)

**Sentence:** 1 -RRB- Voters can `buy `one of two brands when they select their political agents --
a Republican brand that believes in the minimalist state and in the virtues of private markets over
the vices of **[public]** action, and a Democratic brand that believes in big government and in
public intervention to remedy the excesses attendant to the pursuit of private interest.

**Maru2022 label**

* public%5:00:00:common:02 (public.s.01) - affecting the people or community as a whole Examples:
  community leaders | community interests

**Reviewer verdicts**

* **Robert Farren (RF)**
  * Cannot answer: no sense applies
  * Note: This is a distinct sense of "public", defined by the Concise Oxford English Dictionary as
    "of or provided by the state". Although superficially close to sense 1, it's virtually
    interchangeable with "government" or "state", used as modifiers.
* **Patrick White (PW)**
  * public%3:00:00:: (public.a.01) - not private; open to or concerning the people as a whole
    Examples: the public good | public libraries
* **Penny Hands (PH)**
  * public%3:00:00:: (public.a.01) - not private; open to or concerning the people as a whole
    Examples: the public good | public libraries
  * Comment: These two sense are close, but I rejected sense 2 because in the text, we're talking
    about action rather than who is affected. The sense 1 example 'public funds' suggests government
    intervention, which is what the text is talking about.

**Agreement:** Fine: Exactly two agree; Glite: Exactly two agree; Maru2022 fine support: 0/3;
Maru2022 Glite support: 2/3.

### D144. senseval3.d001.s009.t022

**Lemma/POS/source:** `public` / `ADJ` / `senseval3` (`senseval3.d001`)

**Sentence:** 1 -RRB- Voters can `buy `one of two brands when they select their political agents --
a Republican brand that believes in the minimalist state and in the virtues of private markets over
the vices of public action, and a Democratic brand that believes in big government and in
**[public]** intervention to remedy the excesses attendant to the pursuit of private interest.

**Maru2022 label**

* public%5:00:00:common:02 (public.s.01) - affecting the people or community as a whole Examples:
  community leaders | community interests

**Reviewer verdicts**

* **Robert Farren (RF)**
  * Cannot answer: no sense applies
  * Note: This is a distinct sense of "public", defined by the Concise Oxford English Dictionary as
    "of or provided by the state". Although superficially close to sense 1, it's virtually
    interchangeable with "government" or "state", used as modifiers.
* **Patrick White (PW)**
  * public%3:00:00:: (public.a.01) - not private; open to or concerning the people as a whole
    Examples: the public good | public libraries
* **Penny Hands (PH)**
  * public%3:00:00:: (public.a.01) - not private; open to or concerning the people as a whole
    Examples: the public good | public libraries
  * Comment: As above, I rejected sense 2 because in the text, we're talking about action rather
    than who is affected. The sense 1 example 'public funds' suggests government intervention, which
    is what the text is talking about.

**Agreement:** Fine: Exactly two agree; Glite: Exactly two agree; Maru2022 fine support: 0/3;
Maru2022 Glite support: 2/3.

### D145. senseval3.d001.s010.t016

**Lemma/POS/source:** `cost` / `NOUN` / `senseval3` (`senseval3.d001`)

**Sentence:** 2 -RRB- Congressional representatives have two basic responsibilities while voting in
office -- dealing with national issues -LRB- programmatic actions such as casting roll call votes on
legislation that imposes **[costs]** and/or confers benefits on the population at large -RRB- and
attending to local issues -LRB- constituency service and pork barrel -RRB-.

**Maru2022 label**

* cost%1:21:00:: (cost.n.01) - the total spent for goods or services including money and time and
  labor

**Reviewer verdicts**

* **Robert Farren (RF)**
  * Cannot answer: no sense applies
  * Note: This is the plural noun "costs", meaning "the total amount of money that you must spend on
    running your home or business" (http://www.collinsdictionary.com) - roughly synonymous with
    "expenses".
* **Patrick White (PW)**
  * cost%1:07:01:: (price.n.03) - value measured by what must be given or done or undergone to
    obtain something Examples: the cost in human life was enormous | the price of success is hard
    work
* **Penny Hands (PH)**
  * cost%1:07:01:: (price.n.03) - value measured by what must be given or done or undergone to
    obtain something Examples: the cost in human life was enormous | the price of success is hard
    work

**Agreement:** Fine: Exactly two agree; Glite: Exactly two agree; Maru2022 fine support: 0/3;
Maru2022 Glite support: 0/3.

### D146. senseval3.d001.s010.t018

**Lemma/POS/source:** `benefit` / `NOUN` / `senseval3` (`senseval3.d001`)

**Sentence:** 2 -RRB- Congressional representatives have two basic responsibilities while voting in
office -- dealing with national issues -LRB- programmatic actions such as casting roll call votes on
legislation that imposes costs and/or confers **[benefits]** on the population at large -RRB- and
attending to local issues -LRB- constituency service and pork barrel -RRB-.

**Maru2022 label**

* benefit%1:21:00:: (benefit.n.01) - financial assistance in time of need

**Reviewer verdicts**

* **Robert Farren (RF)**
  * Cannot answer: no sense applies
  * Note: The intended meaning of "benefits" here appears to be "advantages" or "improvements" in
    the most general sense, not necessarily financial assistance. It could also be about the
    provision of public services.
* **Patrick White (PW)**
  * benefit%1:07:00:: (benefit.n.02) - something that aids or promotes well-being Examples: for the
    benefit of all
* **Penny Hands (PH)**
  * benefit%1:07:00:: (benefit.n.02) - something that aids or promotes well-being Examples: for the
    benefit of all

**Agreement:** Fine: Exactly two agree; Glite: Exactly two agree; Maru2022 fine support: 0/3;
Maru2022 Glite support: 0/3.

### D147. senseval3.d001.s018.t005

**Lemma/POS/source:** `thing` / `NOUN` / `senseval3` (`senseval3.d001`)

**Sentence:** While this theory is exceedingly simple, it appears to explain several **[things]**.

**Maru2022 label**

* thing%1:11:00:: (thing.n.05) - an event Examples: a funny thing happened on the way to the...

**Reviewer verdicts**

* **Robert Farren (RF)**
  * thing%1:26:00:: (thing.n.01) - a special situation Examples: this thing has got to end | it is a
    remarkable thing
* **Patrick White (PW)**
  * thing%1:09:02:: (matter.n.01) - a vaguely specified concern Examples: several matters to attend
    to | it is none of your affair
* **Penny Hands (PH)**
  * thing%1:09:02:: (matter.n.01) - a vaguely specified concern Examples: several matters to attend
    to | it is none of your affair
  * Comment: They are issues, not events.

**Agreement:** Fine: Exactly two agree; Glite: Exactly two agree; Maru2022 fine support: 0/3;
Maru2022 Glite support: 0/3.

### D148. senseval3.d001.s020.t021

**Lemma/POS/source:** `do` / `VERB` / `senseval3` (`senseval3.d001`)

**Sentence:** Second, it explains why voters hold Congress in disdain but generally love their own
congressional representatives: Any individual legislator's constituents appreciate the specific
benefits that the legislator wins for them but not the overall cost associated with every other
legislator **[doing]** likewise for his own constituency.

**Maru2022 label**

* do%2:29:09:: (act.v.02) - behave in a certain manner; show a certain behavior; conduct or comport
  oneself Examples: You should act like an adult | Don't behave like a fool
* do%2:41:04:: (do.v.03) - get (something) done Examples: I did my job

**Reviewer verdicts**

* **Robert Farren (RF)**
  * do%2:29:09:: (act.v.02) - behave in a certain manner; show a certain behavior; conduct or
    comport oneself Examples: You should act like an adult | Don't behave like a fool
* **Patrick White (PW)**
  * do%2:29:09:: (act.v.02) - behave in a certain manner; show a certain behavior; conduct or
    comport oneself Examples: You should act like an adult | Don't behave like a fool
* **Penny Hands (PH)**
  * do%2:41:04:: (do.v.03) - get (something) done Examples: I did my job
  * Comment: 'Winning benefits' is something that a legislator 'gets done' (sense 3).

**Agreement:** Fine: Exactly two agree; Glite: Exactly two agree; Maru2022 fine support: 0/3;
Maru2022 Glite support: 0/3.

### D149. senseval3.d001.s025.t010

**Lemma/POS/source:** `office` / `NOUN` / `senseval3` (`senseval3.d001`)

**Sentence:** Fourth, the theory indicates why the Republican Party may have a difficult time
attracting viable candidates for congressional **[office]**.

**Maru2022 label**

* office%1:26:00:: (office.n.04) - (of a government or government official) holding an office means
  being in power Examples: being in office already gives a candidate a great advantage | during his
  first year in office

**Reviewer verdicts**

* **Robert Farren (RF)**
  * office%1:26:00:: (office.n.04) - (of a government or government official) holding an office
    means being in power Examples: being in office already gives a candidate a great advantage |
    during his first year in office
* **Patrick White (PW)**
  * office%1:26:00:: (office.n.04) - (of a government or government official) holding an office
    means being in power Examples: being in office already gives a candidate a great advantage |
    during his first year in office
* **Penny Hands (PH)**
  * office%1:04:02:: (position.n.06) - a job in an organization Examples: he occupied a post in the
    treasury
  * Comment: Sense 7 because the text refers to a candidate applying for a post, not running to be
    in power.

**Agreement:** Fine: Exactly two agree; Glite: All three agree; Maru2022 fine support: 2/3; Maru2022
Glite support: 3/3.

### D150. senseval3.d001.s026.t002

**Lemma/POS/source:** `discourage` / `VERB` / `senseval3` (`senseval3.d001`)

**Sentence:** Potential candidates may be **[discouraged]** from running less by the congressional
salary than by the prospect of defeat at the hands of a Democratic opponent.

**Maru2022 label**

* discourage%2:37:00:: (discourage.v.02) - deprive of courage or hope; take away hope from; cause to
  feel discouraged

**Reviewer verdicts**

* **Robert Farren (RF)**
  * discourage%2:37:00:: (discourage.v.02) - deprive of courage or hope; take away hope from; cause
    to feel discouraged
* **Patrick White (PW)**
  * Cannot answer: inventory inadequate
  * Note: Sense 2 is close but here the meaning is to make someone less confident in doing something
    rather than have less hope or courage.
* **Penny Hands (PH)**
  * discourage%2:37:00:: (discourage.v.02) - deprive of courage or hope; take away hope from; cause
    to feel discouraged
  * Comment: Sense 2 is more about an internal feeling, involving someone losing motivation for
    something. Sense 1 is more about someone else actively trying to prevent a person from doing
    something.

**Agreement:** Fine: Exactly two agree; Glite: Exactly two agree; Maru2022 fine support: 2/3;
Maru2022 Glite support: 2/3.

### D151. senseval3.d001.s029.t010

**Lemma/POS/source:** `local` / `ADJ` / `senseval3` (`senseval3.d001`)

**Sentence:** To the extent that Democratic legislators from the South have held a disproportionate
share of power in Congress since 1932 and have been able to translate such clout into relatively
more **[local]** benefits for their respective constituencies, voters in the South have had an
especially strong incentive to keep such Democrats in office.

**Maru2022 label**

* local%3:00:01:: (local.a.01) - relating to or applicable to or concerned with the administration
  of a city or town or district rather than a larger area Examples: local taxes | local authorities

**Reviewer verdicts**

* **Robert Farren (RF)**
  * local%3:00:01:: (local.a.01) - relating to or applicable to or concerned with the administration
    of a city or town or district rather than a larger area Examples: local taxes | local
    authorities
* **Patrick White (PW)**
  * local%3:01:01:: (local.a.02) - of or belonging to or characteristic of a particular locality or
    neighborhood Examples: local customs | local schools
* **Penny Hands (PH)**
  * local%3:01:01:: (local.a.02) - of or belonging to or characteristic of a particular locality or
    neighborhood Examples: local customs | local schools
  * Comment: Sense 1 relates to municipal administration, but the text is not talking about local
    government; it's talking about members of Congress bringing benefits back to their local
    communities (sense 2).

**Agreement:** Fine: Exactly two agree; Glite: All three agree; Maru2022 fine support: 1/3; Maru2022
Glite support: 3/3.

### D152. senseval3.d001.s031.t000

**Lemma/POS/source:** `local` / `ADJ` / `senseval3` (`senseval3.d001`)

**Sentence:** Since **[local]** benefit - seeking matters more and national policy making matters
less in the lower chamber of Congress, this is precisely the pattern one would expect if Republicans
are less willing to engage in local benefit - seeking than their Democratic counterparts.

**Maru2022 label**

* local%3:00:01:: (local.a.01) - relating to or applicable to or concerned with the administration
  of a city or town or district rather than a larger area Examples: local taxes | local authorities

**Reviewer verdicts**

* **Robert Farren (RF)**
  * local%3:00:01:: (local.a.01) - relating to or applicable to or concerned with the administration
    of a city or town or district rather than a larger area Examples: local taxes | local
    authorities
* **Patrick White (PW)**
  * local%3:01:01:: (local.a.02) - of or belonging to or characteristic of a particular locality or
    neighborhood Examples: local customs | local schools
* **Penny Hands (PH)**
  * local%3:01:01:: (local.a.02) - of or belonging to or characteristic of a particular locality or
    neighborhood Examples: local customs | local schools

**Agreement:** Fine: Exactly two agree; Glite: All three agree; Maru2022 fine support: 1/3; Maru2022
Glite support: 3/3.

### D153. senseval3.d001.s036.t006

**Lemma/POS/source:** `attendance` / `NOUN` / `senseval3` (`senseval3.d001`)

**Sentence:** Second, if the key assumption is valid, Democrats should have lower **[attendance]**
rates on roll-call votes than Republicans do to the extent that such votes reflect national policy
making and that participating in such votes takes away from the time a legislator could otherwise
devote to local benefit - seeking.

**Maru2022 label**

* attendance%1:04:00:: (attendance.n.01) - the act of being present (at a meeting or event etc.)

**Reviewer verdicts**

* **Robert Farren (RF)**
  * attendance%1:04:00:: (attendance.n.01) - the act of being present (at a meeting or event etc.)
  * Comment: The full phrase used in the text is "attendance rates", which corresponds to the
    meaning of "attendance" in sense 2. But the lexeme "attendance" alone, as used in the text,
    corresponds to sense 1.
* **Patrick White (PW)**
  * attendance%1:04:00:: (attendance.n.01) - the act of being present (at a meeting or event etc.)
  * Comment: in the compound "attendance rates", attendance has this meaning. However, this sentence
    could equally wellbe written withoiut the word "rates" and it would then have sense 2.
* **Penny Hands (PH)**
  * attendance%1:28:00:: (attendance.n.02) - the frequency with which a person is present Examples:
    a student's attendance is an important factor in her grade

**Agreement:** Fine: Exactly two agree; Glite: All three agree; Maru2022 fine support: 2/3; Maru2022
Glite support: 3/3.

### D154. senseval3.d001.s038.t001

**Lemma/POS/source:** `attendance` / `NOUN` / `senseval3` (`senseval3.d001`)

**Sentence:** The Democratic House **[attendance]** rate has not exceeded the Republican House
attendance rate since 1959.

**Maru2022 label**

* attendance%1:04:00:: (attendance.n.01) - the act of being present (at a meeting or event etc.)

**Reviewer verdicts**

* **Robert Farren (RF)**
  * attendance%1:04:00:: (attendance.n.01) - the act of being present (at a meeting or event etc.)
  * Comment: The full phrase used in the text is "attendance rate", which corresponds to the meaning
    of "attendance" in sense 2. But the lexeme "attendance" alone, as used in the text, corresponds
    to sense 1.
* **Patrick White (PW)**
  * attendance%1:04:00:: (attendance.n.01) - the act of being present (at a meeting or event etc.)
  * Comment: in the compound "attendance rates", attendance has this meaning. However, this sentence
    could equally wellbe written withoiut the word "rates" and it would then have sense 2.
* **Penny Hands (PH)**
  * attendance%1:28:00:: (attendance.n.02) - the frequency with which a person is present Examples:
    a student's attendance is an important factor in her grade

**Agreement:** Fine: Exactly two agree; Glite: All three agree; Maru2022 fine support: 2/3; Maru2022
Glite support: 3/3.

### D155. senseval3.d001.s038.t005

**Lemma/POS/source:** `attendance` / `NOUN` / `senseval3` (`senseval3.d001`)

**Sentence:** The Democratic House attendance rate has not exceeded the Republican House
**[attendance]** rate since 1959.

**Maru2022 label**

* attendance%1:04:00:: (attendance.n.01) - the act of being present (at a meeting or event etc.)

**Reviewer verdicts**

* **Robert Farren (RF)**
  * attendance%1:04:00:: (attendance.n.01) - the act of being present (at a meeting or event etc.)
  * Comment: The full phrase used in the text is "attendance rate", which corresponds to the meaning
    of "attendance" in sense 2. But the lexeme "attendance" alone, as used in the text, corresponds
    to sense 1.
* **Patrick White (PW)**
  * attendance%1:04:00:: (attendance.n.01) - the act of being present (at a meeting or event etc.)
  * Comment: in the compound "attendance rates", attendance has this meaning. However, this sentence
    could equally wellbe written withoiut the word "rates" and it would then have sense 2.
* **Penny Hands (PH)**
  * attendance%1:28:00:: (attendance.n.02) - the frequency with which a person is present Examples:
    a student's attendance is an important factor in her grade

**Agreement:** Fine: Exactly two agree; Glite: All three agree; Maru2022 fine support: 2/3; Maru2022
Glite support: 3/3.

### D156. senseval3.d001.s039.t008

**Lemma/POS/source:** `office` / `NOUN` / `senseval3` (`senseval3.d001`)

**Sentence:** Finally, as shown in the table, Democrats allocate a higher proportion of their
personal staffs to district **[offices]** -- where local benefit - seeking duties matter more and
national policy making activities matter less relative to Washington offices.

**Maru2022 label**

* office%1:14:01:: (agency.n.01) - an administrative unit of government Examples: the Central
  Intelligence Agency | the Census Bureau

**Reviewer verdicts**

* **Robert Farren (RF)**
  * office%1:06:00:: (office.n.01) - place of business where professional or clerical duties are
    performed Examples: he rented an office in the new building
* **Patrick White (PW)**
  * office%1:14:01:: (agency.n.01) - an administrative unit of government Examples: the Central
    Intelligence Agency | the Census Bureau
* **Penny Hands (PH)**
  * office%1:06:00:: (office.n.01) - place of business where professional or clerical duties are
    performed Examples: he rented an office in the new building

**Agreement:** Fine: Exactly two agree; Glite: Exactly two agree; Maru2022 fine support: 1/3;
Maru2022 Glite support: 1/3.

### D157. senseval3.d001.s039.t019

**Lemma/POS/source:** `office` / `NOUN` / `senseval3` (`senseval3.d001`)

**Sentence:** Finally, as shown in the table, Democrats allocate a higher proportion of their
personal staffs to district offices -- where local benefit - seeking duties matter more and national
policy making activities matter less relative to Washington **[offices]**.

**Maru2022 label**

* office%1:14:01:: (agency.n.01) - an administrative unit of government Examples: the Central
  Intelligence Agency | the Census Bureau

**Reviewer verdicts**

* **Robert Farren (RF)**
  * office%1:06:00:: (office.n.01) - place of business where professional or clerical duties are
    performed Examples: he rented an office in the new building
* **Patrick White (PW)**
  * office%1:14:01:: (agency.n.01) - an administrative unit of government Examples: the Central
    Intelligence Agency | the Census Bureau
* **Penny Hands (PH)**
  * office%1:06:00:: (office.n.01) - place of business where professional or clerical duties are
    performed Examples: he rented an office in the new building

**Agreement:** Fine: Exactly two agree; Glite: Exactly two agree; Maru2022 fine support: 1/3;
Maru2022 Glite support: 1/3.

### D158. senseval3.d001.s041.t005

**Lemma/POS/source:** `factor` / `NOUN` / `senseval3` (`senseval3.d001`)

**Sentence:** An additional piece of evidence from the Senate: Holding other **[factors]** constant,
such as incumbency advantages and regional factors, the difference between popular votes for
Republican presidential and senatorial candidates in states conducting a Senate election turns out
to be a positive function of how onerous the federal government's tax burden is per state -LRB- a
progressive tax rate hits higher - income states harder -RRB-.

**Maru2022 label**

* factor%1:11:00:: (factor.n.01) - anything that contributes causally to a result Examples: a number
  of factors determined the outcome

**Reviewer verdicts**

* **Robert Farren (RF)**
  * factor%1:11:00:: (factor.n.01) - anything that contributes causally to a result Examples: a
    number of factors determined the outcome
* **Patrick White (PW)**
  * factor%1:11:00:: (factor.n.01) - anything that contributes causally to a result Examples: a
    number of factors determined the outcome
* **Penny Hands (PH)**
  * factor%1:09:01:: (factor.n.06) - an independent variable in statistics
  * Comment: The context is generally 'statistical' enough to warrant a specifically statistical
    definition of 'function'.

**Agreement:** Fine: Exactly two agree; Glite: All three agree; Maru2022 fine support: 2/3; Maru2022
Glite support: 3/3.

### D159. senseval3.d001.s041.t008

**Lemma/POS/source:** `advantage` / `NOUN` / `senseval3` (`senseval3.d001`)

**Sentence:** An additional piece of evidence from the Senate: Holding other factors constant, such
as incumbency **[advantages]** and regional factors, the difference between popular votes for
Republican presidential and senatorial candidates in states conducting a Senate election turns out
to be a positive function of how onerous the federal government's tax burden is per state -LRB- a
progressive tax rate hits higher - income states harder -RRB-.

**Maru2022 label**

* advantage%1:07:01:: (advantage.n.03) - benefit resulting from some event or action Examples: it
  turned out to my advantage | reaping the rewards of generosity

**Reviewer verdicts**

* **Robert Farren (RF)**
  * advantage%1:07:00:: (advantage.n.01) - the quality of having a superior or more favorable
    position Examples: the experience gave him the advantage over me
* **Patrick White (PW)**
  * advantage%1:07:01:: (advantage.n.03) - benefit resulting from some event or action Examples: it
    turned out to my advantage | reaping the rewards of generosity
* **Penny Hands (PH)**
  * advantage%1:07:01:: (advantage.n.03) - benefit resulting from some event or action Examples: it
    turned out to my advantage | reaping the rewards of generosity
  * Comment: Sense 1 suggests a state, whereas in the text, 'advantages' are specific benefits
    (sense 3).

**Agreement:** Fine: Exactly two agree; Glite: All three agree; Maru2022 fine support: 2/3; Maru2022
Glite support: 3/3.

### D160. senseval3.d001.s041.t010

**Lemma/POS/source:** `factor` / `NOUN` / `senseval3` (`senseval3.d001`)

**Sentence:** An additional piece of evidence from the Senate: Holding other factors constant, such
as incumbency advantages and regional **[factors]**, the difference between popular votes for
Republican presidential and senatorial candidates in states conducting a Senate election turns out
to be a positive function of how onerous the federal government's tax burden is per state -LRB- a
progressive tax rate hits higher - income states harder -RRB-.

**Maru2022 label**

* factor%1:11:00:: (factor.n.01) - anything that contributes causally to a result Examples: a number
  of factors determined the outcome

**Reviewer verdicts**

* **Robert Farren (RF)**
  * factor%1:11:00:: (factor.n.01) - anything that contributes causally to a result Examples: a
    number of factors determined the outcome
* **Patrick White (PW)**
  * factor%1:11:00:: (factor.n.01) - anything that contributes causally to a result Examples: a
    number of factors determined the outcome
* **Penny Hands (PH)**
  * factor%1:09:01:: (factor.n.06) - an independent variable in statistics
  * Comment: The context is sufficiently technical to warrant the more technical definition.

**Agreement:** Fine: Exactly two agree; Glite: All three agree; Maru2022 fine support: 2/3; Maru2022
Glite support: 3/3.

### D161. senseval3.d001.s041.t022

**Lemma/POS/source:** `positive` / `ADJ` / `senseval3` (`senseval3.d001`)

**Sentence:** An additional piece of evidence from the Senate: Holding other factors constant, such
as incumbency advantages and regional factors, the difference between popular votes for Republican
presidential and senatorial candidates in states conducting a Senate election turns out to be a
**[positive]** function of how onerous the federal government's tax burden is per state -LRB- a
progressive tax rate hits higher - income states harder -RRB-.

**Maru2022 label**

* positive%5:00:00:plus:00 (positive.s.05) - greater than zero Examples: positive numbers

**Reviewer verdicts**

* **Robert Farren (RF)**
  * positive%5:00:00:plus:00 (positive.s.05) - greater than zero Examples: positive numbers
* **Patrick White (PW)**
  * positive%5:00:00:plus:00 (positive.s.05) - greater than zero Examples: positive numbers
* **Penny Hands (PH)**
  * positive%3:00:05:: (positive.a.08) - reckoned, situated or tending in the direction which
    naturally or arbitrarily is taken to indicate increase or progress or onward motion Examples:
    positive increase in graduating students
  * Comment: 'Positive' here means that as one thing increases, the other thing also increases.

**Agreement:** Fine: Exactly two agree; Glite: Exactly two agree; Maru2022 fine support: 2/3;
Maru2022 Glite support: 2/3.

### D162. senseval3.d001.s041.t023

**Lemma/POS/source:** `function` / `NOUN` / `senseval3` (`senseval3.d001`)

**Sentence:** An additional piece of evidence from the Senate: Holding other factors constant, such
as incumbency advantages and regional factors, the difference between popular votes for Republican
presidential and senatorial candidates in states conducting a Senate election turns out to be a
positive **[function]** of how onerous the federal government's tax burden is per state -LRB- a
progressive tax rate hits higher - income states harder -RRB-.

**Maru2022 label**

* function%1:24:00:: (function.n.01) - (mathematics) a mathematical relation such that each element
  of a given set (the domain of the function) is associated with an element of another set (the
  range of the function)

**Reviewer verdicts**

* **Robert Farren (RF)**
  * function%1:24:00:: (function.n.01) - (mathematics) a mathematical relation such that each
    element of a given set (the domain of the function) is associated with an element of another set
    (the range of the function)
* **Patrick White (PW)**
  * function%1:24:00:: (function.n.01) - (mathematics) a mathematical relation such that each
    element of a given set (the domain of the function) is associated with an element of another set
    (the range of the function)
* **Penny Hands (PH)**
  * function%1:24:01:: (function.n.04) - a relation such that one thing is dependent on another
    Examples: height is a function of age | price is a function of supply and demand
  * Comment: I rejected sense 1, even though it is closely related, because the text is not about
    mathematical calculations; sense 4 covers a similar idea but in more general terms.

**Agreement:** Fine: Exactly two agree; Glite: All three agree; Maru2022 fine support: 2/3; Maru2022
Glite support: 3/3.

### D163. senseval3.d001.s042.t009

**Lemma/POS/source:** `severe` / `ADJ` / `senseval3` (`senseval3.d001`)

**Sentence:** Put more simply, GOP candidates for president are looked on more kindly by voters than
Republican candidates for the Senate when the prisoner's sentence is more **[severe]**.

**Maru2022 label**

* severe%5:00:00:intense:00 (severe.s.01) - intensely or extremely bad or unpleasant in degree or
  quality Examples: severe pain | a severe case of flu
* severe%5:00:01:bad:00 (severe.s.06) - very bad in degree or extent Examples: a severe worldwide
  depression | the house suffered severe damage

**Reviewer verdicts**

* **Robert Farren (RF)**
  * severe%5:00:02:nonindulgent:00 (severe.s.04) - unsparing and uncompromising in discipline or
    judgment; - H.G.Wells Examples: a parent severe to the pitch of hostility | a hefty six-footer
    with a rather severe mien
* **Patrick White (PW)**
  * severe%5:00:00:intense:00 (severe.s.01) - intensely or extremely bad or unpleasant in degree or
    quality Examples: severe pain | a severe case of flu
* **Penny Hands (PH)**
  * severe%5:00:02:nonindulgent:00 (severe.s.04) - unsparing and uncompromising in discipline or
    judgment; - H.G.Wells Examples: a parent severe to the pitch of hostility | a hefty six-footer
    with a rather severe mien

**Agreement:** Fine: Exactly two agree; Glite: Exactly two agree; Maru2022 fine support: 0/3;
Maru2022 Glite support: 1/3.

### D164. senseval3.d001.s043.t007

**Lemma/POS/source:** `level` / `NOUN` / `senseval3` (`senseval3.d001`)

**Sentence:** Moreover, ticket splitting appears to take the same peculiar pattern at the state
government **[level]** as it does at the federal level.

**Maru2022 label**

* level%1:09:00:: (level.n.07) - an abstract place usually conceived as having depth Examples: a
  good actor communicates on several levels | a simile has at least two layers of meaning

**Reviewer verdicts**

* **Robert Farren (RF)**
  * level%1:26:01:: (grade.n.02) - a relative position or degree of value in a graded group
    Examples: lumber of the highest grade
* **Patrick White (PW)**
  * level%1:09:00:: (level.n.07) - an abstract place usually conceived as having depth Examples: a
    good actor communicates on several levels | a simile has at least two layers of meaning
* **Penny Hands (PH)**
  * level%1:26:01:: (grade.n.02) - a relative position or degree of value in a graded group
    Examples: lumber of the highest grade

**Agreement:** Fine: Exactly two agree; Glite: All three agree; Maru2022 fine support: 1/3; Maru2022
Glite support: 3/3.

### D165. senseval3.d001.s043.t009

**Lemma/POS/source:** `level` / `NOUN` / `senseval3` (`senseval3.d001`)

**Sentence:** Moreover, ticket splitting appears to take the same peculiar pattern at the state
government level as it does at the federal **[level]**.

**Maru2022 label**

* level%1:09:00:: (level.n.07) - an abstract place usually conceived as having depth Examples: a
  good actor communicates on several levels | a simile has at least two layers of meaning

**Reviewer verdicts**

* **Robert Farren (RF)**
  * level%1:26:01:: (grade.n.02) - a relative position or degree of value in a graded group
    Examples: lumber of the highest grade
* **Patrick White (PW)**
  * level%1:09:00:: (level.n.07) - an abstract place usually conceived as having depth Examples: a
    good actor communicates on several levels | a simile has at least two layers of meaning
* **Penny Hands (PH)**
  * level%1:26:01:: (grade.n.02) - a relative position or degree of value in a graded group
    Examples: lumber of the highest grade

**Agreement:** Fine: Exactly two agree; Glite: All three agree; Maru2022 fine support: 1/3; Maru2022
Glite support: 3/3.

### D166. senseval3.d001.s045.t005

**Lemma/POS/source:** `factor` / `NOUN` / `senseval3` (`senseval3.d001`)

**Sentence:** A cross-state econometric investigation, furthermore, reveals that, holding other
**[factors]** constant, the difference between a state's major - party vote going to the Republican
gubernatorial candidate and the Republican share of the lower state house is a positive function of
the state tax rate.

**Maru2022 label**

* factor%1:11:00:: (factor.n.01) - anything that contributes causally to a result Examples: a number
  of factors determined the outcome

**Reviewer verdicts**

* **Robert Farren (RF)**
  * factor%1:11:00:: (factor.n.01) - anything that contributes causally to a result Examples: a
    number of factors determined the outcome
* **Patrick White (PW)**
  * factor%1:11:00:: (factor.n.01) - anything that contributes causally to a result Examples: a
    number of factors determined the outcome
* **Penny Hands (PH)**
  * factor%1:09:01:: (factor.n.06) - an independent variable in statistics
  * Comment: The context is sufficiently technical to warrant the more technical definition.

**Agreement:** Fine: Exactly two agree; Glite: All three agree; Maru2022 fine support: 2/3; Maru2022
Glite support: 3/3.

### D167. senseval3.d001.s045.t017

**Lemma/POS/source:** `share` / `NOUN` / `senseval3` (`senseval3.d001`)

**Sentence:** A cross-state econometric investigation, furthermore, reveals that, holding other
factors constant, the difference between a state's major - party vote going to the Republican
gubernatorial candidate and the Republican **[share]** of the lower state house is a positive
function of the state tax rate.

**Maru2022 label**

* share%1:04:00:: (parcel.n.02) - the allotment of some amount by dividing something Examples: death
  gets more than its share of attention from theologians

**Reviewer verdicts**

* **Robert Farren (RF)**
  * share%1:04:00:: (parcel.n.02) - the allotment of some amount by dividing something Examples:
    death gets more than its share of attention from theologians
* **Patrick White (PW)**
  * share%1:04:00:: (parcel.n.02) - the allotment of some amount by dividing something Examples:
    death gets more than its share of attention from theologians
* **Penny Hands (PH)**
  * share%1:21:00:: (share.n.01) - assets belonging to or due to or contributed by an individual
    person or group Examples: he wanted his share in cash
  * Comment: I rejected sense 3 because 'the allotment of' suggests an act rather than the resulting
    assets.

**Agreement:** Fine: Exactly two agree; Glite: All three agree; Maru2022 fine support: 2/3; Maru2022
Glite support: 3/3.

### D168. senseval3.d001.s045.t020

**Lemma/POS/source:** `positive` / `ADJ` / `senseval3` (`senseval3.d001`)

**Sentence:** A cross-state econometric investigation, furthermore, reveals that, holding other
factors constant, the difference between a state's major - party vote going to the Republican
gubernatorial candidate and the Republican share of the lower state house is a **[positive]**
function of the state tax rate.

**Maru2022 label**

* positive%5:00:00:plus:00 (positive.s.05) - greater than zero Examples: positive numbers

**Reviewer verdicts**

* **Robert Farren (RF)**
  * positive%5:00:00:plus:00 (positive.s.05) - greater than zero Examples: positive numbers
* **Patrick White (PW)**
  * positive%5:00:00:plus:00 (positive.s.05) - greater than zero Examples: positive numbers
* **Penny Hands (PH)**
  * positive%3:00:05:: (positive.a.08) - reckoned, situated or tending in the direction which
    naturally or arbitrarily is taken to indicate increase or progress or onward motion Examples:
    positive increase in graduating students
  * Comment: See reasoning at previous instance.

**Agreement:** Fine: Exactly two agree; Glite: Exactly two agree; Maru2022 fine support: 2/3;
Maru2022 Glite support: 2/3.

### D169. senseval3.d001.s045.t021

**Lemma/POS/source:** `function` / `NOUN` / `senseval3` (`senseval3.d001`)

**Sentence:** A cross-state econometric investigation, furthermore, reveals that, holding other
factors constant, the difference between a state's major - party vote going to the Republican
gubernatorial candidate and the Republican share of the lower state house is a positive
**[function]** of the state tax rate.

**Maru2022 label**

* function%1:24:00:: (function.n.01) - (mathematics) a mathematical relation such that each element
  of a given set (the domain of the function) is associated with an element of another set (the
  range of the function)

**Reviewer verdicts**

* **Robert Farren (RF)**
  * function%1:24:00:: (function.n.01) - (mathematics) a mathematical relation such that each
    element of a given set (the domain of the function) is associated with an element of another set
    (the range of the function)
* **Patrick White (PW)**
  * function%1:24:00:: (function.n.01) - (mathematics) a mathematical relation such that each
    element of a given set (the domain of the function) is associated with an element of another set
    (the range of the function)
* **Penny Hands (PH)**
  * function%1:24:01:: (function.n.04) - a relation such that one thing is dependent on another
    Examples: height is a function of age | price is a function of supply and demand
  * Comment: See reasoning at previous instance.

**Agreement:** Fine: Exactly two agree; Glite: All three agree; Maru2022 fine support: 2/3; Maru2022
Glite support: 3/3.

### D170. senseval3.d001.s046.t004

**Lemma/POS/source:** `level` / `NOUN` / `senseval3` (`senseval3.d001`)

**Sentence:** In sum, at both the federal and state government **[levels]** at least part of the
seemingly irrational behavior voters display in the voting booth may have an exceedingly rational
explanation.

**Maru2022 label**

* level%1:09:00:: (level.n.07) - an abstract place usually conceived as having depth Examples: a
  good actor communicates on several levels | a simile has at least two layers of meaning

**Reviewer verdicts**

* **Robert Farren (RF)**
  * level%1:09:00:: (level.n.07) - an abstract place usually conceived as having depth Examples: a
    good actor communicates on several levels | a simile has at least two layers of meaning
* **Patrick White (PW)**
  * level%1:09:00:: (level.n.07) - an abstract place usually conceived as having depth Examples: a
    good actor communicates on several levels | a simile has at least two layers of meaning
* **Penny Hands (PH)**
  * level%1:26:01:: (grade.n.02) - a relative position or degree of value in a graded group
    Examples: lumber of the highest grade
  * Comment: The synonym 'tier' at sense 2 helps to distinguish it from sense 1 because we talk
    about 'tiers of hierarchy'. In addition, levels of government are not establish based on
    intensity, amount or quality (sense 1). Sense 7 seems to be more to do with abstract thought.

**Agreement:** Fine: Exactly two agree; Glite: All three agree; Maru2022 fine support: 2/3; Maru2022
Glite support: 3/3.

### D171. senseval3.d002.s000.t007

**Lemma/POS/source:** `comfort` / `NOUN` / `senseval3` (`senseval3.d002`)

**Sentence:** In the long, frightening night after Tuesday's devastating earthquake, Bay Area
residents searched for **[comfort]** and solace wherever they could.

**Maru2022 label**

* comfort%1:12:00:: (comfort.n.02) - a feeling of freedom from worry or disappointment
* comfort%1:26:00:: (comfort.n.01) - a state of being relaxed and feeling no pain Examples: he is a
  man who enjoys his comfort | she longed for the comfortableness of her armchair
* comfort%1:26:02:: (comfort.n.05) - satisfaction or physical well-being provided by a person or
  thing Examples: his friendship was a comfort | a padded chair was one of the room's few comforts

**Reviewer verdicts**

* **Robert Farren (RF)**
  * comfort%1:04:00:: (consolation.n.02) - the act of consoling; giving relief in affliction
    Examples: his presence was a consolation to her
* **Patrick White (PW)**
  * comfort%1:04:00:: (consolation.n.02) - the act of consoling; giving relief in affliction
    Examples: his presence was a consolation to her
* **Penny Hands (PH)**
  * comfort%1:12:00:: (comfort.n.02) - a feeling of freedom from worry or disappointment
  * Comment: The residents wanted to have their worries taken away (sense 2). Sense 1 is more about
    general domestic comfort (having nice furniture or luxury household items) rather than finding
    something comforting because it stops you from being anxious, like a child's dummy, a teddy bear
    or a computer screen (sense 2). I rejected sense 3, even though it's in the right ballpark
    semantically, because it talks about an 'act' of consoling, whereas in the text, residents were
    seeking a 'feeling'.

**Agreement:** Fine: Exactly two agree; Glite: All three agree; Maru2022 fine support: 0/3; Maru2022
Glite support: 0/3.

### D172. senseval3.d002.s018.t008

**Lemma/POS/source:** `toss` / `VERB` / `senseval3` (`senseval3.d002`)

**Sentence:** This time, it just got stronger and then the building started shaking violently up and
down as though it were a child's toy block that was being **[tossed]**.

**Maru2022 label**

* toss%2:35:00:: (toss.v.06) - agitate Examples: toss the salad
* toss%2:35:05:: (chuck.v.01) - throw carelessly Examples: chuck the ball

**Reviewer verdicts**

* **Robert Farren (RF)**
  * toss%2:38:01:: (convulse.v.03) - move or stir about violently Examples: The feverish patient
    thrashed around in his bed
* **Patrick White (PW)**
  * toss%2:35:05:: (chuck.v.01) - throw carelessly Examples: chuck the ball
* **Penny Hands (PH)**
  * toss%2:35:05:: (chuck.v.01) - throw carelessly Examples: chuck the ball

**Agreement:** Fine: Exactly two agree; Glite: Exactly two agree; Maru2022 fine support: 0/3;
Maru2022 Glite support: 0/3.

### D173. senseval3.d002.s024.t002

**Lemma/POS/source:** `shop` / `NOUN` / `senseval3` (`senseval3.d002`)

**Sentence:** Then the auto paint **[shop]** fire sent an evil-looking cloud of black smoke into the
air.

**Maru2022 label**

* shop%1:06:00:: (shop.n.01) - a mercantile establishment for the retail sale of goods or services
  Examples: he bought it at a shop on Cape Cod

**Reviewer verdicts**

* **Robert Farren (RF)**
  * Cannot answer: no sense applies
  * Note: Because it's preceded by "auto", this sense of "shop"probably means a place where cars are
    serviced, in this case (auto paint shop), where they are repainted. This is a US term that is
    equivalent to "garage" in British English.
* **Patrick White (PW)**
  * shop%1:06:01:: (workshop.n.01) - small workplace where handcrafts or manufacturing are done
* **Penny Hands (PH)**
  * shop%1:06:01:: (workshop.n.01) - small workplace where handcrafts or manufacturing are done
  * Comment: An auto paint shop is a workshop where car bodywork is touched up or where they do
    re-sprays, for example (i.e. it's not where you buy paint for cars).

**Agreement:** Fine: Exactly two agree; Glite: Exactly two agree; Maru2022 fine support: 0/3;
Maru2022 Glite support: 0/3.

### D174. senseval3.d002.s029.t001

**Lemma/POS/source:** `explode` / `VERB` / `senseval3` (`senseval3.d002`)

**Sentence:** Except for the gas tank at Hustead's Towing Service **[exploding]** and burning in
downtown Berkeley, things here are quite peaceful.

**Maru2022 label**

* explode%2:30:00:: (explode.v.02) - burst outward, usually with noise Examples: The champagne
  bottle exploded

**Reviewer verdicts**

* **Robert Farren (RF)**
  * explode%2:30:04:: (detonate.v.02) - burst and release energy as through a violent chemical or
    physical reaction Examples: the bomb detonated at noon | The Molotov cocktail exploded
* **Patrick White (PW)**
  * explode%2:30:04:: (detonate.v.02) - burst and release energy as through a violent chemical or
    physical reaction Examples: the bomb detonated at noon | The Molotov cocktail exploded
* **Penny Hands (PH)**
  * explode%2:30:00:: (explode.v.02) - burst outward, usually with noise Examples: The champagne
    bottle exploded
  * Comment: While sene 9 seems to fit as well, the examples suggest that it is referring to devices
    that are deliberately designed to explode.

**Agreement:** Fine: Exactly two agree; Glite: All three agree; Maru2022 fine support: 1/3; Maru2022
Glite support: 3/3.

### D175. senseval3.d002.s029.t004

**Lemma/POS/source:** `thing` / `NOUN` / `senseval3` (`senseval3.d002`)

**Sentence:** Except for the gas tank at Hustead's Towing Service exploding and burning in downtown
Berkeley, **[things]** here are quite peaceful.

**Maru2022 label**

* thing%1:09:02:: (matter.n.01) - a vaguely specified concern Examples: several matters to attend to
  | it is none of your affair

**Reviewer verdicts**

* **Robert Farren (RF)**
  * Cannot answer: no sense applies
  * Note: The sense is "everything in general", the status quo, the general situation. As noted
    elsewhere, this sense is always plural and uncountable.
* **Patrick White (PW)**
  * thing%1:09:02:: (matter.n.01) - a vaguely specified concern Examples: several matters to attend
    to | it is none of your affair
* **Penny Hands (PH)**
  * thing%1:09:02:: (matter.n.01) - a vaguely specified concern Examples: several matters to attend
    to | it is none of your affair
  * Comment: I think this is still the 'vague concerns' usage, as in 'How are things?' 'Things are
    good/tough right now'. But it is in the context of an event (a gas tank exploding). The author
    is saying that there are no special events happening at the moment despite that, so there is an
    argument for selecting sense 5.

**Agreement:** Fine: Exactly two agree; Glite: Exactly two agree; Maru2022 fine support: 2/3;
Maru2022 Glite support: 2/3.

### D176. senseval3.d002.s082.t005

**Lemma/POS/source:** `unpredictable` / `ADJ` / `senseval3` (`senseval3.d002`)

**Sentence:** The quivers move through my house every few minutes at **[unpredictable]** intervals,
and the mouse that's been living in my kitchen has taken refuge under my desk.

**Maru2022 label**

* unpredictable%3:00:00:: (unpredictable.a.01) - not capable of being foretold
* unpredictable%5:00:00:indeterminable:00 (unpredictable.s.01) - unknown in advance Examples: an
  unpredictable (or indeterminable) future

**Reviewer verdicts**

* **Robert Farren (RF)**
  * unpredictable%3:00:00:: (unpredictable.a.01) - not capable of being foretold
* **Patrick White (PW)**
  * unpredictable%5:00:00:sporadic:00 (irregular.s.01) - not occurring at expected times
* **Penny Hands (PH)**
  * unpredictable%5:00:00:sporadic:00 (irregular.s.01) - not occurring at expected times
  * Comment: The word 'intervals' in the text helps to narrow this down to sense 3, although sense 1
    is not wrong.

**Agreement:** Fine: Exactly two agree; Glite: All three agree; Maru2022 fine support: 0/3; Maru2022
Glite support: 3/3.

### D177. senseval3.d002.s082.t011

**Lemma/POS/source:** `refuge` / `NOUN` / `senseval3` (`senseval3.d002`)

**Sentence:** The quivers move through my house every few minutes at unpredictable intervals, and
the mouse that's been living in my kitchen has taken **[refuge]** under my desk.

**Maru2022 label**

* refuge%1:07:00:: (recourse.n.02) - something or someone turned to for assistance or security
  Examples: his only recourse was the police | took refuge in lying

**Reviewer verdicts**

* **Robert Farren (RF)**
  * refuge%1:06:00:: (refuge.n.03) - a shelter from danger or hardship
* **Patrick White (PW)**
  * refuge%1:06:00:: (refuge.n.03) - a shelter from danger or hardship
* **Penny Hands (PH)**
  * refuge%1:07:00:: (recourse.n.02) - something or someone turned to for assistance or security
    Examples: his only recourse was the police | took refuge in lying

**Agreement:** Fine: Exactly two agree; Glite: All three agree; Maru2022 fine support: 1/3; Maru2022
Glite support: 3/3.

### D178. senseval3.d002.s086.t002

**Lemma/POS/source:** `run` / `VERB` / `senseval3` (`senseval3.d002`)

**Sentence:** Then as things got rougher, we **[ran]** for the door and spent the next few minutes
outside watching the brick sidewalk under our feet oozing up and down, and the flowers waving in an
eerie rhythm.

**Maru2022 label**

* run%2:38:00:: (run.v.01) - move fast by using one's feet, with one foot off the ground at any
  given time Examples: Don't run--you'll be out of breath | The children ran to the store

**Reviewer verdicts**

* **Robert Farren (RF)**
  * run%2:38:00:: (run.v.01) - move fast by using one's feet, with one foot off the ground at any
    given time Examples: Don't run--you'll be out of breath | The children ran to the store
* **Patrick White (PW)**
  * run%2:38:04:: (scat.v.01) - flee; take to one's heels; cut and run Examples: If you see this
    man, run! | The burglars escaped before the police showed up
* **Penny Hands (PH)**
  * run%2:38:00:: (run.v.01) - move fast by using one's feet, with one foot off the ground at any
    given time Examples: Don't run--you'll be out of breath | The children ran to the store
  * Comment: The context suggests that they were indeed fleeing, but from a grammatical and semantic
    point of view, they were moving fast towards the door, which is sense 1.

**Agreement:** Fine: Exactly two agree; Glite: All three agree; Maru2022 fine support: 2/3; Maru2022
Glite support: 3/3.

### D179. senseval3.d002.s093.t005

**Lemma/POS/source:** `slide` / `VERB` / `senseval3` (`senseval3.d002`)

**Sentence:** He said that one of the computers took a three-foot trip **[sliding]** across the
floor.

**Maru2022 label**

* slide%2:38:01:: (skid.v.04) - move obliquely or sideways, usually in an uncontrolled manner
  Examples: the wheels skidded against the sidewalk

**Reviewer verdicts**

* **Robert Farren (RF)**
  * slide%2:38:01:: (skid.v.04) - move obliquely or sideways, usually in an uncontrolled manner
    Examples: the wheels skidded against the sidewalk
* **Patrick White (PW)**
  * slide%2:38:01:: (skid.v.04) - move obliquely or sideways, usually in an uncontrolled manner
    Examples: the wheels skidded against the sidewalk
* **Penny Hands (PH)**
  * slide%2:38:02:: (slide.v.03) - move smoothly along a surface Examples: He slid the money over to
    the other gambler
  * Comment: I rejected sense 1 because it specifies 'obliquely or sideways', which suggests a
    person or vehicle that had been advancing forwards in a controlled way, and then lost control
    and went sideways off the path or road. In the text, on the other hand, the computer had been
    stationary, and then moved smoothly along the floor (sense 3). It didn't lose control, even if
    it seemed that way in the commotion.

**Agreement:** Fine: Exactly two agree; Glite: All three agree; Maru2022 fine support: 2/3; Maru2022
Glite support: 3/3.

### D180. senseval3.d002.s101.t000

**Lemma/POS/source:** `realize` / `VERB` / `senseval3` (`senseval3.d002`)

**Sentence:** When I **[realized]** it was over, I went and stood out in front of the house, waiting
and praying for Merrill to come home, shivering as if it were 20 below zero until he got there.

**Maru2022 label**

* realize%2:31:00:: (understand.v.02) - perceive (an idea or situation) mentally Examples: Now I
  see! | I just can't see your point

**Reviewer verdicts**

* **Robert Farren (RF)**
  * realize%2:31:00:: (understand.v.02) - perceive (an idea or situation) mentally Examples: Now I
    see! | I just can't see your point
* **Patrick White (PW)**
  * realize%2:31:01:: (recognize.v.02) - be fully aware or cognizant of
* **Penny Hands (PH)**
  * realize%2:31:00:: (understand.v.02) - perceive (an idea or situation) mentally Examples: Now I
    see! | I just can't see your point
  * Comment: Sense 2 is the closest because it gives the idea of *becoming* aware, whereas sense 1
    only talks about *being aware*. However, the sense 2 examples do seem to be more about suddenly
    understanding something after a period of being 'in the dark'. Ideally, there would be a
    definition that read 'be *or become* fully aware or cognizant of'.

**Agreement:** Fine: Exactly two agree; Glite: All three agree; Maru2022 fine support: 2/3; Maru2022
Glite support: 3/3.

### D181. senseval3.d002.s120.t007

**Lemma/POS/source:** `bounce` / `VERB` / `senseval3` (`senseval3.d002`)

**Sentence:** We ran into the house to get Mame, but the next tremor threw me in the air and
**[bounced]** me as I tried to get to my feet.

**Maru2022 label**

* bounce%2:35:03:: (bounce.v.02) - hit something so that it bounces Examples: bounce a ball

**Reviewer verdicts**

* **Robert Farren (RF)**
  * bounce%2:35:03:: (bounce.v.02) - hit something so that it bounces Examples: bounce a ball
* **Patrick White (PW)**
  * bounce%2:38:02:: (bounce.v.03) - move up and down repeatedly
* **Penny Hands (PH)**
  * bounce%2:35:03:: (bounce.v.02) - hit something so that it bounces Examples: bounce a ball
  * Comment: Sense 2 is the only one that definitely describes the transitive use of the verb
    bounce. In the text, the tremor is the agent, throwing the author against the ground. Sense 3 is
    also possible, but I don't think the tremor is repeatedly moving the author up and down – I
    think what is being described is a single bounce (sense 2). Also, sense 3 could be only
    describing the intransitive use of 'bounce', as in 'We bounced along the rough road in the
    truck.' but I can't tell.

**Agreement:** Fine: Exactly two agree; Glite: All three agree; Maru2022 fine support: 2/3; Maru2022
Glite support: 3/3.

### D182. senseval3.d002.s124.t000

**Lemma/POS/source:** `thing` / `NOUN` / `senseval3` (`senseval3.d002`)

**Sentence:** Not one **[thing]** in the house is where it is supposed to be, but the structure is
fine.

**Maru2022 label**

* thing%1:06:00:: (thing.n.04) - an artifact Examples: how does this thing work?

**Reviewer verdicts**

* **Robert Farren (RF)**
  * thing%1:06:00:: (thing.n.04) - an artifact Examples: how does this thing work?
  * Comment: The word "thing" is really part of the phrase "not one thing", a more emphatic variant
    of the pronoun "nothing". As such none of the senses given here is entirely right, though sense
    4 is the closest.
* **Patrick White (PW)**
  * thing%1:06:00:: (thing.n.04) - an artifact Examples: how does this thing work?
* **Penny Hands (PH)**
  * thing%1:06:01:: (thing.n.08) - an entity that is not named specifically Examples: I couldn't
    tell what the thing was
  * Comment: I rejected sense 4 because it refers to a specific object; sense 8 is non-specific and
    could refer to any item.

**Agreement:** Fine: Exactly two agree; Glite: All three agree; Maru2022 fine support: 2/3; Maru2022
Glite support: 3/3.

### D183. senseval3.d002.s137.t003

**Lemma/POS/source:** `symptom` / `NOUN` / `senseval3` (`senseval3.d002`)

**Sentence:** Nausea seems a commonplace **[symptom]**.

**Maru2022 label**

* symptom%1:10:00:: (symptom.n.02) - anything that accompanies X and is regarded as an indication of
  X's existence

**Reviewer verdicts**

* **Robert Farren (RF)**
  * symptom%1:10:00:: (symptom.n.02) - anything that accompanies X and is regarded as an indication
    of X's existence
* **Patrick White (PW)**
  * symptom%1:26:00:: (symptom.n.01) - (medicine) any sensation or change in bodily function that is
    experienced by a patient and is associated with a particular disease
* **Penny Hands (PH)**
  * symptom%1:26:00:: (symptom.n.01) - (medicine) any sensation or change in bodily function that is
    experienced by a patient and is associated with a particular disease

**Agreement:** Fine: Exactly two agree; Glite: Exactly two agree; Maru2022 fine support: 1/3;
Maru2022 Glite support: 1/3.

<a id="appendix-e"></a>

## Appendix E. Two reviewers judged the item unanswerable

Exactly two reviewers used cannot-answer and the third reviewer selected a sense. These items are
removed from the lexEN benchmark. Count: 22.

### E1. semeval2013.d006.s010.t003

**Lemma/POS/source:** `spirit` / `NOUN` / `semeval2013` (`semeval2013.d006`)

**Sentence:** The matter examines the type of damage that is brought to the sporting **[spirit]**.

**Maru2022 label**

* spirit%1:26:00:: (spirit.n.02) - the general atmosphere of a place or situation and the effect
  that it has on people Examples: the feel of the city excited him | a clergyman improved the tone
  of the meeting

**Reviewer verdicts**

* **Robert Farren (RF)**
  * spirit%1:26:00:: (spirit.n.02) - the general atmosphere of a place or situation and the effect
    that it has on people Examples: the feel of the city excited him | a clergyman improved the tone
    of the meeting
* **Patrick White (PW)**
  * Cannot answer: input defective
  * Note: Input text is non-natural English.
* **Penny Hands (PH)**
  * Cannot answer: inventory inadequate
  * Note: Sense 3 is close to the correct sense, but it only seems to refer to a person's character
    ('... determining one's character'). In the text, the author is referring to how we expect
    people to think and behave when playing sports. The definition should be something like 'the
    values and principles that determine how someone approaches something'.

In addition, this text seems to be machine-translated or written by someone who has low proficiency
in English.

**Agreement:** Fine: Exactly two agree; Glite: Exactly two agree; Maru2022 fine support: 1/3;
Maru2022 Glite support: 1/3.

### E2. semeval2013.d006.s011.t002

**Lemma/POS/source:** `spirit` / `NOUN` / `semeval2013` (`semeval2013.d006`)

**Sentence:** One of the advantages that include the sport **[spirit]** is the physical integrity of
the opposite players, aspect that with these actions was n't put into danger, that is to say, there
was no violent game.

**Maru2022 label**

* spirit%1:26:00:: (spirit.n.02) - the general atmosphere of a place or situation and the effect
  that it has on people Examples: the feel of the city excited him | a clergyman improved the tone
  of the meeting

**Reviewer verdicts**

* **Robert Farren (RF)**
  * spirit%1:26:00:: (spirit.n.02) - the general atmosphere of a place or situation and the effect
    that it has on people Examples: the feel of the city excited him | a clergyman improved the tone
    of the meeting
* **Patrick White (PW)**
  * Cannot answer: input defective
  * Note: Input text is non-natural English.
* **Penny Hands (PH)**
  * Cannot answer: input defective, inventory inadequate
  * Note: Sense 3 is close to the correct sense, but it only seems to refer to a person ('...
    determining one's character'). In the text, the author is referring to the fundamental emotional
    principles behind a sport. The definition should be something like 'the ideas, beliefs and aims
    of something', with examples like 'the spirit of the times', 'sporting spirit' and 'the spirit
    of democracy'.

In addition, this text seems to be machine-translated or written by someone who has low proficiency
in English.

**Agreement:** Fine: Exactly two agree; Glite: Exactly two agree; Maru2022 fine support: 1/3;
Maru2022 Glite support: 1/3.

### E3. semeval2013.d006.s019.t011

**Lemma/POS/source:** `cycle` / `NOUN` / `semeval2013` (`semeval2013.d006`)

**Sentence:** But it is about a long term advantage, with a certain degree of indetermination,
because the team can be eliminated first of change, and in addition with this action the players
fulfil a sanction game and go to the second **[cycle]** of cards, in which the suspension by card
accumulation takes place with one less than in the first cycle.

**Maru2022 label**

* cycle%1:11:01:: (cycle.n.05) - a single complete execution of a periodically repeated phenomenon
  Examples: a year constitutes a cycle of the seasons

**Reviewer verdicts**

* **Robert Farren (RF)**
  * Cannot answer: no sense applies
  * Note: Sense 1 is close, except that this sense is not about "an interval" during which events
    occur, but about the specific, pre-arranged series of events itself. It corresponds exactly to
    this definition (from collinsdictionary.com): "a completed series of events that follows or is
    followed by another series of similar events occurring in the same sequence".
* **Patrick White (PW)**
  * Cannot answer: input defective
  * Note: Input text is non-natural English, probably written by a Spanish or French speaker for
    whom "ciclo/cycle" would be the right word in this context.
* **Penny Hands (PH)**
  * cycle%1:28:00:: (cycle.n.01) - an interval during which a recurring sequence of events occurs
    Examples: the never-ending cycle of the seasons
  * Comment: Senses 1 and 5 are close, but I chose sense 1 because of the substitutable synonym
    'round'.

**Agreement:** Fine: Exactly two agree; Glite: Exactly two agree; Maru2022 fine support: 0/3;
Maru2022 Glite support: 1/3.

### E4. semeval2013.d006.s019.t017

**Lemma/POS/source:** `cycle` / `NOUN` / `semeval2013` (`semeval2013.d006`)

**Sentence:** But it is about a long term advantage, with a certain degree of indetermination,
because the team can be eliminated first of change, and in addition with this action the players
fulfil a sanction game and go to the second cycle of cards, in which the suspension by card
accumulation takes place with one less than in the first **[cycle]**.

**Maru2022 label**

* cycle%1:11:01:: (cycle.n.05) - a single complete execution of a periodically repeated phenomenon
  Examples: a year constitutes a cycle of the seasons

**Reviewer verdicts**

* **Robert Farren (RF)**
  * Cannot answer: no sense applies
  * Note: Sense 1 is close, except that this sense is not about "an interval" during which events
    occur, but about the specific, pre-arranged series of events itself. It corresponds exactly to
    this definition (from collinsdictionary.com): "a completed series of events that follows or is
    followed by another series of similar events occurring in the same sequence".
* **Patrick White (PW)**
  * Cannot answer: input defective
  * Note: Input text is non-natural English, probably written by a Spanish or French speaker for
    whom "ciclo/cycle" would be the right word in this context.
* **Penny Hands (PH)**
  * cycle%1:28:00:: (cycle.n.01) - an interval during which a recurring sequence of events occurs
    Examples: the never-ending cycle of the seasons
  * Comment: Senses 1 and 5 are close, but I chose sense 1 based on the substitutable synonym
    'round'.

**Agreement:** Fine: Exactly two agree; Glite: Exactly two agree; Maru2022 fine support: 0/3;
Maru2022 Glite support: 1/3.

### E5. semeval2013.d009.s004.t008

**Lemma/POS/source:** `time` / `NOUN` / `semeval2013` (`semeval2013.d009`)

**Sentence:** The justices agreed to hear the suit; indeed, a landmark 5.5 - hour argument is
expected in March, and the outcome is likely to further roil the 2012 presidential race, which will
be in full swing by the **[time]** the court's decision is released.

**Maru2022 label**

* time%1:11:00:: (time.n.01) - an instance or single occasion for some event Examples: this time he
  succeeded | he called four times

**Reviewer verdicts**

* **Robert Farren (RF)**
  * Cannot answer: inventory inadequate, no sense applies
  * Note: "By the time" is an adverbial that is equivalent in meaning to "when". None of the senses
    above cover it.
* **Patrick White (PW)**
  * time%1:28:03:: (clock_time.n.01) - a reading of a point in time as given by a clock Examples: do
    you know what time it is? | the time is 10 o'clock
  * Comment: although this usage is part of a fixed phrase "by the time (that)..."
* **Penny Hands (PH)**
  * Cannot answer: inventory inadequate
  * Note: Sense 3 is close, but it suggests an extended period, whereas the text refers to a point
    in time. A suitable definition would be 'a period of time or a point in time when something
    happens', with examples like 'By the time you arrive, we will have left' or 'I was still at
    school at the time' or 'It seemed like a good time to leave'. Sense 1 refers to the sense
    demonstrated by phrases like 'every time', 'this time', 'next time', etc.

**Agreement:** Fine: Exactly two agree; Glite: Exactly two agree; Maru2022 fine support: 0/3;
Maru2022 Glite support: 0/3.

### E6. semeval2013.d011.s023.t002

**Lemma/POS/source:** `point` / `NOUN` / `semeval2013` (`semeval2013.d011`)

**Sentence:** Nicolas Sarkozy wished at the start of his mandate to look for missing **[points]** of
growth ``with the teeth.''

**Maru2022 label**

* point%1:10:03:: (item.n.01) - a distinct part that can be specified separately in a group of
  things that could be enumerated on a list Examples: he noticed an item in the New York Times | she
  had several items on her shopping list

**Reviewer verdicts**

* **Robert Farren (RF)**
  * Cannot answer: input defective
  * Note: This phrase is a very non-literal translation of an utterance by Nicolas Sarkozy. The word
    "points" was added in translation and doesn't correspond to anything in the original French.
    It's not entirely clear what it refers to, though the phrase "points de croissance" ("growth
    areas") translates literally as "growth points", so that's a candidate. However, "percentage
    points", and "areas" in the sense of "localities" are also fairly plausible.
* **Patrick White (PW)**
  * Cannot answer: input defective
  * Note: The intended meaning is ambiguous - could be just area/example of growth, or percentage
    points of growth
* **Penny Hands (PH)**
  * point%1:10:03:: (item.n.01) - a distinct part that can be specified separately in a group of
    things that could be enumerated on a list Examples: he noticed an item in the New York Times |
    she had several items on her shopping list

**Agreement:** Fine: Exactly two agree; Glite: Exactly two agree; Maru2022 fine support: 1/3;
Maru2022 Glite support: 1/3.

### E7. semeval2015.d001.s008.t002

**Lemma/POS/source:** `input` / `NOUN` / `semeval2015` (`semeval2015.d001`)

**Sentence:** Below these tabs you will find an **[input]** field to type your functions or do your
calculations.

**Maru2022 label**

* input%1:06:00:: (input.n.04) - a component of production; something that goes into the production
  of output

**Reviewer verdicts**

* **Robert Farren (RF)**
  * Cannot answer: no sense applies
  * Note: This sense of the noun "input" seems derived from a sense of the verb "input", "to enter,
    to write in". It means "a writing in, an entry, an entering"., the act of writing in. An "input
    field" is a place where something can be entered in written form. It doesn't fundamentally have
    to be electronic.
* **Patrick White (PW)**
  * Cannot answer: no sense applies
  * Note: Sense is entering of information into a computer
* **Penny Hands (PH)**
  * input%1:10:00:: (input_signal.n.01) - signal going into an electronic system
  * Comment: I rejected sense 4 because that seems to be more about producing something physical,
    while sense 1 relates specifically to electronic systems.

**Agreement:** Fine: Exactly two agree; Glite: Exactly two agree; Maru2022 fine support: 0/3;
Maru2022 Glite support: 0/3.

### E8. semeval2015.d001.s048.t002

**Lemma/POS/source:** `input` / `NOUN` / `semeval2015` (`semeval2015.d001`)

**Sentence:** Then your focus will go to an **[input]** text box where you can type your function.

**Maru2022 label**

* input%1:06:00:: (input.n.04) - a component of production; something that goes into the production
  of output

**Reviewer verdicts**

* **Robert Farren (RF)**
  * Cannot answer: no sense applies
  * Note: This sense of the noun "input" seems derived from a sense of the verb "input", "to enter,
    to write in". It means "a writing in, an entry, an entering"., the act of writing in. An "input
    field" is a place where something can be entered in written form. It doesn't fundamentally have
    to be electronic.
* **Patrick White (PW)**
  * Cannot answer: no sense applies
  * Note: Sense is entering of information into a computer
* **Penny Hands (PH)**
  * input%1:10:00:: (input_signal.n.01) - signal going into an electronic system
  * Comment: As before, I think it's 1 because we're talking about an electronic system (a
    computer), but there could be an argument for 4 because one is inputting data that will be
    processed and become output.

**Agreement:** Fine: Exactly two agree; Glite: Exactly two agree; Maru2022 fine support: 0/3;
Maru2022 Glite support: 0/3.

### E9. senseval2.d000.s017.t007

**Lemma/POS/source:** `continental` / `ADJ` / `senseval2` (`senseval2.d000`)

**Sentence:** The less complicated version of playing tunes on bells, as do the carillons of
**[continental]** Europe, is considered by the English to be childish, fit only for foreigners.

**Maru2022 label**

* continental%3:01:01:: (continental.a.01) - of or pertaining to or typical of Europe Examples: a
  Continental breakfast

**Reviewer verdicts**

* **Robert Farren (RF)**
  * Cannot answer: no sense applies
  * Note: This common sense of "continental", which can only modify "Europe" or European ways,
    customs, values or ideas, means "excluding Britain" or "outside of Britain". Europe as a foreign
    place, seen from the British perspective.
* **Patrick White (PW)**
  * Cannot answer: inventory inadequate
  * Note: The meaning here is "relating to Europe" but explicitly excluding Britain and Ireland
* **Penny Hands (PH)**
  * continental%3:00:00:: (continental.a.04) - being or concerning or limited to a continent
    especially the continents of North America or Europe Examples: the continental United States |
    continental Europe
  * Comment: I selected sense 4 assuming that 'the continents' refers to the main geographical part
    of those places.

**Agreement:** Fine: Exactly two agree; Glite: Exactly two agree; Maru2022 fine support: 0/3;
Maru2022 Glite support: 0/3.

### E10. senseval2.d002.s003.t018

**Lemma/POS/source:** `interest` / `NOUN` / `senseval2` (`senseval2.d002`)

**Sentence:** And the reason we do not want to is that effective education would require us to
relinquish some cherished metaphysical beliefs about human nature in general and the human nature of
young people in particular, well as to violate some cherished vested **[interests]**.

**Maru2022 label**

* interest%1:07:01:: (sake.n.01) - a reason for wanting something done Examples: for your sake |
  died for the sake of his country

**Reviewer verdicts**

* **Robert Farren (RF)**
  * interest%1:07:01:: (sake.n.01) - a reason for wanting something done Examples: for your sake |
    died for the sake of his country
* **Patrick White (PW)**
  * Cannot answer: inventory inadequate
  * Note: "vested interest" is a compound with its own meanings.
* **Penny Hands (PH)**
  * Cannot answer: no sense applies
  * Note: The original meaning of 'vested interest' is what is described in sense 5: a financial or
    legal share of something, or a financial involvement in something. However, in the text it's
    being used to talk about a personal reason for wanting something to happen.

**Agreement:** Fine: Exactly two agree; Glite: Exactly two agree; Maru2022 fine support: 1/3;
Maru2022 Glite support: 1/3.

### E11. senseval2.d002.s006.t004

**Lemma/POS/source:** `wish` / `VERB` / `senseval2` (`senseval2.d002`)

**Sentence:** If I were to ask a sample of American parents,
`Do you **[wish]** the elementary schools to encourage creativity in your children? `the
near-unanimous answer would be, `Yes, of course. `

**Maru2022 label**

* wish%2:37:01:: (wish.v.04) - feel or express a desire or hope concerning the future or fortune of

**Reviewer verdicts**

* **Robert Farren (RF)**
  * Cannot answer: inventory inadequate, no sense applies
  * Note: Wish (x to do y) in this sense simply means "want or prefer" x to do y. None of the senses
    given seem to reflect the direct object + infinitive complement structure found in this example.
    Sense 2 might be the closest, but the definition doesn't seem to extend to this sense (which is
    why I've also ticked "Inventory inadequate").
* **Patrick White (PW)**
  * wish%2:37:01:: (wish.v.04) - feel or express a desire or hope concerning the future or fortune
    of
* **Penny Hands (PH)**
  * Cannot answer: inventory inadequate
  * Note: Sense 2 is roughly the right area, but the definition should say 'to want to do something
    or *to want something to happen*, with an example like 'Do you wish me to stay?' Sense 1 is
    about things you want, but that are unlikely to happen. Sense 4 is about wishing people well or
    wishing them a happy birthday/Christmas, etc.

**Agreement:** Fine: Exactly two agree; Glite: Exactly two agree; Maru2022 fine support: 1/3;
Maru2022 Glite support: 1/3.

### E12. senseval3.d000.s001.t002

**Lemma/POS/source:** `bleary` / `ADJ` / `senseval3` (`senseval3.d000`)

**Sentence:** Haney peered doubtfully at his drinking companion through **[bleary]**, tear-filled
eyes.

**Maru2022 label**

* bleary%5:00:00:indistinct:00 (bleary.s.02) - indistinct or hazy in outline Examples: a landscape
  of blurred outlines | the trees were just blurry shapes

**Reviewer verdicts**

* **Robert Farren (RF)**
  * bleary%5:00:00:tired:00 (bleary.s.01) - tired to the point of exhaustion
* **Patrick White (PW)**
  * Cannot answer: no sense applies
  * Note: Sense is "(of the eyes) unable to see clearly"
* **Penny Hands (PH)**
  * Cannot answer: inventory inadequate
  * Note: What Haney saw would, of course, have been indistinct or hazy in outline (sense 2), but
    his *eyes* were not indistinct or hazy in outline. Sense 1 is much closer, but it suggests that
    'bleary' means 'tired'. A better definition for sense 1 would be 'not able to see clearly,
    especially due to exhaustion'.

**Agreement:** Fine: Exactly two agree; Glite: Exactly two agree; Maru2022 fine support: 0/3;
Maru2022 Glite support: 1/3.

### E13. senseval3.d000.s027.t007

**Lemma/POS/source:** `good` / `ADJ` / `senseval3` (`senseval3.d000`)

**Sentence:** But he decided he would n't mind company in return for free drinks, even though he
made **[good]** money at his job.

**Maru2022 label**

* good%3:00:01:: (good.a.01) - having desirable or positive qualities especially those suitable for
  a thing specified Examples: good news from the hospital | a good report card

**Reviewer verdicts**

* **Robert Farren (RF)**
  * good%5:00:00:ample:00 (full.s.04) - having the normally expected amount Examples: gives full
    measure | gives good measure
* **Patrick White (PW)**
  * Cannot answer: inventory inadequate
  * Note: Here "good" means large, a sense that does not seem to be covered, although sense 2 is
    close
* **Penny Hands (PH)**
  * Cannot answer: no sense applies
  * Note: In the text, 'good money' means 'great in number, amount or degree' and is used in an
    approving way, e.g. a good size, a good number of people, a good amount of money. That sense
    isn't covered in the inventory.

**Agreement:** Fine: Exactly two agree; Glite: Exactly two agree; Maru2022 fine support: 0/3;
Maru2022 Glite support: 0/3.

### E14. senseval3.d000.s029.t001

**Lemma/POS/source:** `have` / `VERB` / `senseval3` (`senseval3.d000`)

**Sentence:** Now he wondered if it was worth it, **[having]** a screwball for company.

**Maru2022 label**

* have%2:40:00:: (have.v.01) - have or possess, either in a concrete or an abstract sense Examples:
  She has $1,000 in the bank | He has got two beautiful daughters
* have%2:42:12:: (have.v.10) - be confronted with Examples: What do we have here? | Now we have a
  fine mess

**Reviewer verdicts**

* **Robert Farren (RF)**
  * have%2:42:12:: (have.v.10) - be confronted with Examples: What do we have here? | Now we have a
    fine mess
  * Comment: I chose sense 10 after much hesitation, but it's not perfect because it's
    over-specific. I would say this sense is more "be" than "have": "be with", "be in the proximity
    of", be in some relation to some particular situation.
* **Patrick White (PW)**
  * Cannot answer: inventory inadequate
  * Note: phrase is "to have sb for company"
* **Penny Hands (PH)**
  * Cannot answer: no sense applies
  * Note: The correct sense does not appear in the inventory: 'to be with someone', e.g. 'She had a
    few friends with her' 'I had a screwball (with me) for company.' The man doesn't possess the
    screwball (sense 1), neither is 'screwball' a type of relationship (sense 7), neither is he
    confronted by a screwball; he just has a screwball with him.

**Agreement:** Fine: Exactly two agree; Glite: Exactly two agree; Maru2022 fine support: 0/3;
Maru2022 Glite support: 0/3.

### E15. senseval3.d000.s033.t000

**Lemma/POS/source:** `think_of` / `VERB` / `senseval3` (`senseval3.d000`)

**Sentence:** ``Guess I ca n't **[think]** of anyone, Pete.

**Maru2022 label**

* think_of%2:31:04:: (think_of.v.06) - choose in one's mind Examples: Think of any integer between 1
  and 25

**Reviewer verdicts**

* **Robert Farren (RF)**
  * think_of%2:31:04:: (think_of.v.06) - choose in one's mind Examples: Think of any integer between
    1 and 25
* **Patrick White (PW)**
  * Cannot answer: no sense applies
  * Note: Sense is "remember"
* **Penny Hands (PH)**
  * Cannot answer: inventory inadequate
  * Note: Haney is thinking about all the people he knows and trying to select one who could fit the
    bill (sense 6). However, sense 6's example does seem to be more about choosing a random
    number/name.

A more appropriate definition for this use of 'think of' might be 'find or produce an answer'.

**Agreement:** Fine: Exactly two agree; Glite: Exactly two agree; Maru2022 fine support: 1/3;
Maru2022 Glite support: 1/3.

### E16. senseval3.d000.s042.t000

**Lemma/POS/source:** `cost` / `VERB` / `senseval3` (`senseval3.d000`)

**Sentence:** It wo n't **[cost]** you a cent, Phil.

**Maru2022 label**

* cost%2:42:01:: (cost.v.02) - require to lose, suffer, or sacrifice Examples: This mistake cost him
  his job

**Reviewer verdicts**

* **Robert Farren (RF)**
  * Cannot answer: no sense applies
  * Note: This sense of "cost nothing" (or "cost something" etc), means "to have a monetary cost, to
    have a price". This is not exactly the same sense as "to cost $x, to be priced at $x".
* **Patrick White (PW)**
  * Cannot answer: inventory inadequate
  * Note: Sense is to oblige someone to pay a certain amount of money. Related to sense 1
    semantically,
* **Penny Hands (PH)**
  * cost%2:42:01:: (cost.v.02) - require to lose, suffer, or sacrifice Examples: This mistake cost
    him his job
  * Comment: Even though the character mentions money ('a cent'), he is not talking about a price of
    a commodity; he's using the grammatical structure '(not) cost sb sth' to say that Phil wouldn't
    have to sacrifice anything (in this case, money) for this favour.

**Agreement:** Fine: Exactly two agree; Glite: Exactly two agree; Maru2022 fine support: 1/3;
Maru2022 Glite support: 1/3.

### E17. senseval3.d001.s019.t014

**Lemma/POS/source:** `confront` / `VERB` / `senseval3` (`senseval3.d001`)

**Sentence:** First, why ticket splitting has increased and taken the peculiar pattern that it has
over the past half century: Prior to the election of Franklin Roosevelt as president and the advent
of the New Deal, government occupied a much smaller role in society and the prisoner's dilemma
problem **[confronting]** voters in races for Congress was considerably less severe.

**Maru2022 label**

* confront%2:32:03:: (confront.v.03) - present somebody with something, usually to accuse or
  criticize Examples: We confronted him with the evidence | He was faced with all the evidence and
  could no longer deny his actions

**Reviewer verdicts**

* **Robert Farren (RF)**
  * confront%2:32:00:: (confront.v.02) - deal with (something unpleasant) head on Examples: You must
    confront your problems | He faced the terrible consequences of his mistakes
* **Patrick White (PW)**
  * Cannot answer: no sense applies
  * Note: In this common usage, it is the problems/situation that are the subject and a person is
    the object. Sense 2 is closest but describes the reverse situation.
* **Penny Hands (PH)**
  * Cannot answer: no sense applies
  * Note: The inventory is missing the sense '(of problems) appear, and need to be dealt with'.

**Agreement:** Fine: Exactly two agree; Glite: Exactly two agree; Maru2022 fine support: 0/3;
Maru2022 Glite support: 0/3.

### E18. senseval3.d001.s027.t011

**Lemma/POS/source:** `competitive` / `ADJ` / `senseval3` (`senseval3.d001`)

**Sentence:** To the extent that potential Republican candidates and their financial backers realize
that the congressional prisoner's dilemma game works to their disadvantage, the Republican Party
will be hindered in its attempts to field a **[competitive]** slate of congressional candidates.

**Maru2022 label**

* competitive%5:00:00:aggressive:00 (competitive.s.02) - showing a fighting disposition Examples:
  highly competitive sales representative | militant in fighting for better wages for workers

**Reviewer verdicts**

* **Robert Farren (RF)**
  * Cannot answer: no sense applies
  * Note: The sense appears to be this (cited from the Concise Oxford English Dictionary, 12th
    edition): "as good as or better than others of a comparable nature". It's about quality rather
    than the will to compete.
* **Patrick White (PW)**
  * Cannot answer: no sense applies
  * Note: Sense is "as good as or better than others"
* **Penny Hands (PH)**
  * competitive%3:00:00:: (competitive.a.01) - involving competition or competitiveness Examples:
    competitive games | to improve one's competitive position

**Agreement:** Fine: Exactly two agree; Glite: Exactly two agree; Maru2022 fine support: 0/3;
Maru2022 Glite support: 0/3.

### E19. senseval3.d002.s016.t006

**Lemma/POS/source:** `smile` / `VERB` / `senseval3` (`senseval3.d002`)

**Sentence:** I felt the temblor begin and glanced at the table next to mine, **[smiled]** that
guilty smile and we both mouthed the words, `Earth-quake! `together.

**Maru2022 label**

* smile%2:32:00:: (smile.v.02) - express with a smile Examples: She smiled her thanks

**Reviewer verdicts**

* **Robert Farren (RF)**
  * smile%2:29:00:: (smile.v.01) - change one's facial expression by spreading the lips, often to
    signal pleasure
* **Patrick White (PW)**
  * Cannot answer: no sense applies
  * Note: The usage "to smile a smile" means just "to smile"
* **Penny Hands (PH)**
  * Cannot answer: no sense applies
  * Note: The inventory is missing a sense: 'to give a particular type of smile', e.g. to smile a
    gentle/wry/beguiling smile.

**Agreement:** Fine: Exactly two agree; Glite: Exactly two agree; Maru2022 fine support: 0/3;
Maru2022 Glite support: 1/3.

### E20. senseval3.d002.s086.t016

**Lemma/POS/source:** `rhythm` / `NOUN` / `senseval3` (`senseval3.d002`)

**Sentence:** Then as things got rougher, we ran for the door and spent the next few minutes outside
watching the brick sidewalk under our feet oozing up and down, and the flowers waving in an eerie
**[rhythm]**.

**Maru2022 label**

* rhythm%1:28:00:: (cycle.n.01) - an interval during which a recurring sequence of events occurs
  Examples: the never-ending cycle of the seasons

**Reviewer verdicts**

* **Robert Farren (RF)**
  * Cannot answer: no sense applies
  * Note: This usage of "rhythm" suggests "repeated, roughly cyclical movement of diverse items, not
    necessarily with regularity". Thus it's probably a figurative or even incorrect usage of
    "rhythm".
* **Patrick White (PW)**
  * rhythm%1:28:00:: (cycle.n.01) - an interval during which a recurring sequence of events occurs
    Examples: the never-ending cycle of the seasons
* **Penny Hands (PH)**
  * Cannot answer: inventory inadequate
  * Note: Sense 2 is the correct one, but it is worded as if it is defining an adjective
    ('rhythmic'). It should be defined as a noun: 'a regular recurring pattern'.

**Agreement:** Fine: Exactly two agree; Glite: Exactly two agree; Maru2022 fine support: 1/3;
Maru2022 Glite support: 1/3.

### E21. senseval3.d002.s116.t002

**Lemma/POS/source:** `family` / `NOUN` / `senseval3` (`senseval3.d002`)

**Sentence:** Biggest trouble was scared **[family]** who could n't get a phone line through, and
spent a really horrible hour not knowing.

**Maru2022 label**

* family%1:14:02:: (family.n.01) - a social unit living together Examples: he moved his family to
  Virginia | It was a good Christian household

**Reviewer verdicts**

* **Robert Farren (RF)**
  * Cannot answer: inventory inadequate, no sense applies
  * Note: This uncountable US English sense of "family" is equivalent to "family members"
    collectively. In sense 4, the description is heading in the right direction but the example
    makes it clear that this is a countable sense. Sense 5 includes "he's family" as an example, but
    the definition doesn't work because "a person having kinship" is not a description of an
    uncountable noun. So it seems that this exact sense of "family" is not listed.
* **Patrick White (PW)**
  * family%1:14:00:: (family.n.02) - primary social group; parents and children Examples: he wanted
    to have a good job before starting a family
  * family%1:14:02:: (family.n.01) - a social unit living together Examples: he moved his family to
    Virginia | It was a good Christian household
  * Comment: Ambiguous as to whether group living together, or parents/children, or indeed extended
    family members
* **Penny Hands (PH)**
  * Cannot answer: inventory inadequate
  * Note: Sense 2 is closest, but 'family' in the text could be referring to aunts, uncles, cousins,
    grandparents, etc.

**Agreement:** Fine: Exactly two agree; Glite: Exactly two agree; Maru2022 fine support: 0/3;
Maru2022 Glite support: 1/3.

### E22. senseval3.d002.s140.t003

**Lemma/POS/source:** `bundle` / `VERB` / `senseval3` (`senseval3.d002`)

**Sentence:** Next to Chez Panisse a homeless couple, **[bundled]** into a blue sleeping bag, sat
up, said, `Good morning `and then the woman smiled, said, `Is n't it great just to be alive? `

**Maru2022 label**

* bundle%2:29:00:: (bundle.v.04) - sleep fully clothed in the same bed with one's betrothed

**Reviewer verdicts**

* **Robert Farren (RF)**
  * Cannot answer: inventory inadequate
  * Note: The point of this imagistic and figurative sense of the verb "bundle" is to suggest that
    the couple resembles a "bundle" (noun). They "look like a bundle", huddling close together and
    well wrapped up in their sleeping bag. I've chosen "Inventory inadequate" because I think the
    issue here is the POS.
* **Patrick White (PW)**
  * Cannot answer: no sense applies
  * Note: Sense here is "wrap in something warm"
* **Penny Hands (PH)**
  * bundle%2:35:00:: (bundle.v.01) - make into a bundle Examples: he bundled up his few possessions
  * Comment: Sense 4 is an old-fashioned, culturally specific term relating to people who are
    engaged to be married sleeping together while fully clothed. I've chosen sense 1 because the
    couple seem as if they have been wrapped up together in a bundle and put in the sleeping bag.
    However, normally, 'to bundle someone *into* something' (i.e with 'into') means 'to push
    somebody somewhere quickly'. I'm pretty sure that's not what the author means, though.

**Agreement:** Fine: Exactly two agree; Glite: Exactly two agree; Maru2022 fine support: 0/3;
Maru2022 Glite support: 0/3.

<a id="appendix-f"></a>

## Appendix F. All three reviewers disagreed

The three reviewers produced three different fine-grained answers. These items are removed from the
lexEN benchmark. Count: 29.

### F1. semeval2013.d000.s019.t000

**Lemma/POS/source:** `game` / `NOUN` / `semeval2013` (`semeval2013.d000`)

**Sentence:** This is clearly a **[game]** where a new economic hegemony is being developed, said
Ulate, who also serves as the regional Mexico and Central America climate change adviser for
Conservation International.

**Maru2022 label**

* game%1:09:00:: (plot.n.01) - a secret scheme to do something (especially something underhand or
  illegal) Examples: they concocted a plot to discredit the governor | I saw through his little game
  from the start

**Reviewer verdicts**

* **Robert Farren (RF)**
  * Cannot answer: no sense applies
  * Note: In this sentence "game" is figurative, and means something like "tactical or diplomatic
    manoeuvring". This sense is quite common, so it's surprising that none of the definitions given
    above seem to cover it. From http://www.collinsdictionary.com: "a way of behaving in which a
    person uses a particular plan, usually in order to gain an advantage". From the Concise Oxford:
    "a type of activity or business regarded as a game".
* **Patrick White (PW)**
  * game%1:04:00:: (game.n.01) - a contest with rules to determine a winner Examples: you need four
    people to play this game
* **Penny Hands (PH)**
  * game%1:09:00:: (plot.n.01) - a secret scheme to do something (especially something underhand or
    illegal) Examples: they concocted a plot to discredit the governor | I saw through his little
    game from the start

**Agreement:** Fine: All three disagree; Glite: All three disagree; Maru2022 fine support: 1/3;
Maru2022 Glite support: 1/3.

### F2. semeval2013.d002.s012.t000

**Lemma/POS/source:** `treasury` / `NOUN` / `semeval2013` (`semeval2013.d002`)

**Sentence:** **[Treasury]** 10-year bond yields have grown to 3.540% against 3.482% on Tuesday
evening, and 30-year bond yields are at 4.497% against 4.492% the previous evening.

**Maru2022 label**

* treasury%1:14:00:: (treasury.n.02) - the government department responsible for collecting and
  managing and spending public revenues
* treasury%1:14:01:: (department_of_the_treasury.n.01) - the federal department that collects
  revenue and administers federal finances; the Treasury Department was created in 1789

**Reviewer verdicts**

* **Robert Farren (RF)**
  * treasury%1:14:01:: (department_of_the_treasury.n.01) - the federal department that collects
    revenue and administers federal finances; the Treasury Department was created in 1789
  * Comment: The sentence, seen in isolation, is ambiguous in that it may or may not refer
    specifically to the US Treasury (sense 5). The larger context confirms that this is the case.
* **Patrick White (PW)**
  * treasury%1:21:01:: (treasury.n.03) - negotiable debt obligations of the United States government
    which guarantees that interest and principal payments will be paid on time
* **Penny Hands (PH)**
  * treasury%1:14:00:: (treasury.n.02) - the government department responsible for collecting and
    managing and spending public revenues

**Agreement:** Fine: All three disagree; Glite: All three disagree; Maru2022 fine support: 0/3;
Maru2022 Glite support: 0/3.

### F3. semeval2013.d005.s005.t001

**Lemma/POS/source:** `court` / `NOUN` / `semeval2013` (`semeval2013.d005`)

**Sentence:** But lawyers for Mr. Hayes have already made **[court]** filings that sketch out
appeals arguments that are likely to occupy the courts for years.

**Maru2022 label**

* court%1:14:00:: (court.n.01) - an assembly (including one or more judges) to conduct judicial
  business

**Reviewer verdicts**

* **Robert Farren (RF)**
  * court%1:06:05:: (court.n.08) - a tribunal that is presided over by a magistrate or by one or
    more judges who administer justice according to the laws
* **Patrick White (PW)**
  * court%1:06:05:: (court.n.08) - a tribunal that is presided over by a magistrate or by one or
    more judges who administer justice according to the laws
  * court%1:14:00:: (court.n.01) - an assembly (including one or more judges) to conduct judicial
    business
  * Comment: These two definitions seem to be defining the same thing.
* **Penny Hands (PH)**
  * court%1:14:00:: (court.n.01) - an assembly (including one or more judges) to conduct judicial
    business
  * Comment: I chose sense 1 over sense 8 because a tribunal is specifically a type of court with
    the authority to deal with a particular problem or disagreement (military, war, etc.), and that
    isn't the case, looking at the wider context of the text.

**Agreement:** Fine: All three disagree; Glite: All three agree; Maru2022 fine support: 1/3;
Maru2022 Glite support: 3/3.

### F4. semeval2013.d009.s022.t000

**Lemma/POS/source:** `conservative` / `NOUN` / `semeval2013` (`semeval2013.d009`)

**Sentence:** Moreover, **[conservatives]** argue that it's Justice Elena Kagan who has an ethical
issue, not Scalia and Thomas.

**Maru2022 label**

* conservative%1:18:01:: (conservative.n.02) - a member of a Conservative Party

**Reviewer verdicts**

* **Robert Farren (RF)**
  * Cannot answer: no sense applies
  * Note: Although this very American sense of "conservatives" is political, it does not imply
    membership of a political party, but rather, "ideological allegiance to right-wing values"
    generally (and moreover these right-wing values are not necessarily very conservative or
    Conservative).
* **Patrick White (PW)**
  * conservative%1:18:00:: (conservative.n.01) - a person who is reluctant to accept changes and new
    ideas
* **Penny Hands (PH)**
  * conservative%1:18:01:: (conservative.n.02) - a member of a Conservative Party
  * Comment: Even though there is no 'Conservative Party' (see sense 2) per se in the US, I am
    taking this definition to refer to right-leaning political parties in general, and this text is
    clearly about politics.

**Agreement:** Fine: All three disagree; Glite: All three disagree; Maru2022 fine support: 1/3;
Maru2022 Glite support: 1/3.

### F5. semeval2015.d001.s009.t007

**Lemma/POS/source:** `input` / `NOUN` / `semeval2015` (`semeval2015.d001`)

**Sentence:** If we want to understand how it works, the best thing we can do is to realize that our
**[input]** is being converted into MathML although it is not necessary to know MathML.

**Maru2022 label**

* input%1:06:00:: (input.n.04) - a component of production; something that goes into the production
  of output

**Reviewer verdicts**

* **Robert Farren (RF)**
  * input%1:06:00:: (input.n.04) - a component of production; something that goes into the
    production of output
* **Patrick White (PW)**
  * Cannot answer: no sense applies
  * Note: Sense is entering of information into a computer
* **Penny Hands (PH)**
  * input%1:10:00:: (input_signal.n.01) - signal going into an electronic system
  * Comment: I rejected sense 4 because that seems to be more about producing something physical,
    while sense 1 relates specifically to electronic systems.

**Agreement:** Fine: All three disagree; Glite: All three disagree; Maru2022 fine support: 1/3;
Maru2022 Glite support: 1/3.

### F6. semeval2015.d002.s011.t008

**Lemma/POS/source:** `organisation` / `NOUN` / `semeval2015` (`semeval2015.d002`)

**Sentence:** These case studies analysed the background of the initiatives, their impact on
employment patterns and work **[organisations]** and assessed the benefits and problems of the
initiative.

**Maru2022 label**

* organisation%1:14:00:: (organization.n.01) - a group of people who work together
* organisation%1:14:01:: (administration.n.02) - the persons (or committees or departments etc.) who
  make up a body for the purpose of administering something Examples: he claims that the present
  administration is corrupt | the governance of an association is responsible to its members

**Reviewer verdicts**

* **Robert Farren (RF)**
  * organisation%1:14:01:: (administration.n.02) - the persons (or committees or departments etc.)
    who make up a body for the purpose of administering something Examples: he claims that the
    present administration is corrupt | the governance of an association is responsible to its
    members
* **Patrick White (PW)**
  * organisation%1:14:00:: (organization.n.01) - a group of people who work together
* **Penny Hands (PH)**
  * organisation%1:04:01:: (organization.n.06) - the activity or result of distributing or disposing
    persons or things properly or methodically Examples: his organization of the work force was very
    efficient
  * Comment: The sentence is not very well written, but I think it's trying to say 'the way work is
    organised'.

**Agreement:** Fine: All three disagree; Glite: Exactly two agree; Maru2022 fine support: 0/3;
Maru2022 Glite support: 2/3.

### F7. semeval2015.d003.s009.t014

**Lemma/POS/source:** `follow` / `VERB` / `semeval2015` (`semeval2015.d003`)

**Sentence:** In combination with supportive measures such as other veterinary treatment or a
special diet, Cerenia can also be used in the treatment of vomiting (either as injection or as
injection **[followed]** by tablets).

**Maru2022 label**

* follow%2:42:03:: (follow.v.10) - to bring something about at a later time than Examples: She
  followed dinner with a brandy | He followed his lecture with a question and answer period

**Reviewer verdicts**

* **Robert Farren (RF)**
  * follow%2:42:03:: (follow.v.10) - to bring something about at a later time than Examples: She
    followed dinner with a brandy | He followed his lecture with a question and answer period
* **Patrick White (PW)**
  * follow%2:42:01:: (follow.v.06) - come after in time, as a result Examples: A terrible tsunami
    followed the earthquake
* **Penny Hands (PH)**
  * follow%2:42:00:: (postdate.v.01) - be later in time Examples: Tuesday always follows Monday
  * Comment: '... an injection followed by tablets' is a passive construction which can be rephrased
    as 'tablets follow an injection' (just as Wednesday follows Tuesday). There is no human agent
    involved. This means it can't be sense 10 because it would have to be 'She/he follows the
    injections with tablets.' It isn't sense 6 either because the tablets do not come as a result of
    the injection.

**Agreement:** Fine: All three disagree; Glite: All three agree; Maru2022 fine support: 1/3;
Maru2022 Glite support: 3/3.

### F8. semeval2015.d003.s012.t002

**Lemma/POS/source:** `act` / `VERB` / `semeval2015` (`semeval2015.d003`)

**Sentence:** Cerenia blocks a neurokinin 1 (NK1) receptor, which **[acts]** in the central nervous
system.

**Maru2022 label**

* act%2:41:00:: (act.v.01) - perform an action, or work out or perform (an action) Examples: think
  before you act | We must move quickly

**Reviewer verdicts**

* **Robert Farren (RF)**
  * Cannot answer: no sense applies
  * Note: This sense of "act" can't be defined in isolation, it's really "act in the central nervous
    system": the location of the act is what matters, more than what the event is or what exactly
    the receptor does. It "has its role, its function, its purpose" in the central nervous system.
    Something "happens" in the central nervous system.
* **Patrick White (PW)**
  * act%2:41:06:: (work.v.03) - have an effect or outcome; often the one desired or expected
    Examples: The voting process doesn't work as well as people thought | How does your idea work in
    practice?
* **Penny Hands (PH)**
  * act%2:41:00:: (act.v.01) - perform an action, or work out or perform (an action) Examples: think
    before you act | We must move quickly

**Agreement:** Fine: All three disagree; Glite: All three disagree; Maru2022 fine support: 1/3;
Maru2022 Glite support: 1/3.

### F9. senseval2.d001.s009.t002

**Lemma/POS/source:** `make` / `VERB` / `senseval2` (`senseval2.d001`)

**Sentence:** When functioning normally, they **[make]** proteins that hold a cell's growth in
check.

**Maru2022 label**

* make%2:36:00:: (make.v.03) - make or cause to be or to become Examples: make a mess in one's
  office | create a furor
* make%2:36:08:: (cause.v.01) - give rise to; cause to happen or occur, not always intentionally
  Examples: cause a commotion | make a stir

**Reviewer verdicts**

* **Robert Farren (RF)**
  * make%2:36:00:: (make.v.03) - make or cause to be or to become Examples: make a mess in one's
    office | create a furor
* **Patrick White (PW)**
  * make%2:36:01:: (produce.v.02) - create or manufacture a man-made product Examples: We produce
    more cars than we can sell | The company has been making toys for two centuries
  * Comment: Although the thing produced is not man-made, this sense seems the best.
* **Penny Hands (PH)**
  * Cannot answer: inventory inadequate
  * Note: Definitions 3 and 5 are reasonably close, but the examples are all abstract, not physical
    entities that are produced. Sense 6 would have worked if it hadn't specified 'as part of a
    man-made process'. The inventory is lacking the basic sense of 'make', which is 'create or
    produce something as a result of a process.'

**Agreement:** Fine: All three disagree; Glite: All three disagree; Maru2022 fine support: 0/3;
Maru2022 Glite support: 1/3.

### F10. senseval2.d001.s013.t004

**Lemma/POS/source:** `believe` / `VERB` / `senseval2` (`senseval2.d001`)

**Sentence:** In recent months, researchers have come to **[believe]** the two types of cancer genes
work in concert: An oncogene may turn proliferating cells malignant only after the tumor-suppressor
gene has been damaged.

**Maru2022 label**

* believe%2:31:03:: (believe.v.03) - be confident about something Examples: I believe that he will
  come back from the war

**Reviewer verdicts**

* **Robert Farren (RF)**
  * Cannot answer: no sense applies
  * Note: This sense of "believe", in a context involving researchers, can be described as "consider
    to be true, on the balance of probabilities and based on evidence and reason, a hypothesis that
    is not yet proven to be true". Obviously close to sense 1, but much more specific.
* **Patrick White (PW)**
  * believe%2:31:04:: (think.v.01) - judge or regard; look upon; judge Examples: I think he is very
    smart | I believe her to be very smart
* **Penny Hands (PH)**
  * believe%2:31:00:: (believe.v.01) - accept as true; take to be true Examples: I believed his
    report | We didn't believe his stories from the War
  * Comment: I chose sense 1 because researchers now accept this to be true, based on evidence.
    Sense 2 seems to be more about saying what you think someone is like. Sense 3 seems to be more
    about trusting in fate.

**Agreement:** Fine: All three disagree; Glite: Exactly two agree; Maru2022 fine support: 0/3;
Maru2022 Glite support: 2/3.

### F11. senseval2.d001.s015.t001

**Lemma/POS/source:** `make` / `VERB` / `senseval2` (`senseval2.d001`)

**Sentence:** Either copy can **[make]** the proteins needed to control cell growth, so for cancer
to arise, both copies must be impaired.

**Maru2022 label**

* make%2:36:00:: (make.v.03) - make or cause to be or to become Examples: make a mess in one's
  office | create a furor
* make%2:36:08:: (cause.v.01) - give rise to; cause to happen or occur, not always intentionally
  Examples: cause a commotion | make a stir

**Reviewer verdicts**

* **Robert Farren (RF)**
  * make%2:36:00:: (make.v.03) - make or cause to be or to become Examples: make a mess in one's
    office | create a furor
* **Patrick White (PW)**
  * make%2:36:01:: (produce.v.02) - create or manufacture a man-made product Examples: We produce
    more cars than we can sell | The company has been making toys for two centuries
  * Comment: Although the thing produced is not man-made, this sense seems the best.
* **Penny Hands (PH)**
  * Cannot answer: inventory inadequate
  * Note: Definitions 3 and 5 are reasonably close, but the examples are all abstract, not physical
    entities that are produced. Sense 6 would have worked if it hadn't specified 'as part of a
    man-made process'. The inventory is lacking the basic sense of 'make', which is 'create or
    produce something as a result of a process.'

**Agreement:** Fine: All three disagree; Glite: All three disagree; Maru2022 fine support: 0/3;
Maru2022 Glite support: 1/3.

### F12. senseval2.d001.s026.t007

**Lemma/POS/source:** `fundamental` / `ADJ` / `senseval2` (`senseval2.d001`)

**Sentence:**
`It turns out that studying a tragic but uncommon tumor made possible some **[fundamental]** insights about the most basic workings of cancer, `says
Samuel Broder, director of the National Cancer Institute.

**Maru2022 label**

* fundamental%5:00:00:important:00 (cardinal.s.01) - serving as an essential component Examples: a
  cardinal rule | the central cause of the problem
* fundamental%5:00:00:significant:00 (fundamental.s.03) - far-reaching and thoroughgoing in effect
  especially on the nature of something Examples: the fundamental revolution in human values that
  has occurred | the book underwent fundamental changes

**Reviewer verdicts**

* **Robert Farren (RF)**
  * fundamental%5:00:00:basic:00 (fundamental.s.02) - being or involving basic facts or principles
    Examples: the fundamental laws of the universe | a fundamental incomatibility between them
  * fundamental%5:00:00:significant:00 (fundamental.s.03) - far-reaching and thoroughgoing in effect
    especially on the nature of something Examples: the fundamental revolution in human values that
    has occurred | the book underwent fundamental changes
  * Comment: Both senses fit perfectly, and the context doesn't clarify which one is the intended
    meaning.
* **Patrick White (PW)**
  * fundamental%5:00:00:significant:00 (fundamental.s.03) - far-reaching and thoroughgoing in effect
    especially on the nature of something Examples: the fundamental revolution in human values that
    has occurred | the book underwent fundamental changes
* **Penny Hands (PH)**
  * fundamental%5:00:00:basic:00 (fundamental.s.02) - being or involving basic facts or principles
    Examples: the fundamental laws of the universe | a fundamental incomatibility between them
  * Comment: It is tempting to also select sense 3, but I think I would be inferring too much from
    the text. Yes, basic/core/underlying insights often have far-reaching effects, but the text is
    not explicitly talking about fundamental changes or shifts.

**Agreement:** Fine: All three disagree; Glite: All three agree; Maru2022 fine support: 0/3;
Maru2022 Glite support: 3/3.

### F13. senseval2.d001.s041.t005

**Lemma/POS/source:** `specific` / `ADJ` / `senseval2` (`senseval2.d001`)

**Sentence:** Back then, scientists had no way of ferreting out **[specific]** genes, but under a
microscope they could see the 23 pairs of chromosomes in the cells that contain the genes.

**Maru2022 label**

* specific%5:00:00:specified:00 (specific.s.01) - stated explicitly or in detail Examples: needed a
  specific amount

**Reviewer verdicts**

* **Robert Farren (RF)**
  * Cannot answer: no sense applies
  * Note: Constituting one individual member of a set, as distinct from any other member of that
    set.
* **Patrick White (PW)**
  * specific%5:00:00:specified:00 (specific.s.01) - stated explicitly or in detail Examples: needed
    a specific amount
* **Penny Hands (PH)**
  * specific%3:00:00:: (specific.a.01) - (sometimes followed by `to') applying to or characterized
    by or distinguishing something particular or special or unique Examples: rules with specific
    application | demands specific to the job

**Agreement:** Fine: All three disagree; Glite: Exactly two agree; Maru2022 fine support: 1/3;
Maru2022 Glite support: 2/3.

### F14. senseval2.d001.s057.t002

**Lemma/POS/source:** `attention` / `NOUN` / `senseval2` (`senseval2.d001`)

**Sentence:** Dr. Vogelstein next turned his **[attention]** colon cancer, the second biggest cancer
killer in the U.S. after lung cancer.

**Maru2022 label**

* attention%1:09:01:: (attention.n.05) - the faculty or power of mental concentration Examples:
  keeping track of all the details requires your complete attention

**Reviewer verdicts**

* **Robert Farren (RF)**
  * Cannot answer: no sense applies
  * Note: This sense of "attention" can be described as "focused, sustained inquiry", rather than
    concentration.
* **Patrick White (PW)**
  * attention%1:09:01:: (attention.n.05) - the faculty or power of mental concentration Examples:
    keeping track of all the details requires your complete attention
* **Penny Hands (PH)**
  * attention%1:09:00:: (attention.n.01) - the process whereby a person concentrates on some
    features of the environment to the (relative) exclusion of others

**Agreement:** Fine: All three disagree; Glite: Exactly two agree; Maru2022 fine support: 1/3;
Maru2022 Glite support: 2/3.

### F15. senseval2.d001.s086.t008

**Lemma/POS/source:** `think` / `VERB` / `senseval2` (`senseval2.d001`)

**Sentence:** Ray White in Utah and Walter Bodmer, a researcher in Great Britain, are close to
finding another gene involved with some types of colon cancer, **[thought]** to be on chromosome 5.

**Maru2022 label**

* think%2:31:03:: (think.v.02) - expect, believe, or suppose Examples: I imagine she earned a lot of
  money with her new novel | I thought to find her in a bad state

**Reviewer verdicts**

* **Robert Farren (RF)**
  * Cannot answer: no sense applies
  * Note: This sense of "thought", in a research context, can be described as "believed, based on
    evidence and reason, but not yet proven".
* **Patrick White (PW)**
  * think%2:31:03:: (think.v.02) - expect, believe, or suppose Examples: I imagine she earned a lot
    of money with her new novel | I thought to find her in a bad state
* **Penny Hands (PH)**
  * think%2:31:01:: (think.v.01) - judge or regard; look upon; judge Examples: I think he is very
    smart | I believe her to be very smart
  * Comment: I rejected sense 2 because it seems to be more about speculating or guessing.

**Agreement:** Fine: All three disagree; Glite: Exactly two agree; Maru2022 fine support: 1/3;
Maru2022 Glite support: 2/3.

### F16. senseval2.d002.s003.t007

**Lemma/POS/source:** `metaphysical` / `ADJ` / `senseval2` (`senseval2.d002`)

**Sentence:** And the reason we do not want to is that effective education would require us to
relinquish some cherished **[metaphysical]** beliefs about human nature in general and the human
nature of young people in particular, well as to violate some cherished vested interests.

**Maru2022 label**

* metaphysical%5:00:00:theoretical:00 (metaphysical.s.02) - highly abstract and overly theoretical
  Examples: metaphysical reasoning

**Reviewer verdicts**

* **Robert Farren (RF)**
  * Cannot answer: no sense applies
  * Note: This sense of "metaphysical" is approximately opposite in meaning to "empirical, concrete,
    observable, demonstrable". It has connotations of not being rooted in observable everyday
    reality.
* **Patrick White (PW)**
  * metaphysical%3:01:00:: (metaphysical.a.01) - pertaining to or of the nature of metaphysics
    Examples: metaphysical philosophy
* **Penny Hands (PH)**
  * metaphysical%5:00:00:theoretical:00 (metaphysical.s.02) - highly abstract and overly theoretical
    Examples: metaphysical reasoning

**Agreement:** Fine: All three disagree; Glite: All three disagree; Maru2022 fine support: 1/3;
Maru2022 Glite support: 1/3.

### F17. senseval2.d002.s004.t002

**Lemma/POS/source:** `dominate` / `VERB` / `senseval2` (`senseval2.d002`)

**Sentence:** These beliefs so **[dominate]** our educational establishment, our media, our
politicians, and even our parents that it seems almost blasphemous to challenge them.

**Maru2022 label**

* dominate%2:42:00:: (predominate.v.01) - be larger in number, quantity, power, status or importance
  Examples: Money reigns supreme here | Hispanics predominate in this neighborhood

**Reviewer verdicts**

* **Robert Farren (RF)**
  * dominate%2:42:00:: (predominate.v.01) - be larger in number, quantity, power, status or
    importance Examples: Money reigns supreme here | Hispanics predominate in this neighborhood
* **Patrick White (PW)**
  * Cannot answer: inventory inadequate
  * Note: Sense is "be the most important/noticeable part of something". Close to sense 1.
* **Penny Hands (PH)**
  * dominate%2:42:01:: (dominate.v.02) - be in control Examples: Her husband completely dominates
    her
  * Comment: I opted for sense 2 because according to the text, these beliefs strongly influence
    (i.e. dominate) the educational establishment, and 'control' and 'strongly influence' are
    similar in meaning,

**Agreement:** Fine: All three disagree; Glite: Exactly two agree; Maru2022 fine support: 1/3;
Maru2022 Glite support: 2/3.

### F18. senseval2.d002.s055.t001

**Lemma/POS/source:** `involvement` / `NOUN` / `senseval2` (`senseval2.d002`)

**Sentence:** -- `Community **[involvement]** `is an even worse idea.

**Maru2022 label**

* involvement%1:26:01:: (participation.n.02) - the condition of sharing in common with others (as
  fellows or partners etc.)

**Reviewer verdicts**

* **Robert Farren (RF)**
  * Cannot answer: inventory inadequate
  * Note: This sense of "involvement" includes the idea of participating, not only in an activity,
    but also in control or decision-making. It's about sharing power, having a say in how things are
    done, as well as taking an active part in doing them. So it's close to sense 5 above, but more
    specific.
* **Patrick White (PW)**
  * involvement%1:04:00:: (engagement.n.07) - the act of sharing in the activities of a group
    Examples: the teacher tried to increase his students' engagement in class activities
* **Penny Hands (PH)**
  * involvement%1:26:01:: (participation.n.02) - the condition of sharing in common with others (as
    fellows or partners etc.)
  * Comment: This one is more about the relationship between the school and the community, e.g.
    local politicians having an influence over policy decisions (sense 5). It is not about the
    community's active participation in the children's learning (which would be sense 1).

**Agreement:** Fine: All three disagree; Glite: Exactly two agree; Maru2022 fine support: 1/3;
Maru2022 Glite support: 2/3.

### F19. senseval2.d002.s076.t004

**Lemma/POS/source:** `large` / `ADJ` / `senseval2` (`senseval2.d002`)

**Sentence:** -- Most important of all, schools should have principals with a **[large]** measure of
authority over the faculty, the curriculum, and all matters of student discipline.

**Maru2022 label**

* large%5:00:00:significant:00 (large.s.01) - fairly large or important in effect; influential
  Examples: played a large role in the negotiations

**Reviewer verdicts**

* **Robert Farren (RF)**
  * large%5:00:00:comprehensive:00 (large.s.05) - having broad power and range and scope Examples:
    taking the large view | a large effect
* **Patrick White (PW)**
  * large%3:00:00:: (large.a.01) - above average in size or number or quantity or magnitude or
    extent Examples: a large city | set out for the big city
* **Penny Hands (PH)**
  * large%5:00:00:significant:00 (large.s.01) - fairly large or important in effect; influential
    Examples: played a large role in the negotiations
  * Comment: Sense 2 mentions 'influential', which is what is described in the text.

**Agreement:** Fine: All three disagree; Glite: Exactly two agree; Maru2022 fine support: 1/3;
Maru2022 Glite support: 2/3.

### F20. senseval3.d000.s002.t001

**Lemma/POS/source:** `ready` / `ADJ` / `senseval3` (`senseval3.d000`)

**Sentence:** He had no **[ready]** answer, as much from surprise as from the fit of coughing.

**Maru2022 label**

* ready%3:00:00:: (ready.a.01) - completely prepared or in condition for immediate action or use or
  progress Examples: get ready | she is ready to resign

**Reviewer verdicts**

* **Robert Farren (RF)**
  * ready%5:00:01:available:00 (ready.s.01) - (of especially money) immediately available Examples:
    he seems to have ample ready money | a ready source of cash
  * Comment: This attributive sense of "ready" seems quite distinct from the more common predicative
    senses (like sense 1 above). It corresponds colosely to this, form the Concise Oxford:
    "immediate, quick, or prompt". Sense 2 is close.
* **Patrick White (PW)**
  * ready%5:00:00:prepared:00 (ready.s.03) - made suitable and available for immediate use Examples:
    dinner is ready
* **Penny Hands (PH)**
  * Cannot answer: inventory inadequate
  * Note: While sense 5 was the most obvious choice, the definition describes someone's mind rather
    than something they might say. Sense 2 works better from the point of view of having something
    clever ready to say, and I would have opted for that if the definition were worded differently,
    perhaps as: 'available to be used easily and immediately', without the mention of 'especially
    money'. Examples might be 'a ready supply', 'a ready answer' and 'ready cash'.

**Agreement:** Fine: All three disagree; Glite: Exactly two agree; Maru2022 fine support: 0/3;
Maru2022 Glite support: 2/3.

### F21. senseval3.d000.s011.t004

**Lemma/POS/source:** `occasion` / `NOUN` / `senseval3` (`senseval3.d000`)

**Sentence:** It was blurred, after two hours of steady drinking, but the **[occasion]** of it came
back to him.

**Maru2022 label**

* occasion%1:26:00:: (occasion.n.05) - an opportunity to do something Examples: there was never an
  occasion for her to demonstrate her skill

**Reviewer verdicts**

* **Robert Farren (RF)**
  * occasion%1:16:00:: (occasion.n.03) - reason Examples: there was no occasion for complaint
* **Patrick White (PW)**
  * occasion%1:11:00:: (juncture.n.01) - an event that occurs at a critical time Examples: at such
    junctures he always had an impulse to leave | it was needed only on special occasions
* **Penny Hands (PH)**
  * occasion%1:28:00:: (occasion.n.04) - the time of a particular event Examples: on the occasion of
    his 60th birthday
  * Comment: The example at sense 4 is distracting because it mentions a special occasion (60th
    birthday), which is sense 1. If you read sense 4 without its example, it works perfectly well
    for the use we have in the text – a particular time when something happens. (I was close to
    opting for 'Inventory is inadequate', but in the end, went with the sense 4 definition and tried
    to ignore the example.)

**Agreement:** Fine: All three disagree; Glite: Exactly two agree; Maru2022 fine support: 0/3;
Maru2022 Glite support: 2/3.

### F22. senseval3.d000.s021.t003

**Lemma/POS/source:** `time` / `NOUN` / `senseval3` (`senseval3.d000`)

**Sentence:** Haney had n't given it much thought at the **[time]**.

**Maru2022 label**

* time%1:11:00:: (time.n.01) - an instance or single occasion for some event Examples: this time he
  succeeded | he called four times

**Reviewer verdicts**

* **Robert Farren (RF)**
  * time%1:11:00:: (time.n.01) - an instance or single occasion for some event Examples: this time
    he succeeded | he called four times
* **Patrick White (PW)**
  * Cannot answer: inventory inadequate
  * Note: "at the time" is a fixed phrase meaning at that time in the past when something happened
* **Penny Hands (PH)**
  * time%1:28:00:: (time.n.03) - an indefinite period (usually marked by specific attributes or
    activities) Examples: he waited a long time | the time of year for planting
  * Comment: Not sense 1, because that refers to the use of 'time' in every time, next time, this
    time, etc.

**Agreement:** Fine: All three disagree; Glite: Exactly two agree; Maru2022 fine support: 1/3;
Maru2022 Glite support: 2/3.

### F23. senseval3.d000.s031.t002

**Lemma/POS/source:** `realize` / `VERB` / `senseval3` (`senseval3.d000`)

**Sentence:** When he finally got the coughing under control, he **[realized]** that Pete -LRB- all
he gave was his first name -RRB- was still waiting for an answer -- he did n't even seem to wink as
he continued to stare.

**Maru2022 label**

* realize%2:31:00:: (understand.v.02) - perceive (an idea or situation) mentally Examples: Now I
  see! | I just can't see your point

**Reviewer verdicts**

* **Robert Farren (RF)**
  * realize%2:31:00:: (understand.v.02) - perceive (an idea or situation) mentally Examples: Now I
    see! | I just can't see your point
* **Patrick White (PW)**
  * realize%2:31:01:: (recognize.v.02) - be fully aware or cognizant of
* **Penny Hands (PH)**
  * Cannot answer: inventory inadequate
  * Note: Sense 1 definition should include the option ' ... /become'. It should read 'be/become
    fully aware or cognizant of'.

**Agreement:** Fine: All three disagree; Glite: Exactly two agree; Maru2022 fine support: 1/3;
Maru2022 Glite support: 2/3.

### F24. senseval3.d000.s116.t001

**Lemma/POS/source:** `encourage` / `VERB` / `senseval3` (`senseval3.d000`)

**Sentence:** Haney did n't want to **[encourage]** his company, but felt he ought to buy him a
drink anyhow, to prevent possible trouble.

**Maru2022 label**

* encourage%2:32:00:: (encourage.v.03) - spur on Examples: His financial success encouraged him to
  look for a wife

**Reviewer verdicts**

* **Robert Farren (RF)**
  * encourage%2:32:00:: (encourage.v.03) - spur on Examples: His financial success encouraged him to
    look for a wife
* **Patrick White (PW)**
  * Cannot answer: inventory inadequate
  * Note: This usage does not fit neatly with the WordNet senses. It is close to sense 2 but the
    object is not a person.
* **Penny Hands (PH)**
  * encourage%2:41:00:: (promote.v.01) - contribute to the progress or growth of Examples: I am
    promoting the use of computers in the classroom
  * Comment: Senses 2 and 3 refer to situations where someone lacks something such as success or
    confidence, and needs someone or something to push them to do it. In the text, the author's
    companion isn't shy, and doesn't need to be coaxed or boosted with helpful encouragement. So I
    opted for sense 1, which seems to be talking about making something (in this case, Pete's
    company) more likely to develop.

**Agreement:** Fine: All three disagree; Glite: All three disagree; Maru2022 fine support: 1/3;
Maru2022 Glite support: 1/3.

### F25. senseval3.d000.s119.t004

**Lemma/POS/source:** `talk` / `VERB` / `senseval3` (`senseval3.d000`)

**Sentence:** To break the uncomfortable silence, Haney began to **[talk]**.

**Maru2022 label**

* talk%2:32:03:: (speak.v.03) - use language Examples: the baby talks already | the prisoner won't
  speak

**Reviewer verdicts**

* **Robert Farren (RF)**
  * talk%2:32:03:: (speak.v.03) - use language Examples: the baby talks already | the prisoner won't
    speak
  * Comment: Sense 3 is the nearest fit, but it's not great. In this sentence "talk" seems to mean
    something like "talk to fill the silence, make small-talk".
* **Patrick White (PW)**
  * talk%2:32:01:: (talk.v.01) - exchange thoughts; talk with Examples: We often talk business |
    Actions talk louder than words
* **Penny Hands (PH)**
  * talk%2:32:00:: (talk.v.02) - express in speech Examples: She talks a lot of nonsense | This
    depressed patient does not verbalize
  * Comment: I rejected sense 1 because it suggests interaction. (There is none apparent in the
    text.) Sense 3 seems to refer to the ability or willingness to speak. Sense 2 (which I opted
    for) is about simply producing speech. One reservation I have about sense 2 is that the
    definition seems to suggest it only covers a transitive use – I would prefer 'express (oneself)
    in speech' – whereas in the text, 'talk' is intransitive. However, sense 2's second example is
    intransitive, so I went with it.

**Agreement:** Fine: All three disagree; Glite: All three agree; Maru2022 fine support: 1/3;
Maru2022 Glite support: 3/3.

### F26. senseval3.d001.s045.t002

**Lemma/POS/source:** `reveal` / `VERB` / `senseval3` (`senseval3.d001`)

**Sentence:** A cross-state econometric investigation, furthermore, **[reveals]** that, holding
other factors constant, the difference between a state's major - party vote going to the Republican
gubernatorial candidate and the Republican share of the lower state house is a positive function of
the state tax rate.

**Maru2022 label**

* reveal%2:39:00:: (uncover.v.01) - make visible Examples: Summer brings out bright clothes | He
  brings out the best in her

**Reviewer verdicts**

* **Robert Farren (RF)**
  * reveal%2:39:00:: (uncover.v.01) - make visible Examples: Summer brings out bright clothes | He
    brings out the best in her
* **Patrick White (PW)**
  * reveal%2:32:00:: (unwrap.v.02) - make known to the public information that was previously known
    only to a few people or that was meant to be kept a secret Examples: The auction house would not
    disclose the price at which the van Gogh had sold | The actress won't reveal how old she is
* **Penny Hands (PH)**
  * Cannot answer: inventory inadequate
  * Note: Sense 2 is close but it is too restrictive. It would work better if it simply said 'make
    known to someone'

**Agreement:** Fine: All three disagree; Glite: Exactly two agree; Maru2022 fine support: 1/3;
Maru2022 Glite support: 2/3.

### F27. senseval3.d002.s086.t000

**Lemma/POS/source:** `thing` / `NOUN` / `senseval3` (`senseval3.d002`)

**Sentence:** Then as **[things]** got rougher, we ran for the door and spent the next few minutes
outside watching the brick sidewalk under our feet oozing up and down, and the flowers waving in an
eerie rhythm.

**Maru2022 label**

* thing%1:09:02:: (matter.n.01) - a vaguely specified concern Examples: several matters to attend to
  | it is none of your affair
* thing%1:11:00:: (thing.n.05) - an event Examples: a funny thing happened on the way to the...

**Reviewer verdicts**

* **Robert Farren (RF)**
  * Cannot answer: no sense applies
  * Note: Once again, this sense means "everything in general", the status quo, the general
    situation. This sense is always plural and uncountable.
* **Patrick White (PW)**
  * thing%1:09:02:: (matter.n.01) - a vaguely specified concern Examples: several matters to attend
    to | it is none of your affair
* **Penny Hands (PH)**
  * thing%1:11:00:: (thing.n.05) - an event Examples: a funny thing happened on the way to the...
  * Comment: This one is more specific than the vague 'How are things?' or 'Things are a bit rough
    at the moment' usage because an event is now taking place.

**Agreement:** Fine: All three disagree; Glite: All three disagree; Maru2022 fine support: 0/3;
Maru2022 Glite support: 0/3.

### F28. senseval3.d002.s093.t000

**Lemma/POS/source:** `say` / `VERB` / `senseval3` (`senseval3.d002`)

**Sentence:** He **[said]** that one of the computers took a three-foot trip sliding across the
floor.

**Maru2022 label**

* say%2:32:01:: (allege.v.01) - report or maintain Examples: He alleged that he was the victim of a
  crime | He said it was too late to intervene in the war

**Reviewer verdicts**

* **Robert Farren (RF)**
  * say%2:32:01:: (allege.v.01) - report or maintain Examples: He alleged that he was the victim of
    a crime | He said it was too late to intervene in the war
* **Patrick White (PW)**
  * say%2:32:00:: (state.v.01) - express in words Examples: He said that he wanted to marry her |
    tell me what is bothering you
* **Penny Hands (PH)**
  * say%2:32:00:: (state.v.01) - express in words Examples: He said that he wanted to marry her |
    tell me what is bothering you
  * say%2:32:15:: (say.v.08) - utter aloud Examples: She said `Hello' to everyone in the office
  * Comment: Sense 8 seems to be about direct speech, i.e. a quote + a reporting verb (say). But
    there is no proof that he uttered this statement aloud; it could have been a written statement.
    That's why I also selected sense 1.

**Agreement:** Fine: All three disagree; Glite: All three agree; Maru2022 fine support: 1/3;
Maru2022 Glite support: 3/3.

### F29. senseval3.d002.s138.t000

**Lemma/POS/source:** `quiet` / `ADJ` / `senseval3` (`senseval3.d002`)

**Sentence:** Berkeley very **[quiet]** right now.

**Maru2022 label**

* quiet%3:00:01:: (quiet.a.02) - free of noise or uproar; or making little if any sound Examples: a
  quiet audience at the concert | the room was dark and quiet

**Reviewer verdicts**

* **Robert Farren (RF)**
  * quiet%3:00:01:: (quiet.a.02) - free of noise or uproar; or making little if any sound Examples:
    a quiet audience at the concert | the room was dark and quiet
  * quiet%3:00:02:: (quiet.a.01) - characterized by an absence or near absence of agitation or
    activity Examples: a quiet life | a quiet throng of onlookers
  * Comment: Both senses are equally plausible, and the extra context provided by preceding and
    following sentences doesn't clarify which sense is meant.
* **Patrick White (PW)**
  * quiet%3:00:02:: (quiet.a.01) - characterized by an absence or near absence of agitation or
    activity Examples: a quiet life | a quiet throng of onlookers
* **Penny Hands (PH)**
  * quiet%3:00:01:: (quiet.a.02) - free of noise or uproar; or making little if any sound Examples:
    a quiet audience at the concert | the room was dark and quiet
  * Comment: Sense 2 seems to be more about the absence of noise and gives the example of a place
    being quiet (the text is also talking about a place). Sense 1 is more about a lack of unrest,
    and doesn't mention sound at all.

**Agreement:** Fine: All three disagree; Glite: All three agree; Maru2022 fine support: 1/3;
Maru2022 Glite support: 3/3.
