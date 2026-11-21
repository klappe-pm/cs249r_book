---
title: Real Time Fieldbus
type: concept
tags:
- Type/Concept
- Group/System_Types
- Topic/Real_Time_Mixed_Criticality_Computing
- Context/Background
source_repository: https://github.com/klappe-pm/cs249r_book
source_commit: de87c0103806d7bfb1c677dbb77a2b92fa00c298
source_path: taxonomy/taxonomy.yml
source_label: Real-time fieldbus
taxonomy_id: mlsys.deterministic-field-network
taxonomy_status: draft
taxonomy_version: 0.4-draft
---

# Real Time Fieldbus

A device network engineered to provide bounded delivery under stated traffic and scheduling assumptions, whose cycle time and occupancy constrain sensing and control deadlines.

## Browsing Home

[[02 Concepts/System Types/Embodied & Physical Systems/Real Time & Mixed Criticality Computing Subject|Real Time & Mixed Criticality Computing]] → [[02 Concepts/System Types/Embodied & Physical Systems/Embodied & Physical Systems Index|Embodied & Physical Systems]]

This is a background concept on which ML systems reasoning depends; that classification does not make it optional.

## Book Passages

These are explicitly recorded related passages from the upstream draft alignment; they do not certify complete coverage.

No explicit passage alignment is recorded for this concept. Subject reading pointers are available in its browsing home.

## Conditional Relationships

These are the taxonomy's draft editorial relationships. Read each relationship with its condition; an outgoing link is not a prerequisite claim.

- Adds a bounded transport and cycle-time term to [[02 Concepts/System Types/Embodied & Physical Systems/Feedback Delay|Feedback Delay]]. **Condition:** When drives and sensors are reached over the bus rather than on-chip.

- Bounds, by bus occupancy, the achievable period of [[02 Concepts/System Types/Embodied & Physical Systems/Real Time Scheduling|Real Time Scheduling]]. **Condition:** When the control task's period must fit the bus cycle and the number of devices on it.

- Bounds the transport contribution to [[02 Concepts/System Types/Embodied & Physical Systems/Timing Jitter|Timing Jitter]]. **Condition:** When control messages use synchronized, fixed transmission slots with bounded interfering traffic; the bound concerns network-induced variation rather than all sensing, computation, and actuation jitter.

## Search Terms

Upstream search terms may be related terms rather than exact synonyms: EtherCAT; time-sensitive networking; TSN; time-triggered bus; scheduled CAN; deterministic field network.

## Source

[Canonical Taxonomy](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/taxonomy.yml) · [Passage Alignment](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/mlsysbook-alignment.yml)

Taxonomy definitions and relationship wording: CC BY 4.0, with attribution to the Machine Learning Systems curriculum by Vijay Janapa Reddi and contributors. The textbook retains its separate license.
