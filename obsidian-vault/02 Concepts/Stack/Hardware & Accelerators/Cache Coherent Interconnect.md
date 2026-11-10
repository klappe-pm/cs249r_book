---
title: Cache Coherent Interconnect
type: concept
tags:
- Type/Concept
- Group/Stack
- Topic/Host_Device_Scale_Up_Interconnect
source_repository: https://github.com/klappe-pm/cs249r_book
source_commit: de87c0103806d7bfb1c677dbb77a2b92fa00c298
source_path: taxonomy/taxonomy.yml
source_label: Cache-coherent interconnect
taxonomy_id: mlsys.coherent-interconnect
taxonomy_status: draft
taxonomy_version: 0.4-draft
---

# Cache Coherent Interconnect

A link protocol that lets hosts and devices share or pool memory with hardware coherence, such as CXL over a PCIe physical layer.

## Browsing Home

[[02 Concepts/Stack/Hardware & Accelerators/Host Device & Scale Up Interconnect Subject|Host Device & Scale Up Interconnect]] → [[02 Concepts/Stack/Hardware & Accelerators/Hardware & Accelerators Index|Hardware & Accelerators]]

## Book Passages

These are explicitly recorded related passages from the upstream draft alignment; they do not certify complete coverage.

No explicit passage alignment is recorded for this concept. Subject reading pointers are available in its browsing home.

## Conditional Relationships

These are the taxonomy's draft editorial relationships. Read each relationship with its condition; an outgoing link is not a prerequisite claim.

- Can extend [[02 Concepts/Stack/Hardware & Accelerators/Memory Capacity|Memory Capacity]]. **Condition:** Pooled or attached memory is acceptable at its higher latency.

- Is a kind of [[02 Concepts/Stack/Hardware & Accelerators/Host Device Interconnect|Host Device Interconnect]]. **Condition:** The link adds hardware coherence and load-store memory semantics over a host-device physical layer.

- Can provide a pooled tier for [[02 Concepts/Lifecycle/Deployment & Serving/KV Cache Offloading and Tiering|KV Cache Offloading and Tiering]]. **Condition:** Attached or pooled memory is cheaper than device memory and its higher latency can be overlapped with compute.

- Replaces in hardware the software work of [[02 Concepts/Stack/Hardware & Accelerators/DMA Cache Maintenance|DMA Cache Maintenance]]. **Condition:** When the link keeps device and host caches coherent, making explicit cache maintenance unnecessary.

## Search Terms

Upstream search terms may be related terms rather than exact synonyms: CXL.

## Source

[Canonical Taxonomy](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/taxonomy.yml) · [Passage Alignment](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/mlsysbook-alignment.yml)

Taxonomy definitions and relationship wording: CC BY 4.0, with attribution to the Machine Learning Systems curriculum by Vijay Janapa Reddi and contributors. The textbook retains its separate license.
