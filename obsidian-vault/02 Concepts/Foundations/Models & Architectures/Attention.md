---
title: Attention
type: concept
tags:
- Type/Concept
- Group/Foundations
- Topic/Architecture_Building_Blocks
source_repository: https://github.com/klappe-pm/cs249r_book
source_commit: de87c0103806d7bfb1c677dbb77a2b92fa00c298
source_path: taxonomy/taxonomy.yml
source_label: Attention
taxonomy_id: mlsys.attention
taxonomy_status: draft
taxonomy_version: 0.4-draft
---

# Attention

Input-dependent aggregation of value vectors using query-key compatibility scores.

## Browsing Home

[[02 Concepts/Foundations/Models & Architectures/Architecture Building Blocks Subject|Architecture Building Blocks]] → [[02 Concepts/Foundations/Models & Architectures/Models & Architectures Index|Models & Architectures]]

## Book Passages

These are explicitly recorded related passages from the upstream draft alignment; they do not certify complete coverage.

- [[01 Books/Volume I - Foundations/02 Development/06 Network Architectures/V1-06.02 Architectural Principles#^sec-network-architectures-architectural-principles-engineering-tradeoffs-362e|V1-06.02 Architectural Principles]] — Self-attention. [Exact Source Passage](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/books/vol1/06_nn_architectures/06_nn_architectures.qmd#L67).

## Conditional Relationships

These are the taxonomy's draft editorial relationships. Read each relationship with its condition; an outgoing link is not a prerequisite claim.

- Gains sequence-order sensitivity from [[02 Concepts/Foundations/Models & Architectures/Position Encoding|Position Encoding]]. **Condition:** Attention without another position-sensitive mechanism is permutation equivariant.

- Reuses history through [[02 Concepts/Lifecycle/Deployment & Serving/KV Cache|KV Cache]]. **Condition:** For compatible autoregressive attention architectures.

## Search Terms

Upstream search terms may be related terms rather than exact synonyms: self-attention; multi-head attention; cross-attention; scaled dot-product attention.

## Source

[Canonical Taxonomy](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/taxonomy.yml) · [Passage Alignment](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/mlsysbook-alignment.yml)

Taxonomy definitions and relationship wording: CC BY 4.0, with attribution to the Machine Learning Systems curriculum by Vijay Janapa Reddi and contributors. The textbook retains its separate license.
