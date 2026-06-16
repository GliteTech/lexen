---
spec_version: "1"
dataset_id: "raganato-original-all"
source_package_described_at: "2026-06-14"
---
# Raganato 2017 Original ALL

This directory contains the original `ALL` gold key and XML corpus from the Raganato et al. unified
English WSD evaluation framework. lexEN uses this source only as a lineage layer: it records the
pre-Maru label for each retained or removed item whose instance ID also appears in Maru2022
ALLamended.

## Included Files

| File | Purpose | SHA-256 |
| --- | --- | --- |
| `files/ALL.data.xml` | Original Raganato ALL XML corpus in standard WSD format. | `sha256:27a9da01b6d4a1e4dc7c76d15148a38eaa56cc0df371cae4416d04e541b6fe36` |
| `files/ALL.gold.key.txt` | Original Raganato ALL WordNet 3.0 gold key. | `sha256:0bf2ffc38f572587c72b59ea928da676423b99b5a54bd1a83eb4848b517d3170` |

## Provenance

The source distribution is the WSD Evaluation Framework ZIP published by the Linguistic Computing
Laboratory at Sapienza University of Rome:

`http://lcl.uniroma1.it/wsdeval/data/WSD_Evaluation_Framework.zip`

The public fetch script extracts `Evaluation_Datasets/ALL/ALL.data.xml` and
`Evaluation_Datasets/ALL/ALL.gold.key.txt` from that ZIP.

## Use In lexEN

Raganato `ALL` contains 7,253 instance IDs. Maru2022 ALLamended keeps 4,917 of those IDs after
excluding SemEval-2007 and applying Maru et al.'s corrections/removals. The lexEN release builder
extracts the original Raganato label for the 4,917 Maru2022 IDs and stores it alongside the Maru2022
and lexEN labels.
