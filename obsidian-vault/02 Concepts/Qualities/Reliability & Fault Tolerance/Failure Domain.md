---
title: Failure Domain
type: concept
tags:
- Type/Concept
- Group/Qualities
- Topic/Hardware_Faults_Silent_Data_Corruption
source_repository: https://github.com/klappe-pm/cs249r_book
source_commit: de87c0103806d7bfb1c677dbb77a2b92fa00c298
source_path: taxonomy/taxonomy.yml
source_label: Failure domain
taxonomy_id: mlsys.failure-domain
taxonomy_status: draft
taxonomy_version: 0.4-draft
---

# Failure Domain

A set of components that can fail together from a shared cause, such as a rack, power feed, switch, or software release.

## Browsing Home

[[02 Concepts/Qualities/Reliability & Fault Tolerance/Hardware Faults & Silent Data Corruption Subject|Hardware Faults & Silent Data Corruption]] → [[02 Concepts/Qualities/Reliability & Fault Tolerance/Reliability & Fault Tolerance Index|Reliability & Fault Tolerance]]

## Book Passages

These are explicitly recorded related passages from the upstream draft alignment; they do not certify complete coverage.

No explicit passage alignment is recorded for this concept. Subject reading pointers are available in its browsing home.

## Conditional Relationships

These are the taxonomy's draft editorial relationships. Read each relationship with its condition; an outgoing link is not a prerequisite claim.

- Limits the protection of [[02 Concepts/Qualities/Reliability & Fault Tolerance/Replication and Failover|Replication and Failover]]. **Condition:** When replicas share a failure domain, a single cause can take out all of them together.

- Bounds [[02 Concepts/Qualities/Reliability & Fault Tolerance/Blast Radius|Blast Radius]]. **Condition:** When isolation between failure domains holds, so a fault does not propagate across shared dependencies.

## Source

[Canonical Taxonomy](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/taxonomy.yml) · [Passage Alignment](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/mlsysbook-alignment.yml)

Taxonomy definitions and relationship wording: CC BY 4.0, with attribution to the Machine Learning Systems curriculum by Vijay Janapa Reddi and contributors. The textbook retains its separate license.
