---
title: Object Storage
type: concept
tags:
- Type/Concept
- Group/Stack
- Topic/Storage_Data_Delivery
- Context/Background
source_repository: https://github.com/klappe-pm/cs249r_book
source_commit: de87c0103806d7bfb1c677dbb77a2b92fa00c298
source_path: taxonomy/taxonomy.yml
source_label: Object storage
taxonomy_id: mlsys.object-storage
taxonomy_status: draft
taxonomy_version: 0.4-draft
---

# Object Storage

Storage of immutable named objects behind an HTTP-style interface, offering scalable capacity and throughput with higher per-request latency than file systems.

## Browsing Home

[[02 Concepts/Stack/Datacenter Infrastructure & Fleet/Storage & Data Delivery Subject|Storage & Data Delivery]] → [[02 Concepts/Stack/Datacenter Infrastructure & Fleet/Datacenter Infrastructure & Fleet Index|Datacenter Infrastructure & Fleet]]

This is a background concept on which ML systems reasoning depends; that classification does not make it optional.

## Book Passages

These are explicitly recorded related passages from the upstream draft alignment; they do not certify complete coverage.

No explicit passage alignment is recorded for this concept. Subject reading pointers are available in its browsing home.

## Conditional Relationships

These are the taxonomy's draft editorial relationships. Read each relationship with its condition; an outgoing link is not a prerequisite claim.

- Commonly forms the capacity tier in [[02 Concepts/Stack/Datacenter Infrastructure & Fleet/Storage Tiering and Caching|Storage Tiering and Caching]]. **Condition:** Hot data is cached closer to compute.

- Favors large sequential shards in [[02 Concepts/Lifecycle/Data Engineering/Dataset Storage Layout|Dataset Storage Layout]]. **Condition:** Per-request latency is high, so many small reads are slow.

- Protects stored objects with [[02 Concepts/Stack/Datacenter Infrastructure & Fleet/Erasure Coding|Erasure Coding]]. **Condition:** When the store keeps parity fragments rather than full copies.

## Source

[Canonical Taxonomy](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/taxonomy.yml) · [Passage Alignment](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/mlsysbook-alignment.yml)

Taxonomy definitions and relationship wording: CC BY 4.0, with attribution to the Machine Learning Systems curriculum by Vijay Janapa Reddi and contributors. The textbook retains its separate license.
