---
title: Transformer
type: concept
tags:
- Type/Concept
- Group/Foundations
- Topic/Model_Families
source_repository: https://github.com/klappe-pm/cs249r_book
source_commit: de87c0103806d7bfb1c677dbb77a2b92fa00c298
source_path: taxonomy/taxonomy.yml
source_label: Transformer
taxonomy_id: mlsys.transformer
taxonomy_status: draft
taxonomy_version: 0.4-draft
---

# Transformer

A neural architecture of stacked attention and feed-forward blocks with residual connections and normalization, processing all sequence positions in parallel during training.

## Browsing Home

[[02 Concepts/Foundations/Models & Architectures/Model Families Subject|Model Families]] → [[02 Concepts/Foundations/Models & Architectures/Models & Architectures Index|Models & Architectures]]

## Book Passages

These are explicitly recorded related passages from the upstream draft alignment; they do not certify complete coverage.

No explicit passage alignment is recorded for this concept. Subject reading pointers are available in its browsing home.

## Conditional Relationships

These are the taxonomy's draft editorial relationships. Read each relationship with its condition; an outgoing link is not a prerequisite claim.

- Is built from [[02 Concepts/Foundations/Models & Architectures/Attention|Attention]]. **Condition:** The architecture uses attention layers interleaved with feed-forward blocks.

- Stabilizes residual blocks with [[02 Concepts/Foundations/Models & Architectures/Normalization Layers|Normalization Layers]]. **Condition:** Each block applies layer or RMS normalization around attention and feed-forward sublayers.

- Injects order with [[02 Concepts/Foundations/Models & Architectures/Position Encoding|Position Encoding]]. **Condition:** Attention alone is permutation equivariant, so the architecture adds absolute, relative, or rotary positions.

- Is a kind of [[02 Concepts/Foundations/Models & Architectures/Neural Networks|Neural Networks]]. **Condition:** The architecture is a differentiable composition trained by gradient descent.

- Develops, at scale, [[02 Concepts/Qualities/Performance, Efficiency & Benchmarking/Activation Outliers|Activation Outliers]]. **Condition:** In large transformers, roughly beyond a few billion parameters, where a few hidden dimensions carry systematic large-magnitude activations.

## Source

[Canonical Taxonomy](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/taxonomy.yml) · [Passage Alignment](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/mlsysbook-alignment.yml)

Taxonomy definitions and relationship wording: CC BY 4.0, with attribution to the Machine Learning Systems curriculum by Vijay Janapa Reddi and contributors. The textbook retains its separate license.
