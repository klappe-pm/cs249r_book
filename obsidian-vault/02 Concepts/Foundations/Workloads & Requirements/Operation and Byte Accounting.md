---
title: Operation and Byte Accounting
type: concept
tags:
- Type/Concept
- Group/Foundations
- Topic/Workload_Characterization
source_repository: https://github.com/klappe-pm/cs249r_book
source_commit: de87c0103806d7bfb1c677dbb77a2b92fa00c298
source_path: taxonomy/taxonomy.yml
source_label: Operation and byte accounting
taxonomy_id: mlsys.flop-accounting
taxonomy_status: draft
taxonomy_version: 0.4-draft
---

# Operation and Byte Accounting

Estimating a workload's arithmetic operations and bytes moved per example, token, or step from model shapes, to predict cost before measurement.

## Browsing Home

[[02 Concepts/Foundations/Workloads & Requirements/Workload Characterization Subject|Workload Characterization]] → [[02 Concepts/Foundations/Workloads & Requirements/Workloads & Requirements Index|Workloads & Requirements]]

## Book Passages

These are explicitly recorded related passages from the upstream draft alignment; they do not certify complete coverage.

No explicit passage alignment is recorded for this concept. Subject reading pointers are available in its browsing home.

## Conditional Relationships

These are the taxonomy's draft editorial relationships. Read each relationship with its condition; an outgoing link is not a prerequisite claim.

- Supplies the operation and byte counts for [[02 Concepts/Foundations/Quantitative System Models/Arithmetic Intensity|Arithmetic Intensity]]. **Condition:** Operation and byte counts are taken at the same memory boundary.

- Estimates the operations and bytes of [[02 Concepts/Foundations/Workloads & Requirements/Workload Characterization|Workload Characterization]]. **Condition:** Model shapes and input sizes are known.

## Search Terms

Upstream search terms may be related terms rather than exact synonyms: FLOP counting; resource accounting; MAC counting.

## Source

[Canonical Taxonomy](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/taxonomy.yml) · [Passage Alignment](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/mlsysbook-alignment.yml)

Taxonomy definitions and relationship wording: CC BY 4.0, with attribution to the Machine Learning Systems curriculum by Vijay Janapa Reddi and contributors. The textbook retains its separate license.
