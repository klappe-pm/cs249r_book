---
title: Domain Randomization
type: concept
tags:
- Type/Concept
- Group/System_Types
- Topic/Robot_Learning_Sim_to_Real
source_repository: https://github.com/klappe-pm/cs249r_book
source_commit: de87c0103806d7bfb1c677dbb77a2b92fa00c298
source_path: taxonomy/taxonomy.yml
source_label: Domain randomization
taxonomy_id: mlsys.domain-randomization
taxonomy_status: draft
taxonomy_version: 0.4-draft
---

# Domain Randomization

Training in simulation over randomized visual and physical parameters so the policy treats the real world as one more variation.

## Browsing Home

[[02 Concepts/System Types/Embodied & Physical Systems/Robot Learning & Sim to Real Subject|Robot Learning & Sim to Real]] → [[02 Concepts/System Types/Embodied & Physical Systems/Embodied & Physical Systems Index|Embodied & Physical Systems]]

## Book Passages

These are explicitly recorded related passages from the upstream draft alignment; they do not certify complete coverage.

- [[01 Books/Volume IV - Physical AI/02 Teaching the Machine/06 Policy Training/V4-06.05 The Simulator as a System Component#^sec-training-simulator-component|V4-06.05 The Simulator as a System Component]] — Reality gap. [Exact Source Passage](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/books/vol4/06_training/06_training.qmd#L968).

## Conditional Relationships

These are the taxonomy's draft editorial relationships. Read each relationship with its condition; an outgoing link is not a prerequisite claim.

- Improves [[02 Concepts/System Types/Embodied & Physical Systems/Simulation to Real Transfer|Simulation to Real Transfer]]. **Condition:** Holds when the randomized ranges cover the real parameters without making the task unlearnable.

- Generates varied [[02 Concepts/Lifecycle/Data Engineering/Synthetic Data|Synthetic Data]]. **Condition:** Applies to simulator-generated training data for transfer to the real world.

- Generates varied simulated examples instead of transforming recorded ones as in [[02 Concepts/Lifecycle/Data Engineering/Data Augmentation|Data Augmentation]]. **Condition:** When training data for a policy or perception model can be simulated rather than only recorded.

- Mitigates [[02 Concepts/Lifecycle/MLOps & Operations/Distribution Shift|Distribution Shift]]. **Condition:** When the randomized ranges cover the real-world parameters without making the task unlearnable.

- Samples randomized environments from [[02 Concepts/System Types/Embodied & Physical Systems/Parallel Physics Simulation|Parallel Physics Simulation]]. **Condition:** Simulator parameters can be varied per environment instance.

## Source

[Canonical Taxonomy](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/taxonomy.yml) · [Passage Alignment](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/mlsysbook-alignment.yml)

Taxonomy definitions and relationship wording: CC BY 4.0, with attribution to the Machine Learning Systems curriculum by Vijay Janapa Reddi and contributors. The textbook retains its separate license.
