---
title: Action Chunking
type: concept
tags:
- Type/Concept
- Group/System_Types
- Topic/Robot_Learning_Sim_to_Real
source_repository: https://github.com/klappe-pm/cs249r_book
source_commit: de87c0103806d7bfb1c677dbb77a2b92fa00c298
source_path: taxonomy/taxonomy.yml
source_label: Action chunking
taxonomy_id: mlsys.action-chunking
taxonomy_status: draft
taxonomy_version: 0.4-draft
---

# Action Chunking

Predicting a short sequence of future actions per policy inference, decoupling model invocation rate from control rate and reducing compounding error.

## Browsing Home

[[02 Concepts/System Types/Embodied & Physical Systems/Robot Learning & Sim to Real Subject|Robot Learning & Sim to Real]] → [[02 Concepts/System Types/Embodied & Physical Systems/Embodied & Physical Systems Index|Embodied & Physical Systems]]

## Book Passages

These are explicitly recorded related passages from the upstream draft alignment; they do not certify complete coverage.

- [[01 Books/Volume IV - Physical AI/01 Machine Anatomy/03 The Cognitive Brain/V4-03.06 Chunk Supply and Evidence Validity#^sec-brain-action-chunking|V4-03.06 Chunk Supply and Evidence Validity]] — Action chunk. [Exact Source Passage](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/books/vol4/03_brain/03_brain.qmd#L1161).

## Conditional Relationships

These are the taxonomy's draft editorial relationships. Read each relationship with its condition; an outgoing link is not a prerequisite claim.

- Increases, for actions late in a chunk, [[02 Concepts/System Types/Embodied & Physical Systems/Observation Age|Observation Age]]. **Condition:** When chunks execute open loop, so later actions rest on older observations.

- Shortens the effective horizon of [[02 Concepts/Lifecycle/Training & Adaptation/Compounding Error in Sequential Decisions|Compounding Error in Sequential Decisions]]. **Condition:** Actions are predicted in multi-step chunks.

## Source

[Canonical Taxonomy](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/taxonomy.yml) · [Passage Alignment](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/mlsysbook-alignment.yml)

Taxonomy definitions and relationship wording: CC BY 4.0, with attribution to the Machine Learning Systems curriculum by Vijay Janapa Reddi and contributors. The textbook retains its separate license.
