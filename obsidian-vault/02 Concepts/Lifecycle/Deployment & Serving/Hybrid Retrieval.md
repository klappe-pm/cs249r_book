---
title: Hybrid Retrieval
type: concept
tags:
- Type/Concept
- Group/Lifecycle
- Topic/Retrieval_Vector_Search
source_repository: https://github.com/klappe-pm/cs249r_book
source_commit: de87c0103806d7bfb1c677dbb77a2b92fa00c298
source_path: taxonomy/taxonomy.yml
source_label: Hybrid retrieval
taxonomy_id: mlsys.hybrid-retrieval
taxonomy_status: draft
taxonomy_version: 0.4-draft
---

# Hybrid Retrieval

Combining lexical and dense retrieval results through score or rank fusion to recover complementary matches while managing additional search cost and ranking calibration.

## Browsing Home

[[02 Concepts/Lifecycle/Deployment & Serving/Retrieval & Vector Search Subject|Retrieval & Vector Search]] → [[02 Concepts/Lifecycle/Deployment & Serving/Deployment & Serving Index|Deployment & Serving]]

## Book Passages

These are explicitly recorded related passages from the upstream draft alignment; they do not certify complete coverage.

No explicit passage alignment is recorded for this concept. Subject reading pointers are available in its browsing home.

## Conditional Relationships

These are the taxonomy's draft editorial relationships. Read each relationship with its condition; an outgoing link is not a prerequisite claim.

- Uses lexical candidate retrieval [[02 Concepts/Lifecycle/Deployment & Serving/Lexical Retrieval|Lexical Retrieval]]. **Condition:** When exact terms, identifiers, or keyword matches contribute a candidate list.

- Uses embedding-based candidate retrieval [[02 Concepts/Lifecycle/Deployment & Serving/Dense Retrieval|Dense Retrieval]]. **Condition:** When semantic similarity contributes a candidate list that is fused with lexical results.

## Search Terms

Upstream search terms may be related terms rather than exact synonyms: hybrid search; lexical-dense retrieval; reciprocal rank fusion.

## Source

[Canonical Taxonomy](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/taxonomy.yml) · [Passage Alignment](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/mlsysbook-alignment.yml)

Taxonomy definitions and relationship wording: CC BY 4.0, with attribution to the Machine Learning Systems curriculum by Vijay Janapa Reddi and contributors. The textbook retains its separate license.
