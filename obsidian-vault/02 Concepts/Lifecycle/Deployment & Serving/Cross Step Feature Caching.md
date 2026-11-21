---
title: Cross Step Feature Caching
type: concept
tags:
- Type/Concept
- Group/Lifecycle
- Topic/LLM_Generative_Inference
source_repository: https://github.com/klappe-pm/cs249r_book
source_commit: de87c0103806d7bfb1c677dbb77a2b92fa00c298
source_path: taxonomy/taxonomy.yml
source_label: Cross-step feature caching
taxonomy_id: mlsys.diffusion-feature-caching
taxonomy_status: draft
taxonomy_version: 0.4-draft
---

# Cross Step Feature Caching

Reusing intermediate activations that change little between adjacent denoising steps instead of recomputing them, cutting per-step cost at bounded quality loss.

## Browsing Home

[[02 Concepts/Lifecycle/Deployment & Serving/LLM & Generative Inference Subject|LLM & Generative Inference]] → [[02 Concepts/Lifecycle/Deployment & Serving/Deployment & Serving Index|Deployment & Serving]]

## Book Passages

These are explicitly recorded related passages from the upstream draft alignment; they do not certify complete coverage.

No explicit passage alignment is recorded for this concept. Subject reading pointers are available in its browsing home.

## Conditional Relationships

These are the taxonomy's draft editorial relationships. Read each relationship with its condition; an outgoing link is not a prerequisite claim.

- Increases cached-activation [[02 Concepts/Foundations/Workloads & Requirements/Memory Footprint|Memory Footprint]]. **Condition:** Holds because cached features from earlier steps must stay resident.

- Reduces [[02 Concepts/Qualities/Performance, Efficiency & Benchmarking/Execution Time|Execution Time]]. **Condition:** Holds when adjacent-step features change little, so skipped blocks lose little quality.

- Reuses intermediate features across the denoising steps of [[02 Concepts/Foundations/Models & Architectures/Diffusion Model|Diffusion Model]]. **Condition:** When adjacent sampling steps produce similar features in some blocks, so those blocks can be skipped and their cached output reused.

## Search Terms

Upstream search terms may be related terms rather than exact synonyms: diffusion caching.

## Source

[Canonical Taxonomy](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/taxonomy.yml) · [Passage Alignment](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/mlsysbook-alignment.yml)

Taxonomy definitions and relationship wording: CC BY 4.0, with attribution to the Machine Learning Systems curriculum by Vijay Janapa Reddi and contributors. The textbook retains its separate license.
