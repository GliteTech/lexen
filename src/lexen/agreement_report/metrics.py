"""Compute agreement report metrics."""

from __future__ import annotations

from collections import Counter, defaultdict
from itertools import combinations
from pathlib import Path

from lexen.agreement_report.data import (
    cannot_answer_reasons,
    chosen_sense_keys,
    collect_required_sense_keys,
    context_sentence_text,
    item_id,
    load_glite_mapping,
    load_reviews,
    load_selection_records,
    maru_sense_keys,
    report_items_from_selection_records,
    review_comment,
    review_note,
    reviews_by_id,
    target_sentence_tokens,
    target_token_index,
)
from lexen.agreement_report.models import (
    AgreementLevel,
    AgreementMetrics,
    AppendixGroup,
    AppendixGroupID,
    CannotAnswerMetrics,
    CountPercent,
    GliteCoverage,
    Granularity,
    GroupAgreement,
    ItemAgreement,
    LabelCode,
    LabelValue,
    NoConsensusMetrics,
    NoConsensusSampleItem,
    PairwiseAgreement,
    ReportData,
    ReportMetrics,
    ReviewerID,
    ReviewerMaruRelation,
    ReviewerPair,
    ReviewerVerdictShape,
    SenseMetadata,
    VotePattern,
)
from lexen.models import JsonObject, SelectionRecord, SenseKey
from lexen.paths import (
    CANONICAL_ANNOTATORS,
)

CANNOT_ANSWER_CODE: LabelCode = "cannot_answer"
EMPTY_ANSWER_CODE: LabelCode = "empty_answer"
SENSE_LABEL_PREFIX: str = "sense:"
GLITE_LABEL_PREFIX: str = "glite:"
UNMAPPED_PREFIX: str = "unmapped:"
INPUT_DEFECTIVE_REASON: str = "__input_defective__"

RELATION_ALL_THREE_GOLD: str = "all_three_agree_and_gold"
RELATION_ALL_THREE_DIFFERENT: str = "all_three_agree_but_different"
RELATION_EXACTLY_TWO_GOLD: str = "exactly_two_agree_and_gold"
RELATION_EXACTLY_TWO_DIFFERENT: str = "exactly_two_agree_but_different"
RELATION_ALL_DIFFER: str = "all_three_disagree"

APPENDIX_GROUP_DETAILS: dict[AppendixGroupID, tuple[str, str]] = {
    AppendixGroupID.ALL_THREE_MARU2022: (
        "Appendix A. All three reviewers selected the Maru2022 sense",
        "Every reviewer independently chose exactly the same fine-grained WordNet label as "
        "the Maru2022 source label.",
    ),
    AppendixGroupID.ALL_THREE_CORRECTION: (
        "Appendix B. All three reviewers selected the same correction",
        "Every reviewer independently chose the same fine-grained WordNet label, and that "
        "label differs from the Maru2022 source label.",
    ),
    AppendixGroupID.ALL_THREE_UNANSWERABLE: (
        "Appendix C. All three reviewers judged the item unanswerable",
        "All reviewers used a cannot-answer judgement rather than choosing a WordNet sense. "
        "These items are removed from the lexEN benchmark.",
    ),
    AppendixGroupID.TWO_SAME_SENSE: (
        "Appendix D. Two reviewers selected the same sense",
        "Exactly two reviewers agreed on a fine-grained WordNet label and the third reviewer "
        "gave a different answer.",
    ),
    AppendixGroupID.TWO_UNANSWERABLE: (
        "Appendix E. Two reviewers judged the item unanswerable",
        "Exactly two reviewers used cannot-answer and the third reviewer selected a sense. "
        "These items are removed from the lexEN benchmark.",
    ),
    AppendixGroupID.ALL_DIFFER: (
        "Appendix F. All three reviewers disagreed",
        "The three reviewers produced three different fine-grained answers. These items are "
        "removed from the lexEN benchmark.",
    ),
}

NO_CONSENSUS_SAMPLE_NOTES: dict[str, tuple[str, str]] = {
    "semeval2013.d000.s019.t000": (
        "Remove",
        "WordNet lacks the figurative strategic-manoeuvring sense of game in this context.",
    ),
    "semeval2013.d009.s022.t000": (
        "Remove",
        "The US ideological conservative reading is not cleanly captured by the party/member "
        "senses.",
    ),
    "semeval2015.d001.s009.t007": (
        "Remove or adjudicate",
        "The computer-input sense is missing or underspecified, and Maru2022 support is weak.",
    ),
    "semeval2015.d002.s011.t008": (
        "Remove or adjudicate",
        "The context likely means the way work is organised, while the available labels diverge.",
    ),
    "semeval2015.d003.s009.t014": (
        "Remove from fine scoring",
        "The reviewers differ at fine WordNet level even though Glite coarsening makes them agree.",
    ),
    "semeval2015.d003.s012.t002": (
        "Remove",
        "The functional/location use of act in the central nervous system does not map cleanly.",
    ),
    "senseval2.d001.s015.t001": (
        "Remove",
        "The gene-copy context for make proteins lacks a clean production sense in the inventory.",
    ),
    "senseval2.d001.s026.t007": (
        "Remove from fine scoring",
        "The fine-grained distinction is underdetermined even though coarse meaning is closer.",
    ),
    "senseval2.d001.s041.t005": (
        "Remove",
        "Specific genes means particular or individual genes, and reviewers did not converge.",
    ),
    "senseval2.d001.s057.t002": (
        "Remove",
        "Turned his attention to is a fixed research-focus use, not a reliable fine sense.",
    ),
    "senseval2.d002.s004.t002": (
        "Remove or adjudicate",
        "Dominate means strongly influence or prevail over, but the inventory split is unstable.",
    ),
    "senseval2.d002.s055.t001": (
        "Remove or adjudicate",
        "The intended involvement reading mixes participation and control, producing ambiguity.",
    ),
    "senseval3.d000.s002.t001": (
        "Remove",
        "Ready answer means prompt or available answer; the inventory does not fit cleanly.",
    ),
    "senseval3.d000.s011.t004": (
        "Remove or adjudicate",
        "All three choices are plausible but different, and Maru2022 has no support.",
    ),
    "senseval3.d000.s021.t003": (
        "Remove",
        "At the time is a fixed expression and does not support reliable fine-grained tagging.",
    ),
    "senseval3.d000.s031.t002": (
        "Remove or adjudicate",
        "The become-aware nuance exposes a WordNet definition boundary problem.",
    ),
    "senseval3.d000.s116.t001": (
        "Remove",
        "Encourage his company means make more likely or promote, not a clean available sense.",
    ),
    "senseval3.d001.s045.t002": (
        "Remove",
        "Investigation reveals mixes make-known and show evidence; WordNet is too narrow here.",
    ),
    "senseval3.d002.s086.t000": (
        "Remove",
        "Things got rougher uses thing as a general situation marker, not a clean WordNet sense.",
    ),
    "senseval3.d002.s138.t000": (
        "Remove from fine scoring",
        "Quiet has noise versus activity ambiguity; reviewers agree only after Glite coarsening.",
    ),
}


def percent_count(*, count: int, total: int) -> CountPercent:
    if total == 0:
        return CountPercent(count=count, percent=0.0)
    return CountPercent(count=count, percent=count * 100.0 / total)


def sorted_unique(*, values: list[str]) -> list[str]:
    return sorted(set(values))


def label_from_senses(
    *,
    sense_keys: list[SenseKey],
    cannot_answer: list[str],
    glite_mapping: dict[SenseKey, str],
    granularity: Granularity,
) -> LabelValue:
    normalized_senses = sorted_unique(values=sense_keys)
    normalized_cannot = sorted_unique(values=cannot_answer)
    if len(normalized_senses) == 0 and len(normalized_cannot) > 0:
        return LabelValue(
            code=CANNOT_ANSWER_CODE,
            display="cannot answer",
            sense_keys=[],
            coarse_keys=[],
            cannot_answer=normalized_cannot,
        )
    if len(normalized_senses) == 0:
        return LabelValue(
            code=EMPTY_ANSWER_CODE,
            display="empty answer",
            sense_keys=[],
            coarse_keys=[],
            cannot_answer=normalized_cannot,
        )

    coarse_keys = [
        glite_mapping.get(sense_key, f"{UNMAPPED_PREFIX}{sense_key}")
        for sense_key in normalized_senses
    ]
    normalized_coarse = sorted_unique(values=coarse_keys)
    if granularity is Granularity.FINE:
        code = SENSE_LABEL_PREFIX + "|".join(normalized_senses)
        display = ", ".join(normalized_senses)
    else:
        code = GLITE_LABEL_PREFIX + "|".join(normalized_coarse)
        display = ", ".join(normalized_coarse)
    return LabelValue(
        code=code,
        display=display,
        sense_keys=normalized_senses,
        coarse_keys=normalized_coarse,
        cannot_answer=normalized_cannot,
    )


def vote_pattern(*, label_codes: list[LabelCode]) -> VotePattern:
    counts: Counter[LabelCode] = Counter(label_codes)
    if len(counts) == 1:
        return VotePattern(
            level=AgreementLevel.ALL_THREE,
            majority_code=label_codes[0],
        )
    if len(counts) == 2:
        majority_code = counts.most_common(1)[0][0]
        return VotePattern(
            level=AgreementLevel.EXACTLY_TWO,
            majority_code=majority_code,
        )
    return VotePattern(
        level=AgreementLevel.ALL_DIFFER,
        majority_code=None,
    )


def majority_sense_keys(
    *,
    pattern: VotePattern,
    labels_by_reviewer: dict[ReviewerID, LabelValue],
) -> list[SenseKey]:
    if pattern.majority_code is None or not pattern.majority_code.startswith(SENSE_LABEL_PREFIX):
        return []
    for label in labels_by_reviewer.values():
        if label.code == pattern.majority_code:
            return label.sense_keys
    raise ValueError(f"majority label missing from reviewer labels: {pattern.majority_code}")


def cohen_kappa(
    *,
    left_labels: list[LabelCode],
    right_labels: list[LabelCode],
) -> float:
    if len(left_labels) != len(right_labels):
        raise ValueError("left and right labels must have equal length")
    total = len(left_labels)
    if total == 0:
        return 0.0
    observed = (
        sum(1 for index, left_label in enumerate(left_labels) if left_label == right_labels[index])
        / total
    )
    left_counts: Counter[LabelCode] = Counter(left_labels)
    right_counts: Counter[LabelCode] = Counter(right_labels)
    categories = set(left_counts) | set(right_counts)
    expected = sum(
        (left_counts[category] / total) * (right_counts[category] / total)
        for category in categories
    )
    if expected == 1.0:
        return 1.0 if observed == 1.0 else 0.0
    return (observed - expected) / (1.0 - expected)


def fleiss_kappa(*, label_rows: list[list[LabelCode]]) -> float:
    if len(label_rows) == 0:
        return 0.0
    raters_per_item = len(label_rows[0])
    if raters_per_item < 2:
        raise ValueError("Fleiss kappa requires at least two raters")
    category_counts: Counter[LabelCode] = Counter()
    agreement_sum = 0.0
    for labels in label_rows:
        if len(labels) != raters_per_item:
            raise ValueError("all Fleiss rows must have the same number of labels")
        counts: Counter[LabelCode] = Counter(labels)
        category_counts.update(labels)
        agreement_sum += sum(count * (count - 1) for count in counts.values()) / (
            raters_per_item * (raters_per_item - 1)
        )
    item_count = len(label_rows)
    p_bar = agreement_sum / item_count
    total_ratings = item_count * raters_per_item
    p_e = sum(
        (count / total_ratings) * (count / total_ratings) for count in category_counts.values()
    )
    if p_e == 1.0:
        return 1.0 if p_bar == 1.0 else 0.0
    return (p_bar - p_e) / (1.0 - p_e)


def pairwise_agreements(
    *,
    item_agreements: list[ItemAgreement],
    granularity: Granularity,
    reviewers: list[ReviewerID],
) -> list[PairwiseAgreement]:
    output: list[PairwiseAgreement] = []
    for left, right in combinations(reviewers, 2):
        left_labels: list[LabelCode] = []
        right_labels: list[LabelCode] = []
        for item in item_agreements:
            if granularity is Granularity.FINE:
                left_labels.append(item.reviewer_fine[left].code)
                right_labels.append(item.reviewer_fine[right].code)
            else:
                left_labels.append(item.reviewer_glite[left].code)
                right_labels.append(item.reviewer_glite[right].code)
        total = len(left_labels)
        matches = sum(
            1 for index, left_label in enumerate(left_labels) if left_label == right_labels[index]
        )
        output.append(
            PairwiseAgreement(
                granularity=granularity,
                pair=ReviewerPair(left=left, right=right),
                matching_items=matches,
                total_items=total,
                raw_agreement=matches * 100.0 / total,
                cohen_kappa=cohen_kappa(
                    left_labels=left_labels,
                    right_labels=right_labels,
                ),
            )
        )
    return output


def relationship_key(
    *,
    pattern: VotePattern,
    majority_code: LabelCode | None,
    gold_code: LabelCode,
) -> str:
    if pattern.level is AgreementLevel.ALL_DIFFER:
        return RELATION_ALL_DIFFER
    if pattern.level is AgreementLevel.ALL_THREE and majority_code == gold_code:
        return RELATION_ALL_THREE_GOLD
    if pattern.level is AgreementLevel.ALL_THREE:
        return RELATION_ALL_THREE_DIFFERENT
    if pattern.level is AgreementLevel.EXACTLY_TWO and majority_code == gold_code:
        return RELATION_EXACTLY_TWO_GOLD
    return RELATION_EXACTLY_TWO_DIFFERENT


def agreement_metrics(
    *,
    item_agreements: list[ItemAgreement],
    granularity: Granularity,
    reviewers: list[ReviewerID],
) -> AgreementMetrics:
    total = len(item_agreements)
    level_counts_raw: Counter[AgreementLevel] = Counter()
    relationship_counts_raw: Counter[str] = Counter()
    gold_support_counts_raw: Counter[int] = Counter()
    label_rows: list[list[LabelCode]] = []
    all_three_agree_and_gold = 0
    exactly_two_agree_and_gold = 0
    for item in item_agreements:
        if granularity is Granularity.FINE:
            labels = [item.reviewer_fine[reviewer].code for reviewer in reviewers]
            pattern = VotePattern(
                level=item.fine_level,
                majority_code=item.fine_majority_code,
            )
            gold_code = item.maru_fine.code
            gold_support = item.fine_gold_support
        else:
            labels = [item.reviewer_glite[reviewer].code for reviewer in reviewers]
            pattern = VotePattern(
                level=item.glite_level,
                majority_code=item.glite_majority_code,
            )
            gold_code = item.maru_glite.code
            gold_support = item.glite_gold_support
        label_rows.append(labels)
        level_counts_raw[pattern.level] += 1
        gold_support_counts_raw[gold_support] += 1
        relation = relationship_key(
            pattern=pattern,
            majority_code=pattern.majority_code,
            gold_code=gold_code,
        )
        relationship_counts_raw[relation] += 1
        if relation == RELATION_ALL_THREE_GOLD:
            all_three_agree_and_gold += 1
        if relation == RELATION_EXACTLY_TWO_GOLD:
            exactly_two_agree_and_gold += 1
    level_counts = {
        level: percent_count(count=level_counts_raw[level], total=total) for level in AgreementLevel
    }
    gold_support_counts = {
        support_count: percent_count(
            count=gold_support_counts_raw[support_count],
            total=total,
        )
        for support_count in [3, 2, 1, 0]
    }
    relationship_counts = {
        relation: percent_count(count=relationship_counts_raw[relation], total=total)
        for relation in [
            RELATION_ALL_THREE_GOLD,
            RELATION_ALL_THREE_DIFFERENT,
            RELATION_EXACTLY_TWO_GOLD,
            RELATION_EXACTLY_TWO_DIFFERENT,
            RELATION_ALL_DIFFER,
        ]
    }
    return AgreementMetrics(
        granularity=granularity,
        total_items=total,
        level_counts=level_counts,
        all_three_agree_and_gold=percent_count(
            count=all_three_agree_and_gold,
            total=total,
        ),
        exactly_two_agree_and_gold=percent_count(
            count=exactly_two_agree_and_gold,
            total=total,
        ),
        gold_support_counts=gold_support_counts,
        relationship_counts=relationship_counts,
        fleiss_kappa=fleiss_kappa(label_rows=label_rows),
        pairwise=pairwise_agreements(
            item_agreements=item_agreements,
            granularity=granularity,
            reviewers=reviewers,
        ),
    )


def build_item_agreements(
    *,
    items: list[JsonObject],
    reviews: list[JsonObject],
    glite_mapping: dict[SenseKey, str],
    reviewers: list[ReviewerID],
) -> list[ItemAgreement]:
    review_index = reviews_by_id(reviews=reviews)
    output: list[ItemAgreement] = []
    for item in items:
        current_item_id = item_id(item=item)
        review = review_index[current_item_id]
        maru_fine = label_from_senses(
            sense_keys=maru_sense_keys(item=item),
            cannot_answer=[],
            glite_mapping=glite_mapping,
            granularity=Granularity.FINE,
        )
        maru_glite = label_from_senses(
            sense_keys=maru_sense_keys(item=item),
            cannot_answer=[],
            glite_mapping=glite_mapping,
            granularity=Granularity.GLITE,
        )
        reviewer_fine: dict[ReviewerID, LabelValue] = {}
        reviewer_glite: dict[ReviewerID, LabelValue] = {}
        reviewer_notes: dict[ReviewerID, str | None] = {}
        reviewer_comments: dict[ReviewerID, str | None] = {}
        for reviewer in reviewers:
            keys = chosen_sense_keys(review=review, reviewer=reviewer)
            reasons = cannot_answer_reasons(review=review, reviewer=reviewer)
            reviewer_notes[reviewer] = review_note(review=review, reviewer=reviewer)
            reviewer_comments[reviewer] = review_comment(review=review, reviewer=reviewer)
            reviewer_fine[reviewer] = label_from_senses(
                sense_keys=keys,
                cannot_answer=reasons,
                glite_mapping=glite_mapping,
                granularity=Granularity.FINE,
            )
            reviewer_glite[reviewer] = label_from_senses(
                sense_keys=keys,
                cannot_answer=reasons,
                glite_mapping=glite_mapping,
                granularity=Granularity.GLITE,
            )
        fine_pattern = vote_pattern(
            label_codes=[reviewer_fine[reviewer].code for reviewer in reviewers]
        )
        glite_pattern = vote_pattern(
            label_codes=[reviewer_glite[reviewer].code for reviewer in reviewers]
        )
        output.append(
            ItemAgreement(
                item_id=current_item_id,
                lemma=str(item["lemma"]),
                pos=str(item["pos"]),
                source_dataset=str(item["source_dataset"]),
                document_id=str(item["document_id"]),
                target_text=str(item["target"]["text"]),
                sentence_text=context_sentence_text(item=item),
                target_sentence_tokens=target_sentence_tokens(item=item),
                target_token_index=target_token_index(item=item),
                maru_fine=maru_fine,
                maru_glite=maru_glite,
                lexen_gold_keys=majority_sense_keys(
                    pattern=fine_pattern,
                    labels_by_reviewer=reviewer_fine,
                ),
                reviewer_fine=reviewer_fine,
                reviewer_glite=reviewer_glite,
                reviewer_notes=reviewer_notes,
                reviewer_comments=reviewer_comments,
                fine_level=fine_pattern.level,
                glite_level=glite_pattern.level,
                fine_gold_support=sum(
                    1 for reviewer in reviewers if reviewer_fine[reviewer].code == maru_fine.code
                ),
                glite_gold_support=sum(
                    1 for reviewer in reviewers if reviewer_glite[reviewer].code == maru_glite.code
                ),
                fine_majority_code=fine_pattern.majority_code,
                glite_majority_code=glite_pattern.majority_code,
            )
        )
    return output


def verdict_shapes(
    *,
    reviews: list[JsonObject],
    reviewers: list[ReviewerID],
) -> list[ReviewerVerdictShape]:
    output: list[ReviewerVerdictShape] = []
    for reviewer in reviewers:
        single = 0
        multi = 0
        cannot = 0
        comments = 0
        notes = 0
        for review in reviews:
            keys = chosen_sense_keys(review=review, reviewer=reviewer)
            reasons = cannot_answer_reasons(review=review, reviewer=reviewer)
            comment = review_comment(review=review, reviewer=reviewer)
            note = review_note(review=review, reviewer=reviewer)
            if len(keys) == 1:
                single += 1
            if len(keys) > 1:
                multi += 1
            if len(reasons) > 0:
                cannot += 1
            if comment is not None and len(comment.strip()) > 0:
                comments += 1
            if note is not None and len(note.strip()) > 0:
                notes += 1
        output.append(
            ReviewerVerdictShape(
                reviewer=reviewer,
                single_sense_items=single,
                multi_sense_items=multi,
                cannot_answer_items=cannot,
                comment_items=comments,
                note_items=notes,
            )
        )
    return output


def relation_between_reviewer_and_maru(
    *,
    reviewer_label: LabelValue,
    gold_label: LabelValue,
) -> str:
    if len(reviewer_label.sense_keys) == 0 and len(reviewer_label.cannot_answer) > 0:
        return "unanswerable"
    reviewer_keys = set(reviewer_label.sense_keys)
    gold_keys = set(gold_label.sense_keys)
    if reviewer_label.code.startswith(GLITE_LABEL_PREFIX):
        reviewer_keys = set(reviewer_label.coarse_keys)
        gold_keys = set(gold_label.coarse_keys)
    if reviewer_keys == gold_keys:
        return "accept_exact"
    if len(gold_keys) > 0 and gold_keys < reviewer_keys:
        return "accept_plus_extra"
    if len(reviewer_keys & gold_keys) > 0:
        return "partial_overlap"
    return "replace"


def maru_relations(
    *,
    item_agreements: list[ItemAgreement],
    reviewers: list[ReviewerID],
) -> list[ReviewerMaruRelation]:
    output: list[ReviewerMaruRelation] = []
    for granularity in [Granularity.FINE, Granularity.GLITE]:
        for reviewer in reviewers:
            counts: Counter[str] = Counter()
            for item in item_agreements:
                if granularity is Granularity.FINE:
                    reviewer_label = item.reviewer_fine[reviewer]
                    gold_label = item.maru_fine
                else:
                    reviewer_label = item.reviewer_glite[reviewer]
                    gold_label = item.maru_glite
                relation = relation_between_reviewer_and_maru(
                    reviewer_label=reviewer_label,
                    gold_label=gold_label,
                )
                counts[relation] += 1
            total = len(item_agreements)
            output.append(
                ReviewerMaruRelation(
                    granularity=granularity,
                    reviewer=reviewer,
                    accept_exact=percent_count(count=counts["accept_exact"], total=total),
                    accept_plus_extra=percent_count(
                        count=counts["accept_plus_extra"],
                        total=total,
                    ),
                    partial_overlap=percent_count(
                        count=counts["partial_overlap"],
                        total=total,
                    ),
                    replace=percent_count(count=counts["replace"], total=total),
                    unanswerable=percent_count(count=counts["unanswerable"], total=total),
                )
            )
    return output


def group_agreement(
    *,
    group_kind: str,
    group_name: str,
    items: list[ItemAgreement],
) -> GroupAgreement:
    total = len(items)
    fine_counts: Counter[AgreementLevel] = Counter(item.fine_level for item in items)
    glite_counts: Counter[AgreementLevel] = Counter(item.glite_level for item in items)
    return GroupAgreement(
        group_kind=group_kind,
        group_name=group_name,
        total_items=total,
        fine_all_three=percent_count(count=fine_counts[AgreementLevel.ALL_THREE], total=total),
        fine_exactly_two=percent_count(count=fine_counts[AgreementLevel.EXACTLY_TWO], total=total),
        fine_all_differ=percent_count(count=fine_counts[AgreementLevel.ALL_DIFFER], total=total),
        glite_all_three=percent_count(count=glite_counts[AgreementLevel.ALL_THREE], total=total),
        glite_exactly_two=percent_count(
            count=glite_counts[AgreementLevel.EXACTLY_TWO], total=total
        ),
        glite_all_differ=percent_count(count=glite_counts[AgreementLevel.ALL_DIFFER], total=total),
    )


def grouped_agreements(
    *,
    item_agreements: list[ItemAgreement],
    group_kind: str,
    max_groups: int | None,
) -> list[GroupAgreement]:
    grouped: defaultdict[str, list[ItemAgreement]] = defaultdict(list)
    for item in item_agreements:
        if group_kind == "pos":
            key = item.pos
        elif group_kind == "source":
            key = item.source_dataset
        elif group_kind == "headword":
            key = item.lemma
        else:
            raise ValueError(f"unsupported group kind {group_kind}")
        grouped[key].append(item)
    groups = [
        group_agreement(group_kind=group_kind, group_name=name, items=items)
        for name, items in grouped.items()
    ]
    groups.sort(key=lambda group: (-group.total_items, group.group_name))
    if max_groups is None:
        return groups
    return groups[:max_groups]


def cannot_answer_metrics(
    *,
    item_agreements: list[ItemAgreement],
    reviews: list[JsonObject],
    reviewers: list[ReviewerID],
) -> CannotAnswerMetrics:
    reason_counts: dict[ReviewerID, dict[str, int]] = {}
    for reviewer in reviewers:
        counts: Counter[str] = Counter()
        for review in reviews:
            counts.update(cannot_answer_reasons(review=review, reviewer=reviewer))
        reason_counts[reviewer] = dict(sorted(counts.items()))
    at_least_one = 0
    exactly_one = 0
    exactly_two = 0
    at_least_two = 0
    all_three = 0
    at_least_two_reason_item_counts: Counter[str] = Counter()
    input_defective_by_document: Counter[str] = Counter()
    cannot_answer_by_document_support: defaultdict[int, Counter[str]] = defaultdict(Counter)
    input_defective_by_document_support: defaultdict[int, Counter[str]] = defaultdict(Counter)
    agreement_by_id = {item.item_id: item for item in item_agreements}
    for review in reviews:
        current_item_id = str(review["item_id"])
        document_id = agreement_by_id[current_item_id].document_id
        cannot_reasons_by_reviewer = {
            reviewer: cannot_answer_reasons(review=review, reviewer=reviewer)
            for reviewer in reviewers
        }
        cannot_flags = [len(reasons) > 0 for reasons in cannot_reasons_by_reviewer.values()]
        cannot_count = sum(cannot_flags)
        if cannot_count > 0:
            cannot_answer_by_document_support[cannot_count][document_id] += 1
        if any(cannot_flags):
            at_least_one += 1
        if cannot_count == 1:
            exactly_one += 1
        if cannot_count == 2:
            exactly_two += 1
        if cannot_count >= 2:
            at_least_two += 1
            item_reasons = {
                reason for reasons in cannot_reasons_by_reviewer.values() for reason in reasons
            }
            at_least_two_reason_item_counts.update(item_reasons)
        if cannot_count == len(reviewers):
            all_three += 1
        input_defective_count = sum(
            INPUT_DEFECTIVE_REASON in reasons for reasons in cannot_reasons_by_reviewer.values()
        )
        has_input_defective = input_defective_count > 0
        if input_defective_count > 0:
            input_defective_by_document_support[input_defective_count][document_id] += 1
        if has_input_defective:
            input_defective_by_document[document_id] += 1
    return CannotAnswerMetrics(
        reason_counts_by_reviewer=reason_counts,
        at_least_one_unanswerable=at_least_one,
        exactly_one_unanswerable=exactly_one,
        exactly_two_unanswerable=exactly_two,
        at_least_two_unanswerable=at_least_two,
        all_three_unanswerable=all_three,
        at_least_two_reason_item_counts=dict(sorted(at_least_two_reason_item_counts.items())),
        input_defective_by_document=dict(sorted(input_defective_by_document.items())),
        cannot_answer_by_document_support={
            support: dict(sorted(counts.items()))
            for support, counts in sorted(cannot_answer_by_document_support.items())
        },
        input_defective_by_document_support={
            support: dict(sorted(counts.items()))
            for support, counts in sorted(input_defective_by_document_support.items())
        },
    )


def non_empty_text_count(*, values: dict[ReviewerID, str | None]) -> int:
    return sum(1 for value in values.values() if value is not None and len(value.strip()) > 0)


def no_consensus_metrics(
    *,
    item_agreements: list[ItemAgreement],
    reviewers: list[ReviewerID],
) -> NoConsensusMetrics:
    items = [item for item in item_agreements if item.fine_level is AgreementLevel.ALL_DIFFER]
    pos_counts: Counter[str] = Counter(item.pos for item in items)
    source_counts: Counter[str] = Counter(item.source_dataset for item in items)
    fine_gold_support_counts: Counter[int] = Counter(item.fine_gold_support for item in items)
    glite_gold_support_counts: Counter[int] = Counter(item.glite_gold_support for item in items)
    glite_level_counts: Counter[AgreementLevel] = Counter(item.glite_level for item in items)
    cannot_answer_vote_counts: Counter[int] = Counter(
        sum(1 for reviewer in reviewers if len(item.reviewer_fine[reviewer].cannot_answer) > 0)
        for item in items
    )
    comment_count_distribution: Counter[int] = Counter(
        non_empty_text_count(values=item.reviewer_comments) for item in items
    )
    note_count_distribution: Counter[int] = Counter(
        non_empty_text_count(values=item.reviewer_notes) for item in items
    )

    by_id = {item.item_id: item for item in items}
    sampled_items: list[NoConsensusSampleItem] = []
    for item_id_value, (recommendation, rationale) in NO_CONSENSUS_SAMPLE_NOTES.items():
        item = by_id.get(item_id_value)
        if item is None:
            raise ValueError(f"manual no-consensus sample item missing: {item_id_value}")
        sampled_items.append(
            NoConsensusSampleItem(
                item_id=item.item_id,
                lemma=item.lemma,
                pos=item.pos,
                source_dataset=item.source_dataset,
                recommendation=recommendation,
                rationale=rationale,
            )
        )

    return NoConsensusMetrics(
        total_items=len(items),
        pos_counts=dict(sorted(pos_counts.items())),
        source_counts=dict(sorted(source_counts.items())),
        fine_gold_support_counts=dict(sorted(fine_gold_support_counts.items())),
        glite_gold_support_counts=dict(sorted(glite_gold_support_counts.items())),
        glite_level_counts=dict(
            sorted(glite_level_counts.items(), key=lambda value: value[0].value)
        ),
        cannot_answer_vote_counts=dict(sorted(cannot_answer_vote_counts.items())),
        comment_count_distribution=dict(sorted(comment_count_distribution.items())),
        note_count_distribution=dict(sorted(note_count_distribution.items())),
        sampled_items=sampled_items,
    )


def fine_non_unanimous_resolved_by_glite(
    *,
    item_agreements: list[ItemAgreement],
) -> CountPercent:
    fine_non_unanimous = [
        item for item in item_agreements if item.fine_level is not AgreementLevel.ALL_THREE
    ]
    resolved = sum(1 for item in fine_non_unanimous if item.glite_level is AgreementLevel.ALL_THREE)
    return percent_count(count=resolved, total=len(fine_non_unanimous))


def appendix_group_id(
    *,
    item: ItemAgreement,
    reviewers: list[ReviewerID],
) -> AppendixGroupID:
    if item.fine_level is AgreementLevel.ALL_THREE:
        label = item.reviewer_fine[reviewers[0]].code
        if label == CANNOT_ANSWER_CODE:
            return AppendixGroupID.ALL_THREE_UNANSWERABLE
        if label == item.maru_fine.code:
            return AppendixGroupID.ALL_THREE_MARU2022
        return AppendixGroupID.ALL_THREE_CORRECTION

    if item.fine_level is AgreementLevel.EXACTLY_TWO:
        if item.fine_majority_code == CANNOT_ANSWER_CODE:
            return AppendixGroupID.TWO_UNANSWERABLE
        return AppendixGroupID.TWO_SAME_SENSE

    return AppendixGroupID.ALL_DIFFER


def appendix_groups(
    *,
    item_agreements: list[ItemAgreement],
    reviewers: list[ReviewerID],
) -> list[AppendixGroup]:
    grouped: dict[AppendixGroupID, list[ItemAgreement]] = {
        group_id: [] for group_id in AppendixGroupID
    }
    for item in item_agreements:
        grouped[appendix_group_id(item=item, reviewers=reviewers)].append(item)

    return [
        AppendixGroup(
            group_id=group_id,
            title=APPENDIX_GROUP_DETAILS[group_id][0],
            description=APPENDIX_GROUP_DETAILS[group_id][1],
            items=grouped[group_id],
        )
        for group_id in AppendixGroupID
    ]


def sense_metadata_by_key(
    *,
    selection_records: list[SelectionRecord],
) -> dict[SenseKey, SenseMetadata]:
    metadata: dict[SenseKey, SenseMetadata] = {}
    for record in selection_records:
        for sense in record.all_wordnet_senses:
            metadata.setdefault(
                sense.sense_key,
                SenseMetadata(
                    sense_key=sense.sense_key,
                    synset_name=sense.synset_name,
                    lemma=sense.lemma,
                    pos=sense.pos,
                    definition=sense.definition,
                    examples=sense.examples,
                    synonyms=sense.synonyms,
                    in_maru_prompt=sense.in_maru_prompt,
                ),
            )
    return metadata


def build_report_data(*, repo_root: Path) -> ReportData:
    reviewers = list(CANONICAL_ANNOTATORS)
    reviews = load_reviews(repo_root=repo_root)
    selection_records = load_selection_records(repo_root=repo_root)
    items = report_items_from_selection_records(
        selection_records=selection_records,
        reviews=reviews,
    )
    required_sense_keys = collect_required_sense_keys(
        items=items,
        reviews=reviews,
        reviewers=reviewers,
    )
    glite_mapping = load_glite_mapping(
        repo_root=repo_root,
        required_sense_keys=required_sense_keys,
    )
    unmapped = sorted(required_sense_keys - set(glite_mapping))
    item_agreements = build_item_agreements(
        items=items,
        reviews=reviews,
        glite_mapping=glite_mapping,
        reviewers=reviewers,
    )
    fine = agreement_metrics(
        item_agreements=item_agreements,
        granularity=Granularity.FINE,
        reviewers=reviewers,
    )
    glite = agreement_metrics(
        item_agreements=item_agreements,
        granularity=Granularity.GLITE,
        reviewers=reviewers,
    )
    metrics = ReportMetrics(
        reviewed_items=len(item_agreements),
        fine=fine,
        glite=glite,
        verdict_shapes=verdict_shapes(reviews=reviews, reviewers=reviewers),
        maru_relations=maru_relations(
            item_agreements=item_agreements,
            reviewers=reviewers,
        ),
        pos_groups=grouped_agreements(
            item_agreements=item_agreements,
            group_kind="pos",
            max_groups=None,
        ),
        source_groups=grouped_agreements(
            item_agreements=item_agreements,
            group_kind="source",
            max_groups=None,
        ),
        headword_groups=grouped_agreements(
            item_agreements=item_agreements,
            group_kind="headword",
            max_groups=20,
        ),
        cannot_answer=cannot_answer_metrics(
            item_agreements=item_agreements,
            reviews=reviews,
            reviewers=reviewers,
        ),
        no_consensus=no_consensus_metrics(
            item_agreements=item_agreements,
            reviewers=reviewers,
        ),
        glite_coverage=GliteCoverage(
            required_sense_keys=len(required_sense_keys),
            mapped_sense_keys=len(glite_mapping),
            unmapped_sense_keys=unmapped,
        ),
        fine_non_unanimous_resolved_by_glite=fine_non_unanimous_resolved_by_glite(
            item_agreements=item_agreements,
        ),
        appendix_groups=appendix_groups(
            item_agreements=item_agreements,
            reviewers=reviewers,
        ),
    )
    return ReportData(
        item_agreements=item_agreements,
        metrics=metrics,
        reviewers=reviewers,
        sense_metadata_by_key=sense_metadata_by_key(selection_records=selection_records),
    )
