---
title: Parameter Server
type: concept
tags:
- Type/Concept
- Group/Stack
- Topic/Parallelism_Strategies
source_repository: https://github.com/klappe-pm/cs249r_book
source_commit: de87c0103806d7bfb1c677dbb77a2b92fa00c298
source_path: taxonomy/taxonomy.yml
source_label: Parameter server
taxonomy_id: mlsys.parameter-server
taxonomy_status: draft
taxonomy_version: 0.4-draft
---

# Parameter Server

An architecture in which workers pull and push model parameters from sharded server processes, common for sparse recommendation models and asynchronous training.

## Browsing Home

[[02 Concepts/Stack/Parallelism & Distributed Execution/Parallelism Strategies Subject|Parallelism Strategies]] → [[02 Concepts/Stack/Parallelism & Distributed Execution/Parallelism & Distributed Execution Index|Parallelism & Distributed Execution]]

## Book Passages

These are explicitly recorded related passages from the upstream draft alignment; they do not certify complete coverage.

No explicit passage alignment is recorded for this concept. Subject reading pointers are available in its browsing home.

## Conditional Relationships

These are the taxonomy's draft editorial relationships. Read each relationship with its condition; an outgoing link is not a prerequisite claim.

- Commonly operates under [[02 Concepts/Stack/Parallelism & Distributed Execution/Bounded Staleness|Bounded Staleness]]. **Condition:** Workers may read parameters that lag the latest updates by a bounded number of steps.

- Is an alternative to [[02 Concepts/Stack/Parallelism & Distributed Execution/Ring All Reduce|Ring All Reduce]]. **Condition:** Both aggregate gradients for data-parallel training; servers suit sparse or asynchronous updates, all-reduce suits dense synchronous ones.

- Makes asynchronous updates practical for [[02 Concepts/Stack/Parallelism & Distributed Execution/Synchronous vs. Asynchronous Training|Synchronous vs. Asynchronous Training]]. **Condition:** Workers push and pull parameters without a global barrier.

## Search Terms

Upstream search terms may be related terms rather than exact synonyms: PS architecture.

## Source

[Canonical Taxonomy](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/taxonomy.yml) · [Passage Alignment](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/mlsysbook-alignment.yml)

Taxonomy definitions and relationship wording: CC BY 4.0, with attribution to the Machine Learning Systems curriculum by Vijay Janapa Reddi and contributors. The textbook retains its separate license.
