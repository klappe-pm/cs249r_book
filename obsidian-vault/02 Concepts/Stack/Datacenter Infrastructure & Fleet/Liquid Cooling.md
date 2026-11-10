---
title: Liquid Cooling
type: concept
tags:
- Type/Concept
- Group/Stack
- Topic/Datacenter_Power_Cooling_Facilities
- Context/Background
source_repository: https://github.com/klappe-pm/cs249r_book
source_commit: de87c0103806d7bfb1c677dbb77a2b92fa00c298
source_path: taxonomy/taxonomy.yml
source_label: Liquid cooling
taxonomy_id: mlsys.liquid-cooling
taxonomy_status: draft
taxonomy_version: 0.4-draft
---

# Liquid Cooling

Removing heat with liquid through cold plates or immersion, enabling rack power densities beyond the practical limits of air cooling.

## Browsing Home

[[02 Concepts/Stack/Datacenter Infrastructure & Fleet/Datacenter Power, Cooling & Facilities Subject|Datacenter Power, Cooling & Facilities]] → [[02 Concepts/Stack/Datacenter Infrastructure & Fleet/Datacenter Infrastructure & Fleet Index|Datacenter Infrastructure & Fleet]]

This is a background concept on which ML systems reasoning depends; that classification does not make it optional.

## Book Passages

These are explicitly recorded related passages from the upstream draft alignment; they do not certify complete coverage.

No explicit passage alignment is recorded for this concept. Subject reading pointers are available in its browsing home.

## Conditional Relationships

These are the taxonomy's draft editorial relationships. Read each relationship with its condition; an outgoing link is not a prerequisite claim.

- Raises the feasible [[02 Concepts/Stack/Datacenter Infrastructure & Fleet/Rack Power Density|Rack Power Density]]. **Condition:** When air cooling cannot remove the heat generated at the target density.

- Can reduce [[02 Concepts/Stack/Datacenter Infrastructure & Fleet/Power Usage Effectiveness|Power Usage Effectiveness]]. **Condition:** Cooling energy is a large share of facility overhead and liquid loops need less fan and chiller work.

- Mitigates throttling in [[02 Concepts/Stack/Hardware & Accelerators/Thermal Behavior and Throttling|Thermal Behavior and Throttling]]. **Condition:** Air cooling cannot hold chips below their thermal limits at the target power.

## Source

[Canonical Taxonomy](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/taxonomy.yml) · [Passage Alignment](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/mlsysbook-alignment.yml)

Taxonomy definitions and relationship wording: CC BY 4.0, with attribution to the Machine Learning Systems curriculum by Vijay Janapa Reddi and contributors. The textbook retains its separate license.
