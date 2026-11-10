---
title: Model Cascade
type: concept
tags:
- Type/Concept
- Group/Lifecycle
- Topic/Compound_AI_Systems_Model_Routing
source_repository: https://github.com/klappe-pm/cs249r_book
source_commit: de87c0103806d7bfb1c677dbb77a2b92fa00c298
source_path: taxonomy/taxonomy.yml
source_label: Model cascade
taxonomy_id: mlsys.model-cascade
taxonomy_status: draft
taxonomy_version: 0.4-draft
---

# Model Cascade

Sending a request to cheaper models first and escalating to more capable models only when a confidence or quality criterion is not met.

## Browsing Home

[[02 Concepts/Lifecycle/Deployment & Serving/Compound AI Systems & Model Routing Subject|Compound AI Systems & Model Routing]] → [[02 Concepts/Lifecycle/Deployment & Serving/Deployment & Serving Index|Deployment & Serving]]

## Book Passages

These are explicitly recorded related passages from the upstream draft alignment; they do not certify complete coverage.

No explicit passage alignment is recorded for this concept. Subject reading pointers are available in its browsing home.

## Conditional Relationships

These are the taxonomy's draft editorial relationships. Read each relationship with its condition; an outgoing link is not a prerequisite claim.

- Can reduce [[02 Concepts/Qualities/Sustainability & Cost/Cost per Useful Outcome|Cost per Useful Outcome]]. **Condition:** Holds when most requests are resolved by cheap models and the escalation criterion is reliable.

- Relies on [[02 Concepts/Lifecycle/Model Evaluation & Testing/Selective Prediction|Selective Prediction]]. **Condition:** Each stage must abstain and defer when confidence is low; poorly calibrated scores misroute requests.

- Is an alternative to [[02 Concepts/Lifecycle/Deployment & Serving/Model Routing|Model Routing]]. **Condition:** Routing decides before calling a model; a cascade escalates after a cheap model's answer.

## Source

[Canonical Taxonomy](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/taxonomy.yml) · [Passage Alignment](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/mlsysbook-alignment.yml)

Taxonomy definitions and relationship wording: CC BY 4.0, with attribution to the Machine Learning Systems curriculum by Vijay Janapa Reddi and contributors. The textbook retains its separate license.
