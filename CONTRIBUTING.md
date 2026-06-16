# Contributing

lexEN is a benchmark release, so contributions should preserve reproducibility and auditability.

## Reporting Label Issues

Open an issue for suspected label problems. Include:

* `item_id`;
* the current `labels.lexen_gold.sense_keys` value;
* the proposed sense key or removal decision;
* supporting evidence from WordNet 3.0, the item context, and any reviewer evidence if applicable.

Label changes require a documented policy decision and a new release. They should not be made as
silent edits to existing release artifacts.

## Documentation And Tooling Changes

Documentation fixes, verifier improvements, and packaging fixes are welcome when they do not change
the released benchmark semantics. Keep changes narrowly scoped and include tests for code paths that
affect release artifacts.

Do not add private dictionaries, credentials, transport telemetry, or non-public source files to the
repository. New source artifacts should be accompanied by source metadata and hashes.

## Development Setup

Install dependencies with `uv`, then run:

```bash
uv run ruff check .
uv run ruff format --check .
uv run mypy src scripts tests
uv run pytest
uv run python scripts/build_selection_source.py --verify
uv run python scripts/build_source_manifest.py
uv run python scripts/build_release.py --release lexen-v1
uv run python scripts/verify_release.py --release lexen-v1
uv run flowmark --check README.md docs/ DATASHEET.md CHANGELOG.md CONTRIBUTING.md CODE_OF_CONDUCT.md SECURITY.md
```

If a change rebuilds release artifacts, commit the generated artifacts together with the source or
script change that produced them.

## Pull Request Checklist

Before opening a pull request:

* run the checks above;
* confirm `git diff --check` is clean;
* explain whether the change affects release artifacts, documentation only, or tooling only;
* link any issue that motivates a label-policy or dataset-content change.
