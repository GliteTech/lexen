"""Build the lexEN release from versioned source artifacts."""

from __future__ import annotations

import argparse
import json
import xml.etree.ElementTree as ET
from collections import Counter
from pathlib import Path

from lexen.glite import (
    GLITE_MAPPING_ID,
    GLITE_SCHEMA_VERSION,
    UNMAPPED_PREFIX,
    candidate_sense_mappings,
    coarsen_sense_keys,
    load_glite_mapping,
)
from lexen.io import (
    artifact_records_for_paths,
    read_gzip_jsonl_text,
    read_json_object,
    write_json_object,
    write_jsonl_objects,
)
from lexen.models import (
    AnnotatorRecord,
    BuildInputs,
    BuildOutputPaths,
    BuildResult,
    BuiltRecords,
    JsonObject,
    LabelDecision,
    ReviewFile,
    ReviewVerdict,
    SelectionRecord,
    SenseKey,
    SourceSentence,
)
from lexen.paths import (
    ACTIVE_RELEASE_ID,
    CANONICAL_ANNOTATORS,
    CANONICAL_ITEMS_FILENAME,
    DATA_DIRNAME,
    DATA_XML_SUFFIX,
    DATASET_CANARY,
    DATASET_ID,
    DATASET_METADATA_FILENAME,
    DATASET_SCHEMA_VERSION,
    DECISION_THREE_WAY_EXACT,
    DECISION_THREE_WAY_NO_CONSENSUS,
    DECISION_TWO_OF_THREE_CANNOT_ANSWER,
    DECISION_TWO_OF_THREE_SENSE,
    DECISION_UNREVIEWED,
    DEFAULT_REPO_ROOT,
    DISPOSITION_REMOVED,
    DISPOSITION_RETAINED,
    EXPORTS_DIRNAME,
    GOLD_KEY_SUFFIX,
    ITEM_SCHEMA_VERSION,
    MARU_SOURCE_DIR,
    MARU_XML_FILENAME,
    PH_ANNOTATOR_ID,
    PH_REVIEW_SOURCE_DIR,
    PH_VERDICTS_FILENAME,
    PW_ANNOTATOR_ID,
    PW_REVIEW_SOURCE_DIR,
    PW_VERDICTS_FILENAME,
    RAGANATO_EXPORT_DIRNAME,
    RAGANATO_GOLD_FILENAME,
    RAGANATO_SOURCE_DIR,
    REMOVED_SCHEMA_VERSION,
    REMOVED_SUFFIX,
    REPORTS_DIRNAME,
    REVIEW_SCHEMA_VERSION,
    REVIEWS_FILENAME,
    RF_ANNOTATOR_ID,
    RF_REVIEW_SOURCE_DIR,
    RF_VERDICTS_FILENAME,
    SELECTION_JSONL_GZ_FILENAME,
    SELECTION_SOURCE_DIR,
    SENSEBENCH_EXPORT_DIRNAME,
    SOURCE_MANIFEST_FILENAME,
    SOURCES_DIRNAME,
    WATERFALL_SUMMARY_FILENAME,
)


def sentence_words(*, sentence: SourceSentence) -> list[str]:
    return [token.surface for token in sentence.tokens]


def sentence_id_from_item_id(*, item_id: str) -> str:
    return ".".join(item_id.split(".")[:-1])


def document_id_from_item_id(*, item_id: str) -> str:
    return ".".join(item_id.split(".")[:-2])


def sorted_unique_keys(*, keys: list[SenseKey]) -> list[SenseKey]:
    return sorted(set(keys))


def read_gold_key(*, path: Path) -> dict[str, list[SenseKey]]:
    labels: dict[str, list[SenseKey]] = {}
    with path.open(encoding="utf-8") as handle:
        for line_number, raw_line in enumerate(handle, start=1):
            line = raw_line.strip()
            if len(line) == 0:
                continue
            parts = line.split()
            if len(parts) < 2:
                raise ValueError(f"gold key line has no sense key at {path}:{line_number}")
            if parts[0] in labels:
                raise ValueError(f"duplicate gold key item id {parts[0]} in {path}")
            labels[parts[0]] = parts[1:]
    return labels


def annotator_record_from_verdict(*, verdict: ReviewVerdict) -> AnnotatorRecord:
    return AnnotatorRecord(
        chosen_sense_keys=sorted_unique_keys(keys=verdict.chosen_sense_keys),
        cannot_answer=list(verdict.cannot_answer),
        cannot_answer_notes=verdict.cannot_answer_notes,
        comment=verdict.comment,
    )


def annotator_record_json(*, record: AnnotatorRecord) -> JsonObject:
    return {
        "cannot_answer": record.cannot_answer,
        "cannot_answer_notes": record.cannot_answer_notes,
        "chosen_sense_keys": record.chosen_sense_keys,
        "comment": record.comment,
    }


def review_file_to_verdicts_by_id(
    *,
    review_file: ReviewFile,
    annotator: str,
) -> dict[str, ReviewVerdict]:
    verdicts_by_id: dict[str, ReviewVerdict] = {}
    for verdict in review_file.verdicts:
        if verdict.instance_id in verdicts_by_id:
            raise ValueError(f"duplicate {annotator} verdict for {verdict.instance_id}")
        verdicts_by_id[verdict.instance_id] = verdict
    return verdicts_by_id


def load_build_inputs(*, repo_root: Path) -> BuildInputs:
    selection_path = repo_root / SELECTION_SOURCE_DIR / SELECTION_JSONL_GZ_FILENAME
    selection_records = [
        SelectionRecord.model_validate_json(line)
        for line in read_gzip_jsonl_text(path=selection_path)
    ]

    rf_file = ReviewFile.model_validate(
        read_json_object(path=repo_root / RF_REVIEW_SOURCE_DIR / RF_VERDICTS_FILENAME)
    )
    pw_file = ReviewFile.model_validate(
        read_json_object(path=repo_root / PW_REVIEW_SOURCE_DIR / PW_VERDICTS_FILENAME)
    )
    ph_file = ReviewFile.model_validate(
        read_json_object(path=repo_root / PH_REVIEW_SOURCE_DIR / PH_VERDICTS_FILENAME)
    )
    return BuildInputs(
        raganato_original_by_id=read_gold_key(
            path=repo_root / RAGANATO_SOURCE_DIR / RAGANATO_GOLD_FILENAME
        ),
        selection_records=selection_records,
        rf_verdicts_by_id=review_file_to_verdicts_by_id(
            review_file=rf_file,
            annotator=RF_ANNOTATOR_ID,
        ),
        pw_verdicts_by_id=review_file_to_verdicts_by_id(
            review_file=pw_file,
            annotator=PW_ANNOTATOR_ID,
        ),
        ph_verdicts_by_id=review_file_to_verdicts_by_id(
            review_file=ph_file,
            annotator=PH_ANNOTATOR_ID,
        ),
    )


def decide_label(
    *,
    maru_keys: list[SenseKey],
    rf_verdict: ReviewVerdict | None,
    pw_verdict: ReviewVerdict | None,
    ph_verdict: ReviewVerdict | None,
) -> LabelDecision:
    verdicts = [verdict for verdict in (rf_verdict, pw_verdict, ph_verdict) if verdict is not None]
    if len(verdicts) == 0:
        return LabelDecision(
            lexen_gold_keys=maru_keys,
            decision=DECISION_UNREVIEWED,
            disposition=DISPOSITION_RETAINED,
            removal_reason=None,
        )
    if len(verdicts) != len(CANONICAL_ANNOTATORS):
        raise ValueError("reviewed items must have all canonical annotator verdicts")

    non_empty_key_votes: Counter[tuple[SenseKey, ...]] = Counter()
    cannot_answer_votes = 0
    for verdict in verdicts:
        keys = tuple(sorted_unique_keys(keys=verdict.chosen_sense_keys))
        if len(keys) > 0:
            non_empty_key_votes[keys] += 1
            continue
        if len(verdict.cannot_answer) > 0:
            cannot_answer_votes += 1

    if len(non_empty_key_votes) > 0:
        winning_keys, winning_count = non_empty_key_votes.most_common(1)[0]
        if winning_count >= 2:
            decision = (
                DECISION_THREE_WAY_EXACT
                if winning_count == len(CANONICAL_ANNOTATORS)
                else DECISION_TWO_OF_THREE_SENSE
            )
            sense_keys = list(winning_keys)
            return LabelDecision(
                lexen_gold_keys=sense_keys,
                decision=decision,
                disposition=DISPOSITION_RETAINED,
                removal_reason=None,
            )

    if cannot_answer_votes >= 2:
        return LabelDecision(
            lexen_gold_keys=[],
            decision=DECISION_TWO_OF_THREE_CANNOT_ANSWER,
            disposition=DISPOSITION_REMOVED,
            removal_reason=DECISION_TWO_OF_THREE_CANNOT_ANSWER,
        )
    return LabelDecision(
        lexen_gold_keys=[],
        decision=DECISION_THREE_WAY_NO_CONSENSUS,
        disposition=DISPOSITION_REMOVED,
        removal_reason=DECISION_THREE_WAY_NO_CONSENSUS,
    )


def label_glite_json(
    *,
    sense_keys: list[SenseKey],
    glite_mapping: dict[SenseKey, str],
) -> JsonObject:
    return coarsen_sense_keys(sense_keys=sense_keys, mapping=glite_mapping).to_json_object()


def review_annotators_json(
    *,
    rf_verdict: ReviewVerdict,
    pw_verdict: ReviewVerdict,
    ph_verdict: ReviewVerdict,
) -> JsonObject:
    return {
        RF_ANNOTATOR_ID: annotator_record_json(
            record=annotator_record_from_verdict(verdict=rf_verdict)
        ),
        PW_ANNOTATOR_ID: annotator_record_json(
            record=annotator_record_from_verdict(verdict=pw_verdict)
        ),
        PH_ANNOTATOR_ID: annotator_record_json(
            record=annotator_record_from_verdict(verdict=ph_verdict)
        ),
    }


def consensus_json(*, decision: LabelDecision) -> JsonObject:
    return {
        "decision": decision.decision,
        "disposition": decision.disposition,
        "removal_reason": decision.removal_reason,
        "sense_keys": decision.lexen_gold_keys,
    }


def glite_record(
    *,
    candidate_sense_keys: list[SenseKey],
    raganato_original_keys: list[SenseKey],
    maru_keys: list[SenseKey],
    lexen_gold_keys: list[SenseKey],
    annotators: JsonObject | None,
    glite_mapping: dict[SenseKey, str],
) -> JsonObject:
    reviewer_labels: JsonObject | None = None
    if annotators is not None:
        reviewer_labels = {}
        for annotator in CANONICAL_ANNOTATORS:
            annotator_record = annotators[annotator]
            if not isinstance(annotator_record, dict):
                raise TypeError("annotator record must be an object")
            reviewer_labels[annotator] = label_glite_json(
                sense_keys=[str(key) for key in annotator_record["chosen_sense_keys"]],
                glite_mapping=glite_mapping,
            )
    candidate_rows = candidate_sense_mappings(
        sense_keys=candidate_sense_keys,
        mapping=glite_mapping,
    )
    return {
        "candidate_concept_ids": sorted({str(row["concept_id"]) for row in candidate_rows}),
        "candidate_sense_mappings": candidate_rows,
        "labels": {
            "lexen_gold": label_glite_json(
                sense_keys=lexen_gold_keys,
                glite_mapping=glite_mapping,
            ),
            "maru2022": label_glite_json(sense_keys=maru_keys, glite_mapping=glite_mapping),
            "raganato_original": label_glite_json(
                sense_keys=raganato_original_keys,
                glite_mapping=glite_mapping,
            ),
        },
        "mapping_id": GLITE_MAPPING_ID,
        "reviewers": reviewer_labels,
        "schema_version": GLITE_SCHEMA_VERSION,
        "unmapped_prefix": UNMAPPED_PREFIX,
    }


def build_records(
    *,
    inputs: BuildInputs,
    glite_mapping: dict[SenseKey, str],
) -> BuiltRecords:
    items: list[JsonObject] = []
    removed_items: list[JsonObject] = []
    reviews: list[JsonObject] = []
    counts: Counter[str] = Counter()
    reviewed_ids = set(inputs.rf_verdicts_by_id)
    if reviewed_ids != set(inputs.pw_verdicts_by_id):
        raise ValueError("canonical reviewed item id sets differ")
    if reviewed_ids != set(inputs.ph_verdicts_by_id):
        raise ValueError("canonical reviewed item id sets differ")

    for record in inputs.selection_records:
        item_id = record.instance_id
        if item_id not in inputs.raganato_original_by_id:
            raise ValueError(f"Raganato original gold key missing reviewed source id: {item_id}")
        raganato_original_keys = sorted_unique_keys(keys=inputs.raganato_original_by_id[item_id])
        maru_keys = sorted_unique_keys(keys=record.gold_sense_keys)
        rf_verdict = inputs.rf_verdicts_by_id.get(item_id)
        pw_verdict = inputs.pw_verdicts_by_id.get(item_id)
        ph_verdict = inputs.ph_verdicts_by_id.get(item_id)
        reviewed = rf_verdict is not None and pw_verdict is not None and ph_verdict is not None
        decision = decide_label(
            maru_keys=maru_keys,
            rf_verdict=rf_verdict,
            pw_verdict=pw_verdict,
            ph_verdict=ph_verdict,
        )
        target_token_index = record.context.target_token_index
        target_tokens = record.context.target_sentence.tokens
        if target_token_index >= len(target_tokens):
            raise ValueError(f"target_token_index outside target sentence for {item_id}")
        target_token = target_tokens[target_token_index]

        counts["total_source_items"] += 1
        counts[f"decision.{decision.decision}"] += 1
        if reviewed:
            counts["reviewed_audit_items"] += 1

        context = {
            "following_sentences": [
                sentence_words(sentence=sentence) for sentence in record.context.following_sentences
            ],
            "preceding_sentences": [
                sentence_words(sentence=sentence) for sentence in record.context.preceding_sentences
            ],
            "target_sentence": sentence_words(sentence=record.context.target_sentence),
        }
        model_panel = {
            "modal_count": record.modal_count,
            "modal_predicted_sense_id": record.modal_predicted_sense_id,
            "n_correct": record.n_correct,
            "n_distinct_predictions": record.n_distinct_predictions,
            "n_models_total": record.n_models_total,
            "top_prediction_share": record.top_prediction_share,
        }
        candidate_sense_keys = [sense.sense_key for sense in record.all_wordnet_senses]
        annotators: JsonObject | None = None
        consensus: JsonObject | None = None

        if reviewed:
            if rf_verdict is None or pw_verdict is None or ph_verdict is None:
                raise AssertionError("reviewed item must have all verdicts")
            annotators = review_annotators_json(
                rf_verdict=rf_verdict,
                pw_verdict=pw_verdict,
                ph_verdict=ph_verdict,
            )
            consensus = consensus_json(decision=decision)
            reviews.append(
                {
                    "annotators": annotators,
                    "consensus": consensus,
                    "dataset_canary": DATASET_CANARY,
                    "item_id": item_id,
                    "schema_version": REVIEW_SCHEMA_VERSION,
                }
            )

        if decision.disposition == DISPOSITION_REMOVED:
            if not reviewed:
                raise ValueError(f"unreviewed item cannot be removed: {item_id}")
            if rf_verdict is None or pw_verdict is None or ph_verdict is None:
                raise AssertionError("removed item must have all verdicts")
            if annotators is None or consensus is None:
                raise AssertionError("removed item must have annotators and consensus")
            counts["removed_items"] += 1
            removed_items.append(
                {
                    "annotators": annotators,
                    "candidate_sense_keys": candidate_sense_keys,
                    "context": context,
                    "dataset_canary": DATASET_CANARY,
                    "document_id": document_id_from_item_id(item_id=item_id),
                    "glite": glite_record(
                        candidate_sense_keys=candidate_sense_keys,
                        raganato_original_keys=raganato_original_keys,
                        maru_keys=maru_keys,
                        lexen_gold_keys=[],
                        annotators=annotators,
                        glite_mapping=glite_mapping,
                    ),
                    "item_id": item_id,
                    "labels": {
                        "lexen_gold": {
                            "decision": decision.decision,
                            "is_empty": True,
                            "sense_keys": [],
                        },
                        "maru2022": {
                            "sense_keys": maru_keys,
                        },
                        "raganato_original": {
                            "sense_keys": raganato_original_keys,
                        },
                    },
                    "lemma": record.lemma,
                    "maru_prompt_sense_keys": record.candidates_in_maru_prompt,
                    "model_panel": model_panel,
                    "pos": record.pos,
                    "removal": {
                        "decision": decision.decision,
                        "reason": decision.removal_reason,
                    },
                    "review": {
                        "annotators": annotators,
                        "consensus": consensus,
                        "is_reviewed": True,
                        "lexicographer_decision": decision.decision,
                        "model_panel": model_panel,
                        "release_disposition": decision.disposition,
                        "review_annotators": list(CANONICAL_ANNOTATORS),
                        "status": "reviewed",
                        "suspicion_rationale": record.suspicion_rationale,
                        "suspicion_set": record.suspicion_set,
                    },
                    "schema_version": REMOVED_SCHEMA_VERSION,
                    "sentence_id": sentence_id_from_item_id(item_id=item_id),
                    "source_dataset": record.dataset,
                    "target": {
                        "text": target_token.surface,
                        "token_index": target_token_index,
                    },
                }
            )
            continue

        if len(decision.lexen_gold_keys) == 0:
            raise ValueError(f"retained item has empty lexEN label: {item_id}")

        counts["total_items"] += 1
        counts["reviewed_items" if reviewed else "unreviewed_items"] += 1
        if decision.lexen_gold_keys != maru_keys:
            counts["lexen_gold_changed_from_maru"] += 1

        item = {
            "candidate_sense_keys": candidate_sense_keys,
            "context": context,
            "dataset_canary": DATASET_CANARY,
            "document_id": document_id_from_item_id(item_id=item_id),
            "glite": glite_record(
                candidate_sense_keys=candidate_sense_keys,
                raganato_original_keys=raganato_original_keys,
                maru_keys=maru_keys,
                lexen_gold_keys=decision.lexen_gold_keys,
                annotators=annotators,
                glite_mapping=glite_mapping,
            ),
            "item_id": item_id,
            "labels": {
                "lexen_gold": {
                    "decision": decision.decision,
                    "is_empty": False,
                    "sense_keys": decision.lexen_gold_keys,
                },
                "maru2022": {
                    "sense_keys": maru_keys,
                },
                "raganato_original": {
                    "sense_keys": raganato_original_keys,
                },
            },
            "lemma": record.lemma,
            "maru_prompt_sense_keys": record.candidates_in_maru_prompt,
            "pos": record.pos,
            "review": {
                "annotators": annotators,
                "consensus": consensus,
                "is_reviewed": reviewed,
                "lexicographer_decision": decision.decision,
                "model_panel": model_panel,
                "release_disposition": decision.disposition,
                "review_annotators": list(CANONICAL_ANNOTATORS),
                "status": "reviewed" if reviewed else "unreviewed",
                "suspicion_rationale": record.suspicion_rationale,
                "suspicion_set": record.suspicion_set,
            },
            "schema_version": ITEM_SCHEMA_VERSION,
            "sentence_id": sentence_id_from_item_id(item_id=item_id),
            "source_dataset": record.dataset,
            "target": {
                "text": target_token.surface,
                "token_index": target_token_index,
            },
        }
        items.append(item)

    return BuiltRecords(
        items=items,
        removed_items=removed_items,
        reviews=reviews,
        counts=dict(sorted(counts.items())),
    )


def sensebench_record(*, item: JsonObject) -> JsonObject:
    context = item["context"]
    if not isinstance(context, dict):
        raise TypeError("context must be an object")
    preceding_sentences = context["preceding_sentences"]
    target_sentence = context["target_sentence"]
    following_sentences = context["following_sentences"]
    if not isinstance(preceding_sentences, list):
        raise TypeError("preceding_sentences must be a list")
    if not isinstance(target_sentence, list):
        raise TypeError("target_sentence must be a list")
    if not isinstance(following_sentences, list):
        raise TypeError("following_sentences must be a list")
    sentences = [
        [str(token) for token in sentence]
        for sentence in [*preceding_sentences, target_sentence, *following_sentences]
    ]
    labels = item["labels"]
    if not isinstance(labels, dict):
        raise TypeError("labels must be an object")
    lexen_gold = labels["lexen_gold"]
    review = item["review"]
    if not isinstance(lexen_gold, dict) or not isinstance(review, dict):
        raise TypeError("label and review fields must be objects")
    maru2022 = labels["maru2022"]
    raganato_original = labels["raganato_original"]
    glite = item["glite"]
    if not isinstance(maru2022, dict) or not isinstance(raganato_original, dict):
        raise TypeError("label entries must be objects")
    if not isinstance(glite, dict):
        raise TypeError("glite must be an object")
    glite_labels = glite["labels"]
    if not isinstance(glite_labels, dict):
        raise TypeError("glite.labels must be an object")
    glite_lexen = glite_labels["lexen_gold"]
    if not isinstance(glite_lexen, dict):
        raise TypeError("glite lexen_gold label must be an object")
    suspicion_set = review["suspicion_set"]
    metadata = {
        "dataset_canary": DATASET_CANARY,
        "label_set": "lexen_gold",
        "lexen_gold_glite_concept_ids": " ".join(
            str(concept_id) for concept_id in glite_lexen["concept_ids"]
        ),
        "lexen_gold_decision": str(lexen_gold["decision"]),
        "lexen_gold_empty": str(bool(lexen_gold["is_empty"])).lower(),
        "maru2022_sense_keys": " ".join(str(key) for key in maru2022["sense_keys"]),
        "raganato_original_sense_keys": " ".join(
            str(key) for key in raganato_original["sense_keys"]
        ),
        "release_disposition": str(review["release_disposition"]),
        "reviewed": str(bool(review["is_reviewed"])).lower(),
        "source_dataset": str(item["source_dataset"]),
        "suspicion_set": "none" if suspicion_set is None else str(suspicion_set),
    }
    return {
        "document_id": item["document_id"],
        "gold_sense_keys": lexen_gold["sense_keys"],
        "item_id": item["item_id"],
        "lemma": item["lemma"],
        "metadata": metadata,
        "pos": item["pos"],
        "sentence_id": item["sentence_id"],
        "sentence_index": len(preceding_sentences),
        "sentences": sentences,
        "target_text": item["target"]["text"],
        "target_token_index": item["target"]["token_index"],
    }


def write_gold_key(*, path: Path, items: list[JsonObject]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open(mode="w", encoding="utf-8") as handle:
        for item in items:
            keys = item["labels"]["lexen_gold"]["sense_keys"]
            if not isinstance(keys, list) or len(keys) == 0:
                raise ValueError(f"lexEN gold label is empty for {item['item_id']}")
            handle.write(f"{item['item_id']} {' '.join(str(key) for key in keys)}\n")


def write_xml_with_canary(
    *,
    source_path: Path,
    output_path: Path,
    removed_item_ids: set[str],
) -> None:
    tree = ET.parse(source_path)
    root = tree.getroot()
    removed_count = 0
    for element in root.iter("instance"):
        item_id = element.attrib.get("id")
        if item_id not in removed_item_ids:
            continue
        element.tag = "wf"
        del element.attrib["id"]
        removed_count += 1
    if removed_count != len(removed_item_ids):
        missing_count = len(removed_item_ids) - removed_count
        raise ValueError(f"Raganato XML is missing {missing_count} removed item ids")

    canary_comment = ET.Comment(f" lexEN contamination canary: {DATASET_CANARY} ")
    canary_comment.tail = root.text if root.text is not None else "\n  "
    root.insert(0, canary_comment)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    tree.write(
        output_path,
        encoding="utf-8",
        short_empty_elements=False,
        xml_declaration=True,
    )


def build_output_paths(*, output_root: Path, release_id: str) -> BuildOutputPaths:
    release_dir = output_root / DATA_DIRNAME / release_id
    raganato_dir = output_root / EXPORTS_DIRNAME / RAGANATO_EXPORT_DIRNAME / release_id
    sensebench_dir = output_root / EXPORTS_DIRNAME / SENSEBENCH_EXPORT_DIRNAME / release_id
    return BuildOutputPaths(
        canonical_items=release_dir / CANONICAL_ITEMS_FILENAME,
        dataset_metadata=release_dir / DATASET_METADATA_FILENAME,
        raganato_gold=raganato_dir / f"{release_id}{GOLD_KEY_SUFFIX}",
        raganato_xml=raganato_dir / f"{release_id}{DATA_XML_SUFFIX}",
        removed=raganato_dir / f"{release_id}{REMOVED_SUFFIX}",
        reviews=release_dir / REVIEWS_FILENAME,
        sensebench_items=sensebench_dir / CANONICAL_ITEMS_FILENAME,
    )


def source_artifacts(*, repo_root: Path) -> list[JsonObject]:
    source_paths = list((repo_root / SOURCES_DIRNAME).rglob("*"))
    return [
        record.to_json_object()
        for record in artifact_records_for_paths(paths=source_paths, relative_to=repo_root)
    ]


def report_artifacts(*, repo_root: Path) -> list[JsonObject]:
    report_paths = list((repo_root / REPORTS_DIRNAME).rglob("*"))
    return [
        record.to_json_object()
        for record in artifact_records_for_paths(paths=report_paths, relative_to=repo_root)
    ]


def output_artifacts(*, output_paths: BuildOutputPaths, output_root: Path) -> list[JsonObject]:
    paths = [
        output_paths.canonical_items,
        output_paths.reviews,
        output_paths.sensebench_items,
        output_paths.raganato_xml,
        output_paths.raganato_gold,
        output_paths.removed,
    ]
    return [
        record.to_json_object()
        for record in artifact_records_for_paths(paths=paths, relative_to=output_root)
    ]


def release_metadata(
    *,
    counts: dict[str, int],
    repo_root: Path,
    output_root: Path,
    output_paths: BuildOutputPaths,
) -> JsonObject:
    waterfall_summary = read_json_object(
        path=repo_root / SELECTION_SOURCE_DIR / WATERFALL_SUMMARY_FILENAME
    )
    return {
        "annotators_for_gold": list(CANONICAL_ANNOTATORS),
        "contamination_canary": {
            "purpose": (
                "Trace accidental benchmark ingestion and support training-data "
                "decontamination checks."
            ),
            "term": "canary string",
            "value": DATASET_CANARY,
        },
        "counts": counts,
        "created_at": "2026-06-13",
        "dataset_id": DATASET_ID,
        "description": (
            "lexEN v1 is derived from Maru 2022 ALL_NEW / ALLamended and applies "
            "same-protocol three-annotator consensus corrections and removals on the "
            "363 suspicious reviewed items."
        ),
        "label_layers": {
            "lexen_gold": "The scoring label used by lexEN exports.",
            "maru2022": "The Maru2022 ALLamended source label.",
            "raganato_original": "The original Raganato ALL label for the same instance id.",
        },
        "label_policy": {
            "lexen_gold": (
                "For reviewed items, use any non-empty sense-key set selected by at least "
                "two of RF, PW, and PH. Remove reviewed items when at least two reviewers "
                "mark cannot-answer, or when no fine-grained sense receives two-reviewer "
                "support. Unreviewed items keep Maru2022 labels."
            ),
            "removed_items": (
                "Removed reviewed items are excluded from canonical items, Raganato XML "
                "instances, Raganato gold keys, and SenseBench exports. They remain in "
                "reviews.jsonl and in the removed-items sidecar for auditability."
            ),
        },
        "license": {
            "data": "research-only non-commercial release; source packages retain their own terms",
            "lexicographer_reviews": "research-only audit evidence",
            "maru2022": "CC-BY-NC-4.0",
            "release_policy": "research-only non-commercial release",
            "software": "Apache-2.0",
        },
        "output_artifacts": output_artifacts(output_paths=output_paths, output_root=output_root),
        "release_id": ACTIVE_RELEASE_ID,
        "release_status": "benchmark_release",
        "report_artifacts": report_artifacts(repo_root=repo_root),
        "schema_version": DATASET_SCHEMA_VERSION,
        "selection_policy": {
            "generated_by": "scripts/build_selection_source.py",
            "model_panel_size": 10,
            "reviewed_items": 363,
            "source": str(SELECTION_SOURCE_DIR / SELECTION_JSONL_GZ_FILENAME),
            "summary": waterfall_summary,
        },
        "source_manifest": str(Path(SOURCES_DIRNAME) / SOURCE_MANIFEST_FILENAME),
        "source_artifacts": source_artifacts(repo_root=repo_root),
    }


def build_release(
    *,
    repo_root: Path = DEFAULT_REPO_ROOT,
    output_root: Path = DEFAULT_REPO_ROOT,
    release_id: str = ACTIVE_RELEASE_ID,
) -> BuildResult:
    if release_id != ACTIVE_RELEASE_ID:
        raise ValueError(f"only {ACTIVE_RELEASE_ID} can be rebuilt from the versioned sources")
    repo_root = repo_root.resolve()
    output_root = output_root.resolve()
    inputs = load_build_inputs(repo_root=repo_root)
    records = build_records(
        inputs=inputs,
        glite_mapping=load_glite_mapping(repo_root=repo_root),
    )
    paths = build_output_paths(output_root=output_root, release_id=release_id)

    write_jsonl_objects(path=paths.canonical_items, rows=records.items)
    write_jsonl_objects(path=paths.reviews, rows=records.reviews)
    write_jsonl_objects(
        path=paths.sensebench_items,
        rows=[sensebench_record(item=item) for item in records.items],
    )
    write_xml_with_canary(
        source_path=repo_root / MARU_SOURCE_DIR / MARU_XML_FILENAME,
        output_path=paths.raganato_xml,
        removed_item_ids={str(item["item_id"]) for item in records.removed_items},
    )
    write_gold_key(path=paths.raganato_gold, items=records.items)
    write_json_object(
        path=paths.removed,
        data={
            "dataset_canary": DATASET_CANARY,
            "items": records.removed_items,
            "release_id": release_id,
            "schema_version": REMOVED_SCHEMA_VERSION,
        },
    )
    write_json_object(
        path=paths.dataset_metadata,
        data=release_metadata(
            counts=records.counts,
            repo_root=repo_root,
            output_root=output_root,
            output_paths=paths,
        ),
    )
    return BuildResult(release_id=release_id, counts=records.counts, output_paths=paths)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--release", default=ACTIVE_RELEASE_ID, help="Release id to build.")
    parser.add_argument(
        "--repo-root",
        type=Path,
        default=DEFAULT_REPO_ROOT,
        help="Path to the lexEN repository root.",
    )
    parser.add_argument(
        "--output-root",
        type=Path,
        default=DEFAULT_REPO_ROOT,
        help="Path where release artifacts are written.",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    result = build_release(
        repo_root=args.repo_root,
        output_root=args.output_root,
        release_id=str(args.release),
    )
    print(
        json.dumps(
            {
                "counts": result.counts,
                "release_id": result.release_id,
            },
            indent=2,
            sort_keys=True,
        )
    )


if __name__ == "__main__":
    main()
