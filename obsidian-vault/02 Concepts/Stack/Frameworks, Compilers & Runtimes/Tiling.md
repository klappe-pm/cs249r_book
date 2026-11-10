---
title: Tiling
type: concept
tags:
- Type/Concept
- Group/Stack
- Topic/ML_Compilers_Kernel_Optimization
source_repository: https://github.com/klappe-pm/cs249r_book
source_commit: de87c0103806d7bfb1c677dbb77a2b92fa00c298
source_path: taxonomy/taxonomy.yml
source_label: Tiling
taxonomy_id: mlsys.tiling
taxonomy_status: draft
taxonomy_version: 0.4-draft
---

# Tiling

Partitioning computation so working data can be reused within a chosen storage level.

## Browsing Home

[[02 Concepts/Stack/Frameworks, Compilers & Runtimes/ML Compilers & Kernel Optimization Subject|ML Compilers & Kernel Optimization]] → [[02 Concepts/Stack/Frameworks, Compilers & Runtimes/Frameworks, Compilers & Runtimes Index|Frameworks, Compilers & Runtimes]]

## Book Passages

These are explicitly recorded related passages from the upstream draft alignment; they do not certify complete coverage.

- [[01 Books/Volume I - Foundations/03 Optimization/11 Hardware Acceleration/V1-11.08 Hardware Mapping#^sec-hardware-acceleration-tiling-fundamentals-e9e6|V1-11.08 Hardware Mapping]] — Tiling. [Exact Source Passage](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/books/vol1/11_hw_acceleration/11_hw_acceleration.qmd#L4935).

## Conditional Relationships

These are the taxonomy's draft editorial relationships. Read each relationship with its condition; an outgoing link is not a prerequisite claim.

- Improves [[02 Concepts/Foundations/Quantitative System Models/Data Locality|Data Locality]]. **Condition:** Tile size, storage capacity, and execution support constrain useful reuse.

## Source

[Canonical Taxonomy](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/taxonomy.yml) · [Passage Alignment](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/mlsysbook-alignment.yml)

Taxonomy definitions and relationship wording: CC BY 4.0, with attribution to the Machine Learning Systems curriculum by Vijay Janapa Reddi and contributors. The textbook retains its separate license.
