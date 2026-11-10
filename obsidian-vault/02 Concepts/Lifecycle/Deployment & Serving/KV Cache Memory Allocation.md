---
title: KV Cache Memory Allocation
type: concept
tags:
- Type/Concept
- Group/Lifecycle
- Topic/LLM_Generative_Inference
source_repository: https://github.com/klappe-pm/cs249r_book
source_commit: de87c0103806d7bfb1c677dbb77a2b92fa00c298
source_path: taxonomy/taxonomy.yml
source_label: KV-cache memory allocation
taxonomy_id: mlsys.kv-memory-allocation
taxonomy_status: draft
taxonomy_version: 0.4-draft
---

# KV Cache Memory Allocation

Laying out and allocating accelerator memory for cached attention state, which trades fragmentation and sharing against kernel compatibility and allocation cost.

## Browsing Home

[[02 Concepts/Lifecycle/Deployment & Serving/LLM & Generative Inference Subject|LLM & Generative Inference]] → [[02 Concepts/Lifecycle/Deployment & Serving/Deployment & Serving Index|Deployment & Serving]]

## Book Passages

These are explicitly recorded related passages from the upstream draft alignment; they do not certify complete coverage.

No explicit passage alignment is recorded for this concept. Subject reading pointers are available in its browsing home.

## Conditional Relationships

These are the taxonomy's draft editorial relationships. Read each relationship with its condition; an outgoing link is not a prerequisite claim.

- Sets how much KV memory is lost to [[02 Concepts/Stack/Frameworks, Compilers & Runtimes/Runtime Memory Fragmentation|Runtime Memory Fragmentation]]. **Condition:** When sequences of varying and growing length share one accelerator memory pool.

- Provides the storage that holds [[02 Concepts/Lifecycle/Deployment & Serving/KV Cache|KV Cache]]. **Condition:** When a serving engine manages the cache's memory rather than the model framework.

## Search Terms

Upstream search terms may be related terms rather than exact synonyms: KV allocator; KV-cache memory layout.

## Source

[Canonical Taxonomy](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/taxonomy.yml) · [Passage Alignment](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/mlsysbook-alignment.yml)

Taxonomy definitions and relationship wording: CC BY 4.0, with attribution to the Machine Learning Systems curriculum by Vijay Janapa Reddi and contributors. The textbook retains its separate license.
