"""Render the agreement report as standalone HTML."""

from __future__ import annotations

from html import escape
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
    label_html,
    marked_sentence_html,
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


def html_table(
    *,
    headers: list[str],
    rows: list[list[str]],
    class_name: str = "",
) -> str:
    class_attr = f' class="{escape(class_name)}"' if len(class_name) > 0 else ""
    header_html = "".join(f"<th>{escape(header)}</th>" for header in headers)
    row_html: list[str] = []
    for row in rows:
        cells = "".join(f"<td>{cell}</td>" for cell in row)
        row_html.append(f"<tr>{cells}</tr>")
    return (
        f"<table{class_attr}>"
        f"<thead><tr>{header_html}</tr></thead>"
        f"<tbody>{''.join(row_html)}</tbody>"
        f"</table>"
    )


def chart_html(
    *,
    chart_paths: dict[str, Path],
    chart_key: str,
    title: str,
    caption: str,
    report_root: Path,
    wide: bool = False,
) -> str:
    relative_path = chart_paths[chart_key].relative_to(report_root)
    class_name = "chart chart-wide" if wide else "chart"
    return (
        f'<figure class="{class_name}">'
        f'<img src="{escape(str(relative_path))}" alt="{escape(title)}">'
        f"<figcaption><strong>{escape(title)}</strong>{escape(caption)}</figcaption>"
        "</figure>"
    )


def summary_cards(*, data: ReportData) -> str:
    cards = [
        ("Reviewed items", str(data.metrics.reviewed_items), "same-protocol items"),
        (
            "Fine all-three agreement",
            count_percent_text(value=data.metrics.fine.level_counts[AgreementLevel.ALL_THREE]),
            "exact WordNet labels",
        ),
        (
            "Glite all-three agreement",
            count_percent_text(value=data.metrics.glite.level_counts[AgreementLevel.ALL_THREE]),
            "coarse concepts",
        ),
        ("Fine Fleiss kappa", kappa_text(value=data.metrics.fine.fleiss_kappa), "3 reviewers"),
        ("Glite Fleiss kappa", kappa_text(value=data.metrics.glite.fleiss_kappa), "3 reviewers"),
        (
            "Fine Maru2022 3/3 support",
            count_percent_text(value=data.metrics.fine.gold_support_counts[3]),
            "reviewers selected source label",
        ),
    ]
    return "".join(
        (
            '<section class="metric">'
            f"<p>{escape(label)}</p>"
            f"<strong>{escape(value)}</strong>"
            f"<span>{escape(note)}</span>"
            "</section>"
        )
        for label, value, note in cards
    )


def agreement_rows(*, data: ReportData) -> list[list[str]]:
    rows: list[list[str]] = []
    for level in AgreementLevel:
        rows.append(
            [
                escape(level_label(level=level)),
                escape(count_percent_text(value=data.metrics.fine.level_counts[level])),
                escape(count_percent_text(value=data.metrics.glite.level_counts[level])),
            ]
        )
    rows.extend(
        [
            [
                "All three agree and match Maru2022",
                escape(count_percent_text(value=data.metrics.fine.all_three_agree_and_gold)),
                escape(count_percent_text(value=data.metrics.glite.all_three_agree_and_gold)),
            ],
            [
                "Exactly two agree and match Maru2022",
                escape(count_percent_text(value=data.metrics.fine.exactly_two_agree_and_gold)),
                escape(count_percent_text(value=data.metrics.glite.exactly_two_agree_and_gold)),
            ],
            [
                "Fleiss kappa",
                escape(kappa_text(value=data.metrics.fine.fleiss_kappa)),
                escape(kappa_text(value=data.metrics.glite.fleiss_kappa)),
            ],
        ]
    )
    return rows


def support_rows(*, data: ReportData) -> list[list[str]]:
    return [
        [
            f"{support}/3 reviewers selected the Maru2022 label",
            escape(count_percent_text(value=data.metrics.fine.gold_support_counts[support])),
            escape(count_percent_text(value=data.metrics.glite.gold_support_counts[support])),
        ]
        for support in [3, 2, 1, 0]
    ]


def relationship_rows(*, data: ReportData) -> list[list[str]]:
    return [
        [
            escape(relation_label(relation=relation)),
            escape(count_percent_text(value=data.metrics.fine.relationship_counts[relation])),
            escape(count_percent_text(value=data.metrics.glite.relationship_counts[relation])),
        ]
        for relation in data.metrics.fine.relationship_counts
    ]


def pairwise_heatmap_table(
    *,
    data: ReportData,
    granularity: Granularity,
    metric: PairwiseMatrixMetric,
    title: str,
) -> str:
    matrix_rows = pairwise_matrix_cells(
        data=data,
        granularity=granularity,
        metric=metric,
    )
    header_cells = "".join(f"<th>{escape(reviewer)}</th>" for reviewer in data.reviewers)
    body_rows: list[str] = []
    for row_cells in matrix_rows:
        cells = [f"<th>{escape(row_cells[0].row_reviewer)}</th>"]
        for cell in row_cells:
            text = pairwise_matrix_cell_text(cell=cell, metric=metric)
            if cell.diagonal:
                cells.append(f'<td class="matrix-self">{escape(text)}</td>')
                continue
            color = heatmap_color_hex(value=cell.value, metric=metric)
            if metric == "raw_agreement":
                percent, counts = text.split(" ", maxsplit=1)
                cell_html = (
                    f"<strong>{escape(percent)}</strong>"
                    f"<span>{escape(counts.strip('()'))} items</span>"
                )
            else:
                cell_html = f"<strong>{escape(text)}</strong>"
            cells.append(f'<td style="background:{color}">{cell_html}</td>')
        body_rows.append(f"<tr>{''.join(cells)}</tr>")
    return (
        '<section class="pairwise-matrix">'
        f"<h3>{escape(title)}</h3>"
        '<table class="matrix-table">'
        f"<thead><tr><th>Reviewer</th>{header_cells}</tr></thead>"
        f"<tbody>{''.join(body_rows)}</tbody>"
        "</table>"
        "</section>"
    )


def pairwise_matrices_html(*, data: ReportData) -> str:
    sections = [
        pairwise_heatmap_table(
            data=data,
            granularity=Granularity.FINE,
            metric="raw_agreement",
            title="Fine raw agreement",
        ),
        pairwise_heatmap_table(
            data=data,
            granularity=Granularity.GLITE,
            metric="raw_agreement",
            title="Glite raw agreement",
        ),
        pairwise_heatmap_table(
            data=data,
            granularity=Granularity.FINE,
            metric="cohen_kappa",
            title="Fine Cohen's kappa",
        ),
        pairwise_heatmap_table(
            data=data,
            granularity=Granularity.GLITE,
            metric="cohen_kappa",
            title="Glite Cohen's kappa",
        ),
    ]
    return '<div class="pairwise-matrix-grid">' + "".join(sections) + "</div>"


def verdict_shape_rows(*, data: ReportData) -> list[list[str]]:
    return [
        [
            escape(reviewer_label(reviewer=shape.reviewer)),
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
        row = [escape(maru_relation_label(relation=relation_name))]
        for relation in data.metrics.maru_relations:
            if relation.granularity is granularity:
                row.append(
                    escape(
                        count_percent_text(
                            value=maru_relation_value(
                                relation=relation,
                                relation_name=relation_name,
                            )
                        )
                    )
                )
        rows.append(row)
    return rows


def group_rows(*, groups: list[GroupAgreement]) -> list[list[str]]:
    return [
        [
            escape(group.group_name),
            str(group.total_items),
            escape(count_percent_text(value=group.fine_all_three)),
            escape(count_percent_text(value=group.fine_exactly_two)),
            escape(count_percent_text(value=group.fine_all_differ)),
            escape(count_percent_text(value=group.glite_all_three)),
            escape(count_percent_text(value=group.glite_exactly_two)),
            escape(count_percent_text(value=group.glite_all_differ)),
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
                escape(reason_label(reason=reason)),
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
        [escape(document_id), str(count)]
        for document_id, count in data.metrics.cannot_answer.input_defective_by_document.items()
    ]


def report_toc_html(*, data: ReportData) -> str:
    sections = [
        ("what-this-report-includes", "What this report includes"),
        ("how-to-read-the-numbers", "How to read the numbers"),
        ("headline-agreement", "Headline agreement"),
        ("maru2022-label-support-split", "Maru2022 label support"),
        ("pairwise-agreement", "Pairwise agreement"),
        ("reviewer-answer-shape", "Reviewer answer shape"),
        ("glite-coarsening-effect", "Glite coarsening effect"),
        ("disagreement-concentration", "Disagreement concentration"),
        ("cannot-answer-reasons", "Cannot-answer reasons"),
        ("removed-reviewed-items", "Removed reviewed items"),
        ("what-the-agreement-shows", "What the agreement shows"),
        ("technical-method", "Technical method"),
        ("full-item-appendix", "Full item appendix"),
    ]
    section_links = "".join(
        f'<li><a href="#{escape(anchor)}">{escape(label)}</a></li>' for anchor, label in sections
    )
    appendix_links = "".join(
        (
            f'<li><a href="#{escape(appendix_group_anchor(group_id=group.group_id.value))}">'
            f"{escape(group.group_id.value)}. "
            f"{escape(group.title.split('. ', maxsplit=1)[1])}</a></li>"
        )
        for group in data.metrics.appendix_groups
    )
    return (
        '<nav class="report-toc" aria-label="Report contents">'
        "<h2>Contents</h2>"
        f"<ol>{section_links}</ol>"
        "<h3>Appendix</h3>"
        f'<ol class="appendix-toc">{appendix_links}</ol>'
        "</nav>"
    )


def appendix_summary_table_html(*, data: ReportData) -> str:
    rows: list[str] = []
    for group, summary_row in zip(
        data.metrics.appendix_groups,
        appendix_group_summary_rows(data=data),
        strict=True,
    ):
        anchor = appendix_group_anchor(group_id=group.group_id.value)
        cells = "".join(
            f'<td><a href="#{escape(anchor)}">{escape(cell)}</a></td>' for cell in summary_row
        )
        rows.append(f"<tr>{cells}</tr>")
    return (
        '<table class="appendix-summary">'
        "<thead><tr><th>Group</th><th>Outcome</th><th>Items</th></tr></thead>"
        f"<tbody>{''.join(rows)}</tbody>"
        "</table>"
    )


def appendix_group_rows(*, data: ReportData) -> list[list[str]]:
    return [[escape(cell) for cell in row] for row in appendix_group_summary_rows(data=data)]


def reviewer_verdict_html(
    *,
    data: ReportData,
    item: ItemAgreement,
    reviewer: str,
) -> str:
    note = clean_optional_text(value=item.reviewer_notes[reviewer])
    comment = clean_optional_text(value=item.reviewer_comments[reviewer])
    extras: list[str] = []
    if note is not None:
        extras.append(f'<p class="note"><strong>Note:</strong> {escape(note)}</p>')
    if comment is not None:
        extras.append(f'<p class="note"><strong>Comment:</strong> {escape(comment)}</p>')
    return (
        '<section class="reviewer-verdict">'
        f"<h5>{escape(reviewer_label(reviewer=reviewer))}</h5>"
        f"{label_html(data=data, label=item.reviewer_fine[reviewer], include_examples=True)}"
        f"{''.join(extras)}"
        "</section>"
    )


def appendix_item_html(
    *,
    data: ReportData,
    item: ItemAgreement,
    item_id_prefix: str,
) -> str:
    reviewer_html = "".join(
        reviewer_verdict_html(data=data, item=item, reviewer=reviewer)
        for reviewer in data.reviewers
    )
    return f"""
      <article class="appendix-item" id="{escape(item.item_id)}">
        <h4>{escape(item_id_prefix)}. <code>{escape(item.item_id)}</code></h4>
        <p class="meta"><strong>Lemma/POS/source:</strong>
          <code>{escape(item.lemma)}</code> / <code>{escape(item.pos)}</code> /
          <code>{escape(item.source_dataset)}</code> (<code>{escape(item.document_id)}</code>)
        </p>
        <blockquote>{marked_sentence_html(item=item)}</blockquote>
        <section class="maru-label">
          <h5>Maru2022 label</h5>
          {label_html(data=data, label=item.maru_fine, include_examples=True)}
        </section>
        <section class="reviewer-grid">{reviewer_html}</section>
        <p class="agreement">{escape(agreement_short_text(item=item))}</p>
      </article>
    """


def appendix_html(*, data: ReportData) -> str:
    sections: list[str] = []
    for group in data.metrics.appendix_groups:
        items = "".join(
            appendix_item_html(
                data=data,
                item=item,
                item_id_prefix=f"{group.group_id.value}{number}",
            )
            for number, item in enumerate(
                sorted(group.items, key=lambda value: value.item_id), start=1
            )
        )
        anchor = appendix_group_anchor(group_id=group.group_id.value)
        sections.append(
            f"""
            <section class="appendix-group" id="{escape(anchor)}">
              <h3>{escape(group.title)}</h3>
              <p>{escape(group.description)} Count: {len(group.items)}.</p>
              {items}
            </section>
            """
        )
    return "".join(sections)


def render_html(
    *,
    data: ReportData,
    chart_paths: dict[str, Path],
    output_path: Path,
    report_root: Path,
) -> None:
    output_path.parent.mkdir(parents=True, exist_ok=True)
    css = """
    :root {
      color-scheme: light;
      --ink: #17202a;
      --muted: #5d6979;
      --line: #d8dee8;
      --soft: #f5f7fa;
      --table: #eef3f8;
      --accent: #1b6f5d;
      --accent-soft: #e8f4f0;
      --warn-soft: #fff4df;
    }
    * { box-sizing: border-box; }
    body {
      margin: 0;
      color: var(--ink);
      background: white;
      font-family: Inter, ui-sans-serif, system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI",
        sans-serif;
      line-height: 1.52;
    }
    header {
      background: #16212c;
      color: white;
      padding: 48px max(28px, calc((100vw - 1180px) / 2)) 36px;
      border-bottom: 6px solid var(--accent);
    }
    header h1 { margin: 0 0 12px; font-size: clamp(30px, 4vw, 46px); letter-spacing: 0; }
    header p { max-width: 960px; color: #dce6ee; font-size: 17px; margin: 0; }
    .page-shell {
      display: grid;
      grid-template-columns: minmax(0, 1fr) 280px;
      gap: 28px;
      max-width: 1500px;
      margin: 0 auto;
      padding: 28px;
      align-items: start;
    }
    main { min-width: 0; }
    .report-toc {
      position: sticky;
      top: 18px;
      max-height: calc(100vh - 36px);
      overflow: auto;
      border: 1px solid var(--line);
      border-radius: 6px;
      padding: 14px 16px;
      background: #fff;
      font-size: 13px;
    }
    .report-toc h2 {
      margin: 0 0 10px;
      font-size: 17px;
    }
    .report-toc h3 {
      margin: 16px 0 8px;
      font-size: 14px;
    }
    .report-toc ol {
      margin: 0;
      padding-left: 18px;
    }
    .report-toc li { margin: 0 0 6px; }
    .report-toc a {
      color: var(--accent);
      text-decoration: none;
    }
    .report-toc a:hover { text-decoration: underline; }
    section.report-section { padding: 22px 0 30px; border-bottom: 1px solid var(--line); }
    h2 { margin: 0 0 14px; font-size: 26px; letter-spacing: 0; }
    h3 { margin: 26px 0 10px; font-size: 20px; letter-spacing: 0; }
    h4 { margin: 0 0 10px; font-size: 17px; letter-spacing: 0; }
    h5 { margin: 0 0 8px; font-size: 14px; letter-spacing: 0; }
    p { max-width: 920px; }
    .metrics {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(210px, 1fr));
      gap: 12px;
      margin: 18px 0 4px;
    }
    .metric {
      border: 1px solid var(--line);
      border-radius: 6px;
      padding: 14px 16px;
      background: #fff;
    }
    .metric p { margin: 0 0 7px; color: var(--muted); font-size: 13px; }
    .metric strong { display: block; font-size: 23px; }
    .metric span { color: var(--muted); font-size: 12px; }
    table {
      width: 100%;
      border-collapse: collapse;
      font-size: 14px;
      margin: 12px 0 22px;
    }
    th, td { border: 1px solid var(--line); padding: 9px 10px; vertical-align: top; }
    th { background: var(--table); text-align: left; font-weight: 700; }
    tbody tr:nth-child(even) { background: #fbfcfe; }
    table.dense-table th,
    table.dense-table td {
      font-size: 13px;
      line-height: 1.35;
      padding: 7px 8px;
    }
    figure.chart {
      margin: 16px 0 24px;
      padding: 0;
    }
    figure.chart-wide {
      width: 100%;
      margin-left: 0;
      transform: none;
    }
    figure.chart img {
      display: block;
      width: 100%;
      height: auto;
      border: 1px solid var(--line);
      border-radius: 4px;
      background: white;
    }
    figcaption {
      max-width: 880px;
      color: var(--muted);
      font-size: 13px;
      margin-top: 8px;
    }
    .chart-wide figcaption { max-width: 100%; }
    .pairwise-matrix-grid {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(420px, 1fr));
      gap: 18px;
      margin: 10px 0 20px;
    }
    .pairwise-matrix h3 { margin-top: 0; }
    table.matrix-table {
      table-layout: fixed;
      margin: 8px 0 0;
    }
    .matrix-table th,
    .matrix-table td {
      text-align: center;
      vertical-align: middle;
      padding: 12px 10px;
    }
    .matrix-table tbody th {
      background: var(--table);
      font-weight: 700;
    }
    .matrix-table td strong {
      display: block;
      font-size: 16px;
      color: var(--ink);
    }
    .matrix-table td span {
      display: block;
      margin-top: 3px;
      color: #425466;
      font-size: 12px;
    }
    .matrix-table td.matrix-self {
      background: #f1f4f8;
      color: var(--muted);
      font-weight: 700;
    }
    figcaption strong { display: block; color: var(--ink); margin-bottom: 2px; }
    code {
      background: #eef3f8;
      border-radius: 4px;
      padding: 1px 4px;
      font-family: ui-monospace, SFMono-Regular, Menlo, Consolas, monospace;
      font-size: 0.92em;
    }
    blockquote {
      margin: 10px 0 14px;
      padding: 10px 14px;
      border-left: 4px solid var(--accent);
      background: var(--accent-soft);
    }
    mark { background: #ffe08a; padding: 0 3px; border-radius: 3px; }
    .appendix-item {
      border: 1px solid var(--line);
      border-radius: 6px;
      padding: 16px;
      margin: 14px 0;
      break-inside: avoid;
    }
    .appendix-item .meta { color: var(--muted); margin: 0 0 8px; }
    .reviewer-grid {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(260px, 1fr));
      gap: 12px;
      margin-top: 12px;
    }
    .reviewer-verdict,
    .maru-label {
      border-top: 1px solid var(--line);
      padding-top: 10px;
    }
    .label-list {
      margin: 0 0 8px;
      padding-left: 18px;
    }
    .label-list li { margin: 0 0 8px; }
    .synset {
      display: inline-block;
      color: var(--muted);
      margin-left: 4px;
      font-size: 12px;
    }
    .definition,
    .synonyms,
    .examples {
      display: block;
      margin-top: 3px;
    }
    .synonyms,
    .examples,
    .note {
      color: var(--muted);
      font-size: 13px;
    }
    .agreement {
      margin: 12px 0 0;
      padding: 8px 10px;
      background: var(--warn-soft);
      border-radius: 4px;
      font-size: 13px;
    }
    .appendix-group { margin-top: 26px; }
    .appendix-summary a { color: var(--accent); text-decoration: none; }
    .appendix-summary a:hover { text-decoration: underline; }
    html { scroll-behavior: smooth; }
    section[id] { scroll-margin-top: 18px; }
    @media (max-width: 1120px) {
      .page-shell { display: block; max-width: 1180px; }
      .report-toc {
        position: static;
        max-height: none;
        margin-bottom: 22px;
      }
    }
    @media print {
      header { background: white; color: var(--ink); border-bottom: 2px solid var(--line); }
      header p { color: var(--ink); }
      .page-shell { display: block; max-width: none; padding: 18px; }
      .report-toc { display: none; }
      figure.chart img { width: 100%; }
      .appendix-item { page-break-inside: avoid; }
    }
    """
    headline_table = html_table(
        headers=["Metric", "Fine WordNet", "Glite coarse"],
        rows=agreement_rows(data=data),
    )
    agreement_chart = chart_html(
        chart_paths=chart_paths,
        chart_key="agreement_levels",
        title="Agreement levels",
        caption=(
            "Visual summary only; exact counts are in the table above. Colors from left "
            "to right: all three agree, exactly two agree, all three disagree."
        ),
        report_root=report_root,
    )
    relationship_table = html_table(
        headers=["Pattern", "Fine WordNet", "Glite coarse"],
        rows=relationship_rows(data=data),
    )
    support_table = html_table(
        headers=["Support", "Fine WordNet", "Glite coarse"],
        rows=support_rows(data=data),
    )
    support_chart = chart_html(
        chart_paths=chart_paths,
        chart_key="gold_support",
        title="Maru2022 label support",
        caption=(
            "Visual summary only; exact counts are in the support table above. Colors from "
            "left to right: 3/3, 2/3, 1/3, and 0/3 reviewers selected the Maru2022 label."
        ),
        report_root=report_root,
    )
    pairwise_matrices = pairwise_matrices_html(data=data)
    pairwise_table = html_table(
        headers=["Pair", "Fine raw", "Fine kappa", "Glite raw", "Glite kappa"],
        rows=[[escape(cell) for cell in row] for row in pairwise_summary_rows(data=data)],
    )
    verdict_shape_table = html_table(
        headers=[
            "Reviewer",
            "Single sense",
            "Multiple senses",
            "Cannot answer",
            "Comments",
            "Notes",
        ],
        rows=verdict_shape_rows(data=data),
    )
    fine_relation_table = html_table(
        headers=["Relation", *[reviewer_name(reviewer=reviewer) for reviewer in data.reviewers]],
        rows=maru_relation_rows(data=data, granularity=Granularity.FINE),
    )
    glite_relation_table = html_table(
        headers=["Relation", *[reviewer_name(reviewer=reviewer) for reviewer in data.reviewers]],
        rows=maru_relation_rows(data=data, granularity=Granularity.GLITE),
    )
    group_headers = [
        "Items",
        "Fine all 3",
        "Fine 2/3",
        "Fine differ",
        "Glite all 3",
        "Glite 2/3",
        "Glite differ",
    ]
    pos_table = html_table(
        headers=["POS", *group_headers],
        rows=group_rows(groups=data.metrics.pos_groups),
    )
    source_table = html_table(
        headers=["Source", *group_headers],
        rows=group_rows(groups=data.metrics.source_groups),
    )
    headword_table = html_table(
        headers=["Headword", *group_headers],
        rows=group_rows(groups=data.metrics.headword_groups),
    )
    pos_source_chart = chart_html(
        chart_paths=chart_paths,
        chart_key="pos_source_agreement",
        title="Agreement by POS and source",
        caption=(
            "Visual summary only; exact counts are in the POS and source tables above. "
            "Blue bars are Fine WordNet; green bars are Glite coarse."
        ),
        report_root=report_root,
        wide=True,
    )
    cannot_answer_table = html_table(
        headers=["Reason", *data.reviewers],
        rows=cannot_answer_reason_rows(data=data),
    )
    cannot_answer_consensus_table = html_table(
        headers=["Consensus strength", "Items"],
        rows=[[escape(cell) for cell in row] for row in cannot_answer_consensus_rows(data=data)],
    )
    cannot_answer_at_least_two_reason_table = html_table(
        headers=["Reason present in at-least-two subset", "Items"],
        rows=[
            [escape(cell) for cell in row]
            for row in cannot_answer_at_least_two_reason_rows(data=data)
        ],
    )
    cannot_answer_chart = chart_html(
        chart_paths=chart_paths,
        chart_key="cannot_answer_reasons",
        title="Cannot-answer reasons",
        caption=(
            "Visual summary only; exact counts are in the tables in this section. Colors "
            "from left to right: input defective, inventory inadequate, no sense applies."
        ),
        report_root=report_root,
    )
    cannot_answer_document_support_table = html_table(
        headers=["Reviewer support", "Document", "Items"],
        rows=[
            [escape(cell) for cell in row] for row in cannot_answer_document_support_rows(data=data)
        ],
    )
    defective_table = html_table(
        headers=["Reviewer support", "Document", "Items"],
        rows=[
            [escape(cell) for cell in row]
            for row in input_defective_document_support_rows(data=data)
        ],
    )
    removed_reviewed_table = html_table(
        headers=["Removal evidence", "Items", "Benchmark action"],
        rows=[[escape(cell) for cell in row] for row in removed_reviewed_item_rows(data=data)],
    )
    no_consensus_summary_table = html_table(
        headers=["Group", "Items"],
        rows=[[escape(cell) for cell in row] for row in no_consensus_summary_rows(data=data)],
    )
    no_consensus_support_table = html_table(
        headers=["Signal", "Items"],
        rows=[[escape(cell) for cell in row] for row in no_consensus_support_rows(data=data)],
    )
    no_consensus_evidence_table = html_table(
        headers=["Reviewer evidence", "Items"],
        rows=[[escape(cell) for cell in row] for row in no_consensus_evidence_rows(data=data)],
    )
    no_consensus_item_table = html_table(
        headers=[
            "Item",
            "Lemma/POS/source",
            "Fine Maru support",
            "Glite level",
            "Glite Maru support",
            "Cannot votes",
            *data.reviewers,
        ],
        rows=[
            [
                f'<a href="#{escape(row[0])}"><code>{escape(row[0])}</code></a>',
                *[escape(cell) for cell in row[1:]],
            ]
            for row in no_consensus_item_rows(data=data)
        ],
        class_name="dense-table",
    )
    no_consensus_sample_table = html_table(
        headers=["Item", "Lemma/POS/source", "Recommendation", "Rationale"],
        rows=[[escape(cell) for cell in row] for row in no_consensus_sample_rows(data=data)],
        class_name="dense-table",
    )
    toc = report_toc_html(data=data)
    appendix_summary_table = appendix_summary_table_html(data=data)
    appendix = appendix_html(data=data)
    html = f"""<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{escape(REPORT_TITLE)}</title>
  <style>{css}</style>
</head>
<body>
  <header>
    <h1>{escape(REPORT_TITLE)}</h1>
    <p>Report date: {escape(REPORT_VERSION)}. This report audits 363 suspicious Maru2022
    validation items reviewed independently by RF, PW, and PH. Maru2022 labels are source
    labels under review, not a privileged adjudication.</p>
  </header>
  <div class="page-shell">
  <main>
    <section class="report-section" id="what-this-report-includes">
      <h2>What This Report Includes</h2>
      <p>The report is generated from the Maru2022 source copy, the suspicious-item selection
      package, the RF/PW/PH review files, and the Glite coarsening map. It covers fine WordNet
      agreement, Glite-coarsened agreement, pairwise coefficients, reviewer answer shape,
      Maru2022 label support, concentration by item type, cannot-answer evidence, and a full
      appendix for all reviewed items.</p>
      <div class="metrics">{summary_cards(data=data)}</div>
    </section>

    <section class="report-section" id="how-to-read-the-numbers">
      <h2>How To Read The Numbers</h2>
      <p>Fine WordNet agreement compares exact WordNet sense-key sets. Glite agreement first
      maps those sense keys to coarse Glite concepts. Maru2022 support counts how many
      reviewers selected the Maru2022 source label for an item.</p>
    </section>

    <section class="report-section" id="headline-agreement">
      <h2>Headline Agreement</h2>
      {headline_table}
      {agreement_chart}
      <h3>Agreement Pattern Relative To Maru2022</h3>
      {relationship_table}
    </section>

    <section class="report-section" id="maru2022-label-support-split">
      <h2>Maru2022 Label Support Split</h2>
      {support_table}
      {support_chart}
    </section>

    <section class="report-section" id="pairwise-agreement">
      <h2>Pairwise Agreement</h2>
      <p>Each matrix cell compares the row reviewer with the column reviewer. Raw agreement
      cells show the percentage and matching-item count; diagonal cells are neutral
      self-comparisons included to keep the reviewer grid explicit.</p>
      {pairwise_matrices}
      <h3>Compact Pairwise Summary</h3>
      {pairwise_table}
      <p>Raw agreement is the direct match rate. Cohen's kappa corrects for the label
      distribution within each reviewer pair.</p>
    </section>

    <section class="report-section" id="reviewer-answer-shape">
      <h2>Reviewer Answer Shape</h2>
      {verdict_shape_table}
      <h3>Fine Relation To Maru2022</h3>
      {fine_relation_table}
      <h3>Glite Relation To Maru2022</h3>
      {glite_relation_table}
    </section>

    <section class="report-section" id="glite-coarsening-effect">
      <h2>Glite Coarsening Effect</h2>
      <p>Glite coarsening resolves
      {escape(count_percent_text(value=data.metrics.fine_non_unanimous_resolved_by_glite))}
      of fine-grained non-unanimous cases into all-three agreement. The report required
      {data.metrics.glite_coverage.required_sense_keys} distinct WordNet sense keys and mapped
      {data.metrics.glite_coverage.mapped_sense_keys} of them.</p>
    </section>

    <section class="report-section" id="disagreement-concentration">
      <h2>Disagreement Concentration</h2>
      <h3>Part Of Speech</h3>
      {pos_table}
      <h3>Source Dataset</h3>
      {source_table}
      <h3>Frequent Headwords</h3>
      {headword_table}
      {pos_source_chart}
    </section>

    <section class="report-section" id="cannot-answer-reasons">
      <h2>Cannot-Answer Reasons</h2>
      <p>At least one reviewer marked {data.metrics.cannot_answer.at_least_one_unanswerable}
      items unanswerable; all three reviewers marked
      {data.metrics.cannot_answer.all_three_unanswerable} items unanswerable.</p>
      {cannot_answer_table}
      {cannot_answer_chart}
      <h3>Cannot-Answer Consensus</h3>
      {cannot_answer_consensus_table}
      <p>The strongest unusable-item signal is the at-least-two-reviewer subset:
      {data.metrics.cannot_answer.at_least_two_unanswerable} items have at least two
      independent cannot-answer judgements. This includes
      {data.metrics.cannot_answer.exactly_two_unanswerable} exactly-two cases and
      {data.metrics.cannot_answer.all_three_unanswerable} all-three cases. These are not
      ordinary sense disagreements; they indicate that the item, context, or available
      WordNet inventory did not support a reliable fine-grained answer.</p>
      {cannot_answer_at_least_two_reason_table}
      <h3>Cannot-Answer By Document And Reviewer Support</h3>
      <p>This table shows document concentration for items where at least two reviewers
      marked cannot answer, split into exactly-two and all-three reviewer support.</p>
      {cannot_answer_document_support_table}
      <h3>Defective Source Text</h3>
      <p>Input-defective tags identify cases where the sentence, tokenization, target span,
      or source material prevents a reliable WSD judgement. This table is split by how many
      reviewers used the input-defective reason; it is not limited to unanimous cases.</p>
      {defective_table}
    </section>

    <section class="report-section" id="removed-reviewed-items">
      <h2>Removed Reviewed Items</h2>
      <p>lexEN v1 removes reviewed suspicious items when the review evidence does not provide
      a usable two-reviewer fine-grained sense label. No Maru2022 fallback label is used for
      these cases in the benchmark exports.</p>
      {removed_reviewed_table}
      <h3>No Two-Reviewer Fine Agreement</h3>
      <p>The 29 no-consensus items are removed because all three reviewers selected different
      fine-grained answers. Coarse Glite agreement is reported for audit, but lexEN v1 is a
      fine-grained WordNet benchmark, so coarse agreement is not enough to keep a scorable
      item.</p>
      {no_consensus_summary_table}
      {no_consensus_support_table}
      {no_consensus_evidence_table}
      <h3>No-Consensus Item Audit</h3>
      {no_consensus_item_table}
      <h3>Manual Sample Review</h3>
      <p>A manual review of 20 no-consensus items found no case that was safe to keep by
      falling back to the Maru2022 label. Common failure modes were inventory gaps, fixed
      expressions, figurative uses, and fine WordNet distinctions that the context does not
      reliably determine.</p>
      {no_consensus_sample_table}
    </section>

    <section class="report-section" id="what-the-agreement-shows">
      <h2>What The Agreement Shows</h2>
      <p>Unanimous and two-reviewer fine-grained agreements provide direct evidence for
      correcting Maru2022 labels. Two-reviewer cannot-answer cases and cases with no
      fine-grained majority are excluded from the benchmark release, but remain visible here
      for downstream audit.</p>
    </section>

    <section class="report-section" id="technical-method">
      <h2>Technical Method</h2>
      <p>The report is generated by <code>scripts/build_agreement_report.py</code> from
      the RF/PW/PH review JSON files, the selection source package, and the Glite mapping
      files. It writes Markdown, HTML, PDF, metrics JSON, per-item JSONL, and images under
      <code>reports/rf-pw-ph-2026-06-13/</code>.</p>
    </section>

    <section class="report-section" id="full-item-appendix">
      <h2>Full Item Appendix</h2>
      <p>The appendix contains all 363 reviewed items, grouped by fine-grained reviewer outcome.</p>
      {appendix_summary_table}
      {appendix}
    </section>
  </main>
  {toc}
  </div>
</body>
</html>
"""
    output_path.write_text(html, encoding="utf-8")
