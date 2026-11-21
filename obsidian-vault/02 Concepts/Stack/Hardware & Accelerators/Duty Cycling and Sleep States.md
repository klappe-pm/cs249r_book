---
title: Duty Cycling and Sleep States
type: concept
tags:
- Type/Concept
- Group/Stack
- Topic/Chip_Power_Thermal_Limits
source_repository: https://github.com/klappe-pm/cs249r_book
source_commit: de87c0103806d7bfb1c677dbb77a2b92fa00c298
source_path: taxonomy/taxonomy.yml
source_label: Duty cycling and sleep states
taxonomy_id: mlsys.duty-cycling
taxonomy_status: draft
taxonomy_version: 0.4-draft
---

# Duty Cycling and Sleep States

Keeping a device in a low-power sleep state most of the time and waking it briefly to sense and infer, so average power is set by the active fraction and the cost of each wake-up.

## Browsing Home

[[02 Concepts/Stack/Hardware & Accelerators/Chip Power & Thermal Limits Subject|Chip Power & Thermal Limits]] → [[02 Concepts/Stack/Hardware & Accelerators/Hardware & Accelerators Index|Hardware & Accelerators]]

## Book Passages

These are explicitly recorded related passages from the upstream draft alignment; they do not certify complete coverage.

No explicit passage alignment is recorded for this concept. Subject reading pointers are available in its browsing home.

## Conditional Relationships

These are the taxonomy's draft editorial relationships. Read each relationship with its condition; an outgoing link is not a prerequisite claim.

- Exploits the gap between [[02 Concepts/Qualities/Sustainability & Cost/Idle vs. Dynamic Power|Idle vs. Dynamic Power]]. **Condition:** Sleep power is far below active power.

- Cuts average [[02 Concepts/Qualities/Sustainability & Cost/Operating Energy|Operating Energy]]. **Condition:** Sensing and inference are needed only intermittently.

- Lowers average power to limit the heating behind [[02 Concepts/Stack/Hardware & Accelerators/Thermal Behavior and Throttling|Thermal Behavior and Throttling]]. **Condition:** When average power, not peak power, sets the device's sustained temperature.

## Search Terms

Upstream search terms may be related terms rather than exact synonyms: duty cycle; sleep modes; active and sleep power states; low-power modes.

## Source

[Canonical Taxonomy](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/taxonomy.yml) · [Passage Alignment](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/mlsysbook-alignment.yml)

Taxonomy definitions and relationship wording: CC BY 4.0, with attribution to the Machine Learning Systems curriculum by Vijay Janapa Reddi and contributors. The textbook retains its separate license.
