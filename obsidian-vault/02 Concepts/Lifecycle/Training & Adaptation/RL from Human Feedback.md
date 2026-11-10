---
title: RL from Human Feedback
type: concept
tags:
- Type/Concept
- Group/Lifecycle
- Topic/Preference_RL_Post_Training
source_repository: https://github.com/klappe-pm/cs249r_book
source_commit: de87c0103806d7bfb1c677dbb77a2b92fa00c298
source_path: taxonomy/taxonomy.yml
source_label: RL from human feedback
taxonomy_id: mlsys.rlhf
taxonomy_status: draft
taxonomy_version: 0.4-draft
---

# RL from Human Feedback

Optimizing a model's policy against a reward model trained on human preference comparisons, usually with a penalty for drifting from a reference model.

## Browsing Home

[[02 Concepts/Lifecycle/Training & Adaptation/Preference & RL Post Training Subject|Preference & RL Post Training]] → [[02 Concepts/Lifecycle/Training & Adaptation/Training & Adaptation Index|Training & Adaptation]]

## Book Passages

These are explicitly recorded related passages from the upstream draft alignment; they do not certify complete coverage.

No explicit passage alignment is recorded for this concept. Subject reading pointers are available in its browsing home.

## Conditional Relationships

These are the taxonomy's draft editorial relationships. Read each relationship with its condition; an outgoing link is not a prerequisite claim.

- Is exposed to [[02 Concepts/Lifecycle/Training & Adaptation/Reward Hacking|Reward Hacking]]. **Condition:** Holds when the policy optimizes a learned reward beyond the region where it tracks human preference; a reference-model penalty reduces but does not remove it.

- Starts from a policy produced by [[02 Concepts/Lifecycle/Training & Adaptation/Supervised Fine Tuning|Supervised Fine Tuning]]. **Condition:** Holds for the standard InstructGPT-style pipeline; some recipes skip or shorten the SFT stage.

- Is a kind of [[02 Concepts/Lifecycle/Training & Adaptation/Reinforcement Learning|Reinforcement Learning]]. **Condition:** Holds for PPO-style optimization against a learned reward.

- Partially mitigates [[02 Concepts/Qualities/Security & Privacy/Jailbreak|Jailbreak]]. **Condition:** Safety training reduces disallowed outputs but fails under competing objectives and mismatched generalization.

## Search Terms

Upstream search terms may be related terms rather than exact synonyms: RLHF.

## Source

[Canonical Taxonomy](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/taxonomy.yml) · [Passage Alignment](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/mlsysbook-alignment.yml)

Taxonomy definitions and relationship wording: CC BY 4.0, with attribution to the Machine Learning Systems curriculum by Vijay Janapa Reddi and contributors. The textbook retains its separate license.
