---
title: Erasure Coding
type: concept
tags:
- Type/Concept
- Group/Stack
- Topic/Storage_Data_Delivery
- Context/Background
source_repository: https://github.com/klappe-pm/cs249r_book
source_commit: de87c0103806d7bfb1c677dbb77a2b92fa00c298
source_path: taxonomy/taxonomy.yml
source_label: Erasure coding
taxonomy_id: mlsys.erasure-coding
taxonomy_status: draft
taxonomy_version: 0.4-draft
---

# Erasure Coding

Encoding stored data into data and parity fragments so it can be reconstructed after a bounded number of fragment losses, trading storage overhead against encoding and recovery work.

## Browsing Home

[[02 Concepts/Stack/Datacenter Infrastructure & Fleet/Storage & Data Delivery Subject|Storage & Data Delivery]] → [[02 Concepts/Stack/Datacenter Infrastructure & Fleet/Datacenter Infrastructure & Fleet Index|Datacenter Infrastructure & Fleet]]

This is a background concept on which ML systems reasoning depends; that classification does not make it optional.

## Book Passages

These are explicitly recorded related passages from the upstream draft alignment; they do not certify complete coverage.

No explicit passage alignment is recorded for this concept. Subject reading pointers are available in its browsing home.

## Conditional Relationships

These are the taxonomy's draft editorial relationships. Read each relationship with its condition; an outgoing link is not a prerequisite claim.

- Provides storage durability with less overhead than the full-copy replication in [[02 Concepts/Qualities/Reliability & Fault Tolerance/Replication and Failover|Replication and Failover]]. **Condition:** For durable stored data at comparable failure tolerance, not for request failover; reads after a loss pay reconstruction cost.

## Search Terms

Upstream search terms may be related terms rather than exact synonyms: Reed-Solomon coding; erasure-coded storage.

## Source

[Canonical Taxonomy](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/taxonomy.yml) · [Passage Alignment](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/mlsysbook-alignment.yml)

Taxonomy definitions and relationship wording: CC BY 4.0, with attribution to the Machine Learning Systems curriculum by Vijay Janapa Reddi and contributors. The textbook retains its separate license.
