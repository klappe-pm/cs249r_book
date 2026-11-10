---
title: Robotics Middleware and Dataflow
type: concept
tags:
- Type/Concept
- Group/System_Types
- Topic/Real_Time_Mixed_Criticality_Computing
source_repository: https://github.com/klappe-pm/cs249r_book
source_commit: de87c0103806d7bfb1c677dbb77a2b92fa00c298
source_path: taxonomy/taxonomy.yml
source_label: Robotics middleware and dataflow
taxonomy_id: mlsys.robotics-middleware
taxonomy_status: draft
taxonomy_version: 0.4-draft
---

# Robotics Middleware and Dataflow

Software connecting sensing, perception, planning, and control processes as nodes that exchange typed messages over publish-subscribe topics with configurable delivery and timing policies.

## Browsing Home

[[02 Concepts/System Types/Embodied & Physical Systems/Real Time & Mixed Criticality Computing Subject|Real Time & Mixed Criticality Computing]] → [[02 Concepts/System Types/Embodied & Physical Systems/Embodied & Physical Systems Index|Embodied & Physical Systems]]

## Book Passages

These are explicitly recorded related passages from the upstream draft alignment; they do not certify complete coverage.

No explicit passage alignment is recorded for this concept. Subject reading pointers are available in its browsing home.

## Conditional Relationships

These are the taxonomy's draft editorial relationships. Read each relationship with its condition; an outgoing link is not a prerequisite claim.

- Adds transport, serialization, and executor queuing delay to [[02 Concepts/System Types/Embodied & Physical Systems/Feedback Delay|Feedback Delay]]. **Condition:** When sensing, inference, and control run as separate communicating nodes rather than in one process.

- Reaches drives and encoders through [[02 Concepts/System Types/Embodied & Physical Systems/Real Time Fieldbus|Real Time Fieldbus]]. **Condition:** When middleware nodes talk to actuators and sensors over a fieldbus rather than directly.

## Search Terms

Upstream search terms may be related terms rather than exact synonyms: ROS 2; publish-subscribe middleware; DDS.

## Source

[Canonical Taxonomy](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/taxonomy.yml) · [Passage Alignment](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/mlsysbook-alignment.yml)

Taxonomy definitions and relationship wording: CC BY 4.0, with attribution to the Machine Learning Systems curriculum by Vijay Janapa Reddi and contributors. The textbook retains its separate license.
