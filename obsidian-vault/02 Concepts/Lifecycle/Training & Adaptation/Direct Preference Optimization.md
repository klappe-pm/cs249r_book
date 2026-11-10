---
title: Direct Preference Optimization
type: concept
tags:
- Type/Concept
- Group/Lifecycle
- Topic/Preference_RL_Post_Training
source_repository: https://github.com/klappe-pm/cs249r_book
source_commit: de87c0103806d7bfb1c677dbb77a2b92fa00c298
source_path: taxonomy/taxonomy.yml
source_label: Direct preference optimization
taxonomy_id: mlsys.preference-optimization
taxonomy_status: draft
taxonomy_version: 0.4-draft
---

# Direct Preference Optimization

Training a policy directly on preferred-versus-rejected output pairs with a classification-style loss, without a separate reward model or RL loop.

## Browsing Home

[[02 Concepts/Lifecycle/Training & Adaptation/Preference & RL Post Training Subject|Preference & RL Post Training]] → [[02 Concepts/Lifecycle/Training & Adaptation/Training & Adaptation Index|Training & Adaptation]]

## Book Passages

These are explicitly recorded related passages from the upstream draft alignment; they do not certify complete coverage.

No explicit passage alignment is recorded for this concept. Subject reading pointers are available in its browsing home.

## Conditional Relationships

These are the taxonomy's draft editorial relationships. Read each relationship with its condition; an outgoing link is not a prerequisite claim.

- Is an alternative to [[02 Concepts/Lifecycle/Training & Adaptation/RL from Human Feedback|RL from Human Feedback]]. **Condition:** Both align to preference data; DPO skips the separate reward model and RL loop.

- Avoids reward and value models in [[02 Concepts/Lifecycle/Training & Adaptation/Training State|Training State]]. **Condition:** Holds relative to PPO-based RLHF; a frozen reference model is still needed.

- Teaches helpful answers to borderline benign requests, limiting [[02 Concepts/Qualities/Safety & Assurance/Over Refusal|Over Refusal]]. **Condition:** When the preference data includes benign requests that resemble harmful ones, paired with helpful responses.

## Search Terms

Upstream search terms may be related terms rather than exact synonyms: DPO.

## Source

[Canonical Taxonomy](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/taxonomy.yml) · [Passage Alignment](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/mlsysbook-alignment.yml)

Taxonomy definitions and relationship wording: CC BY 4.0, with attribution to the Machine Learning Systems curriculum by Vijay Janapa Reddi and contributors. The textbook retains its separate license.
