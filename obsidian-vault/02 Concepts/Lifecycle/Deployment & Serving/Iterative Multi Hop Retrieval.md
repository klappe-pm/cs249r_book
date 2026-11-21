---
title: Iterative Multi Hop Retrieval
type: concept
tags:
- Type/Concept
- Group/Lifecycle
- Topic/Retrieval_Vector_Search
source_repository: https://github.com/klappe-pm/cs249r_book
source_commit: de87c0103806d7bfb1c677dbb77a2b92fa00c298
source_path: taxonomy/taxonomy.yml
source_label: Iterative multi-hop retrieval
taxonomy_id: mlsys.multi-hop-retrieval
taxonomy_status: draft
taxonomy_version: 0.4-draft
---

# Iterative Multi Hop Retrieval

Retrieval that issues successive queries, each formulated from previously retrieved evidence or reasoning steps, to answer questions no single lookup resolves.

## Browsing Home

[[02 Concepts/Lifecycle/Deployment & Serving/Retrieval & Vector Search Subject|Retrieval & Vector Search]] → [[02 Concepts/Lifecycle/Deployment & Serving/Deployment & Serving Index|Deployment & Serving]]

## Book Passages

These are explicitly recorded related passages from the upstream draft alignment; they do not certify complete coverage.

No explicit passage alignment is recorded for this concept. Subject reading pointers are available in its browsing home.

## Conditional Relationships

These are the taxonomy's draft editorial relationships. Read each relationship with its condition; an outgoing link is not a prerequisite claim.

- Is an iterative form of [[02 Concepts/Lifecycle/Deployment & Serving/Retrieval|Retrieval]]. **Condition:** Later queries depend on earlier results.

- Adds retrieval rounds to [[02 Concepts/Qualities/Performance, Efficiency & Benchmarking/Execution Time|Execution Time]]. **Condition:** Each hop requires another query and model call.

## Search Terms

Upstream search terms may be related terms rather than exact synonyms: agentic retrieval; multi-hop RAG.

## Source

[Canonical Taxonomy](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/taxonomy.yml) · [Passage Alignment](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/mlsysbook-alignment.yml)

Taxonomy definitions and relationship wording: CC BY 4.0, with attribution to the Machine Learning Systems curriculum by Vijay Janapa Reddi and contributors. The textbook retains its separate license.
