---
title: Sparse Tensor Kernels
type: concept
tags:
- Type/Concept
- Group/Stack
- Topic/Tensor_Operators_Memory_Layout
source_repository: https://github.com/klappe-pm/cs249r_book
source_commit: de87c0103806d7bfb1c677dbb77a2b92fa00c298
source_path: taxonomy/taxonomy.yml
source_label: Sparse tensor kernels
taxonomy_id: mlsys.sparse-tensor-kernels
taxonomy_status: draft
taxonomy_version: 0.4-draft
---

# Sparse Tensor Kernels

Kernels such as sparse-dense matrix multiply, sampled dense-dense multiply, and sparse convolution that compute over compressed nonzero structure, trading irregular access for skipped work.

## Browsing Home

[[02 Concepts/Stack/Frameworks, Compilers & Runtimes/Tensor Operators & Memory Layout Subject|Tensor Operators & Memory Layout]] → [[02 Concepts/Stack/Frameworks, Compilers & Runtimes/Frameworks, Compilers & Runtimes Index|Frameworks, Compilers & Runtimes]]

## Book Passages

These are explicitly recorded related passages from the upstream draft alignment; they do not certify complete coverage.

No explicit passage alignment is recorded for this concept. Subject reading pointers are available in its browsing home.

## Conditional Relationships

These are the taxonomy's draft editorial relationships. Read each relationship with its condition; an outgoing link is not a prerequisite claim.

- Stores nonzeros in compressed formats described by [[02 Concepts/Stack/Frameworks, Compilers & Runtimes/Tensor Layout|Tensor Layout]]. **Condition:** Nonzeros are kept in formats such as CSR or coordinate lists.

- Operates on operands stored in [[02 Concepts/Stack/Frameworks, Compilers & Runtimes/Sparse and Ragged Tensor Representation|Sparse and Ragged Tensor Representation]]. **Condition:** Kernels read compressed index structures rather than dense arrays.

- Scatter-adds irregular contributions through [[02 Concepts/Stack/Frameworks, Compilers & Runtimes/Kernel Synchronization and Atomics|Kernel Synchronization and Atomics]]. **Condition:** When several threads contribute to the same output element.

## Search Terms

Upstream search terms may be related terms rather than exact synonyms: SpMM; SDDMM; sparse convolution.

## Source

[Canonical Taxonomy](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/taxonomy.yml) · [Passage Alignment](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/mlsysbook-alignment.yml)

Taxonomy definitions and relationship wording: CC BY 4.0, with attribution to the Machine Learning Systems curriculum by Vijay Janapa Reddi and contributors. The textbook retains its separate license.
