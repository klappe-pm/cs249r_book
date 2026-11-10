---
title: Online and Offline Feature Consistency
type: concept
tags:
- Type/Concept
- Group/Lifecycle
- Topic/Leakage_Training_Serving_Skew
source_repository: https://github.com/klappe-pm/cs249r_book
source_commit: de87c0103806d7bfb1c677dbb77a2b92fa00c298
source_path: taxonomy/taxonomy.yml
source_label: Online and offline feature consistency
taxonomy_id: mlsys.online-feature-consistency
taxonomy_status: draft
taxonomy_version: 0.4-draft
---

# Online and Offline Feature Consistency

Keeping the feature values materialized in the low-latency online store consistent with the offline values used for training, as features are recomputed, backfilled, and updated.

## Browsing Home

[[02 Concepts/Lifecycle/Data Engineering/Leakage & Training Serving Skew Subject|Leakage & Training Serving Skew]] → [[02 Concepts/Lifecycle/Data Engineering/Data Engineering Index|Data Engineering]]

## Book Passages

These are explicitly recorded related passages from the upstream draft alignment; they do not certify complete coverage.

No explicit passage alignment is recorded for this concept. Subject reading pointers are available in its browsing home.

## Conditional Relationships

These are the taxonomy's draft editorial relationships. Read each relationship with its condition; an outgoing link is not a prerequisite claim.

- Prevents [[02 Concepts/Lifecycle/Data Engineering/Training Serving Skew|Training Serving Skew]]. **Condition:** Online and offline stores are populated by separate jobs.

- Trades against [[02 Concepts/Lifecycle/Data Engineering/Feature Freshness|Feature Freshness]]. **Condition:** Features are updated faster than they can be materialized consistently.

## Search Terms

Upstream search terms may be related terms rather than exact synonyms: feature materialization; online store consistency.

## Source

[Canonical Taxonomy](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/taxonomy.yml) · [Passage Alignment](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/mlsysbook-alignment.yml)

Taxonomy definitions and relationship wording: CC BY 4.0, with attribution to the Machine Learning Systems curriculum by Vijay Janapa Reddi and contributors. The textbook retains its separate license.
