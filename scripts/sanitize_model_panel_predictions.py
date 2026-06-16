"""Remove transport and telemetry fields from model-panel prediction artifacts."""

from __future__ import annotations

import argparse
import gzip
import json
from pathlib import Path

from lexen.paths import DEFAULT_REPO_ROOT, MODEL_PANEL_SOURCE_DIR
from lexen.selection import GPT55_MODEL_LABELS

PRIVATE_OR_NOISY_FIELDS: frozenset[str] = frozenset(
    {
        "cost_usd",
        "dataset_id",
        "dataset_split",
        "failed_asset_fallbacks",
        "footer_applied",
        "header_applied",
        "http_status",
        "input_tokens",
        "is_correct_glite_coarsened",
        "latency_seconds",
        "output_tokens",
        "prompt_hash",
        "provider_request_id",
        "reasoning_tokens",
        "retry_after",
        "retry_count",
        "retry_reasons",
        "run_id",
        "variant_id",
    }
)


def sanitized_row(*, row: dict[str, object]) -> dict[str, object]:
    return {key: value for key, value in row.items() if key not in PRIVATE_OR_NOISY_FIELDS}


def read_jsonl_gz(*, path: Path) -> list[dict[str, object]]:
    rows: list[dict[str, object]] = []
    with gzip.open(path, mode="rt", encoding="utf-8") as handle:
        for raw_line in handle:
            row = json.loads(raw_line)
            if not isinstance(row, dict):
                raise TypeError(f"expected JSON object row in {path}")
            rows.append(sanitized_row(row=row))
    return rows


def write_jsonl_gz(*, path: Path, rows: list[dict[str, object]]) -> None:
    with (
        path.open("wb") as raw_handle,
        gzip.GzipFile(
            fileobj=raw_handle,
            mode="wb",
            mtime=0,
        ) as gzip_handle,
    ):
        for row in rows:
            line = json.dumps(row, ensure_ascii=False, sort_keys=True) + "\n"
            gzip_handle.write(line.encode("utf-8"))


def sanitize_model_panel_predictions(*, repo_root: Path = DEFAULT_REPO_ROOT) -> dict[str, int]:
    prediction_root = repo_root / MODEL_PANEL_SOURCE_DIR
    rewritten: dict[str, int] = {}
    for model_label in GPT55_MODEL_LABELS:
        path = prediction_root / model_label / "predictions.jsonl.gz"
        rows = read_jsonl_gz(path=path)
        write_jsonl_gz(path=path, rows=rows)
        rewritten[model_label] = len(rows)
    return rewritten


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--repo-root",
        type=Path,
        default=DEFAULT_REPO_ROOT,
        help="Path to the lexEN repository root.",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    report = sanitize_model_panel_predictions(repo_root=args.repo_root.resolve())
    print(json.dumps(report, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
