---
title: Autoscaling
type: concept
tags:
- Type/Concept
- Group/Lifecycle
- Topic/Batching_Admission_Autoscaling
source_repository: https://github.com/klappe-pm/cs249r_book
source_commit: de87c0103806d7bfb1c677dbb77a2b92fa00c298
source_path: taxonomy/taxonomy.yml
source_label: Autoscaling
taxonomy_id: mlsys.autoscaling
taxonomy_status: draft
taxonomy_version: 0.4-draft
---

# Autoscaling

Changing provisioned service resources in response to measured or predicted demand.

## Browsing Home

[[02 Concepts/Lifecycle/Deployment & Serving/Batching, Admission & Autoscaling Subject|Batching, Admission & Autoscaling]] → [[02 Concepts/Lifecycle/Deployment & Serving/Deployment & Serving Index|Deployment & Serving]]

## Book Passages

These are explicitly recorded related passages from the upstream draft alignment; they do not certify complete coverage.

No explicit passage alignment is recorded for this concept. Subject reading pointers are available in its browsing home.

## Conditional Relationships

These are the taxonomy's draft editorial relationships. Read each relationship with its condition; an outgoing link is not a prerequisite claim.

- Adjusts provisioned [[02 Concepts/Foundations/Quantitative System Models/Service Capacity|Service Capacity]]. **Condition:** Provisioning delay, state transfer, and warm-up affect when capacity becomes useful.

- Raises average [[02 Concepts/Qualities/Performance, Efficiency & Benchmarking/Resource Utilization|Resource Utilization]]. **Condition:** Holds when demand varies and scale-down is permitted.

- Adds capacity before requests wait, cutting [[02 Concepts/Foundations/Quantitative System Models/Queueing Delay|Queueing Delay]]. **Condition:** When new replicas become ready faster than the load rises; cold starts delay the effect.

## Source

[Canonical Taxonomy](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/taxonomy.yml) · [Passage Alignment](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/mlsysbook-alignment.yml)

Taxonomy definitions and relationship wording: CC BY 4.0, with attribution to the Machine Learning Systems curriculum by Vijay Janapa Reddi and contributors. The textbook retains its separate license.
