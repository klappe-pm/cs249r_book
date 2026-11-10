---
title: Error Budget
type: concept
tags:
- Type/Concept
- Group/Foundations
- Topic/Requirements_SLOs_Baselines
source_repository: https://github.com/klappe-pm/cs249r_book
source_commit: de87c0103806d7bfb1c677dbb77a2b92fa00c298
source_path: taxonomy/taxonomy.yml
source_label: Error budget
taxonomy_id: mlsys.error-budget
taxonomy_status: draft
taxonomy_version: 0.4-draft
---

# Error Budget

The amount of service-level-objective violation permitted over a window, used to pace changes and risk against a reliability target.

## Browsing Home

[[02 Concepts/Foundations/Workloads & Requirements/Requirements, SLOs & Baselines Subject|Requirements, SLOs & Baselines]] → [[02 Concepts/Foundations/Workloads & Requirements/Workloads & Requirements Index|Workloads & Requirements]]

## Book Passages

These are explicitly recorded related passages from the upstream draft alignment; they do not certify complete coverage.

No explicit passage alignment is recorded for this concept. Subject reading pointers are available in its browsing home.

## Conditional Relationships

These are the taxonomy's draft editorial relationships. Read each relationship with its condition; an outgoing link is not a prerequisite claim.

- Paces [[02 Concepts/Lifecycle/MLOps & Operations/Staged Rollout|Staged Rollout]]. **Condition:** Teams agree to slow or halt changes when the remaining budget is exhausted.

- Can freeze releases through [[02 Concepts/Lifecycle/MLOps & Operations/Release Gate|Release Gate]]. **Condition:** Teams agree that an exhausted budget blocks or slows promotion of new versions.

- Sets burn-rate thresholds for [[02 Concepts/Lifecycle/MLOps & Operations/Alerting|Alerting]]. **Condition:** Alerts fire when the budget is being consumed faster than the window allows.

## Source

[Canonical Taxonomy](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/taxonomy.yml) · [Passage Alignment](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/mlsysbook-alignment.yml)

Taxonomy definitions and relationship wording: CC BY 4.0, with attribution to the Machine Learning Systems curriculum by Vijay Janapa Reddi and contributors. The textbook retains its separate license.
