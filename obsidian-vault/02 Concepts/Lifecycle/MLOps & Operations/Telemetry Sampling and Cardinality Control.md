---
title: Telemetry Sampling and Cardinality Control
type: concept
tags:
- Type/Concept
- Group/Lifecycle
- Topic/Monitoring_Observability
- Context/Background
source_repository: https://github.com/klappe-pm/cs249r_book
source_commit: de87c0103806d7bfb1c677dbb77a2b92fa00c298
source_path: taxonomy/taxonomy.yml
source_label: Telemetry sampling and cardinality control
taxonomy_id: mlsys.telemetry-sampling
taxonomy_status: draft
taxonomy_version: 0.4-draft
---

# Telemetry Sampling and Cardinality Control

Choosing which traces, events, and metric label combinations to keep, by sampling and by bounding or aggregating label values, so fleet telemetry stays affordable at the risk of losing rare failures and fine-grained detail.

## Browsing Home

[[02 Concepts/Lifecycle/MLOps & Operations/Monitoring & Observability Subject|Monitoring & Observability]] → [[02 Concepts/Lifecycle/MLOps & Operations/MLOps & Operations Index|MLOps & Operations]]

This is a background concept on which ML systems reasoning depends; that classification does not make it optional.

## Book Passages

These are explicitly recorded related passages from the upstream draft alignment; they do not certify complete coverage.

No explicit passage alignment is recorded for this concept. Subject reading pointers are available in its browsing home.

## Conditional Relationships

These are the taxonomy's draft editorial relationships. Read each relationship with its condition; an outgoing link is not a prerequisite claim.

- Trades telemetry cost against the investigative reach of [[02 Concepts/Lifecycle/MLOps & Operations/System Observability|System Observability]]. **Condition:** When sampling drops the records, or aggregation drops the label detail, that would explain a rare failure.

## Search Terms

Upstream search terms may be related terms rather than exact synonyms: trace sampling; tail-based sampling; metric cardinality management.

## Source

[Canonical Taxonomy](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/taxonomy.yml) · [Passage Alignment](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/mlsysbook-alignment.yml)

Taxonomy definitions and relationship wording: CC BY 4.0, with attribution to the Machine Learning Systems curriculum by Vijay Janapa Reddi and contributors. The textbook retains its separate license.
