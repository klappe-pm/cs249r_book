---
title: System Requirements
type: concept
tags:
- Type/Concept
- Group/Foundations
- Topic/Requirements_SLOs_Baselines
source_repository: https://github.com/klappe-pm/cs249r_book
source_commit: de87c0103806d7bfb1c677dbb77a2b92fa00c298
source_path: taxonomy/taxonomy.yml
source_label: System requirements
taxonomy_id: mlsys.requirements
taxonomy_status: draft
taxonomy_version: 0.4-draft
---

# System Requirements

Measurable desired behavior and constraints for a specified workload.

## Browsing Home

[[02 Concepts/Foundations/Workloads & Requirements/Requirements, SLOs & Baselines Subject|Requirements, SLOs & Baselines]] → [[02 Concepts/Foundations/Workloads & Requirements/Workloads & Requirements Index|Workloads & Requirements]]

## Book Passages

These are explicitly recorded related passages from the upstream draft alignment; they do not certify complete coverage.

- [[01 Books/Volume I - Foundations/01 Foundations/03 ML Lifecycle/V1-03.06 Stage 1 Problem Definition#^sec-ml-workflow-balancing-competing-constraints-b92a|V1-03.06 Stage 1 Problem Definition]] — System requirements. [Exact Source Passage](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/books/vol1/03_ml_lifecycle/03_ml_lifecycle.qmd#L1036).

## Conditional Relationships

These are the taxonomy's draft editorial relationships. Read each relationship with its condition; an outgoing link is not a prerequisite claim.

- Sets acceptance thresholds for [[02 Concepts/Lifecycle/Model Evaluation & Testing/Evaluation Metrics|Evaluation Metrics]]. **Condition:** The operational outcome, evaluation population, and threshold must be declared.

- Sets targets for [[02 Concepts/Foundations/Workloads & Requirements/Service Level Objective|Service Level Objective]]. **Condition:** Service targets are part of the stated deployment requirements.

- Determine feasible [[02 Concepts/Foundations/Workloads & Requirements/Execution Placement|Execution Placement]]. **Condition:** Latency, privacy, connectivity, and power requirements rule out some device, edge, or datacenter placements.

- Set the externally promised terms of [[02 Concepts/Foundations/Workloads & Requirements/Service Level Agreement|Service Level Agreement]]. **Condition:** When service commitments to customers are part of the stated deployment requirements.

## Themes

- [[03 Themes/Constraints Drive Architecture|Constraints Drive Architecture]]

## Search Terms

Upstream search terms may be related terms rather than exact synonyms: acceptance criteria; non-functional requirements.

## Source

[Canonical Taxonomy](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/taxonomy.yml) · [Passage Alignment](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/mlsysbook-alignment.yml)

Taxonomy definitions and relationship wording: CC BY 4.0, with attribution to the Machine Learning Systems curriculum by Vijay Janapa Reddi and contributors. The textbook retains its separate license.
