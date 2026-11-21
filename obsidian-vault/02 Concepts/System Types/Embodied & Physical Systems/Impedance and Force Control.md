---
title: Impedance and Force Control
type: concept
tags:
- Type/Concept
- Group/System_Types
- Topic/Motion_Planning_Control
- Context/Background
source_repository: https://github.com/klappe-pm/cs249r_book
source_commit: de87c0103806d7bfb1c677dbb77a2b92fa00c298
source_path: taxonomy/taxonomy.yml
source_label: Impedance and force control
taxonomy_id: mlsys.impedance-force-control
taxonomy_status: draft
taxonomy_version: 0.4-draft
---

# Impedance and Force Control

Feedback control that regulates the relationship between motion and contact force, by commanding a virtual stiffness and damping or by tracking a force setpoint, so a robot can touch, push, and insert without the force spikes that pure position control produces at contact.

## Browsing Home

[[02 Concepts/System Types/Embodied & Physical Systems/Motion Planning & Control Subject|Motion Planning & Control]] → [[02 Concepts/System Types/Embodied & Physical Systems/Embodied & Physical Systems Index|Embodied & Physical Systems]]

This is a background concept on which ML systems reasoning depends; that classification does not make it optional.

## Book Passages

These are explicitly recorded related passages from the upstream draft alignment; they do not certify complete coverage.

No explicit passage alignment is recorded for this concept. Subject reading pointers are available in its browsing home.

## Conditional Relationships

These are the taxonomy's draft editorial relationships. Read each relationship with its condition; an outgoing link is not a prerequisite claim.

- Is the contact-regulating form of [[02 Concepts/System Types/Embodied & Physical Systems/Feedback Control|Feedback Control]]. **Condition:** The regulated variable is the force-motion relationship rather than position alone.

- Models the environment's stiffness and damping through [[02 Concepts/System Types/Embodied & Physical Systems/Contact and Compliance|Contact and Compliance]]. **Condition:** Stable contact depends on the combined compliance of robot, controller, and environment.

## Search Terms

Upstream search terms may be related terms rather than exact synonyms: impedance control; admittance control; force control; compliant control; hybrid position-force control.

## Source

[Canonical Taxonomy](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/taxonomy.yml) · [Passage Alignment](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/mlsysbook-alignment.yml)

Taxonomy definitions and relationship wording: CC BY 4.0, with attribution to the Machine Learning Systems curriculum by Vijay Janapa Reddi and contributors. The textbook retains its separate license.
