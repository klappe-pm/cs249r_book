---
title: Process Reward Model
type: concept
tags:
- Type/Concept
- Group/Lifecycle
- Topic/Test_Time_Compute
source_repository: https://github.com/klappe-pm/cs249r_book
source_commit: de87c0103806d7bfb1c677dbb77a2b92fa00c298
source_path: taxonomy/taxonomy.yml
source_label: Process reward model
taxonomy_id: mlsys.process-reward-model
taxonomy_status: draft
taxonomy_version: 0.4-draft
---

# Process Reward Model

A verifier that scores intermediate reasoning steps rather than only final answers.

## Browsing Home

[[02 Concepts/Lifecycle/Deployment & Serving/Test Time Compute Subject|Test Time Compute]] → [[02 Concepts/Lifecycle/Deployment & Serving/Deployment & Serving Index|Deployment & Serving]]

## Book Passages

These are explicitly recorded related passages from the upstream draft alignment; they do not certify complete coverage.

No explicit passage alignment is recorded for this concept. Subject reading pointers are available in its browsing home.

## Conditional Relationships

These are the taxonomy's draft editorial relationships. Read each relationship with its condition; an outgoing link is not a prerequisite claim.

- Is a step-level form of [[02 Concepts/Lifecycle/Deployment & Serving/Verifier|Verifier]]. **Condition:** Requires step-level labels or estimates of step correctness.

- Can supply the training signal of [[02 Concepts/Lifecycle/Training & Adaptation/Reward Model|Reward Model]]. **Condition:** When step scores train the policy rather than only guide inference-time search.

- Provides step-level signals for [[02 Concepts/Lifecycle/Training & Adaptation/Credit Assignment|Credit Assignment]]. **Condition:** Intermediate steps can be judged.

## Search Terms

Upstream search terms may be related terms rather than exact synonyms: PRM.

## Source

[Canonical Taxonomy](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/taxonomy.yml) · [Passage Alignment](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/mlsysbook-alignment.yml)

Taxonomy definitions and relationship wording: CC BY 4.0, with attribution to the Machine Learning Systems curriculum by Vijay Janapa Reddi and contributors. The textbook retains its separate license.
