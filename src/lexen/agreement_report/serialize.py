"""Serialize agreement report metrics."""

from __future__ import annotations

from lexen.agreement_report.metrics import (
    RELATION_ALL_DIFFER,
    RELATION_ALL_THREE_DIFFERENT,
    RELATION_ALL_THREE_GOLD,
    RELATION_EXACTLY_TWO_DIFFERENT,
    RELATION_EXACTLY_TWO_GOLD,
)
from lexen.agreement_report.models import (
    AgreementMetrics,
    AppendixGroup,
    CannotAnswerMetrics,
    CountPercent,
    GliteCoverage,
    GroupAgreement,
    ItemAgreement,
    NoConsensusMetrics,
    NoConsensusSampleItem,
    PairwiseAgreement,
    ReportData,
    ReportMetrics,
    ReviewerMaruRelation,
    ReviewerVerdictShape,
)
from lexen.models import JsonObject


def rounded(*, value: float, digits: int = 3) -> float:
    return round(value, digits)


def count_percent_json(*, value: CountPercent) -> JsonObject:
    return {
        "count": value.count,
        "percent": rounded(value=value.percent),
    }


def pairwise_json(*, value: PairwiseAgreement) -> JsonObject:
    return {
        "cohen_kappa": rounded(value=value.cohen_kappa),
        "granularity": value.granularity.value,
        "matching_items": value.matching_items,
        "pair": f"{value.pair.left}+{value.pair.right}",
        "raw_agreement_percent": rounded(value=value.raw_agreement),
        "total_items": value.total_items,
    }


def agreement_metrics_json(*, value: AgreementMetrics) -> JsonObject:
    return {
        "all_three_agree_and_maru2022_gold": count_percent_json(
            value=value.all_three_agree_and_gold,
        ),
        "exactly_two_agree_and_maru2022_gold": count_percent_json(
            value=value.exactly_two_agree_and_gold,
        ),
        "fleiss_kappa": rounded(value=value.fleiss_kappa),
        "gold_support_counts": {
            str(support_count): count_percent_json(value=count_percent)
            for support_count, count_percent in value.gold_support_counts.items()
        },
        "granularity": value.granularity.value,
        "level_counts": {
            level.value: count_percent_json(value=count_percent)
            for level, count_percent in value.level_counts.items()
        },
        "pairwise": [pairwise_json(value=pairwise) for pairwise in value.pairwise],
        "relationship_counts": {
            relation: count_percent_json(value=count_percent)
            for relation, count_percent in value.relationship_counts.items()
        },
        "total_items": value.total_items,
    }


def verdict_shape_json(*, value: ReviewerVerdictShape) -> JsonObject:
    return {
        "cannot_answer_items": value.cannot_answer_items,
        "comment_items": value.comment_items,
        "multi_sense_items": value.multi_sense_items,
        "note_items": value.note_items,
        "reviewer": value.reviewer,
        "single_sense_items": value.single_sense_items,
    }


def maru_relation_json(*, value: ReviewerMaruRelation) -> JsonObject:
    return {
        "accept_exact": count_percent_json(value=value.accept_exact),
        "accept_plus_extra": count_percent_json(value=value.accept_plus_extra),
        "granularity": value.granularity.value,
        "partial_overlap": count_percent_json(value=value.partial_overlap),
        "replace": count_percent_json(value=value.replace),
        "reviewer": value.reviewer,
        "unanswerable": count_percent_json(value=value.unanswerable),
    }


def group_agreement_json(*, value: GroupAgreement) -> JsonObject:
    return {
        "fine_all_differ": count_percent_json(value=value.fine_all_differ),
        "fine_all_three": count_percent_json(value=value.fine_all_three),
        "fine_exactly_two": count_percent_json(value=value.fine_exactly_two),
        "glite_all_differ": count_percent_json(value=value.glite_all_differ),
        "glite_all_three": count_percent_json(value=value.glite_all_three),
        "glite_exactly_two": count_percent_json(value=value.glite_exactly_two),
        "group_kind": value.group_kind,
        "group_name": value.group_name,
        "total_items": value.total_items,
    }


def cannot_answer_json(*, value: CannotAnswerMetrics) -> JsonObject:
    return {
        "all_three_unanswerable": value.all_three_unanswerable,
        "at_least_one_unanswerable": value.at_least_one_unanswerable,
        "at_least_two_reason_item_counts": value.at_least_two_reason_item_counts,
        "at_least_two_unanswerable": value.at_least_two_unanswerable,
        "exactly_one_unanswerable": value.exactly_one_unanswerable,
        "exactly_two_unanswerable": value.exactly_two_unanswerable,
        "cannot_answer_by_document_support": value.cannot_answer_by_document_support,
        "input_defective_by_document": value.input_defective_by_document,
        "input_defective_by_document_support": value.input_defective_by_document_support,
        "reason_counts_by_reviewer": value.reason_counts_by_reviewer,
    }


def glite_coverage_json(*, value: GliteCoverage) -> JsonObject:
    return {
        "mapped_sense_keys": value.mapped_sense_keys,
        "required_sense_keys": value.required_sense_keys,
        "unmapped_sense_keys": value.unmapped_sense_keys,
    }


def no_consensus_sample_json(*, value: NoConsensusSampleItem) -> JsonObject:
    return {
        "item_id": value.item_id,
        "lemma": value.lemma,
        "pos": value.pos,
        "rationale": value.rationale,
        "recommendation": value.recommendation,
        "source_dataset": value.source_dataset,
    }


def no_consensus_json(*, value: NoConsensusMetrics) -> JsonObject:
    return {
        "cannot_answer_vote_counts": {
            str(key): count for key, count in value.cannot_answer_vote_counts.items()
        },
        "comment_count_distribution": {
            str(key): count for key, count in value.comment_count_distribution.items()
        },
        "fine_gold_support_counts": {
            str(key): count for key, count in value.fine_gold_support_counts.items()
        },
        "glite_gold_support_counts": {
            str(key): count for key, count in value.glite_gold_support_counts.items()
        },
        "glite_level_counts": {key.value: count for key, count in value.glite_level_counts.items()},
        "note_count_distribution": {
            str(key): count for key, count in value.note_count_distribution.items()
        },
        "pos_counts": value.pos_counts,
        "sampled_items": [no_consensus_sample_json(value=item) for item in value.sampled_items],
        "source_counts": value.source_counts,
        "total_items": value.total_items,
    }


def appendix_group_json(*, value: AppendixGroup) -> JsonObject:
    return {
        "count": len(value.items),
        "description": value.description,
        "group_id": value.group_id.value,
        "item_ids": [item.item_id for item in value.items],
        "title": value.title,
    }


def report_metrics_json(*, value: ReportMetrics) -> JsonObject:
    return {
        "cannot_answer": cannot_answer_json(value=value.cannot_answer),
        "fine": agreement_metrics_json(value=value.fine),
        "fine_non_unanimous_resolved_by_glite": count_percent_json(
            value=value.fine_non_unanimous_resolved_by_glite,
        ),
        "glite": agreement_metrics_json(value=value.glite),
        "glite_coverage": glite_coverage_json(value=value.glite_coverage),
        "headword_groups": [group_agreement_json(value=group) for group in value.headword_groups],
        "maru_relations": [maru_relation_json(value=relation) for relation in value.maru_relations],
        "no_consensus": no_consensus_json(value=value.no_consensus),
        "pos_groups": [group_agreement_json(value=group) for group in value.pos_groups],
        "relationship_order": [
            RELATION_ALL_THREE_GOLD,
            RELATION_ALL_THREE_DIFFERENT,
            RELATION_EXACTLY_TWO_GOLD,
            RELATION_EXACTLY_TWO_DIFFERENT,
            RELATION_ALL_DIFFER,
        ],
        "reviewed_items": value.reviewed_items,
        "source_groups": [group_agreement_json(value=group) for group in value.source_groups],
        "appendix_groups": [appendix_group_json(value=group) for group in value.appendix_groups],
        "verdict_shapes": [verdict_shape_json(value=shape) for shape in value.verdict_shapes],
    }


def label_json_keys(*, item: ItemAgreement, reviewer: str) -> JsonObject:
    fine = item.reviewer_fine[reviewer]
    glite = item.reviewer_glite[reviewer]
    return {
        "cannot_answer": fine.cannot_answer,
        "comment": item.reviewer_comments[reviewer],
        "fine_sense_keys": fine.sense_keys,
        "glite_concept_ids": glite.coarse_keys,
        "note": item.reviewer_notes[reviewer],
    }


def item_agreement_json(*, item: ItemAgreement) -> JsonObject:
    reviewers = sorted(item.reviewer_fine)
    return {
        "document_id": item.document_id,
        "fine_gold_support": item.fine_gold_support,
        "fine_level": item.fine_level.value,
        "glite_gold_support": item.glite_gold_support,
        "glite_level": item.glite_level.value,
        "item_id": item.item_id,
        "lemma": item.lemma,
        "lexen_gold_sense_keys": item.lexen_gold_keys,
        "maru2022_glite_concept_ids": item.maru_glite.coarse_keys,
        "maru2022_sense_keys": item.maru_fine.sense_keys,
        "pos": item.pos,
        "reviewers": {
            reviewer: label_json_keys(item=item, reviewer=reviewer) for reviewer in reviewers
        },
        "sentence": item.sentence_text,
        "source_dataset": item.source_dataset,
        "target_text": item.target_text,
    }


def report_data_json(*, data: ReportData) -> JsonObject:
    return {
        "metrics": report_metrics_json(value=data.metrics),
    }


def per_item_rows(*, data: ReportData) -> list[JsonObject]:
    return [
        item_agreement_json(item=item)
        for item in sorted(data.item_agreements, key=lambda value: value.item_id)
    ]
