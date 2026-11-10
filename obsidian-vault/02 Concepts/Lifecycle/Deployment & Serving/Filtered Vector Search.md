---
title: Filtered Vector Search
type: concept
tags:
- Type/Concept
- Group/Lifecycle
- Topic/Retrieval_Vector_Search
source_repository: https://github.com/klappe-pm/cs249r_book
source_commit: de87c0103806d7bfb1c677dbb77a2b92fa00c298
source_path: taxonomy/taxonomy.yml
source_label: Filtered vector search
taxonomy_id: mlsys.filtered-vector-search
taxonomy_status: draft
taxonomy_version: 0.4-draft
---

# Filtered Vector Search

Nearest-neighbor search restricted to records satisfying metadata predicates, where naive pre- or post-filtering loses recall or cost under selective filters.

## Browsing Home

[[02 Concepts/Lifecycle/Deployment & Serving/Retrieval & Vector Search Subject|Retrieval & Vector Search]] → [[02 Concepts/Lifecycle/Deployment & Serving/Deployment & Serving Index|Deployment & Serving]]

## Book Passages

These are explicitly recorded related passages from the upstream draft alignment; they do not certify complete coverage.

No explicit passage alignment is recorded for this concept. Subject reading pointers are available in its browsing home.

## Conditional Relationships

These are the taxonomy's draft editorial relationships. Read each relationship with its condition; an outgoing link is not a prerequisite claim.

- Commonly runs on [[02 Concepts/Lifecycle/Deployment & Serving/Approximate Nearest Neighbor Search|Approximate Nearest Neighbor Search]]. **Condition:** When the filter leaves too many candidates for exact search.

- Extends traversal of [[02 Concepts/Lifecycle/Deployment & Serving/Graph Based Vector Index|Graph Based Vector Index]]. **Condition:** Applies to predicate-agnostic methods that densify a proximity graph to keep filtered recall.

## Search Terms

Upstream search terms may be related terms rather than exact synonyms: predicate-constrained ANN.

## Source

[Canonical Taxonomy](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/taxonomy.yml) · [Passage Alignment](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/mlsysbook-alignment.yml)

Taxonomy definitions and relationship wording: CC BY 4.0, with attribution to the Machine Learning Systems curriculum by Vijay Janapa Reddi and contributors. The textbook retains its separate license.
