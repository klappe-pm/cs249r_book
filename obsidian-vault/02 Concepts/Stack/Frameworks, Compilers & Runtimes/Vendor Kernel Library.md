---
title: Vendor Kernel Library
type: concept
tags:
- Type/Concept
- Group/Stack
- Topic/Tensor_Operators_Memory_Layout
source_repository: https://github.com/klappe-pm/cs249r_book
source_commit: de87c0103806d7bfb1c677dbb77a2b92fa00c298
source_path: taxonomy/taxonomy.yml
source_label: Vendor kernel library
taxonomy_id: mlsys.kernel-library
taxonomy_status: draft
taxonomy_version: 0.4-draft
---

# Vendor Kernel Library

Tuned implementations of common operators supplied for a hardware platform, which frameworks call rather than generating their own kernels.

## Browsing Home

[[02 Concepts/Stack/Frameworks, Compilers & Runtimes/Tensor Operators & Memory Layout Subject|Tensor Operators & Memory Layout]] → [[02 Concepts/Stack/Frameworks, Compilers & Runtimes/Frameworks, Compilers & Runtimes Index|Frameworks, Compilers & Runtimes]]

## Book Passages

These are explicitly recorded related passages from the upstream draft alignment; they do not certify complete coverage.

No explicit passage alignment is recorded for this concept. Subject reading pointers are available in its browsing home.

## Conditional Relationships

These are the taxonomy's draft editorial relationships. Read each relationship with its condition; an outgoing link is not a prerequisite claim.

- Can limit opportunities for [[02 Concepts/Stack/Frameworks, Compilers & Runtimes/Kernel Fusion|Kernel Fusion]]. **Condition:** Library calls are opaque to the compiler and cannot be fused with neighbors.

- Provides tuned [[02 Concepts/Stack/Frameworks, Compilers & Runtimes/Matrix Multiplication|Matrix Multiplication]]. **Condition:** Vendor libraries supply GEMM and convolution kernels selected per shape and precision.

- Is an alternative to [[02 Concepts/Stack/Frameworks, Compilers & Runtimes/Kernel DSL|Kernel DSL]]. **Condition:** Both supply operator kernels; libraries cover common shapes, DSLs let engineers write fused or novel kernels.

## Search Terms

Upstream search terms may be related terms rather than exact synonyms: cuBLAS; cuDNN.

## Source

[Canonical Taxonomy](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/taxonomy.yml) · [Passage Alignment](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/mlsysbook-alignment.yml)

Taxonomy definitions and relationship wording: CC BY 4.0, with attribution to the Machine Learning Systems curriculum by Vijay Janapa Reddi and contributors. The textbook retains its separate license.
