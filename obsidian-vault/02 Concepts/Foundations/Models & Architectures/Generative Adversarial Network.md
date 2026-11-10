---
title: Generative Adversarial Network
type: concept
tags:
- Type/Concept
- Group/Foundations
- Topic/Model_Families
source_repository: https://github.com/klappe-pm/cs249r_book
source_commit: de87c0103806d7bfb1c677dbb77a2b92fa00c298
source_path: taxonomy/taxonomy.yml
source_label: Generative adversarial network
taxonomy_id: mlsys.gan
taxonomy_status: draft
taxonomy_version: 0.4-draft
---

# Generative Adversarial Network

A generator and a discriminator trained against each other, so the generator learns to produce samples the discriminator cannot tell apart from data.

## Browsing Home

[[02 Concepts/Foundations/Models & Architectures/Model Families Subject|Model Families]] → [[02 Concepts/Foundations/Models & Architectures/Models & Architectures Index|Models & Architectures]]

## Book Passages

These are explicitly recorded related passages from the upstream draft alignment; they do not certify complete coverage.

No explicit passage alignment is recorded for this concept. Subject reading pointers are available in its browsing home.

## Conditional Relationships

These are the taxonomy's draft editorial relationships. Read each relationship with its condition; an outgoing link is not a prerequisite claim.

- Competes for sample generation with [[02 Concepts/Foundations/Models & Architectures/Diffusion Model|Diffusion Model]]. **Condition:** Single-step sampling versus many denoising steps, with different stability and diversity.

- Is prone to [[02 Concepts/Lifecycle/Training & Adaptation/Mode Collapse|Mode Collapse]]. **Condition:** The generator outpaces the discriminator during adversarial training.

## Search Terms

Upstream search terms may be related terms rather than exact synonyms: GAN.

## Source

[Canonical Taxonomy](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/taxonomy.yml) · [Passage Alignment](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/mlsysbook-alignment.yml)

Taxonomy definitions and relationship wording: CC BY 4.0, with attribution to the Machine Learning Systems curriculum by Vijay Janapa Reddi and contributors. The textbook retains its separate license.
