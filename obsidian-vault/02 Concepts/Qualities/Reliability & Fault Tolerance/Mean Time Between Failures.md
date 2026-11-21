---
title: Mean Time Between Failures
type: concept
tags:
- Type/Concept
- Group/Qualities
- Topic/Hardware_Faults_Silent_Data_Corruption
source_repository: https://github.com/klappe-pm/cs249r_book
source_commit: de87c0103806d7bfb1c677dbb77a2b92fa00c298
source_path: taxonomy/taxonomy.yml
source_label: Mean time between failures
taxonomy_id: mlsys.mtbf
taxonomy_status: draft
taxonomy_version: 0.4-draft
---

# Mean Time Between Failures

The expected operating time between failures of a component or system; for independent components, system MTBF shrinks roughly in inverse proportion to component count.

## Browsing Home

[[02 Concepts/Qualities/Reliability & Fault Tolerance/Hardware Faults & Silent Data Corruption Subject|Hardware Faults & Silent Data Corruption]] → [[02 Concepts/Qualities/Reliability & Fault Tolerance/Reliability & Fault Tolerance Index|Reliability & Fault Tolerance]]

## Book Passages

These are explicitly recorded related passages from the upstream draft alignment; they do not certify complete coverage.

- [[01 Books/Volume II - Scaling/02 Distributed ML/07 Fault Tolerance/V2-07.03 The Mathematics of Inevitable Failure#^sec-fault-tolerance-reliability-reliability-mathematics-inevitable-failure-93ef|V2-07.03 The Mathematics of Inevitable Failure]] — Job failure rate. [Exact Source Passage](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/books/vol2/07_fault_tolerance/07_fault_tolerance.qmd#L208).

## Conditional Relationships

These are the taxonomy's draft editorial relationships. Read each relationship with its condition; an outgoing link is not a prerequisite claim.

- Determines [[02 Concepts/Qualities/Reliability & Fault Tolerance/Optimal Checkpoint Interval|Optimal Checkpoint Interval]]. **Condition:** Under approximately exponential failure times, where the optimal interval scales with the square root of checkpoint cost times MTBF.

- Raises [[02 Concepts/Qualities/Reliability & Fault Tolerance/Availability|Availability]]. **Condition:** For a repairable component in steady state, availability is approximately MTBF divided by MTBF plus mean time to repair.

- Bounds [[02 Concepts/Qualities/Performance, Efficiency & Benchmarking/Training Goodput|Training Goodput]]. **Condition:** For large synchronous jobs, where job MTBF shrinks with component count and each failure costs rework plus restart.

## Search Terms

Upstream search terms may be related terms rather than exact synonyms: MTBF.

## Source

[Canonical Taxonomy](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/taxonomy.yml) · [Passage Alignment](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/mlsysbook-alignment.yml)

Taxonomy definitions and relationship wording: CC BY 4.0, with attribution to the Machine Learning Systems curriculum by Vijay Janapa Reddi and contributors. The textbook retains its separate license.
