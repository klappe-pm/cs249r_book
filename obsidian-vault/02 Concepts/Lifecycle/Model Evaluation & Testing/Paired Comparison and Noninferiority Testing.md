---
title: Paired Comparison and Noninferiority Testing
type: concept
tags:
- Type/Concept
- Group/Lifecycle
- Topic/Evaluation_Design_Experiments
source_repository: https://github.com/klappe-pm/cs249r_book
source_commit: de87c0103806d7bfb1c677dbb77a2b92fa00c298
source_path: taxonomy/taxonomy.yml
source_label: Paired comparison and noninferiority testing
taxonomy_id: mlsys.paired-comparison
taxonomy_status: draft
taxonomy_version: 0.4-draft
---

# Paired Comparison and Noninferiority Testing

Comparing two systems on the same items or units and testing per-item differences, including whether a candidate is no worse than a baseline by a preset margin.

## Browsing Home

[[02 Concepts/Lifecycle/Model Evaluation & Testing/Evaluation Design & Experiments Subject|Evaluation Design & Experiments]] → [[02 Concepts/Lifecycle/Model Evaluation & Testing/Model Evaluation & Testing Index|Model Evaluation & Testing]]

## Book Passages

These are explicitly recorded related passages from the upstream draft alignment; they do not certify complete coverage.

No explicit passage alignment is recorded for this concept. Subject reading pointers are available in its browsing home.

## Conditional Relationships

These are the taxonomy's draft editorial relationships. Read each relationship with its condition; an outgoing link is not a prerequisite claim.

- Cancels shared item variance from [[02 Concepts/Lifecycle/Model Evaluation & Testing/Statistical Uncertainty|Statistical Uncertainty]]. **Condition:** Both systems are scored on the same items.

- Tests candidates against [[02 Concepts/Foundations/Workloads & Requirements/Baseline|Baseline]]. **Condition:** A noninferiority margin is declared in advance.

- Raises, by cancelling shared item variance, [[02 Concepts/Lifecycle/Model Evaluation & Testing/Statistical Power|Statistical Power]]. **Condition:** When both systems are scored on the same items so per-item differences vary less than independent samples.

## Search Terms

Upstream search terms may be related terms rather than exact synonyms: paired difference test; noninferiority test.

## Source

[Canonical Taxonomy](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/taxonomy.yml) · [Passage Alignment](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/mlsysbook-alignment.yml)

Taxonomy definitions and relationship wording: CC BY 4.0, with attribution to the Machine Learning Systems curriculum by Vijay Janapa Reddi and contributors. The textbook retains its separate license.
