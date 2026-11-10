---
title: Paged KV Allocation
type: concept
tags:
- Type/Concept
- Group/Lifecycle
- Topic/LLM_Generative_Inference
source_repository: https://github.com/klappe-pm/cs249r_book
source_commit: de87c0103806d7bfb1c677dbb77a2b92fa00c298
source_path: taxonomy/taxonomy.yml
source_label: Paged KV allocation
taxonomy_id: mlsys.paged-kv
taxonomy_status: draft
taxonomy_version: 0.4-draft
---

# Paged KV Allocation

Managing attention state in blocks to reduce allocation waste and support sharing.

## Browsing Home

[[02 Concepts/Lifecycle/Deployment & Serving/LLM & Generative Inference Subject|LLM & Generative Inference]] → [[02 Concepts/Lifecycle/Deployment & Serving/Deployment & Serving Index|Deployment & Serving]]

## Book Passages

These are explicitly recorded related passages from the upstream draft alignment; they do not certify complete coverage.

- [[01 Books/Volume I - Foundations/04 Deployment/13 Model Serving/V1-13.10 LLM Serving#^sec-model-serving-pagedattention-b8d4|V1-13.10 LLM Serving]] — Paged KV allocation. [Exact Source Passage](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/books/vol1/13_model_serving/13_model_serving.qmd#L4995).

## Conditional Relationships

These are the taxonomy's draft editorial relationships. Read each relationship with its condition; an outgoing link is not a prerequisite claim.

- Stores, in fixed-size blocks mapped by a block table, the [[02 Concepts/Lifecycle/Deployment & Serving/KV Cache|KV Cache]]. **Condition:** When a block table maps each request's positions to retained key-value blocks that attention can retrieve.

- Enables block sharing for [[02 Concepts/Lifecycle/Deployment & Serving/Prefix Caching|Prefix Caching]]. **Condition:** Holds when the allocator supports copy-on-write sharing of identical prefix blocks.

- Raises batch size and so [[02 Concepts/Foundations/Quantitative System Models/Service Capacity|Service Capacity]]. **Condition:** Holds when KV memory fragmentation was limiting concurrency.

- Is the block-based form of [[02 Concepts/Lifecycle/Deployment & Serving/KV Cache Memory Allocation|KV Cache Memory Allocation]]. **Condition:** When attention state is stored in fixed-size blocks mapped by a block table.

## Search Terms

Upstream search terms may be related terms rather than exact synonyms: PagedAttention.

## Source

[Canonical Taxonomy](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/taxonomy.yml) · [Passage Alignment](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/mlsysbook-alignment.yml)

Taxonomy definitions and relationship wording: CC BY 4.0, with attribution to the Machine Learning Systems curriculum by Vijay Janapa Reddi and contributors. The textbook retains its separate license.
