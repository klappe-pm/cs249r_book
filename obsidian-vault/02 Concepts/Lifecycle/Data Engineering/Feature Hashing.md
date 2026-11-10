---
title: Feature Hashing
type: concept
tags:
- Type/Concept
- Group/Lifecycle
- Topic/Data_Validation_Feature_Engineering
source_repository: https://github.com/klappe-pm/cs249r_book
source_commit: de87c0103806d7bfb1c677dbb77a2b92fa00c298
source_path: taxonomy/taxonomy.yml
source_label: Feature hashing
taxonomy_id: mlsys.feature-hashing
taxonomy_status: draft
taxonomy_version: 0.4-draft
---

# Feature Hashing

Mapping high-cardinality or open-vocabulary categorical values into a fixed number of buckets with a hash function, bounding table size at the cost of collisions.

## Browsing Home

[[02 Concepts/Lifecycle/Data Engineering/Data Validation & Feature Engineering Subject|Data Validation & Feature Engineering]] → [[02 Concepts/Lifecycle/Data Engineering/Data Engineering Index|Data Engineering]]

## Book Passages

These are explicitly recorded related passages from the upstream draft alignment; they do not certify complete coverage.

No explicit passage alignment is recorded for this concept. Subject reading pointers are available in its browsing home.

## Conditional Relationships

These are the taxonomy's draft editorial relationships. Read each relationship with its condition; an outgoing link is not a prerequisite claim.

- Is a technique within [[02 Concepts/Lifecycle/Data Engineering/Feature Engineering|Feature Engineering]]. **Condition:** Categorical inputs with large or open vocabularies.

- Bounds [[02 Concepts/Foundations/Workloads & Requirements/Memory Footprint|Memory Footprint]]. **Condition:** Weight or embedding tables indexed by hash bucket.

## Search Terms

Upstream search terms may be related terms rather than exact synonyms: hashing trick; hashed features.

## Source

[Canonical Taxonomy](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/taxonomy.yml) · [Passage Alignment](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/mlsysbook-alignment.yml)

Taxonomy definitions and relationship wording: CC BY 4.0, with attribution to the Machine Learning Systems curriculum by Vijay Janapa Reddi and contributors. The textbook retains its separate license.
