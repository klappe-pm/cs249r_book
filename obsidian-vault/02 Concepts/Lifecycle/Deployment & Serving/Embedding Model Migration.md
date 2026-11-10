---
title: Embedding Model Migration
type: concept
tags:
- Type/Concept
- Group/Lifecycle
- Topic/Retrieval_Vector_Search
source_repository: https://github.com/klappe-pm/cs249r_book
source_commit: de87c0103806d7bfb1c677dbb77a2b92fa00c298
source_path: taxonomy/taxonomy.yml
source_label: Embedding model migration
taxonomy_id: mlsys.embedding-migration
taxonomy_status: draft
taxonomy_version: 0.4-draft
---

# Embedding Model Migration

Changing the encoder behind a vector index while keeping queries and stored vectors comparable, by re-encoding the corpus, validated mappings, or backward-compatible training, with a controlled serving cutover.

## Browsing Home

[[02 Concepts/Lifecycle/Deployment & Serving/Retrieval & Vector Search Subject|Retrieval & Vector Search]] → [[02 Concepts/Lifecycle/Deployment & Serving/Deployment & Serving Index|Deployment & Serving]]

## Book Passages

These are explicitly recorded related passages from the upstream draft alignment; they do not certify complete coverage.

No explicit passage alignment is recorded for this concept. Subject reading pointers are available in its browsing home.

## Conditional Relationships

These are the taxonomy's draft editorial relationships. Read each relationship with its condition; an outgoing link is not a prerequisite claim.

- Keeps query and corpus encoders aligned through [[02 Concepts/Lifecycle/MLOps & Operations/Model and Feature Compatibility|Model and Feature Compatibility]]. **Condition:** When query encoders and stored corpus representations change across releases.

- Re-encodes historical corpus records in shadow indexes using [[02 Concepts/Lifecycle/Data Engineering/Feature Backfill|Feature Backfill]]. **Condition:** Before switching live query traffic to the new embedding model.

## Search Terms

Upstream search terms may be related terms rather than exact synonyms: re-embedding; vector index backfill; embedding version upgrade.

## Source

[Canonical Taxonomy](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/taxonomy.yml) · [Passage Alignment](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/mlsysbook-alignment.yml)

Taxonomy definitions and relationship wording: CC BY 4.0, with attribution to the Machine Learning Systems curriculum by Vijay Janapa Reddi and contributors. The textbook retains its separate license.
