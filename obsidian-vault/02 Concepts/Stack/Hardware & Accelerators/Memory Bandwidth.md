---
title: Memory Bandwidth
type: concept
tags:
- Type/Concept
- Group/Stack
- Topic/Memory_Hierarchy_Bandwidth
source_repository: https://github.com/klappe-pm/cs249r_book
source_commit: de87c0103806d7bfb1c677dbb77a2b92fa00c298
source_path: taxonomy/taxonomy.yml
source_label: Memory bandwidth
taxonomy_id: mlsys.memory-bandwidth
taxonomy_status: draft
taxonomy_version: 0.4-draft
---

# Memory Bandwidth

The sustainable rate at which bytes move across a specified memory interface.

## Browsing Home

[[02 Concepts/Stack/Hardware & Accelerators/Memory Hierarchy & Bandwidth Subject|Memory Hierarchy & Bandwidth]] → [[02 Concepts/Stack/Hardware & Accelerators/Hardware & Accelerators Index|Hardware & Accelerators]]

## Book Passages

These are explicitly recorded related passages from the upstream draft alignment; they do not certify complete coverage.

- [[01 Books/Volume I - Foundations/03 Optimization/11 Hardware Acceleration/V1-11.07 Performance Bounds#^sec-hardware-acceleration-calculating-memory-bandwidth-bounds-7fc0|V1-11.07 Performance Bounds]] — Memory bandwidth. [Exact Source Passage](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/books/vol1/11_hw_acceleration/11_hw_acceleration.qmd#L3735).

- [[01 Books/Volume IV - Physical AI/01 Machine Anatomy/03 The Cognitive Brain/V4-03.05 The Cost of a Fresh Evaluation#^sec-brain-memory-wall|V4-03.05 The Cost of a Fresh Evaluation]] — Weight bandwidth. [Exact Source Passage](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/books/vol4/03_brain/03_brain.qmd#L637).

## Conditional Relationships

These are the taxonomy's draft editorial relationships. Read each relationship with its condition; an outgoing link is not a prerequisite claim.

- Sets the sloped ceiling of [[02 Concepts/Foundations/Quantitative System Models/Roofline Bound|Roofline Bound]]. **Condition:** The bandwidth must correspond to the memory boundary used for arithmetic intensity.

- Bounds the decode phase of [[02 Concepts/Lifecycle/Deployment & Serving/Prefill and Decode|Prefill and Decode]]. **Condition:** The dominant resource depends on architecture, batch, context length, and implementation.

- Bounds [[02 Concepts/Lifecycle/Deployment & Serving/Time per Output Token|Time per Output Token]]. **Condition:** Holds in decode at small batch, where each step reads weights and KV cache with low arithmetic intensity.

- Caps the weight-fetch rate of [[02 Concepts/Stack/Hardware & Accelerators/Execute in Place Weights|Execute in Place Weights]]. **Condition:** Flash read bandwidth and wait states bound execute-in-place inference when operators reuse weights little.

## Themes

- [[03 Themes/Memory and Bandwidth|Memory and Bandwidth]]

## Source

[Canonical Taxonomy](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/taxonomy.yml) · [Passage Alignment](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/mlsysbook-alignment.yml)

Taxonomy definitions and relationship wording: CC BY 4.0, with attribution to the Machine Learning Systems curriculum by Vijay Janapa Reddi and contributors. The textbook retains its separate license.
