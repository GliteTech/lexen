"""Fetch upstream Raganato and Maru2022 source files used by lexEN."""

from __future__ import annotations

import argparse
import json
import zipfile
from pathlib import Path
from urllib.request import urlopen

from lexen.io import sha256_file
from lexen.paths import (
    DEFAULT_REPO_ROOT,
    MARU_GOLD_FILENAME,
    MARU_SOURCE_DIR,
    MARU_XML_FILENAME,
    RAGANATO_GOLD_FILENAME,
    RAGANATO_SOURCE_DIR,
    RAGANATO_XML_FILENAME,
)

UPSTREAM_FILES: tuple[tuple[str, Path], ...] = (
    (
        "http://lcl.uniroma1.it/wsdeval/data/WSD_Evaluation_Framework.zip",
        Path("sources/raganato/original/upstream/WSD_Evaluation_Framework.zip"),
    ),
    (
        "https://raw.githubusercontent.com/SapienzaNLP/wsd-hard-benchmark/main/wsd_hard_benchmark/ALLamended/ALLamended.data.xml",
        MARU_SOURCE_DIR / MARU_XML_FILENAME,
    ),
    (
        "https://raw.githubusercontent.com/SapienzaNLP/wsd-hard-benchmark/main/wsd_hard_benchmark/ALLamended/ALLamended.gold.key.txt",
        MARU_SOURCE_DIR / MARU_GOLD_FILENAME,
    ),
)
RAGANATO_ZIP_RELATIVE_PATH: Path = Path(
    "sources/raganato/original/upstream/WSD_Evaluation_Framework.zip"
)
RAGANATO_ZIP_XML_MEMBER: str = "WSD_Evaluation_Framework/Evaluation_Datasets/ALL/ALL.data.xml"
RAGANATO_ZIP_GOLD_MEMBER: str = "WSD_Evaluation_Framework/Evaluation_Datasets/ALL/ALL.gold.key.txt"


def download_file(*, url: str, destination: Path, overwrite: bool) -> None:
    destination.parent.mkdir(parents=True, exist_ok=True)
    if destination.exists() and not overwrite:
        return
    with urlopen(url) as response:
        data = response.read()
    destination.write_bytes(data)


def fetch_upstream_sources(*, repo_root: Path, overwrite: bool) -> dict[str, str]:
    for url, relative_path in UPSTREAM_FILES:
        download_file(url=url, destination=repo_root / relative_path, overwrite=overwrite)
    zip_path = repo_root / RAGANATO_ZIP_RELATIVE_PATH
    with zipfile.ZipFile(zip_path) as archive:
        raganato_xml_path = repo_root / RAGANATO_SOURCE_DIR / RAGANATO_XML_FILENAME
        raganato_gold_path = repo_root / RAGANATO_SOURCE_DIR / RAGANATO_GOLD_FILENAME
        if overwrite or not raganato_xml_path.exists():
            raganato_xml_path.parent.mkdir(parents=True, exist_ok=True)
            raganato_xml_path.write_bytes(archive.read(RAGANATO_ZIP_XML_MEMBER))
        if overwrite or not raganato_gold_path.exists():
            raganato_gold_path.parent.mkdir(parents=True, exist_ok=True)
            raganato_gold_path.write_bytes(archive.read(RAGANATO_ZIP_GOLD_MEMBER))
    return {
        str(path.relative_to(repo_root)): sha256_file(path=path)
        for path in [
            repo_root / RAGANATO_SOURCE_DIR / RAGANATO_XML_FILENAME,
            repo_root / RAGANATO_SOURCE_DIR / RAGANATO_GOLD_FILENAME,
            repo_root / MARU_SOURCE_DIR / MARU_XML_FILENAME,
            repo_root / MARU_SOURCE_DIR / MARU_GOLD_FILENAME,
        ]
        if path.exists()
    }


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--repo-root",
        type=Path,
        default=DEFAULT_REPO_ROOT,
        help="Path to the lexEN repository root.",
    )
    parser.add_argument(
        "--overwrite",
        action="store_true",
        help="Overwrite existing upstream source files.",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    hashes = fetch_upstream_sources(
        repo_root=args.repo_root.resolve(),
        overwrite=bool(args.overwrite),
    )
    print(json.dumps({"hashes": hashes, "status": "ok"}, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
