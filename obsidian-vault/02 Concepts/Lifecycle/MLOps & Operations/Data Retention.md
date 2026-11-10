---
title: Data Retention
type: concept
tags:
- Type/Concept
- Group/Lifecycle
- Topic/Model_Retirement
source_repository: https://github.com/klappe-pm/cs249r_book
source_commit: de87c0103806d7bfb1c677dbb77a2b92fa00c298
source_path: taxonomy/taxonomy.yml
source_label: Data retention
taxonomy_id: mlsys.data-retention
taxonomy_status: draft
taxonomy_version: 0.4-draft
---

# Data Retention

Policy and mechanisms that set how long data, logs, and derived artifacts are kept and when they are deleted.

## Browsing Home

[[02 Concepts/Lifecycle/MLOps & Operations/Model Retirement Subject|Model Retirement]] → [[02 Concepts/Lifecycle/MLOps & Operations/MLOps & Operations Index|MLOps & Operations]]

## Book Passages

These are explicitly recorded related passages from the upstream draft alignment; they do not certify complete coverage.

No explicit passage alignment is recorded for this concept. Subject reading pointers are available in its browsing home.

## Conditional Relationships

These are the taxonomy's draft editorial relationships. Read each relationship with its condition; an outgoing link is not a prerequisite claim.

- Implements requirements of [[02 Concepts/Qualities/Security & Privacy/Privacy Requirements|Privacy Requirements]]. **Condition:** Holds when retention limits apply to raw data, logs, and derived artifacts such as features and models.

- Trades off against [[02 Concepts/Lifecycle/MLOps & Operations/Artifact Archival|Artifact Archival]]. **Condition:** Holds when audit or reproduction needs conflict with deletion obligations.

- Limits which past examples are available to [[02 Concepts/Lifecycle/Training & Adaptation/Experience Replay|Experience Replay]]. **Condition:** Holds when retention or deletion policies remove raw training data after a fixed period.

- Requires [[02 Concepts/Qualities/Security & Privacy/Machine Unlearning|Machine Unlearning]]. **Condition:** When deletion obligations extend to models trained on the deleted records.

## Source

[Canonical Taxonomy](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/taxonomy.yml) · [Passage Alignment](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/mlsysbook-alignment.yml)

Taxonomy definitions and relationship wording: CC BY 4.0, with attribution to the Machine Learning Systems curriculum by Vijay Janapa Reddi and contributors. The textbook retains its separate license.
