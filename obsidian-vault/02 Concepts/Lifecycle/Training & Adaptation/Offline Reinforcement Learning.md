---
title: Offline Reinforcement Learning
type: concept
tags:
- Type/Concept
- Group/Lifecycle
- Topic/Learning_Paradigms
- Context/Background
source_repository: https://github.com/klappe-pm/cs249r_book
source_commit: de87c0103806d7bfb1c677dbb77a2b92fa00c298
source_path: taxonomy/taxonomy.yml
source_label: Offline reinforcement learning
taxonomy_id: mlsys.offline-rl
taxonomy_status: draft
taxonomy_version: 0.4-draft
---

# Offline Reinforcement Learning

Learning a policy from a fixed dataset of previously logged interactions without further environment access, limited by how well the data covers states the policy would visit.

## Browsing Home

[[02 Concepts/Lifecycle/Training & Adaptation/Learning Paradigms Subject|Learning Paradigms]] → [[02 Concepts/Lifecycle/Training & Adaptation/Training & Adaptation Index|Training & Adaptation]]

This is a background concept on which ML systems reasoning depends; that classification does not make it optional.

## Book Passages

These are explicitly recorded related passages from the upstream draft alignment; they do not certify complete coverage.

No explicit passage alignment is recorded for this concept. Subject reading pointers are available in its browsing home.

## Conditional Relationships

These are the taxonomy's draft editorial relationships. Read each relationship with its condition; an outgoing link is not a prerequisite claim.

- Is a fixed-dataset form of [[02 Concepts/Lifecycle/Training & Adaptation/Reinforcement Learning|Reinforcement Learning]]. **Condition:** No further environment interaction is allowed.

- Can improve on demonstrations unlike [[02 Concepts/Lifecycle/Training & Adaptation/Imitation Learning|Imitation Learning]]. **Condition:** Logged data carries reward labels.

## Search Terms

Upstream search terms may be related terms rather than exact synonyms: batch reinforcement learning; offline RL.

## Source

[Canonical Taxonomy](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/taxonomy.yml) · [Passage Alignment](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/mlsysbook-alignment.yml)

Taxonomy definitions and relationship wording: CC BY 4.0, with attribution to the Machine Learning Systems curriculum by Vijay Janapa Reddi and contributors. The textbook retains its separate license.
