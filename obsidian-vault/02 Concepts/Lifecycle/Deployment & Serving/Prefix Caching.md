---
title: Prefix Caching
type: concept
tags:
- Type/Concept
- Group/Lifecycle
- Topic/LLM_Generative_Inference
source_repository: https://github.com/klappe-pm/cs249r_book
source_commit: de87c0103806d7bfb1c677dbb77a2b92fa00c298
source_path: taxonomy/taxonomy.yml
source_label: Prefix caching
taxonomy_id: mlsys.prefix-cache
taxonomy_status: draft
taxonomy_version: 0.4-draft
---

# Prefix Caching

Reusing compatible computed state for an identical request prefix.

## Browsing Home

[[02 Concepts/Lifecycle/Deployment & Serving/LLM & Generative Inference Subject|LLM & Generative Inference]] → [[02 Concepts/Lifecycle/Deployment & Serving/Deployment & Serving Index|Deployment & Serving]]

## Book Passages

These are explicitly recorded related passages from the upstream draft alignment; they do not certify complete coverage.

- [[01 Books/Volume I - Foundations/04 Deployment/13 Model Serving/V1-13.10 LLM Serving#^sec-model-serving-prefix-caching-offloading|V1-13.10 LLM Serving]] — Prefix caching. [Exact Source Passage](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/books/vol1/13_model_serving/13_model_serving.qmd#L5239).

- [[01 Books/Volume III - Agentic Systems/02 Agent Memory/05 KV Cache Management/V3-05.06 Prefix Caching Across Turns#^sec-vol3-kv-cache-prefix-compatibility|V3-05.06 Prefix Caching Across Turns]] — Prefix reuse. [Exact Source Passage](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/books/vol3/05_kv_cache/05_kv_cache.qmd#L694).

## Conditional Relationships

These are the taxonomy's draft editorial relationships. Read each relationship with its condition; an outgoing link is not a prerequisite claim.

- Reuses compatible [[02 Concepts/Lifecycle/Deployment & Serving/KV Cache|KV Cache]]. **Condition:** Token prefix, model state, position conventions, and access boundaries must match.

- Skips recomputed prefill to reduce [[02 Concepts/Lifecycle/Deployment & Serving/Time to First Token|Time to First Token]]. **Condition:** Holds when requests share long identical prefixes and the cache hits.

- Avoids recomputing shared prefixes, lowering [[02 Concepts/Qualities/Sustainability & Cost/Cost per Token|Cost per Token]]. **Condition:** Requests share long prefixes such as system prompts; cache hits must be routed to the holding replica.

## Search Terms

Upstream search terms may be related terms rather than exact synonyms: prompt caching; context caching.

## Source

[Canonical Taxonomy](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/taxonomy.yml) · [Passage Alignment](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/mlsysbook-alignment.yml)

Taxonomy definitions and relationship wording: CC BY 4.0, with attribution to the Machine Learning Systems curriculum by Vijay Janapa Reddi and contributors. The textbook retains its separate license.
