"""File IO helpers for lexEN build and verification."""

from __future__ import annotations

import gzip
import hashlib
import json
from collections.abc import Iterable
from pathlib import Path

from lexen.models import ArtifactRecord, JsonObject
from lexen.paths import HASH_CHUNK_SIZE_BYTES, SHA256_PREFIX


def sha256_file(*, path: Path) -> str:
    digest = hashlib.sha256()
    with path.open(mode="rb") as handle:
        while True:
            chunk = handle.read(HASH_CHUNK_SIZE_BYTES)
            if len(chunk) == 0:
                break
            digest.update(chunk)
    return f"{SHA256_PREFIX}{digest.hexdigest()}"


def read_json_object(*, path: Path) -> JsonObject:
    with path.open(encoding="utf-8") as handle:
        data = json.load(handle)
    if not isinstance(data, dict):
        raise TypeError(f"expected JSON object in {path}")
    return data


def read_jsonl_objects(*, path: Path) -> list[JsonObject]:
    rows: list[JsonObject] = []
    with path.open(encoding="utf-8") as handle:
        for line_number, raw_line in enumerate(handle, start=1):
            line = raw_line.strip()
            if len(line) == 0:
                continue
            row = json.loads(line)
            if not isinstance(row, dict):
                raise TypeError(f"expected JSON object at {path}:{line_number}")
            rows.append(row)
    return rows


def read_gzip_jsonl_text(*, path: Path) -> list[str]:
    rows: list[str] = []
    with gzip.open(path, mode="rt", encoding="utf-8") as handle:
        for raw_line in handle:
            line = raw_line.strip()
            if len(line) > 0:
                rows.append(line)
    return rows


def write_json_object(*, path: Path, data: JsonObject) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        json.dumps(data, ensure_ascii=False, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )


def write_jsonl_objects(*, path: Path, rows: Iterable[JsonObject]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open(mode="w", encoding="utf-8") as handle:
        for row in rows:
            handle.write(json.dumps(row, ensure_ascii=False, sort_keys=True) + "\n")


def artifact_record(*, path: Path, relative_to: Path) -> ArtifactRecord:
    return ArtifactRecord(
        path=str(path.relative_to(relative_to)),
        sha256=sha256_file(path=path),
        bytes=path.stat().st_size,
    )


def artifact_records_for_paths(
    *,
    paths: Iterable[Path],
    relative_to: Path,
) -> list[ArtifactRecord]:
    return [
        artifact_record(path=path, relative_to=relative_to)
        for path in sorted(paths)
        if path.is_file()
    ]
