---
title: Self Supervised Learning
type: concept
tags:
- Type/Concept
- Group/Lifecycle
- Topic/Learning_Paradigms
- Context/Background
source_repository: https://github.com/klappe-pm/cs249r_book
source_commit: de87c0103806d7bfb1c677dbb77a2b92fa00c298
source_path: taxonomy/taxonomy.yml
source_label: Self-supervised learning
taxonomy_id: mlsys.self-supervised-learning
taxonomy_status: draft
taxonomy_version: 0.4-draft
---

# Self Supervised Learning

Learning from targets constructed from the observed data itself.

## Browsing Home

[[02 Concepts/Lifecycle/Training & Adaptation/Learning Paradigms Subject|Learning Paradigms]] → [[02 Concepts/Lifecycle/Training & Adaptation/Training & Adaptation Index|Training & Adaptation]]

This is a background concept on which ML systems reasoning depends; that classification does not make it optional.

## Book Passages

These are explicitly recorded related passages from the upstream draft alignment; they do not certify complete coverage.

No explicit passage alignment is recorded for this concept. Subject reading pointers are available in its browsing home.

## Conditional Relationships

These are the taxonomy's draft editorial relationships. Read each relationship with its condition; an outgoing link is not a prerequisite claim.

- Constructs targets for its own [[02 Concepts/Lifecycle/Training & Adaptation/Training Loss|Training Loss]]. **Condition:** Targets are derived from the data under a specified objective and corruption or prediction scheme.

- Pretrains representations for [[02 Concepts/Lifecycle/Training & Adaptation/Transfer Learning|Transfer Learning]]. **Condition:** Holds when the pretraining data covers the target domain.

- Produces [[02 Concepts/Foundations/Models & Architectures/Embeddings|Embeddings]]. **Condition:** Applies to contrastive and masked-prediction objectives.

- Often trains through [[02 Concepts/Lifecycle/Training & Adaptation/Contrastive Learning|Contrastive Learning]]. **Condition:** When positives and negatives are constructed from the data itself, without example-level labels.

## Source

[Canonical Taxonomy](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/taxonomy.yml) · [Passage Alignment](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/mlsysbook-alignment.yml)

Taxonomy definitions and relationship wording: CC BY 4.0, with attribution to the Machine Learning Systems curriculum by Vijay Janapa Reddi and contributors. The textbook retains its separate license.
