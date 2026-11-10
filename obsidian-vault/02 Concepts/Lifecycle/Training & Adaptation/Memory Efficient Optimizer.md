---
title: Memory Efficient Optimizer
type: concept
tags:
- Type/Concept
- Group/Lifecycle
- Topic/Training_Memory_State
source_repository: https://github.com/klappe-pm/cs249r_book
source_commit: de87c0103806d7bfb1c677dbb77a2b92fa00c298
source_path: taxonomy/taxonomy.yml
source_label: Memory-efficient optimizer
taxonomy_id: mlsys.memory-efficient-optimizer
taxonomy_status: draft
taxonomy_version: 0.4-draft
---

# Memory Efficient Optimizer

Optimizers that shrink per-parameter state through factorization, low-rank projection, or low-precision storage, cutting the memory adaptive methods such as Adam otherwise require.

## Browsing Home

[[02 Concepts/Lifecycle/Training & Adaptation/Training Memory & State Subject|Training Memory & State]] → [[02 Concepts/Lifecycle/Training & Adaptation/Training & Adaptation Index|Training & Adaptation]]

## Book Passages

These are explicitly recorded related passages from the upstream draft alignment; they do not certify complete coverage.

No explicit passage alignment is recorded for this concept. Subject reading pointers are available in its browsing home.

## Conditional Relationships

These are the taxonomy's draft editorial relationships. Read each relationship with its condition; an outgoing link is not a prerequisite claim.

- Is a reduced-state form of [[02 Concepts/Lifecycle/Training & Adaptation/Optimization Algorithm|Optimization Algorithm]]. **Condition:** Full adaptive state exceeds memory.

- Shrinks the optimizer-state share of [[02 Concepts/Foundations/Workloads & Requirements/Memory Footprint|Memory Footprint]]. **Condition:** Optimizer state dominates training memory.

- Shrinks state rather than distributing it as in [[02 Concepts/Stack/Parallelism & Distributed Execution/Training State Sharding|Training State Sharding]]. **Condition:** Few devices are available to shard across.

## Search Terms

Upstream search terms may be related terms rather than exact synonyms: low-rank optimizer state; 8-bit optimizer.

## Source

[Canonical Taxonomy](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/taxonomy.yml) · [Passage Alignment](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/mlsysbook-alignment.yml)

Taxonomy definitions and relationship wording: CC BY 4.0, with attribution to the Machine Learning Systems curriculum by Vijay Janapa Reddi and contributors. The textbook retains its separate license.
