from __future__ import annotations

from collections.abc import Sequence

from lexen.models import ReviewVerdict, SenseKey
from lexen.paths import (
    DECISION_THREE_WAY_EXACT,
    DECISION_THREE_WAY_NO_CONSENSUS,
    DECISION_TWO_OF_THREE_CANNOT_ANSWER,
    DECISION_TWO_OF_THREE_SENSE,
    DECISION_UNREVIEWED,
    DISPOSITION_REMOVED,
    DISPOSITION_RETAINED,
)
from lexen.release import decide_label


def review_verdict(
    *,
    keys: Sequence[SenseKey] = (),
    cannot_answer: Sequence[str] = (),
) -> ReviewVerdict:
    return ReviewVerdict(
        instance_id="d000.s000.t000",
        cannot_answer=list(cannot_answer),
        chosen_sense_keys=list(keys),
    )


def test_unreviewed_items_keep_maru_label() -> None:
    maru_keys = ["run%2:38:00::"]

    decision = decide_label(
        maru_keys=maru_keys,
        rf_verdict=None,
        pw_verdict=None,
        ph_verdict=None,
    )

    assert decision.lexen_gold_keys == maru_keys
    assert decision.decision == DECISION_UNREVIEWED
    assert decision.disposition == DISPOSITION_RETAINED
    assert decision.removal_reason is None


def test_unanimous_same_protocol_agreement_becomes_gold_label() -> None:
    maru_keys = ["run%2:38:00::"]

    decision = decide_label(
        maru_keys=maru_keys,
        rf_verdict=review_verdict(keys=["run%2:41:00::", "run%2:41:00::"]),
        pw_verdict=review_verdict(keys=["run%2:41:00::"]),
        ph_verdict=review_verdict(keys=["run%2:41:00::"]),
    )

    assert decision.lexen_gold_keys == ["run%2:41:00::"]
    assert decision.decision == DECISION_THREE_WAY_EXACT
    assert decision.disposition == DISPOSITION_RETAINED
    assert decision.removal_reason is None


def test_two_of_three_sense_agreement_becomes_gold_label() -> None:
    maru_keys = ["run%2:38:00::"]

    decision = decide_label(
        maru_keys=maru_keys,
        rf_verdict=review_verdict(keys=["run%2:41:00::"]),
        pw_verdict=review_verdict(keys=["run%2:41:00::"]),
        ph_verdict=review_verdict(keys=["run%2:42:00::"]),
    )

    assert decision.lexen_gold_keys == ["run%2:41:00::"]
    assert decision.decision == DECISION_TWO_OF_THREE_SENSE
    assert decision.disposition == DISPOSITION_RETAINED
    assert decision.removal_reason is None


def test_two_of_three_cannot_answer_removes_item() -> None:
    maru_keys = ["run%2:38:00::"]

    decision = decide_label(
        maru_keys=maru_keys,
        rf_verdict=review_verdict(cannot_answer=["__no_sense_applies__"]),
        pw_verdict=review_verdict(cannot_answer=["__inventory_inadequate__"]),
        ph_verdict=review_verdict(keys=["run%2:42:00::"]),
    )

    assert decision.lexen_gold_keys == []
    assert decision.decision == DECISION_TWO_OF_THREE_CANNOT_ANSWER
    assert decision.disposition == DISPOSITION_REMOVED
    assert decision.removal_reason == DECISION_TWO_OF_THREE_CANNOT_ANSWER


def test_no_three_annotator_consensus_removes_item() -> None:
    maru_keys = ["run%2:38:00::"]

    decision = decide_label(
        maru_keys=maru_keys,
        rf_verdict=review_verdict(keys=["run%2:41:00::"]),
        pw_verdict=review_verdict(keys=["run%2:42:00::"]),
        ph_verdict=review_verdict(keys=["run%2:43:00::"]),
    )

    assert decision.lexen_gold_keys == []
    assert decision.decision == DECISION_THREE_WAY_NO_CONSENSUS
    assert decision.disposition == DISPOSITION_REMOVED
    assert decision.removal_reason == DECISION_THREE_WAY_NO_CONSENSUS
