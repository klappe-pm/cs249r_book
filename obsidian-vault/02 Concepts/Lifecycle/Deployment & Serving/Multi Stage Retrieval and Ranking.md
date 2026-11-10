---
title: Multi Stage Retrieval and Ranking
type: concept
tags:
- Type/Concept
- Group/Lifecycle
- Topic/Serving_Architectures
source_repository: https://github.com/klappe-pm/cs249r_book
source_commit: de87c0103806d7bfb1c677dbb77a2b92fa00c298
source_path: taxonomy/taxonomy.yml
source_label: Multi-stage retrieval and ranking
taxonomy_id: mlsys.ranking-funnel
taxonomy_status: draft
taxonomy_version: 0.4-draft
---

# Multi Stage Retrieval and Ranking

Candidate generation followed by progressively costlier ranking stages under one latency budget, the dominant architecture for recommendation and search.

## Browsing Home

[[02 Concepts/Lifecycle/Deployment & Serving/Serving Architectures Subject|Serving Architectures]] → [[02 Concepts/Lifecycle/Deployment & Serving/Deployment & Serving Index|Deployment & Serving]]

## Book Passages

These are explicitly recorded related passages from the upstream draft alignment; they do not certify complete coverage.

No explicit passage alignment is recorded for this concept. Subject reading pointers are available in its browsing home.

## Conditional Relationships

These are the taxonomy's draft editorial relationships. Read each relationship with its condition; an outgoing link is not a prerequisite claim.

- Uses for candidate generation [[02 Concepts/Lifecycle/Deployment & Serving/Approximate Nearest Neighbor Search|Approximate Nearest Neighbor Search]]. **Condition:** The first stage retrieves candidates by approximate similarity before learned ranking.

- Runs in its ranking stages a [[02 Concepts/Foundations/Models & Architectures/Deep Recommendation Model|Deep Recommendation Model]]. **Condition:** Candidate generation narrows the set before costly deep ranking models score it within the latency budget.

## Search Terms

Upstream search terms may be related terms rather than exact synonyms: ranking funnel; candidate generation.

## Source

[Canonical Taxonomy](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/taxonomy.yml) · [Passage Alignment](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/mlsysbook-alignment.yml)

Taxonomy definitions and relationship wording: CC BY 4.0, with attribution to the Machine Learning Systems curriculum by Vijay Janapa Reddi and contributors. The textbook retains its separate license.
