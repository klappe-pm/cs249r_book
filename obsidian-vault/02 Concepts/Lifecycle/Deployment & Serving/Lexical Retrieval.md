---
title: Lexical Retrieval
type: concept
tags:
- Type/Concept
- Group/Lifecycle
- Topic/Retrieval_Vector_Search
- Context/Background
source_repository: https://github.com/klappe-pm/cs249r_book
source_commit: de87c0103806d7bfb1c677dbb77a2b92fa00c298
source_path: taxonomy/taxonomy.yml
source_label: Lexical retrieval
taxonomy_id: mlsys.lexical-retrieval
taxonomy_status: draft
taxonomy_version: 0.4-draft
---

# Lexical Retrieval

Retrieving records by weighted term overlap with the query using an inverted index, as in BM25.

## Browsing Home

[[02 Concepts/Lifecycle/Deployment & Serving/Retrieval & Vector Search Subject|Retrieval & Vector Search]] → [[02 Concepts/Lifecycle/Deployment & Serving/Deployment & Serving Index|Deployment & Serving]]

This is a background concept on which ML systems reasoning depends; that classification does not make it optional.

## Book Passages

These are explicitly recorded related passages from the upstream draft alignment; they do not certify complete coverage.

No explicit passage alignment is recorded for this concept. Subject reading pointers are available in its browsing home.

## Conditional Relationships

These are the taxonomy's draft editorial relationships. Read each relationship with its condition; an outgoing link is not a prerequisite claim.

- Is a complementary alternative to [[02 Concepts/Lifecycle/Deployment & Serving/Dense Retrieval|Dense Retrieval]]. **Condition:** Lexical matching handles rare terms and exact identifiers that embeddings may miss; hybrid systems combine both scores.

- Is a kind of [[02 Concepts/Lifecycle/Deployment & Serving/Retrieval|Retrieval]]. **Condition:** Applies when relevance is scored by weighted term overlap over an inverted index.

## Search Terms

Upstream search terms may be related terms rather than exact synonyms: sparse retrieval; BM25.

## Source

[Canonical Taxonomy](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/taxonomy.yml) · [Passage Alignment](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/mlsysbook-alignment.yml)

Taxonomy definitions and relationship wording: CC BY 4.0, with attribution to the Machine Learning Systems curriculum by Vijay Janapa Reddi and contributors. The textbook retains its separate license.
