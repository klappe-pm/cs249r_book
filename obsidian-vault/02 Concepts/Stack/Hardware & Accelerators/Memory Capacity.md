---
title: Memory Capacity
type: concept
tags:
- Type/Concept
- Group/Stack
- Topic/Memory_Hierarchy_Bandwidth
source_repository: https://github.com/klappe-pm/cs249r_book
source_commit: de87c0103806d7bfb1c677dbb77a2b92fa00c298
source_path: taxonomy/taxonomy.yml
source_label: Memory capacity
taxonomy_id: mlsys.memory-capacity
taxonomy_status: draft
taxonomy_version: 0.4-draft
---

# Memory Capacity

Available storage for concurrently resident state and intermediates.

## Browsing Home

[[02 Concepts/Stack/Hardware & Accelerators/Memory Hierarchy & Bandwidth Subject|Memory Hierarchy & Bandwidth]] → [[02 Concepts/Stack/Hardware & Accelerators/Hardware & Accelerators Index|Hardware & Accelerators]]

## Book Passages

These are explicitly recorded related passages from the upstream draft alignment; they do not certify complete coverage.

- [[01 Books/Volume I - Foundations/01 Foundations/02 System Paradigms/V1-02.02 Four Deployment Regimes Across Nine Orders of Magnitude#^sec-ml-systems-deployment-paradigm-framework-0d25|V1-02.02 Four Deployment Regimes Across Nine Orders of Magnitude]] — Memory capacity. [Exact Source Passage](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/books/vol1/02_system_paradigms/02_system_paradigms.qmd#L67).

- [[01 Books/Volume II - Scaling/01 The Fleet/02 Compute Infrastructure/V2-02.04 The Memory Wall#^sec-compute-memory-wall|V2-02.04 The Memory Wall]] — Memory capacity. [Exact Source Passage](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/books/vol2/02_compute_infrastructure/02_compute_infrastructure.qmd#L1040).

## Conditional Relationships

These are the taxonomy's draft editorial relationships. Read each relationship with its condition; an outgoing link is not a prerequisite claim.

- Limits the per-device [[02 Concepts/Lifecycle/Training & Adaptation/Training Batch Size|Training Batch Size]]. **Condition:** Activation and workspace demand depend on execution and accumulation choices.

- Limits the per-device [[02 Concepts/Lifecycle/Training & Adaptation/Training State|Training State]]. **Condition:** Count resident parameters, gradients, optimizer state, and other retained data separately.

- Limits the resident [[02 Concepts/Lifecycle/Deployment & Serving/KV Cache|KV Cache]]. **Condition:** Size depends on architecture, sequence length, format, and concurrency.

- Limits feasible [[02 Concepts/Lifecycle/Deployment & Serving/Request Batching|Request Batching]]. **Condition:** Model state, request state, intermediates, and allocator overhead must fit for the selected execution strategy.

- Caps [[02 Concepts/Foundations/Workloads & Requirements/Memory Footprint|Memory Footprint]]. **Condition:** All resident state is counted at its peak, including runtime buffers.

- Constrains [[02 Concepts/Lifecycle/Training & Adaptation/On Device Training|On Device Training]]. **Condition:** Holds on devices whose memory cannot hold full activations and optimizer state, forcing sparse or partial updates.

- Constrains [[02 Concepts/Lifecycle/Deployment & Serving/On Device Inference Runtime|On Device Inference Runtime]]. **Condition:** Holds on microcontrollers and mobile devices where weights, activations, and runtime must fit in limited RAM and flash.

## Themes

- [[03 Themes/Constraints Drive Architecture|Constraints Drive Architecture]]
- [[03 Themes/Memory and Bandwidth|Memory and Bandwidth]]

## Source

[Canonical Taxonomy](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/taxonomy.yml) · [Passage Alignment](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/mlsysbook-alignment.yml)

Taxonomy definitions and relationship wording: CC BY 4.0, with attribution to the Machine Learning Systems curriculum by Vijay Janapa Reddi and contributors. The textbook retains its separate license.
