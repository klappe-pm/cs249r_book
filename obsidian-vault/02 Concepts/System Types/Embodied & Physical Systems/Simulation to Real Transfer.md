---
title: Simulation to Real Transfer
type: concept
tags:
- Type/Concept
- Group/System_Types
- Topic/Robot_Learning_Sim_to_Real
source_repository: https://github.com/klappe-pm/cs249r_book
source_commit: de87c0103806d7bfb1c677dbb77a2b92fa00c298
source_path: taxonomy/taxonomy.yml
source_label: Simulation-to-real transfer
taxonomy_id: mlsys.sim-to-real
taxonomy_status: draft
taxonomy_version: 0.4-draft
---

# Simulation to Real Transfer

Transferring a policy trained in simulation to physical hardware, where differences in dynamics, sensing, contact, and timing can degrade behavior and motivate randomization, system identification, or adaptation on real experience.

## Browsing Home

[[02 Concepts/System Types/Embodied & Physical Systems/Robot Learning & Sim to Real Subject|Robot Learning & Sim to Real]] → [[02 Concepts/System Types/Embodied & Physical Systems/Embodied & Physical Systems Index|Embodied & Physical Systems]]

## Book Passages

These are explicitly recorded related passages from the upstream draft alignment; they do not certify complete coverage.

- [[01 Books/Volume IV - Physical AI/02 Teaching the Machine/06 Policy Training/V4-06.05 The Simulator as a System Component#^sec-training-simulator-component|V4-06.05 The Simulator as a System Component]] — Reality gap. [Exact Source Passage](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/books/vol4/06_training/06_training.qmd#L968).

## Conditional Relationships

These are the taxonomy's draft editorial relationships. Read each relationship with its condition; an outgoing link is not a prerequisite claim.

- Requires assessing simulator mismatch in [[02 Concepts/System Types/Embodied & Physical Systems/Physical Dynamics|Physical Dynamics]]. **Condition:** Simulation evidence must be evaluated against the actual deployment conditions.

- Starts from policies trained in [[02 Concepts/System Types/Embodied & Physical Systems/Parallel Physics Simulation|Parallel Physics Simulation]]. **Condition:** When the policy's experience came from batched simulated environments rather than physical collection.

## Search Terms

Upstream search terms may be related terms rather than exact synonyms: sim-to-real; sim2real.

## Source

[Canonical Taxonomy](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/taxonomy.yml) · [Passage Alignment](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/mlsysbook-alignment.yml)

Taxonomy definitions and relationship wording: CC BY 4.0, with attribution to the Machine Learning Systems curriculum by Vijay Janapa Reddi and contributors. The textbook retains its separate license.
