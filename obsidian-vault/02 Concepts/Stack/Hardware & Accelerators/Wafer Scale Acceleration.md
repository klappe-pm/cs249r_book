---
title: Wafer Scale Acceleration
type: concept
tags:
- Type/Concept
- Group/Stack
- Topic/Accelerator_Architecture
source_repository: https://github.com/klappe-pm/cs249r_book
source_commit: de87c0103806d7bfb1c677dbb77a2b92fa00c298
source_path: taxonomy/taxonomy.yml
source_label: Wafer-scale acceleration
taxonomy_id: mlsys.wafer-scale-acceleration
taxonomy_status: draft
taxonomy_version: 0.4-draft
---

# Wafer Scale Acceleration

Executing ML on a compute-and-memory array spanning most of a semiconductor wafer, making spatial placement and communication between tiles central to performance.

## Browsing Home

[[02 Concepts/Stack/Hardware & Accelerators/Accelerator Architecture Subject|Accelerator Architecture]] → [[02 Concepts/Stack/Hardware & Accelerators/Hardware & Accelerators Index|Hardware & Accelerators]]

## Book Passages

These are explicitly recorded related passages from the upstream draft alignment; they do not certify complete coverage.

No explicit passage alignment is recorded for this concept. Subject reading pointers are available in its browsing home.

## Conditional Relationships

These are the taxonomy's draft editorial relationships. Read each relationship with its condition; an outgoing link is not a prerequisite claim.

- Specializes accelerator organization at wafer scale [[02 Concepts/Stack/Hardware & Accelerators/Domain Specific Architecture|Domain Specific Architecture]]. **Condition:** When the wafer-scale device is designed for ML computation.

- Uses explicit operand and intermediate placement [[02 Concepts/Stack/Hardware & Accelerators/Accelerator Dataflow|Accelerator Dataflow]]. **Condition:** When work is mapped across distributed compute tiles and local memories.

## Search Terms

Upstream search terms may be related terms rather than exact synonyms: wafer-scale accelerator; wafer-scale engine.

## Source

[Canonical Taxonomy](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/taxonomy.yml) · [Passage Alignment](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/mlsysbook-alignment.yml)

Taxonomy definitions and relationship wording: CC BY 4.0, with attribution to the Machine Learning Systems curriculum by Vijay Janapa Reddi and contributors. The textbook retains its separate license.
