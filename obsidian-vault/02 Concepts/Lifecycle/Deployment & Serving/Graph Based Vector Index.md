---
title: Graph Based Vector Index
type: concept
tags:
- Type/Concept
- Group/Lifecycle
- Topic/Retrieval_Vector_Search
source_repository: https://github.com/klappe-pm/cs249r_book
source_commit: de87c0103806d7bfb1c677dbb77a2b92fa00c298
source_path: taxonomy/taxonomy.yml
source_label: Graph-based vector index
taxonomy_id: mlsys.graph-vector-index
taxonomy_status: draft
taxonomy_version: 0.4-draft
---

# Graph Based Vector Index

An approximate nearest-neighbor index linking vectors into a proximity graph, often hierarchical, searched by greedy traversal for high recall at high memory cost.

## Browsing Home

[[02 Concepts/Lifecycle/Deployment & Serving/Retrieval & Vector Search Subject|Retrieval & Vector Search]] → [[02 Concepts/Lifecycle/Deployment & Serving/Deployment & Serving Index|Deployment & Serving]]

## Book Passages

These are explicitly recorded related passages from the upstream draft alignment; they do not certify complete coverage.

No explicit passage alignment is recorded for this concept. Subject reading pointers are available in its browsing home.

## Conditional Relationships

These are the taxonomy's draft editorial relationships. Read each relationship with its condition; an outgoing link is not a prerequisite claim.

- Implements [[02 Concepts/Lifecycle/Deployment & Serving/Approximate Nearest Neighbor Search|Approximate Nearest Neighbor Search]]. **Condition:** Best recall-latency trade-off when the full graph and vectors fit in memory.

- Update and delete cost bounds attainable [[02 Concepts/Lifecycle/Deployment & Serving/Vector Index Freshness|Vector Index Freshness]]. **Condition:** Deletes and in-place updates degrade graph connectivity unless repaired or periodically rebuilt.

## Search Terms

Upstream search terms may be related terms rather than exact synonyms: HNSW; proximity-graph index.

## Source

[Canonical Taxonomy](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/taxonomy.yml) · [Passage Alignment](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/mlsysbook-alignment.yml)

Taxonomy definitions and relationship wording: CC BY 4.0, with attribution to the Machine Learning Systems curriculum by Vijay Janapa Reddi and contributors. The textbook retains its separate license.
