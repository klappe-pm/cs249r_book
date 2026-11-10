---
title: Sharding Annotation and Propagation
type: concept
tags:
- Type/Concept
- Group/Stack
- Topic/Parallelization_Planning_Placement
source_repository: https://github.com/klappe-pm/cs249r_book
source_commit: de87c0103806d7bfb1c677dbb77a2b92fa00c298
source_path: taxonomy/taxonomy.yml
source_label: Sharding annotation and propagation
taxonomy_id: mlsys.sharding-propagation
taxonomy_status: draft
taxonomy_version: 0.4-draft
---

# Sharding Annotation and Propagation

Annotating a few tensors with layouts over a device mesh and letting the compiler infer the remaining layouts and insert required collectives, yielding one SPMD program.

## Browsing Home

[[02 Concepts/Stack/Parallelism & Distributed Execution/Parallelization Planning & Placement Subject|Parallelization Planning & Placement]] → [[02 Concepts/Stack/Parallelism & Distributed Execution/Parallelism & Distributed Execution Index|Parallelism & Distributed Execution]]

## Book Passages

These are explicitly recorded related passages from the upstream draft alignment; they do not certify complete coverage.

No explicit passage alignment is recorded for this concept. Subject reading pointers are available in its browsing home.

## Conditional Relationships

These are the taxonomy's draft editorial relationships. Read each relationship with its condition; an outgoing link is not a prerequisite claim.

- Implements [[02 Concepts/Stack/Parallelism & Distributed Execution/Automatic Parallelization|Automatic Parallelization]]. **Condition:** Holds when users supply seed annotations and the compiler propagates layouts through operators with known sharding rules.

- Inserts [[02 Concepts/Stack/Parallelism & Distributed Execution/Collective Communication|Collective Communication]]. **Condition:** Collectives are inserted wherever an operator's input layouts differ from what its sharded implementation requires.

- Is defined over the axes of [[02 Concepts/Stack/Parallelism & Distributed Execution/Device Mesh|Device Mesh]]. **Condition:** Tensor dimensions are sharded over named mesh axes, so mesh shape bounds which layouts are expressible.

- Propagates layouts through [[02 Concepts/Stack/Frameworks, Compilers & Runtimes/ML Compiler IR|ML Compiler IR]]. **Condition:** Sharding annotations are attached to operations in the compiler IR.

## Search Terms

Upstream search terms may be related terms rather than exact synonyms: SPMD partitioning; GSPMD-style sharding.

## Source

[Canonical Taxonomy](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/taxonomy.yml) · [Passage Alignment](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/mlsysbook-alignment.yml)

Taxonomy definitions and relationship wording: CC BY 4.0, with attribution to the Machine Learning Systems curriculum by Vijay Janapa Reddi and contributors. The textbook retains its separate license.
