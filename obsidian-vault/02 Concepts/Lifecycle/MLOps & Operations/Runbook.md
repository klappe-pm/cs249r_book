---
title: Runbook
type: concept
tags:
- Type/Concept
- Group/Lifecycle
- Topic/Incident_Response
- Context/Background
source_repository: https://github.com/klappe-pm/cs249r_book
source_commit: de87c0103806d7bfb1c677dbb77a2b92fa00c298
source_path: taxonomy/taxonomy.yml
source_label: Runbook
taxonomy_id: mlsys.runbook
taxonomy_status: draft
taxonomy_version: 0.4-draft
---

# Runbook

A written or automated procedure attached to an alert that says how to confirm, mitigate, and escalate a known failure, so that response speed does not depend on who is on call.

## Browsing Home

[[02 Concepts/Lifecycle/MLOps & Operations/Incident Response Subject|Incident Response]] → [[02 Concepts/Lifecycle/MLOps & Operations/MLOps & Operations Index|MLOps & Operations]]

This is a background concept on which ML systems reasoning depends; that classification does not make it optional.

## Book Passages

These are explicitly recorded related passages from the upstream draft alignment; they do not certify complete coverage.

No explicit passage alignment is recorded for this concept. Subject reading pointers are available in its browsing home.

## Conditional Relationships

These are the taxonomy's draft editorial relationships. Read each relationship with its condition; an outgoing link is not a prerequisite claim.

- Scripts the first steps of [[02 Concepts/Lifecycle/MLOps & Operations/Incident Response|Incident Response]]. **Condition:** When the failure has been seen before and its mitigation is known.

- Often names, as the first mitigation, [[02 Concepts/Lifecycle/MLOps & Operations/Rollback|Rollback]]. **Condition:** For model-serving incidents where the previous version is known good.

## Search Terms

Upstream search terms may be related terms rather than exact synonyms: playbook; on-call procedure; operational procedure.

## Source

[Canonical Taxonomy](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/taxonomy.yml) · [Passage Alignment](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/mlsysbook-alignment.yml)

Taxonomy definitions and relationship wording: CC BY 4.0, with attribution to the Machine Learning Systems curriculum by Vijay Janapa Reddi and contributors. The textbook retains its separate license.
