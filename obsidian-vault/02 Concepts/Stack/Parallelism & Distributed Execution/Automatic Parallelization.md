---
title: Automatic Parallelization
type: concept
tags:
- Type/Concept
- Group/Stack
- Topic/Parallelization_Planning_Placement
source_repository: https://github.com/klappe-pm/cs249r_book
source_commit: de87c0103806d7bfb1c677dbb77a2b92fa00c298
source_path: taxonomy/taxonomy.yml
source_label: Automatic parallelization
taxonomy_id: mlsys.auto-parallelization
taxonomy_status: draft
taxonomy_version: 0.4-draft
---

# Automatic Parallelization

Compiler-derived multi-device partitioning of a single-device program, found by propagating sharding annotations or by searching parallelism strategies under a cost model.

## Browsing Home

[[02 Concepts/Stack/Parallelism & Distributed Execution/Parallelization Planning & Placement Subject|Parallelization Planning & Placement]] → [[02 Concepts/Stack/Parallelism & Distributed Execution/Parallelism & Distributed Execution Index|Parallelism & Distributed Execution]]

## Book Passages

These are explicitly recorded related passages from the upstream draft alignment; they do not certify complete coverage.

No explicit passage alignment is recorded for this concept. Subject reading pointers are available in its browsing home.

## Conditional Relationships

These are the taxonomy's draft editorial relationships. Read each relationship with its condition; an outgoing link is not a prerequisite claim.

- Derives [[02 Concepts/Stack/Parallelism & Distributed Execution/Hybrid Parallelism|Hybrid Parallelism]]. **Condition:** The compiler's cost model must reflect the target device mesh's compute and link bandwidths for the chosen plan to be competitive.

- Ranks plans with [[02 Concepts/Foundations/Quantitative System Models/Analytical Performance Model|Analytical Performance Model]]. **Condition:** The search evaluates candidate partitionings with a cost model of compute and communication.

## Search Terms

Upstream search terms may be related terms rather than exact synonyms: auto-sharding; automatic parallelism.

## Source

[Canonical Taxonomy](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/taxonomy.yml) · [Passage Alignment](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/mlsysbook-alignment.yml)

Taxonomy definitions and relationship wording: CC BY 4.0, with attribution to the Machine Learning Systems curriculum by Vijay Janapa Reddi and contributors. The textbook retains its separate license.
