---
title: Sensor Fusion
type: concept
tags:
- Type/Concept
- Group/System_Types
- Topic/Sensing_Perception_Fusion
source_repository: https://github.com/klappe-pm/cs249r_book
source_commit: de87c0103806d7bfb1c677dbb77a2b92fa00c298
source_path: taxonomy/taxonomy.yml
source_label: Sensor fusion
taxonomy_id: mlsys.sensor-fusion
taxonomy_status: draft
taxonomy_version: 0.4-draft
---

# Sensor Fusion

Combining measurements from multiple sensors or modalities, at raw, feature, or decision level, into one estimate more accurate or robust than any single source.

## Browsing Home

[[02 Concepts/System Types/Embodied & Physical Systems/Sensing, Perception & Fusion Subject|Sensing, Perception & Fusion]] → [[02 Concepts/System Types/Embodied & Physical Systems/Embodied & Physical Systems Index|Embodied & Physical Systems]]

## Book Passages

These are explicitly recorded related passages from the upstream draft alignment; they do not certify complete coverage.

No explicit passage alignment is recorded for this concept. Subject reading pointers are available in its browsing home.

## Conditional Relationships

These are the taxonomy's draft editorial relationships. Read each relationship with its condition; an outgoing link is not a prerequisite claim.

- Requires [[02 Concepts/System Types/Embodied & Physical Systems/Sensor Time Synchronization|Sensor Time Synchronization]]. **Condition:** Timestamp error translates to spatial error proportional to relative motion.

- Requires extrinsic calibration from [[02 Concepts/System Types/Embodied & Physical Systems/Sensor Calibration|Sensor Calibration]]. **Condition:** Fused estimates inherit calibration errors between sensor frames.

- Increases [[02 Concepts/System Types/Embodied & Physical Systems/State Observability|State Observability]]. **Condition:** When an added modality measures a state the others cannot distinguish, such as scale for monocular vision.

- Uses [[02 Concepts/System Types/Embodied & Physical Systems/Recursive State Filtering|Recursive State Filtering]]. **Condition:** When fused measurements arrive asynchronously and are combined through prediction and correction steps.

- Cross-checks modalities against [[02 Concepts/Qualities/Security & Privacy/Sensor Spoofing|Sensor Spoofing]]. **Condition:** The attacker cannot spoof all modalities consistently.

- Receives synchronized sensor streams through [[02 Concepts/System Types/Embodied & Physical Systems/Robotics Middleware and Dataflow|Robotics Middleware and Dataflow]]. **Condition:** Sensors publish on separate topics consumed by a fusion node.

- Can outvote corrupted readings from [[02 Concepts/System Types/Embodied & Physical Systems/Active Sensor Interference|Active Sensor Interference]]. **Condition:** Independent modalities observe the same scene.

- Projects heterogeneous sensor measurements into a common reference frame using [[02 Concepts/System Types/Embodied & Physical Systems/Coordinate Frames and Transforms|Coordinate Frames and Transforms]]. **Condition:** Before combining camera, lidar, radar, and inertial observations.

- Combines modalities with distinct physical failure modes to mitigate [[02 Concepts/System Types/Embodied & Physical Systems/Sensor Degradation|Sensor Degradation]]. **Condition:** When complementary sensors retain useful measurements and fusion handles degraded inputs.

## Source

[Canonical Taxonomy](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/taxonomy.yml) · [Passage Alignment](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/mlsysbook-alignment.yml)

Taxonomy definitions and relationship wording: CC BY 4.0, with attribution to the Machine Learning Systems curriculum by Vijay Janapa Reddi and contributors. The textbook retains its separate license.
