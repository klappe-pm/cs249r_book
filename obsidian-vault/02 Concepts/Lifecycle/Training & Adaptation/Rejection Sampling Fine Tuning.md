---
title: Rejection Sampling Fine Tuning
type: concept
tags:
- Type/Concept
- Group/Lifecycle
- Topic/Preference_RL_Post_Training
source_repository: https://github.com/klappe-pm/cs249r_book
source_commit: de87c0103806d7bfb1c677dbb77a2b92fa00c298
source_path: taxonomy/taxonomy.yml
source_label: Rejection-sampling fine-tuning
taxonomy_id: mlsys.rejection-sampling-fine-tuning
taxonomy_status: draft
taxonomy_version: 0.4-draft
---

# Rejection Sampling Fine Tuning

Generating candidate responses, filtering them with an acceptance criterion, and fine-tuning on accepted responses to turn a selection signal into supervised training data, with repeated filtering potentially reducing diversity.

## Browsing Home

[[02 Concepts/Lifecycle/Training & Adaptation/Preference & RL Post Training Subject|Preference & RL Post Training]] → [[02 Concepts/Lifecycle/Training & Adaptation/Training & Adaptation Index|Training & Adaptation]]

## Book Passages

These are explicitly recorded related passages from the upstream draft alignment; they do not certify complete coverage.

No explicit passage alignment is recorded for this concept. Subject reading pointers are available in its browsing home.

## Conditional Relationships

These are the taxonomy's draft editorial relationships. Read each relationship with its condition; an outgoing link is not a prerequisite claim.

- Is the self-generated-data form of [[02 Concepts/Lifecycle/Training & Adaptation/Supervised Fine Tuning|Supervised Fine Tuning]]. **Condition:** When the training targets are the model's own accepted samples rather than human demonstrations.

- Filters candidates with [[02 Concepts/Lifecycle/Deployment & Serving/Verifier|Verifier]]. **Condition:** When acceptance is decided by a programmatic check, a reward model, or a grader; filter errors become training labels.

- Is an offline, SFT-based alternative to [[02 Concepts/Lifecycle/Training & Adaptation/RL with Verifiable Rewards|RL with Verifiable Rewards]]. **Condition:** Both learn from verifiable outcomes; rejection sampling updates only on accepted samples while RLVR takes policy gradients over all sampled outcomes.

- Narrows sampled diversity across rounds toward [[02 Concepts/Lifecycle/Training & Adaptation/Mode Collapse|Mode Collapse]]. **Condition:** When successive rounds train only on the model's own high-scoring samples, concentrating training mass on a narrowing response family without fresh human or real data.

## Search Terms

Upstream search terms may be related terms rather than exact synonyms: STaR; ReST; filtered self-training.

## Source

[Canonical Taxonomy](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/taxonomy.yml) · [Passage Alignment](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/mlsysbook-alignment.yml)

Taxonomy definitions and relationship wording: CC BY 4.0, with attribution to the Machine Learning Systems curriculum by Vijay Janapa Reddi and contributors. The textbook retains its separate license.
