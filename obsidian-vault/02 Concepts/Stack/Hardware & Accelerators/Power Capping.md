---
title: Power Capping
type: concept
tags:
- Type/Concept
- Group/Stack
- Topic/Chip_Power_Thermal_Limits
source_repository: https://github.com/klappe-pm/cs249r_book
source_commit: de87c0103806d7bfb1c677dbb77a2b92fa00c298
source_path: taxonomy/taxonomy.yml
source_label: Power capping
taxonomy_id: mlsys.power-capping
taxonomy_status: draft
taxonomy_version: 0.4-draft
---

# Power Capping

Enforcing a maximum power draw on a device or group by limiting clocks or activity, trading peak throughput for bounded power.

## Browsing Home

[[02 Concepts/Stack/Hardware & Accelerators/Chip Power & Thermal Limits Subject|Chip Power & Thermal Limits]] → [[02 Concepts/Stack/Hardware & Accelerators/Hardware & Accelerators Index|Hardware & Accelerators]]

## Book Passages

These are explicitly recorded related passages from the upstream draft alignment; they do not certify complete coverage.

No explicit passage alignment is recorded for this concept. Subject reading pointers are available in its browsing home.

## Conditional Relationships

These are the taxonomy's draft editorial relationships. Read each relationship with its condition; an outgoing link is not a prerequisite claim.

- Can lower [[02 Concepts/Stack/Hardware & Accelerators/Compute Throughput|Compute Throughput]]. **Condition:** The cap binds below the power the workload would otherwise draw.

- Enforces caps through [[02 Concepts/Stack/Hardware & Accelerators/Dynamic Voltage and Frequency Scaling|Dynamic Voltage and Frequency Scaling]]. **Condition:** The device lowers clocks and voltage when measured power exceeds the cap.

- Smooths [[02 Concepts/Stack/Datacenter Infrastructure & Fleet/Synchronous Training Power Swings|Synchronous Training Power Swings]]. **Condition:** Device power caps and floors applied to bound ramp rates.

## Source

[Canonical Taxonomy](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/taxonomy.yml) · [Passage Alignment](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/mlsysbook-alignment.yml)

Taxonomy definitions and relationship wording: CC BY 4.0, with attribution to the Machine Learning Systems curriculum by Vijay Janapa Reddi and contributors. The textbook retains its separate license.
