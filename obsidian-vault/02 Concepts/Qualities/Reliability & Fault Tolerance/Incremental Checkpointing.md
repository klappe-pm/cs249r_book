---
title: Incremental Checkpointing
type: concept
tags:
- Type/Concept
- Group/Qualities
- Topic/Checkpointing_Elastic_Recovery
source_repository: https://github.com/klappe-pm/cs249r_book
source_commit: de87c0103806d7bfb1c677dbb77a2b92fa00c298
source_path: taxonomy/taxonomy.yml
source_label: Incremental checkpointing
taxonomy_id: mlsys.incremental-checkpointing
taxonomy_status: draft
taxonomy_version: 0.4-draft
---

# Incremental Checkpointing

Persisting only the state that changed since the preceding checkpoint, with periodic full checkpoints as bases, which cuts write volume when updates are sparse at the cost of reconstructing state from a chain on restore.

## Browsing Home

[[02 Concepts/Qualities/Reliability & Fault Tolerance/Checkpointing & Elastic Recovery Subject|Checkpointing & Elastic Recovery]] → [[02 Concepts/Qualities/Reliability & Fault Tolerance/Reliability & Fault Tolerance Index|Reliability & Fault Tolerance]]

## Book Passages

These are explicitly recorded related passages from the upstream draft alignment; they do not certify complete coverage.

No explicit passage alignment is recorded for this concept. Subject reading pointers are available in its browsing home.

## Conditional Relationships

These are the taxonomy's draft editorial relationships. Read each relationship with its condition; an outgoing link is not a prerequisite claim.

- Produces, as a base plus a chain of changes, [[02 Concepts/Qualities/Reliability & Fault Tolerance/Recovery Checkpoint|Recovery Checkpoint]]. **Condition:** When only a fraction of the state, such as touched embedding rows, changes between checkpoints.

- Cuts the bytes written by [[02 Concepts/Stack/Datacenter Infrastructure & Fleet/Checkpoint IO|Checkpoint IO]]. **Condition:** When the changed fraction of state is small; restore must read the base and every later delta.

## Search Terms

Upstream search terms may be related terms rather than exact synonyms: delta checkpoint.

## Source

[Canonical Taxonomy](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/taxonomy.yml) · [Passage Alignment](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/mlsysbook-alignment.yml)

Taxonomy definitions and relationship wording: CC BY 4.0, with attribution to the Machine Learning Systems curriculum by Vijay Janapa Reddi and contributors. The textbook retains its separate license.
