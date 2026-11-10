---
title: Power Oversubscription
type: concept
tags:
- Type/Concept
- Group/Stack
- Topic/Datacenter_Power_Cooling_Facilities
- Context/Background
source_repository: https://github.com/klappe-pm/cs249r_book
source_commit: de87c0103806d7bfb1c677dbb77a2b92fa00c298
source_path: taxonomy/taxonomy.yml
source_label: Power oversubscription
taxonomy_id: mlsys.power-oversubscription
taxonomy_status: draft
taxonomy_version: 0.4-draft
---

# Power Oversubscription

Deploying more equipment than the sum of nameplate power a feed supports, relying on non-coincident peaks and power capping to stay within limits.

## Browsing Home

[[02 Concepts/Stack/Datacenter Infrastructure & Fleet/Datacenter Power, Cooling & Facilities Subject|Datacenter Power, Cooling & Facilities]] → [[02 Concepts/Stack/Datacenter Infrastructure & Fleet/Datacenter Infrastructure & Fleet Index|Datacenter Infrastructure & Fleet]]

This is a background concept on which ML systems reasoning depends; that classification does not make it optional.

## Book Passages

These are explicitly recorded related passages from the upstream draft alignment; they do not certify complete coverage.

No explicit passage alignment is recorded for this concept. Subject reading pointers are available in its browsing home.

## Conditional Relationships

These are the taxonomy's draft editorial relationships. Read each relationship with its condition; an outgoing link is not a prerequisite claim.

- Relies on [[02 Concepts/Stack/Hardware & Accelerators/Power Capping|Power Capping]]. **Condition:** Simultaneous peaks across equipment are rare but must be bounded when they occur.

- Reduces [[02 Concepts/Qualities/Sustainability & Cost/Total Cost of Ownership|Total Cost of Ownership]]. **Condition:** More servers share provisioned power capacity because their peaks rarely coincide.

## Source

[Canonical Taxonomy](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/taxonomy.yml) · [Passage Alignment](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/mlsysbook-alignment.yml)

Taxonomy definitions and relationship wording: CC BY 4.0, with attribution to the Machine Learning Systems curriculum by Vijay Janapa Reddi and contributors. The textbook retains its separate license.
