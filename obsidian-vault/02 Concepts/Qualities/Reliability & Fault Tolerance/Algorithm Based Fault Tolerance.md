---
title: Algorithm Based Fault Tolerance
type: concept
tags:
- Type/Concept
- Group/Qualities
- Topic/Hardware_Faults_Silent_Data_Corruption
source_repository: https://github.com/klappe-pm/cs249r_book
source_commit: de87c0103806d7bfb1c677dbb77a2b92fa00c298
source_path: taxonomy/taxonomy.yml
source_label: Algorithm-based fault tolerance
taxonomy_id: mlsys.abft
taxonomy_status: draft
taxonomy_version: 0.4-draft
---

# Algorithm Based Fault Tolerance

Detecting or correcting computational errors by carrying checksums through an algorithm, such as matrix multiplication, and verifying invariants on its outputs.

## Browsing Home

[[02 Concepts/Qualities/Reliability & Fault Tolerance/Hardware Faults & Silent Data Corruption Subject|Hardware Faults & Silent Data Corruption]] → [[02 Concepts/Qualities/Reliability & Fault Tolerance/Reliability & Fault Tolerance Index|Reliability & Fault Tolerance]]

## Book Passages

These are explicitly recorded related passages from the upstream draft alignment; they do not certify complete coverage.

No explicit passage alignment is recorded for this concept. Subject reading pointers are available in its browsing home.

## Conditional Relationships

These are the taxonomy's draft editorial relationships. Read each relationship with its condition; an outgoing link is not a prerequisite claim.

- Detects [[02 Concepts/Qualities/Reliability & Fault Tolerance/Silent Data Corruption|Silent Data Corruption]]. **Condition:** For linear-algebra operations whose input checksums predict output checksums, within the floating-point tolerance used for comparison.

- Carries checksums through [[02 Concepts/Stack/Frameworks, Compilers & Runtimes/Matrix Multiplication|Matrix Multiplication]]. **Condition:** For linear-algebra kernels whose input checksums predict output checksums.

- Adds checksum overhead to [[02 Concepts/Qualities/Performance, Efficiency & Benchmarking/Execution Time|Execution Time]]. **Condition:** The overhead is small relative to large matrix multiplications but nonzero.

## Search Terms

Upstream search terms may be related terms rather than exact synonyms: ABFT.

## Source

[Canonical Taxonomy](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/taxonomy.yml) · [Passage Alignment](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/mlsysbook-alignment.yml)

Taxonomy definitions and relationship wording: CC BY 4.0, with attribution to the Machine Learning Systems curriculum by Vijay Janapa Reddi and contributors. The textbook retains its separate license.
