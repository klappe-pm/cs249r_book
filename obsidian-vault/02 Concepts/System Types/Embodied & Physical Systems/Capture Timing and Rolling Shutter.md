---
title: Capture Timing and Rolling Shutter
type: concept
tags:
- Type/Concept
- Group/System_Types
- Topic/Sensing_Perception_Fusion
- Context/Background
source_repository: https://github.com/klappe-pm/cs249r_book
source_commit: de87c0103806d7bfb1c677dbb77a2b92fa00c298
source_path: taxonomy/taxonomy.yml
source_label: Capture timing and rolling shutter
taxonomy_id: mlsys.capture-epoch
taxonomy_status: draft
taxonomy_version: 0.4-draft
---

# Capture Timing and Rolling Shutter

The time or interval over which a measurement is acquired, whose spread across rows or beams can require motion compensation before observations are fused.

## Browsing Home

[[02 Concepts/System Types/Embodied & Physical Systems/Sensing, Perception & Fusion Subject|Sensing, Perception & Fusion]] → [[02 Concepts/System Types/Embodied & Physical Systems/Embodied & Physical Systems Index|Embodied & Physical Systems]]

This is a background concept on which ML systems reasoning depends; that classification does not make it optional.

## Book Passages

These are explicitly recorded related passages from the upstream draft alignment; they do not certify complete coverage.

No explicit passage alignment is recorded for this concept. Subject reading pointers are available in its browsing home.

## Conditional Relationships

These are the taxonomy's draft editorial relationships. Read each relationship with its condition; an outgoing link is not a prerequisite claim.

- Fixes the start instant of [[02 Concepts/System Types/Embodied & Physical Systems/Observation Age|Observation Age]]. **Condition:** Observation age is measured from the capture epoch, not from the frame's arrival at the processor.

- Misaligns measurements taken at different instants within [[02 Concepts/System Types/Embodied & Physical Systems/Sensor Fusion|Sensor Fusion]]. **Condition:** When the platform or scene moves during exposure or a scan and the measurements are not de-skewed before fusion.

## Search Terms

Upstream search terms may be related terms rather than exact synonyms: rolling shutter; global shutter; capture timestamp; capture epoch.

## Source

[Canonical Taxonomy](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/taxonomy.yml) · [Passage Alignment](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/mlsysbook-alignment.yml)

Taxonomy definitions and relationship wording: CC BY 4.0, with attribution to the Machine Learning Systems curriculum by Vijay Janapa Reddi and contributors. The textbook retains its separate license.
