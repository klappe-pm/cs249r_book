---
title: Pipeline Parallelism
type: concept
tags:
- Type/Concept
- Group/Stack
- Topic/Parallelism_Strategies
source_repository: https://github.com/klappe-pm/cs249r_book
source_commit: de87c0103806d7bfb1c677dbb77a2b92fa00c298
source_path: taxonomy/taxonomy.yml
source_label: Pipeline parallelism
taxonomy_id: mlsys.pipeline-parallel
taxonomy_status: draft
taxonomy_version: 0.4-draft
---

# Pipeline Parallelism

Partitioning a computation into stages that process different microbatches concurrently.

## Browsing Home

[[02 Concepts/Stack/Parallelism & Distributed Execution/Parallelism Strategies Subject|Parallelism Strategies]] → [[02 Concepts/Stack/Parallelism & Distributed Execution/Parallelism & Distributed Execution Index|Parallelism & Distributed Execution]]

## Book Passages

These are explicitly recorded related passages from the upstream draft alignment; they do not certify complete coverage.

- [[01 Books/Volume II - Scaling/02 Distributed ML/06 Distributed Training/V2-06.06 Model Parallelism#^sec-distributed-training-systems-systems-pipeline-parallelism-8748|V2-06.06 Model Parallelism]] — Pipeline parallelism. [Exact Source Passage](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/books/vol2/06_distributed_training/06_distributed_training.qmd#L3948).

## Conditional Relationships

These are the taxonomy's draft editorial relationships. Read each relationship with its condition; an outgoing link is not a prerequisite claim.

- Incurs [[02 Concepts/Stack/Parallelism & Distributed Execution/Pipeline Bubble|Pipeline Bubble]]. **Condition:** Microbatches per step are few relative to pipeline stages.

- Divides per-device parameter [[02 Concepts/Foundations/Workloads & Requirements/Memory Footprint|Memory Footprint]]. **Condition:** Each stage holds only its layers' parameters and their state.

- Is one dimension of [[02 Concepts/Stack/Parallelism & Distributed Execution/Hybrid Parallelism|Hybrid Parallelism]]. **Condition:** Pipeline stages are combined with data and tensor parallelism across nodes.

## Themes

- [[03 Themes/Scaling and Coordination|Scaling and Coordination]]

## Search Terms

Upstream search terms may be related terms rather than exact synonyms: inter-layer model parallelism.

## Source

[Canonical Taxonomy](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/taxonomy.yml) · [Passage Alignment](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/mlsysbook-alignment.yml)

Taxonomy definitions and relationship wording: CC BY 4.0, with attribution to the Machine Learning Systems curriculum by Vijay Janapa Reddi and contributors. The textbook retains its separate license.
