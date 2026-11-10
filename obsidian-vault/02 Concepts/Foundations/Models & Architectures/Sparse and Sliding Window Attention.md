---
title: Sparse and Sliding Window Attention
type: concept
tags:
- Type/Concept
- Group/Foundations
- Topic/Long_Context_Efficient_Sequence_Models
source_repository: https://github.com/klappe-pm/cs249r_book
source_commit: de87c0103806d7bfb1c677dbb77a2b92fa00c298
source_path: taxonomy/taxonomy.yml
source_label: Sparse and sliding-window attention
taxonomy_id: mlsys.sliding-window-attention
taxonomy_status: draft
taxonomy_version: 0.4-draft
---

# Sparse and Sliding Window Attention

Attention restricted to local windows or predetermined sparse patterns, reducing attended query-key pairs; cost is linear in sequence length when the attended positions per query remain bounded.

## Browsing Home

[[02 Concepts/Foundations/Models & Architectures/Long Context & Efficient Sequence Models Subject|Long Context & Efficient Sequence Models]] → [[02 Concepts/Foundations/Models & Architectures/Models & Architectures Index|Models & Architectures]]

## Book Passages

These are explicitly recorded related passages from the upstream draft alignment; they do not certify complete coverage.

No explicit passage alignment is recorded for this concept. Subject reading pointers are available in its browsing home.

## Conditional Relationships

These are the taxonomy's draft editorial relationships. Read each relationship with its condition; an outgoing link is not a prerequisite claim.

- Makes longer contexts more affordable by reducing attention cost over [[02 Concepts/Foundations/Models & Architectures/Context Window|Context Window]]. **Condition:** The attention pattern reduces attended query-key pairs relative to dense attention; linear cost requires bounded attended positions per query, and quality on long-range tasks may change.

- Is a restricted kind of [[02 Concepts/Foundations/Models & Architectures/Attention|Attention]]. **Condition:** Each position attends only within a window or fixed sparse pattern.

- Caps the size of [[02 Concepts/Lifecycle/Deployment & Serving/KV Cache|KV Cache]]. **Condition:** During decoding only the most recent window of keys and values must be retained.

## Search Terms

Upstream search terms may be related terms rather than exact synonyms: local attention.

## Source

[Canonical Taxonomy](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/taxonomy.yml) · [Passage Alignment](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/mlsysbook-alignment.yml)

Taxonomy definitions and relationship wording: CC BY 4.0, with attribution to the Machine Learning Systems curriculum by Vijay Janapa Reddi and contributors. The textbook retains its separate license.
