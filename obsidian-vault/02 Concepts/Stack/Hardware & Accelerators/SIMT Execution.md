---
title: SIMT Execution
type: concept
tags:
- Type/Concept
- Group/Stack
- Topic/Accelerator_Architecture
source_repository: https://github.com/klappe-pm/cs249r_book
source_commit: de87c0103806d7bfb1c677dbb77a2b92fa00c298
source_path: taxonomy/taxonomy.yml
source_label: SIMT execution
taxonomy_id: mlsys.simt
taxonomy_status: draft
taxonomy_version: 0.4-draft
---

# SIMT Execution

An execution model in which groups of threads issue common instructions to active lanes, with divergent paths executed under lane masks and architecture-specific reconvergence.

## Browsing Home

[[02 Concepts/Stack/Hardware & Accelerators/Accelerator Architecture Subject|Accelerator Architecture]] → [[02 Concepts/Stack/Hardware & Accelerators/Hardware & Accelerators Index|Hardware & Accelerators]]

## Book Passages

These are explicitly recorded related passages from the upstream draft alignment; they do not certify complete coverage.

No explicit passage alignment is recorded for this concept. Subject reading pointers are available in its browsing home.

## Conditional Relationships

These are the taxonomy's draft editorial relationships. Read each relationship with its condition; an outgoing link is not a prerequisite claim.

- Sets the achieved fraction of, through lane masking under divergence, [[02 Concepts/Stack/Hardware & Accelerators/Compute Throughput|Compute Throughput]]. **Condition:** When threads in a warp take different control-flow paths, so masked lanes idle while each path executes in turn.

- Is a kind of [[02 Concepts/Stack/Hardware & Accelerators/Accelerator Execution Architecture|Accelerator Execution Architecture]]. **Condition:** Thread groups issue the same instruction and divergent paths serialize.

## Search Terms

Upstream search terms may be related terms rather than exact synonyms: SIMT.

## Source

[Canonical Taxonomy](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/taxonomy.yml) · [Passage Alignment](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/mlsysbook-alignment.yml)

Taxonomy definitions and relationship wording: CC BY 4.0, with attribution to the Machine Learning Systems curriculum by Vijay Janapa Reddi and contributors. The textbook retains its separate license.
