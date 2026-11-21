---
title: IO Aware Attention Kernel
type: concept
tags:
- Type/Concept
- Group/Stack
- Topic/Tensor_Operators_Memory_Layout
source_repository: https://github.com/klappe-pm/cs249r_book
source_commit: de87c0103806d7bfb1c677dbb77a2b92fa00c298
source_path: taxonomy/taxonomy.yml
source_label: IO-aware attention kernel
taxonomy_id: mlsys.io-aware-attention
taxonomy_status: draft
taxonomy_version: 0.4-draft
---

# IO Aware Attention Kernel

An exact attention implementation that tiles queries, keys, and values through on-chip memory to avoid materializing the full score matrix in off-chip memory.

## Browsing Home

[[02 Concepts/Stack/Frameworks, Compilers & Runtimes/Tensor Operators & Memory Layout Subject|Tensor Operators & Memory Layout]] → [[02 Concepts/Stack/Frameworks, Compilers & Runtimes/Frameworks, Compilers & Runtimes Index|Frameworks, Compilers & Runtimes]]

## Book Passages

These are explicitly recorded related passages from the upstream draft alignment; they do not certify complete coverage.

No explicit passage alignment is recorded for this concept. Subject reading pointers are available in its browsing home.

## Conditional Relationships

These are the taxonomy's draft editorial relationships. Read each relationship with its condition; an outgoing link is not a prerequisite claim.

- Depends on the capacity of [[02 Concepts/Stack/Hardware & Accelerators/On Chip SRAM and Scratchpads|On Chip SRAM and Scratchpads]]. **Condition:** Tile sizes are chosen to fit on-chip memory.

- Exactly computes [[02 Concepts/Foundations/Models & Architectures/Attention|Attention]]. **Condition:** The result matches standard softmax attention up to floating-point reordering.

- Is built on [[02 Concepts/Stack/Frameworks, Compilers & Runtimes/Tiling|Tiling]]. **Condition:** Query, key, and value blocks are staged through on-chip memory with an online softmax.

- Keeps attention tiles resident on chip to improve [[02 Concepts/Foundations/Quantitative System Models/Data Locality|Data Locality]]. **Condition:** Requires on-chip storage large enough for the chosen tile and an exact tiled formulation.

## Themes

- [[03 Themes/Memory and Bandwidth|Memory and Bandwidth]]

## Search Terms

Upstream search terms may be related terms rather than exact synonyms: FlashAttention.

## Source

[Canonical Taxonomy](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/taxonomy.yml) · [Passage Alignment](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/mlsysbook-alignment.yml)

Taxonomy definitions and relationship wording: CC BY 4.0, with attribution to the Machine Learning Systems curriculum by Vijay Janapa Reddi and contributors. The textbook retains its separate license.
