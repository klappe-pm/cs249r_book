---
title: Matrix Engine Programming
type: concept
tags:
- Type/Concept
- Group/Stack
- Topic/Kernel_GPU_Programming_Model
source_repository: https://github.com/klappe-pm/cs249r_book
source_commit: de87c0103806d7bfb1c677dbb77a2b92fa00c298
source_path: taxonomy/taxonomy.yml
source_label: Matrix-engine programming
taxonomy_id: mlsys.matrix-engine-programming
taxonomy_status: draft
taxonomy_version: 0.4-draft
---

# Matrix Engine Programming

Issuing tile-level matrix-multiply-accumulate instructions with the layouts, fragment shapes, and precisions a tensor-core-class unit requires.

## Browsing Home

[[02 Concepts/Stack/Frameworks, Compilers & Runtimes/Kernel & GPU Programming Model Subject|Kernel & GPU Programming Model]] → [[02 Concepts/Stack/Frameworks, Compilers & Runtimes/Frameworks, Compilers & Runtimes Index|Frameworks, Compilers & Runtimes]]

## Book Passages

These are explicitly recorded related passages from the upstream draft alignment; they do not certify complete coverage.

No explicit passage alignment is recorded for this concept. Subject reading pointers are available in its browsing home.

## Conditional Relationships

These are the taxonomy's draft editorial relationships. Read each relationship with its condition; an outgoing link is not a prerequisite claim.

- Is required to reach peak [[02 Concepts/Stack/Hardware & Accelerators/Compute Throughput|Compute Throughput]]. **Condition:** Peak matrix throughput is available only to instructions with supported shapes, layouts, and precisions.

- Issues instructions to [[02 Concepts/Stack/Hardware & Accelerators/Matrix Engine|Matrix Engine]]. **Condition:** Fragments are loaded in the shapes and layouts the unit accepts.

- Requires specific operand [[02 Concepts/Stack/Frameworks, Compilers & Runtimes/Tensor Layout|Tensor Layout]]. **Condition:** Matrix instructions accept only particular fragment layouts, so data may need rearrangement.

## Search Terms

Upstream search terms may be related terms rather than exact synonyms: tensor core programming; MMA.

## Source

[Canonical Taxonomy](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/taxonomy.yml) · [Passage Alignment](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/mlsysbook-alignment.yml)

Taxonomy definitions and relationship wording: CC BY 4.0, with attribution to the Machine Learning Systems curriculum by Vijay Janapa Reddi and contributors. The textbook retains its separate license.
