---
title: Multimodal Encoder Disaggregation
type: concept
tags:
- Type/Concept
- Group/Lifecycle
- Topic/LLM_Generative_Inference
source_repository: https://github.com/klappe-pm/cs249r_book
source_commit: de87c0103806d7bfb1c677dbb77a2b92fa00c298
source_path: taxonomy/taxonomy.yml
source_label: Multimodal encoder disaggregation
taxonomy_id: mlsys.encoder-disaggregation
taxonomy_status: draft
taxonomy_version: 0.4-draft
---

# Multimodal Encoder Disaggregation

Scheduling modality encoders separately from prefill and decode and caching encoder outputs so image or audio inputs do not stall token generation.

## Browsing Home

[[02 Concepts/Lifecycle/Deployment & Serving/LLM & Generative Inference Subject|LLM & Generative Inference]] → [[02 Concepts/Lifecycle/Deployment & Serving/Deployment & Serving Index|Deployment & Serving]]

## Book Passages

These are explicitly recorded related passages from the upstream draft alignment; they do not certify complete coverage.

No explicit passage alignment is recorded for this concept. Subject reading pointers are available in its browsing home.

## Conditional Relationships

These are the taxonomy's draft editorial relationships. Read each relationship with its condition; an outgoing link is not a prerequisite claim.

- Reduces [[02 Concepts/Lifecycle/Deployment & Serving/Tail Latency|Tail Latency]]. **Condition:** Large media inputs would otherwise block token generation for requests sharing the batch.

- Schedules separately the [[02 Concepts/Foundations/Models & Architectures/Modality Encoder|Modality Encoder]]. **Condition:** Image or audio encoding is heavy enough to stall token generation if co-scheduled.

## Search Terms

Upstream search terms may be related terms rather than exact synonyms: encode-prefill-decode disaggregation.

## Source

[Canonical Taxonomy](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/taxonomy.yml) · [Passage Alignment](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/mlsysbook-alignment.yml)

Taxonomy definitions and relationship wording: CC BY 4.0, with attribution to the Machine Learning Systems curriculum by Vijay Janapa Reddi and contributors. The textbook retains its separate license.
