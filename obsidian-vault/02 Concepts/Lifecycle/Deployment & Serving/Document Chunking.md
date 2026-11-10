---
title: Document Chunking
type: concept
tags:
- Type/Concept
- Group/Lifecycle
- Topic/Retrieval_Vector_Search
source_repository: https://github.com/klappe-pm/cs249r_book
source_commit: de87c0103806d7bfb1c677dbb77a2b92fa00c298
source_path: taxonomy/taxonomy.yml
source_label: Document chunking
taxonomy_id: mlsys.document-chunking
taxonomy_status: draft
taxonomy_version: 0.4-draft
---

# Document Chunking

Dividing source documents into retrievable units with chosen boundaries, overlap, and source identifiers so retrieval granularity fits embedding and generation budgets.

## Browsing Home

[[02 Concepts/Lifecycle/Deployment & Serving/Retrieval & Vector Search Subject|Retrieval & Vector Search]] → [[02 Concepts/Lifecycle/Deployment & Serving/Deployment & Serving Index|Deployment & Serving]]

## Book Passages

These are explicitly recorded related passages from the upstream draft alignment; they do not certify complete coverage.

No explicit passage alignment is recorded for this concept. Subject reading pointers are available in its browsing home.

## Conditional Relationships

These are the taxonomy's draft editorial relationships. Read each relationship with its condition; an outgoing link is not a prerequisite claim.

- Uses token counts to enforce chunk boundaries [[02 Concepts/Foundations/Models & Architectures/Tokenization|Tokenization]]. **Condition:** For token-budgeted chunkers, whose sizes and overlaps are specified in model tokens.

- Sets the unit embedded and returned by [[02 Concepts/Lifecycle/Deployment & Serving/Dense Retrieval|Dense Retrieval]]. **Condition:** When documents exceed encoder limits or one document vector would blur distinct topics.

- Defines the indexed units of [[02 Concepts/Lifecycle/Deployment & Serving/Retrieval Augmented Generation|Retrieval Augmented Generation]]. **Condition:** When the RAG application builds its retrieval corpus from document chunks.

## Search Terms

Upstream search terms may be related terms rather than exact synonyms: retrieval chunking; passage segmentation; semantic chunking.

## Source

[Canonical Taxonomy](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/taxonomy.yml) · [Passage Alignment](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/mlsysbook-alignment.yml)

Taxonomy definitions and relationship wording: CC BY 4.0, with attribution to the Machine Learning Systems curriculum by Vijay Janapa Reddi and contributors. The textbook retains its separate license.
