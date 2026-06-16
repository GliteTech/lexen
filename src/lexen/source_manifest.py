"""Build the machine-readable source manifest for lexEN."""

from __future__ import annotations

import argparse
import json
from dataclasses import dataclass
from pathlib import Path

from lexen.io import artifact_records_for_paths
from lexen.models import JsonObject
from lexen.paths import DEFAULT_REPO_ROOT, SOURCE_MANIFEST_FILENAME, SOURCES_DIRNAME


@dataclass(frozen=True, slots=True)
class SourcePackage:
    """Static public metadata for one source package."""

    package_id: str
    name: str
    local_path: str
    kind: str
    license_id: str
    access: str
    source_url: str | None
    citation: str | None
    generated_by: str | None = None


SOURCE_PACKAGES: tuple[SourcePackage, ...] = (
    SourcePackage(
        package_id="raganato-original-all",
        name="Raganato et al. 2017 ALL evaluation benchmark",
        local_path="sources/raganato/original",
        kind="upstream_original",
        license_id="research-benchmark",
        access="public",
        source_url="http://lcl.uniroma1.it/wsdeval/data/WSD_Evaluation_Framework.zip",
        citation="Raganato, Camacho-Collados, and Navigli (EACL 2017)",
    ),
    SourcePackage(
        package_id="maru2022-allamended",
        name="Maru et al. 2022 ALLamended",
        local_path="sources/maru2022/original",
        kind="upstream_original",
        license_id="CC-BY-NC-4.0",
        access="public",
        source_url="https://github.com/SapienzaNLP/wsd-hard-benchmark",
        citation="Maru, Conia, Bevilacqua, and Navigli (ACL 2022)",
    ),
    SourcePackage(
        package_id="maru2022-paper",
        name="Maru et al. 2022 paper",
        local_path="sources/maru2022/papers",
        kind="paper",
        license_id="CC-BY-4.0",
        access="public",
        source_url="https://aclanthology.org/2022.acl-long.324/",
        citation="Maru, Conia, Bevilacqua, and Navigli (ACL 2022)",
    ),
    SourcePackage(
        package_id="lexen-model-panel",
        name="Model-panel predictions used for suspicious-item selection",
        local_path="sources/model-panel",
        kind="model_predictions",
        license_id="research-only",
        access="included-research-use",
        source_url=None,
        citation=None,
    ),
    SourcePackage(
        package_id="lexen-selection",
        name="Generated 4,917-row suspicious-item selection package",
        local_path="sources/selection",
        kind="generated_intermediate",
        license_id="research-only",
        access="included-research-use",
        source_url=None,
        citation=None,
        generated_by="scripts/build_selection_source.py",
    ),
    SourcePackage(
        package_id="lexen-reviews",
        name="Raw lexicographer review exports and reviewer-facing brief",
        local_path="sources/reviews",
        kind="human_review",
        license_id="research-only",
        access="included-research-use",
        source_url="https://marureview.com/brief",
        citation=None,
    ),
    SourcePackage(
        package_id="glite-coarsening",
        name="Glite WordNet-to-concept coarsening subset for Maru2022",
        local_path="sources/glite-coarsening",
        kind="sense_mapping",
        license_id="research-only",
        access="included-research-use",
        source_url=None,
        citation=None,
        generated_by="scripts/build_public_glite_subset.py",
    ),
)


def files_for_package(*, repo_root: Path, package: SourcePackage) -> list[JsonObject]:
    package_root = repo_root / package.local_path
    paths = [
        path
        for path in package_root.rglob("*")
        if path.is_file() and path.name != SOURCE_MANIFEST_FILENAME
    ]
    return [
        record.to_json_object()
        for record in artifact_records_for_paths(paths=paths, relative_to=repo_root)
    ]


def build_source_manifest(*, repo_root: Path = DEFAULT_REPO_ROOT) -> JsonObject:
    packages: list[JsonObject] = []
    for package in SOURCE_PACKAGES:
        packages.append(
            {
                "access": package.access,
                "citation": package.citation,
                "files": files_for_package(repo_root=repo_root, package=package),
                "generated_by": package.generated_by,
                "kind": package.kind,
                "license": package.license_id,
                "local_path": package.local_path,
                "name": package.name,
                "package_id": package.package_id,
                "source_url": package.source_url,
            }
        )
    return {
        "description": (
            "Traceable source manifest for lexEN. Code is Apache-2.0; data packages keep "
            "their own source licenses and access restrictions."
        ),
        "manifest_schema_version": "lexen.source_manifest.v1",
        "packages": packages,
    }


def write_source_manifest(*, repo_root: Path = DEFAULT_REPO_ROOT) -> Path:
    path = repo_root / SOURCES_DIRNAME / SOURCE_MANIFEST_FILENAME
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        json.dumps(build_source_manifest(repo_root=repo_root), ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    return path


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
    path = write_source_manifest(repo_root=args.repo_root.resolve())
    print(json.dumps({"path": str(path), "status": "written"}, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
