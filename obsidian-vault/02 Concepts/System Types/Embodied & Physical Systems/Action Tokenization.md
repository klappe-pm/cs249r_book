---
title: Action Tokenization
type: concept
tags:
- Type/Concept
- Group/System_Types
- Topic/Robot_Learning_Sim_to_Real
source_repository: https://github.com/klappe-pm/cs249r_book
source_commit: de87c0103806d7bfb1c677dbb77a2b92fa00c298
source_path: taxonomy/taxonomy.yml
source_label: Action tokenization
taxonomy_id: mlsys.action-tokenization
taxonomy_status: draft
taxonomy_version: 0.4-draft
---

# Action Tokenization

Encoding continuous robot actions or action sequences as discrete model tokens, making reconstruction error and token count determinants of policy fidelity and execution cost.

## Browsing Home

[[02 Concepts/System Types/Embodied & Physical Systems/Robot Learning & Sim to Real Subject|Robot Learning & Sim to Real]] → [[02 Concepts/System Types/Embodied & Physical Systems/Embodied & Physical Systems Index|Embodied & Physical Systems]]

## Book Passages

These are explicitly recorded related passages from the upstream draft alignment; they do not certify complete coverage.

No explicit passage alignment is recorded for this concept. Subject reading pointers are available in its browsing home.

## Conditional Relationships

These are the taxonomy's draft editorial relationships. Read each relationship with its condition; an outgoing link is not a prerequisite claim.

- Uses discretization of continuous action information [[02 Concepts/Qualities/Performance, Efficiency & Benchmarking/Quantization|Quantization]]. **Condition:** When continuous commands or transformed action coefficients are mapped to a finite vocabulary.

- Sets the sequential decoding work in [[02 Concepts/Qualities/Performance, Efficiency & Benchmarking/Execution Time|Execution Time]]. **Condition:** When actions are decoded autoregressively and architecture, hardware, and action horizon are held fixed.

- Is the action output representation of [[02 Concepts/System Types/Embodied & Physical Systems/Vision Language Action Model|Vision Language Action Model]]. **Condition:** For vision-language-action models that emit actions as tokens.

## Search Terms

Upstream search terms may be related terms rather than exact synonyms: robot action tokenization; action-sequence tokenization.

## Source

[Canonical Taxonomy](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/taxonomy.yml) · [Passage Alignment](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/mlsysbook-alignment.yml)

Taxonomy definitions and relationship wording: CC BY 4.0, with attribution to the Machine Learning Systems curriculum by Vijay Janapa Reddi and contributors. The textbook retains its separate license.
