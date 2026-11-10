---
title: RAG Pipeline Scheduling
type: concept
tags:
- Type/Concept
- Group/Lifecycle
- Topic/Retrieval_Vector_Search
source_repository: https://github.com/klappe-pm/cs249r_book
source_commit: de87c0103806d7bfb1c677dbb77a2b92fa00c298
source_path: taxonomy/taxonomy.yml
source_label: RAG pipeline scheduling
taxonomy_id: mlsys.rag-pipeline-scheduling
taxonomy_status: draft
taxonomy_version: 0.4-draft
---

# RAG Pipeline Scheduling

Coordinating the retrieval and generation work of retrieval-augmented requests across requests and processors, overlapping and batching work across the stage boundary and optionally adapting retrieval settings per query, to meet latency and answer-quality targets.

## Browsing Home

[[02 Concepts/Lifecycle/Deployment & Serving/Retrieval & Vector Search Subject|Retrieval & Vector Search]] → [[02 Concepts/Lifecycle/Deployment & Serving/Deployment & Serving Index|Deployment & Serving]]

## Book Passages

These are explicitly recorded related passages from the upstream draft alignment; they do not certify complete coverage.

No explicit passage alignment is recorded for this concept. Subject reading pointers are available in its browsing home.

## Conditional Relationships

These are the taxonomy's draft editorial relationships. Read each relationship with its condition; an outgoing link is not a prerequisite claim.

- Overlaps retrieval with generation work to shorten [[02 Concepts/Lifecycle/Deployment & Serving/Time to First Token|Time to First Token]]. **Condition:** When retrieval sits on the request's critical path before prefill.

- Avoids waiting for generation memory through joint configuration and scheduling, cutting [[02 Concepts/Foundations/Quantitative System Models/Queueing Delay|Queueing Delay]]. **Condition:** When a fixed RAG configuration would wait for accelerator memory but another configuration meeting the query's quality target fits.

- Overlaps retrieval and generation through [[02 Concepts/Lifecycle/Deployment & Serving/Compound Workflow Pipelining|Compound Workflow Pipelining]]. **Condition:** When retrieval or other upstream stages expose stable partial results that downstream generation can process while upstream work continues.

## Search Terms

Upstream search terms may be related terms rather than exact synonyms: retrieval-generation co-scheduling.

## Source

[Canonical Taxonomy](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/taxonomy.yml) · [Passage Alignment](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/mlsysbook-alignment.yml)

Taxonomy definitions and relationship wording: CC BY 4.0, with attribution to the Machine Learning Systems curriculum by Vijay Janapa Reddi and contributors. The textbook retains its separate license.
