---
title: Captured Graph Replay
type: concept
tags:
- Type/Concept
- Group/Stack
- Topic/Runtime_Execution_Dispatch
source_repository: https://github.com/klappe-pm/cs249r_book
source_commit: de87c0103806d7bfb1c677dbb77a2b92fa00c298
source_path: taxonomy/taxonomy.yml
source_label: Captured graph replay
taxonomy_id: mlsys.graph-replay
taxonomy_status: draft
taxonomy_version: 0.4-draft
---

# Captured Graph Replay

Recording a fixed sequence of kernel launches once and replaying it as a unit to remove per-launch host overhead.

## Browsing Home

[[02 Concepts/Stack/Frameworks, Compilers & Runtimes/Runtime Execution & Dispatch Subject|Runtime Execution & Dispatch]] → [[02 Concepts/Stack/Frameworks, Compilers & Runtimes/Frameworks, Compilers & Runtimes Index|Frameworks, Compilers & Runtimes]]

## Book Passages

These are explicitly recorded related passages from the upstream draft alignment; they do not certify complete coverage.

No explicit passage alignment is recorded for this concept. Subject reading pointers are available in its browsing home.

## Conditional Relationships

These are the taxonomy's draft editorial relationships. Read each relationship with its condition; an outgoing link is not a prerequisite claim.

- Reduces [[02 Concepts/Stack/Frameworks, Compilers & Runtimes/Host Dispatch Overhead|Host Dispatch Overhead]]. **Condition:** The launch sequence and tensor addresses are static across iterations.

- Is captured from and replayed on [[02 Concepts/Stack/Frameworks, Compilers & Runtimes/Device Streams|Device Streams]]. **Condition:** Work enqueued on a stream is recorded as a graph and replayed as one launch.

- Reduces per-step launch overhead in [[02 Concepts/Lifecycle/Deployment & Serving/Time per Output Token|Time per Output Token]]. **Condition:** Decode steps launch many small kernels with static shapes, so host overhead is a large share of step time.

## Search Terms

Upstream search terms may be related terms rather than exact synonyms: CUDA Graphs.

## Source

[Canonical Taxonomy](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/taxonomy.yml) · [Passage Alignment](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/mlsysbook-alignment.yml)

Taxonomy definitions and relationship wording: CC BY 4.0, with attribution to the Machine Learning Systems curriculum by Vijay Janapa Reddi and contributors. The textbook retains its separate license.
