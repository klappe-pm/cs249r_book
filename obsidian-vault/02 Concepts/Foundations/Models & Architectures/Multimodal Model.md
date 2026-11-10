---
title: Multimodal Model
type: concept
tags:
- Type/Concept
- Group/Foundations
- Topic/Model_Families
source_repository: https://github.com/klappe-pm/cs249r_book
source_commit: de87c0103806d7bfb1c677dbb77a2b92fa00c298
source_path: taxonomy/taxonomy.yml
source_label: Multimodal model
taxonomy_id: mlsys.multimodal-model
taxonomy_status: draft
taxonomy_version: 0.4-draft
---

# Multimodal Model

A model that consumes or produces several modalities, such as text, images, audio, or video, through modality encoders feeding a shared backbone.

## Browsing Home

[[02 Concepts/Foundations/Models & Architectures/Model Families Subject|Model Families]] → [[02 Concepts/Foundations/Models & Architectures/Models & Architectures Index|Models & Architectures]]

## Book Passages

These are explicitly recorded related passages from the upstream draft alignment; they do not certify complete coverage.

No explicit passage alignment is recorded for this concept. Subject reading pointers are available in its browsing home.

## Conditional Relationships

These are the taxonomy's draft editorial relationships. Read each relationship with its condition; an outgoing link is not a prerequisite claim.

- Is composed with [[02 Concepts/Foundations/Models & Architectures/Modality Encoder|Modality Encoder]]. **Condition:** Non-text inputs are encoded into tokens the shared backbone attends over.

- Commonly uses as its shared backbone a [[02 Concepts/Foundations/Models & Architectures/Transformer|Transformer]]. **Condition:** Encoded modality tokens are processed together with text tokens by a transformer.

## Search Terms

Upstream search terms may be related terms rather than exact synonyms: vision-language model; VLM.

## Source

[Canonical Taxonomy](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/taxonomy.yml) · [Passage Alignment](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/mlsysbook-alignment.yml)

Taxonomy definitions and relationship wording: CC BY 4.0, with attribution to the Machine Learning Systems curriculum by Vijay Janapa Reddi and contributors. The textbook retains its separate license.
