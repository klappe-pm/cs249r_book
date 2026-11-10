---
title: Online Experimentation
type: concept
tags:
- Type/Concept
- Group/Lifecycle
- Topic/Evaluation_Design_Experiments
source_repository: https://github.com/klappe-pm/cs249r_book
source_commit: de87c0103806d7bfb1c677dbb77a2b92fa00c298
source_path: taxonomy/taxonomy.yml
source_label: Online experimentation
taxonomy_id: mlsys.online-experiment
taxonomy_status: draft
taxonomy_version: 0.4-draft
---

# Online Experimentation

A controlled intervention used to estimate effects on deployed-system outcomes.

## Browsing Home

[[02 Concepts/Lifecycle/Model Evaluation & Testing/Evaluation Design & Experiments Subject|Evaluation Design & Experiments]] → [[02 Concepts/Lifecycle/Model Evaluation & Testing/Model Evaluation & Testing Index|Model Evaluation & Testing]]

## Book Passages

These are explicitly recorded related passages from the upstream draft alignment; they do not certify complete coverage.

No explicit passage alignment is recorded for this concept. Subject reading pointers are available in its browsing home.

## Conditional Relationships

These are the taxonomy's draft editorial relationships. Read each relationship with its condition; an outgoing link is not a prerequisite claim.

- Estimates causal effects on [[02 Concepts/Lifecycle/Model Evaluation & Testing/Evaluation Metrics|Evaluation Metrics]]. **Condition:** Causal interpretation depends on assignment, interference, observation, and stopping assumptions.

- Controls error rates across many decision metrics with [[02 Concepts/Lifecycle/Model Evaluation & Testing/Multiple Comparisons Correction|Multiple Comparisons Correction]]. **Condition:** When an experiment's launch decision rests on several metrics or segments.

- Tests on live traffic a winner chosen under [[02 Concepts/Lifecycle/Model Evaluation & Testing/Model Selection Optimism|Model Selection Optimism]]. **Condition:** When a model picked by offline comparison is exposed to a controlled share of real users.

## Search Terms

Upstream search terms may be related terms rather than exact synonyms: A/B testing; A/B test; controlled online experiment.

## Source

[Canonical Taxonomy](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/taxonomy.yml) · [Passage Alignment](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/mlsysbook-alignment.yml)

Taxonomy definitions and relationship wording: CC BY 4.0, with attribution to the Machine Learning Systems curriculum by Vijay Janapa Reddi and contributors. The textbook retains its separate license.
