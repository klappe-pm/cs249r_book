---
title: Bias Mitigation
type: concept
tags:
- Type/Concept
- Group/Qualities
- Topic/Fairness_Bias
source_repository: https://github.com/klappe-pm/cs249r_book
source_commit: de87c0103806d7bfb1c677dbb77a2b92fa00c298
source_path: taxonomy/taxonomy.yml
source_label: Bias mitigation
taxonomy_id: mlsys.bias-mitigation
taxonomy_status: draft
taxonomy_version: 0.4-draft
---

# Bias Mitigation

Interventions on data (pre-processing), training objective (in-processing), or decisions (post-processing) that reduce measured disparities, usually at some cost in other metrics.

## Browsing Home

[[02 Concepts/Qualities/Responsible AI/Fairness & Bias Subject|Fairness & Bias]] → [[02 Concepts/Qualities/Responsible AI/Responsible AI Index|Responsible AI]]

## Book Passages

These are explicitly recorded related passages from the upstream draft alignment; they do not certify complete coverage.

No explicit passage alignment is recorded for this concept. Subject reading pointers are available in its browsing home.

## Conditional Relationships

These are the taxonomy's draft editorial relationships. Read each relationship with its condition; an outgoing link is not a prerequisite claim.

- Trades off against aggregate [[02 Concepts/Lifecycle/Model Evaluation & Testing/Evaluation Metrics|Evaluation Metrics]]. **Condition:** Reducing a disparity often lowers aggregate accuracy or shifts error to other groups or metrics.

- Implements [[02 Concepts/Qualities/Responsible AI/Fairness Criteria|Fairness Criteria]]. **Condition:** When the intervention targets a declared criterion and is re-evaluated on held-out data.

- Uses reweighting and resampling from [[02 Concepts/Lifecycle/Data Engineering/Data Selection|Data Selection]]. **Condition:** For pre-processing methods that change the training distribution across groups.

- Reduces the disparity from [[02 Concepts/Qualities/Responsible AI/Proxy Discrimination|Proxy Discrimination]]. **Condition:** When mitigation constrains outcomes rather than only dropping the attribute.

## Source

[Canonical Taxonomy](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/taxonomy.yml) · [Passage Alignment](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/mlsysbook-alignment.yml)

Taxonomy definitions and relationship wording: CC BY 4.0, with attribution to the Machine Learning Systems curriculum by Vijay Janapa Reddi and contributors. The textbook retains its separate license.
