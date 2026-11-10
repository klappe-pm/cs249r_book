---
title: Colocated Versus Disaggregated RL Post Training
type: concept
tags:
- Type/Concept
- Group/Lifecycle
- Topic/Preference_RL_Post_Training
source_repository: https://github.com/klappe-pm/cs249r_book
source_commit: de87c0103806d7bfb1c677dbb77a2b92fa00c298
source_path: taxonomy/taxonomy.yml
source_label: Colocated versus disaggregated RL post-training
taxonomy_id: mlsys.rl-training-colocation
taxonomy_status: draft
taxonomy_version: 0.4-draft
---

# Colocated Versus Disaggregated RL Post Training

Whether rollout generation and policy updates share the same accelerators, alternating phases and re-sharding weights in place, or run on separate pools that exchange weights and samples, trading idle time within each phase against transfer cost and policy staleness.

## Browsing Home

[[02 Concepts/Lifecycle/Training & Adaptation/Preference & RL Post Training Subject|Preference & RL Post Training]] → [[02 Concepts/Lifecycle/Training & Adaptation/Training & Adaptation Index|Training & Adaptation]]

## Book Passages

These are explicitly recorded related passages from the upstream draft alignment; they do not certify complete coverage.

No explicit passage alignment is recorded for this concept. Subject reading pointers are available in its browsing home.

## Conditional Relationships

These are the taxonomy's draft editorial relationships. Read each relationship with its condition; an outgoing link is not a prerequisite claim.

- Sets the transfer path and cost of [[02 Concepts/Lifecycle/Training & Adaptation/Policy Weight Synchronization|Policy Weight Synchronization]]. **Condition:** Colocated designs reshard in device memory; disaggregated ones send weights across the network.

- Switches between training and generation layouts with [[02 Concepts/Stack/Parallelism & Distributed Execution/Dynamic Re Parallelization|Dynamic Re Parallelization]]. **Condition:** When the colocated design runs both phases on one device set.

- Raises, in its disaggregated asynchronous form, [[02 Concepts/Lifecycle/Training & Adaptation/Policy Staleness|Policy Staleness]]. **Condition:** When rollout workers keep generating while trainers update.

## Search Terms

Upstream search terms may be related terms rather than exact synonyms: actor-learner colocation; hybrid RL engine; disaggregated rollout and training.

## Source

[Canonical Taxonomy](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/taxonomy.yml) · [Passage Alignment](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/mlsysbook-alignment.yml)

Taxonomy definitions and relationship wording: CC BY 4.0, with attribution to the Machine Learning Systems curriculum by Vijay Janapa Reddi and contributors. The textbook retains its separate license.
