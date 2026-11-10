---
title: Denoising Step Reduction
type: concept
tags:
- Type/Concept
- Group/Lifecycle
- Topic/LLM_Generative_Inference
source_repository: https://github.com/klappe-pm/cs249r_book
source_commit: de87c0103806d7bfb1c677dbb77a2b92fa00c298
source_path: taxonomy/taxonomy.yml
source_label: Denoising-step reduction
taxonomy_id: mlsys.denoising-step-reduction
taxonomy_status: draft
taxonomy_version: 0.4-draft
---

# Denoising Step Reduction

Lowering network evaluations per diffusion sample with faster samplers, step distillation, or consistency models, trading sample quality against latency and cost.

## Browsing Home

[[02 Concepts/Lifecycle/Deployment & Serving/LLM & Generative Inference Subject|LLM & Generative Inference]] → [[02 Concepts/Lifecycle/Deployment & Serving/Deployment & Serving Index|Deployment & Serving]]

## Book Passages

These are explicitly recorded related passages from the upstream draft alignment; they do not certify complete coverage.

No explicit passage alignment is recorded for this concept. Subject reading pointers are available in its browsing home.

## Conditional Relationships

These are the taxonomy's draft editorial relationships. Read each relationship with its condition; an outgoing link is not a prerequisite claim.

- Often uses step [[02 Concepts/Qualities/Performance, Efficiency & Benchmarking/Knowledge Distillation|Knowledge Distillation]]. **Condition:** Applies to progressive and consistency distillation, not to training-free fast samplers.

- Reduces per-sample [[02 Concepts/Qualities/Performance, Efficiency & Benchmarking/Execution Time|Execution Time]]. **Condition:** Holds roughly in proportion to the number of network evaluations removed.

## Search Terms

Upstream search terms may be related terms rather than exact synonyms: few-step sampling; step distillation.

## Source

[Canonical Taxonomy](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/taxonomy.yml) · [Passage Alignment](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/mlsysbook-alignment.yml)

Taxonomy definitions and relationship wording: CC BY 4.0, with attribution to the Machine Learning Systems curriculum by Vijay Janapa Reddi and contributors. The textbook retains its separate license.
