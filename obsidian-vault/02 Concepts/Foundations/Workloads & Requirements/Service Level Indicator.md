---
title: Service Level Indicator
type: concept
tags:
- Type/Concept
- Group/Foundations
- Topic/Requirements_SLOs_Baselines
source_repository: https://github.com/klappe-pm/cs249r_book
source_commit: de87c0103806d7bfb1c677dbb77a2b92fa00c298
source_path: taxonomy/taxonomy.yml
source_label: Service-level indicator
taxonomy_id: mlsys.sli
taxonomy_status: draft
taxonomy_version: 0.4-draft
---

# Service Level Indicator

A quantitative measure of one aspect of delivered service, such as latency, availability, or accepted-output rate, computed over a stated population and window.

## Browsing Home

[[02 Concepts/Foundations/Workloads & Requirements/Requirements, SLOs & Baselines Subject|Requirements, SLOs & Baselines]] → [[02 Concepts/Foundations/Workloads & Requirements/Workloads & Requirements Index|Workloads & Requirements]]

## Book Passages

These are explicitly recorded related passages from the upstream draft alignment; they do not certify complete coverage.

No explicit passage alignment is recorded for this concept. Subject reading pointers are available in its browsing home.

## Conditional Relationships

These are the taxonomy's draft editorial relationships. Read each relationship with its condition; an outgoing link is not a prerequisite claim.

- Is the measured quantity in [[02 Concepts/Foundations/Workloads & Requirements/Service Level Objective|Service Level Objective]]. **Condition:** The indicator's population, window, and aggregation must match the objective's.

- Commonly measures, as a percentile, [[02 Concepts/Lifecycle/Deployment & Serving/Tail Latency|Tail Latency]]. **Condition:** Latency indicators are computed as a high percentile over a stated request population and window.

- Commonly measures [[02 Concepts/Qualities/Reliability & Fault Tolerance/Availability|Availability]]. **Condition:** Availability indicators count successful requests or uptime over a defined population and window.

## Search Terms

Upstream search terms may be related terms rather than exact synonyms: SLI.

## Source

[Canonical Taxonomy](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/taxonomy.yml) · [Passage Alignment](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/mlsysbook-alignment.yml)

Taxonomy definitions and relationship wording: CC BY 4.0, with attribution to the Machine Learning Systems curriculum by Vijay Janapa Reddi and contributors. The textbook retains its separate license.
