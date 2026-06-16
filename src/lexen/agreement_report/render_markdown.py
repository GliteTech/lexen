"""Render a Markdown companion for the agreement report."""

from __future__ import annotations

from pathlib import Path

from lexen.agreement_report.formatting import (
    count_percent_text,
    kappa_text,
    level_label,
    maru_relation_label,
    relation_label,
)
from lexen.agreement_report.models import (
    AgreementLevel,
    CountPercent,
    Granularity,
    GroupAgreement,
    ReportData,
    ReviewerMaruRelation,
)
from lexen.agreement_report.paths import REPORT_TITLE, REPORT_VERSION
from lexen.agreement_report.report_content import (
    agreement_short_text,
    appendix_group_anchor,
    appendix_group_summary_rows,
    cannot_answer_at_least_two_reason_rows,
    cannot_answer_consensus_rows,
    cannot_answer_document_support_rows,
    glite_resolution_text,
    input_defective_document_support_rows,
    label_plain_lines,
    marked_sentence_text,
    no_consensus_evidence_rows,
    no_consensus_item_rows,
    no_consensus_sample_rows,
    no_consensus_summary_rows,
    no_consensus_support_rows,
    pairwise_matrix_rows,
    pairwise_summary_rows,
    reason_label,
    removed_reviewed_item_rows,
    reviewer_label,
    reviewer_name,
)


def markdown_table(
    *,
    headers: list[str],
    rows: list[list[str]],
) -> str:
    header = "| " + " | ".join(headers) + " |"
    separator = "| " + " | ".join("---" for _header in headers) + " |"
    body = ["| " + " | ".join(cell.replace("\n", " ") for cell in row) + " |" for row in rows]
    return "\n".join([header, separator, *body])


def agreement_rows(*, data: ReportData) -> list[list[str]]:
    rows: list[list[str]] = []
    for level in AgreementLevel:
        rows.append(
            [
                level_label(level=level),
                count_percent_text(value=data.metrics.fine.level_counts[level]),
                count_percent_text(value=data.metrics.glite.level_counts[level]),
            ]
        )
    rows.extend(
        [
            [
                "All three agree and match Maru2022",
                count_percent_text(value=data.metrics.fine.all_three_agree_and_gold),
                count_percent_text(value=data.metrics.glite.all_three_agree_and_gold),
            ],
            [
                "Exactly two agree and match Maru2022",
                count_percent_text(value=data.metrics.fine.exactly_two_agree_and_gold),
                count_percent_text(value=data.metrics.glite.exactly_two_agree_and_gold),
            ],
            [
                "Fleiss kappa",
                kappa_text(value=data.metrics.fine.fleiss_kappa),
                kappa_text(value=data.metrics.glite.fleiss_kappa),
            ],
        ]
    )
    return rows


def support_rows(*, data: ReportData) -> list[list[str]]:
    return [
        [
            f"{support}/3 reviewers selected the Maru2022 label",
            count_percent_text(value=data.metrics.fine.gold_support_counts[support]),
            count_percent_text(value=data.metrics.glite.gold_support_counts[support]),
        ]
        for support in [3, 2, 1, 0]
    ]


def contents_markdown(*, data: ReportData) -> str:
    lines = [
        "* [What This Report Includes](#what-this-report-includes)",
        "* [How To Read The Numbers](#how-to-read-the-numbers)",
        "* [Headline Agreement](#headline-agreement)",
        "* [Maru2022 Label Support Split](#maru2022-label-support-split)",
        "* [Pairwise Agreement](#pairwise-agreement)",
        "* [Reviewer Answer Shape](#reviewer-answer-shape)",
        "* [Glite Coarsening Effect](#glite-coarsening-effect)",
        "* [Disagreement Concentration](#disagreement-concentration)",
        "* [Cannot-Answer Reasons](#cannot-answer-reasons)",
        "* [Removed Reviewed Items](#removed-reviewed-items)",
        "* [What The Agreement Shows](#what-the-agreement-shows)",
        "* [Technical Method](#technical-method)",
        "* [Full Item Appendix](#full-item-appendix)",
    ]
    for group in data.metrics.appendix_groups:
        lines.append(
            f"  * [{group.group_id.value}. {group.title.split('. ', maxsplit=1)[1]}]"
            f"(#{appendix_group_anchor(group_id=group.group_id.value)})"
        )
    return "\n".join(lines)


def verdict_rows(*, data: ReportData) -> list[list[str]]:
    return [
        [
            reviewer_label(reviewer=shape.reviewer),
            str(shape.single_sense_items),
            str(shape.multi_sense_items),
            str(shape.cannot_answer_items),
            str(shape.comment_items),
            str(shape.note_items),
        ]
        for shape in data.metrics.verdict_shapes
    ]


def maru_relation_value(
    *,
    relation: ReviewerMaruRelation,
    relation_name: str,
) -> CountPercent:
    if relation_name == "accept_exact":
        return relation.accept_exact
    if relation_name == "accept_plus_extra":
        return relation.accept_plus_extra
    if relation_name == "partial_overlap":
        return relation.partial_overlap
    if relation_name == "replace":
        return relation.replace
    if relation_name == "unanswerable":
        return relation.unanswerable
    raise ValueError(f"unknown Maru2022 relation {relation_name}")


def maru_relation_rows(
    *,
    data: ReportData,
    granularity: Granularity,
) -> list[list[str]]:
    rows: list[list[str]] = []
    for relation_name in [
        "accept_exact",
        "accept_plus_extra",
        "replace",
        "partial_overlap",
        "unanswerable",
    ]:
        row = [maru_relation_label(relation=relation_name)]
        for relation in data.metrics.maru_relations:
            if relation.granularity is granularity:
                row.append(
                    count_percent_text(
                        value=maru_relation_value(
                            relation=relation,
                            relation_name=relation_name,
                        )
                    )
                )
        rows.append(row)
    return rows


def relationship_rows(*, data: ReportData) -> list[list[str]]:
    return [
        [
            relation_label(relation=relation),
            count_percent_text(value=data.metrics.fine.relationship_counts[relation]),
            count_percent_text(value=data.metrics.glite.relationship_counts[relation]),
        ]
        for relation in data.metrics.fine.relationship_counts
    ]


def group_rows(*, groups: list[GroupAgreement]) -> list[list[str]]:
    return [
        [
            group.group_name,
            str(group.total_items),
            count_percent_text(value=group.fine_all_three),
            count_percent_text(value=group.fine_exactly_two),
            count_percent_text(value=group.fine_all_differ),
            count_percent_text(value=group.glite_all_three),
            count_percent_text(value=group.glite_exactly_two),
            count_percent_text(value=group.glite_all_differ),
        ]
        for group in groups
    ]


def cannot_answer_reason_rows(*, data: ReportData) -> list[list[str]]:
    reasons = sorted(
        {
            reason
            for counts in data.metrics.cannot_answer.reason_counts_by_reviewer.values()
            for reason in counts
        }
    )
    rows: list[list[str]] = []
    for reason in reasons:
        rows.append(
            [
                reason_label(reason=reason),
                *[
                    str(
                        data.metrics.cannot_answer.reason_counts_by_reviewer[reviewer].get(
                            reason,
                            0,
                        )
                    )
                    for reviewer in data.reviewers
                ],
            ]
        )
    return rows


def document_rows(*, data: ReportData) -> list[list[str]]:
    return [
        [document_id, str(count)]
        for document_id, count in data.metrics.cannot_answer.input_defective_by_document.items()
    ]


def appendix_group_summary_link_rows(*, data: ReportData) -> list[list[str]]:
    rows: list[list[str]] = []
    for group, summary_row in zip(
        data.metrics.appendix_groups,
        appendix_group_summary_rows(data=data),
        strict=True,
    ):
        anchor = appendix_group_anchor(group_id=group.group_id.value)
        group_text, outcome_text, items_text = summary_row
        rows.append(
            [
                f"[{group_text}](#{anchor})",
                f"[{outcome_text}](#{anchor})",
                f"[{items_text}](#{anchor})",
            ]
        )
    return rows


def appendix_item_markdown(
    *,
    data: ReportData,
    item_index: int,
    item_id_prefix: str,
) -> list[str]:
    item = data.item_agreements[item_index]
    lines = [
        f"### {item_id_prefix}. {item.item_id}",
        "",
        f"**Lemma/POS/source:** `{item.lemma}` / `{item.pos}` / `{item.source_dataset}` "
        f"(`{item.document_id}`)",
        "",
        f"**Sentence:** {marked_sentence_text(item=item, open_marker='**[', close_marker=']**')}",
        "",
        "**Maru2022 label**",
        "",
    ]
    for label_line in label_plain_lines(data=data, label=item.maru_fine, include_examples=True):
        lines.append(f"* {label_line}")
    lines.extend(["", "**Reviewer verdicts**", ""])
    for reviewer in data.reviewers:
        label = item.reviewer_fine[reviewer]
        lines.append(f"* **{reviewer_label(reviewer=reviewer)}**")
        for label_line in label_plain_lines(data=data, label=label, include_examples=True):
            lines.append(f"  * {label_line}")
        note = item.reviewer_notes[reviewer]
        if note is not None and len(note.strip()) > 0:
            lines.append(f"  * Note: {note.strip()}")
        comment = item.reviewer_comments[reviewer]
        if comment is not None and len(comment.strip()) > 0:
            lines.append(f"  * Comment: {comment.strip()}")
    lines.extend(
        [
            "",
            f"**Agreement:** {agreement_short_text(item=item)}",
            "",
        ]
    )
    return lines


def appendix_markdown(*, data: ReportData) -> list[str]:
    lines = [
        "## Full Item Appendix",
        "",
        "The appendix contains all 363 reviewed items. Items are grouped by the fine-grained "
        "three-reviewer outcome, because this is the level at which lexEN decides whether "
        "Maru2022 is retained, corrected, or removed for lack of usable consensus.",
        "",
        markdown_table(
            headers=["Group", "Outcome", "Items"],
            rows=appendix_group_summary_link_rows(data=data),
        ),
        "",
    ]
    for group in data.metrics.appendix_groups:
        anchor = appendix_group_anchor(group_id=group.group_id.value)
        lines.extend(
            [
                f'<a id="{anchor}"></a>',
                "",
                f"## {group.title}",
                "",
                f"{group.description} Count: {len(group.items)}.",
                "",
            ]
        )
        for number, item in enumerate(
            sorted(group.items, key=lambda value: value.item_id), start=1
        ):
            item_index = data.item_agreements.index(item)
            lines.extend(
                appendix_item_markdown(
                    data=data,
                    item_index=item_index,
                    item_id_prefix=f"{group.group_id.value}{number}",
                )
            )
    return lines


def render_markdown(
    *,
    data: ReportData,
    output_path: Path,
) -> None:
    output_path.parent.mkdir(parents=True, exist_ok=True)
    fine_all_three = count_percent_text(
        value=data.metrics.fine.level_counts[AgreementLevel.ALL_THREE]
    )
    fine_exactly_two = count_percent_text(
        value=data.metrics.fine.level_counts[AgreementLevel.EXACTLY_TWO]
    )
    glite_all_three = count_percent_text(
        value=data.metrics.glite.level_counts[AgreementLevel.ALL_THREE]
    )
    fine_all_three_correction = count_percent_text(
        value=data.metrics.fine.relationship_counts["all_three_agree_but_different"]
    )
    fine_exactly_two_correction = count_percent_text(
        value=data.metrics.fine.relationship_counts["exactly_two_agree_but_different"]
    )
    at_least_two_unanswerable = count_percent_text(
        value=CountPercent(
            count=data.metrics.cannot_answer.at_least_two_unanswerable,
            percent=(
                data.metrics.cannot_answer.at_least_two_unanswerable
                * 100.0
                / data.metrics.reviewed_items
            ),
        )
    )
    lines = [
        f"# {REPORT_TITLE}",
        "",
        f"Report date: {REPORT_VERSION}. Maru2022 labels are source labels under review.",
        "",
        "This report audits the 363 Maru2022 validation items flagged by the S1-S6 "
        "model-panel waterfall for lexicographer review. The items were reviewed "
        "independently by three professional lexicographers using the same marureview.com "
        "brief. The report is generated from the Maru2022 source copy, the suspicious-item "
        "selection package, the RF/PW/PH review JSON files, and the Glite coarsening map.",
        "",
        "## Contents",
        "",
        contents_markdown(data=data),
        "",
        "## What This Report Includes",
        "",
        "* Fine WordNet agreement among RF, PW, and PH.",
        "* The same agreement analysis after Glite coarsening of WordNet senses.",
        "* Pairwise raw agreement, Cohen's kappa for each reviewer pair, and Fleiss kappa.",
        "* The split of reviewer support for the Maru2022 source label.",
        "* Reviewer-level answer shape: single-sense, multi-sense, cannot-answer, comments, "
        "and notes.",
        "* Concentration by part of speech, source dataset, and frequent headword.",
        "* Cannot-answer reason tags and defective-input concentration by document.",
        "* A complete appendix with all 363 reviewed items, reviewer choices, notes, "
        "comments, and WordNet definitions.",
        "",
        "## How To Read The Numbers",
        "",
        "Fine WordNet agreement compares the exact WordNet sense-key sets chosen by the "
        "reviewers. Glite agreement first maps those sense keys to Glite coarse concepts, "
        "so two different WordNet senses can agree at the coarse concept level. Maru2022 "
        "support counts how many reviewers selected the Maru2022 source label for an item; "
        "it does not treat Maru2022 as a privileged adjudication.",
        "",
        "## Headline Agreement",
        "",
        markdown_table(
            headers=["Metric", "Fine WordNet", "Glite coarse"],
            rows=agreement_rows(data=data),
        ),
        "",
        "Fine-grained agreement is strong for a set that was deliberately selected to be "
        f"suspicious: all three reviewers agree on {fine_all_three} items, and exactly "
        f"two agree on {fine_exactly_two}. Coarsening resolves many apparent sense-key "
        f"splits: Glite all-three agreement rises to {glite_all_three}.",
        "",
        "## Agreement Pattern Relative To Maru2022",
        "",
        markdown_table(
            headers=["Pattern", "Fine WordNet", "Glite coarse"],
            rows=relationship_rows(data=data),
        ),
        "",
        "This table explains why labels changed. At the fine level, "
        f"{fine_all_three_correction} "
        "items have unanimous reviewer agreement on a label different from Maru2022, and "
        f"{fine_exactly_two_correction} "
        "have a two-reviewer majority different from Maru2022. Those are the main sources "
        "of lexEN corrections. The no-consensus group is removed from the benchmark because "
        "it does not provide enough reviewer agreement to assign a reliable replacement.",
        "",
        "## Maru2022 Label Support Split",
        "",
        markdown_table(
            headers=["Support", "Fine WordNet", "Glite coarse"],
            rows=support_rows(data=data),
        ),
        "",
        "Only "
        f"{count_percent_text(value=data.metrics.fine.gold_support_counts[3])} fine-grained "
        "items received three-reviewer support for the Maru2022 label. At the Glite level, "
        f"{count_percent_text(value=data.metrics.glite.gold_support_counts[3])} receive "
        "three-reviewer support, showing that many disagreements are between closely related "
        "fine WordNet senses rather than between clearly different coarse meanings.",
        "",
        "## Pairwise Agreement",
        "",
        "Each 3x3 matrix cell compares the row reviewer with the column reviewer. Raw "
        "agreement cells show the percentage and the matching-item count. Diagonal cells "
        "are self-comparisons included only to keep the reviewer grid explicit.",
        "",
        "### Fine Raw Agreement Matrix",
        "",
        markdown_table(
            headers=["Reviewer", *data.reviewers],
            rows=pairwise_matrix_rows(
                data=data,
                granularity=Granularity.FINE,
                metric="raw_agreement",
            ),
        ),
        "",
        "### Glite Raw Agreement Matrix",
        "",
        markdown_table(
            headers=["Reviewer", *data.reviewers],
            rows=pairwise_matrix_rows(
                data=data,
                granularity=Granularity.GLITE,
                metric="raw_agreement",
            ),
        ),
        "",
        "### Fine Cohen's Kappa Matrix",
        "",
        markdown_table(
            headers=["Reviewer", *data.reviewers],
            rows=pairwise_matrix_rows(
                data=data,
                granularity=Granularity.FINE,
                metric="cohen_kappa",
            ),
        ),
        "",
        "### Glite Cohen's Kappa Matrix",
        "",
        markdown_table(
            headers=["Reviewer", *data.reviewers],
            rows=pairwise_matrix_rows(
                data=data,
                granularity=Granularity.GLITE,
                metric="cohen_kappa",
            ),
        ),
        "",
        "### Compact Pairwise Summary",
        "",
        markdown_table(
            headers=["Pair", "Fine raw", "Fine kappa", "Glite raw", "Glite kappa"],
            rows=pairwise_summary_rows(data=data),
        ),
        "",
        "Pairwise coefficients are reported for both granularities. Raw agreement is the "
        "direct share of matching labels. Cohen's kappa corrects for the label distribution "
        "in each pair, which matters because cannot-answer and high-frequency senses are "
        "not evenly distributed across the reviewed set.",
        "",
        "## Reviewer Answer Shape",
        "",
        markdown_table(
            headers=["Reviewer", "Single", "Multi", "Cannot", "Comments", "Notes"],
            rows=verdict_rows(data=data),
        ),
        "",
        "These counts are behavior diagnostics, not quality rankings. Multi-sense answers "
        "capture cases where a lexicographer judged several WordNet keys acceptable. "
        "Cannot-answer tags capture source-text defects, inventory gaps, and cases where "
        "no listed sense applied.",
        "",
        "## How Each Reviewer Related To Maru2022",
        "",
        "### Fine WordNet",
        "",
        markdown_table(
            headers=[
                "Relation",
                *[reviewer_name(reviewer=reviewer) for reviewer in data.reviewers],
            ],
            rows=maru_relation_rows(data=data, granularity=Granularity.FINE),
        ),
        "",
        "### Glite Coarse",
        "",
        markdown_table(
            headers=[
                "Relation",
                *[reviewer_name(reviewer=reviewer) for reviewer in data.reviewers],
            ],
            rows=maru_relation_rows(data=data, granularity=Granularity.GLITE),
        ),
        "",
        "## Glite Coarsening Effect",
        "",
        "Glite coarsening resolves "
        f"{glite_resolution_text(data=data)} of fine-grained non-unanimous cases into "
        "all-three agreement. The report needed "
        f"{data.metrics.glite_coverage.required_sense_keys} distinct WordNet sense keys and "
        f"mapped {data.metrics.glite_coverage.mapped_sense_keys} of them. Unmapped keys are "
        "preserved as explicit `unmapped:<sense_key>` concepts rather than silently dropped.",
        "",
        "## Disagreement Concentration",
        "",
        "### Part Of Speech",
        "",
        markdown_table(
            headers=[
                "POS",
                "Items",
                "Fine all 3",
                "Fine 2/3",
                "Fine differ",
                "Glite all 3",
                "Glite 2/3",
                "Glite differ",
            ],
            rows=group_rows(groups=data.metrics.pos_groups),
        ),
        "",
        "### Source Dataset",
        "",
        markdown_table(
            headers=[
                "Source",
                "Items",
                "Fine all 3",
                "Fine 2/3",
                "Fine differ",
                "Glite all 3",
                "Glite 2/3",
                "Glite differ",
            ],
            rows=group_rows(groups=data.metrics.source_groups),
        ),
        "",
        "### Frequent Headwords In The Reviewed Set",
        "",
        markdown_table(
            headers=[
                "Headword",
                "Items",
                "Fine all 3",
                "Fine 2/3",
                "Fine differ",
                "Glite all 3",
                "Glite 2/3",
                "Glite differ",
            ],
            rows=group_rows(groups=data.metrics.headword_groups),
        ),
        "",
        "## Cannot-Answer Reasons",
        "",
        f"At least one reviewer marked {data.metrics.cannot_answer.at_least_one_unanswerable} "
        "items unanswerable. All three reviewers marked "
        f"{data.metrics.cannot_answer.all_three_unanswerable} items unanswerable.",
        "",
        markdown_table(
            headers=["Reason", *data.reviewers],
            rows=cannot_answer_reason_rows(data=data),
        ),
        "",
        "### Cannot-Answer Consensus",
        "",
        markdown_table(
            headers=["Consensus strength", "Items"],
            rows=cannot_answer_consensus_rows(data=data),
        ),
        "",
        "The strongest unusable-item signal is the at-least-two-reviewer subset: "
        f"{at_least_two_unanswerable} items have at least two independent cannot-answer "
        "judgements. This includes "
        f"{data.metrics.cannot_answer.exactly_two_unanswerable} exactly-two cases and "
        f"{data.metrics.cannot_answer.all_three_unanswerable} all-three cases. These are "
        "not ordinary sense disagreements; they indicate that the item, context, or "
        "available WordNet inventory did not support a reliable fine-grained answer.",
        "",
        markdown_table(
            headers=["Reason present in at-least-two subset", "Items"],
            rows=cannot_answer_at_least_two_reason_rows(data=data),
        ),
        "",
        "### Cannot-Answer By Document And Reviewer Support",
        "",
        "This table shows document concentration for items where at least two reviewers "
        "marked cannot answer, split into exactly-two and all-three reviewer support.",
        "",
        markdown_table(
            headers=["Reviewer support", "Document", "Items"],
            rows=cannot_answer_document_support_rows(data=data),
        ),
        "",
        "### Defective Source Text",
        "",
        "Input-defective tags identify cases where the sentence, tokenization, target span, "
        "or source material prevents a reliable WSD judgement. This table is split by how "
        "many reviewers used the input-defective reason; it is not limited to unanimous "
        "cases.",
        "",
        markdown_table(
            headers=["Reviewer support", "Document", "Items"],
            rows=input_defective_document_support_rows(data=data),
        ),
        "",
        "## Removed Reviewed Items",
        "",
        "lexEN v1 removes reviewed suspicious items when the review evidence does not "
        "provide a usable two-reviewer fine-grained sense label. No Maru2022 fallback label "
        "is used for these cases in the benchmark exports.",
        "",
        markdown_table(
            headers=["Removal evidence", "Items", "Benchmark action"],
            rows=removed_reviewed_item_rows(data=data),
        ),
        "",
        "### No Two-Reviewer Fine Agreement",
        "",
        "The 29 no-consensus items are removed because all three reviewers selected "
        "different fine-grained answers. Some become closer after Glite coarsening, but "
        "lexEN v1 is a fine-grained WordNet benchmark, so coarse agreement is not enough "
        "to keep a scorable item.",
        "",
        markdown_table(headers=["Group", "Items"], rows=no_consensus_summary_rows(data=data)),
        "",
        markdown_table(headers=["Signal", "Items"], rows=no_consensus_support_rows(data=data)),
        "",
        markdown_table(
            headers=["Reviewer evidence", "Items"],
            rows=no_consensus_evidence_rows(data=data),
        ),
        "",
        "### No-Consensus Item Audit",
        "",
        markdown_table(
            headers=[
                "Item",
                "Lemma/POS/source",
                "Fine Maru support",
                "Glite level",
                "Glite Maru support",
                "Cannot votes",
                *data.reviewers,
            ],
            rows=no_consensus_item_rows(data=data),
        ),
        "",
        "### Manual Sample Review",
        "",
        "A manual review of 20 no-consensus items found no case that was safe to keep by "
        "falling back to the Maru2022 label. The common failure modes were inventory gaps, "
        "fixed expressions, figurative uses, and fine WordNet distinctions that the context "
        "does not reliably determine.",
        "",
        markdown_table(
            headers=["Item", "Lemma/POS/source", "Recommendation", "Rationale"],
            rows=no_consensus_sample_rows(data=data),
        ),
        "",
        "## What The Agreement Shows",
        "",
        "The reviewer evidence supports a conservative benchmark construction policy. "
        "Unanimous and two-reviewer fine-grained agreements provide direct corrections to "
        "Maru2022. Cases where two reviewers mark the item unanswerable and cases with no "
        "fine-grained majority are excluded from the benchmark release but remain visible "
        "in this report, so downstream users can audit them.",
        "",
        "## Technical Method",
        "",
        "The report is generated by `scripts/build_agreement_report.py`. It reads "
        "`data/lexen-v1/reviews.jsonl`, "
        "`sources/selection/lexicographer_review.jsonl.gz`, and the Glite mapping files. "
        "The script writes Markdown, HTML, PDF, `metrics.json`, "
        "`per_item_agreement.jsonl`, and chart images under "
        "`reports/rf-pw-ph-2026-06-13/`.",
        "",
        *appendix_markdown(data=data),
    ]
    output_path.write_text("\n".join(lines) + "\n", encoding="utf-8")
