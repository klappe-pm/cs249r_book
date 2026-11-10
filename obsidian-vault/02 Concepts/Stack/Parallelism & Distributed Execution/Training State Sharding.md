---
title: Training State Sharding
type: concept
tags:
- Type/Concept
- Group/Stack
- Topic/Parallelism_Strategies
source_repository: https://github.com/klappe-pm/cs249r_book
source_commit: de87c0103806d7bfb1c677dbb77a2b92fa00c298
source_path: taxonomy/taxonomy.yml
source_label: Training-state sharding
taxonomy_id: mlsys.state-sharding
taxonomy_status: draft
taxonomy_version: 0.4-draft
---

# Training State Sharding

Partitioning parameters, gradients, or optimizer state across workers.

## Browsing Home

[[02 Concepts/Stack/Parallelism & Distributed Execution/Parallelism Strategies Subject|Parallelism Strategies]] → [[02 Concepts/Stack/Parallelism & Distributed Execution/Parallelism & Distributed Execution Index|Parallelism & Distributed Execution]]

## Book Passages

These are explicitly recorded related passages from the upstream draft alignment; they do not certify complete coverage.

- [[01 Books/Volume II - Scaling/02 Distributed ML/06 Distributed Training/V2-06.04 Data Parallelism#^sec-distributed-training-systems-systems-memoryefficient-data-parallelism-zero-fsdp-0e69|V2-06.04 Data Parallelism]] — Training-state sharding. [Exact Source Passage](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/books/vol2/06_distributed_training/06_distributed_training.qmd#L1865).

## Conditional Relationships

These are the taxonomy's draft editorial relationships. Read each relationship with its condition; an outgoing link is not a prerequisite claim.

- Reduces per-worker copies of [[02 Concepts/Lifecycle/Training & Adaptation/Training State|Training State]]. **Condition:** Replication, communication, and reconstruction depend on the sharding stage.

- Gathers and scatters state through [[02 Concepts/Stack/Parallelism & Distributed Execution/Collective Communication|Collective Communication]]. **Condition:** Sharded parameters are all-gathered before use and gradients reduce-scattered after.

- Divides per-worker [[02 Concepts/Foundations/Workloads & Requirements/Memory Footprint|Memory Footprint]]. **Condition:** Parameters, gradients, or optimizer state are partitioned instead of replicated.

- All-gathers parameters before use and reduce-scatters gradients after, through [[02 Concepts/Stack/Parallelism & Distributed Execution/Reduce Scatter and All Gather|Reduce Scatter and All Gather]]. **Condition:** When parameters, gradients, or optimizer state are sharded across data-parallel workers, as in ZeRO stage 3 or FSDP.

## Search Terms

Upstream search terms may be related terms rather than exact synonyms: ZeRO; FSDP; fully sharded data parallel.

## Source

[Canonical Taxonomy](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/taxonomy.yml) · [Passage Alignment](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/mlsysbook-alignment.yml)

Taxonomy definitions and relationship wording: CC BY 4.0, with attribution to the Machine Learning Systems curriculum by Vijay Janapa Reddi and contributors. The textbook retains its separate license.
