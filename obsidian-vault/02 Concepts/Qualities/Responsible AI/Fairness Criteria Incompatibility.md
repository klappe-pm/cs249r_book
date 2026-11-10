---
title: Fairness Criteria Incompatibility
type: concept
tags:
- Type/Concept
- Group/Qualities
- Topic/Fairness_Bias
source_repository: https://github.com/klappe-pm/cs249r_book
source_commit: de87c0103806d7bfb1c677dbb77a2b92fa00c298
source_path: taxonomy/taxonomy.yml
source_label: Fairness criteria incompatibility
taxonomy_id: mlsys.fairness-incompatibility
taxonomy_status: draft
taxonomy_version: 0.4-draft
---

# Fairness Criteria Incompatibility

The result that calibration and error-rate parity across groups cannot generally hold together when base rates differ, forcing an explicit choice among criteria.

## Browsing Home

[[02 Concepts/Qualities/Responsible AI/Fairness & Bias Subject|Fairness & Bias]] → [[02 Concepts/Qualities/Responsible AI/Responsible AI Index|Responsible AI]]

## Book Passages

These are explicitly recorded related passages from the upstream draft alignment; they do not certify complete coverage.

- [[01 Books/Volume I - Foundations/04 Deployment/15 Responsible Engineering/V1-15.04 Responsible Engineering Across the Lifecycle#^sec-responsible-engineering-testing-across-populations-9f20|V1-15.04 Responsible Engineering Across the Lifecycle]] — Subgroup fairness. [Exact Source Passage](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/books/vol1/15_responsible_engr/15_responsible_engr.qmd#L585).

- [[01 Books/Volume II - Scaling/04 The Responsible Fleet/16 Responsible AI/V2-16.06 Fairness and Bias Mitigation#^sec-responsible-ai-fairness-machine-learning-2ba4|V2-16.06 Fairness and Bias Mitigation]] — Fairness criterion. [Exact Source Passage](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/books/vol2/16_responsible_ai/16_responsible_ai.qmd#L372).

## Conditional Relationships

These are the taxonomy's draft editorial relationships. Read each relationship with its condition; an outgoing link is not a prerequisite claim.

- Forces a choice among [[02 Concepts/Qualities/Responsible AI/Group Fairness Metrics|Group Fairness Metrics]]. **Condition:** Holds when base rates differ across groups and the predictor is imperfect.

- Limits per-group [[02 Concepts/Lifecycle/Model Evaluation & Testing/Probability Calibration|Probability Calibration]]. **Condition:** When base rates differ and error-rate parity is also required.

- Limits which criteria can jointly hold in [[02 Concepts/Qualities/Responsible AI/Fairness Criteria|Fairness Criteria]]. **Condition:** When base rates differ across groups and the predictor is imperfect.

## Source

[Canonical Taxonomy](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/taxonomy.yml) · [Passage Alignment](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/mlsysbook-alignment.yml)

Taxonomy definitions and relationship wording: CC BY 4.0, with attribution to the Machine Learning Systems curriculum by Vijay Janapa Reddi and contributors. The textbook retains its separate license.
