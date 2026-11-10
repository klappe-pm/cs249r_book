---
title: KV Cache Transfer
type: concept
tags:
- Type/Concept
- Group/Lifecycle
- Topic/LLM_Generative_Inference
source_repository: https://github.com/klappe-pm/cs249r_book
source_commit: de87c0103806d7bfb1c677dbb77a2b92fa00c298
source_path: taxonomy/taxonomy.yml
source_label: KV-cache transfer
taxonomy_id: mlsys.kv-cache-transfer
taxonomy_status: draft
taxonomy_version: 0.4-draft
---

# KV Cache Transfer

Shipping KV state between instances or nodes, as in disaggregated prefill and decode or cross-instance prefix reuse, overlapped with compute to hide network latency.

## Browsing Home

[[02 Concepts/Lifecycle/Deployment & Serving/LLM & Generative Inference Subject|LLM & Generative Inference]] → [[02 Concepts/Lifecycle/Deployment & Serving/Deployment & Serving Index|Deployment & Serving]]

## Book Passages

These are explicitly recorded related passages from the upstream draft alignment; they do not certify complete coverage.

No explicit passage alignment is recorded for this concept. Subject reading pointers are available in its browsing home.

## Conditional Relationships

These are the taxonomy's draft editorial relationships. Read each relationship with its condition; an outgoing link is not a prerequisite claim.

- Moves state with [[02 Concepts/Stack/Hardware & Accelerators/Peer to Peer Device Transfer|Peer to Peer Device Transfer]]. **Condition:** Direct device or NIC transfers avoid staging KV blocks through host memory.

- Uses [[02 Concepts/Stack/Datacenter Infrastructure & Fleet/Remote Direct Memory Access|Remote Direct Memory Access]]. **Condition:** Applies in disaggregated clusters with RDMA fabrics.

- Hides latency with [[02 Concepts/Stack/Parallelism & Distributed Execution/Communication Overlap|Communication Overlap]]. **Condition:** Holds when layer-wise KV transfer can proceed while later layers still compute.

## Search Terms

Upstream search terms may be related terms rather than exact synonyms: KV migration.

## Source

[Canonical Taxonomy](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/taxonomy.yml) · [Passage Alignment](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/mlsysbook-alignment.yml)

Taxonomy definitions and relationship wording: CC BY 4.0, with attribution to the Machine Learning Systems curriculum by Vijay Janapa Reddi and contributors. The textbook retains its separate license.
