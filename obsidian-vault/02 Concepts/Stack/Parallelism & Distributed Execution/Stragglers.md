---
title: Stragglers
type: concept
tags:
- Type/Concept
- Group/Stack
- Topic/Collective_Communication
source_repository: https://github.com/klappe-pm/cs249r_book
source_commit: de87c0103806d7bfb1c677dbb77a2b92fa00c298
source_path: taxonomy/taxonomy.yml
source_label: Stragglers
taxonomy_id: mlsys.stragglers
taxonomy_status: draft
taxonomy_version: 0.4-draft
---

# Stragglers

Workers or tasks whose delayed completion holds back coordinated work.

## Browsing Home

[[02 Concepts/Stack/Parallelism & Distributed Execution/Collective Communication Subject|Collective Communication]] → [[02 Concepts/Stack/Parallelism & Distributed Execution/Parallelism & Distributed Execution Index|Parallelism & Distributed Execution]]

## Book Passages

These are explicitly recorded related passages from the upstream draft alignment; they do not certify complete coverage.

No explicit passage alignment is recorded for this concept. Subject reading pointers are available in its browsing home.

## Conditional Relationships

These are the taxonomy's draft editorial relationships. Read each relationship with its condition; an outgoing link is not a prerequisite claim.

- Stall [[02 Concepts/Stack/Parallelism & Distributed Execution/Pipeline Parallelism|Pipeline Parallelism]]. **Condition:** Dependencies and pipeline bubbles expose unequal stage or worker times.

- Reduce [[02 Concepts/Foundations/Quantitative System Models/Parallel Scaling Efficiency|Parallel Scaling Efficiency]]. **Condition:** Workers synchronize so the slowest determines step time.

- Idles every other rank, lowering [[02 Concepts/Qualities/Performance, Efficiency & Benchmarking/Training Goodput|Training Goodput]]. **Condition:** In synchronous training, where each step waits for the slowest rank; asynchronous or straggler-tolerant schemes break the dependence.

## Source

[Canonical Taxonomy](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/taxonomy.yml) · [Passage Alignment](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/mlsysbook-alignment.yml)

Taxonomy definitions and relationship wording: CC BY 4.0, with attribution to the Machine Learning Systems curriculum by Vijay Janapa Reddi and contributors. The textbook retains its separate license.
