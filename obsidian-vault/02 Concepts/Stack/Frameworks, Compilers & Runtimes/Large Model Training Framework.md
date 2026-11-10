---
title: Large Model Training Framework
type: concept
tags:
- Type/Concept
- Group/Stack
- Topic/ML_Frameworks_Programming_Models
source_repository: https://github.com/klappe-pm/cs249r_book
source_commit: de87c0103806d7bfb1c677dbb77a2b92fa00c298
source_path: taxonomy/taxonomy.yml
source_label: Large-model training framework
taxonomy_id: mlsys.llm-training-framework
taxonomy_status: draft
taxonomy_version: 0.4-draft
---

# Large Model Training Framework

A library that composes data, tensor, pipeline, and sharded-state parallelism with memory optimizations behind one training configuration for models exceeding one device.

## Browsing Home

[[02 Concepts/Stack/Frameworks, Compilers & Runtimes/ML Frameworks & Programming Models Subject|ML Frameworks & Programming Models]] → [[02 Concepts/Stack/Frameworks, Compilers & Runtimes/Frameworks, Compilers & Runtimes Index|Frameworks, Compilers & Runtimes]]

## Book Passages

These are explicitly recorded related passages from the upstream draft alignment; they do not certify complete coverage.

No explicit passage alignment is recorded for this concept. Subject reading pointers are available in its browsing home.

## Conditional Relationships

These are the taxonomy's draft editorial relationships. Read each relationship with its condition; an outgoing link is not a prerequisite claim.

- Packages [[02 Concepts/Stack/Parallelism & Distributed Execution/Hybrid Parallelism|Hybrid Parallelism]]. **Condition:** Parallelism degrees are set by configuration and mapped to the device topology.

- Commonly applies [[02 Concepts/Stack/Parallelism & Distributed Execution/Training State Sharding|Training State Sharding]]. **Condition:** Optimizer and parameter state exceed per-device memory.

- Commonly applies [[02 Concepts/Lifecycle/Training & Adaptation/Activation Recomputation|Activation Recomputation]]. **Condition:** Activation memory limits sequence length or micro-batch size.

## Search Terms

Upstream search terms may be related terms rather than exact synonyms: Megatron-LM; DeepSpeed; distributed training library.

## Source

[Canonical Taxonomy](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/taxonomy.yml) · [Passage Alignment](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/mlsysbook-alignment.yml)

Taxonomy definitions and relationship wording: CC BY 4.0, with attribution to the Machine Learning Systems curriculum by Vijay Janapa Reddi and contributors. The textbook retains its separate license.
