---
title: Heterogeneous Accelerator Training and Serving
type: concept
tags:
- Type/Concept
- Group/Stack
- Topic/Parallelization_Planning_Placement
source_repository: https://github.com/klappe-pm/cs249r_book
source_commit: de87c0103806d7bfb1c677dbb77a2b92fa00c298
source_path: taxonomy/taxonomy.yml
source_label: Heterogeneous-accelerator training and serving
taxonomy_id: mlsys.heterogeneous-accelerator-execution
taxonomy_status: draft
taxonomy_version: 0.4-draft
---

# Heterogeneous Accelerator Training and Serving

Partitioning one training or serving job across accelerators of different types or generations, sizing stages and batch shares to each device's compute, memory, and links.

## Browsing Home

[[02 Concepts/Stack/Parallelism & Distributed Execution/Parallelization Planning & Placement Subject|Parallelization Planning & Placement]] → [[02 Concepts/Stack/Parallelism & Distributed Execution/Parallelism & Distributed Execution Index|Parallelism & Distributed Execution]]

## Book Passages

These are explicitly recorded related passages from the upstream draft alignment; they do not certify complete coverage.

No explicit passage alignment is recorded for this concept. Subject reading pointers are available in its browsing home.

## Conditional Relationships

These are the taxonomy's draft editorial relationships. Read each relationship with its condition; an outgoing link is not a prerequisite claim.

- Assigns unequal stages through [[02 Concepts/Stack/Parallelism & Distributed Execution/Pipeline Parallelism|Pipeline Parallelism]]. **Condition:** Stage sizes are matched to each device type's compute and memory.

- Searches placements and plans with [[02 Concepts/Stack/Parallelism & Distributed Execution/Automatic Parallelization|Automatic Parallelization]]. **Condition:** Device types differ in throughput, memory, and interconnect.

## Search Terms

Upstream search terms may be related terms rather than exact synonyms: heterogeneous GPU clusters; mixed-generation GPU training.

## Source

[Canonical Taxonomy](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/taxonomy.yml) · [Passage Alignment](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/mlsysbook-alignment.yml)

Taxonomy definitions and relationship wording: CC BY 4.0, with attribution to the Machine Learning Systems curriculum by Vijay Janapa Reddi and contributors. The textbook retains its separate license.
