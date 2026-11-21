---
title: Partitioned and Quantized Vector Index
type: concept
tags:
- Type/Concept
- Group/Lifecycle
- Topic/Retrieval_Vector_Search
source_repository: https://github.com/klappe-pm/cs249r_book
source_commit: de87c0103806d7bfb1c677dbb77a2b92fa00c298
source_path: taxonomy/taxonomy.yml
source_label: Partitioned and quantized vector index
taxonomy_id: mlsys.quantized-vector-index
taxonomy_status: draft
taxonomy_version: 0.4-draft
---

# Partitioned and Quantized Vector Index

An index that clusters vectors into partitions probed selectively and compresses them with product quantization, trading recall for memory footprint and scan cost.

## Browsing Home

[[02 Concepts/Lifecycle/Deployment & Serving/Retrieval & Vector Search Subject|Retrieval & Vector Search]] → [[02 Concepts/Lifecycle/Deployment & Serving/Deployment & Serving Index|Deployment & Serving]]

## Book Passages

These are explicitly recorded related passages from the upstream draft alignment; they do not certify complete coverage.

No explicit passage alignment is recorded for this concept. Subject reading pointers are available in its browsing home.

## Conditional Relationships

These are the taxonomy's draft editorial relationships. Read each relationship with its condition; an outgoing link is not a prerequisite claim.

- Implements [[02 Concepts/Lifecycle/Deployment & Serving/Approximate Nearest Neighbor Search|Approximate Nearest Neighbor Search]]. **Condition:** Preferred when memory per vector is the binding constraint, accepting lower recall or a reranking pass on exact vectors.

- Trades memory against recall versus [[02 Concepts/Lifecycle/Deployment & Serving/Graph Based Vector Index|Graph Based Vector Index]]. **Condition:** Compared at equal query latency on the same corpus and recall target.

- Compresses vectors to reduce [[02 Concepts/Foundations/Workloads & Requirements/Memory Footprint|Memory Footprint]]. **Condition:** Vectors are stored as shorter quantized codes rather than full-precision coordinates; recall depends on quantization, partition probing, reranking, and the data.

## Search Terms

Upstream search terms may be related terms rather than exact synonyms: IVF-PQ.

## Source

[Canonical Taxonomy](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/taxonomy.yml) · [Passage Alignment](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/mlsysbook-alignment.yml)

Taxonomy definitions and relationship wording: CC BY 4.0, with attribution to the Machine Learning Systems curriculum by Vijay Janapa Reddi and contributors. The textbook retains its separate license.
