---
title: Kernel DSL
type: concept
tags:
- Type/Concept
- Group/Stack
- Topic/ML_Compilers_Kernel_Optimization
source_repository: https://github.com/klappe-pm/cs249r_book
source_commit: de87c0103806d7bfb1c677dbb77a2b92fa00c298
source_path: taxonomy/taxonomy.yml
source_label: Kernel DSL
taxonomy_id: mlsys.kernel-dsl
taxonomy_status: draft
taxonomy_version: 0.4-draft
---

# Kernel DSL

A domain-specific language for writing tiled tensor kernels above the level of vendor assembly, with the compiler handling memory and thread mapping.

## Browsing Home

[[02 Concepts/Stack/Frameworks, Compilers & Runtimes/ML Compilers & Kernel Optimization Subject|ML Compilers & Kernel Optimization]] → [[02 Concepts/Stack/Frameworks, Compilers & Runtimes/Frameworks, Compilers & Runtimes Index|Frameworks, Compilers & Runtimes]]

## Book Passages

These are explicitly recorded related passages from the upstream draft alignment; they do not certify complete coverage.

No explicit passage alignment is recorded for this concept. Subject reading pointers are available in its browsing home.

## Conditional Relationships

These are the taxonomy's draft editorial relationships. Read each relationship with its condition; an outgoing link is not a prerequisite claim.

- Is written in terms of [[02 Concepts/Stack/Frameworks, Compilers & Runtimes/Tiling|Tiling]]. **Condition:** Kernels are written in terms of blocks that the compiler maps to threads and memory.

- Lets the compiler manage [[02 Concepts/Stack/Hardware & Accelerators/On Chip SRAM and Scratchpads|On Chip SRAM and Scratchpads]]. **Condition:** Programs are written over blocks while the compiler allocates shared memory and registers.

- Enables custom [[02 Concepts/Stack/Frameworks, Compilers & Runtimes/Kernel Fusion|Kernel Fusion]]. **Condition:** Engineers can write a single kernel that combines operations no library provides fused.

## Search Terms

Upstream search terms may be related terms rather than exact synonyms: Triton.

## Source

[Canonical Taxonomy](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/taxonomy.yml) · [Passage Alignment](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/mlsysbook-alignment.yml)

Taxonomy definitions and relationship wording: CC BY 4.0, with attribution to the Machine Learning Systems curriculum by Vijay Janapa Reddi and contributors. The textbook retains its separate license.
