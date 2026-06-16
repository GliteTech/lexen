"""Render the agreement report as PDF."""

from __future__ import annotations

from html import escape
from pathlib import Path
from typing import Any

from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import inch
from reportlab.platypus import (
    CondPageBreak,
    Image,
    PageBreak,
    Paragraph,
    SimpleDocTemplate,
    Spacer,
    Table,
    TableStyle,
)
from reportlab.platypus.tableofcontents import TableOfContents

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
    ItemAgreement,
    ReportData,
    ReviewerMaruRelation,
)
from lexen.agreement_report.paths import REPORT_TITLE, REPORT_VERSION
from lexen.agreement_report.report_content import (
    PairwiseMatrixMetric,
    agreement_short_text,
    appendix_group_anchor,
    appendix_group_summary_rows,
    cannot_answer_at_least_two_reason_rows,
    cannot_answer_consensus_rows,
    cannot_answer_document_support_rows,
    clean_optional_text,
    heatmap_color_hex,
    input_defective_document_support_rows,
    label_plain_lines,
    marked_sentence_text,
    no_consensus_evidence_rows,
    no_consensus_item_rows,
    no_consensus_sample_rows,
    no_consensus_summary_rows,
    no_consensus_support_rows,
    pairwise_matrix_cell_text,
    pairwise_matrix_cells,
    pairwise_summary_rows,
    reason_label,
    removed_reviewed_item_rows,
    reviewer_label,
    reviewer_name,
)

CONTENT_WIDTH: float = 7.15 * inch
FOOTER_Y: float = 0.32 * inch
APPENDIX_ITEM_MIN_START_HEIGHT: float = 3.35 * inch


def styles() -> dict[str, ParagraphStyle]:
    base = getSampleStyleSheet()
    return {
        "title": ParagraphStyle(
            "ReportTitle",
            parent=base["Title"],
            fontName="Helvetica-Bold",
            fontSize=23,
            leading=28,
            textColor=colors.HexColor("#17202a"),
            spaceAfter=12,
        ),
        "h1": ParagraphStyle(
            "ReportH1",
            parent=base["Heading1"],
            fontName="Helvetica-Bold",
            fontSize=16,
            leading=20,
            textColor=colors.HexColor("#17202a"),
            spaceBefore=12,
            spaceAfter=8,
        ),
        "h2": ParagraphStyle(
            "ReportH2",
            parent=base["Heading2"],
            fontName="Helvetica-Bold",
            fontSize=12.5,
            leading=16,
            textColor=colors.HexColor("#17202a"),
            spaceBefore=8,
            spaceAfter=5,
        ),
        "h3": ParagraphStyle(
            "ReportH3",
            parent=base["Heading3"],
            fontName="Helvetica-Bold",
            fontSize=10.5,
            leading=13,
            textColor=colors.HexColor("#17202a"),
            spaceBefore=7,
            spaceAfter=4,
        ),
        "toc_title": ParagraphStyle(
            "ReportTOCTitle",
            parent=base["Heading1"],
            fontName="Helvetica-Bold",
            fontSize=16,
            leading=20,
            textColor=colors.HexColor("#17202a"),
            spaceBefore=10,
            spaceAfter=10,
        ),
        "toc_0": ParagraphStyle(
            "ReportTOCLevel0",
            parent=base["BodyText"],
            fontName="Helvetica-Bold",
            fontSize=9.6,
            leading=12,
            leftIndent=0,
            firstLineIndent=0,
            textColor=colors.HexColor("#17202a"),
            spaceBefore=5,
        ),
        "toc_1": ParagraphStyle(
            "ReportTOCLevel1",
            parent=base["BodyText"],
            fontName="Helvetica",
            fontSize=8.4,
            leading=10.5,
            leftIndent=14,
            firstLineIndent=0,
            textColor=colors.HexColor("#293441"),
            spaceBefore=2,
        ),
        "body": ParagraphStyle(
            "ReportBody",
            parent=base["BodyText"],
            fontName="Helvetica",
            fontSize=9.2,
            leading=12.4,
            textColor=colors.HexColor("#293441"),
            spaceAfter=6,
        ),
        "small": ParagraphStyle(
            "ReportSmall",
            parent=base["BodyText"],
            fontName="Helvetica",
            fontSize=7.2,
            leading=9.2,
            textColor=colors.HexColor("#293441"),
            spaceAfter=3,
        ),
        "table": ParagraphStyle(
            "ReportTable",
            parent=base["BodyText"],
            fontName="Helvetica",
            fontSize=7.2,
            leading=9.2,
            textColor=colors.HexColor("#17202a"),
        ),
        "appendix_item_title": ParagraphStyle(
            "ReportAppendixItemTitle",
            parent=base["BodyText"],
            fontName="Helvetica-Bold",
            fontSize=9.4,
            leading=11.5,
            textColor=colors.white,
            spaceBefore=6,
            spaceAfter=0,
        ),
        "appendix_meta": ParagraphStyle(
            "ReportAppendixMeta",
            parent=base["BodyText"],
            fontName="Helvetica",
            fontSize=7.4,
            leading=9.4,
            textColor=colors.HexColor("#293441"),
            spaceAfter=3,
        ),
        "appendix_context": ParagraphStyle(
            "ReportAppendixContext",
            parent=base["BodyText"],
            fontName="Helvetica",
            fontSize=8.2,
            leading=10.8,
            textColor=colors.HexColor("#17202a"),
            spaceAfter=4,
        ),
        "appendix_label_title": ParagraphStyle(
            "ReportAppendixLabelTitle",
            parent=base["BodyText"],
            fontName="Helvetica-Bold",
            fontSize=7.9,
            leading=10,
            textColor=colors.HexColor("#17202a"),
            spaceBefore=2,
            spaceAfter=2,
        ),
        "appendix_bullet": ParagraphStyle(
            "ReportAppendixBullet",
            parent=base["BodyText"],
            fontName="Helvetica",
            fontSize=6.9,
            leading=8.7,
            leftIndent=9,
            firstLineIndent=-5,
            textColor=colors.HexColor("#293441"),
            spaceAfter=2,
        ),
        "appendix_panel_title": ParagraphStyle(
            "ReportAppendixPanelTitle",
            parent=base["BodyText"],
            fontName="Helvetica-Bold",
            fontSize=8.1,
            leading=10,
            textColor=colors.HexColor("#17202a"),
        ),
        "appendix_panel_body": ParagraphStyle(
            "ReportAppendixPanelBody",
            parent=base["BodyText"],
            fontName="Helvetica",
            fontSize=7.4,
            leading=9.5,
            textColor=colors.HexColor("#293441"),
        ),
        "appendix_row_label": ParagraphStyle(
            "ReportAppendixRowLabel",
            parent=base["BodyText"],
            fontName="Helvetica-Bold",
            fontSize=7.5,
            leading=9.4,
            textColor=colors.HexColor("#17202a"),
        ),
        "appendix_row_value": ParagraphStyle(
            "ReportAppendixRowValue",
            parent=base["BodyText"],
            fontName="Helvetica",
            fontSize=7.0,
            leading=9.0,
            leftIndent=7,
            firstLineIndent=-5,
            textColor=colors.HexColor("#293441"),
        ),
        "appendix_note": ParagraphStyle(
            "ReportAppendixNote",
            parent=base["BodyText"],
            fontName="Helvetica",
            fontSize=6.9,
            leading=8.7,
            textColor=colors.HexColor("#293441"),
            spaceAfter=3,
        ),
        "appendix_agreement": ParagraphStyle(
            "ReportAppendixAgreement",
            parent=base["BodyText"],
            fontName="Helvetica-Bold",
            fontSize=7,
            leading=8.8,
            textColor=colors.HexColor("#1b6f5d"),
            spaceAfter=7,
        ),
        "table_header": ParagraphStyle(
            "ReportTableHeader",
            parent=base["BodyText"],
            fontName="Helvetica-Bold",
            fontSize=7.2,
            leading=9.2,
            textColor=colors.white,
        ),
    }


class ReportDocTemplate(SimpleDocTemplate):  # type: ignore[misc]
    """SimpleDocTemplate with PDF outline and generated TOC support."""

    def afterFlowable(self, flowable: Any) -> None:
        bookmark_name = getattr(flowable, "_bookmark_name", None)
        if not isinstance(bookmark_name, str):
            return
        toc_title = getattr(flowable, "_toc_title", "")
        toc_level = getattr(flowable, "_toc_level", 0)
        if not isinstance(toc_title, str) or not isinstance(toc_level, int):
            return
        self.canv.bookmarkPage(bookmark_name)
        self.canv.addOutlineEntry(toc_title, bookmark_name, level=toc_level, closed=False)
        self.notify("TOCEntry", (toc_level, toc_title, self.page, bookmark_name))


def paragraph(*, text: str, style: ParagraphStyle) -> Paragraph:
    return Paragraph(escape(text), style)


def anchored_heading(
    *,
    text: str,
    anchor: str,
    style: ParagraphStyle,
    toc_level: int,
) -> Paragraph:
    heading = Paragraph(f'<a name="{escape(anchor)}"/>{escape(text)}', style)
    heading._bookmark_name = anchor
    heading._toc_title = text
    heading._toc_level = toc_level
    return heading


def add_heading(
    *,
    story: list[Any],
    text: str,
    anchor: str,
    style_map: dict[str, ParagraphStyle],
    toc_level: int = 0,
    style_name: str = "h1",
) -> None:
    story.append(
        anchored_heading(
            text=text,
            anchor=anchor,
            style=style_map[style_name],
            toc_level=toc_level,
        )
    )


def contents_flowable(*, style_map: dict[str, ParagraphStyle]) -> TableOfContents:
    toc = TableOfContents()
    toc.levelStyles = [style_map["toc_0"], style_map["toc_1"]]
    toc.dotsMinLevel = 0
    return toc


def draw_page_footer(canvas: Any, document: Any) -> None:
    canvas.saveState()
    canvas.setStrokeColor(colors.HexColor("#d8dee8"))
    canvas.setLineWidth(0.35)
    canvas.line(
        document.leftMargin,
        FOOTER_Y + 0.12 * inch,
        A4[0] - document.rightMargin,
        FOOTER_Y + 0.12 * inch,
    )
    canvas.setFillColor(colors.HexColor("#5d6979"))
    canvas.setFont("Helvetica", 7.2)
    canvas.drawString(document.leftMargin, FOOTER_Y, REPORT_TITLE)
    canvas.drawRightString(A4[0] - document.rightMargin, FOOTER_Y, f"Page {document.page}")
    canvas.restoreState()


def table_cell(*, text: str, style: ParagraphStyle) -> Paragraph:
    return Paragraph(escape(text), style)


def rich_cell(*, html: str, style: ParagraphStyle) -> Paragraph:
    return Paragraph(html, style)


def table_flowable(
    *,
    headers: list[str],
    rows: list[list[str]],
    style_map: dict[str, ParagraphStyle],
    col_widths: list[float] | None = None,
) -> Table:
    data: list[list[Paragraph]] = [
        [table_cell(text=header, style=style_map["table_header"]) for header in headers]
    ]
    for row in rows:
        data.append([table_cell(text=cell, style=style_map["table"]) for cell in row])
    table = Table(data, repeatRows=1, colWidths=col_widths, hAlign="LEFT")
    table.setStyle(
        TableStyle(
            [
                ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#17202a")),
                ("TEXTCOLOR", (0, 0), (-1, 0), colors.white),
                ("GRID", (0, 0), (-1, -1), 0.35, colors.HexColor("#d8dee8")),
                ("VALIGN", (0, 0), (-1, -1), "TOP"),
                ("ROWBACKGROUNDS", (0, 1), (-1, -1), [colors.white, colors.HexColor("#f6f8fb")]),
                ("LEFTPADDING", (0, 0), (-1, -1), 4),
                ("RIGHTPADDING", (0, 0), (-1, -1), 4),
                ("TOPPADDING", (0, 0), (-1, -1), 4),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 4),
            ]
        )
    )
    return table


def heatmap_cell_paragraph(
    *,
    text: str,
    metric: PairwiseMatrixMetric,
    style: ParagraphStyle,
) -> Paragraph:
    if metric == "raw_agreement":
        percent, counts = text.split(" ", maxsplit=1)
        html = (
            f"<b>{escape(percent)}</b><br/>"
            f'<font size="6.2">{escape(counts.strip("()"))} items</font>'
        )
        return Paragraph(html, style)
    return Paragraph(f"<b>{escape(text)}</b>", style)


def pairwise_heatmap_flowable(
    *,
    data: ReportData,
    granularity: Granularity,
    metric: PairwiseMatrixMetric,
    style_map: dict[str, ParagraphStyle],
) -> Table:
    matrix_rows = pairwise_matrix_cells(
        data=data,
        granularity=granularity,
        metric=metric,
    )
    table_data: list[list[Paragraph]] = [
        [
            table_cell(text=header, style=style_map["table_header"])
            for header in ["Reviewer", *data.reviewers]
        ]
    ]
    style_commands: list[tuple[Any, ...]] = [
        ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#17202a")),
        ("TEXTCOLOR", (0, 0), (-1, 0), colors.white),
        ("GRID", (0, 0), (-1, -1), 0.35, colors.HexColor("#d8dee8")),
        ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
        ("ALIGN", (0, 0), (-1, -1), "CENTER"),
        ("LEFTPADDING", (0, 0), (-1, -1), 5),
        ("RIGHTPADDING", (0, 0), (-1, -1), 5),
        ("TOPPADDING", (0, 0), (-1, -1), 5),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 5),
    ]
    for row_index, row_cells in enumerate(matrix_rows, start=1):
        table_row = [table_cell(text=row_cells[0].row_reviewer, style=style_map["table"])]
        style_commands.append(
            ("BACKGROUND", (0, row_index), (0, row_index), colors.HexColor("#eef3f8"))
        )
        for column_index, cell in enumerate(row_cells, start=1):
            text = pairwise_matrix_cell_text(cell=cell, metric=metric)
            table_row.append(
                heatmap_cell_paragraph(
                    text=text,
                    metric=metric,
                    style=style_map["table"],
                )
            )
            background = (
                "#f1f4f8"
                if cell.diagonal
                else heatmap_color_hex(
                    value=cell.value,
                    metric=metric,
                )
            )
            style_commands.append(
                (
                    "BACKGROUND",
                    (column_index, row_index),
                    (column_index, row_index),
                    colors.HexColor(background),
                )
            )
        table_data.append(table_row)
    table = Table(
        table_data,
        repeatRows=1,
        colWidths=[1.2 * inch, 1.45 * inch, 1.45 * inch, 1.45 * inch],
        hAlign="LEFT",
    )
    table.setStyle(TableStyle(style_commands))
    return table


def add_pairwise_heatmap(
    *,
    story: list[Any],
    title: str,
    data: ReportData,
    granularity: Granularity,
    metric: PairwiseMatrixMetric,
    style_map: dict[str, ParagraphStyle],
) -> None:
    story.append(paragraph(text=title, style=style_map["h2"]))
    story.append(
        pairwise_heatmap_flowable(
            data=data,
            granularity=granularity,
            metric=metric,
            style_map=style_map,
        )
    )
    story.append(Spacer(width=1, height=0.10 * inch))


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


def relationship_rows(*, data: ReportData) -> list[list[str]]:
    return [
        [
            relation_label(relation=relation),
            count_percent_text(value=data.metrics.fine.relationship_counts[relation]),
            count_percent_text(value=data.metrics.glite.relationship_counts[relation]),
        ]
        for relation in data.metrics.fine.relationship_counts
    ]


def verdict_shape_rows(*, data: ReportData) -> list[list[str]]:
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


def no_consensus_pdf_item_rows(*, data: ReportData) -> list[list[str]]:
    rows: list[list[str]] = []
    for row in no_consensus_item_rows(data=data):
        rows.append(
            [
                row[0],
                row[1],
                row[2],
                f"{row[3]}; Maru2022 support {row[4]}",
                row[5],
            ]
        )
    return rows


def add_chart(
    *,
    story: list[Any],
    chart_path: Path,
    title: str,
    style_map: dict[str, ParagraphStyle],
    caption: str,
    height: float = 3.55 * inch,
) -> None:
    story.append(paragraph(text=title, style=style_map["h2"]))
    story.append(Image(str(chart_path), width=CONTENT_WIDTH, height=height))
    story.append(paragraph(text=caption, style=style_map["small"]))
    story.append(Spacer(width=1, height=0.14 * inch))


def add_label_block(
    *,
    story: list[Any],
    title: str,
    lines: list[str],
    style_map: dict[str, ParagraphStyle],
) -> None:
    story.append(paragraph(text=title, style=style_map["appendix_label_title"]))
    for line in lines:
        story.append(paragraph(text=f"- {line}", style=style_map["appendix_bullet"]))


def appendix_label_value_html(*, lines: list[str]) -> str:
    return "<br/>".join(f"- {escape(line)}" for line in lines)


def appendix_reviewer_value_html(
    *,
    data: ReportData,
    item: ItemAgreement,
    reviewer: str,
) -> str:
    lines = label_plain_lines(
        data=data,
        label=item.reviewer_fine[reviewer],
        include_examples=True,
    )
    html_parts = [appendix_label_value_html(lines=lines)]
    note = clean_optional_text(value=item.reviewer_notes[reviewer])
    comment = clean_optional_text(value=item.reviewer_comments[reviewer])
    if note is not None:
        html_parts.append(f'<font color="#6c4b16"><b>Note:</b> {escape(note)}</font>')
    if comment is not None:
        html_parts.append(f'<font color="#6c4b16"><b>Comment:</b> {escape(comment)}</font>')
    return "<br/>".join(html_parts)


def appendix_panel_flowable(
    *,
    title: str,
    body_html: str,
    style_map: dict[str, ParagraphStyle],
    width: float = CONTENT_WIDTH,
    title_background: str = "#e8f4f0",
    body_background: str = "#ffffff",
    border_color: str = "#d8dee8",
) -> Table:
    table = Table(
        [
            [table_cell(text=title, style=style_map["appendix_panel_title"])],
            [rich_cell(html=body_html, style=style_map["appendix_panel_body"])],
        ],
        colWidths=[width],
        hAlign="LEFT",
        splitByRow=0,
    )
    table.setStyle(
        TableStyle(
            [
                ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor(title_background)),
                ("BACKGROUND", (0, 1), (-1, 1), colors.HexColor(body_background)),
                ("BOX", (0, 0), (-1, -1), 0.35, colors.HexColor(border_color)),
                ("LINEBELOW", (0, 0), (-1, 0), 0.35, colors.HexColor(border_color)),
                ("VALIGN", (0, 0), (-1, -1), "TOP"),
                ("LEFTPADDING", (0, 0), (-1, -1), 7),
                ("RIGHTPADDING", (0, 0), (-1, -1), 7),
                ("TOPPADDING", (0, 0), (-1, -1), 5),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 5),
            ]
        )
    )
    return table


def reviewer_answer_is_compact(
    *,
    data: ReportData,
    item: ItemAgreement,
    reviewer: str,
) -> bool:
    if clean_optional_text(value=item.reviewer_notes[reviewer]) is not None:
        return False
    if clean_optional_text(value=item.reviewer_comments[reviewer]) is not None:
        return False
    lines = label_plain_lines(
        data=data,
        label=item.reviewer_fine[reviewer],
        include_examples=True,
    )
    return len(lines) == 1 and len(lines[0]) <= 245


def appendix_reviewer_grid_flowable(
    *,
    data: ReportData,
    item: ItemAgreement,
    style_map: dict[str, ParagraphStyle],
) -> Table:
    gap = 0.08 * inch
    panel_width = (CONTENT_WIDTH - (2 * gap)) / 3
    panels = [
        appendix_panel_flowable(
            title=reviewer_label(reviewer=reviewer),
            body_html=appendix_reviewer_value_html(
                data=data,
                item=item,
                reviewer=reviewer,
            ),
            style_map=style_map,
            width=panel_width,
        )
        for reviewer in data.reviewers
    ]
    table = Table(
        [panels],
        colWidths=[panel_width, panel_width, panel_width],
        hAlign="LEFT",
    )
    table.setStyle(
        TableStyle(
            [
                ("VALIGN", (0, 0), (-1, -1), "TOP"),
                ("LEFTPADDING", (0, 0), (-1, -1), 0),
                ("RIGHTPADDING", (0, 0), (-1, -1), gap),
                ("RIGHTPADDING", (-1, 0), (-1, -1), 0),
                ("TOPPADDING", (0, 0), (-1, -1), 0),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 0),
            ]
        )
    )
    return table


def appendix_header_flowable(
    *,
    data: ReportData,
    item: ItemAgreement,
    item_id_prefix: str,
    style_map: dict[str, ParagraphStyle],
) -> Table:
    table = Table(
        [
            [
                table_cell(
                    text=f"{item_id_prefix}. {item.item_id}",
                    style=style_map["appendix_item_title"],
                )
            ],
            [
                table_cell(
                    text=(
                        f"Lemma/POS/source: {item.lemma} / {item.pos} / {item.source_dataset} "
                        f"({item.document_id})"
                    ),
                    style=style_map["appendix_meta"],
                )
            ],
            [
                table_cell(
                    text=(
                        "Context: "
                        f"{marked_sentence_text(item=item, open_marker='[', close_marker=']')}"
                    ),
                    style=style_map["appendix_context"],
                )
            ],
        ],
        colWidths=[CONTENT_WIDTH],
        hAlign="LEFT",
        splitByRow=1,
    )
    table.setStyle(
        TableStyle(
            [
                ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#17202a")),
                ("BACKGROUND", (0, 1), (-1, 1), colors.HexColor("#eef3f8")),
                ("BACKGROUND", (0, 2), (-1, 2), colors.HexColor("#f6f8fb")),
                ("BOX", (0, 0), (-1, -1), 0.35, colors.HexColor("#d8dee8")),
                ("LINEBELOW", (0, 0), (-1, 0), 0.35, colors.HexColor("#d8dee8")),
                ("LINEBELOW", (0, 1), (-1, 1), 0.35, colors.HexColor("#d8dee8")),
                ("VALIGN", (0, 0), (-1, -1), "TOP"),
                ("LEFTPADDING", (0, 0), (-1, -1), 7),
                ("RIGHTPADDING", (0, 0), (-1, -1), 7),
                ("TOPPADDING", (0, 0), (-1, -1), 5),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 5),
                ("TOPPADDING", (0, 0), (-1, 0), 8),
                ("BOTTOMPADDING", (0, 0), (-1, 0), 8),
            ]
        )
    )
    return table


def add_reviewer_block(
    *,
    story: list[Any],
    data: ReportData,
    item: ItemAgreement,
    reviewer: str,
    style_map: dict[str, ParagraphStyle],
) -> None:
    lines = label_plain_lines(
        data=data,
        label=item.reviewer_fine[reviewer],
        include_examples=True,
    )
    note = clean_optional_text(value=item.reviewer_notes[reviewer])
    comment = clean_optional_text(value=item.reviewer_comments[reviewer])
    add_label_block(
        story=story,
        title=reviewer_label(reviewer=reviewer),
        lines=lines,
        style_map=style_map,
    )
    if note is not None:
        story.append(paragraph(text=f"Note: {note}", style=style_map["appendix_note"]))
    if comment is not None:
        story.append(paragraph(text=f"Comment: {comment}", style=style_map["appendix_note"]))


def add_appendix_item(
    *,
    story: list[Any],
    data: ReportData,
    item: ItemAgreement,
    item_id_prefix: str,
    style_map: dict[str, ParagraphStyle],
) -> None:
    story.append(CondPageBreak(APPENDIX_ITEM_MIN_START_HEIGHT))
    story.append(
        appendix_header_flowable(
            data=data,
            item=item,
            item_id_prefix=item_id_prefix,
            style_map=style_map,
        )
    )
    story.append(Spacer(width=1, height=0.06 * inch))
    story.append(
        appendix_panel_flowable(
            title="Maru2022 label",
            body_html=appendix_label_value_html(
                lines=label_plain_lines(
                    data=data,
                    label=item.maru_fine,
                    include_examples=True,
                )
            ),
            style_map=style_map,
        )
    )
    story.append(Spacer(width=1, height=0.05 * inch))
    if all(
        reviewer_answer_is_compact(data=data, item=item, reviewer=reviewer)
        for reviewer in data.reviewers
    ):
        story.append(
            appendix_reviewer_grid_flowable(
                data=data,
                item=item,
                style_map=style_map,
            )
        )
        story.append(Spacer(width=1, height=0.05 * inch))
    else:
        for reviewer in data.reviewers:
            story.append(
                appendix_panel_flowable(
                    title=reviewer_label(reviewer=reviewer),
                    body_html=appendix_reviewer_value_html(
                        data=data,
                        item=item,
                        reviewer=reviewer,
                    ),
                    style_map=style_map,
                )
            )
            story.append(Spacer(width=1, height=0.05 * inch))
    story.append(
        appendix_panel_flowable(
            title="Agreement",
            body_html=escape(agreement_short_text(item=item)),
            style_map=style_map,
            title_background="#fff4df",
            body_background="#fffaf0",
            border_color="#ead7b3",
        )
    )
    story.append(Spacer(width=1, height=0.14 * inch))


def add_section_table(
    *,
    story: list[Any],
    title: str,
    headers: list[str],
    rows: list[list[str]],
    style_map: dict[str, ParagraphStyle],
    col_widths: list[float] | None = None,
    title_style: str = "h1",
) -> None:
    story.append(paragraph(text=title, style=style_map[title_style]))
    story.append(
        table_flowable(
            headers=headers,
            rows=rows,
            style_map=style_map,
            col_widths=col_widths,
        )
    )
    story.append(Spacer(width=1, height=0.08 * inch))


def render_pdf(
    *,
    data: ReportData,
    chart_paths: dict[str, Path],
    output_path: Path,
) -> None:
    output_path.parent.mkdir(parents=True, exist_ok=True)
    style_map = styles()
    document = ReportDocTemplate(
        str(output_path),
        pagesize=A4,
        rightMargin=0.48 * inch,
        leftMargin=0.48 * inch,
        topMargin=0.55 * inch,
        bottomMargin=0.68 * inch,
        title=REPORT_TITLE,
        invariant=1,
    )
    story: list[Any] = []
    story.append(paragraph(text=REPORT_TITLE, style=style_map["title"]))
    story.append(
        paragraph(
            text=(
                f"Report date: {REPORT_VERSION}. This report audits 363 suspicious Maru2022 "
                "validation items reviewed independently by RF, PW, and PH. Maru2022 labels "
                "are source labels under review, not a privileged adjudication."
            ),
            style=style_map["body"],
        )
    )
    story.append(paragraph(text="Contents", style=style_map["toc_title"]))
    story.append(contents_flowable(style_map=style_map))
    story.append(PageBreak())

    add_heading(
        story=story,
        text="What This Report Includes",
        anchor="what-this-report-includes",
        style_map=style_map,
    )
    story.append(
        paragraph(
            text=(
                "Fine WordNet agreement, Glite-coarsened agreement, pairwise coefficients, "
                "reviewer answer shape, Maru2022 label support, concentration by item type, "
                "cannot-answer evidence, and a full appendix for all reviewed items."
            ),
            style=style_map["body"],
        )
    )
    add_section_table(
        story=story,
        title="Headline Metrics",
        headers=["Metric", "Value"],
        rows=[
            ["Reviewed items", str(data.metrics.reviewed_items)],
            [
                "Fine all-three agreement",
                count_percent_text(value=data.metrics.fine.level_counts[AgreementLevel.ALL_THREE]),
            ],
            [
                "Glite all-three agreement",
                count_percent_text(value=data.metrics.glite.level_counts[AgreementLevel.ALL_THREE]),
            ],
            ["Fine Fleiss kappa", kappa_text(value=data.metrics.fine.fleiss_kappa)],
            ["Glite Fleiss kappa", kappa_text(value=data.metrics.glite.fleiss_kappa)],
        ],
        style_map=style_map,
        col_widths=[3.35 * inch, 3.65 * inch],
        title_style="h2",
    )
    add_heading(
        story=story,
        text="How To Read The Numbers",
        anchor="how-to-read-the-numbers",
        style_map=style_map,
    )
    story.append(
        paragraph(
            text=(
                "Fine WordNet agreement compares exact WordNet sense-key sets. Glite "
                "agreement first maps those sense keys to coarse Glite concepts. Maru2022 "
                "support counts how many reviewers selected the Maru2022 source label for "
                "an item."
            ),
            style=style_map["body"],
        )
    )
    story.append(PageBreak())

    add_heading(
        story=story,
        text="Headline Agreement",
        anchor="headline-agreement",
        style_map=style_map,
    )
    add_section_table(
        story=story,
        title="Agreement Levels",
        headers=["Metric", "Fine WordNet", "Glite coarse"],
        rows=agreement_rows(data=data),
        style_map=style_map,
        col_widths=[3.2 * inch, 1.9 * inch, 1.9 * inch],
        title_style="h2",
    )
    add_chart(
        story=story,
        chart_path=chart_paths["agreement_levels"],
        title="Agreement levels",
        caption=(
            "Visual summary only; exact counts are in the table above. Colors from left "
            "to right: all three agree, exactly two agree, all three disagree."
        ),
        style_map=style_map,
    )
    add_section_table(
        story=story,
        title="Agreement Pattern Relative To Maru2022",
        headers=["Pattern", "Fine WordNet", "Glite coarse"],
        rows=relationship_rows(data=data),
        style_map=style_map,
        col_widths=[3.2 * inch, 1.9 * inch, 1.9 * inch],
        title_style="h2",
    )
    add_heading(
        story=story,
        text="Maru2022 Label Support Split",
        anchor="maru2022-label-support-split",
        style_map=style_map,
    )
    add_section_table(
        story=story,
        title="Reviewer Support For The Maru2022 Label",
        headers=["Support", "Fine WordNet", "Glite coarse"],
        rows=support_rows(data=data),
        style_map=style_map,
        col_widths=[3.2 * inch, 1.9 * inch, 1.9 * inch],
        title_style="h2",
    )
    add_chart(
        story=story,
        chart_path=chart_paths["gold_support"],
        title="Maru2022 label support",
        caption=(
            "Visual summary only; exact counts are in the support table above. Colors from "
            "left to right: 3/3, 2/3, 1/3, and 0/3 reviewers selected the Maru2022 label."
        ),
        style_map=style_map,
    )
    story.append(PageBreak())

    add_heading(
        story=story,
        text="Pairwise Agreement",
        anchor="pairwise-agreement",
        style_map=style_map,
    )
    story.append(
        paragraph(
            text=(
                "Each 3x3 matrix cell compares the row reviewer with the column reviewer. "
                "Raw agreement cells show the percentage and matching-item count. Diagonal "
                "cells are self-comparisons included only to keep the reviewer grid explicit."
            ),
            style=style_map["body"],
        )
    )
    add_pairwise_heatmap(
        story=story,
        title="Fine raw agreement",
        data=data,
        granularity=Granularity.FINE,
        metric="raw_agreement",
        style_map=style_map,
    )
    add_pairwise_heatmap(
        story=story,
        title="Glite raw agreement",
        data=data,
        granularity=Granularity.GLITE,
        metric="raw_agreement",
        style_map=style_map,
    )
    add_pairwise_heatmap(
        story=story,
        title="Fine Cohen's kappa",
        data=data,
        granularity=Granularity.FINE,
        metric="cohen_kappa",
        style_map=style_map,
    )
    add_pairwise_heatmap(
        story=story,
        title="Glite Cohen's kappa",
        data=data,
        granularity=Granularity.GLITE,
        metric="cohen_kappa",
        style_map=style_map,
    )
    add_section_table(
        story=story,
        title="Compact Pairwise Summary",
        headers=["Pair", "Fine raw", "Fine kappa", "Glite raw", "Glite kappa"],
        rows=pairwise_summary_rows(data=data),
        style_map=style_map,
        title_style="h2",
    )
    story.append(
        paragraph(
            text=(
                "Raw agreement is the direct match rate. Cohen's kappa corrects for the "
                "label distribution within each reviewer pair."
            ),
            style=style_map["body"],
        )
    )
    story.append(PageBreak())

    add_heading(
        story=story,
        text="Reviewer Answer Shape",
        anchor="reviewer-answer-shape",
        style_map=style_map,
    )
    add_section_table(
        story=story,
        title="Reviewer Answer Shape",
        headers=["Reviewer", "Single", "Multi", "Cannot", "Comments", "Notes"],
        rows=verdict_shape_rows(data=data),
        style_map=style_map,
        title_style="h2",
    )
    add_section_table(
        story=story,
        title="Fine Relation To Maru2022",
        headers=["Relation", *[reviewer_name(reviewer=reviewer) for reviewer in data.reviewers]],
        rows=maru_relation_rows(data=data, granularity=Granularity.FINE),
        style_map=style_map,
        title_style="h2",
    )
    add_section_table(
        story=story,
        title="Glite Relation To Maru2022",
        headers=["Relation", *[reviewer_name(reviewer=reviewer) for reviewer in data.reviewers]],
        rows=maru_relation_rows(data=data, granularity=Granularity.GLITE),
        style_map=style_map,
        title_style="h2",
    )
    story.append(PageBreak())

    add_heading(
        story=story,
        text="Glite Coarsening Effect",
        anchor="glite-coarsening-effect",
        style_map=style_map,
    )
    story.append(
        paragraph(
            text=(
                "Glite coarsening resolves "
                f"{count_percent_text(value=data.metrics.fine_non_unanimous_resolved_by_glite)} "
                "of fine-grained non-unanimous cases into all-three agreement. The report "
                f"required {data.metrics.glite_coverage.required_sense_keys} distinct WordNet "
                f"sense keys and mapped {data.metrics.glite_coverage.mapped_sense_keys} of them."
            ),
            style=style_map["body"],
        )
    )
    add_heading(
        story=story,
        text="Disagreement Concentration",
        anchor="disagreement-concentration",
        style_map=style_map,
    )
    for title, groups in [
        ("Part Of Speech", data.metrics.pos_groups),
        ("Source Dataset", data.metrics.source_groups),
        ("Frequent Headwords", data.metrics.headword_groups),
    ]:
        add_section_table(
            story=story,
            title=title,
            headers=[
                "Group",
                "Items",
                "Fine all 3",
                "Fine 2/3",
                "Fine differ",
                "Glite all 3",
                "Glite 2/3",
                "Glite differ",
            ],
            rows=group_rows(groups=groups),
            style_map=style_map,
            title_style="h2",
        )
    add_chart(
        story=story,
        chart_path=chart_paths["pos_source_agreement"],
        title="Agreement by POS and source",
        caption=(
            "Visual summary only; exact counts are in the POS and source tables above. "
            "Blue bars are Fine WordNet; green bars are Glite coarse."
        ),
        style_map=style_map,
    )
    story.append(PageBreak())

    add_heading(
        story=story,
        text="Cannot-Answer Reasons",
        anchor="cannot-answer-reasons",
        style_map=style_map,
    )
    story.append(
        paragraph(
            text=(
                f"At least one reviewer marked "
                f"{data.metrics.cannot_answer.at_least_one_unanswerable} items unanswerable; "
                f"all three reviewers marked {data.metrics.cannot_answer.all_three_unanswerable} "
                "items unanswerable."
            ),
            style=style_map["body"],
        )
    )
    story.append(
        table_flowable(
            headers=["Reason", *data.reviewers],
            rows=cannot_answer_reason_rows(data=data),
            style_map=style_map,
        )
    )
    add_chart(
        story=story,
        chart_path=chart_paths["cannot_answer_reasons"],
        title="Cannot-answer reasons",
        caption=(
            "Visual summary only; exact counts are in the tables in this section. Colors "
            "from left to right: input defective, inventory inadequate, no sense applies."
        ),
        style_map=style_map,
    )
    add_section_table(
        story=story,
        title="Cannot-Answer Consensus",
        headers=["Consensus strength", "Items"],
        rows=cannot_answer_consensus_rows(data=data),
        style_map=style_map,
        col_widths=[4.7 * inch, 2.3 * inch],
        title_style="h2",
    )
    story.append(
        paragraph(
            text=(
                "The strongest unusable-item signal is the at-least-two-reviewer subset: "
                f"{data.metrics.cannot_answer.at_least_two_unanswerable} items have at least "
                "two independent cannot-answer judgements. This includes "
                f"{data.metrics.cannot_answer.exactly_two_unanswerable} exactly-two cases and "
                f"{data.metrics.cannot_answer.all_three_unanswerable} all-three cases. These "
                "are not ordinary sense disagreements; they indicate that the item, context, "
                "or available WordNet inventory did not support a reliable fine-grained answer."
            ),
            style=style_map["body"],
        )
    )
    add_section_table(
        story=story,
        title="At-Least-Two Cannot-Answer Reasons",
        headers=["Reason present in at-least-two subset", "Items"],
        rows=cannot_answer_at_least_two_reason_rows(data=data),
        style_map=style_map,
        col_widths=[4.7 * inch, 2.3 * inch],
        title_style="h2",
    )
    add_section_table(
        story=story,
        title="Cannot-Answer By Document And Reviewer Support",
        headers=["Reviewer support", "Document", "Items"],
        rows=cannot_answer_document_support_rows(data=data),
        style_map=style_map,
        col_widths=[1.7 * inch, 4.1 * inch, 1.2 * inch],
        title_style="h2",
    )
    story.append(
        paragraph(
            text=(
                "Input-defective tags identify cases where the sentence, tokenization, "
                "target span, or source material prevents a reliable WSD judgement. The "
                "table below is split by how many reviewers used the input-defective reason; "
                "it is not limited to unanimous cases."
            ),
            style=style_map["body"],
        )
    )
    add_section_table(
        story=story,
        title="Defective Source Text",
        headers=["Reviewer support", "Document", "Items"],
        rows=input_defective_document_support_rows(data=data),
        style_map=style_map,
        col_widths=[1.7 * inch, 4.1 * inch, 1.2 * inch],
        title_style="h2",
    )
    story.append(PageBreak())

    add_heading(
        story=story,
        text="Removed Reviewed Items",
        anchor="removed-reviewed-items",
        style_map=style_map,
    )
    story.append(
        paragraph(
            text=(
                "lexEN v1 removes reviewed suspicious items when the review evidence does "
                "not provide a usable two-reviewer fine-grained sense label. No Maru2022 "
                "fallback label is used for these cases in the benchmark exports."
            ),
            style=style_map["body"],
        )
    )
    add_section_table(
        story=story,
        title="Removal Policy Applied To Reviewed Items",
        headers=["Removal evidence", "Items", "Benchmark action"],
        rows=removed_reviewed_item_rows(data=data),
        style_map=style_map,
        col_widths=[3.25 * inch, 0.8 * inch, 2.95 * inch],
        title_style="h2",
    )
    story.append(
        paragraph(
            text=(
                "The 29 no-consensus items are removed because all three reviewers selected "
                "different fine-grained answers. Coarse Glite agreement is reported for audit, "
                "but lexEN v1 is a fine-grained WordNet benchmark, so coarse agreement is not "
                "enough to keep a scorable item."
            ),
            style=style_map["body"],
        )
    )
    add_section_table(
        story=story,
        title="No Two-Reviewer Fine Agreement: Composition",
        headers=["Group", "Items"],
        rows=no_consensus_summary_rows(data=data),
        style_map=style_map,
        col_widths=[5.7 * inch, 1.3 * inch],
        title_style="h2",
    )
    add_section_table(
        story=story,
        title="No Two-Reviewer Fine Agreement: Label Support",
        headers=["Signal", "Items"],
        rows=no_consensus_support_rows(data=data),
        style_map=style_map,
        col_widths=[5.7 * inch, 1.3 * inch],
        title_style="h2",
    )
    add_section_table(
        story=story,
        title="No Two-Reviewer Fine Agreement: Reviewer Evidence",
        headers=["Reviewer evidence", "Items"],
        rows=no_consensus_evidence_rows(data=data),
        style_map=style_map,
        col_widths=[5.7 * inch, 1.3 * inch],
        title_style="h2",
    )
    add_section_table(
        story=story,
        title="No-Consensus Item Audit",
        headers=[
            "Item",
            "Lemma/POS/source",
            "Fine Maru support",
            "Glite result",
            "Cannot votes",
        ],
        rows=no_consensus_pdf_item_rows(data=data),
        style_map=style_map,
        col_widths=[
            1.85 * inch,
            2.05 * inch,
            1.0 * inch,
            1.55 * inch,
            0.55 * inch,
        ],
        title_style="h2",
    )
    story.append(PageBreak())
    add_section_table(
        story=story,
        title="Manual Sample Review",
        headers=["Item", "Lemma/POS/source", "Recommendation", "Rationale"],
        rows=no_consensus_sample_rows(data=data),
        style_map=style_map,
        col_widths=[1.55 * inch, 1.35 * inch, 1.3 * inch, 2.8 * inch],
        title_style="h2",
    )
    story.append(PageBreak())

    add_heading(
        story=story,
        text="What The Agreement Shows",
        anchor="what-the-agreement-shows",
        style_map=style_map,
    )
    story.append(
        paragraph(
            text=(
                "Unanimous and two-reviewer fine-grained agreements provide direct evidence "
                "for correcting Maru2022 labels. Two-reviewer cannot-answer cases and cases "
                "with no fine-grained majority are excluded from the benchmark release, but "
                "remain visible here for downstream audit."
            ),
            style=style_map["body"],
        )
    )
    add_heading(
        story=story,
        text="Technical Method",
        anchor="technical-method",
        style_map=style_map,
    )
    story.append(
        paragraph(
            text=(
                "The report is generated by scripts/build_agreement_report.py from the RF/PW/PH "
                "review JSON files, the selection source package, and the Glite mapping files. It "
                "writes Markdown, HTML, PDF, metrics JSON, per-item JSONL, and images "
                "under reports/rf-pw-ph-2026-06-13/."
            ),
            style=style_map["body"],
        )
    )

    add_heading(
        story=story,
        text="Full Item Appendix",
        anchor="full-item-appendix",
        style_map=style_map,
    )
    story.append(
        paragraph(
            text=(
                "The appendix contains all 363 reviewed items, grouped by fine-grained reviewer "
                "outcome. The group entries below are also present as PDF bookmarks."
            ),
            style=style_map["body"],
        )
    )
    add_section_table(
        story=story,
        title="Appendix Groups",
        headers=["Group", "Outcome", "Items"],
        rows=appendix_group_summary_rows(data=data),
        style_map=style_map,
        col_widths=[0.6 * inch, 4.75 * inch, 1.65 * inch],
        title_style="h2",
    )
    for group in data.metrics.appendix_groups:
        story.append(PageBreak())
        add_heading(
            story=story,
            text=group.title,
            anchor=appendix_group_anchor(group_id=group.group_id.value),
            style_map=style_map,
            toc_level=1,
        )
        story.append(
            paragraph(
                text=f"{group.description} Count: {len(group.items)}.", style=style_map["body"]
            )
        )
        for number, item in enumerate(
            sorted(group.items, key=lambda value: value.item_id), start=1
        ):
            add_appendix_item(
                story=story,
                data=data,
                item=item,
                item_id_prefix=f"{group.group_id.value}{number}",
                style_map=style_map,
            )
    document.multiBuild(
        story,
        onFirstPage=draw_page_footer,
        onLaterPages=draw_page_footer,
    )
