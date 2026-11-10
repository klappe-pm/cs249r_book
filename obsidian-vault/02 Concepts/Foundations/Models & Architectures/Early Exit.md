---
title: Early Exit
type: concept
tags:
- Type/Concept
- Group/Foundations
- Topic/Sparse_Conditional_Computation
source_repository: https://github.com/klappe-pm/cs249r_book
source_commit: de87c0103806d7bfb1c677dbb77a2b92fa00c298
source_path: taxonomy/taxonomy.yml
source_label: Early exit
taxonomy_id: mlsys.early-exit
taxonomy_status: draft
taxonomy_version: 0.4-draft
---

# Early Exit

Terminating inference at an intermediate layer once a confidence criterion is met, so per-input compute varies with input difficulty.

## Browsing Home

[[02 Concepts/Foundations/Models & Architectures/Sparse & Conditional Computation Subject|Sparse & Conditional Computation]] → [[02 Concepts/Foundations/Models & Architectures/Models & Architectures Index|Models & Architectures]]

## Book Passages

These are explicitly recorded related passages from the upstream draft alignment; they do not certify complete coverage.

No explicit passage alignment is recorded for this concept. Subject reading pointers are available in its browsing home.

## Conditional Relationships

These are the taxonomy's draft editorial relationships. Read each relationship with its condition; an outgoing link is not a prerequisite claim.

- Reduces average, and makes input-dependent, [[02 Concepts/Qualities/Performance, Efficiency & Benchmarking/Execution Time|Execution Time]]. **Condition:** Exit criteria differ across inputs, so latency varies with input difficulty.

- Relies on confidence quality assessed by [[02 Concepts/Lifecycle/Model Evaluation & Testing/Probability Calibration|Probability Calibration]]. **Condition:** Exit decisions threshold an intermediate confidence; overconfident exits return wrong answers early.

- Reduces average [[02 Concepts/Qualities/Sustainability & Cost/Energy per Inference|Energy per Inference]]. **Condition:** Many inputs are easy enough to exit at an early classifier and the exit overhead is small.

## Search Terms

Upstream search terms may be related terms rather than exact synonyms: adaptive computation.

## Source

[Canonical Taxonomy](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/taxonomy.yml) · [Passage Alignment](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/mlsysbook-alignment.yml)

Taxonomy definitions and relationship wording: CC BY 4.0, with attribution to the Machine Learning Systems curriculum by Vijay Janapa Reddi and contributors. The textbook retains its separate license.
