---
title: Pass@k
type: concept
tags:
- Type/Concept
- Group/Lifecycle
- Topic/Evaluating_Generative_Agentic_Systems
source_repository: https://github.com/klappe-pm/cs249r_book
source_commit: de87c0103806d7bfb1c677dbb77a2b92fa00c298
source_path: taxonomy/taxonomy.yml
source_label: pass@k
taxonomy_id: mlsys.pass-at-k
taxonomy_status: draft
taxonomy_version: 0.4-draft
---

# Pass@k

The probability that at least one of k sampled outputs satisfies a correctness check.

## Browsing Home

[[02 Concepts/Lifecycle/Model Evaluation & Testing/Evaluating Generative & Agentic Systems Subject|Evaluating Generative & Agentic Systems]] → [[02 Concepts/Lifecycle/Model Evaluation & Testing/Model Evaluation & Testing Index|Model Evaluation & Testing]]

## Book Passages

These are explicitly recorded related passages from the upstream draft alignment; they do not certify complete coverage.

- [[01 Books/Volume III - Agentic Systems/01 The Model/03 Test-Time Compute/V3-03.04 Selecting from a Candidate Pool#^sec-vol3-test-time-compute-candidate-diversity|V3-03.04 Selecting from a Candidate Pool]] — Candidate selection. [Exact Source Passage](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/books/vol3/03_test_time_compute/03_test_time_compute.qmd#L376).

- [[01 Books/Volume III - Agentic Systems/04 The Agent Runtime/13 Agent Evaluation/V3-13.06 Statistical Evaluation Rigor#^sec-vol3-evaluation-pass-k|V3-13.06 Statistical Evaluation Rigor]] — Repeated-run consistency. [Exact Source Passage](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/books/vol3/13_evaluation/13_evaluation.qmd#L799).

## Conditional Relationships

These are the taxonomy's draft editorial relationships. Read each relationship with its condition; an outgoing link is not a prerequisite claim.

- Upper-bounds accuracy of [[02 Concepts/Lifecycle/Deployment & Serving/Best of N Sampling|Best of N Sampling]]. **Condition:** Best-of-n reaches pass@n only with a perfect selector; real verifiers lose part of the gap.

- Is a kind of [[02 Concepts/Lifecycle/Model Evaluation & Testing/Evaluation Metrics|Evaluation Metrics]]. **Condition:** Applies when outputs have an automatic correctness check, as in code generation.

- Counts a sample as correct according to a [[02 Concepts/Lifecycle/Model Evaluation & Testing/Test Oracle|Test Oracle]]. **Condition:** When the check is unit tests or a programmatic grader; the metric inherits the oracle's false positives.

## Source

[Canonical Taxonomy](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/taxonomy.yml) · [Passage Alignment](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/mlsysbook-alignment.yml)

Taxonomy definitions and relationship wording: CC BY 4.0, with attribution to the Machine Learning Systems curriculum by Vijay Janapa Reddi and contributors. The textbook retains its separate license.
