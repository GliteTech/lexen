"""Repository paths and release constants."""

from __future__ import annotations

from pathlib import Path

PACKAGE_DIR: Path = Path(__file__).resolve().parent
DEFAULT_REPO_ROOT: Path = PACKAGE_DIR.parents[1]

DATASET_ID: str = "lexen"
ACTIVE_RELEASE_ID: str = "lexen-v1"
SUPPORTED_RELEASE_IDS: set[str] = {ACTIVE_RELEASE_ID}

ITEM_SCHEMA_VERSION: str = "lexen.item.v2"
REVIEW_SCHEMA_VERSION: str = "lexen.review.v2"
DATASET_SCHEMA_VERSION: str = "lexen.dataset.v2"
REMOVED_SCHEMA_VERSION: str = "lexen.removed.v2"
DATASET_CANARY: str = "lexen-canary-v1-U4f9Yzq6Rk2nQ8wL7cP3tB5aHxM1sD0e"

DATA_DIRNAME: str = "data"
EXPORTS_DIRNAME: str = "exports"
RAGANATO_EXPORT_DIRNAME: str = "raganato"
SENSEBENCH_EXPORT_DIRNAME: str = "sensebench"
SOURCES_DIRNAME: str = "sources"
REPORTS_DIRNAME: str = "reports"

RAGANATO_SOURCE_DIR: Path = Path(SOURCES_DIRNAME) / "raganato" / "original" / "files"
MARU_SOURCE_DIR: Path = Path(SOURCES_DIRNAME) / "maru2022" / "original" / "files"
SELECTION_SOURCE_DIR: Path = Path(SOURCES_DIRNAME) / "selection"
MODEL_PANEL_SOURCE_DIR: Path = Path(SOURCES_DIRNAME) / "model-panel" / "predictions"
GLITE_COARSENING_DIR: Path = Path(SOURCES_DIRNAME) / "glite-coarsening"
GLITE_COARSENING_FILES_DIR: Path = GLITE_COARSENING_DIR / "files"
RF_REVIEW_SOURCE_DIR: Path = Path(SOURCES_DIRNAME) / "reviews" / "rf-2026-05-26"
PW_REVIEW_SOURCE_DIR: Path = Path(SOURCES_DIRNAME) / "reviews" / "pw-2026-05-29"
PH_REVIEW_SOURCE_DIR: Path = Path(SOURCES_DIRNAME) / "reviews" / "ph-2026-06-13"

RAGANATO_XML_FILENAME: str = "ALL.data.xml"
RAGANATO_GOLD_FILENAME: str = "ALL.gold.key.txt"
MARU_XML_FILENAME: str = "ALLamended.data.xml"
MARU_GOLD_FILENAME: str = "ALLamended.gold.key.txt"
SELECTION_JSONL_GZ_FILENAME: str = "lexicographer_review.jsonl.gz"
SELECTION_SCHEMA_FILENAME: str = "schema.json"
WATERFALL_SUMMARY_FILENAME: str = "waterfall_summary.json"
SOURCE_MANIFEST_FILENAME: str = "manifest.json"
GLITE_SENSE_TO_CONCEPT_FILENAME: str = "wordnet_sense_key_to_glite_concept.jsonl"
GLITE_MAPPING_COVERAGE_FILENAME: str = "mapping_coverage.json"
GLITE_REPORT_ALIASES_FILENAME: str = "lexen_report_aliases.json"
RF_VERDICTS_FILENAME: str = "maru2022-wsd-verdicts-2026-05-26.json"
PW_VERDICTS_FILENAME: str = "maru2022-wsd-verdicts-2026-05-29.json"
PH_VERDICTS_FILENAME: str = "maru2022-wsd-verdicts-2026-06-13.json"
REVIEWER_BRIEF_FILENAME: str = "reviewer_brief.md"

DATASET_METADATA_FILENAME: str = "dataset.json"
CANONICAL_ITEMS_FILENAME: str = "items.jsonl"
REVIEWS_FILENAME: str = "reviews.jsonl"
REMOVED_SUFFIX: str = ".removed.json"
DATA_XML_SUFFIX: str = ".data.xml"
GOLD_KEY_SUFFIX: str = ".gold.key.txt"

XML_DECLARATION_PREFIX_BYTES: bytes = b"<?xml"
XML_LINE_SEPARATOR_BYTES: bytes = b"\n"
XML_CANARY_PREFIX: str = "<!-- lexEN contamination canary: "
XML_CANARY_SUFFIX: str = " -->"

RF_ANNOTATOR_ID: str = "RF"
PW_ANNOTATOR_ID: str = "PW"
PH_ANNOTATOR_ID: str = "PH"
CANONICAL_ANNOTATORS: tuple[str, str, str] = (
    RF_ANNOTATOR_ID,
    PW_ANNOTATOR_ID,
    PH_ANNOTATOR_ID,
)

EXPECTED_SOURCE_ITEMS: int = 4917
EXPECTED_TOTAL_ITEMS: int = 4861
EXPECTED_REVIEWED_AUDIT_ITEMS: int = 363
EXPECTED_REVIEWED_ITEMS: int = 307
EXPECTED_UNREVIEWED_ITEMS: int = 4554
EXPECTED_THREE_WAY_EXACT_AGREEMENT: int = 124
EXPECTED_TWO_OF_THREE_SENSE_AGREEMENT: int = 183
EXPECTED_REMOVED_ITEMS: int = 56
EXPECTED_REMOVED_TWO_OF_THREE_CANNOT_ANSWER: int = 27
EXPECTED_REMOVED_THREE_WAY_NO_CONSENSUS: int = 29
EXPECTED_LEXEN_GOLD_CHANGED_FROM_MARU: int = 211

DECISION_UNREVIEWED: str = "unreviewed_kept_maru"
DECISION_THREE_WAY_EXACT: str = "three_way_exact_agreement"
DECISION_TWO_OF_THREE_SENSE: str = "two_of_three_sense_agreement"
DECISION_TWO_OF_THREE_CANNOT_ANSWER: str = "two_of_three_cannot_answer_removed"
DECISION_THREE_WAY_NO_CONSENSUS: str = "three_way_no_consensus_removed"

DISPOSITION_RETAINED: str = "retained"
DISPOSITION_REMOVED: str = "removed"

SHA256_PREFIX: str = "sha256:"
HASH_CHUNK_SIZE_BYTES: int = 1024 * 1024
