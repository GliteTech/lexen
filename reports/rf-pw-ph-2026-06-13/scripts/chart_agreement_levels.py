"""Render the agreement-level chart."""

from __future__ import annotations

from lexen.agreement_report.build import build_report_data, render_single_chart
from lexen.agreement_report.paths import DEFAULT_REPORT_ROOT
from lexen.paths import DEFAULT_REPO_ROOT

CHART_NAME: str = "agreement_levels"


def main() -> None:
    data = build_report_data(repo_root=DEFAULT_REPO_ROOT)
    output_path = render_single_chart(
        chart_name=CHART_NAME,
        data=data,
        report_root=DEFAULT_REPORT_ROOT,
    )
    print(output_path)


if __name__ == "__main__":
    main()
