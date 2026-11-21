---
title: RL Rollout Generation
type: concept
tags:
- Type/Concept
- Group/Lifecycle
- Topic/Preference_RL_Post_Training
source_repository: https://github.com/klappe-pm/cs249r_book
source_commit: de87c0103806d7bfb1c677dbb77a2b92fa00c298
source_path: taxonomy/taxonomy.yml
source_label: RL rollout generation
taxonomy_id: mlsys.rl-rollout
taxonomy_status: draft
taxonomy_version: 0.4-draft
---

# RL Rollout Generation

Sampling responses or trajectories from the current policy, often with an inference engine, to produce experience for policy updates.

## Browsing Home

[[02 Concepts/Lifecycle/Training & Adaptation/Preference & RL Post Training Subject|Preference & RL Post Training]] → [[02 Concepts/Lifecycle/Training & Adaptation/Training & Adaptation Index|Training & Adaptation]]

## Book Passages

These are explicitly recorded related passages from the upstream draft alignment; they do not certify complete coverage.

No explicit passage alignment is recorded for this concept. Subject reading pointers are available in its browsing home.

## Conditional Relationships

These are the taxonomy's draft editorial relationships. Read each relationship with its condition; an outgoing link is not a prerequisite claim.

- Asynchronous generation increases [[02 Concepts/Lifecycle/Training & Adaptation/Policy Staleness|Policy Staleness]]. **Condition:** Holds when rollouts overlap with policy updates.

- Generates many sampled responses per prompt through [[02 Concepts/Lifecycle/Deployment & Serving/Continuous Batching|Continuous Batching]]. **Condition:** When rollouts are produced by a serving engine rather than the training framework, so engine throughput bounds samples per step.

## Source

[Canonical Taxonomy](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/taxonomy.yml) · [Passage Alignment](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/mlsysbook-alignment.yml)

Taxonomy definitions and relationship wording: CC BY 4.0, with attribution to the Machine Learning Systems curriculum by Vijay Janapa Reddi and contributors. The textbook retains its separate license.
