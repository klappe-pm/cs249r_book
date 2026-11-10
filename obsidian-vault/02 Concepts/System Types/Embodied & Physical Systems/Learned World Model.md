---
title: Learned World Model
type: concept
tags:
- Type/Concept
- Group/System_Types
- Topic/State_Estimation_Localization_Mapping
source_repository: https://github.com/klappe-pm/cs249r_book
source_commit: de87c0103806d7bfb1c677dbb77a2b92fa00c298
source_path: taxonomy/taxonomy.yml
source_label: Learned world model
taxonomy_id: mlsys.world-model
taxonomy_status: draft
taxonomy_version: 0.4-draft
---

# Learned World Model

A learned model that predicts future observations or latent states conditioned on actions, used for planning, policy training, or simulation.

## Browsing Home

[[02 Concepts/System Types/Embodied & Physical Systems/State Estimation, Localization & Mapping Subject|State Estimation, Localization & Mapping]] → [[02 Concepts/System Types/Embodied & Physical Systems/Embodied & Physical Systems Index|Embodied & Physical Systems]]

## Book Passages

These are explicitly recorded related passages from the upstream draft alignment; they do not certify complete coverage.

No explicit passage alignment is recorded for this concept. Subject reading pointers are available in its browsing home.

## Conditional Relationships

These are the taxonomy's draft editorial relationships. Read each relationship with its condition; an outgoing link is not a prerequisite claim.

- Enables sample-efficient [[02 Concepts/Lifecycle/Training & Adaptation/Reinforcement Learning|Reinforcement Learning]]. **Condition:** When policies are trained on imagined rollouts from the learned model rather than only on environment interaction.

- Is trained to predict future observations by [[02 Concepts/Lifecycle/Training & Adaptation/Self Supervised Learning|Self Supervised Learning]]. **Condition:** When the model learns from action-conditioned sequences without task labels.

## Source

[Canonical Taxonomy](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/taxonomy.yml) · [Passage Alignment](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/mlsysbook-alignment.yml)

Taxonomy definitions and relationship wording: CC BY 4.0, with attribution to the Machine Learning Systems curriculum by Vijay Janapa Reddi and contributors. The textbook retains its separate license.
