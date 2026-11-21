---
title: Agent Training Environment
type: concept
tags:
- Type/Concept
- Group/Lifecycle
- Topic/Preference_RL_Post_Training
source_repository: https://github.com/klappe-pm/cs249r_book
source_commit: de87c0103806d7bfb1c677dbb77a2b92fa00c298
source_path: taxonomy/taxonomy.yml
source_label: Agent training environment
taxonomy_id: mlsys.agent-training-environment
taxonomy_status: draft
taxonomy_version: 0.4-draft
---

# Agent Training Environment

A task system that supplies observations, accepts actions, and manages episode state for training tool-using policies, whose throughput and reset fidelity limit rollout collection.

## Browsing Home

[[02 Concepts/Lifecycle/Training & Adaptation/Preference & RL Post Training Subject|Preference & RL Post Training]] → [[02 Concepts/Lifecycle/Training & Adaptation/Training & Adaptation Index|Training & Adaptation]]

## Book Passages

These are explicitly recorded related passages from the upstream draft alignment; they do not certify complete coverage.

No explicit passage alignment is recorded for this concept. Subject reading pointers are available in its browsing home.

## Conditional Relationships

These are the taxonomy's draft editorial relationships. Read each relationship with its condition; an outgoing link is not a prerequisite claim.

- Provides the world acted in during [[02 Concepts/Lifecycle/Training & Adaptation/RL Rollout Generation|RL Rollout Generation]]. **Condition:** When rollouts are multi-turn and call tools.

- Isolates each episode with [[02 Concepts/Qualities/Security & Privacy/Ephemeral Sandbox|Ephemeral Sandbox]]. **Condition:** When episodes execute code or mutate files.

## Search Terms

Upstream search terms may be related terms rather than exact synonyms: agent rollout environment; agentic RL environment.

## Source

[Canonical Taxonomy](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/taxonomy.yml) · [Passage Alignment](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/mlsysbook-alignment.yml)

Taxonomy definitions and relationship wording: CC BY 4.0, with attribution to the Machine Learning Systems curriculum by Vijay Janapa Reddi and contributors. The textbook retains its separate license.
