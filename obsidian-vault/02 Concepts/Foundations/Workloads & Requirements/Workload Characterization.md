---
title: Workload Characterization
type: concept
tags:
- Type/Concept
- Group/Foundations
- Topic/Workload_Characterization
source_repository: https://github.com/klappe-pm/cs249r_book
source_commit: de87c0103806d7bfb1c677dbb77a2b92fa00c298
source_path: taxonomy/taxonomy.yml
source_label: Workload characterization
taxonomy_id: mlsys.workload
taxonomy_status: draft
taxonomy_version: 0.4-draft
---

# Workload Characterization

The input, request, model, and execution distributions that a system must support.

## Browsing Home

[[02 Concepts/Foundations/Workloads & Requirements/Workload Characterization Subject|Workload Characterization]] → [[02 Concepts/Foundations/Workloads & Requirements/Workloads & Requirements Index|Workloads & Requirements]]

## Book Passages

These are explicitly recorded related passages from the upstream draft alignment; they do not certify complete coverage.

No explicit passage alignment is recorded for this concept. Subject reading pointers are available in its browsing home.

## Conditional Relationships

These are the taxonomy's draft editorial relationships. Read each relationship with its condition; an outgoing link is not a prerequisite claim.

- Determines resource demand for [[02 Concepts/Stack/Datacenter Infrastructure & Fleet/Capacity Planning|Capacity Planning]]. **Condition:** Sizing must include input and request distributions, not just a representative average.

- Is characterized empirically using [[02 Concepts/Foundations/Workloads & Requirements/Workload Trace|Workload Trace]]. **Condition:** The trace window covers the arrival, size, and mix variation that matters for the decision being evaluated.

- Quantifies the demands of [[02 Concepts/System Types/Agentic Systems/Agentic Workload|Agentic Workload]]. **Condition:** The workload is a multi-step agent trajectory rather than independent requests.

## Source

[Canonical Taxonomy](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/taxonomy.yml) · [Passage Alignment](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/mlsysbook-alignment.yml)

Taxonomy definitions and relationship wording: CC BY 4.0, with attribution to the Machine Learning Systems curriculum by Vijay Janapa Reddi and contributors. The textbook retains its separate license.
