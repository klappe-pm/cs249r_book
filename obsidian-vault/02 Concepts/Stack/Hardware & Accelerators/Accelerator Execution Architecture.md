---
title: Accelerator Execution Architecture
type: concept
tags:
- Type/Concept
- Group/Stack
- Topic/Accelerator_Architecture
source_repository: https://github.com/klappe-pm/cs249r_book
source_commit: de87c0103806d7bfb1c677dbb77a2b92fa00c298
source_path: taxonomy/taxonomy.yml
source_label: Accelerator execution architecture
taxonomy_id: mlsys.accelerator-execution-architecture
taxonomy_status: draft
taxonomy_version: 0.4-draft
---

# Accelerator Execution Architecture

Organization of arithmetic units, execution lanes or threads, scheduling resources, and local storage that determines how supported operations run. SIMD/SIMT, matrix units, and systolic arrays are distinct examples.

## Browsing Home

[[02 Concepts/Stack/Hardware & Accelerators/Accelerator Architecture Subject|Accelerator Architecture]] → [[02 Concepts/Stack/Hardware & Accelerators/Hardware & Accelerators Index|Hardware & Accelerators]]

## Book Passages

These are explicitly recorded related passages from the upstream draft alignment; they do not certify complete coverage.

No explicit passage alignment is recorded for this concept. Subject reading pointers are available in its browsing home.

## Conditional Relationships

These are the taxonomy's draft editorial relationships. Read each relationship with its condition; an outgoing link is not a prerequisite claim.

- Constrains supported mappings of [[02 Concepts/Stack/Frameworks, Compilers & Runtimes/Matrix Multiplication|Matrix Multiplication]]. **Condition:** Operations, data types, shapes, and implementation must match the execution resources; peak throughput is not achieved throughput.

## Search Terms

Upstream search terms may be related terms rather than exact synonyms: GPU architecture; streaming multiprocessor; SM.

## Source

[Canonical Taxonomy](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/taxonomy.yml) · [Passage Alignment](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/mlsysbook-alignment.yml)

Taxonomy definitions and relationship wording: CC BY 4.0, with attribution to the Machine Learning Systems curriculum by Vijay Janapa Reddi and contributors. The textbook retains its separate license.
