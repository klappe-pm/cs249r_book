---
title: Power Delivery and Integrity
type: concept
tags:
- Type/Concept
- Group/Stack
- Topic/Chip_Power_Thermal_Limits
source_repository: https://github.com/klappe-pm/cs249r_book
source_commit: de87c0103806d7bfb1c677dbb77a2b92fa00c298
source_path: taxonomy/taxonomy.yml
source_label: Power delivery and integrity
taxonomy_id: mlsys.power-delivery
taxonomy_status: draft
taxonomy_version: 0.4-draft
---

# Power Delivery and Integrity

Supply paths, conversion stages, limits, and transient behavior that must maintain required voltages while workloads and actuators draw or return power.

## Browsing Home

[[02 Concepts/Stack/Hardware & Accelerators/Chip Power & Thermal Limits Subject|Chip Power & Thermal Limits]] → [[02 Concepts/Stack/Hardware & Accelerators/Hardware & Accelerators Index|Hardware & Accelerators]]

## Book Passages

These are explicitly recorded related passages from the upstream draft alignment; they do not certify complete coverage.

- [[01 Books/Volume IV - Physical AI/01 Machine Anatomy/02 The Physical Body/V4-02.07 Electrical Power Integrity#^sec-body-power-integrity|V4-02.07 Electrical Power Integrity]] — Supply integrity. [Exact Source Passage](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/books/vol4/02_body/02_body.qmd#L1968).

## Conditional Relationships

These are the taxonomy's draft editorial relationships. Read each relationship with its condition; an outgoing link is not a prerequisite claim.

- Constrains feasible operating points for [[02 Concepts/Stack/Hardware & Accelerators/Compute Throughput|Compute Throughput]]. **Condition:** Supply limits, voltage integrity, and platform power management can constrain sustained execution; power is distinct from energy.

- Bounds [[02 Concepts/Stack/Datacenter Infrastructure & Fleet/Rack Power Density|Rack Power Density]]. **Condition:** Facility and rack feeds, conversion stages, and breakers limit sustained draw per rack.

- Can cause, through insufficient voltage margin, [[02 Concepts/Qualities/Reliability & Fault Tolerance/Silent Data Corruption|Silent Data Corruption]]. **Condition:** Droop or marginal supply under heavy load leaves circuits below the voltage they need for correct timing.

- Sets, when a shared rail sags, the torque available within [[02 Concepts/System Types/Embodied & Physical Systems/Actuator Limits|Actuator Limits]]. **Condition:** When compute and actuators share a supply and simultaneous demand or regeneration droops the rail below the drive's operating window.

## Source

[Canonical Taxonomy](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/taxonomy.yml) · [Passage Alignment](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/mlsysbook-alignment.yml)

Taxonomy definitions and relationship wording: CC BY 4.0, with attribution to the Machine Learning Systems curriculum by Vijay Janapa Reddi and contributors. The textbook retains its separate license.
