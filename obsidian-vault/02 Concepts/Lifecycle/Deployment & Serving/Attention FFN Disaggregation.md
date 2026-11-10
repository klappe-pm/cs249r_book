---
title: Attention FFN Disaggregation
type: concept
tags:
- Type/Concept
- Group/Lifecycle
- Topic/LLM_Generative_Inference
source_repository: https://github.com/klappe-pm/cs249r_book
source_commit: de87c0103806d7bfb1c677dbb77a2b92fa00c298
source_path: taxonomy/taxonomy.yml
source_label: Attention-FFN disaggregation
taxonomy_id: mlsys.attention-ffn-disaggregation
taxonomy_status: draft
taxonomy_version: 0.4-draft
---

# Attention FFN Disaggregation

Running attention layers and the feed-forward or expert layers on separate accelerator pools during decode, so memory-bound attention over the KV cache and compute-bound expert matmuls are each batched and provisioned on hardware suited to them, at the cost of streaming activations between pools at every layer.

## Browsing Home

[[02 Concepts/Lifecycle/Deployment & Serving/LLM & Generative Inference Subject|LLM & Generative Inference]] → [[02 Concepts/Lifecycle/Deployment & Serving/Deployment & Serving Index|Deployment & Serving]]

## Book Passages

These are explicitly recorded related passages from the upstream draft alignment; they do not certify complete coverage.

No explicit passage alignment is recorded for this concept. Subject reading pointers are available in its browsing home.

## Conditional Relationships

These are the taxonomy's draft editorial relationships. Read each relationship with its condition; an outgoing link is not a prerequisite claim.

- Pools tokens from many attention instances to raise the expert-side [[02 Concepts/Foundations/Quantitative System Models/Arithmetic Intensity|Arithmetic Intensity]]. **Condition:** When the FFN or expert pool batches tokens across several attention replicas, so each weight read serves more tokens.

- Hides inter-pool activation transfer with [[02 Concepts/Stack/Parallelism & Distributed Execution/Communication Overlap|Communication Overlap]]. **Condition:** When micro-batches are pipelined so one batch computes while another's activations are in flight.

- Serves the expert pool with [[02 Concepts/Stack/Parallelism & Distributed Execution/Expert Parallelism|Expert Parallelism]]. **Condition:** For mixture-of-experts models whose experts are spread across the FFN pool.

- Adds a per-layer activation transfer that lengthens [[02 Concepts/Lifecycle/Deployment & Serving/Inter Token Latency|Inter Token Latency]]. **Condition:** When the activation exchange between pools is not hidden by ping-pong micro-batching.

- Can place each pool on a different accelerator type through [[02 Concepts/Stack/Parallelism & Distributed Execution/Heterogeneous Accelerator Training and Serving|Heterogeneous Accelerator Training and Serving]]. **Condition:** When attention is deployed on bandwidth-rich devices and FFN on compute-rich devices.

## Search Terms

Upstream search terms may be related terms rather than exact synonyms: AFD; attention-expert disaggregation; ping-pong pipelined decoding; disaggregated expert parallelism.

## Source

[Canonical Taxonomy](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/taxonomy.yml) · [Passage Alignment](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/mlsysbook-alignment.yml)

Taxonomy definitions and relationship wording: CC BY 4.0, with attribution to the Machine Learning Systems curriculum by Vijay Janapa Reddi and contributors. The textbook retains its separate license.
