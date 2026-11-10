---
title: Cross Validation
type: concept
tags:
- Type/Concept
- Group/Lifecycle
- Topic/Evaluation_Design_Experiments
- Context/Background
source_repository: https://github.com/klappe-pm/cs249r_book
source_commit: de87c0103806d7bfb1c677dbb77a2b92fa00c298
source_path: taxonomy/taxonomy.yml
source_label: Cross-validation
taxonomy_id: mlsys.cross-validation
taxonomy_status: draft
taxonomy_version: 0.4-draft
---

# Cross Validation

Estimating performance by repeatedly training on some data partitions and evaluating on the held-out remainder.

## Browsing Home

[[02 Concepts/Lifecycle/Model Evaluation & Testing/Evaluation Design & Experiments Subject|Evaluation Design & Experiments]] → [[02 Concepts/Lifecycle/Model Evaluation & Testing/Model Evaluation & Testing Index|Model Evaluation & Testing]]

This is a background concept on which ML systems reasoning depends; that classification does not make it optional.

## Book Passages

These are explicitly recorded related passages from the upstream draft alignment; they do not certify complete coverage.

No explicit passage alignment is recorded for this concept. Subject reading pointers are available in its browsing home.

## Conditional Relationships

These are the taxonomy's draft editorial relationships. Read each relationship with its condition; an outgoing link is not a prerequisite claim.

- Reduces variance of estimates under [[02 Concepts/Lifecycle/Model Evaluation & Testing/Statistical Uncertainty|Statistical Uncertainty]]. **Condition:** Holds for i.i.d. data; temporal or grouped data need splits that respect dependence.

- Is a rotating [[02 Concepts/Lifecycle/Model Evaluation & Testing/Evaluation Split|Evaluation Split]]. **Condition:** Applies when data is too scarce for a single fixed validation split and examples are exchangeable.

## Source

[Canonical Taxonomy](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/taxonomy.yml) · [Passage Alignment](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/mlsysbook-alignment.yml)

Taxonomy definitions and relationship wording: CC BY 4.0, with attribution to the Machine Learning Systems curriculum by Vijay Janapa Reddi and contributors. The textbook retains its separate license.
