---
title: Capacity Planning
type: concept
tags:
- Type/Concept
- Group/Stack
- Topic/Capacity_Planning_Multi_Tenancy
source_repository: https://github.com/klappe-pm/cs249r_book
source_commit: de87c0103806d7bfb1c677dbb77a2b92fa00c298
source_path: taxonomy/taxonomy.yml
source_label: Capacity planning
taxonomy_id: mlsys.capacity-planning
taxonomy_status: draft
taxonomy_version: 0.4-draft
---

# Capacity Planning

Provisioning resources for a workload distribution and service objectives.

## Browsing Home

[[02 Concepts/Stack/Datacenter Infrastructure & Fleet/Capacity Planning & Multi Tenancy Subject|Capacity Planning & Multi Tenancy]] → [[02 Concepts/Stack/Datacenter Infrastructure & Fleet/Datacenter Infrastructure & Fleet Index|Datacenter Infrastructure & Fleet]]

## Book Passages

These are explicitly recorded related passages from the upstream draft alignment; they do not certify complete coverage.

- [[01 Books/Volume I - Foundations/04 Deployment/13 Model Serving/V1-13.11 Economics and Planning#^sec-model-serving-capacity-planning-96a3|V1-13.11 Economics and Planning]] — Serving capacity. [Exact Source Passage](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/books/vol1/13_model_serving/13_model_serving.qmd#L5702).

## Conditional Relationships

These are the taxonomy's draft editorial relationships. Read each relationship with its condition; an outgoing link is not a prerequisite claim.

- Is sized against [[02 Concepts/Foundations/Workloads & Requirements/Service Level Objective|Service Level Objective]]. **Condition:** Provisioning decisions must account for demand variation and resource constraints.

- Grounds demand estimates in [[02 Concepts/Foundations/Workloads & Requirements/Workload Trace|Workload Trace]]. **Condition:** The trace is representative of the arrival, size, and mix distribution being provisioned for.

- Sizes concurrency with [[02 Concepts/Foundations/Quantitative System Models/Little's Law|Little's Law]]. **Condition:** Arrival rate and time in system are measured for a stable operating point.

- Sizes accelerators from [[02 Concepts/Foundations/Workloads & Requirements/Inference Compute and Memory Estimate|Inference Compute and Memory Estimate]]. **Condition:** Planning precedes measurement on the target system.

## Source

[Canonical Taxonomy](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/taxonomy.yml) · [Passage Alignment](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/mlsysbook-alignment.yml)

Taxonomy definitions and relationship wording: CC BY 4.0, with attribution to the Machine Learning Systems curriculum by Vijay Janapa Reddi and contributors. The textbook retains its separate license.
