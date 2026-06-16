"""Chart rendering for the agreement report."""

from __future__ import annotations

from pathlib import Path
from typing import Any

import matplotlib

matplotlib.use("Agg")

from matplotlib import pyplot as plt
from matplotlib import ticker

from lexen.agreement_report.models import AgreementLevel, ReportData
from lexen.agreement_report.paths import (
    CHART_AGREEMENT_LEVELS_FILENAME,
    CHART_CANNOT_ANSWER_FILENAME,
    CHART_GOLD_SUPPORT_FILENAME,
    CHART_PAIRWISE_FILENAME,
    CHART_POS_SOURCE_FILENAME,
    CHART_VERDICT_SHAPE_FILENAME,
    REPORT_IMAGES_DIR,
)

COLOR_GREEN: str = "#13795b"
COLOR_BLUE: str = "#2f6fed"
COLOR_ORANGE: str = "#d97904"
COLOR_RED: str = "#c43b4d"
COLOR_PURPLE: str = "#7a4cc2"
COLOR_CYAN: str = "#0f8aa6"
COLOR_GRAY: str = "#6c757d"
COLOR_GRID: str = "#e6ebf2"
COLOR_DARK: str = "#17202a"

FIGURE_DPI: int = 180


def configure_style() -> None:
    plt.rcParams.update(
        {
            "axes.edgecolor": "#d8dee8",
            "axes.facecolor": "white",
            "axes.grid": False,
            "axes.labelcolor": COLOR_DARK,
            "axes.spines.right": False,
            "axes.spines.top": False,
            "figure.facecolor": "white",
            "font.family": "DejaVu Sans",
            "font.size": 10,
            "grid.color": COLOR_GRID,
            "grid.linewidth": 0.7,
            "legend.frameon": False,
            "savefig.facecolor": "white",
            "xtick.color": COLOR_DARK,
            "ytick.color": COLOR_DARK,
        }
    )


def configure_percent_axis(*, axis: Any, maximum: float = 100.0, step: float = 20.0) -> None:
    axis.set_xlim(0, maximum)
    axis.xaxis.set_major_locator(ticker.MultipleLocator(step))
    axis.xaxis.set_major_formatter(ticker.PercentFormatter(xmax=100, decimals=0))
    axis.set_axisbelow(True)


def save_current_figure(*, output_path: Path) -> None:
    output_path.parent.mkdir(parents=True, exist_ok=True)
    plt.tight_layout()
    plt.savefig(output_path, dpi=FIGURE_DPI, bbox_inches="tight")
    plt.close()


def chart_agreement_levels(
    *,
    data: ReportData,
    output_path: Path,
) -> None:
    configure_style()
    _figure, axis = plt.subplots(figsize=(9.2, 4.6))
    granularities = ["Fine WordNet", "Glite coarse"]
    metrics = [data.metrics.fine, data.metrics.glite]
    levels = [
        (AgreementLevel.ALL_THREE, COLOR_GREEN),
        (AgreementLevel.EXACTLY_TWO, COLOR_ORANGE),
        (AgreementLevel.ALL_DIFFER, COLOR_RED),
    ]
    y_positions = [0.0, 1.0]
    lefts = [0.0 for _metric in metrics]
    for level, color in levels:
        values = [metric.level_counts[level].percent for metric in metrics]
        axis.barh(
            y_positions,
            values,
            left=lefts,
            color=color,
            height=0.46,
            zorder=3,
        )
        lefts = [lefts[index] + values[index] for index in range(len(lefts))]
    configure_percent_axis(axis=axis)
    axis.set_xlabel("Share of 363 reviewed items")
    axis.set_yticks(y_positions, granularities)
    axis.set_ylim(-0.50, 1.50)
    axis.invert_yaxis()
    save_current_figure(output_path=output_path)


def chart_gold_support(
    *,
    data: ReportData,
    output_path: Path,
) -> None:
    configure_style()
    _figure, axis = plt.subplots(figsize=(9.2, 4.6))
    support_levels = [3, 2, 1, 0]
    rows = [
        ("Fine WordNet", data.metrics.fine.gold_support_counts),
        ("Glite coarse", data.metrics.glite.gold_support_counts),
    ]
    colors = [COLOR_GREEN, COLOR_CYAN, COLOR_ORANGE, COLOR_RED]
    y_positions = [0.0, 1.0]
    lefts = [0.0 for _row in rows]
    for support, color in zip(support_levels, colors, strict=True):
        values = [counts[support].percent for _name, counts in rows]
        axis.barh(
            y_positions,
            values,
            left=lefts,
            color=color,
            height=0.46,
            zorder=3,
        )
        lefts = [lefts[index] + values[index] for index in range(len(lefts))]
    configure_percent_axis(axis=axis)
    axis.set_xlabel("Share of 363 reviewed items")
    axis.set_yticks(y_positions, [name for name, _counts in rows])
    axis.set_ylim(-0.50, 1.50)
    axis.invert_yaxis()
    save_current_figure(output_path=output_path)


def chart_pairwise_coefficients(
    *,
    data: ReportData,
    output_path: Path,
) -> None:
    configure_style()
    figure, axes = plt.subplots(nrows=1, ncols=2, figsize=(10.8, 4.8), sharey=True)
    pair_labels = [
        f"{pairwise.pair.left} + {pairwise.pair.right}" for pairwise in data.metrics.fine.pairwise
    ]
    y_positions = [float(index) for index in range(len(pair_labels))]
    fine_raw = [pairwise.raw_agreement for pairwise in data.metrics.fine.pairwise]
    glite_raw = [pairwise.raw_agreement for pairwise in data.metrics.glite.pairwise]
    fine_kappa = [pairwise.cohen_kappa for pairwise in data.metrics.fine.pairwise]
    glite_kappa = [pairwise.cohen_kappa for pairwise in data.metrics.glite.pairwise]
    panels = [
        (axes[0], "Raw agreement", fine_raw, glite_raw, 0.0, 85.0, 10.0),
        (axes[1], "Cohen's kappa", fine_kappa, glite_kappa, 0.0, 0.85, 0.10),
    ]
    for axis, x_label, fine_values, glite_values, x_min, x_max, step in panels:
        fine_positions = [position - 0.17 for position in y_positions]
        glite_positions = [position + 0.17 for position in y_positions]
        axis.barh(
            fine_positions,
            fine_values,
            height=0.28,
            color=COLOR_BLUE,
            zorder=3,
        )
        axis.barh(
            glite_positions,
            glite_values,
            height=0.28,
            color=COLOR_GREEN,
            zorder=3,
        )
        axis.set_xlim(x_min, x_max)
        axis.xaxis.set_major_locator(ticker.MultipleLocator(step))
        if x_label == "Raw agreement":
            axis.xaxis.set_major_formatter(ticker.PercentFormatter(xmax=100, decimals=0))
        else:
            axis.xaxis.set_major_formatter(ticker.FormatStrFormatter("%.1f"))
        axis.set_xlabel(x_label)
        axis.set_yticks(y_positions, pair_labels)
    axes[0].invert_yaxis()
    figure.subplots_adjust(wspace=0.25)
    save_current_figure(output_path=output_path)


def chart_verdict_shape(
    *,
    data: ReportData,
    output_path: Path,
) -> None:
    configure_style()
    _figure, axis = plt.subplots(figsize=(9.2, 4.2))
    reviewers = [shape.reviewer for shape in data.metrics.verdict_shapes]
    y_positions = [float(index) for index in range(len(reviewers))]
    single = [shape.single_sense_items for shape in data.metrics.verdict_shapes]
    multi = [shape.multi_sense_items for shape in data.metrics.verdict_shapes]
    cannot = [shape.cannot_answer_items for shape in data.metrics.verdict_shapes]
    left = [0 for _ in reviewers]
    for values, color in [
        (single, COLOR_GREEN),
        (multi, COLOR_BLUE),
        (cannot, COLOR_RED),
    ]:
        axis.barh(
            y_positions,
            values,
            left=left,
            color=color,
            height=0.48,
            zorder=3,
        )
        left = [left[index] + values[index] for index in range(len(left))]
    axis.set_xlabel("Items")
    axis.set_yticks(y_positions, reviewers)
    axis.set_xlim(0, data.metrics.reviewed_items)
    axis.xaxis.set_major_locator(ticker.MultipleLocator(60))
    axis.set_axisbelow(True)
    axis.invert_yaxis()
    save_current_figure(output_path=output_path)


def chart_cannot_answer(
    *,
    data: ReportData,
    output_path: Path,
) -> None:
    configure_style()
    _figure, axis = plt.subplots(figsize=(9.2, 4.9))
    reviewers = list(data.metrics.cannot_answer.reason_counts_by_reviewer)
    reasons = sorted(
        {
            reason
            for counts in data.metrics.cannot_answer.reason_counts_by_reviewer.values()
            for reason in counts
        }
    )
    colors = [COLOR_RED, COLOR_ORANGE, COLOR_PURPLE, COLOR_GRAY]
    y_positions = [float(index) for index in range(len(reviewers))]
    left = [0 for _ in reviewers]
    for reason_index, reason in enumerate(reasons):
        values = [
            data.metrics.cannot_answer.reason_counts_by_reviewer[reviewer].get(reason, 0)
            for reviewer in reviewers
        ]
        color = colors[reason_index % len(colors)]
        axis.barh(
            y_positions,
            values,
            left=left,
            color=color,
            height=0.48,
            zorder=3,
        )
        left = [left[index] + values[index] for index in range(len(left))]
    axis.set_xlabel("Reason tags")
    axis.set_yticks(y_positions, reviewers)
    axis.set_xlim(0, max(left) + 8)
    axis.xaxis.set_major_locator(ticker.MultipleLocator(10))
    axis.set_axisbelow(True)
    axis.invert_yaxis()
    save_current_figure(output_path=output_path)


def chart_pos_source(
    *,
    data: ReportData,
    output_path: Path,
) -> None:
    configure_style()
    figure, axes = plt.subplots(nrows=1, ncols=2, figsize=(12.0, 4.9), sharex=True)
    panels = [
        (axes[0], "Part of speech", data.metrics.pos_groups),
        (axes[1], "Source test set", data.metrics.source_groups),
    ]
    for axis, title, groups in panels:
        names = [f"{group.group_name} (n={group.total_items})" for group in groups]
        fine_values = [group.fine_all_three.percent for group in groups]
        glite_values = [group.glite_all_three.percent for group in groups]
        y_positions = [float(index) for index in range(len(names))]
        fine_positions = [position - 0.17 for position in y_positions]
        glite_positions = [position + 0.17 for position in y_positions]
        axis.barh(
            fine_positions,
            fine_values,
            height=0.28,
            color=COLOR_BLUE,
            zorder=3,
        )
        axis.barh(
            glite_positions,
            glite_values,
            height=0.28,
            color=COLOR_GREEN,
            zorder=3,
        )
        axis.set_title(title, fontsize=13, fontweight="bold", loc="left")
        configure_percent_axis(axis=axis, maximum=85.0, step=10.0)
        axis.set_yticks(y_positions, names)
        axis.invert_yaxis()
        axis.set_xlabel("All-three agreement")
    figure.subplots_adjust(wspace=0.42)
    save_current_figure(output_path=output_path)


def render_all_charts(
    *,
    data: ReportData,
    report_root: Path,
) -> dict[str, Path]:
    images_dir = report_root / REPORT_IMAGES_DIR.name
    chart_paths = {
        "agreement_levels": images_dir / CHART_AGREEMENT_LEVELS_FILENAME,
        "gold_support": images_dir / CHART_GOLD_SUPPORT_FILENAME,
        "pairwise_coefficients": images_dir / CHART_PAIRWISE_FILENAME,
        "verdict_shape": images_dir / CHART_VERDICT_SHAPE_FILENAME,
        "cannot_answer_reasons": images_dir / CHART_CANNOT_ANSWER_FILENAME,
        "pos_source_agreement": images_dir / CHART_POS_SOURCE_FILENAME,
    }
    chart_agreement_levels(data=data, output_path=chart_paths["agreement_levels"])
    chart_gold_support(data=data, output_path=chart_paths["gold_support"])
    chart_pairwise_coefficients(data=data, output_path=chart_paths["pairwise_coefficients"])
    chart_verdict_shape(data=data, output_path=chart_paths["verdict_shape"])
    chart_cannot_answer(data=data, output_path=chart_paths["cannot_answer_reasons"])
    chart_pos_source(data=data, output_path=chart_paths["pos_source_agreement"])
    return chart_paths


def chart_function_by_name() -> dict[str, str]:
    return {
        "agreement_levels": CHART_AGREEMENT_LEVELS_FILENAME,
        "cannot_answer_reasons": CHART_CANNOT_ANSWER_FILENAME,
        "gold_support": CHART_GOLD_SUPPORT_FILENAME,
        "pairwise_coefficients": CHART_PAIRWISE_FILENAME,
        "pos_source_agreement": CHART_POS_SOURCE_FILENAME,
        "verdict_shape": CHART_VERDICT_SHAPE_FILENAME,
    }
