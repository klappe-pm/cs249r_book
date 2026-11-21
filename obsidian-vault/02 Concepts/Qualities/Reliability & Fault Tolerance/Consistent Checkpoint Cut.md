---
title: Consistent Checkpoint Cut
type: concept
tags:
- Type/Concept
- Group/Qualities
- Topic/Checkpointing_Elastic_Recovery
source_repository: https://github.com/klappe-pm/cs249r_book
source_commit: de87c0103806d7bfb1c677dbb77a2b92fa00c298
source_path: taxonomy/taxonomy.yml
source_label: Consistent checkpoint cut
taxonomy_id: mlsys.consistent-cut
taxonomy_status: draft
taxonomy_version: 0.4-draft
---

# Consistent Checkpoint Cut

A set of per-worker checkpoint states taken so that no saved state depends on an update or message that another worker's saved state has not yet recorded, so restoring all of them together yields one coherent global state.

## Browsing Home

[[02 Concepts/Qualities/Reliability & Fault Tolerance/Checkpointing & Elastic Recovery Subject|Checkpointing & Elastic Recovery]] → [[02 Concepts/Qualities/Reliability & Fault Tolerance/Reliability & Fault Tolerance Index|Reliability & Fault Tolerance]]

## Book Passages

These are explicitly recorded related passages from the upstream draft alignment; they do not certify complete coverage.

- [[01 Books/Volume II - Scaling/02 Distributed ML/07 Fault Tolerance/V2-07.09 Checkpointing and Progress Preservation#^sec-fault-tolerance-reliability-checkpoint-coordination-patterns-f670|V2-07.09 Checkpointing and Progress Preservation]] — Consistent checkpoint cut. [Exact Source Passage](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/books/vol2/07_fault_tolerance/07_fault_tolerance.qmd#L2003).

## Conditional Relationships

These are the taxonomy's draft editorial relationships. Read each relationship with its condition; an outgoing link is not a prerequisite claim.

- Enables [[02 Concepts/Qualities/Reliability & Fault Tolerance/Checkpoint Resharding|Checkpoint Resharding]]. **Condition:** A sharded checkpoint can be remapped to a new layout only when all shards were saved from the same training step.

## Source

[Canonical Taxonomy](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/taxonomy.yml) · [Passage Alignment](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/mlsysbook-alignment.yml)

Taxonomy definitions and relationship wording: CC BY 4.0, with attribution to the Machine Learning Systems curriculum by Vijay Janapa Reddi and contributors. The textbook retains its separate license.
