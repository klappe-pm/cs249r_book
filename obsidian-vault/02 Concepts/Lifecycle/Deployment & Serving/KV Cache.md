---
title: KV Cache
type: concept
tags:
- Type/Concept
- Group/Lifecycle
- Topic/LLM_Generative_Inference
source_repository: https://github.com/klappe-pm/cs249r_book
source_commit: de87c0103806d7bfb1c677dbb77a2b92fa00c298
source_path: taxonomy/taxonomy.yml
source_label: KV cache
taxonomy_id: mlsys.kv-cache
taxonomy_status: draft
taxonomy_version: 0.4-draft
---

# KV Cache

Retained attention keys and values reused during autoregressive execution.

## Browsing Home

[[02 Concepts/Lifecycle/Deployment & Serving/LLM & Generative Inference Subject|LLM & Generative Inference]] → [[02 Concepts/Lifecycle/Deployment & Serving/Deployment & Serving Index|Deployment & Serving]]

## Book Passages

These are explicitly recorded related passages from the upstream draft alignment; they do not certify complete coverage.

- [[01 Books/Volume I - Foundations/04 Deployment/13 Model Serving/V1-13.10 LLM Serving#^sec-model-serving-memory-kv-cache-d1ea|V1-13.10 LLM Serving]] — KV cache per conversation. [Exact Source Passage](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/books/vol1/13_model_serving/13_model_serving.qmd#L5061).

- [[01 Books/Volume II - Scaling/03 The Fleet in Production/10 Serving at Scale/V2-10.08 Memory and Decode-Time Management#^sec-inference-scale-kv-cache-wall|V2-10.08 Memory and Decode-Time Management]] — KV cache. [Exact Source Passage](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/books/vol2/10_inference/10_inference.qmd#L3084).

- [[01 Books/Volume III - Agentic Systems/02 Agent Memory/05 KV Cache Management/V3-05.03 The Footprint of Retained Attention State#^sec-vol3-kvcache-geometry|V3-05.03 The Footprint of Retained Attention State]] — Retained KV state. [Exact Source Passage](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/books/vol3/05_kv_cache/05_kv_cache.qmd#L85).

## Conditional Relationships

These are the taxonomy's draft editorial relationships. Read each relationship with its condition; an outgoing link is not a prerequisite claim.

- Adds per-request state to [[02 Concepts/Foundations/Workloads & Requirements/Memory Footprint|Memory Footprint]]. **Condition:** Autoregressive serving retains keys and values for every in-flight token; the term grows with batch size and context length.

## Themes

- [[03 Themes/Memory and Bandwidth|Memory and Bandwidth]]

## Search Terms

Upstream search terms may be related terms rather than exact synonyms: Key-value cache.

## Source

[Canonical Taxonomy](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/taxonomy.yml) · [Passage Alignment](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/mlsysbook-alignment.yml)

Taxonomy definitions and relationship wording: CC BY 4.0, with attribution to the Machine Learning Systems curriculum by Vijay Janapa Reddi and contributors. The textbook retains its separate license.
