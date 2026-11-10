---
title: Regularization
type: concept
tags:
- Type/Concept
- Group/Lifecycle
- Topic/Optimization_Training_Dynamics
- Context/Background
source_repository: https://github.com/klappe-pm/cs249r_book
source_commit: de87c0103806d7bfb1c677dbb77a2b92fa00c298
source_path: taxonomy/taxonomy.yml
source_label: Regularization
taxonomy_id: mlsys.regularization
taxonomy_status: draft
taxonomy_version: 0.4-draft
---

# Regularization

Constraints or training procedures used to control sensitivity and generalization behavior.

## Browsing Home

[[02 Concepts/Lifecycle/Training & Adaptation/Optimization & Training Dynamics Subject|Optimization & Training Dynamics]] → [[02 Concepts/Lifecycle/Training & Adaptation/Training & Adaptation Index|Training & Adaptation]]

This is a background concept on which ML systems reasoning depends; that classification does not make it optional.

## Book Passages

These are explicitly recorded related passages from the upstream draft alignment; they do not certify complete coverage.

No explicit passage alignment is recorded for this concept. Subject reading pointers are available in its browsing home.

## Conditional Relationships

These are the taxonomy's draft editorial relationships. Read each relationship with its condition; an outgoing link is not a prerequisite claim.

- Shapes [[02 Concepts/Lifecycle/Model Evaluation & Testing/Generalization|Generalization]]. **Condition:** Effects depend on the data, model, objective, and optimization regime.

- Reduces the overfitting exploited by [[02 Concepts/Qualities/Security & Privacy/Membership Inference|Membership Inference]]. **Condition:** Reduces but does not bound leakage; formal bounds need differential privacy.

- Mitigates [[02 Concepts/Lifecycle/Training & Adaptation/Overfitting|Overfitting]]. **Condition:** When the penalty or procedure limits the model's ability to fit training-set noise.

- Penalizes drift from the base parameters or outputs, limiting [[02 Concepts/Lifecycle/Training & Adaptation/Catastrophic Forgetting|Catastrophic Forgetting]]. **Condition:** The penalty, such as a KL term to the base model, must be weighted against the target-task loss.

## Source

[Canonical Taxonomy](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/taxonomy.yml) · [Passage Alignment](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/mlsysbook-alignment.yml)

Taxonomy definitions and relationship wording: CC BY 4.0, with attribution to the Machine Learning Systems curriculum by Vijay Janapa Reddi and contributors. The textbook retains its separate license.
