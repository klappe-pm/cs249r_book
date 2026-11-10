---
title: FPGA Based ML Acceleration
type: concept
tags:
- Type/Concept
- Group/Stack
- Topic/Accelerator_Architecture
source_repository: https://github.com/klappe-pm/cs249r_book
source_commit: de87c0103806d7bfb1c677dbb77a2b92fa00c298
source_path: taxonomy/taxonomy.yml
source_label: FPGA-based ML acceleration
taxonomy_id: mlsys.fpga-acceleration
taxonomy_status: draft
taxonomy_version: 0.4-draft
---

# FPGA Based ML Acceleration

Mapping ML operations to reconfigurable logic, arithmetic blocks, and local memories so datapaths can match a workload at the cost of hardware compilation and resource constraints.

## Browsing Home

[[02 Concepts/Stack/Hardware & Accelerators/Accelerator Architecture Subject|Accelerator Architecture]] → [[02 Concepts/Stack/Hardware & Accelerators/Hardware & Accelerators Index|Hardware & Accelerators]]

## Book Passages

These are explicitly recorded related passages from the upstream draft alignment; they do not certify complete coverage.

No explicit passage alignment is recorded for this concept. Subject reading pointers are available in its browsing home.

## Conditional Relationships

These are the taxonomy's draft editorial relationships. Read each relationship with its condition; an outgoing link is not a prerequisite claim.

- Implements workload-specialized hardware [[02 Concepts/Stack/Hardware & Accelerators/Domain Specific Architecture|Domain Specific Architecture]]. **Condition:** When the configured fabric realizes an ML accelerator datapath.

- Uses explicit operand placement and streaming schedules [[02 Concepts/Stack/Hardware & Accelerators/Accelerator Dataflow|Accelerator Dataflow]]. **Condition:** When operators are mapped onto configured arithmetic and memory resources.

## Search Terms

Upstream search terms may be related terms rather than exact synonyms: FPGA inference; reconfigurable ML acceleration.

## Source

[Canonical Taxonomy](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/taxonomy.yml) · [Passage Alignment](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/mlsysbook-alignment.yml)

Taxonomy definitions and relationship wording: CC BY 4.0, with attribution to the Machine Learning Systems curriculum by Vijay Janapa Reddi and contributors. The textbook retains its separate license.
