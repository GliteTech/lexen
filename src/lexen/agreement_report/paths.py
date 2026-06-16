"""Paths for the three-reviewer agreement report."""

from __future__ import annotations

from pathlib import Path

from lexen.paths import (
    ACTIVE_RELEASE_ID,
    CANONICAL_ITEMS_FILENAME,
    DATA_DIRNAME,
    DEFAULT_REPO_ROOT,
    REPORTS_DIRNAME,
    REVIEWS_FILENAME,
    SOURCES_DIRNAME,
)

REPORT_ID: str = "rf-pw-ph-2026-06-13"
REPORT_VERSION: str = "2026-06-13"
REPORT_TITLE: str = "lexEN v1 Three-Reviewer Agreement Report"
REPORT_DIR: Path = Path(REPORTS_DIRNAME) / REPORT_ID
REPORT_SCRIPTS_DIR: Path = REPORT_DIR / "scripts"
REPORT_IMAGES_DIR: Path = REPORT_DIR / "images"

REPORT_HTML_FILENAME: str = "lexicographer_agreement_2026_06_13.html"
REPORT_PDF_FILENAME: str = "lexicographer_agreement_2026_06_13.pdf"
REPORT_MARKDOWN_FILENAME: str = "lexicographer_agreement_2026_06_13.md"
REPORT_METRICS_FILENAME: str = "metrics.json"
REPORT_PER_ITEM_FILENAME: str = "per_item_agreement.jsonl"

GLITE_COARSENING_DIR: Path = Path(SOURCES_DIRNAME) / "glite-coarsening"
GLITE_COARSENING_FILES_DIR: Path = GLITE_COARSENING_DIR / "files"
GLITE_SENSE_TO_CONCEPT_FILENAME: str = "wordnet_sense_key_to_glite_concept.jsonl"
GLITE_MAPPING_COVERAGE_FILENAME: str = "mapping_coverage.json"
GLITE_REPORT_ALIASES_FILENAME: str = "lexen_report_aliases.json"

ACTIVE_ITEMS_PATH: Path = Path(DATA_DIRNAME) / ACTIVE_RELEASE_ID / CANONICAL_ITEMS_FILENAME
ACTIVE_REVIEWS_PATH: Path = Path(DATA_DIRNAME) / ACTIVE_RELEASE_ID / REVIEWS_FILENAME

CHART_AGREEMENT_LEVELS_FILENAME: str = "agreement_levels.png"
CHART_GOLD_SUPPORT_FILENAME: str = "gold_support.png"
CHART_PAIRWISE_FILENAME: str = "pairwise_coefficients.png"
CHART_VERDICT_SHAPE_FILENAME: str = "verdict_shape.png"
CHART_CANNOT_ANSWER_FILENAME: str = "cannot_answer_reasons.png"
CHART_POS_SOURCE_FILENAME: str = "pos_source_agreement.png"

DEFAULT_REPORT_ROOT: Path = DEFAULT_REPO_ROOT / REPORT_DIR
