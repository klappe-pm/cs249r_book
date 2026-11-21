---
title: Dense Retrieval
type: concept
tags:
- Type/Concept
- Group/Lifecycle
- Topic/Retrieval_Vector_Search
source_repository: https://github.com/klappe-pm/cs249r_book
source_commit: de87c0103806d7bfb1c677dbb77a2b92fa00c298
source_path: taxonomy/taxonomy.yml
source_label: Dense retrieval
taxonomy_id: mlsys.dense-retrieval
taxonomy_status: draft
taxonomy_version: 0.4-draft
---

# Dense Retrieval

Retrieving records by similarity between learned embeddings of query and records.

## Browsing Home

[[02 Concepts/Lifecycle/Deployment & Serving/Retrieval & Vector Search Subject|Retrieval & Vector Search]] → [[02 Concepts/Lifecycle/Deployment & Serving/Deployment & Serving Index|Deployment & Serving]]

## Book Passages

These are explicitly recorded related passages from the upstream draft alignment; they do not certify complete coverage.

No explicit passage alignment is recorded for this concept. Subject reading pointers are available in its browsing home.

## Conditional Relationships

These are the taxonomy's draft editorial relationships. Read each relationship with its condition; an outgoing link is not a prerequisite claim.

- Uses at scale [[02 Concepts/Lifecycle/Deployment & Serving/Approximate Nearest Neighbor Search|Approximate Nearest Neighbor Search]]. **Condition:** Holds when the collection is too large for exact similarity search within latency limits.

- Uses [[02 Concepts/Foundations/Models & Architectures/Embeddings|Embeddings]]. **Condition:** Holds for bi-encoder retrieval where queries and records are embedded separately.

- Is a kind of [[02 Concepts/Lifecycle/Deployment & Serving/Retrieval|Retrieval]]. **Condition:** Applies when relevance is scored by similarity of learned vectors.

## Search Terms

Upstream search terms may be related terms rather than exact synonyms: two-tower model; dual encoder; bi-encoder.

## Source

[Canonical Taxonomy](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/taxonomy.yml) · [Passage Alignment](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/mlsysbook-alignment.yml)

Taxonomy definitions and relationship wording: CC BY 4.0, with attribution to the Machine Learning Systems curriculum by Vijay Janapa Reddi and contributors. The textbook retains its separate license.
