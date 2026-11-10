---
title: Memory Mapped Model Weights
type: concept
tags:
- Type/Concept
- Group/Stack
- Topic/Runtime_Execution_Dispatch
source_repository: https://github.com/klappe-pm/cs249r_book
source_commit: de87c0103806d7bfb1c677dbb77a2b92fa00c298
source_path: taxonomy/taxonomy.yml
source_label: Memory-mapped model weights
taxonomy_id: mlsys.mmap-weights
taxonomy_status: draft
taxonomy_version: 0.4-draft
---

# Memory Mapped Model Weights

Mapping a weight file into virtual memory so pages load on demand and read-only weights are shared across processes, cutting load time and duplicate memory at the cost of page faults.

## Browsing Home

[[02 Concepts/Stack/Frameworks, Compilers & Runtimes/Runtime Execution & Dispatch Subject|Runtime Execution & Dispatch]] → [[02 Concepts/Stack/Frameworks, Compilers & Runtimes/Frameworks, Compilers & Runtimes Index|Frameworks, Compilers & Runtimes]]

## Book Passages

These are explicitly recorded related passages from the upstream draft alignment; they do not certify complete coverage.

No explicit passage alignment is recorded for this concept. Subject reading pointers are available in its browsing home.

## Conditional Relationships

These are the taxonomy's draft editorial relationships. Read each relationship with its condition; an outgoing link is not a prerequisite claim.

- Removes duplicate copies from [[02 Concepts/Foundations/Workloads & Requirements/Memory Footprint|Memory Footprint]]. **Condition:** Several processes serve the same read-only weights.

- Shortens [[02 Concepts/Lifecycle/Deployment & Serving/Model Cold Start|Model Cold Start]]. **Condition:** Only the pages touched by the first requests must load.

- Makes weight pages reclaimable without killing the process under [[02 Concepts/Stack/Frameworks, Compilers & Runtimes/OS Memory Pressure and Paging|OS Memory Pressure and Paging]]. **Condition:** When file-backed pages can be dropped and reread instead of the app being terminated.

## Search Terms

Upstream search terms may be related terms rather than exact synonyms: mmap weights; shared weight mapping; zero-copy model loading.

## Source

[Canonical Taxonomy](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/taxonomy.yml) · [Passage Alignment](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/mlsysbook-alignment.yml)

Taxonomy definitions and relationship wording: CC BY 4.0, with attribution to the Machine Learning Systems curriculum by Vijay Janapa Reddi and contributors. The textbook retains its separate license.
