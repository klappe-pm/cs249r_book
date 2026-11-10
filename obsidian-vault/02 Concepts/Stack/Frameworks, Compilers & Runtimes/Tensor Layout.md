---
title: Tensor Layout
type: concept
tags:
- Type/Concept
- Group/Stack
- Topic/Tensor_Operators_Memory_Layout
source_repository: https://github.com/klappe-pm/cs249r_book
source_commit: de87c0103806d7bfb1c677dbb77a2b92fa00c298
source_path: taxonomy/taxonomy.yml
source_label: Tensor layout
taxonomy_id: mlsys.tensor-layout
taxonomy_status: draft
taxonomy_version: 0.4-draft
---

# Tensor Layout

The mapping from tensor indices to storage locations, including strides and materialization.

## Browsing Home

[[02 Concepts/Stack/Frameworks, Compilers & Runtimes/Tensor Operators & Memory Layout Subject|Tensor Operators & Memory Layout]] → [[02 Concepts/Stack/Frameworks, Compilers & Runtimes/Frameworks, Compilers & Runtimes Index|Frameworks, Compilers & Runtimes]]

## Book Passages

These are explicitly recorded related passages from the upstream draft alignment; they do not certify complete coverage.

No explicit passage alignment is recorded for this concept. Subject reading pointers are available in its browsing home.

## Conditional Relationships

These are the taxonomy's draft editorial relationships. Read each relationship with its condition; an outgoing link is not a prerequisite claim.

- Sets the data-movement cost of [[02 Concepts/Stack/Frameworks, Compilers & Runtimes/Matrix Multiplication|Matrix Multiplication]]. **Condition:** Views and physical copies have different costs; kernels support particular layouts.

- Is metadata carried by [[02 Concepts/Stack/Frameworks, Compilers & Runtimes/Tensor|Tensor]]. **Condition:** The framework records strides or format metadata with each tensor.

- Determines whether accesses achieve [[02 Concepts/Stack/Frameworks, Compilers & Runtimes/Memory Coalescing|Memory Coalescing]]. **Condition:** Strides decide whether adjacent threads touch adjacent addresses.

## Search Terms

Upstream search terms may be related terms rather than exact synonyms: memory alignment; alignment padding.

## Source

[Canonical Taxonomy](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/taxonomy.yml) · [Passage Alignment](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/mlsysbook-alignment.yml)

Taxonomy definitions and relationship wording: CC BY 4.0, with attribution to the Machine Learning Systems curriculum by Vijay Janapa Reddi and contributors. The textbook retains its separate license.
