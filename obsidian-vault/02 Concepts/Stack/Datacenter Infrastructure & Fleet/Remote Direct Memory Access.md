---
title: Remote Direct Memory Access
type: concept
tags:
- Type/Concept
- Group/Stack
- Topic/Network_Fabrics
- Context/Background
source_repository: https://github.com/klappe-pm/cs249r_book
source_commit: de87c0103806d7bfb1c677dbb77a2b92fa00c298
source_path: taxonomy/taxonomy.yml
source_label: Remote direct memory access
taxonomy_id: mlsys.rdma
taxonomy_status: draft
taxonomy_version: 0.4-draft
---

# Remote Direct Memory Access

Network transfers that read or write remote memory directly through the network interface without remote CPU involvement, giving low latency and high throughput.

## Browsing Home

[[02 Concepts/Stack/Datacenter Infrastructure & Fleet/Network Fabrics Subject|Network Fabrics]] → [[02 Concepts/Stack/Datacenter Infrastructure & Fleet/Datacenter Infrastructure & Fleet Index|Datacenter Infrastructure & Fleet]]

This is a background concept on which ML systems reasoning depends; that classification does not make it optional.

## Book Passages

These are explicitly recorded related passages from the upstream draft alignment; they do not certify complete coverage.

No explicit passage alignment is recorded for this concept. Subject reading pointers are available in its browsing home.

## Conditional Relationships

These are the taxonomy's draft editorial relationships. Read each relationship with its condition; an outgoing link is not a prerequisite claim.

- Lowers per-message overhead of [[02 Concepts/Stack/Parallelism & Distributed Execution/Collective Communication|Collective Communication]]. **Condition:** Transfers bypass host network stacks and remote CPUs.

- Can read and write device memory through [[02 Concepts/Stack/Hardware & Accelerators/Peer to Peer Device Transfer|Peer to Peer Device Transfer]]. **Condition:** The NIC and driver support direct access to accelerator memory.

- Avoids costly go-back-N retransmissions on fast links through [[02 Concepts/Stack/Datacenter Infrastructure & Fleet/Forward Error Correction|Forward Error Correction]]. **Condition:** When the RDMA transport recovers from loss by go-back-N retransmission, so even rare uncorrected bit errors would stall throughput.

## Search Terms

Upstream search terms may be related terms rather than exact synonyms: RDMA; InfiniBand; RoCE.

## Source

[Canonical Taxonomy](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/taxonomy.yml) · [Passage Alignment](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/mlsysbook-alignment.yml)

Taxonomy definitions and relationship wording: CC BY 4.0, with attribution to the Machine Learning Systems curriculum by Vijay Janapa Reddi and contributors. The textbook retains its separate license.
