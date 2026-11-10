---
title: Training Memory Estimate
type: concept
tags:
- Type/Concept
- Group/Lifecycle
- Topic/Training_Memory_State
source_repository: https://github.com/klappe-pm/cs249r_book
source_commit: de87c0103806d7bfb1c677dbb77a2b92fa00c298
source_path: taxonomy/taxonomy.yml
source_label: Training memory estimate
taxonomy_id: mlsys.training-memory-estimate
taxonomy_status: draft
taxonomy_version: 0.4-draft
---

# Training Memory Estimate

Approximating a training step's accelerator memory as a per-parameter cost for weights, gradients, and optimizer state in their chosen precisions, plus activation memory that grows with batch size, sequence length, and depth, to decide what fits before a run is launched.

## Browsing Home

[[02 Concepts/Lifecycle/Training & Adaptation/Training Memory & State Subject|Training Memory & State]] → [[02 Concepts/Lifecycle/Training & Adaptation/Training & Adaptation Index|Training & Adaptation]]

## Book Passages

These are explicitly recorded related passages from the upstream draft alignment; they do not certify complete coverage.

No explicit passage alignment is recorded for this concept. Subject reading pointers are available in its browsing home.

## Conditional Relationships

These are the taxonomy's draft editorial relationships. Read each relationship with its condition; an outgoing link is not a prerequisite claim.

- Sizes [[02 Concepts/Lifecycle/Training & Adaptation/Training State|Training State]]. **Condition:** For dense models where each component's precision and the optimizer's state count are known.

- Takes byte widths from [[02 Concepts/Stack/Frameworks, Compilers & Runtimes/Numerical Precision|Numerical Precision]]. **Condition:** Each state component may use a different format.

- Estimates the training share of [[02 Concepts/Foundations/Workloads & Requirements/Memory Footprint|Memory Footprint]]. **Condition:** Runtime buffers and allocator overhead are added separately.

## Search Terms

Upstream search terms may be related terms rather than exact synonyms: bytes per parameter; mixed-precision memory rule; activation memory estimate.

## Source

[Canonical Taxonomy](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/taxonomy.yml) · [Passage Alignment](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/mlsysbook-alignment.yml)

Taxonomy definitions and relationship wording: CC BY 4.0, with attribution to the Machine Learning Systems curriculum by Vijay Janapa Reddi and contributors. The textbook retains its separate license.
