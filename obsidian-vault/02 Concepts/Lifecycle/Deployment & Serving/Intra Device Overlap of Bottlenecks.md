---
title: Intra Device Overlap of Bottlenecks
type: concept
tags:
- Type/Concept
- Group/Lifecycle
- Topic/LLM_Generative_Inference
source_repository: https://github.com/klappe-pm/cs249r_book
source_commit: de87c0103806d7bfb1c677dbb77a2b92fa00c298
source_path: taxonomy/taxonomy.yml
source_label: Intra-device overlap of bottlenecks
taxonomy_id: mlsys.intra-device-overlap
taxonomy_status: draft
taxonomy_version: 0.4-draft
---

# Intra Device Overlap of Bottlenecks

Scheduling generative-inference operations with complementary compute, memory, or communication demands concurrently on one accelerator, using small batches or fused kernels so several hardware resources stay busy together.

## Browsing Home

[[02 Concepts/Lifecycle/Deployment & Serving/LLM & Generative Inference Subject|LLM & Generative Inference]] → [[02 Concepts/Lifecycle/Deployment & Serving/Deployment & Serving Index|Deployment & Serving]]

## Book Passages

These are explicitly recorded related passages from the upstream draft alignment; they do not certify complete coverage.

No explicit passage alignment is recorded for this concept. Subject reading pointers are available in its browsing home.

## Conditional Relationships

These are the taxonomy's draft editorial relationships. Read each relationship with its condition; an outgoing link is not a prerequisite claim.

- Co-locates on one device the phases separated by [[02 Concepts/Lifecycle/Deployment & Serving/Prefill Decode Disaggregation|Prefill Decode Disaggregation]]. **Condition:** When a deployment chooses between running prefill and decode on the same devices or on separate pools.

- Keeps several hardware resources busy at once, raising [[02 Concepts/Qualities/Performance, Efficiency & Benchmarking/Resource Utilization|Resource Utilization]]. **Condition:** When the co-scheduled operations are bound by different resources and scheduling overhead stays small.

- Overlaps the prefill and decode work in the mixed batches formed by [[02 Concepts/Lifecycle/Deployment & Serving/Chunked Prefill|Chunked Prefill]]. **Condition:** When chunked prefill puts prefill chunks and decode steps in the same iteration, and a fused kernel runs them on the same compute units.

## Search Terms

Upstream search terms may be related terms rather than exact synonyms: nano-batching; intra-device operation overlap.

## Source

[Canonical Taxonomy](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/taxonomy.yml) · [Passage Alignment](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/mlsysbook-alignment.yml)

Taxonomy definitions and relationship wording: CC BY 4.0, with attribution to the Machine Learning Systems curriculum by Vijay Janapa Reddi and contributors. The textbook retains its separate license.
