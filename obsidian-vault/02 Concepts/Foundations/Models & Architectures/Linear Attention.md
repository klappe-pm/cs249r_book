---
title: Linear Attention
type: concept
tags:
- Type/Concept
- Group/Foundations
- Topic/Long_Context_Efficient_Sequence_Models
source_repository: https://github.com/klappe-pm/cs249r_book
source_commit: de87c0103806d7bfb1c677dbb77a2b92fa00c298
source_path: taxonomy/taxonomy.yml
source_label: Linear attention
taxonomy_id: mlsys.linear-attention
taxonomy_status: draft
taxonomy_version: 0.4-draft
---

# Linear Attention

Attention reformulated with kernel feature maps so it is computed in linear time with a fixed-size recurrent state.

## Browsing Home

[[02 Concepts/Foundations/Models & Architectures/Long Context & Efficient Sequence Models Subject|Long Context & Efficient Sequence Models]] → [[02 Concepts/Foundations/Models & Architectures/Models & Architectures Index|Models & Architectures]]

## Book Passages

These are explicitly recorded related passages from the upstream draft alignment; they do not certify complete coverage.

No explicit passage alignment is recorded for this concept. Subject reading pointers are available in its browsing home.

## Conditional Relationships

These are the taxonomy's draft editorial relationships. Read each relationship with its condition; an outgoing link is not a prerequisite claim.

- Replaces with a fixed-size state [[02 Concepts/Lifecycle/Deployment & Serving/KV Cache|KV Cache]]. **Condition:** The attention kernel is approximated by a feature map that permits a recurrent formulation.

- Is a kernelized variant of [[02 Concepts/Foundations/Models & Architectures/Attention|Attention]]. **Condition:** Softmax similarity is replaced by a feature-map inner product, changing model quality.

- Is an alternative to [[02 Concepts/Foundations/Models & Architectures/Sparse and Sliding Window Attention|Sparse and Sliding Window Attention]]. **Condition:** Both reduce attention cost growth for long sequences, trading different quality losses.

## Source

[Canonical Taxonomy](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/taxonomy.yml) · [Passage Alignment](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/mlsysbook-alignment.yml)

Taxonomy definitions and relationship wording: CC BY 4.0, with attribution to the Machine Learning Systems curriculum by Vijay Janapa Reddi and contributors. The textbook retains its separate license.
