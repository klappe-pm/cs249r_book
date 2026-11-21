---
title: Execute in Place Weights
type: concept
tags:
- Type/Concept
- Group/Stack
- Topic/Edge_Embedded_Hardware
source_repository: https://github.com/klappe-pm/cs249r_book
source_commit: de87c0103806d7bfb1c677dbb77a2b92fa00c298
source_path: taxonomy/taxonomy.yml
source_label: Execute-in-place weights
taxonomy_id: mlsys.execute-in-place
taxonomy_status: draft
taxonomy_version: 0.4-draft
---

# Execute in Place Weights

Reading immutable model weights from memory-mapped flash during inference without first copying them into SRAM, reducing working memory while exposing flash-access latency.

## Browsing Home

[[02 Concepts/Stack/Hardware & Accelerators/Edge & Embedded Hardware Subject|Edge & Embedded Hardware]] → [[02 Concepts/Stack/Hardware & Accelerators/Hardware & Accelerators Index|Hardware & Accelerators]]

## Book Passages

These are explicitly recorded related passages from the upstream draft alignment; they do not certify complete coverage.

No explicit passage alignment is recorded for this concept. Subject reading pointers are available in its browsing home.

## Conditional Relationships

These are the taxonomy's draft editorial relationships. Read each relationship with its condition; an outgoing link is not a prerequisite claim.

- Keeps frozen weights out of working SRAM in [[02 Concepts/Foundations/Workloads & Requirements/Memory Footprint|Memory Footprint]]. **Condition:** When read-only parameters stay in memory-mapped flash during inference.

## Search Terms

Upstream search terms may be related terms rather than exact synonyms: XIP; flash-resident weights.

## Source

[Canonical Taxonomy](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/taxonomy.yml) · [Passage Alignment](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/mlsysbook-alignment.yml)

Taxonomy definitions and relationship wording: CC BY 4.0, with attribution to the Machine Learning Systems curriculum by Vijay Janapa Reddi and contributors. The textbook retains its separate license.
