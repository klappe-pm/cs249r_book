---
title: Dynamic Voltage and Frequency Scaling
type: concept
tags:
- Type/Concept
- Group/Stack
- Topic/Chip_Power_Thermal_Limits
- Context/Background
source_repository: https://github.com/klappe-pm/cs249r_book
source_commit: de87c0103806d7bfb1c677dbb77a2b92fa00c298
source_path: taxonomy/taxonomy.yml
source_label: Dynamic voltage and frequency scaling
taxonomy_id: mlsys.dvfs
taxonomy_status: draft
taxonomy_version: 0.4-draft
---

# Dynamic Voltage and Frequency Scaling

Adjusting supply voltage and clock frequency at runtime to trade performance for power, since dynamic power grows superlinearly with voltage.

## Browsing Home

[[02 Concepts/Stack/Hardware & Accelerators/Chip Power & Thermal Limits Subject|Chip Power & Thermal Limits]] → [[02 Concepts/Stack/Hardware & Accelerators/Hardware & Accelerators Index|Hardware & Accelerators]]

This is a background concept on which ML systems reasoning depends; that classification does not make it optional.

## Book Passages

These are explicitly recorded related passages from the upstream draft alignment; they do not certify complete coverage.

No explicit passage alignment is recorded for this concept. Subject reading pointers are available in its browsing home.

## Conditional Relationships

These are the taxonomy's draft editorial relationships. Read each relationship with its condition; an outgoing link is not a prerequisite claim.

- Can reduce, at some cost in speed, [[02 Concepts/Qualities/Sustainability & Cost/Operating Energy|Operating Energy]]. **Condition:** Workload phases tolerate lower clocks, such as memory-bound phases.

## Search Terms

Upstream search terms may be related terms rather than exact synonyms: DVFS.

## Source

[Canonical Taxonomy](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/taxonomy.yml) · [Passage Alignment](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/mlsysbook-alignment.yml)

Taxonomy definitions and relationship wording: CC BY 4.0, with attribution to the Machine Learning Systems curriculum by Vijay Janapa Reddi and contributors. The textbook retains its separate license.
