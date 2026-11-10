---
title: Side Channel Attack
type: concept
tags:
- Type/Concept
- Group/Qualities
- Topic/Access_Control_Isolation
source_repository: https://github.com/klappe-pm/cs249r_book
source_commit: de87c0103806d7bfb1c677dbb77a2b92fa00c298
source_path: taxonomy/taxonomy.yml
source_label: Side-channel attack
taxonomy_id: mlsys.side-channel
taxonomy_status: draft
taxonomy_version: 0.4-draft
---

# Side Channel Attack

Inferring secrets from observable resource behavior, such as timing, power, memory, or cache contention, across an isolation boundary.

## Browsing Home

[[02 Concepts/Qualities/Security & Privacy/Access Control & Isolation Subject|Access Control & Isolation]] → [[02 Concepts/Qualities/Security & Privacy/Security & Privacy Index|Security & Privacy]]

## Book Passages

These are explicitly recorded related passages from the upstream draft alignment; they do not certify complete coverage.

No explicit passage alignment is recorded for this concept. Subject reading pointers are available in its browsing home.

## Conditional Relationships

These are the taxonomy's draft editorial relationships. Read each relationship with its condition; an outgoing link is not a prerequisite claim.

- Can bypass [[02 Concepts/Qualities/Security & Privacy/Execution Isolation|Execution Isolation]]. **Condition:** When tenants share accelerators, caches, memory, or interconnect whose timing or contention is observable across the boundary.

- Can cause [[02 Concepts/Qualities/Security & Privacy/Privacy Leakage|Privacy Leakage]]. **Condition:** When observed timing, power, or memory behavior correlates with secret inputs or model parameters.

## Source

[Canonical Taxonomy](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/taxonomy.yml) · [Passage Alignment](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/mlsysbook-alignment.yml)

Taxonomy definitions and relationship wording: CC BY 4.0, with attribution to the Machine Learning Systems curriculum by Vijay Janapa Reddi and contributors. The textbook retains its separate license.
