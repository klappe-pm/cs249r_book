---
title: Group Fairness Metrics
type: concept
tags:
- Type/Concept
- Group/Qualities
- Topic/Fairness_Bias
source_repository: https://github.com/klappe-pm/cs249r_book
source_commit: de87c0103806d7bfb1c677dbb77a2b92fa00c298
source_path: taxonomy/taxonomy.yml
source_label: Group fairness metrics
taxonomy_id: mlsys.group-fairness-metric
taxonomy_status: draft
taxonomy_version: 0.4-draft
---

# Group Fairness Metrics

Statistics comparing selection rates, error rates, or calibration of a model's decisions across protected groups.

## Browsing Home

[[02 Concepts/Qualities/Responsible AI/Fairness & Bias Subject|Fairness & Bias]] → [[02 Concepts/Qualities/Responsible AI/Responsible AI Index|Responsible AI]]

## Book Passages

These are explicitly recorded related passages from the upstream draft alignment; they do not certify complete coverage.

- [[01 Books/Volume I - Foundations/04 Deployment/15 Responsible Engineering/V1-15.04 Responsible Engineering Across the Lifecycle#^sec-responsible-engineering-testing-across-populations-9f20|V1-15.04 Responsible Engineering Across the Lifecycle]] — Subgroup fairness. [Exact Source Passage](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/books/vol1/15_responsible_engr/15_responsible_engr.qmd#L585).

## Conditional Relationships

These are the taxonomy's draft editorial relationships. Read each relationship with its condition; an outgoing link is not a prerequisite claim.

- Measures [[02 Concepts/Qualities/Responsible AI/Fairness Criteria|Fairness Criteria]]. **Condition:** A metric measures one criterion on a chosen population and grouping; other criteria remain unmeasured.

- Measures the disparity produced by [[02 Concepts/Qualities/Responsible AI/Proxy Discrimination|Proxy Discrimination]]. **Condition:** When controlled comparisons or causal evidence isolate the part of the disparity due to proxy features.

## Search Terms

Upstream search terms may be related terms rather than exact synonyms: demographic parity; equalized odds; predictive parity; disparate impact ratio; equal opportunity.

## Source

[Canonical Taxonomy](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/taxonomy.yml) · [Passage Alignment](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/mlsysbook-alignment.yml)

Taxonomy definitions and relationship wording: CC BY 4.0, with attribution to the Machine Learning Systems curriculum by Vijay Janapa Reddi and contributors. The textbook retains its separate license.
