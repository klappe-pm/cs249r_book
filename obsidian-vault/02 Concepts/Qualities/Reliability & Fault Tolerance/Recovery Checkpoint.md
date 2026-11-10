---
title: Recovery Checkpoint
type: concept
tags:
- Type/Concept
- Group/Qualities
- Topic/Checkpointing_Elastic_Recovery
source_repository: https://github.com/klappe-pm/cs249r_book
source_commit: de87c0103806d7bfb1c677dbb77a2b92fa00c298
source_path: taxonomy/taxonomy.yml
source_label: Recovery checkpoint
taxonomy_id: mlsys.checkpoint
taxonomy_status: draft
taxonomy_version: 0.4-draft
---

# Recovery Checkpoint

A persisted state from which a specified computation can resume.

## Browsing Home

[[02 Concepts/Qualities/Reliability & Fault Tolerance/Checkpointing & Elastic Recovery Subject|Checkpointing & Elastic Recovery]] → [[02 Concepts/Qualities/Reliability & Fault Tolerance/Reliability & Fault Tolerance Index|Reliability & Fault Tolerance]]

## Book Passages

These are explicitly recorded related passages from the upstream draft alignment; they do not certify complete coverage.

- [[01 Books/Volume II - Scaling/01 The Fleet/04 Data Storage/V2-04.07 Checkpoint Storage#^sec-storage-checkpointing|V2-04.07 Checkpoint Storage]] — Durable checkpoint. [Exact Source Passage](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/books/vol2/04_data_storage/04_data_storage.qmd#L3523).

- [[01 Books/Volume III - Agentic Systems/04 The Agent Runtime/11 Durable Execution/V3-11.05 Checkpoints#^sec-vol3-persistence-checkpointing|V3-11.05 Checkpoints]] — Recovery checkpoint. [Exact Source Passage](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/books/vol3/11_durable_execution/11_durable_execution.qmd#L337).

## Conditional Relationships

These are the taxonomy's draft editorial relationships. Read each relationship with its condition; an outgoing link is not a prerequisite claim.

- Requires, for distributed jobs, a [[02 Concepts/Qualities/Reliability & Fault Tolerance/Consistent Checkpoint Cut|Consistent Checkpoint Cut]]. **Condition:** The saved worker states and dependencies must form a recoverable state.

- Enables restarts that recover from [[02 Concepts/Lifecycle/Training & Adaptation/Training Instability|Training Instability]]. **Condition:** Holds when loss spikes are handled by rolling back to an earlier checkpoint and changing data order or hyperparameters.

## Themes

- [[03 Themes/Reliability and Recovery|Reliability and Recovery]]

## Source

[Canonical Taxonomy](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/taxonomy.yml) · [Passage Alignment](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/mlsysbook-alignment.yml)

Taxonomy definitions and relationship wording: CC BY 4.0, with attribution to the Machine Learning Systems curriculum by Vijay Janapa Reddi and contributors. The textbook retains its separate license.
