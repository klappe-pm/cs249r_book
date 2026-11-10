---
title: Compute in Memory
type: concept
tags:
- Type/Concept
- Group/Stack
- Topic/Accelerator_Architecture
source_repository: https://github.com/klappe-pm/cs249r_book
source_commit: de87c0103806d7bfb1c677dbb77a2b92fa00c298
source_path: taxonomy/taxonomy.yml
source_label: Compute-in-memory
taxonomy_id: mlsys.compute-in-memory
taxonomy_status: draft
taxonomy_version: 0.4-draft
---

# Compute in Memory

Performing matrix-vector operations inside or beside memory arrays, often in the analog domain, so weights need not move to separate compute units.

## Browsing Home

[[02 Concepts/Stack/Hardware & Accelerators/Accelerator Architecture Subject|Accelerator Architecture]] → [[02 Concepts/Stack/Hardware & Accelerators/Hardware & Accelerators Index|Hardware & Accelerators]]

## Book Passages

These are explicitly recorded related passages from the upstream draft alignment; they do not certify complete coverage.

No explicit passage alignment is recorded for this concept. Subject reading pointers are available in its browsing home.

## Conditional Relationships

These are the taxonomy's draft editorial relationships. Read each relationship with its condition; an outgoing link is not a prerequisite claim.

- Lowers by computing where weights are stored [[02 Concepts/Foundations/Quantitative System Models/Data Movement Energy|Data Movement Energy]]. **Condition:** Weight-stationary matrix-vector workloads whose weights fit in the memory arrays.

- Caps the effective bit width of [[02 Concepts/Stack/Frameworks, Compilers & Runtimes/Numerical Precision|Numerical Precision]]. **Condition:** Analog implementations, where device noise, drift, and converter resolution bound precision.

## Search Terms

Upstream search terms may be related terms rather than exact synonyms: in-memory computing; processing-in-memory; PIM; analog in-memory computing.

## Source

[Canonical Taxonomy](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/taxonomy.yml) · [Passage Alignment](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/mlsysbook-alignment.yml)

Taxonomy definitions and relationship wording: CC BY 4.0, with attribution to the Machine Learning Systems curriculum by Vijay Janapa Reddi and contributors. The textbook retains its separate license.
