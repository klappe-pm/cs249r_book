---
title: Sequential Versus Random Storage Access
type: concept
tags:
- Type/Concept
- Group/Stack
- Topic/Storage_Data_Delivery
- Context/Background
source_repository: https://github.com/klappe-pm/cs249r_book
source_commit: de87c0103806d7bfb1c677dbb77a2b92fa00c298
source_path: taxonomy/taxonomy.yml
source_label: Sequential versus random storage access
taxonomy_id: mlsys.storage-access-pattern
taxonomy_status: draft
taxonomy_version: 0.4-draft
---

# Sequential Versus Random Storage Access

Whether a workload reads storage in large contiguous ranges or in many small scattered requests, which decides whether sequential throughput or per-request latency and IOPS bound it, and so which media, layout, and shard sizes suit it.

## Browsing Home

[[02 Concepts/Stack/Datacenter Infrastructure & Fleet/Storage & Data Delivery Subject|Storage & Data Delivery]] → [[02 Concepts/Stack/Datacenter Infrastructure & Fleet/Datacenter Infrastructure & Fleet Index|Datacenter Infrastructure & Fleet]]

This is a background concept on which ML systems reasoning depends; that classification does not make it optional.

## Book Passages

These are explicitly recorded related passages from the upstream draft alignment; they do not certify complete coverage.

No explicit passage alignment is recorded for this concept. Subject reading pointers are available in its browsing home.

## Conditional Relationships

These are the taxonomy's draft editorial relationships. Read each relationship with its condition; an outgoing link is not a prerequisite claim.

- Motivates large sequential shards in [[02 Concepts/Lifecycle/Data Engineering/Dataset Storage Layout|Dataset Storage Layout]]. **Condition:** When training streams whole corpora so sequential bandwidth, not IOPS, is the binding resource.

- Bounds the read stage of [[02 Concepts/Stack/Frameworks, Compilers & Runtimes/Training Input Pipeline|Training Input Pipeline]]. **Condition:** When examples are fetched by many small random reads from media or stores with high per-request latency.

- Decides which tier serves which data in [[02 Concepts/Stack/Datacenter Infrastructure & Fleet/Storage Tiering and Caching|Storage Tiering and Caching]]. **Condition:** When random-access working sets, such as retrieval indexes or hot shards, are kept on NVMe or in memory while bulk corpora stream from capacity tiers.

## Search Terms

Upstream search terms may be related terms rather than exact synonyms: storage access pattern; sequential storage access; random storage access.

## Source

[Canonical Taxonomy](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/taxonomy.yml) · [Passage Alignment](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/mlsysbook-alignment.yml)

Taxonomy definitions and relationship wording: CC BY 4.0, with attribution to the Machine Learning Systems curriculum by Vijay Janapa Reddi and contributors. The textbook retains its separate license.
