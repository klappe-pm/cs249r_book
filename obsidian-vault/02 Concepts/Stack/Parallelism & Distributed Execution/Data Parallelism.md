---
title: Data Parallelism
type: concept
tags:
- Type/Concept
- Group/Stack
- Topic/Parallelism_Strategies
source_repository: https://github.com/klappe-pm/cs249r_book
source_commit: de87c0103806d7bfb1c677dbb77a2b92fa00c298
source_path: taxonomy/taxonomy.yml
source_label: Data parallelism
taxonomy_id: mlsys.data-parallel
taxonomy_status: draft
taxonomy_version: 0.4-draft
---

# Data Parallelism

Executing model replicas on different examples while coordinating learning state.

## Browsing Home

[[02 Concepts/Stack/Parallelism & Distributed Execution/Parallelism Strategies Subject|Parallelism Strategies]] → [[02 Concepts/Stack/Parallelism & Distributed Execution/Parallelism & Distributed Execution Index|Parallelism & Distributed Execution]]

## Book Passages

These are explicitly recorded related passages from the upstream draft alignment; they do not certify complete coverage.

- [[01 Books/Volume II - Scaling/02 Distributed ML/06 Distributed Training/V2-06.04 Data Parallelism#^sec-distributed-training-systems-systems-data-parallelism-6132|V2-06.04 Data Parallelism]] — Data parallelism. [Exact Source Passage](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/books/vol2/06_distributed_training/06_distributed_training.qmd#L794).

## Conditional Relationships

These are the taxonomy's draft editorial relationships. Read each relationship with its condition; an outgoing link is not a prerequisite claim.

- Uses [[02 Concepts/Stack/Parallelism & Distributed Execution/Collective Communication|Collective Communication]]. **Condition:** Synchronous replicas commonly aggregate gradients; other learning semantics differ.

- Replicates, multiplying the total footprint of, [[02 Concepts/Lifecycle/Training & Adaptation/Training State|Training State]]. **Condition:** Conventional replicated data parallelism keeps model and update state at each worker; ZeRO and hybrid strategies shard selected components.

- Cuts gradient-synchronization volume with [[02 Concepts/Stack/Parallelism & Distributed Execution/Gradient Compression|Gradient Compression]]. **Condition:** Convergence is preserved, for example through error feedback, at the chosen compression ratio.

- Requires [[02 Concepts/Stack/Datacenter Infrastructure & Fleet/Gang Scheduling|Gang Scheduling]]. **Condition:** Synchronous replicas cannot start or step until every worker holds its allocation.

- Synchronizes gradients through [[02 Concepts/Stack/Parallelism & Distributed Execution/All Reduce|All Reduce]]. **Condition:** When replicas combine gradients before each optimizer step, as in synchronous data parallelism.

- Is the outermost dimension of [[02 Concepts/Stack/Parallelism & Distributed Execution/Hybrid Parallelism|Hybrid Parallelism]]. **Condition:** When replicas of a tensor- or pipeline-parallel model group are themselves data-parallel across nodes.

- Partitions state across workers through [[02 Concepts/Stack/Parallelism & Distributed Execution/Training State Sharding|Training State Sharding]]. **Condition:** When each worker processes different examples but holds only a shard of parameters, gradients, or optimizer state.

## Themes

- [[03 Themes/Scaling and Coordination|Scaling and Coordination]]

## Source

[Canonical Taxonomy](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/taxonomy.yml) · [Passage Alignment](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/mlsysbook-alignment.yml)

Taxonomy definitions and relationship wording: CC BY 4.0, with attribution to the Machine Learning Systems curriculum by Vijay Janapa Reddi and contributors. The textbook retains its separate license.
