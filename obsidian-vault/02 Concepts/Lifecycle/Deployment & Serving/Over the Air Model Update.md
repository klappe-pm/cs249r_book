---
title: Over the Air Model Update
type: concept
tags:
- Type/Concept
- Group/Lifecycle
- Topic/On_Device_Edge_Deployment
source_repository: https://github.com/klappe-pm/cs249r_book
source_commit: de87c0103806d7bfb1c677dbb77a2b92fa00c298
source_path: taxonomy/taxonomy.yml
source_label: Over-the-air model update
taxonomy_id: mlsys.ota-model-update
taxonomy_status: draft
taxonomy_version: 0.4-draft
---

# Over the Air Model Update

Delivering model weights to deployed devices remotely, whether the first download after installation or a later version, with staging, verification, and rollback across the device fleet.

## Browsing Home

[[02 Concepts/Lifecycle/Deployment & Serving/On Device & Edge Deployment Subject|On Device & Edge Deployment]] → [[02 Concepts/Lifecycle/Deployment & Serving/Deployment & Serving Index|Deployment & Serving]]

## Book Passages

These are explicitly recorded related passages from the upstream draft alignment; they do not certify complete coverage.

No explicit passage alignment is recorded for this concept. Subject reading pointers are available in its browsing home.

## Conditional Relationships

These are the taxonomy's draft editorial relationships. Read each relationship with its condition; an outgoing link is not a prerequisite claim.

- Applies staged exposure from [[02 Concepts/Lifecycle/MLOps & Operations/Staged Rollout|Staged Rollout]]. **Condition:** Holds for device fleets where updates are staged by cohort and devices may be offline.

- Must verify [[02 Concepts/Qualities/Security & Privacy/Model Artifact Signing|Model Artifact Signing]]. **Condition:** Holds for any fleet where tampered models could be pushed.

- Relies on on-device [[02 Concepts/Lifecycle/MLOps & Operations/Rollback|Rollback]]. **Condition:** Requires the previous model to stay on the device.

## Search Terms

Upstream search terms may be related terms rather than exact synonyms: OTA update; on-demand model download; model download on first use; deferred model download.

## Source

[Canonical Taxonomy](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/taxonomy.yml) · [Passage Alignment](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/mlsysbook-alignment.yml)

Taxonomy definitions and relationship wording: CC BY 4.0, with attribution to the Machine Learning Systems curriculum by Vijay Janapa Reddi and contributors. The textbook retains its separate license.
