---
title: Contrastive Learning
type: concept
tags:
- Type/Concept
- Group/Lifecycle
- Topic/Learning_Paradigms
- Context/Background
source_repository: https://github.com/klappe-pm/cs249r_book
source_commit: de87c0103806d7bfb1c677dbb77a2b92fa00c298
source_path: taxonomy/taxonomy.yml
source_label: Contrastive learning
taxonomy_id: mlsys.contrastive-learning
taxonomy_status: draft
taxonomy_version: 0.4-draft
---

# Contrastive Learning

A self-supervised or paired-data objective that pulls representations of matched views or pairs together and pushes mismatched ones apart, whose quality depends on how many negatives each step sees, which makes large batches and their memory a systems cost.

## Browsing Home

[[02 Concepts/Lifecycle/Training & Adaptation/Learning Paradigms Subject|Learning Paradigms]] → [[02 Concepts/Lifecycle/Training & Adaptation/Training & Adaptation Index|Training & Adaptation]]

This is a background concept on which ML systems reasoning depends; that classification does not make it optional.

## Book Passages

These are explicitly recorded related passages from the upstream draft alignment; they do not certify complete coverage.

No explicit passage alignment is recorded for this concept. Subject reading pointers are available in its browsing home.

## Conditional Relationships

These are the taxonomy's draft editorial relationships. Read each relationship with its condition; an outgoing link is not a prerequisite claim.

- Trains the encoders behind [[02 Concepts/Foundations/Models & Architectures/Embeddings|Embeddings]]. **Condition:** When the learned representation is reused for retrieval, classification heads, or multimodal alignment.

- Trains the bi-encoders used by [[02 Concepts/Lifecycle/Deployment & Serving/Dense Retrieval|Dense Retrieval]]. **Condition:** When query-document pairs supply positives and in-batch items supply negatives.

## Search Terms

Upstream search terms may be related terms rather than exact synonyms: InfoNCE; SimCLR-style training; CLIP-style training; in-batch negatives.

## Source

[Canonical Taxonomy](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/taxonomy.yml) · [Passage Alignment](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/mlsysbook-alignment.yml)

Taxonomy definitions and relationship wording: CC BY 4.0, with attribution to the Machine Learning Systems curriculum by Vijay Janapa Reddi and contributors. The textbook retains its separate license.
