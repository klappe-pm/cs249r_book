---
title: Dual Rate Hierarchical Policy
type: concept
tags:
- Type/Concept
- Group/System_Types
- Topic/Robot_Learning_Sim_to_Real
source_repository: https://github.com/klappe-pm/cs249r_book
source_commit: de87c0103806d7bfb1c677dbb77a2b92fa00c298
source_path: taxonomy/taxonomy.yml
source_label: Dual-rate hierarchical policy
taxonomy_id: mlsys.dual-rate-hierarchical-policy
taxonomy_status: draft
taxonomy_version: 0.4-draft
---

# Dual Rate Hierarchical Policy

Splitting a robot policy into a slow high-level model that sets goals or latent commands and a fast low-level controller that tracks them at control rate, so large-model latency does not set the control loop's rate.

## Browsing Home

[[02 Concepts/System Types/Embodied & Physical Systems/Robot Learning & Sim to Real Subject|Robot Learning & Sim to Real]] → [[02 Concepts/System Types/Embodied & Physical Systems/Embodied & Physical Systems Index|Embodied & Physical Systems]]

## Book Passages

These are explicitly recorded related passages from the upstream draft alignment; they do not certify complete coverage.

No explicit passage alignment is recorded for this concept. Subject reading pointers are available in its browsing home.

## Conditional Relationships

These are the taxonomy's draft editorial relationships. Read each relationship with its condition; an outgoing link is not a prerequisite claim.

- Decouples model rate from control rate differently from [[02 Concepts/System Types/Embodied & Physical Systems/Action Chunking|Action Chunking]]. **Condition:** When the large model is too slow to emit a new chunk before the current one runs out.

- Queries, as its slow high-level layer, [[02 Concepts/System Types/Embodied & Physical Systems/Vision Language Action Model|Vision Language Action Model]]. **Condition:** When the slow layer is a vision-language-action model.

## Search Terms

Upstream search terms may be related terms rather than exact synonyms: slow-fast policy; high-level and low-level policy; System 1 / System 2 control.

## Source

[Canonical Taxonomy](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/taxonomy.yml) · [Passage Alignment](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/mlsysbook-alignment.yml)

Taxonomy definitions and relationship wording: CC BY 4.0, with attribution to the Machine Learning Systems curriculum by Vijay Janapa Reddi and contributors. The textbook retains its separate license.
