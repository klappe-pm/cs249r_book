---
title: Evaluation Harness
type: concept
tags:
- Type/Concept
- Group/Lifecycle
- Topic/Evaluation_Design_Experiments
source_repository: https://github.com/klappe-pm/cs249r_book
source_commit: de87c0103806d7bfb1c677dbb77a2b92fa00c298
source_path: taxonomy/taxonomy.yml
source_label: Evaluation harness
taxonomy_id: mlsys.evaluation-harness
taxonomy_status: draft
taxonomy_version: 0.4-draft
---

# Evaluation Harness

A system running versioned benchmark suites against model checkpoints with fixed prompts, decoding settings, and scorers, sharding and caching work so results stay reproducible and comparable.

## Browsing Home

[[02 Concepts/Lifecycle/Model Evaluation & Testing/Evaluation Design & Experiments Subject|Evaluation Design & Experiments]] → [[02 Concepts/Lifecycle/Model Evaluation & Testing/Model Evaluation & Testing Index|Model Evaluation & Testing]]

## Book Passages

These are explicitly recorded related passages from the upstream draft alignment; they do not certify complete coverage.

No explicit passage alignment is recorded for this concept. Subject reading pointers are available in its browsing home.

## Conditional Relationships

These are the taxonomy's draft editorial relationships. Read each relationship with its condition; an outgoing link is not a prerequisite claim.

- Implements [[02 Concepts/Qualities/Performance, Efficiency & Benchmarking/Benchmark Protocol|Benchmark Protocol]]. **Condition:** Comparability holds only when prompt templates, decoding settings, and scorer versions are pinned with the results.

- Records results into [[02 Concepts/Lifecycle/Training & Adaptation/Experiment Tracking|Experiment Tracking]]. **Condition:** Holds when each run logs checkpoint, suite version, and configuration alongside scores.

- Can score open-ended outputs with [[02 Concepts/Lifecycle/Model Evaluation & Testing/Model Based Grading|Model Based Grading]]. **Condition:** Applies when tasks lack exact-match references.

- Reruns a fixed base-capability suite on each checkpoint, revealing [[02 Concepts/Lifecycle/Training & Adaptation/Catastrophic Forgetting|Catastrophic Forgetting]]. **Condition:** The suite and prompts are held fixed across checkpoints.

## Search Terms

Upstream search terms may be related terms rather than exact synonyms: eval harness; hidden tests; grader isolation.

## Source

[Canonical Taxonomy](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/taxonomy.yml) · [Passage Alignment](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/mlsysbook-alignment.yml)

Taxonomy definitions and relationship wording: CC BY 4.0, with attribution to the Machine Learning Systems curriculum by Vijay Janapa Reddi and contributors. The textbook retains its separate license.
