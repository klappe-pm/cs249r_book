---
title: Pretraining
type: concept
tags:
- Type/Concept
- Group/Lifecycle
- Topic/Learning_Paradigms
source_repository: https://github.com/klappe-pm/cs249r_book
source_commit: de87c0103806d7bfb1c677dbb77a2b92fa00c298
source_path: taxonomy/taxonomy.yml
source_label: Pretraining
taxonomy_id: mlsys.pretraining
taxonomy_status: draft
taxonomy_version: 0.4-draft
---

# Pretraining

Training a model from scratch on a large, broad corpus with a self-supervised objective to produce a general base model for later adaptation.

## Browsing Home

[[02 Concepts/Lifecycle/Training & Adaptation/Learning Paradigms Subject|Learning Paradigms]] → [[02 Concepts/Lifecycle/Training & Adaptation/Training & Adaptation Index|Training & Adaptation]]

## Book Passages

These are explicitly recorded related passages from the upstream draft alignment; they do not certify complete coverage.

No explicit passage alignment is recorded for this concept. Subject reading pointers are available in its browsing home.

## Conditional Relationships

These are the taxonomy's draft editorial relationships. Read each relationship with its condition; an outgoing link is not a prerequisite claim.

- Optimizes an objective from [[02 Concepts/Lifecycle/Training & Adaptation/Self Supervised Learning|Self Supervised Learning]]. **Condition:** Unlabeled corpora supply the training targets.

- Supplies base models for [[02 Concepts/Lifecycle/Training & Adaptation/Transfer Learning|Transfer Learning]]. **Condition:** Downstream tasks share structure with the pretraining corpus.

- Draws its corpus from [[02 Concepts/Lifecycle/Data Engineering/Data Mixture|Data Mixture]]. **Condition:** Corpora combine multiple domains or sources.

- Commonly optimizes [[02 Concepts/Lifecycle/Training & Adaptation/Causal Language Modeling|Causal Language Modeling]]. **Condition:** Decoder-only language-model pretraining.

- Gives rise to [[02 Concepts/Lifecycle/Training & Adaptation/In Context Learning|In Context Learning]]. **Condition:** Sufficient model and data scale.

- Yields the base weights of [[02 Concepts/Foundations/Models & Architectures/Large Language Model|Large Language Model]]. **Condition:** Training uses broad corpora and a self-supervised language-modeling objective.

- Chooses model size and token count with [[02 Concepts/Foundations/Quantitative System Models/Compute Optimal Allocation|Compute Optimal Allocation]]. **Condition:** When a fixed training compute budget is allocated before the run and the fitted law covers the target scale.

## Search Terms

Upstream search terms may be related terms rather than exact synonyms: base-model pretraining; pretraining run.

## Source

[Canonical Taxonomy](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/taxonomy.yml) · [Passage Alignment](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/mlsysbook-alignment.yml)

Taxonomy definitions and relationship wording: CC BY 4.0, with attribution to the Machine Learning Systems curriculum by Vijay Janapa Reddi and contributors. The textbook retains its separate license.
