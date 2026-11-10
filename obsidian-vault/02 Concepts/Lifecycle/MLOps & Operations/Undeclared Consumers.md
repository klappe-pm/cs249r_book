---
title: Undeclared Consumers
type: concept
tags:
- Type/Concept
- Group/Lifecycle
- Topic/ML_Platforms_Teams_Technical_Debt
source_repository: https://github.com/klappe-pm/cs249r_book
source_commit: de87c0103806d7bfb1c677dbb77a2b92fa00c298
source_path: taxonomy/taxonomy.yml
source_label: Undeclared consumers
taxonomy_id: mlsys.undeclared-consumers
taxonomy_status: draft
taxonomy_version: 0.4-draft
---

# Undeclared Consumers

Systems that use a model's outputs without the model owner's knowledge, creating hidden coupling.

## Browsing Home

[[02 Concepts/Lifecycle/MLOps & Operations/ML Platforms, Teams & Technical Debt Subject|ML Platforms, Teams & Technical Debt]] → [[02 Concepts/Lifecycle/MLOps & Operations/MLOps & Operations Index|MLOps & Operations]]

## Book Passages

These are explicitly recorded related passages from the upstream draft alignment; they do not certify complete coverage.

No explicit passage alignment is recorded for this concept. Subject reading pointers are available in its browsing home.

## Conditional Relationships

These are the taxonomy's draft editorial relationships. Read each relationship with its condition; an outgoing link is not a prerequisite claim.

- Can create hidden [[02 Concepts/Lifecycle/MLOps & Operations/Deployment Feedback Loop|Deployment Feedback Loop]]. **Condition:** Holds when unknown consumers act on model outputs in ways that change future training data.

- Can block or break [[02 Concepts/Lifecycle/MLOps & Operations/Model Deprecation|Model Deprecation]]. **Condition:** Holds when consumers cannot be identified and migrated before the model is removed.

- Add hidden coupling to [[02 Concepts/Lifecycle/MLOps & Operations/ML Technical Debt|ML Technical Debt]]. **Condition:** Holds whenever model outputs are consumed without access control or registration.

## Source

[Canonical Taxonomy](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/taxonomy.yml) · [Passage Alignment](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/mlsysbook-alignment.yml)

Taxonomy definitions and relationship wording: CC BY 4.0, with attribution to the Machine Learning Systems curriculum by Vijay Janapa Reddi and contributors. The textbook retains its separate license.
