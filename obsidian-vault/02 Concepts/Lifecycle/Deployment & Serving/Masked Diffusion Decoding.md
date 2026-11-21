---
title: Masked Diffusion Decoding
type: concept
tags:
- Type/Concept
- Group/Lifecycle
- Topic/LLM_Generative_Inference
source_repository: https://github.com/klappe-pm/cs249r_book
source_commit: de87c0103806d7bfb1c677dbb77a2b92fa00c298
source_path: taxonomy/taxonomy.yml
source_label: Masked diffusion decoding
taxonomy_id: mlsys.masked-diffusion-decoding
taxonomy_status: draft
taxonomy_version: 0.4-draft
---

# Masked Diffusion Decoding

Generating text by repeatedly predicting and committing masked positions in parallel, trading refinement passes for token parallelism while weakening the attention-state reuse that autoregressive decoding relies on.

## Browsing Home

[[02 Concepts/Lifecycle/Deployment & Serving/LLM & Generative Inference Subject|LLM & Generative Inference]] → [[02 Concepts/Lifecycle/Deployment & Serving/Deployment & Serving Index|Deployment & Serving]]

## Book Passages

These are explicitly recorded related passages from the upstream draft alignment; they do not certify complete coverage.

No explicit passage alignment is recorded for this concept. Subject reading pointers are available in its browsing home.

## Conditional Relationships

These are the taxonomy's draft editorial relationships. Read each relationship with its condition; an outgoing link is not a prerequisite claim.

- Generates text with a discrete denoising model from [[02 Concepts/Foundations/Models & Architectures/Diffusion Model|Diffusion Model]]. **Condition:** When a language model is trained to predict masked tokens over several refinement passes.

- Limits unchanged-prefix state reuse in [[02 Concepts/Lifecycle/Deployment & Serving/Prefix Caching|Prefix Caching]]. **Condition:** When refinement passes can revise earlier positions, so a fixed prefix's attention state is not final.

## Search Terms

Upstream search terms may be related terms rather than exact synonyms: masked diffusion language decoding; parallel masked-token decoding.

## Source

[Canonical Taxonomy](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/taxonomy.yml) · [Passage Alignment](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/mlsysbook-alignment.yml)

Taxonomy definitions and relationship wording: CC BY 4.0, with attribution to the Machine Learning Systems curriculum by Vijay Janapa Reddi and contributors. The textbook retains its separate license.
