---
title: Host Device Interconnect
type: concept
tags:
- Type/Concept
- Group/Stack
- Topic/Host_Device_Scale_Up_Interconnect
source_repository: https://github.com/klappe-pm/cs249r_book
source_commit: de87c0103806d7bfb1c677dbb77a2b92fa00c298
source_path: taxonomy/taxonomy.yml
source_label: Host-device interconnect
taxonomy_id: mlsys.host-device-interconnect
taxonomy_status: draft
taxonomy_version: 0.4-draft
---

# Host Device Interconnect

Communication path through which a host and accelerator exchange data and control, with transport, topology, and memory-access semantics that affect transfers.

## Browsing Home

[[02 Concepts/Stack/Hardware & Accelerators/Host Device & Scale Up Interconnect Subject|Host Device & Scale Up Interconnect]] → [[02 Concepts/Stack/Hardware & Accelerators/Hardware & Accelerators Index|Hardware & Accelerators]]

## Book Passages

These are explicitly recorded related passages from the upstream draft alignment; they do not certify complete coverage.

No explicit passage alignment is recorded for this concept. Subject reading pointers are available in its browsing home.

## Conditional Relationships

These are the taxonomy's draft editorial relationships. Read each relationship with its condition; an outgoing link is not a prerequisite claim.

- Can add transfer delay to [[02 Concepts/Qualities/Performance, Efficiency & Benchmarking/Execution Time|Execution Time]]. **Condition:** When the measured execution boundary includes traffic crossing the host-device path, transport, topology, contention, reuse, and overlap determine its contribution; fully hidden transfers need not increase end-to-end time.

- Bounds the throughput of [[02 Concepts/Lifecycle/Training & Adaptation/Training State Offloading|Training State Offloading]]. **Condition:** Offloaded optimizer state, parameters, or activations cross the host link every step.

- Bounds reload rate in [[02 Concepts/Lifecycle/Deployment & Serving/KV Cache Offloading and Tiering|KV Cache Offloading and Tiering]]. **Condition:** Offloaded KV blocks return to device memory over the host link on reuse.

- Caps the transfer rate available to [[02 Concepts/Lifecycle/Deployment & Serving/CPU GPU Hybrid Inference|CPU GPU Hybrid Inference]]. **Condition:** Activations or KV state cross the host link at each step.

- Bounds the expert-loading rate of [[02 Concepts/Lifecycle/Deployment & Serving/Expert Offloading|Expert Offloading]]. **Condition:** When each batch needs experts that are not already resident in accelerator memory.

- Bounds how fast models can be loaded in [[02 Concepts/Lifecycle/Deployment & Serving/Model Swapping and Residency|Model Swapping and Residency]]. **Condition:** When a model's weights must move from host memory or storage before it can serve.

## Source

[Canonical Taxonomy](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/taxonomy.yml) · [Passage Alignment](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/mlsysbook-alignment.yml)

Taxonomy definitions and relationship wording: CC BY 4.0, with attribution to the Machine Learning Systems curriculum by Vijay Janapa Reddi and contributors. The textbook retains its separate license.
