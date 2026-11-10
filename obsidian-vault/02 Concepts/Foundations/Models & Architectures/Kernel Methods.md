---
title: Kernel Methods
type: concept
tags:
- Type/Concept
- Group/Foundations
- Topic/Model_Families
- Context/Background
source_repository: https://github.com/klappe-pm/cs249r_book
source_commit: de87c0103806d7bfb1c677dbb77a2b92fa00c298
source_path: taxonomy/taxonomy.yml
source_label: Kernel methods
taxonomy_id: mlsys.kernel-method
taxonomy_status: draft
taxonomy_version: 0.4-draft
---

# Kernel Methods

Models that score an input by a kernel similarity to retained training examples or to an explicit feature approximation, so storage and evaluation cost grow with the number of retained examples unless the kernel is approximated.

## Browsing Home

[[02 Concepts/Foundations/Models & Architectures/Model Families Subject|Model Families]] → [[02 Concepts/Foundations/Models & Architectures/Models & Architectures Index|Models & Architectures]]

This is a background concept on which ML systems reasoning depends; that classification does not make it optional.

## Book Passages

These are explicitly recorded related passages from the upstream draft alignment; they do not certify complete coverage.

No explicit passage alignment is recorded for this concept. Subject reading pointers are available in its browsing home.

## Conditional Relationships

These are the taxonomy's draft editorial relationships. Read each relationship with its condition; an outgoing link is not a prerequisite claim.

- Determines the size of [[02 Concepts/Foundations/Models & Architectures/Model Artifact|Model Artifact]]. **Condition:** Support vectors or an explicit approximation affect the stored state and evaluation cost.

- Has a quadratic training [[02 Concepts/Foundations/Workloads & Requirements/Memory Footprint|Memory Footprint]]. **Condition:** Exact training forms or stores an n-by-n kernel matrix, so memory grows with the square of the training set size unless approximated.

- Encodes its inductive bias through the choice of kernel in [[02 Concepts/Foundations/Models & Architectures/Inductive Bias|Inductive Bias]]. **Condition:** The kernel function fixes which similarity structure the model can exploit.

## Search Terms

Upstream search terms may be related terms rather than exact synonyms: support vector machine; SVM.

## Source

[Canonical Taxonomy](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/taxonomy.yml) · [Passage Alignment](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/mlsysbook-alignment.yml)

Taxonomy definitions and relationship wording: CC BY 4.0, with attribution to the Machine Learning Systems curriculum by Vijay Janapa Reddi and contributors. The textbook retains its separate license.
