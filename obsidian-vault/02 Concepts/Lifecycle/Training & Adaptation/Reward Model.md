---
title: Reward Model
type: concept
tags:
- Type/Concept
- Group/Lifecycle
- Topic/Preference_RL_Post_Training
source_repository: https://github.com/klappe-pm/cs249r_book
source_commit: de87c0103806d7bfb1c677dbb77a2b92fa00c298
source_path: taxonomy/taxonomy.yml
source_label: Reward model
taxonomy_id: mlsys.reward-model
taxonomy_status: draft
taxonomy_version: 0.4-draft
---

# Reward Model

A learned model that scores outputs or trajectories to supply the training signal for policy optimization.

## Browsing Home

[[02 Concepts/Lifecycle/Training & Adaptation/Preference & RL Post Training Subject|Preference & RL Post Training]] → [[02 Concepts/Lifecycle/Training & Adaptation/Training & Adaptation Index|Training & Adaptation]]

## Book Passages

These are explicitly recorded related passages from the upstream draft alignment; they do not certify complete coverage.

No explicit passage alignment is recorded for this concept. Subject reading pointers are available in its browsing home.

## Conditional Relationships

These are the taxonomy's draft editorial relationships. Read each relationship with its condition; an outgoing link is not a prerequisite claim.

- Supplies the training signal in [[02 Concepts/Lifecycle/Training & Adaptation/RL from Human Feedback|RL from Human Feedback]]. **Condition:** Holds for RLHF pipelines that learn a reward model from human comparisons.

- Can invite [[02 Concepts/Lifecycle/Training & Adaptation/Reward Hacking|Reward Hacking]]. **Condition:** Policies optimized hard against a learned reward model can exploit its errors, scoring higher while true quality falls.

- Requires reliable preference [[02 Concepts/Lifecycle/Data Engineering/Label Quality|Label Quality]]. **Condition:** Holds because reward accuracy is bounded by comparison label agreement.

## Source

[Canonical Taxonomy](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/taxonomy.yml) · [Passage Alignment](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/mlsysbook-alignment.yml)

Taxonomy definitions and relationship wording: CC BY 4.0, with attribution to the Machine Learning Systems curriculum by Vijay Janapa Reddi and contributors. The textbook retains its separate license.
