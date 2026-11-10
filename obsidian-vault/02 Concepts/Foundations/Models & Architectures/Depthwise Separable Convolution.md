---
title: Depthwise Separable Convolution
type: concept
tags:
- Type/Concept
- Group/Foundations
- Topic/Architecture_Building_Blocks
source_repository: https://github.com/klappe-pm/cs249r_book
source_commit: de87c0103806d7bfb1c677dbb77a2b92fa00c298
source_path: taxonomy/taxonomy.yml
source_label: Depthwise separable convolution
taxonomy_id: mlsys.depthwise-separable-convolution
taxonomy_status: draft
taxonomy_version: 0.4-draft
---

# Depthwise Separable Convolution

Factoring a standard convolution into a per-channel spatial convolution followed by a pointwise convolution, reducing operations and parameters.

## Browsing Home

[[02 Concepts/Foundations/Models & Architectures/Architecture Building Blocks Subject|Architecture Building Blocks]] → [[02 Concepts/Foundations/Models & Architectures/Models & Architectures Index|Models & Architectures]]

## Book Passages

These are explicitly recorded related passages from the upstream draft alignment; they do not certify complete coverage.

No explicit passage alignment is recorded for this concept. Subject reading pointers are available in its browsing home.

## Conditional Relationships

These are the taxonomy's draft editorial relationships. Read each relationship with its condition; an outgoing link is not a prerequisite claim.

- Lowers [[02 Concepts/Foundations/Quantitative System Models/Arithmetic Intensity|Arithmetic Intensity]]. **Condition:** Fewer operations per output come with less data reuse, so memory-bound depthwise layers may not speed up in proportion to the FLOP reduction.

- Is a factorized kind of [[02 Concepts/Foundations/Models & Architectures/Convolution|Convolution]]. **Condition:** A standard convolution is split into depthwise and pointwise steps.

- Cuts parameter storage in [[02 Concepts/Foundations/Workloads & Requirements/Memory Footprint|Memory Footprint]]. **Condition:** Parameter memory is a significant share of the deployed footprint, as on mobile and embedded targets.

## Source

[Canonical Taxonomy](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/taxonomy.yml) · [Passage Alignment](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/mlsysbook-alignment.yml)

Taxonomy definitions and relationship wording: CC BY 4.0, with attribution to the Machine Learning Systems curriculum by Vijay Janapa Reddi and contributors. The textbook retains its separate license.
