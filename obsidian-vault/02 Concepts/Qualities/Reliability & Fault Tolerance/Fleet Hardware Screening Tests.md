---
title: Fleet Hardware Screening Tests
type: concept
tags:
- Type/Concept
- Group/Qualities
- Topic/Hardware_Faults_Silent_Data_Corruption
source_repository: https://github.com/klappe-pm/cs249r_book
source_commit: de87c0103806d7bfb1c677dbb77a2b92fa00c298
source_path: taxonomy/taxonomy.yml
source_label: Fleet hardware screening tests
taxonomy_id: mlsys.fleet-hardware-screening
taxonomy_status: draft
taxonomy_version: 0.4-draft
---

# Fleet Hardware Screening Tests

Periodically running test workloads with known outputs on fleet accelerators and processors, at intake and during production, to find defective or silently miscomputing units before they corrupt jobs, at the cost of fleet time spent on tests.

## Browsing Home

[[02 Concepts/Qualities/Reliability & Fault Tolerance/Hardware Faults & Silent Data Corruption Subject|Hardware Faults & Silent Data Corruption]] → [[02 Concepts/Qualities/Reliability & Fault Tolerance/Reliability & Fault Tolerance Index|Reliability & Fault Tolerance]]

## Book Passages

These are explicitly recorded related passages from the upstream draft alignment; they do not certify complete coverage.

No explicit passage alignment is recorded for this concept. Subject reading pointers are available in its browsing home.

## Conditional Relationships

These are the taxonomy's draft editorial relationships. Read each relationship with its condition; an outgoing link is not a prerequisite claim.

- Finds the units responsible for [[02 Concepts/Qualities/Reliability & Fault Tolerance/Silent Data Corruption|Silent Data Corruption]]. **Condition:** For faults that reproduce under the test workload; intermittent and workload-dependent faults need longer or in-production screening.

- Compares outputs against [[02 Concepts/Lifecycle/Model Evaluation & Testing/Test Oracle|Test Oracle]]. **Condition:** When reference outputs are computed on trusted hardware or by a redundant run.

- Spends fleet time that would otherwise count toward [[02 Concepts/Qualities/Performance, Efficiency & Benchmarking/Resource Utilization|Resource Utilization]]. **Condition:** When screening runs on production capacity rather than on units already out of service.

## Search Terms

Upstream search terms may be related terms rather than exact synonyms: proactive SDC testing; fleet burn-in; accelerator diagnostics; known-answer tests.

## Source

[Canonical Taxonomy](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/taxonomy.yml) · [Passage Alignment](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/mlsysbook-alignment.yml)

Taxonomy definitions and relationship wording: CC BY 4.0, with attribution to the Machine Learning Systems curriculum by Vijay Janapa Reddi and contributors. The textbook retains its separate license.
