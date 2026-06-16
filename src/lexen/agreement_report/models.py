"""Typed report data structures."""

from __future__ import annotations

from dataclasses import dataclass
from enum import StrEnum

from lexen.models import ItemID, SenseKey

type ConceptID = str
type LabelCode = str
type ReviewerID = str


class Granularity(StrEnum):
    FINE = "fine"
    GLITE = "glite"


class AgreementLevel(StrEnum):
    ALL_THREE = "all_three_agree"
    EXACTLY_TWO = "exactly_two_agree"
    ALL_DIFFER = "all_three_disagree"


class AppendixGroupID(StrEnum):
    ALL_THREE_MARU2022 = "A"
    ALL_THREE_CORRECTION = "B"
    ALL_THREE_UNANSWERABLE = "C"
    TWO_SAME_SENSE = "D"
    TWO_UNANSWERABLE = "E"
    ALL_DIFFER = "F"


@dataclass(frozen=True, slots=True)
class ReviewerPair:
    left: ReviewerID
    right: ReviewerID


@dataclass(frozen=True, slots=True)
class LabelValue:
    code: LabelCode
    display: str
    sense_keys: list[SenseKey]
    coarse_keys: list[ConceptID]
    cannot_answer: list[str]


@dataclass(frozen=True, slots=True)
class SenseMetadata:
    sense_key: SenseKey
    synset_name: str
    lemma: str
    pos: str
    definition: str
    examples: list[str]
    synonyms: list[str]
    in_maru_prompt: bool


@dataclass(frozen=True, slots=True)
class VotePattern:
    level: AgreementLevel
    majority_code: LabelCode | None


@dataclass(frozen=True, slots=True)
class ItemAgreement:
    item_id: ItemID
    lemma: str
    pos: str
    source_dataset: str
    document_id: str
    target_text: str
    sentence_text: str
    target_sentence_tokens: list[str]
    target_token_index: int
    maru_fine: LabelValue
    maru_glite: LabelValue
    lexen_gold_keys: list[SenseKey]
    reviewer_fine: dict[ReviewerID, LabelValue]
    reviewer_glite: dict[ReviewerID, LabelValue]
    reviewer_notes: dict[ReviewerID, str | None]
    reviewer_comments: dict[ReviewerID, str | None]
    fine_level: AgreementLevel
    glite_level: AgreementLevel
    fine_gold_support: int
    glite_gold_support: int
    fine_majority_code: LabelCode | None
    glite_majority_code: LabelCode | None


@dataclass(frozen=True, slots=True)
class CountPercent:
    count: int
    percent: float


@dataclass(frozen=True, slots=True)
class PairwiseAgreement:
    granularity: Granularity
    pair: ReviewerPair
    matching_items: int
    total_items: int
    raw_agreement: float
    cohen_kappa: float


@dataclass(frozen=True, slots=True)
class AgreementMetrics:
    granularity: Granularity
    total_items: int
    level_counts: dict[AgreementLevel, CountPercent]
    all_three_agree_and_gold: CountPercent
    exactly_two_agree_and_gold: CountPercent
    gold_support_counts: dict[int, CountPercent]
    relationship_counts: dict[str, CountPercent]
    fleiss_kappa: float
    pairwise: list[PairwiseAgreement]


@dataclass(frozen=True, slots=True)
class ReviewerVerdictShape:
    reviewer: ReviewerID
    single_sense_items: int
    multi_sense_items: int
    cannot_answer_items: int
    comment_items: int
    note_items: int


@dataclass(frozen=True, slots=True)
class ReviewerMaruRelation:
    granularity: Granularity
    reviewer: ReviewerID
    accept_exact: CountPercent
    accept_plus_extra: CountPercent
    partial_overlap: CountPercent
    replace: CountPercent
    unanswerable: CountPercent


@dataclass(frozen=True, slots=True)
class GroupAgreement:
    group_kind: str
    group_name: str
    total_items: int
    fine_all_three: CountPercent
    fine_exactly_two: CountPercent
    fine_all_differ: CountPercent
    glite_all_three: CountPercent
    glite_exactly_two: CountPercent
    glite_all_differ: CountPercent


@dataclass(frozen=True, slots=True)
class CannotAnswerMetrics:
    reason_counts_by_reviewer: dict[ReviewerID, dict[str, int]]
    at_least_one_unanswerable: int
    exactly_one_unanswerable: int
    exactly_two_unanswerable: int
    at_least_two_unanswerable: int
    all_three_unanswerable: int
    at_least_two_reason_item_counts: dict[str, int]
    input_defective_by_document: dict[str, int]
    cannot_answer_by_document_support: dict[int, dict[str, int]]
    input_defective_by_document_support: dict[int, dict[str, int]]


@dataclass(frozen=True, slots=True)
class NoConsensusSampleItem:
    item_id: ItemID
    lemma: str
    pos: str
    source_dataset: str
    recommendation: str
    rationale: str


@dataclass(frozen=True, slots=True)
class NoConsensusMetrics:
    total_items: int
    pos_counts: dict[str, int]
    source_counts: dict[str, int]
    fine_gold_support_counts: dict[int, int]
    glite_gold_support_counts: dict[int, int]
    glite_level_counts: dict[AgreementLevel, int]
    cannot_answer_vote_counts: dict[int, int]
    comment_count_distribution: dict[int, int]
    note_count_distribution: dict[int, int]
    sampled_items: list[NoConsensusSampleItem]


@dataclass(frozen=True, slots=True)
class GliteCoverage:
    required_sense_keys: int
    mapped_sense_keys: int
    unmapped_sense_keys: list[SenseKey]


@dataclass(frozen=True, slots=True)
class AppendixGroup:
    group_id: AppendixGroupID
    title: str
    description: str
    items: list[ItemAgreement]


@dataclass(frozen=True, slots=True)
class ReportMetrics:
    reviewed_items: int
    fine: AgreementMetrics
    glite: AgreementMetrics
    verdict_shapes: list[ReviewerVerdictShape]
    maru_relations: list[ReviewerMaruRelation]
    pos_groups: list[GroupAgreement]
    source_groups: list[GroupAgreement]
    headword_groups: list[GroupAgreement]
    cannot_answer: CannotAnswerMetrics
    no_consensus: NoConsensusMetrics
    glite_coverage: GliteCoverage
    fine_non_unanimous_resolved_by_glite: CountPercent
    appendix_groups: list[AppendixGroup]


@dataclass(frozen=True, slots=True)
class ReportData:
    item_agreements: list[ItemAgreement]
    metrics: ReportMetrics
    reviewers: list[ReviewerID]
    sense_metadata_by_key: dict[SenseKey, SenseMetadata]
