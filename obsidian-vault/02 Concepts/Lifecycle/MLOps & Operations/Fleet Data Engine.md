---
title: Fleet Data Engine
type: concept
tags:
- Type/Concept
- Group/Lifecycle
- Topic/Drift_Feedback_Loops_Retraining
source_repository: https://github.com/klappe-pm/cs249r_book
source_commit: de87c0103806d7bfb1c677dbb77a2b92fa00c298
source_path: taxonomy/taxonomy.yml
source_label: Fleet data engine
taxonomy_id: mlsys.fleet-data-engine
taxonomy_status: draft
taxonomy_version: 0.4-draft
---

# Fleet Data Engine

Collecting training data from deployed devices through on-device triggers that flag rare or uncertain events, uploading selected samples under bandwidth budgets for labeling and retraining.

## Browsing Home

[[02 Concepts/Lifecycle/MLOps & Operations/Drift, Feedback Loops & Retraining Subject|Drift, Feedback Loops & Retraining]] → [[02 Concepts/Lifecycle/MLOps & Operations/MLOps & Operations Index|MLOps & Operations]]

## Book Passages

These are explicitly recorded related passages from the upstream draft alignment; they do not certify complete coverage.

No explicit passage alignment is recorded for this concept. Subject reading pointers are available in its browsing home.

## Conditional Relationships

These are the taxonomy's draft editorial relationships. Read each relationship with its condition; an outgoing link is not a prerequisite claim.

- Selects uploads with [[02 Concepts/Lifecycle/Data Engineering/Active Learning|Active Learning]]. **Condition:** Triggers prioritize uncertain or rare events for labeling.

- Counters [[02 Concepts/Lifecycle/MLOps & Operations/Distribution Shift|Distribution Shift]]. **Condition:** Mined data covers conditions the deployed fleet now encounters.

## Search Terms

Upstream search terms may be related terms rather than exact synonyms: data engine; triggered data collection; edge-case mining; data flywheel.

## Source

[Canonical Taxonomy](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/taxonomy.yml) · [Passage Alignment](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/mlsysbook-alignment.yml)

Taxonomy definitions and relationship wording: CC BY 4.0, with attribution to the Machine Learning Systems curriculum by Vijay Janapa Reddi and contributors. The textbook retains its separate license.
