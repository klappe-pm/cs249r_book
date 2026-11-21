---
title: Alerting
type: concept
tags:
- Type/Concept
- Group/Lifecycle
- Topic/Monitoring_Observability
source_repository: https://github.com/klappe-pm/cs249r_book
source_commit: de87c0103806d7bfb1c677dbb77a2b92fa00c298
source_path: taxonomy/taxonomy.yml
source_label: Alerting
taxonomy_id: mlsys.alerting
taxonomy_status: draft
taxonomy_version: 0.4-draft
---

# Alerting

Rules that turn monitored signals into notifications for responders, tuned to balance missed incidents against alert fatigue.

## Browsing Home

[[02 Concepts/Lifecycle/MLOps & Operations/Monitoring & Observability Subject|Monitoring & Observability]] → [[02 Concepts/Lifecycle/MLOps & Operations/MLOps & Operations Index|MLOps & Operations]]

## Book Passages

These are explicitly recorded related passages from the upstream draft alignment; they do not certify complete coverage.

No explicit passage alignment is recorded for this concept. Subject reading pointers are available in its browsing home.

## Conditional Relationships

These are the taxonomy's draft editorial relationships. Read each relationship with its condition; an outgoing link is not a prerequisite claim.

- Initiates [[02 Concepts/Lifecycle/MLOps & Operations/Incident Response|Incident Response]]. **Condition:** Holds when alerts are actionable; excessive alerting degrades response through fatigue.

- Fires on thresholds over [[02 Concepts/Foundations/Workloads & Requirements/Service Level Indicator|Service Level Indicator]]. **Condition:** Applies when alerts are defined over user-facing indicators rather than raw resource metrics.

- Links each page to a [[02 Concepts/Lifecycle/MLOps & Operations/Runbook|Runbook]]. **Condition:** When alerts are actionable and name the procedure to follow.

- Fires on thresholds over statistics from [[02 Concepts/Lifecycle/MLOps & Operations/Drift Detection|Drift Detection]]. **Condition:** When drift statistics are alerted on directly; detected drift is a signal to diagnose, not proof of degraded quality.

## Source

[Canonical Taxonomy](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/taxonomy.yml) · [Passage Alignment](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/mlsysbook-alignment.yml)

Taxonomy definitions and relationship wording: CC BY 4.0, with attribution to the Machine Learning Systems curriculum by Vijay Janapa Reddi and contributors. The textbook retains its separate license.
