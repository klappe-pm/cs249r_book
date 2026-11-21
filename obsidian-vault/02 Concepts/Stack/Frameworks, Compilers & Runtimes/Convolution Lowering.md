---
title: Convolution Lowering
type: concept
tags:
- Type/Concept
- Group/Stack
- Topic/Tensor_Operators_Memory_Layout
source_repository: https://github.com/klappe-pm/cs249r_book
source_commit: de87c0103806d7bfb1c677dbb77a2b92fa00c298
source_path: taxonomy/taxonomy.yml
source_label: Convolution lowering
taxonomy_id: mlsys.convolution-lowering
taxonomy_status: draft
taxonomy_version: 0.4-draft
---

# Convolution Lowering

Implementing convolution by rearranging input patches into matrices for GEMM, or by direct, FFT, or Winograd algorithms with different memory costs.

## Browsing Home

[[02 Concepts/Stack/Frameworks, Compilers & Runtimes/Tensor Operators & Memory Layout Subject|Tensor Operators & Memory Layout]] → [[02 Concepts/Stack/Frameworks, Compilers & Runtimes/Frameworks, Compilers & Runtimes Index|Frameworks, Compilers & Runtimes]]

## Book Passages

These are explicitly recorded related passages from the upstream draft alignment; they do not certify complete coverage.

No explicit passage alignment is recorded for this concept. Subject reading pointers are available in its browsing home.

## Conditional Relationships

These are the taxonomy's draft editorial relationships. Read each relationship with its condition; an outgoing link is not a prerequisite claim.

- Maps convolution onto [[02 Concepts/Stack/Frameworks, Compilers & Runtimes/Matrix Multiplication|Matrix Multiplication]]. **Condition:** The im2col-style transformation is used, at the cost of duplicated input data.

- Implements [[02 Concepts/Foundations/Models & Architectures/Convolution|Convolution]]. **Condition:** A lowering algorithm is chosen per layer shape.

- Can increase, through duplicated patches, [[02 Concepts/Foundations/Workloads & Requirements/Memory Footprint|Memory Footprint]]. **Condition:** im2col-style lowering copies overlapping input patches into a larger matrix.

## Search Terms

Upstream search terms may be related terms rather than exact synonyms: im2col.

## Source

[Canonical Taxonomy](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/taxonomy.yml) · [Passage Alignment](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/mlsysbook-alignment.yml)

Taxonomy definitions and relationship wording: CC BY 4.0, with attribution to the Machine Learning Systems curriculum by Vijay Janapa Reddi and contributors. The textbook retains its separate license.
