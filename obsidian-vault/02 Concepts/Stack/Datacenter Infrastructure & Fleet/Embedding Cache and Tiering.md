---
title: Embedding Cache and Tiering
type: concept
tags:
- Type/Concept
- Group/Stack
- Topic/Storage_Data_Delivery
source_repository: https://github.com/klappe-pm/cs249r_book
source_commit: de87c0103806d7bfb1c677dbb77a2b92fa00c298
source_path: taxonomy/taxonomy.yml
source_label: Embedding cache and tiering
taxonomy_id: mlsys.embedding-cache
taxonomy_status: draft
taxonomy_version: 0.4-draft
---

# Embedding Cache and Tiering

Keeping frequently accessed embedding rows in accelerator memory and cold rows in host memory or SSD, exploiting the skew of lookups.

## Browsing Home

[[02 Concepts/Stack/Datacenter Infrastructure & Fleet/Storage & Data Delivery Subject|Storage & Data Delivery]] → [[02 Concepts/Stack/Datacenter Infrastructure & Fleet/Datacenter Infrastructure & Fleet Index|Datacenter Infrastructure & Fleet]]

## Book Passages

These are explicitly recorded related passages from the upstream draft alignment; they do not certify complete coverage.

No explicit passage alignment is recorded for this concept. Subject reading pointers are available in its browsing home.

## Conditional Relationships

These are the taxonomy's draft editorial relationships. Read each relationship with its condition; an outgoing link is not a prerequisite claim.

- Is a kind of [[02 Concepts/Stack/Datacenter Infrastructure & Fleet/Storage Tiering and Caching|Storage Tiering and Caching]]. **Condition:** Rows are placed across accelerator memory, host memory, and SSD by access frequency.

- Keeps only hot embedding rows resident, shrinking the accelerator-side [[02 Concepts/Foundations/Workloads & Requirements/Memory Footprint|Memory Footprint]]. **Condition:** When footprint is measured in accelerator memory and lookup skew lets cold rows live in host memory or SSD; total stored model bytes are unchanged.

## Search Terms

Upstream search terms may be related terms rather than exact synonyms: embedding offload.

## Source

[Canonical Taxonomy](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/taxonomy.yml) · [Passage Alignment](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/mlsysbook-alignment.yml)

Taxonomy definitions and relationship wording: CC BY 4.0, with attribution to the Machine Learning Systems curriculum by Vijay Janapa Reddi and contributors. The textbook retains its separate license.
