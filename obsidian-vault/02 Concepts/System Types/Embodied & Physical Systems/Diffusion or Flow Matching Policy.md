---
title: Diffusion or Flow Matching Policy
type: concept
tags:
- Type/Concept
- Group/System_Types
- Topic/Robot_Learning_Sim_to_Real
source_repository: https://github.com/klappe-pm/cs249r_book
source_commit: de87c0103806d7bfb1c677dbb77a2b92fa00c298
source_path: taxonomy/taxonomy.yml
source_label: Diffusion or flow-matching policy
taxonomy_id: mlsys.diffusion-policy
taxonomy_status: draft
taxonomy_version: 0.4-draft
---

# Diffusion or Flow Matching Policy

Robot policies that generate continuous actions through iterative denoising or learned-flow integration, representing multiple action modes while spending an inference-iteration budget.

## Browsing Home

[[02 Concepts/System Types/Embodied & Physical Systems/Robot Learning & Sim to Real Subject|Robot Learning & Sim to Real]] → [[02 Concepts/System Types/Embodied & Physical Systems/Embodied & Physical Systems Index|Embodied & Physical Systems]]

## Book Passages

These are explicitly recorded related passages from the upstream draft alignment; they do not certify complete coverage.

No explicit passage alignment is recorded for this concept. Subject reading pointers are available in its browsing home.

## Conditional Relationships

These are the taxonomy's draft editorial relationships. Read each relationship with its condition; an outgoing link is not a prerequisite claim.

- Generates actions with [[02 Concepts/Foundations/Models & Architectures/Diffusion Model|Diffusion Model]]. **Condition:** When the action generator reverses a noising process; flow-matching policies integrate a learned flow instead.

- Predicts action sequences as in [[02 Concepts/System Types/Embodied & Physical Systems/Action Chunking|Action Chunking]]. **Condition:** Actions are generated over a short horizon.

- Generates continuous actions by denoising rather than through the discretization of [[02 Concepts/System Types/Embodied & Physical Systems/Action Tokenization|Action Tokenization]]. **Condition:** When choosing a robot policy's action head: tokens trade reconstruction error and decode steps against expressiveness; denoising trades inference iterations against multimodality.

## Search Terms

Upstream search terms may be related terms rather than exact synonyms: flow-matching policy; diffusion policy.

## Source

[Canonical Taxonomy](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/taxonomy.yml) · [Passage Alignment](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/mlsysbook-alignment.yml)

Taxonomy definitions and relationship wording: CC BY 4.0, with attribution to the Machine Learning Systems curriculum by Vijay Janapa Reddi and contributors. The textbook retains its separate license.
