---
title: Technology Scaling
type: concept
tags:
- Type/Concept
- Group/Stack
- Topic/Chip_Power_Thermal_Limits
- Context/Background
source_repository: https://github.com/klappe-pm/cs249r_book
source_commit: de87c0103806d7bfb1c677dbb77a2b92fa00c298
source_path: taxonomy/taxonomy.yml
source_label: Technology scaling
taxonomy_id: mlsys.technology-scaling
taxonomy_status: draft
taxonomy_version: 0.4-draft
---

# Technology Scaling

The historical trends by which transistor density doubled on a steady cadence while, for a long period, power density stayed constant as transistors shrank; the end of constant power density is why added transistors can no longer all be clocked at once, pushing designs toward parallelism and specialization.

## Browsing Home

[[02 Concepts/Stack/Hardware & Accelerators/Chip Power & Thermal Limits Subject|Chip Power & Thermal Limits]] → [[02 Concepts/Stack/Hardware & Accelerators/Hardware & Accelerators Index|Hardware & Accelerators]]

This is a background concept on which ML systems reasoning depends; that classification does not make it optional.

## Book Passages

These are explicitly recorded related passages from the upstream draft alignment; they do not certify complete coverage.

No explicit passage alignment is recorded for this concept. Subject reading pointers are available in its browsing home.

## Conditional Relationships

These are the taxonomy's draft editorial relationships. Read each relationship with its condition; an outgoing link is not a prerequisite claim.

- Produces, once constant power density ends, [[02 Concepts/Stack/Hardware & Accelerators/Dark Silicon|Dark Silicon]]. **Condition:** When transistor count keeps growing but power density no longer falls with feature size.

- Constrains, once power density stops falling, per-chip gains in [[02 Concepts/Stack/Hardware & Accelerators/Compute Throughput|Compute Throughput]]. **Condition:** When transistor-density gains lack corresponding voltage and power improvements, so a fixed power budget prevents all added arithmetic units from operating at once at the intended clock rate.

## Search Terms

Upstream search terms may be related terms rather than exact synonyms: Moore's law; Dennard scaling; end of Dennard scaling; transistor scaling.

## Source

[Canonical Taxonomy](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/taxonomy.yml) · [Passage Alignment](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/mlsysbook-alignment.yml)

Taxonomy definitions and relationship wording: CC BY 4.0, with attribution to the Machine Learning Systems curriculum by Vijay Janapa Reddi and contributors. The textbook retains its separate license.
