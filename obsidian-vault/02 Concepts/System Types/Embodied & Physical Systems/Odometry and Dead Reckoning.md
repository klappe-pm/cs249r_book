---
title: Odometry and Dead Reckoning
type: concept
tags:
- Type/Concept
- Group/System_Types
- Topic/State_Estimation_Localization_Mapping
- Context/Background
source_repository: https://github.com/klappe-pm/cs249r_book
source_commit: de87c0103806d7bfb1c677dbb77a2b92fa00c298
source_path: taxonomy/taxonomy.yml
source_label: Odometry and dead reckoning
taxonomy_id: mlsys.odometry
taxonomy_status: draft
taxonomy_version: 0.4-draft
---

# Odometry and Dead Reckoning

Estimating a platform's pose change by integrating its own motion measurements, from wheel encoders, inertial units, or feature motion in camera and lidar frames, whose error grows without bound with distance traveled unless corrected by loop closure or an external reference.

## Browsing Home

[[02 Concepts/System Types/Embodied & Physical Systems/State Estimation, Localization & Mapping Subject|State Estimation, Localization & Mapping]] → [[02 Concepts/System Types/Embodied & Physical Systems/Embodied & Physical Systems Index|Embodied & Physical Systems]]

This is a background concept on which ML systems reasoning depends; that classification does not make it optional.

## Book Passages

These are explicitly recorded related passages from the upstream draft alignment; they do not certify complete coverage.

No explicit passage alignment is recorded for this concept. Subject reading pointers are available in its browsing home.

## Conditional Relationships

These are the taxonomy's draft editorial relationships. Read each relationship with its condition; an outgoing link is not a prerequisite claim.

- Is the relative-motion, drift-accumulating form of [[02 Concepts/System Types/Embodied & Physical Systems/State Estimation|State Estimation]]. **Condition:** Only relative motion is measured, so absolute pose is unobservable without an external reference.

- Accumulates pose in the odometry frame defined by [[02 Concepts/System Types/Embodied & Physical Systems/Coordinate Frames and Transforms|Coordinate Frames and Transforms]]. **Condition:** In systems that keep a continuous odometry frame beneath a map frame, so the map-to-odometry transform absorbs drift correction.

## Search Terms

Upstream search terms may be related terms rather than exact synonyms: odometry; dead reckoning; wheel odometry; visual odometry; visual-inertial odometry; inertial integration.

## Source

[Canonical Taxonomy](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/taxonomy.yml) · [Passage Alignment](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/mlsysbook-alignment.yml)

Taxonomy definitions and relationship wording: CC BY 4.0, with attribution to the Machine Learning Systems curriculum by Vijay Janapa Reddi and contributors. The textbook retains its separate license.
