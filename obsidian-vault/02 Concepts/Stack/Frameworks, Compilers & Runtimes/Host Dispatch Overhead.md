---
title: Host Dispatch Overhead
type: concept
tags:
- Type/Concept
- Group/Stack
- Topic/Runtime_Execution_Dispatch
source_repository: https://github.com/klappe-pm/cs249r_book
source_commit: de87c0103806d7bfb1c677dbb77a2b92fa00c298
source_path: taxonomy/taxonomy.yml
source_label: Host dispatch overhead
taxonomy_id: mlsys.dispatch
taxonomy_status: draft
taxonomy_version: 0.4-draft
---

# Host Dispatch Overhead

Host-side work required to launch or orchestrate device operations.

## Browsing Home

[[02 Concepts/Stack/Frameworks, Compilers & Runtimes/Runtime Execution & Dispatch Subject|Runtime Execution & Dispatch]] → [[02 Concepts/Stack/Frameworks, Compilers & Runtimes/Frameworks, Compilers & Runtimes Index|Frameworks, Compilers & Runtimes]]

## Book Passages

These are explicitly recorded related passages from the upstream draft alignment; they do not certify complete coverage.

- [[01 Books/Volume I - Foundations/02 Development/07 ML Frameworks/V1-07.04 Execution from Graphs to Kernels#^sec-ml-frameworks-dispatch-tax|V1-07.04 Execution from Graphs to Kernels]] — Dispatch overhead. [Exact Source Passage](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/books/vol1/07_frameworks/07_frameworks.qmd#L860).

## Conditional Relationships

These are the taxonomy's draft editorial relationships. Read each relationship with its condition; an outgoing link is not a prerequisite claim.

- Places small operations on the overhead-bound side of [[02 Concepts/Foundations/Quantitative System Models/Compute Bound vs. Memory Bound|Compute Bound vs. Memory Bound]]. **Condition:** When per-kernel work is so small that host launch and orchestration time exceeds device execution time, as in small-batch decode of small models.

- Contributes host-side, non-overlapped work to [[02 Concepts/Foundations/Quantitative System Models/Serial Fraction|Serial Fraction]]. **Condition:** When launch and orchestration time is not overlapped with device execution, so it stays constant as device throughput or worker count grows.

## Search Terms

Upstream search terms may be related terms rather than exact synonyms: kernel launch overhead.

## Source

[Canonical Taxonomy](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/taxonomy.yml) · [Passage Alignment](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/mlsysbook-alignment.yml)

Taxonomy definitions and relationship wording: CC BY 4.0, with attribution to the Machine Learning Systems curriculum by Vijay Janapa Reddi and contributors. The textbook retains its separate license.
