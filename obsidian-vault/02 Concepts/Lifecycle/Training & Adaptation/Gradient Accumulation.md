---
title: Gradient Accumulation
type: concept
tags:
- Type/Concept
- Group/Lifecycle
- Topic/Training_Memory_State
source_repository: https://github.com/klappe-pm/cs249r_book
source_commit: de87c0103806d7bfb1c677dbb77a2b92fa00c298
source_path: taxonomy/taxonomy.yml
source_label: Gradient accumulation
taxonomy_id: mlsys.gradient-accumulation
taxonomy_status: draft
taxonomy_version: 0.4-draft
---

# Gradient Accumulation

Summing gradients over several micro-batches before one optimizer update to emulate a larger batch within limited memory.

## Browsing Home

[[02 Concepts/Lifecycle/Training & Adaptation/Training Memory & State Subject|Training Memory & State]] → [[02 Concepts/Lifecycle/Training & Adaptation/Training & Adaptation Index|Training & Adaptation]]

## Book Passages

These are explicitly recorded related passages from the upstream draft alignment; they do not certify complete coverage.

No explicit passage alignment is recorded for this concept. Subject reading pointers are available in its browsing home.

## Conditional Relationships

These are the taxonomy's draft editorial relationships. Read each relationship with its condition; an outgoing link is not a prerequisite claim.

- Enables large effective batch sizes within limited memory for [[02 Concepts/Lifecycle/Training & Adaptation/Training Batch Size|Training Batch Size]]. **Condition:** Holds for losses that sum over examples; per-batch statistics such as batch normalization still see micro-batches.

- Shrinks, through more microbatches, [[02 Concepts/Stack/Parallelism & Distributed Execution/Pipeline Bubble|Pipeline Bubble]]. **Condition:** More microbatches per optimizer step fill the pipeline relative to the number of stages.

- Reduces per-step activation [[02 Concepts/Foundations/Workloads & Requirements/Memory Footprint|Memory Footprint]]. **Condition:** Holds because activation memory scales with micro-batch, not effective batch.

- Reduces the frequency of [[02 Concepts/Stack/Parallelism & Distributed Execution/Collective Communication|Collective Communication]]. **Condition:** Holds when gradient all-reduce is deferred to the last micro-batch.

## Source

[Canonical Taxonomy](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/taxonomy.yml) · [Passage Alignment](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/mlsysbook-alignment.yml)

Taxonomy definitions and relationship wording: CC BY 4.0, with attribution to the Machine Learning Systems curriculum by Vijay Janapa Reddi and contributors. The textbook retains its separate license.
