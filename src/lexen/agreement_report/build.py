"""Build the agreement report package."""

from __future__ import annotations

import argparse
import json
from dataclasses import dataclass
from pathlib import Path
from typing import Protocol

from lexen.agreement_report.charts import (
    chart_agreement_levels,
    chart_cannot_answer,
    chart_gold_support,
    chart_pairwise_coefficients,
    chart_pos_source,
    chart_verdict_shape,
    render_all_charts,
)
from lexen.agreement_report.metrics import build_report_data
from lexen.agreement_report.models import ReportData
from lexen.agreement_report.paths import (
    CHART_AGREEMENT_LEVELS_FILENAME,
    CHART_CANNOT_ANSWER_FILENAME,
    CHART_GOLD_SUPPORT_FILENAME,
    CHART_PAIRWISE_FILENAME,
    CHART_POS_SOURCE_FILENAME,
    CHART_VERDICT_SHAPE_FILENAME,
    DEFAULT_REPORT_ROOT,
    REPORT_HTML_FILENAME,
    REPORT_MARKDOWN_FILENAME,
    REPORT_METRICS_FILENAME,
    REPORT_PDF_FILENAME,
    REPORT_PER_ITEM_FILENAME,
)
from lexen.agreement_report.render_html import render_html
from lexen.agreement_report.render_markdown import render_markdown
from lexen.agreement_report.render_pdf import render_pdf
from lexen.agreement_report.serialize import per_item_rows, report_data_json
from lexen.io import write_json_object, write_jsonl_objects
from lexen.paths import DEFAULT_REPO_ROOT


class ChartRenderer(Protocol):
    def __call__(
        self,
        *,
        data: ReportData,
        output_path: Path,
    ) -> None: ...


@dataclass(frozen=True, slots=True)
class ChartSpec:
    name: str
    filename: str
    renderer: ChartRenderer


@dataclass(frozen=True, slots=True)
class ReportBuildResult:
    report_root: Path
    html_path: Path
    pdf_path: Path
    markdown_path: Path
    metrics_path: Path
    per_item_path: Path
    chart_paths: dict[str, Path]


CHART_SPECS: list[ChartSpec] = [
    ChartSpec(
        name="agreement_levels",
        filename=CHART_AGREEMENT_LEVELS_FILENAME,
        renderer=chart_agreement_levels,
    ),
    ChartSpec(
        name="gold_support",
        filename=CHART_GOLD_SUPPORT_FILENAME,
        renderer=chart_gold_support,
    ),
    ChartSpec(
        name="pairwise_coefficients",
        filename=CHART_PAIRWISE_FILENAME,
        renderer=chart_pairwise_coefficients,
    ),
    ChartSpec(
        name="verdict_shape",
        filename=CHART_VERDICT_SHAPE_FILENAME,
        renderer=chart_verdict_shape,
    ),
    ChartSpec(
        name="cannot_answer_reasons",
        filename=CHART_CANNOT_ANSWER_FILENAME,
        renderer=chart_cannot_answer,
    ),
    ChartSpec(
        name="pos_source_agreement",
        filename=CHART_POS_SOURCE_FILENAME,
        renderer=chart_pos_source,
    ),
]


def chart_output_path(
    *,
    report_root: Path,
    chart_name: str,
) -> Path:
    for chart_spec in CHART_SPECS:
        if chart_spec.name == chart_name:
            return report_root / "images" / chart_spec.filename
    raise ValueError(f"unknown chart {chart_name}")


def render_single_chart(
    *,
    chart_name: str,
    data: ReportData,
    report_root: Path,
) -> Path:
    for chart_spec in CHART_SPECS:
        if chart_spec.name == chart_name:
            output_path = chart_output_path(
                report_root=report_root,
                chart_name=chart_name,
            )
            chart_spec.renderer(data=data, output_path=output_path)
            return output_path
    raise ValueError(f"unknown chart {chart_name}")


def format_markdown_report(*, markdown_path: Path) -> None:
    try:
        from flowmark import reformat_file
    except ImportError as error:
        raise RuntimeError(
            "flowmark is required to build the formatted Markdown agreement report"
        ) from error

    reformat_file(
        path=markdown_path,
        output=None,
        width=100,
        inplace=True,
        nobackup=True,
        cleanups=True,
    )


def build_agreement_report(
    *,
    repo_root: Path = DEFAULT_REPO_ROOT,
    report_root: Path = DEFAULT_REPORT_ROOT,
) -> ReportBuildResult:
    repo_root = repo_root.resolve()
    report_root = report_root.resolve()
    data = build_report_data(repo_root=repo_root)
    chart_paths = render_all_charts(data=data, report_root=report_root)
    metrics_path = report_root / REPORT_METRICS_FILENAME
    per_item_path = report_root / REPORT_PER_ITEM_FILENAME
    html_path = report_root / REPORT_HTML_FILENAME
    pdf_path = report_root / REPORT_PDF_FILENAME
    markdown_path = report_root / REPORT_MARKDOWN_FILENAME

    write_json_object(path=metrics_path, data=report_data_json(data=data))
    write_jsonl_objects(path=per_item_path, rows=per_item_rows(data=data))
    render_html(
        data=data,
        chart_paths=chart_paths,
        output_path=html_path,
        report_root=report_root,
    )
    render_pdf(
        data=data,
        chart_paths=chart_paths,
        output_path=pdf_path,
    )
    render_markdown(data=data, output_path=markdown_path)
    format_markdown_report(markdown_path=markdown_path)
    return ReportBuildResult(
        report_root=report_root,
        html_path=html_path,
        pdf_path=pdf_path,
        markdown_path=markdown_path,
        metrics_path=metrics_path,
        per_item_path=per_item_path,
        chart_paths=chart_paths,
    )


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--repo-root",
        type=Path,
        default=DEFAULT_REPO_ROOT,
        help="Path to the lexEN repository root.",
    )
    parser.add_argument(
        "--report-root",
        type=Path,
        default=DEFAULT_REPORT_ROOT,
        help="Directory where report artifacts are written.",
    )
    parser.add_argument(
        "--chart",
        choices=[chart_spec.name for chart_spec in CHART_SPECS],
        default=None,
        help="Render only one chart by name.",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    repo_root = Path(args.repo_root).resolve()
    report_root = Path(args.report_root).resolve()
    data = build_report_data(repo_root=repo_root)
    if args.chart is not None:
        chart_path = render_single_chart(
            chart_name=str(args.chart),
            data=data,
            report_root=report_root,
        )
        print(json.dumps({"chart": str(chart_path)}, indent=2, sort_keys=True))
        return
    result = build_agreement_report(repo_root=repo_root, report_root=report_root)
    print(
        json.dumps(
            {
                "html": str(result.html_path),
                "markdown": str(result.markdown_path),
                "metrics": str(result.metrics_path),
                "pdf": str(result.pdf_path),
                "per_item": str(result.per_item_path),
                "report_root": str(result.report_root),
            },
            indent=2,
            sort_keys=True,
        )
    )


if __name__ == "__main__":
    main()
