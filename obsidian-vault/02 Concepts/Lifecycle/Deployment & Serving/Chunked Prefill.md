---
title: Chunked Prefill
type: concept
tags:
- Type/Concept
- Group/Lifecycle
- Topic/LLM_Generative_Inference
source_repository: https://github.com/klappe-pm/cs249r_book
source_commit: de87c0103806d7bfb1c677dbb77a2b92fa00c298
source_path: taxonomy/taxonomy.yml
source_label: Chunked prefill
taxonomy_id: mlsys.chunked-prefill
taxonomy_status: draft
taxonomy_version: 0.4-draft
---

# Chunked Prefill

Splitting a long prompt's prefill into chunks interleaved with decode steps to bound per-iteration latency.

## Browsing Home

[[02 Concepts/Lifecycle/Deployment & Serving/LLM & Generative Inference Subject|LLM & Generative Inference]] → [[02 Concepts/Lifecycle/Deployment & Serving/Deployment & Serving Index|Deployment & Serving]]

## Book Passages

These are explicitly recorded related passages from the upstream draft alignment; they do not certify complete coverage.

No explicit passage alignment is recorded for this concept. Subject reading pointers are available in its browsing home.

## Conditional Relationships

These are the taxonomy's draft editorial relationships. Read each relationship with its condition; an outgoing link is not a prerequisite claim.

- Reduces decode stalls in [[02 Concepts/Lifecycle/Deployment & Serving/Time per Output Token|Time per Output Token]]. **Condition:** Holds when long prefills would otherwise stall decode iterations of co-batched requests; it can raise TTFT for the long prompt.

- Is an alternative to [[02 Concepts/Lifecycle/Deployment & Serving/Prefill Decode Disaggregation|Prefill Decode Disaggregation]]. **Condition:** Both limit prefill-decode interference; one colocates with chunking, the other separates pools.

- Piggybacks prefill chunks on [[02 Concepts/Lifecycle/Deployment & Serving/Continuous Batching|Continuous Batching]]. **Condition:** Holds when the scheduler admits work at each iteration under a per-iteration token budget.

- Bounds prefill work per iteration to limit [[02 Concepts/Foundations/Quantitative System Models/Head of Line Blocking|Head of Line Blocking]]. **Condition:** When a long prompt's prefill would otherwise hold the decode step of every co-batched request.

## Source

[Canonical Taxonomy](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/taxonomy.yml) · [Passage Alignment](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/mlsysbook-alignment.yml)

Taxonomy definitions and relationship wording: CC BY 4.0, with attribution to the Machine Learning Systems curriculum by Vijay Janapa Reddi and contributors. The textbook retains its separate license.
