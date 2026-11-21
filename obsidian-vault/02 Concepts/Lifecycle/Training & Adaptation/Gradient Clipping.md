---
title: Gradient Clipping
type: concept
tags:
- Type/Concept
- Group/Lifecycle
- Topic/Optimization_Training_Dynamics
- Context/Background
source_repository: https://github.com/klappe-pm/cs249r_book
source_commit: de87c0103806d7bfb1c677dbb77a2b92fa00c298
source_path: taxonomy/taxonomy.yml
source_label: Gradient clipping
taxonomy_id: mlsys.gradient-clipping
taxonomy_status: draft
taxonomy_version: 0.4-draft
---

# Gradient Clipping

Rescaling or truncating gradients whose norm exceeds a threshold so that a single large update cannot destabilize training.

## Browsing Home

[[02 Concepts/Lifecycle/Training & Adaptation/Optimization & Training Dynamics Subject|Optimization & Training Dynamics]] → [[02 Concepts/Lifecycle/Training & Adaptation/Training & Adaptation Index|Training & Adaptation]]

This is a background concept on which ML systems reasoning depends; that classification does not make it optional.

## Book Passages

These are explicitly recorded related passages from the upstream draft alignment; they do not certify complete coverage.

No explicit passage alignment is recorded for this concept. Subject reading pointers are available in its browsing home.

## Conditional Relationships

These are the taxonomy's draft editorial relationships. Read each relationship with its condition; an outgoing link is not a prerequisite claim.

- Suppresses [[02 Concepts/Lifecycle/Training & Adaptation/Training Instability|Training Instability]]. **Condition:** Instability arises from occasional very large gradients.

- Is applied in the update step of [[02 Concepts/Lifecycle/Training & Adaptation/Optimization Algorithm|Optimization Algorithm]]. **Condition:** Gradients are clipped before the optimizer step.

## Search Terms

Upstream search terms may be related terms rather than exact synonyms: gradient norm clipping.

## Source

[Canonical Taxonomy](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/taxonomy.yml) · [Passage Alignment](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/mlsysbook-alignment.yml)

Taxonomy definitions and relationship wording: CC BY 4.0, with attribution to the Machine Learning Systems curriculum by Vijay Janapa Reddi and contributors. The textbook retains its separate license.
