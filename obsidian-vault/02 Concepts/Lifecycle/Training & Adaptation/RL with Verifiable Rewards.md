---
title: RL with Verifiable Rewards
type: concept
tags:
- Type/Concept
- Group/Lifecycle
- Topic/Preference_RL_Post_Training
source_repository: https://github.com/klappe-pm/cs249r_book
source_commit: de87c0103806d7bfb1c677dbb77a2b92fa00c298
source_path: taxonomy/taxonomy.yml
source_label: RL with verifiable rewards
taxonomy_id: mlsys.rlvr
taxonomy_status: draft
taxonomy_version: 0.4-draft
---

# RL with Verifiable Rewards

Reinforcement learning whose rewards come from programmatic outcome checks, making verifier correctness and reward computation part of the training system.

## Browsing Home

[[02 Concepts/Lifecycle/Training & Adaptation/Preference & RL Post Training Subject|Preference & RL Post Training]] → [[02 Concepts/Lifecycle/Training & Adaptation/Training & Adaptation Index|Training & Adaptation]]

## Book Passages

These are explicitly recorded related passages from the upstream draft alignment; they do not certify complete coverage.

- [[01 Books/Volume III - Agentic Systems/05 Learning from Trajectories/17 Reinforcement Learning from Verifiable Rewards/V3-17.04 Verifiable Rewards#^sec-vol3-rlvr-score-intended-outcome|V3-17.04 Verifiable Rewards]] — Verifiable reward. [Exact Source Passage](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/books/vol3/17_rlvr/17_rlvr.qmd#L157).

## Conditional Relationships

These are the taxonomy's draft editorial relationships. Read each relationship with its condition; an outgoing link is not a prerequisite claim.

- Requires [[02 Concepts/Lifecycle/Deployment & Serving/Verifier|Verifier]]. **Condition:** Rewards are only as reliable as the programmatic checker; exploitable checkers produce reward hacking.

- Is a kind of [[02 Concepts/Lifecycle/Training & Adaptation/Reinforcement Learning|Reinforcement Learning]]. **Condition:** Holds when rewards come from programmatic outcome checks.

- Requires many sampled responses from [[02 Concepts/Lifecycle/Training & Adaptation/RL Rollout Generation|RL Rollout Generation]]. **Condition:** Holds for policy-gradient training where rewards are computed on generated outputs.

## Search Terms

Upstream search terms may be related terms rather than exact synonyms: RLVR.

## Source

[Canonical Taxonomy](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/taxonomy.yml) · [Passage Alignment](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/mlsysbook-alignment.yml)

Taxonomy definitions and relationship wording: CC BY 4.0, with attribution to the Machine Learning Systems curriculum by Vijay Janapa Reddi and contributors. The textbook retains its separate license.
