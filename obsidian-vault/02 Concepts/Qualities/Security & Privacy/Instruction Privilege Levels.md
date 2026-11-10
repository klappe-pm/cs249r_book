---
title: Instruction Privilege Levels
type: concept
tags:
- Type/Concept
- Group/Qualities
- Topic/Threat_Models_Adversarial_Attacks
source_repository: https://github.com/klappe-pm/cs249r_book
source_commit: de87c0103806d7bfb1c677dbb77a2b92fa00c298
source_path: taxonomy/taxonomy.yml
source_label: Instruction privilege levels
taxonomy_id: mlsys.instruction-hierarchy
taxonomy_status: draft
taxonomy_version: 0.4-draft
---

# Instruction Privilege Levels

Giving instructions from the system, the user, and retrieved or tool-returned content distinct privilege levels, through prompt formatting, delimiting, or training, so that lower-privilege content is less able to override higher-privilege instructions.

## Browsing Home

[[02 Concepts/Qualities/Security & Privacy/Threat Models & Adversarial Attacks Subject|Threat Models & Adversarial Attacks]] → [[02 Concepts/Qualities/Security & Privacy/Security & Privacy Index|Security & Privacy]]

## Book Passages

These are explicitly recorded related passages from the upstream draft alignment; they do not certify complete coverage.

No explicit passage alignment is recorded for this concept. Subject reading pointers are available in its browsing home.

## Conditional Relationships

These are the taxonomy's draft editorial relationships. Read each relationship with its condition; an outgoing link is not a prerequisite claim.

- Lowers the success rate of [[02 Concepts/Qualities/Security & Privacy/Prompt Injection|Prompt Injection]]. **Condition:** When the model has been trained to respect source precedence or uses a provenance-marking prompt scheme validated against the applicable injection attacks, with trusted role assignments controlled outside attacker-supplied content.

- Learns instruction precedence using [[02 Concepts/Lifecycle/Training & Adaptation/RL from Human Feedback|RL from Human Feedback]]. **Condition:** When human preference comparisons over instruction-following behavior train a reward model and reinforcement learning optimizes the policy against that reward.

## Search Terms

Upstream search terms may be related terms rather than exact synonyms: instruction hierarchy; system-prompt precedence.

## Source

[Canonical Taxonomy](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/taxonomy.yml) · [Passage Alignment](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/mlsysbook-alignment.yml)

Taxonomy definitions and relationship wording: CC BY 4.0, with attribution to the Machine Learning Systems curriculum by Vijay Janapa Reddi and contributors. The textbook retains its separate license.
