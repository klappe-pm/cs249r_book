---
title: Vision Language Action Model
type: concept
tags:
- Type/Concept
- Group/System_Types
- Topic/Robot_Learning_Sim_to_Real
source_repository: https://github.com/klappe-pm/cs249r_book
source_commit: de87c0103806d7bfb1c677dbb77a2b92fa00c298
source_path: taxonomy/taxonomy.yml
source_label: Vision-language-action model
taxonomy_id: mlsys.vla-model
taxonomy_status: draft
taxonomy_version: 0.4-draft
---

# Vision Language Action Model

A policy built on a pretrained vision-language backbone that maps images and language instructions to robot actions.

## Browsing Home

[[02 Concepts/System Types/Embodied & Physical Systems/Robot Learning & Sim to Real Subject|Robot Learning & Sim to Real]] → [[02 Concepts/System Types/Embodied & Physical Systems/Embodied & Physical Systems Index|Embodied & Physical Systems]]

## Book Passages

These are explicitly recorded related passages from the upstream draft alignment; they do not certify complete coverage.

No explicit passage alignment is recorded for this concept. Subject reading pointers are available in its browsing home.

## Conditional Relationships

These are the taxonomy's draft editorial relationships. Read each relationship with its condition; an outgoing link is not a prerequisite claim.

- Increases [[02 Concepts/System Types/Embodied & Physical Systems/Observation Age|Observation Age]]. **Condition:** Holds when billion-parameter inference on robot compute runs slower than the control loop.

- Uses, to decouple control rate from inference rate, [[02 Concepts/System Types/Embodied & Physical Systems/Action Chunking|Action Chunking]]. **Condition:** Chunks executed open-loop delay reaction to new observations until the next inference.

- Is a kind of [[02 Concepts/Foundations/Models & Architectures/Multimodal Model|Multimodal Model]]. **Condition:** The model consumes images and language and emits actions through a shared backbone.

- Is commonly trained by [[02 Concepts/Lifecycle/Training & Adaptation/Imitation Learning|Imitation Learning]]. **Condition:** Applies when robot demonstrations supply the action targets.

- Transfers web-scale vision-language knowledge through [[02 Concepts/Lifecycle/Training & Adaptation/Transfer Learning|Transfer Learning]]. **Condition:** When the policy is fine-tuned from a pretrained vision-language backbone.

- Is fine-tuned on [[02 Concepts/System Types/Embodied & Physical Systems/Teleoperation Data|Teleoperation Data]]. **Condition:** When robot action labels come from human-driven demonstrations.

- Can emit continuous actions through a [[02 Concepts/System Types/Embodied & Physical Systems/Diffusion or Flow Matching Policy|Diffusion or Flow Matching Policy]]. **Condition:** When the action head denoises or integrates a learned flow instead of decoding action tokens (pi0 and its successors).

- Is commonly pretrained with [[02 Concepts/System Types/Embodied & Physical Systems/Cross Embodiment Training|Cross Embodiment Training]]. **Condition:** When the policy is pretrained on pooled multi-robot datasets before task fine-tuning.

## Search Terms

Upstream search terms may be related terms rather than exact synonyms: VLA; robot foundation model.

## Source

[Canonical Taxonomy](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/taxonomy.yml) · [Passage Alignment](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/mlsysbook-alignment.yml)

Taxonomy definitions and relationship wording: CC BY 4.0, with attribution to the Machine Learning Systems curriculum by Vijay Janapa Reddi and contributors. The textbook retains its separate license.
