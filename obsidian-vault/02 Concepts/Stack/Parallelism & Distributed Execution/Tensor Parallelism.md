---
title: Tensor Parallelism
type: concept
tags:
- Type/Concept
- Group/Stack
- Topic/Parallelism_Strategies
source_repository: https://github.com/klappe-pm/cs249r_book
source_commit: de87c0103806d7bfb1c677dbb77a2b92fa00c298
source_path: taxonomy/taxonomy.yml
source_label: Tensor parallelism
taxonomy_id: mlsys.tensor-parallel
taxonomy_status: draft
taxonomy_version: 0.4-draft
---

# Tensor Parallelism

Partitioning a layer's tensors and operations across devices so each computes a slice, reducing per-device state while adding communication along the partitioned dimensions, usually within a fast scale-up domain.

## Browsing Home

[[02 Concepts/Stack/Parallelism & Distributed Execution/Parallelism Strategies Subject|Parallelism Strategies]] → [[02 Concepts/Stack/Parallelism & Distributed Execution/Parallelism & Distributed Execution Index|Parallelism & Distributed Execution]]

## Book Passages

These are explicitly recorded related passages from the upstream draft alignment; they do not certify complete coverage.

- [[01 Books/Volume II - Scaling/02 Distributed ML/06 Distributed Training/V2-06.06 Model Parallelism#^sec-distributed-training-systems-systems-tensor-parallelism-d76e|V2-06.06 Model Parallelism]] — Tensor parallelism. [Exact Source Passage](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/books/vol2/06_distributed_training/06_distributed_training.qmd#L4345).

## Conditional Relationships

These are the taxonomy's draft editorial relationships. Read each relationship with its condition; an outgoing link is not a prerequisite claim.

- Requires per-layer [[02 Concepts/Stack/Parallelism & Distributed Execution/Collective Communication|Collective Communication]]. **Condition:** Partitioned operations require data exchange according to their decomposition.

- Partitions [[02 Concepts/Stack/Frameworks, Compilers & Runtimes/Matrix Multiplication|Matrix Multiplication]]. **Condition:** For tensor decompositions whose operand and reduction partitions require compatible communication and layout.

- Replaces per-layer all-reduce with [[02 Concepts/Stack/Parallelism & Distributed Execution/Reduce Scatter and All Gather|Reduce Scatter and All Gather]]. **Condition:** When tensor-parallel layers are combined with Megatron-style sequence parallelism so each all-reduce becomes a reduce-scatter and all-gather pair.

- Is one dimension of [[02 Concepts/Stack/Parallelism & Distributed Execution/Hybrid Parallelism|Hybrid Parallelism]]. **Condition:** When tensor-parallel groups are placed within the fastest scale-up domain and combined with data and pipeline parallelism across nodes.

- Shards a layer's parameters and activations to lower the per-device [[02 Concepts/Foundations/Workloads & Requirements/Memory Footprint|Memory Footprint]]. **Condition:** Aggregate footprint is unchanged; per-device savings depend on which tensors are partitioned.

- Pools the memory bandwidth of several devices to shorten [[02 Concepts/Lifecycle/Deployment & Serving/Time per Output Token|Time per Output Token]]. **Condition:** For the same model, precision, batch, and output workload, when tensor sharding reduces per-device decode memory traffic and the saved memory-access time exceeds the added collective, synchronization, and execution overhead.

## Themes

- [[03 Themes/Scaling and Coordination|Scaling and Coordination]]

## Search Terms

Upstream search terms may be related terms rather than exact synonyms: intra-layer model parallelism.

## Source

[Canonical Taxonomy](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/taxonomy.yml) · [Passage Alignment](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/mlsysbook-alignment.yml)

Taxonomy definitions and relationship wording: CC BY 4.0, with attribution to the Machine Learning Systems curriculum by Vijay Janapa Reddi and contributors. The textbook retains its separate license.
