---
title: Perception Latency Budget
type: concept
tags:
- Type/Concept
- Group/System_Types
- Topic/Sensing_Perception_Fusion
source_repository: https://github.com/klappe-pm/cs249r_book
source_commit: de87c0103806d7bfb1c677dbb77a2b92fa00c298
source_path: taxonomy/taxonomy.yml
source_label: Perception latency budget
taxonomy_id: mlsys.perception-latency-budget
taxonomy_status: draft
taxonomy_version: 0.4-draft
---

# Perception Latency Budget

The share of a robot's sense-to-act deadline allotted to sensing and perception, which bounds model size, input resolution, and frame rate on the onboard computer.

## Browsing Home

[[02 Concepts/System Types/Embodied & Physical Systems/Sensing, Perception & Fusion Subject|Sensing, Perception & Fusion]] → [[02 Concepts/System Types/Embodied & Physical Systems/Embodied & Physical Systems Index|Embodied & Physical Systems]]

## Book Passages

These are explicitly recorded related passages from the upstream draft alignment; they do not certify complete coverage.

No explicit passage alignment is recorded for this concept. Subject reading pointers are available in its browsing home.

## Conditional Relationships

These are the taxonomy's draft editorial relationships. Read each relationship with its condition; an outgoing link is not a prerequisite claim.

- Is the sensing share of [[02 Concepts/System Types/Embodied & Physical Systems/Feedback Delay|Feedback Delay]]. **Condition:** Perception runs inside the control loop.

- Bounds model size and resolution for [[02 Concepts/System Types/Embodied & Physical Systems/Robot Perception|Robot Perception]]. **Condition:** Perception runs on fixed onboard hardware.

## Themes

- [[03 Themes/Latency and Throughput|Latency and Throughput]]

## Search Terms

Upstream search terms may be related terms rather than exact synonyms: sense-to-act latency budget.

## Source

[Canonical Taxonomy](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/taxonomy.yml) · [Passage Alignment](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/mlsysbook-alignment.yml)

Taxonomy definitions and relationship wording: CC BY 4.0, with attribution to the Machine Learning Systems curriculum by Vijay Janapa Reddi and contributors. The textbook retains its separate license.
