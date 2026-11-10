---
title: Model Merging
type: concept
tags:
- Type/Concept
- Group/Lifecycle
- Topic/Adaptation_Fine_Tuning_Prompting_Transfer
source_repository: https://github.com/klappe-pm/cs249r_book
source_commit: de87c0103806d7bfb1c677dbb77a2b92fa00c298
source_path: taxonomy/taxonomy.yml
source_label: Model merging
taxonomy_id: mlsys.model-merging
taxonomy_status: draft
taxonomy_version: 0.4-draft
---

# Model Merging

Combining compatible model parameters or parameter updates, by averaging or arithmetic on weight differences, into one model that consolidates capabilities without further training or serving the sources separately.

## Browsing Home

[[02 Concepts/Lifecycle/Training & Adaptation/Adaptation Fine Tuning, Prompting & Transfer Subject|Adaptation Fine Tuning, Prompting & Transfer]] → [[02 Concepts/Lifecycle/Training & Adaptation/Training & Adaptation Index|Training & Adaptation]]

## Book Passages

These are explicitly recorded related passages from the upstream draft alignment; they do not certify complete coverage.

No explicit passage alignment is recorded for this concept. Subject reading pointers are available in its browsing home.

## Conditional Relationships

These are the taxonomy's draft editorial relationships. Read each relationship with its condition; an outgoing link is not a prerequisite claim.

- Folds several fine-tunes into one weight set instead of [[02 Concepts/Lifecycle/Deployment & Serving/Multi Adapter Serving|Multi Adapter Serving]]. **Condition:** When the fine-tunes need not stay separately addressable and the merged model keeps acceptable quality on each task.

- Limits [[02 Concepts/Lifecycle/Training & Adaptation/Catastrophic Forgetting|Catastrophic Forgetting]]. **Condition:** Relative to the fine-tuned model alone, when interpolating with the pretrained base improves measured retention on the original tasks.

## Search Terms

Upstream search terms may be related terms rather than exact synonyms: model soup; task arithmetic; TIES-merging; weight merging.

## Source

[Canonical Taxonomy](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/taxonomy.yml) · [Passage Alignment](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/mlsysbook-alignment.yml)

Taxonomy definitions and relationship wording: CC BY 4.0, with attribution to the Machine Learning Systems curriculum by Vijay Janapa Reddi and contributors. The textbook retains its separate license.
