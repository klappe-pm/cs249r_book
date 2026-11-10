---
title: Cost Sensitive Decision
type: concept
tags:
- Type/Concept
- Group/Foundations
- Topic/Objectives_Proxies_Decision_Policies
source_repository: https://github.com/klappe-pm/cs249r_book
source_commit: de87c0103806d7bfb1c677dbb77a2b92fa00c298
source_path: taxonomy/taxonomy.yml
source_label: Cost-sensitive decision
taxonomy_id: mlsys.cost-sensitive-decision
taxonomy_status: draft
taxonomy_version: 0.4-draft
---

# Cost Sensitive Decision

Choosing actions or thresholds to minimize expected cost when different error types carry unequal consequences.

## Browsing Home

[[02 Concepts/Foundations/Workloads & Requirements/Objectives, Proxies & Decision Policies Subject|Objectives, Proxies & Decision Policies]] → [[02 Concepts/Foundations/Workloads & Requirements/Workloads & Requirements Index|Workloads & Requirements]]

## Book Passages

These are explicitly recorded related passages from the upstream draft alignment; they do not certify complete coverage.

No explicit passage alignment is recorded for this concept. Subject reading pointers are available in its browsing home.

## Conditional Relationships

These are the taxonomy's draft editorial relationships. Read each relationship with its condition; an outgoing link is not a prerequisite claim.

- Sets thresholds in [[02 Concepts/Foundations/Workloads & Requirements/Decision Policy|Decision Policy]]. **Condition:** Error costs and class priors can be stated for the deployment context.

- Requires calibrated probabilities from [[02 Concepts/Lifecycle/Model Evaluation & Testing/Probability Calibration|Probability Calibration]]. **Condition:** Expected-cost thresholds are computed from predicted probabilities, which must match observed frequencies on the deployment distribution.

- Sets the abstention threshold in [[02 Concepts/Lifecycle/Model Evaluation & Testing/Selective Prediction|Selective Prediction]]. **Condition:** Deferring to a human or fallback has a known cost that can be compared with the expected cost of each error type.

- Re-weights decisions by the real cost of each error type, correcting a misaligned [[02 Concepts/Foundations/Workloads & Requirements/Proxy Objective|Proxy Objective]]. **Condition:** Error costs must be stated per outcome, not inferred from the proxy.

## Source

[Canonical Taxonomy](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/taxonomy.yml) · [Passage Alignment](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/mlsysbook-alignment.yml)

Taxonomy definitions and relationship wording: CC BY 4.0, with attribution to the Machine Learning Systems curriculum by Vijay Janapa Reddi and contributors. The textbook retains its separate license.
