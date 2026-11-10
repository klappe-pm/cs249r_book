---
title: Dynamic Sparse Attention
type: concept
tags:
- Type/Concept
- Group/Foundations
- Topic/Long_Context_Efficient_Sequence_Models
source_repository: https://github.com/klappe-pm/cs249r_book
source_commit: de87c0103806d7bfb1c677dbb77a2b92fa00c298
source_path: taxonomy/taxonomy.yml
source_label: Dynamic sparse attention
taxonomy_id: mlsys.dynamic-sparse-attention
taxonomy_status: draft
taxonomy_version: 0.4-draft
---

# Dynamic Sparse Attention

Attention that computes only the query-key blocks predicted important for each input at runtime, rather than a fixed pattern, to cut long-context cost.

## Browsing Home

[[02 Concepts/Foundations/Models & Architectures/Long Context & Efficient Sequence Models Subject|Long Context & Efficient Sequence Models]] → [[02 Concepts/Foundations/Models & Architectures/Models & Architectures Index|Models & Architectures]]

## Book Passages

These are explicitly recorded related passages from the upstream draft alignment; they do not certify complete coverage.

No explicit passage alignment is recorded for this concept. Subject reading pointers are available in its browsing home.

## Conditional Relationships

These are the taxonomy's draft editorial relationships. Read each relationship with its condition; an outgoing link is not a prerequisite claim.

- Is a runtime-sparsified form of [[02 Concepts/Foundations/Models & Architectures/Attention|Attention]]. **Condition:** Only predicted-important query-key blocks are computed.

- Replaces fixed sparsity patterns of [[02 Concepts/Foundations/Models & Architectures/Sparse and Sliding Window Attention|Sparse and Sliding Window Attention]]. **Condition:** Sparsity is chosen per input rather than fixed in advance.

- Shortens long-prompt [[02 Concepts/Lifecycle/Deployment & Serving/Time to First Token|Time to First Token]]. **Condition:** Prefill attention over long contexts dominates first-token latency.

## Search Terms

Upstream search terms may be related terms rather than exact synonyms: content-adaptive sparse attention; input-dependent sparse attention.

## Source

[Canonical Taxonomy](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/taxonomy.yml) · [Passage Alignment](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/mlsysbook-alignment.yml)

Taxonomy definitions and relationship wording: CC BY 4.0, with attribution to the Machine Learning Systems curriculum by Vijay Janapa Reddi and contributors. The textbook retains its separate license.
