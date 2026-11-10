---
title: Fairness Monitoring
type: concept
tags:
- Type/Concept
- Group/Qualities
- Topic/Fairness_Bias
source_repository: https://github.com/klappe-pm/cs249r_book
source_commit: de87c0103806d7bfb1c677dbb77a2b92fa00c298
source_path: taxonomy/taxonomy.yml
source_label: Fairness monitoring
taxonomy_id: mlsys.fairness-monitoring
taxonomy_status: draft
taxonomy_version: 0.4-draft
---

# Fairness Monitoring

Tracking group fairness metrics on production traffic over time, with the sampling, delayed-label, and protected-attribute availability problems that make subgroup estimates noisier than aggregate ones, so that disparities introduced by drift or retraining are caught before they accumulate.

## Browsing Home

[[02 Concepts/Qualities/Responsible AI/Fairness & Bias Subject|Fairness & Bias]] → [[02 Concepts/Qualities/Responsible AI/Responsible AI Index|Responsible AI]]

## Book Passages

These are explicitly recorded related passages from the upstream draft alignment; they do not certify complete coverage.

No explicit passage alignment is recorded for this concept. Subject reading pointers are available in its browsing home.

## Conditional Relationships

These are the taxonomy's draft editorial relationships. Read each relationship with its condition; an outgoing link is not a prerequisite claim.

- Computes on live traffic the [[02 Concepts/Qualities/Responsible AI/Group Fairness Metrics|Group Fairness Metrics]]. **Condition:** When protected attributes or accepted proxies are available at monitoring time.

- Is a kind of [[02 Concepts/Lifecycle/MLOps & Operations/Production Monitoring|Production Monitoring]]. **Condition:** When the monitored signal is a disparity across groups rather than an aggregate.

- Applies in production the per-group measurement of [[02 Concepts/Lifecycle/Model Evaluation & Testing/Sliced Evaluation|Sliced Evaluation]]. **Condition:** When slices are protected groups and the evaluation is continuous rather than a release gate.

- Supplements group metrics with subgroup tests from [[02 Concepts/Lifecycle/MLOps & Operations/Drift Detection|Drift Detection]]. **Condition:** When a subgroup's metric moves and the cause must be separated from model, label, or sampling changes.

## Search Terms

Upstream search terms may be related terms rather than exact synonyms: production fairness monitoring; subgroup performance monitoring; post-market bias monitoring.

## Source

[Canonical Taxonomy](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/taxonomy.yml) · [Passage Alignment](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/mlsysbook-alignment.yml)

Taxonomy definitions and relationship wording: CC BY 4.0, with attribution to the Machine Learning Systems curriculum by Vijay Janapa Reddi and contributors. The textbook retains its separate license.
