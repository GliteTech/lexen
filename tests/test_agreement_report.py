from __future__ import annotations

import re
from pathlib import Path

from lexen.agreement_report.metrics import build_report_data
from lexen.agreement_report.models import AgreementLevel, AppendixGroupID
from lexen.agreement_report.render_markdown import render_markdown
from lexen.paths import DEFAULT_REPO_ROOT


def test_three_reviewer_agreement_report_metrics() -> None:
    data = build_report_data(repo_root=DEFAULT_REPO_ROOT)

    assert data.metrics.reviewed_items == 363
    assert data.metrics.fine.level_counts[AgreementLevel.ALL_THREE].count == 129
    assert data.metrics.fine.level_counts[AgreementLevel.EXACTLY_TWO].count == 205
    assert data.metrics.fine.level_counts[AgreementLevel.ALL_DIFFER].count == 29
    assert data.metrics.glite.level_counts[AgreementLevel.ALL_THREE].count == 229
    assert data.metrics.glite.level_counts[AgreementLevel.EXACTLY_TWO].count == 124
    assert data.metrics.glite.level_counts[AgreementLevel.ALL_DIFFER].count == 10

    assert data.metrics.fine.gold_support_counts[3].count == 40
    assert data.metrics.fine.gold_support_counts[2].count == 56
    assert data.metrics.fine.gold_support_counts[1].count == 96
    assert data.metrics.fine.gold_support_counts[0].count == 171
    assert data.metrics.glite.gold_support_counts[3].count == 196
    assert data.metrics.glite.gold_support_counts[2].count == 54
    assert data.metrics.glite.gold_support_counts[1].count == 47
    assert data.metrics.glite.gold_support_counts[0].count == 66

    assert data.metrics.fine.all_three_agree_and_gold.count == 40
    assert data.metrics.fine.exactly_two_agree_and_gold.count == 56
    assert data.metrics.glite.all_three_agree_and_gold.count == 196
    assert data.metrics.glite.exactly_two_agree_and_gold.count == 54
    assert data.metrics.fine_non_unanimous_resolved_by_glite.count == 100
    assert {
        f"{pairwise.pair.left}+{pairwise.pair.right}": pairwise.matching_items
        for pairwise in data.metrics.fine.pairwise
    } == {
        "RF+PW": 208,
        "RF+PH": 170,
        "PW+PH": 214,
    }
    assert {
        f"{pairwise.pair.left}+{pairwise.pair.right}": pairwise.matching_items
        for pairwise in data.metrics.glite.pairwise
    } == {
        "RF+PW": 274,
        "RF+PH": 250,
        "PW+PH": 287,
    }
    assert data.metrics.cannot_answer.exactly_one_unanswerable == 50
    assert data.metrics.cannot_answer.exactly_two_unanswerable == 22
    assert data.metrics.cannot_answer.at_least_two_unanswerable == 27
    assert data.metrics.cannot_answer.at_least_two_reason_item_counts == {
        "__input_defective__": 6,
        "__inventory_inadequate__": 18,
        "__no_sense_applies__": 24,
    }
    assert data.metrics.cannot_answer.input_defective_by_document_support == {
        1: {"semeval2013.d006": 5, "semeval2015.d001": 1},
        2: {"semeval2013.d006": 1, "semeval2013.d011": 1},
    }
    assert data.metrics.cannot_answer.cannot_answer_by_document_support[2]["senseval3.d000"] == 5
    assert data.metrics.cannot_answer.cannot_answer_by_document_support[3] == {
        "semeval2013.d006": 1,
        "semeval2013.d011": 1,
        "senseval2.d002": 2,
        "senseval3.d000": 1,
    }
    assert data.metrics.no_consensus.total_items == 29
    assert data.metrics.no_consensus.pos_counts == {"ADJ": 6, "NOUN": 11, "VERB": 12}
    assert data.metrics.no_consensus.source_counts == {
        "semeval2013": 4,
        "semeval2015": 4,
        "senseval2": 11,
        "senseval3": 10,
    }
    assert data.metrics.no_consensus.fine_gold_support_counts == {0: 9, 1: 20}
    assert data.metrics.no_consensus.glite_gold_support_counts == {
        0: 2,
        1: 8,
        2: 13,
        3: 6,
    }
    assert data.metrics.no_consensus.cannot_answer_vote_counts == {0: 10, 1: 19}
    assert len(data.metrics.no_consensus.sampled_items) == 20


def test_agreement_report_appendix_groups_and_metadata() -> None:
    data = build_report_data(repo_root=DEFAULT_REPO_ROOT)

    assert {group.group_id: len(group.items) for group in data.metrics.appendix_groups} == {
        AppendixGroupID.ALL_THREE_MARU2022: 40,
        AppendixGroupID.ALL_THREE_CORRECTION: 84,
        AppendixGroupID.ALL_THREE_UNANSWERABLE: 5,
        AppendixGroupID.TWO_SAME_SENSE: 183,
        AppendixGroupID.TWO_UNANSWERABLE: 22,
        AppendixGroupID.ALL_DIFFER: 29,
    }

    negotiation = data.sense_metadata_by_key["negotiation%1:04:00::"]
    assert negotiation.synset_name == "negotiation.n.02"
    assert (
        negotiation.definition
        == "the activity or business of negotiating an agreement; coming to terms"
    )


def test_agreement_report_markdown_contains_full_appendix(tmp_path: Path) -> None:
    data = build_report_data(repo_root=DEFAULT_REPO_ROOT)
    output_path = tmp_path / "lexicographer_agreement.md"

    render_markdown(data=data, output_path=output_path)
    text = output_path.read_text(encoding="utf-8")

    assert len(re.findall(r"^### [A-F][0-9]+\.", text, flags=re.MULTILINE)) == 363
    assert "## Appendix A. All three reviewers selected the Maru2022 sense" in text
    assert "## Appendix F. All three reviewers disagreed" in text
    assert "[A](#appendix-a)" in text
    assert '<a id="appendix-e"></a>' in text
    assert "### Fine Raw Agreement Matrix" in text
    assert "57.3% (208/363)" in text
    assert "At least two reviewers marked cannot answer | 27 (7.4%)" in text
    assert "## Removed Reviewed Items" in text
    assert "No Maru2022 fallback label is used" in text
    assert "| No fine-grained sense received two-reviewer support | 29 |" in text
    assert "### No-Consensus Item Audit" in text
    assert "| 2/3 reviewers | semeval2013.d006 | 1 |" in text
    assert "united_states%1:14:00:: (united_states_government.n.01)" in text
    assert "Model " + "Score" not in text
