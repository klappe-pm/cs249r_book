---
title: Activation Recomputation
type: concept
tags:
- Type/Concept
- Group/Lifecycle
- Topic/Training_Memory_State
source_repository: https://github.com/klappe-pm/cs249r_book
source_commit: de87c0103806d7bfb1c677dbb77a2b92fa00c298
source_path: taxonomy/taxonomy.yml
source_label: Activation recomputation
taxonomy_id: mlsys.activation-recompute
taxonomy_status: draft
taxonomy_version: 0.4-draft
---

# Activation Recomputation

Recreating forward intermediates during backward execution to reduce retained memory.

## Browsing Home

[[02 Concepts/Lifecycle/Training & Adaptation/Training Memory & State Subject|Training Memory & State]] → [[02 Concepts/Lifecycle/Training & Adaptation/Training & Adaptation Index|Training & Adaptation]]

## Book Passages

These are explicitly recorded related passages from the upstream draft alignment; they do not certify complete coverage.

- [[01 Books/Volume I - Foundations/02 Development/08 Model Training/V1-08.07 Pipeline Optimizations#^sec-model-training-gradient-accumulation-checkpointing-0c47|V1-08.07 Pipeline Optimizations]] — Activation checkpointing. [Exact Source Passage](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/books/vol1/08_training/08_training.qmd#L5142).

## Conditional Relationships

These are the taxonomy's draft editorial relationships. Read each relationship with its condition; an outgoing link is not a prerequisite claim.

- Reduces the peak [[02 Concepts/Foundations/Workloads & Requirements/Memory Footprint|Memory Footprint]]. **Condition:** Retained activations dominate training memory and spare compute is available to recompute them.

- Adds about one extra forward pass to [[02 Concepts/Qualities/Performance, Efficiency & Benchmarking/Execution Time|Execution Time]]. **Condition:** Holds for full recomputation; selective schemes recompute less.

- Is an alternative to [[02 Concepts/Lifecycle/Training & Adaptation/Training State Offloading|Training State Offloading]]. **Condition:** Both relieve accelerator memory; one spends compute, the other interconnect bandwidth.

- Lowers measured [[02 Concepts/Qualities/Performance, Efficiency & Benchmarking/Model FLOPS Utilization|Model FLOPS Utilization]]. **Condition:** Because recomputed FLOPs are excluded from MFU's model-required count, so MFU falls while hardware FLOPs utilization rises.

## Search Terms

Upstream search terms may be related terms rather than exact synonyms: Activation checkpointing; Gradient checkpointing.

## Source

[Canonical Taxonomy](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/taxonomy.yml) · [Passage Alignment](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/mlsysbook-alignment.yml)

Taxonomy definitions and relationship wording: CC BY 4.0, with attribution to the Machine Learning Systems curriculum by Vijay Janapa Reddi and contributors. The textbook retains its separate license.
