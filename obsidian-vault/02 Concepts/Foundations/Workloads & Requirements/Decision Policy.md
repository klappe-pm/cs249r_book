---
title: Decision Policy
type: concept
tags:
- Type/Concept
- Group/Foundations
- Topic/Objectives_Proxies_Decision_Policies
source_repository: https://github.com/klappe-pm/cs249r_book
source_commit: de87c0103806d7bfb1c677dbb77a2b92fa00c298
source_path: taxonomy/taxonomy.yml
source_label: Decision policy
taxonomy_id: mlsys.decision-policy
taxonomy_status: draft
taxonomy_version: 0.4-draft
---

# Decision Policy

The rule that converts model outputs and system state into actions, thresholds, abstentions, or escalation.

## Browsing Home

[[02 Concepts/Foundations/Workloads & Requirements/Objectives, Proxies & Decision Policies Subject|Objectives, Proxies & Decision Policies]] → [[02 Concepts/Foundations/Workloads & Requirements/Workloads & Requirements Index|Workloads & Requirements]]

## Book Passages

These are explicitly recorded related passages from the upstream draft alignment; they do not certify complete coverage.

No explicit passage alignment is recorded for this concept. Subject reading pointers are available in its browsing home.

## Conditional Relationships

These are the taxonomy's draft editorial relationships. Read each relationship with its condition; an outgoing link is not a prerequisite claim.

- Uses outputs assessed by [[02 Concepts/Lifecycle/Model Evaluation & Testing/Probability Calibration|Probability Calibration]]. **Condition:** A probability threshold needs task costs and deployment-distribution evidence as well as calibration.

- Sets its operating threshold from the curve of [[02 Concepts/Lifecycle/Model Evaluation & Testing/Precision, Recall, and ROC Analysis|Precision, Recall, and ROC Analysis]]. **Condition:** When the policy thresholds a score and the two error rates must be traded explicitly.

## Source

[Canonical Taxonomy](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/taxonomy.yml) · [Passage Alignment](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/mlsysbook-alignment.yml)

Taxonomy definitions and relationship wording: CC BY 4.0, with attribution to the Machine Learning Systems curriculum by Vijay Janapa Reddi and contributors. The textbook retains its separate license.
