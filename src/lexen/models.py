"""Typed models used by the lexEN release builder."""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import Any

from pydantic import BaseModel, ConfigDict, Field

type ItemID = str
type SenseKey = str
type JsonObject = dict[str, Any]


class SourceToken(BaseModel):
    """One token from the selection source package."""

    model_config = ConfigDict(frozen=True, extra="forbid")

    surface: str
    lemma: str | None = None
    pos: str
    is_target_instance: bool
    instance_id: str | None = None


class SourceSentence(BaseModel):
    """One tokenized source sentence."""

    model_config = ConfigDict(frozen=True, extra="forbid")

    tokens: list[SourceToken]


class SourceContext(BaseModel):
    """Context window shown to lexicographers."""

    model_config = ConfigDict(frozen=True, extra="forbid")

    preceding_sentences: list[SourceSentence]
    target_sentence: SourceSentence
    following_sentences: list[SourceSentence]
    target_token_index: int = Field(ge=0)


class WordNetSense(BaseModel):
    """WordNet sense metadata from the selection source package."""

    model_config = ConfigDict(frozen=True, extra="forbid")

    sense_key: SenseKey
    synset_name: str
    lemma: str
    pos: str
    definition: str
    examples: list[str]
    synonyms: list[str]
    in_maru_prompt: bool


class ModelPrediction(BaseModel):
    """Compact prediction evidence used to select suspicious items."""

    model_config = ConfigDict(frozen=True, extra="allow")

    predicted_sense_key: SenseKey | None
    is_correct: bool | None
    agrees_with_modal: bool | None
    agrees_with_gold: bool | None
    justifications: object | None = None


class SelectionRecord(BaseModel):
    """One record from the 4,917-row selection source package."""

    model_config = ConfigDict(frozen=True, extra="forbid")

    instance_id: ItemID
    lemma: str
    pos: str
    dataset: str
    context: SourceContext
    candidates_in_maru_prompt: list[SenseKey]
    all_wordnet_senses: list[WordNetSense]
    gold_sense_keys: list[SenseKey]
    gold_sense_id: SenseKey | None
    modal_predicted_sense_id: SenseKey | None
    modal_count: int
    model_predictions: dict[str, ModelPrediction]
    n_models_total: int
    n_correct: int
    n_distinct_predictions: int
    top_prediction_share: float
    suspicion_set: str | None
    suspicion_rationale: str


class ReviewVerdict(BaseModel):
    """One raw same-protocol lexicographer verdict."""

    model_config = ConfigDict(frozen=True, extra="forbid")

    instance_id: ItemID
    chosen_sense_keys: list[SenseKey] = Field(default_factory=list)
    cannot_answer: list[str] = Field(default_factory=list)
    cannot_answer_notes: str | None = None
    comment: str | None = None


class ReviewFile(BaseModel):
    """A raw review JSON file."""

    model_config = ConfigDict(frozen=True, extra="forbid")

    saved_at: str
    total_items: int
    reviewed: int
    verdicts: list[ReviewVerdict]


@dataclass(frozen=True, slots=True)
class AnnotatorRecord:
    """Normalized verdict data for one annotator."""

    chosen_sense_keys: list[SenseKey]
    cannot_answer: list[str]
    cannot_answer_notes: str | None
    comment: str | None


@dataclass(frozen=True, slots=True)
class LabelDecision:
    """Release label decision for one source item."""

    lexen_gold_keys: list[SenseKey]
    decision: str
    disposition: str
    removal_reason: str | None


@dataclass(frozen=True, slots=True)
class BuildInputs:
    """Loaded source data used by the release builder."""

    selection_records: list[SelectionRecord]
    raganato_original_by_id: dict[ItemID, list[SenseKey]]
    rf_verdicts_by_id: dict[ItemID, ReviewVerdict]
    pw_verdicts_by_id: dict[ItemID, ReviewVerdict]
    ph_verdicts_by_id: dict[ItemID, ReviewVerdict]


@dataclass(frozen=True, slots=True)
class BuiltRecords:
    """Canonical records produced before writing files."""

    items: list[JsonObject]
    removed_items: list[JsonObject]
    reviews: list[JsonObject]
    counts: dict[str, int]


@dataclass(frozen=True, slots=True)
class BuildOutputPaths:
    """Paths emitted by a release build."""

    dataset_metadata: Path
    canonical_items: Path
    reviews: Path
    sensebench_items: Path
    raganato_xml: Path
    raganato_gold: Path
    removed: Path


@dataclass(frozen=True, slots=True)
class BuildResult:
    """Summary of a completed release build."""

    release_id: str
    counts: dict[str, int]
    output_paths: BuildOutputPaths


@dataclass(frozen=True, slots=True)
class ArtifactRecord:
    """Hash metadata for one source or output artifact."""

    path: str
    sha256: str
    bytes: int

    def to_json_object(self) -> JsonObject:
        return {
            "bytes": self.bytes,
            "path": self.path,
            "sha256": self.sha256,
        }
