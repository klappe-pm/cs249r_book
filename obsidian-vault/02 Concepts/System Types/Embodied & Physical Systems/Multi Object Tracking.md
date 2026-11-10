---
title: Multi Object Tracking
type: concept
tags:
- Type/Concept
- Group/System_Types
- Topic/State_Estimation_Localization_Mapping
source_repository: https://github.com/klappe-pm/cs249r_book
source_commit: de87c0103806d7bfb1c677dbb77a2b92fa00c298
source_path: taxonomy/taxonomy.yml
source_label: Multi-object tracking
taxonomy_id: mlsys.multi-object-tracking
taxonomy_status: draft
taxonomy_version: 0.4-draft
---

# Multi Object Tracking

Maintaining identities and states of multiple moving objects over time by associating new detections with existing tracks and starting or ending tracks.

## Browsing Home

[[02 Concepts/System Types/Embodied & Physical Systems/State Estimation, Localization & Mapping Subject|State Estimation, Localization & Mapping]] → [[02 Concepts/System Types/Embodied & Physical Systems/Embodied & Physical Systems Index|Embodied & Physical Systems]]

## Book Passages

These are explicitly recorded related passages from the upstream draft alignment; they do not certify complete coverage.

No explicit passage alignment is recorded for this concept. Subject reading pointers are available in its browsing home.

## Conditional Relationships

These are the taxonomy's draft editorial relationships. Read each relationship with its condition; an outgoing link is not a prerequisite claim.

- Is a multi-target form of [[02 Concepts/System Types/Embodied & Physical Systems/State Estimation|State Estimation]]. **Condition:** Several objects are observed with unknown correspondence.

- Propagates each track with [[02 Concepts/System Types/Embodied & Physical Systems/Recursive State Filtering|Recursive State Filtering]]. **Condition:** Object motion is modeled between frames.

## Search Terms

Upstream search terms may be related terms rather than exact synonyms: MOT; data association; track management.

## Source

[Canonical Taxonomy](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/taxonomy.yml) · [Passage Alignment](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/mlsysbook-alignment.yml)

Taxonomy definitions and relationship wording: CC BY 4.0, with attribution to the Machine Learning Systems curriculum by Vijay Janapa Reddi and contributors. The textbook retains its separate license.
