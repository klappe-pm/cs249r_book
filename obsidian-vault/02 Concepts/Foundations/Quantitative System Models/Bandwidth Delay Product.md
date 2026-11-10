---
title: Bandwidth Delay Product
type: concept
tags:
- Type/Concept
- Group/Foundations
- Topic/Queueing_Capacity_Models
- Context/Background
source_repository: https://github.com/klappe-pm/cs249r_book
source_commit: de87c0103806d7bfb1c677dbb77a2b92fa00c298
source_path: taxonomy/taxonomy.yml
source_label: Bandwidth-delay product
taxonomy_id: mlsys.bandwidth-delay-product
taxonomy_status: draft
taxonomy_version: 0.4-draft
---

# Bandwidth Delay Product

A path's bottleneck bandwidth times its round-trip time, the amount of outstanding data a window-controlled flow must sustain to keep the path full.

## Browsing Home

[[02 Concepts/Foundations/Quantitative System Models/Queueing & Capacity Models Subject|Queueing & Capacity Models]] → [[02 Concepts/Foundations/Quantitative System Models/Quantitative System Models Index|Quantitative System Models]]

This is a background concept on which ML systems reasoning depends; that classification does not make it optional.

## Book Passages

These are explicitly recorded related passages from the upstream draft alignment; they do not certify complete coverage.

No explicit passage alignment is recorded for this concept. Subject reading pointers are available in its browsing home.

## Conditional Relationships

These are the taxonomy's draft editorial relationships. Read each relationship with its condition; an outgoing link is not a prerequisite claim.

- Sets the window that [[02 Concepts/Stack/Datacenter Infrastructure & Fleet/Datacenter Congestion Control|Datacenter Congestion Control]]. **Condition:** When a window-controlled flow must keep a long or fast path full while acknowledgments are in flight.

## Search Terms

Upstream search terms may be related terms rather than exact synonyms: BDP.

## Source

[Canonical Taxonomy](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/taxonomy.yml) · [Passage Alignment](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/mlsysbook-alignment.yml)

Taxonomy definitions and relationship wording: CC BY 4.0, with attribution to the Machine Learning Systems curriculum by Vijay Janapa Reddi and contributors. The textbook retains its separate license.
