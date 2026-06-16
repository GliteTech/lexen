# Agreement Report

The agreement report package is `reports/rf-pw-ph-2026-06-13/`.

## Report Files

* `lexicographer_agreement_2026_06_13.html` - full standalone HTML report with charts, tables, and
  per-item appendix.
* `lexicographer_agreement_2026_06_13.pdf` - full paginated PDF report.
* `lexicographer_agreement_2026_06_13.md` - Markdown companion with the headline tables.
* `metrics.json` - machine-readable fine and Glite-coarse agreement metrics.
* `per_item_agreement.jsonl` - per-reviewed-item fine and Glite agreement rows.
* `images/*.png` - chart assets rendered by the report scripts.
* `scripts/` - reproducible report builder plus one script per chart.

The report consistently refers to the source labels as **Maru2022 labels**, not authoritative
labels. The review evidence shows many are wrong, so the report treats them as the source annotation
under audit.

The report covers all 363 reviewed suspicious items, including reviewed items removed from the
benchmark. It includes a dedicated analysis of the 29 items where no fine-grained sense received
two-reviewer support.

## Regenerating The Report

Run:

```bash
uv run python scripts/build_agreement_report.py
```

or:

```bash
uv run lexen-build-agreement-report
```

Individual charts can be regenerated with the scripts in `reports/rf-pw-ph-2026-06-13/scripts/`, for
example:

```bash
uv run python reports/rf-pw-ph-2026-06-13/scripts/chart_pairwise_coefficients.py
```

The Glite-coarse metrics use
`sources/glite-coarsening/files/wordnet_sense_key_to_glite_concept.jsonl` plus the small, auditable
`lexen_report_aliases.json` table for five legacy/British WordNet sense keys present in these review
items.

## Purpose

The report is not required to score the benchmark, but it is part of the audit trail. It documents
how consistent the three professional lexicographers were and explains the label/removal policy used
for `lexen-v1`.

`data/lexen-v1/dataset.json` records checksums for every report artifact. The verifier checks those
checksums so the published report package can be reproduced exactly.

## Relationship To The Builder

The release builder calculates labels and removals from the RF/PW/PH raw JSON verdicts. The report
package is included for transparency, citation, and independent inspection.
