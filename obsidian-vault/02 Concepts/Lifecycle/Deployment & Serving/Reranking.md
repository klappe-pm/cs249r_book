---
title: Reranking
type: concept
tags:
- Type/Concept
- Group/Lifecycle
- Topic/Retrieval_Vector_Search
source_repository: https://github.com/klappe-pm/cs249r_book
source_commit: de87c0103806d7bfb1c677dbb77a2b92fa00c298
source_path: taxonomy/taxonomy.yml
source_label: Reranking
taxonomy_id: mlsys.reranking
taxonomy_status: draft
taxonomy_version: 0.4-draft
---

# Reranking

Reordering a retrieved candidate set with a more expensive relevance model before use.

## Browsing Home

[[02 Concepts/Lifecycle/Deployment & Serving/Retrieval & Vector Search Subject|Retrieval & Vector Search]] → [[02 Concepts/Lifecycle/Deployment & Serving/Deployment & Serving Index|Deployment & Serving]]

## Book Passages

These are explicitly recorded related passages from the upstream draft alignment; they do not certify complete coverage.

No explicit passage alignment is recorded for this concept. Subject reading pointers are available in its browsing home.

## Conditional Relationships

These are the taxonomy's draft editorial relationships. Read each relationship with its condition; an outgoing link is not a prerequisite claim.

- Is the precision stage of [[02 Concepts/Lifecycle/Deployment & Serving/Retrieval|Retrieval]]. **Condition:** Holds when first-stage recall is adequate and reranker cost fits the latency budget.

- Mitigates position effects behind [[02 Concepts/Foundations/Models & Architectures/Long Context Degradation|Long Context Degradation]]. **Condition:** Reranked evidence is placed where models use it best, near the start or end of the context.

- Is a late stage of [[02 Concepts/Lifecycle/Deployment & Serving/Multi Stage Retrieval and Ranking|Multi Stage Retrieval and Ranking]]. **Condition:** Holds when a cheap candidate stage precedes a costlier scoring model under one latency budget.

- Commonly uses cross-encoder [[02 Concepts/Foundations/Models & Architectures/Transformer|Transformer]]. **Condition:** Applies to neural rerankers that jointly encode query and candidate.

## Source

[Canonical Taxonomy](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/taxonomy.yml) · [Passage Alignment](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/mlsysbook-alignment.yml)

Taxonomy definitions and relationship wording: CC BY 4.0, with attribution to the Machine Learning Systems curriculum by Vijay Janapa Reddi and contributors. The textbook retains its separate license.
