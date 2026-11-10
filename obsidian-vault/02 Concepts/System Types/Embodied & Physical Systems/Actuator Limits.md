---
title: Actuator Limits
type: concept
tags:
- Type/Concept
- Group/System_Types
- Topic/Motion_Planning_Control
source_repository: https://github.com/klappe-pm/cs249r_book
source_commit: de87c0103806d7bfb1c677dbb77a2b92fa00c298
source_path: taxonomy/taxonomy.yml
source_label: Actuator limits
taxonomy_id: mlsys.actuator-limits
taxonomy_status: draft
taxonomy_version: 0.4-draft
---

# Actuator Limits

Bounds on the force, torque, speed, and sustained duty an actuator can deliver, set by drive current limits, gearing, and motor heating.

## Browsing Home

[[02 Concepts/System Types/Embodied & Physical Systems/Motion Planning & Control Subject|Motion Planning & Control]] → [[02 Concepts/System Types/Embodied & Physical Systems/Embodied & Physical Systems Index|Embodied & Physical Systems]]

## Book Passages

These are explicitly recorded related passages from the upstream draft alignment; they do not certify complete coverage.

- [[01 Books/Volume IV - Physical AI/01 Machine Anatomy/02 The Physical Body/V4-02.04 Kinetic Momentum#^sec-body-kinetic-momentum|V4-02.04 Kinetic Momentum]] — Braking authority. [Exact Source Passage](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/books/vol4/02_body/02_body.qmd#L362).

- [[01 Books/Volume IV - Physical AI/01 Machine Anatomy/02 The Physical Body/V4-02.06 Thermal Duty Cycles#^sec-body-thermal-capacity|V4-02.06 Thermal Duty Cycles]] — Thermal headroom. [Exact Source Passage](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/books/vol4/02_body/02_body.qmd#L1407).

## Conditional Relationships

These are the taxonomy's draft editorial relationships. Read each relationship with its condition; an outgoing link is not a prerequisite claim.

- Sets which motions satisfy [[02 Concepts/System Types/Embodied & Physical Systems/Trajectory Feasibility|Trajectory Feasibility]]. **Condition:** Planned motions demand force or speed near the actuator's capability.

## Search Terms

Upstream search terms may be related terms rather than exact synonyms: torque saturation; thermal duty limits.

## Source

[Canonical Taxonomy](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/taxonomy.yml) · [Passage Alignment](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/mlsysbook-alignment.yml)

Taxonomy definitions and relationship wording: CC BY 4.0, with attribution to the Machine Learning Systems curriculum by Vijay Janapa Reddi and contributors. The textbook retains its separate license.
