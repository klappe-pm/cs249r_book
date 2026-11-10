---
title: CPU Execution Architecture
type: concept
tags:
- Type/Concept
- Group/Stack
- Topic/Accelerator_Architecture
source_repository: https://github.com/klappe-pm/cs249r_book
source_commit: de87c0103806d7bfb1c677dbb77a2b92fa00c298
source_path: taxonomy/taxonomy.yml
source_label: CPU execution architecture
taxonomy_id: mlsys.cpu-execution-architecture
taxonomy_status: draft
taxonomy_version: 0.4-draft
---

# CPU Execution Architecture

Organization of general-purpose processor cores, SIMD vector units, and multilevel caches that runs host code, preprocessing, classical models, and CPU inference.

## Browsing Home

[[02 Concepts/Stack/Hardware & Accelerators/Accelerator Architecture Subject|Accelerator Architecture]] → [[02 Concepts/Stack/Hardware & Accelerators/Hardware & Accelerators Index|Hardware & Accelerators]]

## Book Passages

These are explicitly recorded related passages from the upstream draft alignment; they do not certify complete coverage.

No explicit passage alignment is recorded for this concept. Subject reading pointers are available in its browsing home.

## Conditional Relationships

These are the taxonomy's draft editorial relationships. Read each relationship with its condition; an outgoing link is not a prerequisite claim.

- Is a competing execution target to [[02 Concepts/Stack/Hardware & Accelerators/Accelerator Execution Architecture|Accelerator Execution Architecture]]. **Condition:** The workload is small, sparse, or latency-bound enough that host execution is viable.

- Relies on caches and DRAM levels of [[02 Concepts/Stack/Hardware & Accelerators/Memory Hierarchy|Memory Hierarchy]]. **Condition:** Performance depends on working-set reuse in the cache levels.

## Search Terms

Upstream search terms may be related terms rather than exact synonyms: general-purpose CPU; host CPU; CPU vector units.

## Source

[Canonical Taxonomy](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/taxonomy.yml) · [Passage Alignment](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/mlsysbook-alignment.yml)

Taxonomy definitions and relationship wording: CC BY 4.0, with attribution to the Machine Learning Systems curriculum by Vijay Janapa Reddi and contributors. The textbook retains its separate license.
