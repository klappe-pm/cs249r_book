---
title: Slice Discovery
type: concept
tags:
- Type/Concept
- Group/Lifecycle
- Topic/Sliced_Robustness_Evaluation
source_repository: https://github.com/klappe-pm/cs249r_book
source_commit: de87c0103806d7bfb1c677dbb77a2b92fa00c298
source_path: taxonomy/taxonomy.yml
source_label: Slice discovery
taxonomy_id: mlsys.slice-discovery
taxonomy_status: draft
taxonomy_version: 0.4-draft
---

# Slice Discovery

Automatically finding coherent data subsets on which a model underperforms, without predefined slice labels.

## Browsing Home

[[02 Concepts/Lifecycle/Model Evaluation & Testing/Sliced & Robustness Evaluation Subject|Sliced & Robustness Evaluation]] → [[02 Concepts/Lifecycle/Model Evaluation & Testing/Model Evaluation & Testing Index|Model Evaluation & Testing]]

## Book Passages

These are explicitly recorded related passages from the upstream draft alignment; they do not certify complete coverage.

No explicit passage alignment is recorded for this concept. Subject reading pointers are available in its browsing home.

## Conditional Relationships

These are the taxonomy's draft editorial relationships. Read each relationship with its condition; an outgoing link is not a prerequisite claim.

- Proposes slices for [[02 Concepts/Lifecycle/Model Evaluation & Testing/Sliced Evaluation|Sliced Evaluation]]. **Condition:** Discovered slices require human review for coherence and multiple-comparison effects.

- Clusters errors with [[02 Concepts/Lifecycle/Training & Adaptation/Unsupervised Learning|Unsupervised Learning]]. **Condition:** Applies to methods that group examples without predefined slice labels.

- Searches for coherent slices in [[02 Concepts/Foundations/Models & Architectures/Embeddings|Embeddings]]. **Condition:** Holds for embedding-based methods such as Domino.

## Source

[Canonical Taxonomy](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/taxonomy.yml) · [Passage Alignment](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/mlsysbook-alignment.yml)

Taxonomy definitions and relationship wording: CC BY 4.0, with attribution to the Machine Learning Systems curriculum by Vijay Janapa Reddi and contributors. The textbook retains its separate license.
