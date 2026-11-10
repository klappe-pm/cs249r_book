---
title: Individual Fairness
type: concept
tags:
- Type/Concept
- Group/Qualities
- Topic/Fairness_Bias
source_repository: https://github.com/klappe-pm/cs249r_book
source_commit: de87c0103806d7bfb1c677dbb77a2b92fa00c298
source_path: taxonomy/taxonomy.yml
source_label: Individual fairness
taxonomy_id: mlsys.individual-fairness
taxonomy_status: draft
taxonomy_version: 0.4-draft
---

# Individual Fairness

A requirement that individuals who are similar with respect to the task receive similar outcomes under a stated similarity metric.

## Browsing Home

[[02 Concepts/Qualities/Responsible AI/Fairness & Bias Subject|Fairness & Bias]] → [[02 Concepts/Qualities/Responsible AI/Responsible AI Index|Responsible AI]]

## Book Passages

These are explicitly recorded related passages from the upstream draft alignment; they do not certify complete coverage.

No explicit passage alignment is recorded for this concept. Subject reading pointers are available in its browsing home.

## Conditional Relationships

These are the taxonomy's draft editorial relationships. Read each relationship with its condition; an outgoing link is not a prerequisite claim.

- Can conflict with [[02 Concepts/Qualities/Responsible AI/Group Fairness Metrics|Group Fairness Metrics]]. **Condition:** Holds when similarity under the task metric does not align with group membership.

- States fairness over similar individuals rather than across groups as in [[02 Concepts/Qualities/Responsible AI/Fairness Criteria|Fairness Criteria]]. **Condition:** When a system must choose which fairness notion to enforce or audit.

- Constrains [[02 Concepts/Foundations/Workloads & Requirements/Decision Policy|Decision Policy]]. **Condition:** When a task-specific similarity metric is declared and accepted by stakeholders.

## Source

[Canonical Taxonomy](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/taxonomy.yml) · [Passage Alignment](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/mlsysbook-alignment.yml)

Taxonomy definitions and relationship wording: CC BY 4.0, with attribution to the Machine Learning Systems curriculum by Vijay Janapa Reddi and contributors. The textbook retains its separate license.
