---
title: Geo Distributed Training
type: concept
tags:
- Type/Concept
- Group/Stack
- Topic/Parallelization_Planning_Placement
source_repository: https://github.com/klappe-pm/cs249r_book
source_commit: de87c0103806d7bfb1c677dbb77a2b92fa00c298
source_path: taxonomy/taxonomy.yml
source_label: Geo-distributed training
taxonomy_id: mlsys.geo-distributed-training
taxonomy_status: draft
taxonomy_version: 0.4-draft
---

# Geo Distributed Training

Planning one training job across accelerators in several datacenters by placing the low-communication parallelism dimension (pipeline stages, local-SGD replicas, or asynchronous hierarchies) on the long, narrow inter-site links and the bandwidth-hungry dimensions inside each site, and scheduling the WAN transfers against its latency and bandwidth.

## Browsing Home

[[02 Concepts/Stack/Parallelism & Distributed Execution/Parallelization Planning & Placement Subject|Parallelization Planning & Placement]] → [[02 Concepts/Stack/Parallelism & Distributed Execution/Parallelism & Distributed Execution Index|Parallelism & Distributed Execution]]

## Book Passages

These are explicitly recorded related passages from the upstream draft alignment; they do not certify complete coverage.

No explicit passage alignment is recorded for this concept. Subject reading pointers are available in its browsing home.

## Conditional Relationships

These are the taxonomy's draft editorial relationships. Read each relationship with its condition; an outgoing link is not a prerequisite claim.

- Cuts cross-site synchronization frequency with [[02 Concepts/Stack/Parallelism & Distributed Execution/Local SGD|Local SGD]]. **Condition:** When inter-site bandwidth cannot carry per-step gradient exchange.

- Places stage boundaries on inter-site links using [[02 Concepts/Stack/Parallelism & Distributed Execution/Pipeline Parallelism|Pipeline Parallelism]]. **Condition:** When per-micro-batch activations are far smaller than the gradients a data-parallel cut would send across the WAN.

- Extends to the datacenter tier the hierarchy mapping of [[02 Concepts/Stack/Parallelism & Distributed Execution/Hybrid Parallelism|Hybrid Parallelism]]. **Condition:** When the hardware hierarchy runs chip, node, rack, and site, and each dimension is matched to a tier's link speed.

## Search Terms

Upstream search terms may be related terms rather than exact synonyms: cross-datacenter training; multi-datacenter training; cross-region training; WAN training.

## Source

[Canonical Taxonomy](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/taxonomy.yml) · [Passage Alignment](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/mlsysbook-alignment.yml)

Taxonomy definitions and relationship wording: CC BY 4.0, with attribution to the Machine Learning Systems curriculum by Vijay Janapa Reddi and contributors. The textbook retains its separate license.
