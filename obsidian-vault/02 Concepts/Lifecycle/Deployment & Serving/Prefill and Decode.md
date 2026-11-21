---
title: Prefill and Decode
type: concept
tags:
- Type/Concept
- Group/Lifecycle
- Topic/LLM_Generative_Inference
source_repository: https://github.com/klappe-pm/cs249r_book
source_commit: de87c0103806d7bfb1c677dbb77a2b92fa00c298
source_path: taxonomy/taxonomy.yml
source_label: Prefill and decode
taxonomy_id: mlsys.prefill-decode
taxonomy_status: draft
taxonomy_version: 0.4-draft
---

# Prefill and Decode

The prompt-processing and incremental token-generation phases of autoregressive inference.

## Browsing Home

[[02 Concepts/Lifecycle/Deployment & Serving/LLM & Generative Inference Subject|LLM & Generative Inference]] → [[02 Concepts/Lifecycle/Deployment & Serving/Deployment & Serving Index|Deployment & Serving]]

## Book Passages

These are explicitly recorded related passages from the upstream draft alignment; they do not certify complete coverage.

- [[01 Books/Volume I - Foundations/04 Deployment/13 Model Serving/V1-13.10 LLM Serving#^sec-model-serving-performance-metrics-ttft-tpot-b009|V1-13.10 LLM Serving]] — Prefill. [Exact Source Passage](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/books/vol1/13_model_serving/13_model_serving.qmd#L4699).

- [[01 Books/Volume I - Foundations/04 Deployment/13 Model Serving/V1-13.10 LLM Serving#^sec-model-serving-memory-kv-cache-d1ea|V1-13.10 LLM Serving]] — Decode. [Exact Source Passage](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/books/vol1/13_model_serving/13_model_serving.qmd#L5061).

## Conditional Relationships

These are the taxonomy's draft editorial relationships. Read each relationship with its condition; an outgoing link is not a prerequisite claim.

- Classifies prefill as compute-bound and decode as memory-bound in [[02 Concepts/Foundations/Quantitative System Models/Compute Bound vs. Memory Bound|Compute Bound vs. Memory Bound]]. **Condition:** Prefill processes many tokens per weight read while decode processes few.

- Prefill phase dominates [[02 Concepts/Lifecycle/Deployment & Serving/Time to First Token|Time to First Token]]. **Condition:** Holds when queueing delay is small relative to prompt processing time.

## Source

[Canonical Taxonomy](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/taxonomy.yml) · [Passage Alignment](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/mlsysbook-alignment.yml)

Taxonomy definitions and relationship wording: CC BY 4.0, with attribution to the Machine Learning Systems curriculum by Vijay Janapa Reddi and contributors. The textbook retains its separate license.
