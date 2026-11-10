---
title: Simultaneous Localization and Mapping
type: concept
tags:
- Type/Concept
- Group/System_Types
- Topic/State_Estimation_Localization_Mapping
- Context/Background
source_repository: https://github.com/klappe-pm/cs249r_book
source_commit: de87c0103806d7bfb1c677dbb77a2b92fa00c298
source_path: taxonomy/taxonomy.yml
source_label: Simultaneous localization and mapping
taxonomy_id: mlsys.slam
taxonomy_status: draft
taxonomy_version: 0.4-draft
---

# Simultaneous Localization and Mapping

Jointly estimating a platform's pose and a map of an unknown environment from its own sensor observations.

## Browsing Home

[[02 Concepts/System Types/Embodied & Physical Systems/State Estimation, Localization & Mapping Subject|State Estimation, Localization & Mapping]] → [[02 Concepts/System Types/Embodied & Physical Systems/Embodied & Physical Systems Index|Embodied & Physical Systems]]

This is a background concept on which ML systems reasoning depends; that classification does not make it optional.

## Book Passages

These are explicitly recorded related passages from the upstream draft alignment; they do not certify complete coverage.

No explicit passage alignment is recorded for this concept. Subject reading pointers are available in its browsing home.

## Conditional Relationships

These are the taxonomy's draft editorial relationships. Read each relationship with its condition; an outgoing link is not a prerequisite claim.

- Specializes [[02 Concepts/System Types/Embodied & Physical Systems/State Estimation|State Estimation]]. **Condition:** Drift accumulates without loop closure or external references.

- Takes its motion prior between keyframes from [[02 Concepts/System Types/Embodied & Physical Systems/Odometry and Dead Reckoning|Odometry and Dead Reckoning]]. **Condition:** When the front end propagates pose with odometry and the back end corrects drift at loop closure.

- Builds and maintains the [[02 Concepts/System Types/Embodied & Physical Systems/mAP Representation|mAP Representation]]. **Condition:** When mapping runs online from the platform's own observations.

## Search Terms

Upstream search terms may be related terms rather than exact synonyms: SLAM.

## Source

[Canonical Taxonomy](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/taxonomy.yml) · [Passage Alignment](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/mlsysbook-alignment.yml)

Taxonomy definitions and relationship wording: CC BY 4.0, with attribution to the Machine Learning Systems curriculum by Vijay Janapa Reddi and contributors. The textbook retains its separate license.
