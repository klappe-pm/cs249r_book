---
title: Power Usage Effectiveness
type: concept
tags:
- Type/Concept
- Group/Stack
- Topic/Datacenter_Power_Cooling_Facilities
- Context/Background
source_repository: https://github.com/klappe-pm/cs249r_book
source_commit: de87c0103806d7bfb1c677dbb77a2b92fa00c298
source_path: taxonomy/taxonomy.yml
source_label: Power usage effectiveness
taxonomy_id: mlsys.pue
taxonomy_status: draft
taxonomy_version: 0.4-draft
---

# Power Usage Effectiveness

Total facility energy divided by IT equipment energy, measuring overhead from cooling, power conversion, and other non-compute loads.

## Browsing Home

[[02 Concepts/Stack/Datacenter Infrastructure & Fleet/Datacenter Power, Cooling & Facilities Subject|Datacenter Power, Cooling & Facilities]] → [[02 Concepts/Stack/Datacenter Infrastructure & Fleet/Datacenter Infrastructure & Fleet Index|Datacenter Infrastructure & Fleet]]

This is a background concept on which ML systems reasoning depends; that classification does not make it optional.

## Book Passages

These are explicitly recorded related passages from the upstream draft alignment; they do not certify complete coverage.

- [[01 Books/Volume II - Scaling/04 The Responsible Fleet/15 Sustainable AI/V2-15.06 Carbon Footprint Calculation#^sec-sustainable-ai-operational-carbon-calculation-4627-calculation-4627|V2-15.06 Carbon Footprint Calculation]] — Operational carbon. [Exact Source Passage](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/books/vol2/15_sustainable_ai/15_sustainable_ai.qmd#L2437).

## Conditional Relationships

These are the taxonomy's draft editorial relationships. Read each relationship with its condition; an outgoing link is not a prerequisite claim.

- Scales IT energy to facility energy in [[02 Concepts/Qualities/Sustainability & Cost/Operating Energy|Operating Energy]]. **Condition:** The accounting boundary includes facility overheads.

- Measures facility overhead of [[02 Concepts/Stack/Datacenter Infrastructure & Fleet/Warehouse Scale Computer|Warehouse Scale Computer]]. **Condition:** IT and total facility energy are metered over the same period.

- Multiplies IT energy into [[02 Concepts/Qualities/Sustainability & Cost/Operational Carbon|Operational Carbon]]. **Condition:** Facility overhead for cooling and power conversion scales IT energy by PUE before carbon intensity applies.

## Search Terms

Upstream search terms may be related terms rather than exact synonyms: PUE.

## Source

[Canonical Taxonomy](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/taxonomy.yml) · [Passage Alignment](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/mlsysbook-alignment.yml)

Taxonomy definitions and relationship wording: CC BY 4.0, with attribution to the Machine Learning Systems curriculum by Vijay Janapa Reddi and contributors. The textbook retains its separate license.
