---
title: UPS and Battery Energy Storage
type: concept
tags:
- Type/Concept
- Group/Stack
- Topic/Datacenter_Power_Cooling_Facilities
- Context/Background
source_repository: https://github.com/klappe-pm/cs249r_book
source_commit: de87c0103806d7bfb1c677dbb77a2b92fa00c298
source_path: taxonomy/taxonomy.yml
source_label: UPS and battery energy storage
taxonomy_id: mlsys.facility-energy-storage
taxonomy_status: draft
taxonomy_version: 0.4-draft
---

# UPS and Battery Energy Storage

Facility batteries that carry load through outages until generators start and can also buffer fast load swings or shave demand peaks.

## Browsing Home

[[02 Concepts/Stack/Datacenter Infrastructure & Fleet/Datacenter Power, Cooling & Facilities Subject|Datacenter Power, Cooling & Facilities]] → [[02 Concepts/Stack/Datacenter Infrastructure & Fleet/Datacenter Infrastructure & Fleet Index|Datacenter Infrastructure & Fleet]]

This is a background concept on which ML systems reasoning depends; that classification does not make it optional.

## Book Passages

These are explicitly recorded related passages from the upstream draft alignment; they do not certify complete coverage.

No explicit passage alignment is recorded for this concept. Subject reading pointers are available in its browsing home.

## Conditional Relationships

These are the taxonomy's draft editorial relationships. Read each relationship with its condition; an outgoing link is not a prerequisite claim.

- Buffers [[02 Concepts/Stack/Datacenter Infrastructure & Fleet/Synchronous Training Power Swings|Synchronous Training Power Swings]]. **Condition:** Storage sized and controlled to respond at the swing frequency.

- Raises [[02 Concepts/Qualities/Reliability & Fault Tolerance/Availability|Availability]]. **Condition:** Carrying load through utility outages until generators take over.

## Search Terms

Upstream search terms may be related terms rather than exact synonyms: UPS; uninterruptible power supply; BESS.

## Source

[Canonical Taxonomy](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/taxonomy.yml) · [Passage Alignment](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/mlsysbook-alignment.yml)

Taxonomy definitions and relationship wording: CC BY 4.0, with attribution to the Machine Learning Systems curriculum by Vijay Janapa Reddi and contributors. The textbook retains its separate license.
