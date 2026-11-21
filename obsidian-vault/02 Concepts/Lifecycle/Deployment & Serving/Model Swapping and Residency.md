---
title: Model Swapping and Residency
type: concept
tags:
- Type/Concept
- Group/Lifecycle
- Topic/Serving_Architectures
source_repository: https://github.com/klappe-pm/cs249r_book
source_commit: de87c0103806d7bfb1c677dbb77a2b92fa00c298
source_path: taxonomy/taxonomy.yml
source_label: Model swapping and residency
taxonomy_id: mlsys.model-swapping
taxonomy_status: draft
taxonomy_version: 0.4-draft
---

# Model Swapping and Residency

Keeping some models' weights resident in accelerator memory and loading others from host memory or storage on demand, so a shared accelerator serves more models than fit at once, at the cost of transfer latency.

## Browsing Home

[[02 Concepts/Lifecycle/Deployment & Serving/Serving Architectures Subject|Serving Architectures]] → [[02 Concepts/Lifecycle/Deployment & Serving/Deployment & Serving Index|Deployment & Serving]]

## Book Passages

These are explicitly recorded related passages from the upstream draft alignment; they do not certify complete coverage.

No explicit passage alignment is recorded for this concept. Subject reading pointers are available in its browsing home.

## Conditional Relationships

These are the taxonomy's draft editorial relationships. Read each relationship with its condition; an outgoing link is not a prerequisite claim.

- Is the weight-movement mechanism of [[02 Concepts/Lifecycle/Deployment & Serving/Multi Model Serving|Multi Model Serving]]. **Condition:** When more models are offered than fit in accelerator memory at once.

- Lets otherwise idle accelerators serve other models, raising [[02 Concepts/Qualities/Performance, Efficiency & Benchmarking/Resource Utilization|Resource Utilization]]. **Condition:** When demand across models is uneven over time and the transfer latency fits the service objective.

## Search Terms

Upstream search terms may be related terms rather than exact synonyms: weight swapping; model residency management.

## Source

[Canonical Taxonomy](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/taxonomy.yml) · [Passage Alignment](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/mlsysbook-alignment.yml)

Taxonomy definitions and relationship wording: CC BY 4.0, with attribution to the Machine Learning Systems curriculum by Vijay Janapa Reddi and contributors. The textbook retains its separate license.
