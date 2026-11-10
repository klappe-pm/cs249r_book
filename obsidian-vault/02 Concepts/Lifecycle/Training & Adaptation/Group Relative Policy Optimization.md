---
title: Group Relative Policy Optimization
type: concept
tags:
- Type/Concept
- Group/Lifecycle
- Topic/Preference_RL_Post_Training
source_repository: https://github.com/klappe-pm/cs249r_book
source_commit: de87c0103806d7bfb1c677dbb77a2b92fa00c298
source_path: taxonomy/taxonomy.yml
source_label: Group relative policy optimization
taxonomy_id: mlsys.group-relative-policy-optimization
taxonomy_status: draft
taxonomy_version: 0.4-draft
---

# Group Relative Policy Optimization

A policy-gradient method that scores each sampled response against the mean reward of a group of responses to the same prompt, removing the learned critic at the cost of generating several rollouts per prompt.

## Browsing Home

[[02 Concepts/Lifecycle/Training & Adaptation/Preference & RL Post Training Subject|Preference & RL Post Training]] → [[02 Concepts/Lifecycle/Training & Adaptation/Training & Adaptation Index|Training & Adaptation]]

## Book Passages

These are explicitly recorded related passages from the upstream draft alignment; they do not certify complete coverage.

No explicit passage alignment is recorded for this concept. Subject reading pointers are available in its browsing home.

## Conditional Relationships

These are the taxonomy's draft editorial relationships. Read each relationship with its condition; an outgoing link is not a prerequisite claim.

- Specializes policy optimization within [[02 Concepts/Lifecycle/Training & Adaptation/Reinforcement Learning|Reinforcement Learning]]. **Condition:** When group-relative advantages drive policy updates.

- Uses grouped sampled responses from [[02 Concepts/Lifecycle/Training & Adaptation/RL Rollout Generation|RL Rollout Generation]]. **Condition:** When several responses or trajectories are sampled for each prompt.

- Removes the critic model's parameters and optimizer state from [[02 Concepts/Lifecycle/Training & Adaptation/Training State|Training State]]. **Condition:** Compared with PPO-style actor-critic training that keeps a separate value model.

## Search Terms

Upstream search terms may be related terms rather than exact synonyms: GRPO.

## Source

[Canonical Taxonomy](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/taxonomy.yml) · [Passage Alignment](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/mlsysbook-alignment.yml)

Taxonomy definitions and relationship wording: CC BY 4.0, with attribution to the Machine Learning Systems curriculum by Vijay Janapa Reddi and contributors. The textbook retains its separate license.
