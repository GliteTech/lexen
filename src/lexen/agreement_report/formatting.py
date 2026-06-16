"""Formatting helpers for reports."""

from __future__ import annotations

from lexen.agreement_report.models import AgreementLevel, CountPercent


def count_percent_text(*, value: CountPercent) -> str:
    return f"{value.count} ({value.percent:.1f}%)"


def percent_text(*, value: float) -> str:
    return f"{value:.1f}%"


def kappa_text(*, value: float) -> str:
    return f"{value:.3f}"


def level_label(*, level: AgreementLevel) -> str:
    if level is AgreementLevel.ALL_THREE:
        return "All three agree"
    if level is AgreementLevel.EXACTLY_TWO:
        return "Exactly two agree"
    return "All three disagree"


def relation_label(*, relation: str) -> str:
    labels = {
        "all_three_agree_and_gold": "All three agree and match Maru2022",
        "all_three_agree_but_different": "All three agree, different from Maru2022",
        "all_three_disagree": "All three disagree",
        "exactly_two_agree_and_gold": "Exactly two agree and match Maru2022",
        "exactly_two_agree_but_different": "Exactly two agree, different from Maru2022",
    }
    return labels.get(relation, relation)


def maru_relation_label(*, relation: str) -> str:
    labels = {
        "accept_exact": "Selected exactly the Maru2022 label",
        "accept_plus_extra": "Selected Maru2022 plus extra sense(s)",
        "partial_overlap": "Partially overlapped Maru2022",
        "replace": "Selected different sense(s)",
        "unanswerable": "Marked cannot answer",
    }
    return labels[relation]


def short_label_list(*, values: list[str], limit: int = 80) -> str:
    text = ", ".join(values)
    if len(text) <= limit:
        return text
    return text[: limit - 1] + "…"
