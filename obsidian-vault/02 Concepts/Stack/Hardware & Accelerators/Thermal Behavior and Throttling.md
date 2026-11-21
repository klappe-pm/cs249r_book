---
title: Thermal Behavior and Throttling
type: concept
tags:
- Type/Concept
- Group/Stack
- Topic/Chip_Power_Thermal_Limits
source_repository: https://github.com/klappe-pm/cs249r_book
source_commit: de87c0103806d7bfb1c677dbb77a2b92fa00c298
source_path: taxonomy/taxonomy.yml
source_label: Thermal behavior and throttling
taxonomy_id: mlsys.thermal-dynamics
taxonomy_status: draft
taxonomy_version: 0.4-draft
---

# Thermal Behavior and Throttling

Evolution of temperature under heat generation and removal, and the performance controls or operating restrictions that follow under a platform thermal policy.

## Browsing Home

[[02 Concepts/Stack/Hardware & Accelerators/Chip Power & Thermal Limits Subject|Chip Power & Thermal Limits]] → [[02 Concepts/Stack/Hardware & Accelerators/Hardware & Accelerators Index|Hardware & Accelerators]]

## Book Passages

These are explicitly recorded related passages from the upstream draft alignment; they do not certify complete coverage.

- [[01 Books/Volume IV - Physical AI/03 Running the Machine/13 Workload Placement/V4-13.05 Thermal and Timing Coupling#^sec-placement-thermal-timing-coupling|V4-13.05 Thermal and Timing Coupling]] — Thermal throttling. [Exact Source Passage](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/books/vol4/13_placement/13_placement.qmd#L1002).

## Conditional Relationships

These are the taxonomy's draft editorial relationships. Read each relationship with its condition; an outgoing link is not a prerequisite claim.

- Can increase [[02 Concepts/Qualities/Performance, Efficiency & Benchmarking/Execution Time|Execution Time]]. **Condition:** When thermal controls reduce frequency or service rate or suspend operation, a cold unloaded timing measurement need not characterize sustained or shared operation.

- Adds cooling overhead to [[02 Concepts/Qualities/Sustainability & Cost/Operating Energy|Operating Energy]]. **Condition:** The system boundary and cooling overhead must be stated; carbon conclusions additionally require energy mix and lifecycle assumptions.

- Throttles through [[02 Concepts/Stack/Hardware & Accelerators/Dynamic Voltage and Frequency Scaling|Dynamic Voltage and Frequency Scaling]]. **Condition:** Thermal controls lower frequency and voltage when temperature limits are approached.

- Adds, through frequency throttling, [[02 Concepts/System Types/Embodied & Physical Systems/Timing Jitter|Timing Jitter]]. **Condition:** When clock changes under thermal policy alter task completion times between periods.

- Fixes the clock and memory-timing assumptions under which a bound is a valid [[02 Concepts/System Types/Embodied & Physical Systems/Worst Case Execution Time|Worst Case Execution Time]]. **Condition:** When the bound was derived at full clock; the analysis must include the allowed throttled operating states or explicitly exclude them.

- Sets the sustained-duty component of [[02 Concepts/System Types/Embodied & Physical Systems/Actuator Limits|Actuator Limits]]. **Condition:** When motor winding temperature, not drive current, binds continuous torque; peak torque remains current-limited.

- Makes short runs overstate sustained performance, a source of [[02 Concepts/Qualities/Performance, Efficiency & Benchmarking/Performance Measurement Variability|Performance Measurement Variability]]. **Condition:** Measurement windows shorter than the device's thermal time constant.

## Source

[Canonical Taxonomy](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/taxonomy.yml) · [Passage Alignment](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/mlsysbook-alignment.yml)

Taxonomy definitions and relationship wording: CC BY 4.0, with attribution to the Machine Learning Systems curriculum by Vijay Janapa Reddi and contributors. The textbook retains its separate license.
