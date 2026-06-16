"""Shared content helpers for agreement report renderers."""

from __future__ import annotations

from dataclasses import dataclass
from html import escape
from typing import Literal

from lexen.agreement_report.data import detokenize
from lexen.agreement_report.formatting import (
    count_percent_text,
    kappa_text,
    level_label,
    percent_text,
)
from lexen.agreement_report.models import (
    AgreementLevel,
    CountPercent,
    Granularity,
    ItemAgreement,
    LabelValue,
    PairwiseAgreement,
    ReportData,
    ReviewerID,
    SenseMetadata,
)
from lexen.models import SenseKey

REVIEWER_DISPLAY_NAMES: dict[ReviewerID, str] = {
    "RF": "Robert Farren",
    "PW": "Patrick White",
    "PH": "Penny Hands",
}

type PairwiseMatrixMetric = Literal["raw_agreement", "cohen_kappa"]


@dataclass(frozen=True, slots=True)
class PairwiseMatrixCell:
    row_reviewer: ReviewerID
    column_reviewer: ReviewerID
    value: float
    matching_items: int
    total_items: int
    diagonal: bool


def reviewer_name(*, reviewer: ReviewerID) -> str:
    return REVIEWER_DISPLAY_NAMES.get(reviewer, reviewer)


def reviewer_label(*, reviewer: ReviewerID) -> str:
    return f"{reviewer_name(reviewer=reviewer)} ({reviewer})"


def clean_optional_text(*, value: str | None) -> str | None:
    if value is None:
        return None
    stripped = value.strip()
    if len(stripped) == 0:
        return None
    return stripped


def reason_label(*, reason: str) -> str:
    return reason.strip("_").replace("_", " ")


def reason_list_text(*, reasons: list[str]) -> str:
    return ", ".join(reason_label(reason=reason) for reason in reasons)


def sense_metadata(
    *,
    data: ReportData,
    sense_key: SenseKey,
) -> SenseMetadata | None:
    return data.sense_metadata_by_key.get(sense_key)


def sense_plain_text(
    *,
    data: ReportData,
    sense_key: SenseKey,
    include_examples: bool,
) -> str:
    metadata = sense_metadata(data=data, sense_key=sense_key)
    if metadata is None:
        return f"{sense_key} - definition unavailable in release source metadata"
    text = f"{sense_key} ({metadata.synset_name}) - {metadata.definition}"
    if include_examples and len(metadata.examples) > 0:
        text += " Examples: " + " | ".join(metadata.examples[:2])
    return text


def sense_html(
    *,
    data: ReportData,
    sense_key: SenseKey,
    include_examples: bool,
) -> str:
    metadata = sense_metadata(data=data, sense_key=sense_key)
    if metadata is None:
        return (
            f"<code>{escape(sense_key)}</code> "
            '<span class="missing-definition">definition unavailable in source metadata</span>'
        )
    examples = ""
    if include_examples and len(metadata.examples) > 0:
        example_text = " | ".join(metadata.examples[:2])
        examples = f'<span class="examples">Examples: {escape(example_text)}</span>'
    synonyms = ""
    if len(metadata.synonyms) > 0:
        synonyms = f'<span class="synonyms">Synonyms: {escape(", ".join(metadata.synonyms))}</span>'
    return (
        f"<code>{escape(sense_key)}</code> "
        f'<span class="synset">{escape(metadata.synset_name)}</span>'
        f'<span class="definition">{escape(metadata.definition)}</span>'
        f"{synonyms}{examples}"
    )


def label_plain_lines(
    *,
    data: ReportData,
    label: LabelValue,
    include_examples: bool,
) -> list[str]:
    lines: list[str] = []
    if len(label.sense_keys) > 0:
        lines.extend(
            sense_plain_text(
                data=data,
                sense_key=sense_key,
                include_examples=include_examples,
            )
            for sense_key in label.sense_keys
        )
    if len(label.cannot_answer) > 0:
        prefix = "Cannot answer"
        if len(label.sense_keys) > 0:
            prefix = "Cannot-answer flag"
        lines.append(f"{prefix}: {reason_list_text(reasons=label.cannot_answer)}")
    if len(lines) == 0:
        lines.append("No answer recorded")
    return lines


def label_html(
    *,
    data: ReportData,
    label: LabelValue,
    include_examples: bool,
) -> str:
    items: list[str] = []
    for sense_key in label.sense_keys:
        items.append(
            "<li>"
            + sense_html(data=data, sense_key=sense_key, include_examples=include_examples)
            + "</li>"
        )
    if len(label.cannot_answer) > 0:
        cannot_label = "Cannot answer"
        if len(label.sense_keys) > 0:
            cannot_label = "Cannot-answer flag"
        items.append(
            f"<li><strong>{escape(cannot_label)}:</strong> "
            f"{escape(reason_list_text(reasons=label.cannot_answer))}</li>"
        )
    if len(items) == 0:
        items.append("<li>No answer recorded</li>")
    return f'<ul class="label-list">{"".join(items)}</ul>'


def marked_sentence_text(
    *,
    item: ItemAgreement,
    open_marker: str,
    close_marker: str,
) -> str:
    tokens = list(item.target_sentence_tokens)
    if 0 <= item.target_token_index < len(tokens):
        tokens[item.target_token_index] = (
            f"{open_marker}{tokens[item.target_token_index]}{close_marker}"
        )
    return detokenize(tokens=tokens)


def marked_sentence_html(*, item: ItemAgreement) -> str:
    tokens = [escape(token) for token in item.target_sentence_tokens]
    if 0 <= item.target_token_index < len(tokens):
        tokens[item.target_token_index] = f"<mark>{tokens[item.target_token_index]}</mark>"
    return detokenize(tokens=tokens)


def agreement_short_text(*, item: ItemAgreement) -> str:
    return (
        f"Fine: {level_label(level=item.fine_level)}; "
        f"Glite: {level_label(level=item.glite_level)}; "
        f"Maru2022 fine support: {item.fine_gold_support}/3; "
        f"Maru2022 Glite support: {item.glite_gold_support}/3."
    )


def reviewer_choice_short_text(*, item: ItemAgreement, reviewer: ReviewerID) -> str:
    label = item.reviewer_fine[reviewer]
    if len(label.sense_keys) > 0:
        return ", ".join(label.sense_keys)
    if len(label.cannot_answer) > 0:
        return "Cannot answer: " + reason_list_text(reasons=label.cannot_answer)
    return "No answer"


def appendix_item_sort_key(*, item: ItemAgreement) -> tuple[str, str]:
    return (item.lemma.lower(), item.item_id)


def appendix_group_summary_rows(*, data: ReportData) -> list[list[str]]:
    total = data.metrics.reviewed_items
    rows: list[list[str]] = []
    for group in data.metrics.appendix_groups:
        value = CountPercent(count=len(group.items), percent=len(group.items) * 100.0 / total)
        rows.append(
            [
                group.group_id.value,
                group.title.split(". ", maxsplit=1)[1],
                count_percent_text(value=value),
            ]
        )
    return rows


def appendix_group_anchor(*, group_id: str) -> str:
    return f"appendix-{group_id.lower()}"


def granularity_label(*, granularity: Granularity) -> str:
    if granularity is Granularity.FINE:
        return "Fine WordNet"
    return "Glite coarse"


def pairwise_agreements_for_granularity(
    *,
    data: ReportData,
    granularity: Granularity,
) -> list[PairwiseAgreement]:
    if granularity is Granularity.FINE:
        return data.metrics.fine.pairwise
    return data.metrics.glite.pairwise


def pairwise_lookup(
    *,
    data: ReportData,
    granularity: Granularity,
) -> dict[frozenset[ReviewerID], PairwiseAgreement]:
    return {
        frozenset((pairwise.pair.left, pairwise.pair.right)): pairwise
        for pairwise in pairwise_agreements_for_granularity(
            data=data,
            granularity=granularity,
        )
    }


def pairwise_matrix_cell_value(
    *,
    pairwise: PairwiseAgreement,
    metric: PairwiseMatrixMetric,
) -> float:
    if metric == "raw_agreement":
        return pairwise.raw_agreement
    return pairwise.cohen_kappa


def pairwise_matrix_cells(
    *,
    data: ReportData,
    granularity: Granularity,
    metric: PairwiseMatrixMetric,
) -> list[list[PairwiseMatrixCell]]:
    lookup = pairwise_lookup(data=data, granularity=granularity)
    matrix: list[list[PairwiseMatrixCell]] = []
    for row_reviewer in data.reviewers:
        row: list[PairwiseMatrixCell] = []
        for column_reviewer in data.reviewers:
            if row_reviewer == column_reviewer:
                row.append(
                    PairwiseMatrixCell(
                        row_reviewer=row_reviewer,
                        column_reviewer=column_reviewer,
                        value=100.0 if metric == "raw_agreement" else 1.0,
                        matching_items=data.metrics.reviewed_items,
                        total_items=data.metrics.reviewed_items,
                        diagonal=True,
                    )
                )
                continue
            pairwise = lookup[frozenset((row_reviewer, column_reviewer))]
            row.append(
                PairwiseMatrixCell(
                    row_reviewer=row_reviewer,
                    column_reviewer=column_reviewer,
                    value=pairwise_matrix_cell_value(pairwise=pairwise, metric=metric),
                    matching_items=pairwise.matching_items,
                    total_items=pairwise.total_items,
                    diagonal=False,
                )
            )
        matrix.append(row)
    return matrix


def pairwise_matrix_cell_text(
    *,
    cell: PairwiseMatrixCell,
    metric: PairwiseMatrixMetric,
) -> str:
    if metric == "raw_agreement":
        return f"{percent_text(value=cell.value)} ({cell.matching_items}/{cell.total_items})"
    return kappa_text(value=cell.value)


def pairwise_matrix_rows(
    *,
    data: ReportData,
    granularity: Granularity,
    metric: PairwiseMatrixMetric,
) -> list[list[str]]:
    return [
        [
            row_cells[0].row_reviewer,
            *[pairwise_matrix_cell_text(cell=cell, metric=metric) for cell in row_cells],
        ]
        for row_cells in pairwise_matrix_cells(
            data=data,
            granularity=granularity,
            metric=metric,
        )
    ]


def pairwise_summary_rows(*, data: ReportData) -> list[list[str]]:
    rows: list[list[str]] = []
    for fine_pairwise, glite_pairwise in zip(
        data.metrics.fine.pairwise,
        data.metrics.glite.pairwise,
        strict=True,
    ):
        rows.append(
            [
                f"{fine_pairwise.pair.left} + {fine_pairwise.pair.right}",
                (
                    f"{percent_text(value=fine_pairwise.raw_agreement)} "
                    f"({fine_pairwise.matching_items}/{fine_pairwise.total_items})"
                ),
                kappa_text(value=fine_pairwise.cohen_kappa),
                (
                    f"{percent_text(value=glite_pairwise.raw_agreement)} "
                    f"({glite_pairwise.matching_items}/{glite_pairwise.total_items})"
                ),
                kappa_text(value=glite_pairwise.cohen_kappa),
            ]
        )
    return rows


def cannot_answer_consensus_rows(*, data: ReportData) -> list[list[str]]:
    total = data.metrics.reviewed_items
    metrics = data.metrics.cannot_answer
    return [
        [
            "Exactly one reviewer marked cannot answer",
            count_percent_text(
                value=CountPercent(
                    count=metrics.exactly_one_unanswerable,
                    percent=metrics.exactly_one_unanswerable * 100.0 / total,
                )
            ),
        ],
        [
            "Exactly two reviewers marked cannot answer",
            count_percent_text(
                value=CountPercent(
                    count=metrics.exactly_two_unanswerable,
                    percent=metrics.exactly_two_unanswerable * 100.0 / total,
                )
            ),
        ],
        [
            "All three reviewers marked cannot answer",
            count_percent_text(
                value=CountPercent(
                    count=metrics.all_three_unanswerable,
                    percent=metrics.all_three_unanswerable * 100.0 / total,
                )
            ),
        ],
        [
            "At least two reviewers marked cannot answer",
            count_percent_text(
                value=CountPercent(
                    count=metrics.at_least_two_unanswerable,
                    percent=metrics.at_least_two_unanswerable * 100.0 / total,
                )
            ),
        ],
    ]


def cannot_answer_at_least_two_reason_rows(*, data: ReportData) -> list[list[str]]:
    total = data.metrics.reviewed_items
    return [
        [
            reason_label(reason=reason),
            count_percent_text(
                value=CountPercent(
                    count=count,
                    percent=count * 100.0 / total,
                )
            ),
        ]
        for reason, count in data.metrics.cannot_answer.at_least_two_reason_item_counts.items()
    ]


def document_support_rows(
    *,
    support_by_document: dict[int, dict[str, int]],
    support_levels: list[int],
) -> list[list[str]]:
    rows: list[list[str]] = []
    for support in support_levels:
        document_counts = support_by_document.get(support, {})
        if len(document_counts) == 0:
            rows.append([f"{support}/3 reviewers", "None", "0"])
            continue
        for document_id, count in document_counts.items():
            rows.append([f"{support}/3 reviewers", document_id, str(count)])
    return rows


def removed_reviewed_item_rows(*, data: ReportData) -> list[list[str]]:
    cannot_answer_removed = data.metrics.cannot_answer.at_least_two_unanswerable
    no_consensus_removed = data.metrics.no_consensus.total_items
    total_removed = cannot_answer_removed + no_consensus_removed
    return [
        [
            "Two or three reviewers marked cannot answer",
            str(cannot_answer_removed),
            "Removed from lexEN benchmark",
        ],
        [
            "No fine-grained sense received two-reviewer support",
            str(no_consensus_removed),
            "Removed from lexEN benchmark",
        ],
        [
            "Total reviewed items removed",
            str(total_removed),
            "No Maru2022 fallback label is used",
        ],
    ]


def count_distribution_rows(*, counts: dict[int, int], label: str) -> list[list[str]]:
    return [[f"{key} {label}", str(value)] for key, value in sorted(counts.items())]


def string_count_rows(*, counts: dict[str, int]) -> list[list[str]]:
    return [[key, str(value)] for key, value in sorted(counts.items())]


def no_consensus_summary_rows(*, data: ReportData) -> list[list[str]]:
    metrics = data.metrics.no_consensus
    rows: list[list[str]] = [["Total no-consensus items", str(metrics.total_items)]]
    rows.extend([["POS: " + key, str(value)] for key, value in sorted(metrics.pos_counts.items())])
    rows.extend(
        [["Source: " + key, str(value)] for key, value in sorted(metrics.source_counts.items())]
    )
    return rows


def no_consensus_support_rows(*, data: ReportData) -> list[list[str]]:
    metrics = data.metrics.no_consensus
    rows: list[list[str]] = []
    rows.extend(
        [f"Fine Maru2022 support: {key}/3", str(value)]
        for key, value in sorted(metrics.fine_gold_support_counts.items())
    )
    rows.extend(
        [f"Glite Maru2022 support: {key}/3", str(value)]
        for key, value in sorted(metrics.glite_gold_support_counts.items())
    )
    rows.extend(
        [f"Glite reviewer agreement: {level_label(level=key)}", str(value)]
        for key, value in sorted(
            metrics.glite_level_counts.items(),
            key=lambda value: value[0].value,
        )
    )
    return rows


def no_consensus_evidence_rows(*, data: ReportData) -> list[list[str]]:
    metrics = data.metrics.no_consensus
    rows: list[list[str]] = []
    rows.extend(
        [f"Cannot-answer votes: {key}/3 reviewers", str(value)]
        for key, value in sorted(metrics.cannot_answer_vote_counts.items())
    )
    rows.extend(
        [f"Reviewer comments on item: {key}", str(value)]
        for key, value in sorted(metrics.comment_count_distribution.items())
    )
    rows.extend(
        [f"Cannot-answer notes on item: {key}", str(value)]
        for key, value in sorted(metrics.note_count_distribution.items())
    )
    return rows


def no_consensus_items(*, data: ReportData) -> list[ItemAgreement]:
    return sorted(
        [item for item in data.item_agreements if item.fine_level is AgreementLevel.ALL_DIFFER],
        key=lambda item: item.item_id,
    )


def no_consensus_item_rows(*, data: ReportData) -> list[list[str]]:
    rows: list[list[str]] = []
    for item in no_consensus_items(data=data):
        cannot_votes = sum(
            1 for reviewer in data.reviewers if len(item.reviewer_fine[reviewer].cannot_answer) > 0
        )
        rows.append(
            [
                item.item_id,
                f"{item.lemma} / {item.pos} / {item.source_dataset}",
                f"{item.fine_gold_support}/3",
                level_label(level=item.glite_level),
                f"{item.glite_gold_support}/3",
                str(cannot_votes),
                *[
                    reviewer_choice_short_text(item=item, reviewer=reviewer)
                    for reviewer in data.reviewers
                ],
            ]
        )
    return rows


def no_consensus_sample_rows(*, data: ReportData) -> list[list[str]]:
    return [
        [
            item.item_id,
            f"{item.lemma} / {item.pos} / {item.source_dataset}",
            item.recommendation,
            item.rationale,
        ]
        for item in data.metrics.no_consensus.sampled_items
    ]


def cannot_answer_document_support_rows(*, data: ReportData) -> list[list[str]]:
    return document_support_rows(
        support_by_document=data.metrics.cannot_answer.cannot_answer_by_document_support,
        support_levels=[2, 3],
    )


def input_defective_document_support_rows(*, data: ReportData) -> list[list[str]]:
    return document_support_rows(
        support_by_document=data.metrics.cannot_answer.input_defective_by_document_support,
        support_levels=[1, 2, 3],
    )


def heatmap_color_hex(
    *,
    value: float,
    metric: PairwiseMatrixMetric,
) -> str:
    if metric == "raw_agreement":
        normalized = max(0.0, min(1.0, value / 100.0))
    else:
        normalized = max(0.0, min(1.0, value))
    low = (246, 251, 248)
    high = (118, 190, 162)
    red = round(low[0] + (high[0] - low[0]) * normalized)
    green = round(low[1] + (high[1] - low[1]) * normalized)
    blue = round(low[2] + (high[2] - low[2]) * normalized)
    return f"#{red:02x}{green:02x}{blue:02x}"


def glite_resolution_text(*, data: ReportData) -> str:
    return count_percent_text(value=data.metrics.fine_non_unanimous_resolved_by_glite)


def relationship_interpretation(*, level: AgreementLevel) -> str:
    if level is AgreementLevel.ALL_THREE:
        return "unanimous"
    if level is AgreementLevel.EXACTLY_TWO:
        return "majority"
    return "no majority"
