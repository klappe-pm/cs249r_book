---
title: Multi Task Learning
type: concept
tags:
- Type/Concept
- Group/Lifecycle
- Topic/Learning_Paradigms
source_repository: https://github.com/klappe-pm/cs249r_book
source_commit: de87c0103806d7bfb1c677dbb77a2b92fa00c298
source_path: taxonomy/taxonomy.yml
source_label: Multi-task learning
taxonomy_id: mlsys.multi-task-learning
taxonomy_status: draft
taxonomy_version: 0.4-draft
---

# Multi Task Learning

Jointly learning several tasks through shared parameters, often a shared backbone with task-specific heads, so their training signals can help or interfere with one another.

## Browsing Home

[[02 Concepts/Lifecycle/Training & Adaptation/Learning Paradigms Subject|Learning Paradigms]] → [[02 Concepts/Lifecycle/Training & Adaptation/Training & Adaptation Index|Training & Adaptation]]

## Book Passages

These are explicitly recorded related passages from the upstream draft alignment; they do not certify complete coverage.

No explicit passage alignment is recorded for this concept. Subject reading pointers are available in its browsing home.

## Conditional Relationships

These are the taxonomy's draft editorial relationships. Read each relationship with its condition; an outgoing link is not a prerequisite claim.

- Consolidates several tasks into one shared-backbone model instead of hosting separate models in [[02 Concepts/Lifecycle/Deployment & Serving/Multi Model Serving|Multi Model Serving]]. **Condition:** When tasks share inputs and enough representation that one backbone serves them without unacceptable quality loss.

- Learns tasks jointly rather than carrying learning across as in [[02 Concepts/Lifecycle/Training & Adaptation/Transfer Learning|Transfer Learning]]. **Condition:** When several related tasks are available at training time.

## Search Terms

Upstream search terms may be related terms rather than exact synonyms: multitask learning; shared-backbone multi-task model.

## Source

[Canonical Taxonomy](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/taxonomy.yml) · [Passage Alignment](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/mlsysbook-alignment.yml)

Taxonomy definitions and relationship wording: CC BY 4.0, with attribution to the Machine Learning Systems curriculum by Vijay Janapa Reddi and contributors. The textbook retains its separate license.
