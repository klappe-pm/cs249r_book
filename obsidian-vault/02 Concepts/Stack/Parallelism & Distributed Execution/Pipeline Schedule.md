---
title: Pipeline Schedule
type: concept
tags:
- Type/Concept
- Group/Stack
- Topic/Parallelism_Strategies
source_repository: https://github.com/klappe-pm/cs249r_book
source_commit: de87c0103806d7bfb1c677dbb77a2b92fa00c298
source_path: taxonomy/taxonomy.yml
source_label: Pipeline schedule
taxonomy_id: mlsys.pipeline-schedule
taxonomy_status: draft
taxonomy_version: 0.4-draft
---

# Pipeline Schedule

The order in which pipeline stages run the forward and backward passes of microbatches (fill-drain, one-forward-one-backward, interleaved), which sets the bubble fraction and how many microbatches' activations each stage holds.

## Browsing Home

[[02 Concepts/Stack/Parallelism & Distributed Execution/Parallelism Strategies Subject|Parallelism Strategies]] → [[02 Concepts/Stack/Parallelism & Distributed Execution/Parallelism & Distributed Execution Index|Parallelism & Distributed Execution]]

## Book Passages

These are explicitly recorded related passages from the upstream draft alignment; they do not certify complete coverage.

- [[01 Books/Volume II - Scaling/02 Distributed ML/06 Distributed Training/V2-06.06 Model Parallelism#^sec-distributed-training-systems-systems-pipeline-parallelism-8748|V2-06.06 Model Parallelism]] — Pipeline parallelism. [Exact Source Passage](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/books/vol2/06_distributed_training/06_distributed_training.qmd#L3948).

## Conditional Relationships

These are the taxonomy's draft editorial relationships. Read each relationship with its condition; an outgoing link is not a prerequisite claim.

- Sets the idle fraction known as [[02 Concepts/Stack/Parallelism & Distributed Execution/Pipeline Bubble|Pipeline Bubble]]. **Condition:** For a given number of stages and microbatches; fill-drain, one-forward-one-backward, interleaved, and zero-bubble orders give different bubbles.

- Is the execution order of [[02 Concepts/Stack/Parallelism & Distributed Execution/Pipeline Parallelism|Pipeline Parallelism]]. **Condition:** When a model is partitioned into pipeline stages.

- Sets how many microbatches' activations each stage holds in [[02 Concepts/Foundations/Workloads & Requirements/Memory Footprint|Memory Footprint]]. **Condition:** When stages keep forward activations until the matching backward pass runs.

## Search Terms

Upstream search terms may be related terms rather than exact synonyms: GPipe schedule; 1F1B; interleaved 1F1B; zero-bubble schedule.

## Source

[Canonical Taxonomy](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/taxonomy.yml) · [Passage Alignment](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/mlsysbook-alignment.yml)

Taxonomy definitions and relationship wording: CC BY 4.0, with attribution to the Machine Learning Systems curriculum by Vijay Janapa Reddi and contributors. The textbook retains its separate license.
