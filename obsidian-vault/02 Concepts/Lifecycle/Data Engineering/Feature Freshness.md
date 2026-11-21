---
title: Feature Freshness
type: concept
tags:
- Type/Concept
- Group/Lifecycle
- Topic/Leakage_Training_Serving_Skew
source_repository: https://github.com/klappe-pm/cs249r_book
source_commit: de87c0103806d7bfb1c677dbb77a2b92fa00c298
source_path: taxonomy/taxonomy.yml
source_label: Feature freshness
taxonomy_id: mlsys.feature-freshness
taxonomy_status: draft
taxonomy_version: 0.4-draft
---

# Feature Freshness

How recent a feature's value is at the moment it is used for a prediction, relative to the recency assumed when training examples were built; stale values shift inputs away from the training distribution.

## Browsing Home

[[02 Concepts/Lifecycle/Data Engineering/Leakage & Training Serving Skew Subject|Leakage & Training Serving Skew]] → [[02 Concepts/Lifecycle/Data Engineering/Data Engineering Index|Data Engineering]]

## Book Passages

These are explicitly recorded related passages from the upstream draft alignment; they do not certify complete coverage.

No explicit passage alignment is recorded for this concept. Subject reading pointers are available in its browsing home.

## Conditional Relationships

These are the taxonomy's draft editorial relationships. Read each relationship with its condition; an outgoing link is not a prerequisite claim.

- Stale values can cause [[02 Concepts/Lifecycle/Data Engineering/Training Serving Skew|Training Serving Skew]]. **Condition:** Holds when serving-time feature age differs from the age assumed when training examples were built.

## Source

[Canonical Taxonomy](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/taxonomy.yml) · [Passage Alignment](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/mlsysbook-alignment.yml)

Taxonomy definitions and relationship wording: CC BY 4.0, with attribution to the Machine Learning Systems curriculum by Vijay Janapa Reddi and contributors. The textbook retains its separate license.
