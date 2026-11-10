---
title: System Identification
type: concept
tags:
- Type/Concept
- Group/System_Types
- Topic/Motion_Planning_Control
- Context/Background
source_repository: https://github.com/klappe-pm/cs249r_book
source_commit: de87c0103806d7bfb1c677dbb77a2b92fa00c298
source_path: taxonomy/taxonomy.yml
source_label: System identification
taxonomy_id: mlsys.system-identification
taxonomy_status: draft
taxonomy_version: 0.4-draft
---

# System Identification

Estimating the parameters of a dynamics model, such as masses, friction, delays, and actuator gains, from measured input-output data of the physical system.

## Browsing Home

[[02 Concepts/System Types/Embodied & Physical Systems/Motion Planning & Control Subject|Motion Planning & Control]] → [[02 Concepts/System Types/Embodied & Physical Systems/Embodied & Physical Systems Index|Embodied & Physical Systems]]

This is a background concept on which ML systems reasoning depends; that classification does not make it optional.

## Book Passages

These are explicitly recorded related passages from the upstream draft alignment; they do not certify complete coverage.

No explicit passage alignment is recorded for this concept. Subject reading pointers are available in its browsing home.

## Conditional Relationships

These are the taxonomy's draft editorial relationships. Read each relationship with its condition; an outgoing link is not a prerequisite claim.

- Narrows the reality gap by measurement instead of randomizing over [[02 Concepts/System Types/Embodied & Physical Systems/Domain Randomization|Domain Randomization]]. **Condition:** As a way to close the sim-to-real dynamics gap when parameters are observable in logged data; the two are often combined.

- Supplies the model required by [[02 Concepts/System Types/Embodied & Physical Systems/Model Predictive Control|Model Predictive Control]]. **Condition:** When MPC uses a physics-based rather than learned dynamics model.

- Aligns simulated dynamics with hardware for [[02 Concepts/System Types/Embodied & Physical Systems/Simulation to Real Transfer|Simulation to Real Transfer]]. **Condition:** When identified plant and actuator parameters are imported into the training simulator.

## Source

[Canonical Taxonomy](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/taxonomy.yml) · [Passage Alignment](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/mlsysbook-alignment.yml)

Taxonomy definitions and relationship wording: CC BY 4.0, with attribution to the Machine Learning Systems curriculum by Vijay Janapa Reddi and contributors. The textbook retains its separate license.
