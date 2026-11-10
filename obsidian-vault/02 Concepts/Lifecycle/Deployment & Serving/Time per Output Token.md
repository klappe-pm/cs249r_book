---
title: Time per Output Token
type: concept
tags:
- Type/Concept
- Group/Lifecycle
- Topic/Latency_Throughput_Goodput
source_repository: https://github.com/klappe-pm/cs249r_book
source_commit: de87c0103806d7bfb1c677dbb77a2b92fa00c298
source_path: taxonomy/taxonomy.yml
source_label: Time per output token
taxonomy_id: mlsys.tpot
taxonomy_status: draft
taxonomy_version: 0.4-draft
---

# Time per Output Token

For a request producing multiple tokens, its elapsed decoding time after the first output divided by its remaining generated-token count, summarizing average decoding speed at a declared measurement boundary.

## Browsing Home

[[02 Concepts/Lifecycle/Deployment & Serving/Latency, Throughput & Goodput Subject|Latency, Throughput & Goodput]] → [[02 Concepts/Lifecycle/Deployment & Serving/Deployment & Serving Index|Deployment & Serving]]

## Book Passages

These are explicitly recorded related passages from the upstream draft alignment; they do not certify complete coverage.

- [[01 Books/Volume I - Foundations/04 Deployment/13 Model Serving/V1-13.10 LLM Serving#^sec-model-serving-performance-metrics-ttft-tpot-b009|V1-13.10 LLM Serving]] — Time per output token. [Exact Source Passage](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/books/vol1/13_model_serving/13_model_serving.qmd#L4699).

## Conditional Relationships

These are the taxonomy's draft editorial relationships. Read each relationship with its condition; an outgoing link is not a prerequisite claim.

- Quantifies the delivery cadence of [[02 Concepts/Lifecycle/Deployment & Serving/Token Streaming|Token Streaming]]. **Condition:** Output is returned token by token after the first.

## Search Terms

Upstream search terms may be related terms rather than exact synonyms: TPOT.

## Source

[Canonical Taxonomy](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/taxonomy.yml) · [Passage Alignment](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/mlsysbook-alignment.yml)

Taxonomy definitions and relationship wording: CC BY 4.0, with attribution to the Machine Learning Systems curriculum by Vijay Janapa Reddi and contributors. The textbook retains its separate license.
