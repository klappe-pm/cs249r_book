---
title: Device Cloud Partitioning
type: concept
tags:
- Type/Concept
- Group/Lifecycle
- Topic/On_Device_Edge_Deployment
source_repository: https://github.com/klappe-pm/cs249r_book
source_commit: de87c0103806d7bfb1c677dbb77a2b92fa00c298
source_path: taxonomy/taxonomy.yml
source_label: Device-cloud partitioning
taxonomy_id: mlsys.device-cloud-partitioning
taxonomy_status: draft
taxonomy_version: 0.4-draft
---

# Device Cloud Partitioning

Splitting inference between device and server, by layer or by model, to balance latency, energy, bandwidth, and privacy.

## Browsing Home

[[02 Concepts/Lifecycle/Deployment & Serving/On Device & Edge Deployment Subject|On Device & Edge Deployment]] → [[02 Concepts/Lifecycle/Deployment & Serving/Deployment & Serving Index|Deployment & Serving]]

## Book Passages

These are explicitly recorded related passages from the upstream draft alignment; they do not certify complete coverage.

No explicit passage alignment is recorded for this concept. Subject reading pointers are available in its browsing home.

## Conditional Relationships

These are the taxonomy's draft editorial relationships. Read each relationship with its condition; an outgoing link is not a prerequisite claim.

- Is a form of [[02 Concepts/Foundations/Workloads & Requirements/Execution Placement|Execution Placement]]. **Condition:** Holds when part of the computation can run on either side of a network link.

- Can reduce on-device [[02 Concepts/Qualities/Sustainability & Cost/Energy per Inference|Energy per Inference]]. **Condition:** Holds when uplink cost is lower than the compute it moves off device.

## Search Terms

Upstream search terms may be related terms rather than exact synonyms: split computing; offloading.

## Source

[Canonical Taxonomy](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/taxonomy.yml) · [Passage Alignment](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/mlsysbook-alignment.yml)

Taxonomy definitions and relationship wording: CC BY 4.0, with attribution to the Machine Learning Systems curriculum by Vijay Janapa Reddi and contributors. The textbook retains its separate license.
