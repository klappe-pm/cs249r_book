---
title: Multi Adapter Serving
type: concept
tags:
- Type/Concept
- Group/Lifecycle
- Topic/Serving_Architectures
source_repository: https://github.com/klappe-pm/cs249r_book
source_commit: de87c0103806d7bfb1c677dbb77a2b92fa00c298
source_path: taxonomy/taxonomy.yml
source_label: Multi-adapter serving
taxonomy_id: mlsys.multi-adapter-serving
taxonomy_status: draft
taxonomy_version: 0.4-draft
---

# Multi Adapter Serving

Serving many low-rank adapters over one shared base model by batching requests for different adapters with heterogeneous kernels and paging adapter weights on demand.

## Browsing Home

[[02 Concepts/Lifecycle/Deployment & Serving/Serving Architectures Subject|Serving Architectures]] → [[02 Concepts/Lifecycle/Deployment & Serving/Deployment & Serving Index|Deployment & Serving]]

## Book Passages

These are explicitly recorded related passages from the upstream draft alignment; they do not certify complete coverage.

No explicit passage alignment is recorded for this concept. Subject reading pointers are available in its browsing home.

## Conditional Relationships

These are the taxonomy's draft editorial relationships. Read each relationship with its condition; an outgoing link is not a prerequisite claim.

- Serves many instances of [[02 Concepts/Lifecycle/Training & Adaptation/Low Rank Adaptation|Low Rank Adaptation]]. **Condition:** Holds when adapters share one frozen base model so base weights are loaded once and only low-rank factors differ per request.

- Specializes [[02 Concepts/Lifecycle/Deployment & Serving/Multi Model Serving|Multi Model Serving]]. **Condition:** Applies when hosted variants differ only by adapters, letting requests for different variants share one batch.

- Reduces [[02 Concepts/Qualities/Sustainability & Cost/Cost per Useful Outcome|Cost per Useful Outcome]]. **Condition:** Holds relative to one dedicated deployment per fine-tuned model.

## Search Terms

Upstream search terms may be related terms rather than exact synonyms: multi-LoRA serving; multi-tenant LoRA.

## Source

[Canonical Taxonomy](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/taxonomy.yml) · [Passage Alignment](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/mlsysbook-alignment.yml)

Taxonomy definitions and relationship wording: CC BY 4.0, with attribution to the Machine Learning Systems curriculum by Vijay Janapa Reddi and contributors. The textbook retains its separate license.
