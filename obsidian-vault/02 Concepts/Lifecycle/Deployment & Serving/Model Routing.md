---
title: Model Routing
type: concept
tags:
- Type/Concept
- Group/Lifecycle
- Topic/Compound_AI_Systems_Model_Routing
source_repository: https://github.com/klappe-pm/cs249r_book
source_commit: de87c0103806d7bfb1c677dbb77a2b92fa00c298
source_path: taxonomy/taxonomy.yml
source_label: Model routing
taxonomy_id: mlsys.model-routing
taxonomy_status: draft
taxonomy_version: 0.4-draft
---

# Model Routing

Choosing which model serves each request from request features, predicted quality, and cost.

## Browsing Home

[[02 Concepts/Lifecycle/Deployment & Serving/Compound AI Systems & Model Routing Subject|Compound AI Systems & Model Routing]] → [[02 Concepts/Lifecycle/Deployment & Serving/Deployment & Serving Index|Deployment & Serving]]

## Book Passages

These are explicitly recorded related passages from the upstream draft alignment; they do not certify complete coverage.

No explicit passage alignment is recorded for this concept. Subject reading pointers are available in its browsing home.

## Conditional Relationships

These are the taxonomy's draft editorial relationships. Read each relationship with its condition; an outgoing link is not a prerequisite claim.

- Depends on [[02 Concepts/Lifecycle/Model Evaluation & Testing/Probability Calibration|Probability Calibration]]. **Condition:** When routers or cascade gates escalate on predicted quality or confidence, which must be calibrated to the request distribution.

- Lowers the average [[02 Concepts/Qualities/Sustainability & Cost/Cost per Token|Cost per Token]]. **Condition:** When a router sends requests a cheaper model can handle to that model while meeting the quality target.

## Source

[Canonical Taxonomy](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/taxonomy.yml) · [Passage Alignment](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/mlsysbook-alignment.yml)

Taxonomy definitions and relationship wording: CC BY 4.0, with attribution to the Machine Learning Systems curriculum by Vijay Janapa Reddi and contributors. The textbook retains its separate license.
