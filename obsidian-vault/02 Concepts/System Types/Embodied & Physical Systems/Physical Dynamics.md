---
title: Physical Dynamics
type: concept
tags:
- Type/Concept
- Group/System_Types
- Topic/Motion_Planning_Control
- Context/Background
source_repository: https://github.com/klappe-pm/cs249r_book
source_commit: de87c0103806d7bfb1c677dbb77a2b92fa00c298
source_path: taxonomy/taxonomy.yml
source_label: Physical dynamics
taxonomy_id: mlsys.dynamics
taxonomy_status: draft
taxonomy_version: 0.4-draft
---

# Physical Dynamics

The evolution of a physical system under inputs, disturbances, and constraints.

## Browsing Home

[[02 Concepts/System Types/Embodied & Physical Systems/Motion Planning & Control Subject|Motion Planning & Control]] → [[02 Concepts/System Types/Embodied & Physical Systems/Embodied & Physical Systems Index|Embodied & Physical Systems]]

This is a background concept on which ML systems reasoning depends; that classification does not make it optional.

## Book Passages

These are explicitly recorded related passages from the upstream draft alignment; they do not certify complete coverage.

- [[01 Books/Volume IV - Physical AI/01 Machine Anatomy/02 The Physical Body/V4-02.04 Kinetic Momentum#^sec-body-kinetic-momentum|V4-02.04 Kinetic Momentum]] — Braking authority. [Exact Source Passage](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/books/vol4/02_body/02_body.qmd#L362).

## Conditional Relationships

These are the taxonomy's draft editorial relationships. Read each relationship with its condition; an outgoing link is not a prerequisite claim.

- Constrains [[02 Concepts/System Types/Embodied & Physical Systems/Trajectory Feasibility|Trajectory Feasibility]]. **Condition:** Physical states, inputs, disturbances, and constraints determine admissible motion.

- Governs the plant response to [[02 Concepts/System Types/Embodied & Physical Systems/Feedback Control|Feedback Control]]. **Condition:** The closed-loop response depends on the plant, disturbances, constraints, sensing, and controller implementation.

- Sets, together with the controller, the [[02 Concepts/System Types/Embodied & Physical Systems/Loop Stability Margin|Loop Stability Margin]]. **Condition:** The margin is a property of the plant-controller pair, not of the controller alone.

## Source

[Canonical Taxonomy](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/taxonomy.yml) · [Passage Alignment](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/mlsysbook-alignment.yml)

Taxonomy definitions and relationship wording: CC BY 4.0, with attribution to the Machine Learning Systems curriculum by Vijay Janapa Reddi and contributors. The textbook retains its separate license.
