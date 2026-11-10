---
title: Motion Planning
type: concept
tags:
- Type/Concept
- Group/System_Types
- Topic/Motion_Planning_Control
- Context/Background
source_repository: https://github.com/klappe-pm/cs249r_book
source_commit: de87c0103806d7bfb1c677dbb77a2b92fa00c298
source_path: taxonomy/taxonomy.yml
source_label: Motion planning
taxonomy_id: mlsys.motion-planning
taxonomy_status: draft
taxonomy_version: 0.4-draft
---

# Motion Planning

Computing a collision-free path or trajectory from a start to a goal configuration using search, sampling, or trajectory optimization.

## Browsing Home

[[02 Concepts/System Types/Embodied & Physical Systems/Motion Planning & Control Subject|Motion Planning & Control]] → [[02 Concepts/System Types/Embodied & Physical Systems/Embodied & Physical Systems Index|Embodied & Physical Systems]]

This is a background concept on which ML systems reasoning depends; that classification does not make it optional.

## Book Passages

These are explicitly recorded related passages from the upstream draft alignment; they do not certify complete coverage.

No explicit passage alignment is recorded for this concept. Subject reading pointers are available in its browsing home.

## Conditional Relationships

These are the taxonomy's draft editorial relationships. Read each relationship with its condition; an outgoing link is not a prerequisite claim.

- Must satisfy [[02 Concepts/System Types/Embodied & Physical Systems/Trajectory Feasibility|Trajectory Feasibility]]. **Condition:** Geometric planners need a later step to enforce dynamic and actuation limits.

- Requires [[02 Concepts/System Types/Embodied & Physical Systems/State Estimation|State Estimation]]. **Condition:** Plans are valid only relative to the estimated pose and map they start from.

- Plans over maps from [[02 Concepts/System Types/Embodied & Physical Systems/Simultaneous Localization and Mapping|Simultaneous Localization and Mapping]]. **Condition:** When the environment is not known in advance and the map is built online.

- Plans against the predicted occupancy from [[02 Concepts/System Types/Embodied & Physical Systems/Motion Forecasting|Motion Forecasting]]. **Condition:** In environments shared with other moving agents such as people or vehicles.

- Maps between task and configuration space with [[02 Concepts/System Types/Embodied & Physical Systems/Robot Kinematics|Robot Kinematics]]. **Condition:** When goals are given as end-effector poses.

- Answers collision and clearance queries against the [[02 Concepts/System Types/Embodied & Physical Systems/mAP Representation|mAP Representation]]. **Condition:** The representation must support the query the planner issues at planning rate, such as distance-to-obstacle or occupancy lookup.

## Source

[Canonical Taxonomy](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/taxonomy.yml) · [Passage Alignment](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/mlsysbook-alignment.yml)

Taxonomy definitions and relationship wording: CC BY 4.0, with attribution to the Machine Learning Systems curriculum by Vijay Janapa Reddi and contributors. The textbook retains its separate license.
