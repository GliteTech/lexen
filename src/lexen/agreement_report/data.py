"""Load report inputs from release artifacts."""

from __future__ import annotations

import json
from pathlib import Path

from pydantic import BaseModel, ConfigDict, TypeAdapter

from lexen.agreement_report.paths import (
    ACTIVE_ITEMS_PATH,
    ACTIVE_REVIEWS_PATH,
    GLITE_COARSENING_FILES_DIR,
    GLITE_REPORT_ALIASES_FILENAME,
    GLITE_SENSE_TO_CONCEPT_FILENAME,
)
from lexen.io import read_gzip_jsonl_text, read_jsonl_objects
from lexen.models import JsonObject, SelectionRecord, SenseKey, SourceSentence
from lexen.paths import SELECTION_JSONL_GZ_FILENAME, SELECTION_SOURCE_DIR


class GliteAliasRecord(BaseModel):
    model_config = ConfigDict(frozen=True, extra="forbid")

    source_sense_key: SenseKey
    target_sense_key: SenseKey
    concept_id: str
    reason: str


class GliteAliasFile(BaseModel):
    model_config = ConfigDict(frozen=True, extra="forbid")

    spec_version: str
    aliases: list[GliteAliasRecord]


_GLITE_ALIAS_ADAPTER: TypeAdapter[GliteAliasFile] = TypeAdapter(GliteAliasFile)
_SELECTION_RECORD_ADAPTER: TypeAdapter[SelectionRecord] = TypeAdapter(SelectionRecord)


def require_object(*, value: object, field_name: str) -> JsonObject:
    if not isinstance(value, dict):
        raise TypeError(f"{field_name} must be an object")
    return value


def require_list(*, value: object, field_name: str) -> list[object]:
    if not isinstance(value, list):
        raise TypeError(f"{field_name} must be a list")
    return value


def require_string(*, value: object, field_name: str) -> str:
    if not isinstance(value, str):
        raise TypeError(f"{field_name} must be a string")
    return value


def optional_string(*, value: object, field_name: str) -> str | None:
    if value is None:
        return None
    if not isinstance(value, str):
        raise TypeError(f"{field_name} must be a string or null")
    return value


def require_string_list(*, value: object, field_name: str) -> list[str]:
    return [
        require_string(value=item, field_name=f"{field_name}[]")
        for item in require_list(value=value, field_name=field_name)
    ]


def load_items(*, repo_root: Path) -> list[JsonObject]:
    return read_jsonl_objects(path=repo_root / ACTIVE_ITEMS_PATH)


def load_reviews(*, repo_root: Path) -> list[JsonObject]:
    return read_jsonl_objects(path=repo_root / ACTIVE_REVIEWS_PATH)


def load_selection_records(*, repo_root: Path) -> list[SelectionRecord]:
    path = repo_root / SELECTION_SOURCE_DIR / SELECTION_JSONL_GZ_FILENAME
    return [
        _SELECTION_RECORD_ADAPTER.validate_json(line) for line in read_gzip_jsonl_text(path=path)
    ]


def sentence_words(*, sentence: SourceSentence) -> list[str]:
    return [str(token.surface) for token in sentence.tokens]


def sentence_id_from_item_id(*, value: str) -> str:
    return ".".join(value.split(".")[:-1])


def document_id_from_item_id(*, value: str) -> str:
    return ".".join(value.split(".")[:-2])


def report_items_from_selection_records(
    *,
    selection_records: list[SelectionRecord],
    reviews: list[JsonObject],
) -> list[JsonObject]:
    reviewed_ids = {
        require_string(value=review["item_id"], field_name="review.item_id") for review in reviews
    }
    output: list[JsonObject] = []
    for record in selection_records:
        if record.instance_id not in reviewed_ids:
            continue
        target_token_index = record.context.target_token_index
        target_tokens = record.context.target_sentence.tokens
        if target_token_index >= len(target_tokens):
            raise ValueError(f"target_token_index outside target sentence for {record.instance_id}")
        target_token = target_tokens[target_token_index]
        output.append(
            {
                "context": {
                    "following_sentences": [
                        sentence_words(sentence=sentence)
                        for sentence in record.context.following_sentences
                    ],
                    "preceding_sentences": [
                        sentence_words(sentence=sentence)
                        for sentence in record.context.preceding_sentences
                    ],
                    "target_sentence": sentence_words(sentence=record.context.target_sentence),
                },
                "document_id": document_id_from_item_id(value=record.instance_id),
                "item_id": record.instance_id,
                "labels": {
                    "maru2022": {
                        "sense_keys": sorted(set(record.gold_sense_keys)),
                    },
                },
                "lemma": record.lemma,
                "pos": record.pos,
                "sentence_id": sentence_id_from_item_id(value=record.instance_id),
                "source_dataset": record.dataset,
                "target": {
                    "text": target_token.surface,
                    "token_index": target_token_index,
                },
            }
        )
    if len(output) != len(reviewed_ids):
        available_ids = {str(item["item_id"]) for item in output}
        missing = sorted(reviewed_ids - available_ids)
        raise ValueError(f"selection source missing reviewed item ids: {missing[:5]}")
    return output


def target_sentence_tokens(*, item: JsonObject) -> list[str]:
    context = require_object(value=item["context"], field_name="item.context")
    return require_string_list(
        value=context["target_sentence"],
        field_name="item.context.target_sentence",
    )


def target_token_index(*, item: JsonObject) -> int:
    target = require_object(value=item["target"], field_name="item.target")
    token_index = target["token_index"]
    if not isinstance(token_index, int):
        raise TypeError("item.target.token_index must be an integer")
    return token_index


def reviews_by_id(*, reviews: list[JsonObject]) -> dict[str, JsonObject]:
    indexed: dict[str, JsonObject] = {}
    for review in reviews:
        item_id = require_string(value=review["item_id"], field_name="review.item_id")
        if item_id in indexed:
            raise ValueError(f"duplicate review item_id {item_id}")
        indexed[item_id] = review
    return indexed


def reviewed_items(*, items: list[JsonObject]) -> list[JsonObject]:
    output: list[JsonObject] = []
    for item in items:
        review = require_object(value=item["review"], field_name="item.review")
        if bool(review["is_reviewed"]):
            output.append(item)
    return output


def item_id(*, item: JsonObject) -> str:
    return require_string(value=item["item_id"], field_name="item.item_id")


def item_labels(*, item: JsonObject) -> JsonObject:
    return require_object(value=item["labels"], field_name="item.labels")


def maru_sense_keys(*, item: JsonObject) -> list[SenseKey]:
    labels = item_labels(item=item)
    maru = require_object(value=labels["maru2022"], field_name="item.labels.maru2022")
    return require_string_list(
        value=maru["sense_keys"],
        field_name="item.labels.maru2022.sense_keys",
    )


def review_annotator_record(
    *,
    review: JsonObject,
    reviewer: str,
) -> JsonObject:
    annotators = require_object(value=review["annotators"], field_name="review.annotators")
    return require_object(value=annotators[reviewer], field_name=f"review.annotators.{reviewer}")


def chosen_sense_keys(
    *,
    review: JsonObject,
    reviewer: str,
) -> list[SenseKey]:
    record = review_annotator_record(review=review, reviewer=reviewer)
    return require_string_list(
        value=record["chosen_sense_keys"],
        field_name=f"review.annotators.{reviewer}.chosen_sense_keys",
    )


def cannot_answer_reasons(
    *,
    review: JsonObject,
    reviewer: str,
) -> list[str]:
    record = review_annotator_record(review=review, reviewer=reviewer)
    return require_string_list(
        value=record["cannot_answer"],
        field_name=f"review.annotators.{reviewer}.cannot_answer",
    )


def review_comment(
    *,
    review: JsonObject,
    reviewer: str,
) -> str | None:
    record = review_annotator_record(review=review, reviewer=reviewer)
    return optional_string(value=record["comment"], field_name=f"{reviewer}.comment")


def review_note(
    *,
    review: JsonObject,
    reviewer: str,
) -> str | None:
    record = review_annotator_record(review=review, reviewer=reviewer)
    return optional_string(
        value=record["cannot_answer_notes"],
        field_name=f"{reviewer}.cannot_answer_notes",
    )


def context_sentence_text(*, item: JsonObject) -> str:
    return detokenize(tokens=target_sentence_tokens(item=item))


def detokenize(*, tokens: list[str]) -> str:
    no_space_before: set[str] = {
        ".",
        ",",
        ":",
        ";",
        "?",
        "!",
        "%",
        "''",
        "'s",
        ")",
        "]",
        "}",
    }
    no_space_after: set[str] = {
        "``",
        "(",
        "[",
        "{",
        "$",
    }
    parts: list[str] = []
    previous: str | None = None
    for token in tokens:
        if len(parts) == 0 or token in no_space_before or previous in no_space_after:
            parts.append(token)
        else:
            parts.append(f" {token}")
        previous = token
    return "".join(parts).replace(" `` ", ' "').replace(" ''", '"')


def collect_required_sense_keys(
    *,
    items: list[JsonObject],
    reviews: list[JsonObject],
    reviewers: list[str],
) -> set[SenseKey]:
    required: set[SenseKey] = set()
    for item in items:
        required.update(maru_sense_keys(item=item))
    for review in reviews:
        for reviewer in reviewers:
            required.update(chosen_sense_keys(review=review, reviewer=reviewer))
    return required


def load_glite_mapping(
    *,
    repo_root: Path,
    required_sense_keys: set[SenseKey],
) -> dict[SenseKey, str]:
    path = repo_root / GLITE_COARSENING_FILES_DIR / GLITE_SENSE_TO_CONCEPT_FILENAME
    mapping: dict[SenseKey, str] = {}
    with path.open(encoding="utf-8") as handle:
        for raw_line in handle:
            row = json.loads(raw_line)
            if not isinstance(row, dict):
                raise TypeError("Glite mapping rows must be objects")
            sense_key = require_string(value=row["sense_key"], field_name="sense_key")
            if sense_key not in required_sense_keys:
                continue
            concept_id = require_string(value=row["concept_id"], field_name="concept_id")
            mapping[sense_key] = concept_id
            if len(mapping) == len(required_sense_keys):
                break
    alias_path = repo_root / GLITE_COARSENING_FILES_DIR / GLITE_REPORT_ALIASES_FILENAME
    if alias_path.exists():
        alias_file = _GLITE_ALIAS_ADAPTER.validate_json(alias_path.read_bytes())
        for alias in alias_file.aliases:
            if alias.source_sense_key not in required_sense_keys:
                continue
            target_concept_id = mapping.get(alias.target_sense_key)
            if target_concept_id is not None and target_concept_id != alias.concept_id:
                raise ValueError(
                    "Glite alias concept differs from canonical target mapping: "
                    f"{alias.source_sense_key}"
                )
            mapping[alias.source_sense_key] = alias.concept_id
    return mapping
