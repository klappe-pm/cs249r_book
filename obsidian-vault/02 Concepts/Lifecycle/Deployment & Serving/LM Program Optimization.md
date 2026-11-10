---
title: LM Program Optimization
type: concept
tags:
- Type/Concept
- Group/Lifecycle
- Topic/Compound_AI_Systems_Model_Routing
source_repository: https://github.com/klappe-pm/cs249r_book
source_commit: de87c0103806d7bfb1c677dbb77a2b92fa00c298
source_path: taxonomy/taxonomy.yml
source_label: LM program optimization
taxonomy_id: mlsys.lm-program-optimization
taxonomy_status: draft
taxonomy_version: 0.4-draft
---

# LM Program Optimization

Automatically tuning the prompts, demonstrations, or weights of each model call in a declared pipeline against an end-to-end metric rather than per call.

## Browsing Home

[[02 Concepts/Lifecycle/Deployment & Serving/Compound AI Systems & Model Routing Subject|Compound AI Systems & Model Routing]] → [[02 Concepts/Lifecycle/Deployment & Serving/Deployment & Serving Index|Deployment & Serving]]

## Book Passages

These are explicitly recorded related passages from the upstream draft alignment; they do not certify complete coverage.

No explicit passage alignment is recorded for this concept. Subject reading pointers are available in its browsing home.

## Conditional Relationships

These are the taxonomy's draft editorial relationships. Read each relationship with its condition; an outgoing link is not a prerequisite claim.

- Tunes the prompts and weights of [[02 Concepts/Lifecycle/Deployment & Serving/Compound AI System|Compound AI System]]. **Condition:** Requires a declared program structure and an end-to-end metric evaluable on a training set of inputs.

- Optimizes against an end-to-end [[02 Concepts/Lifecycle/Model Evaluation & Testing/Evaluation Metrics|Evaluation Metrics]]. **Condition:** Holds because the optimizer can only improve what the declared metric scores.

- Automates [[02 Concepts/Lifecycle/Training & Adaptation/Prompt Engineering|Prompt Engineering]]. **Condition:** An end-to-end metric and training examples are available.

## Search Terms

Upstream search terms may be related terms rather than exact synonyms: prompt optimization.

## Source

[Canonical Taxonomy](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/taxonomy.yml) · [Passage Alignment](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/mlsysbook-alignment.yml)

Taxonomy definitions and relationship wording: CC BY 4.0, with attribution to the Machine Learning Systems curriculum by Vijay Janapa Reddi and contributors. The textbook retains its separate license.
