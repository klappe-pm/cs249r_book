---
title: Sparse and Ragged Tensor Representation
type: concept
tags:
- Type/Concept
- Group/Stack
- Topic/Tensor_Operators_Memory_Layout
source_repository: https://github.com/klappe-pm/cs249r_book
source_commit: de87c0103806d7bfb1c677dbb77a2b92fa00c298
source_path: taxonomy/taxonomy.yml
source_label: Sparse and ragged tensor representation
taxonomy_id: mlsys.sparse-ragged-tensors
taxonomy_status: draft
taxonomy_version: 0.4-draft
---

# Sparse and Ragged Tensor Representation

Storing tensors with mostly zero entries or variable-length dimensions in compressed formats such as COO, CSR, or offset-indexed ragged layouts instead of padded dense arrays.

## Browsing Home

[[02 Concepts/Stack/Frameworks, Compilers & Runtimes/Tensor Operators & Memory Layout Subject|Tensor Operators & Memory Layout]] → [[02 Concepts/Stack/Frameworks, Compilers & Runtimes/Frameworks, Compilers & Runtimes Index|Frameworks, Compilers & Runtimes]]

## Book Passages

These are explicitly recorded related passages from the upstream draft alignment; they do not certify complete coverage.

No explicit passage alignment is recorded for this concept. Subject reading pointers are available in its browsing home.

## Conditional Relationships

These are the taxonomy's draft editorial relationships. Read each relationship with its condition; an outgoing link is not a prerequisite claim.

- Is a compressed form of [[02 Concepts/Stack/Frameworks, Compilers & Runtimes/Tensor Layout|Tensor Layout]]. **Condition:** Storage records only nonzero entries or actual sequence extents.

- Shrinks [[02 Concepts/Foundations/Workloads & Requirements/Memory Footprint|Memory Footprint]]. **Condition:** Density is low or lengths vary widely, so padding would dominate storage.

## Search Terms

Upstream search terms may be related terms rather than exact synonyms: ragged tensor; nested tensor; jagged tensor; CSR format.

## Source

[Canonical Taxonomy](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/taxonomy.yml) · [Passage Alignment](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/mlsysbook-alignment.yml)

Taxonomy definitions and relationship wording: CC BY 4.0, with attribution to the Machine Learning Systems curriculum by Vijay Janapa Reddi and contributors. The textbook retains its separate license.
