---
title: Forward Error Correction
type: concept
tags:
- Type/Concept
- Group/Stack
- Topic/Network_Fabrics
- Context/Background
source_repository: https://github.com/klappe-pm/cs249r_book
source_commit: de87c0103806d7bfb1c677dbb77a2b92fa00c298
source_path: taxonomy/taxonomy.yml
source_label: Forward error correction
taxonomy_id: mlsys.forward-error-correction
taxonomy_status: draft
taxonomy_version: 0.4-draft
---

# Forward Error Correction

Adding redundant bits to transmitted data so the receiver corrects supported error patterns without retransmission, at the cost of coding overhead and decoding delay.

## Browsing Home

[[02 Concepts/Stack/Datacenter Infrastructure & Fleet/Network Fabrics Subject|Network Fabrics]] → [[02 Concepts/Stack/Datacenter Infrastructure & Fleet/Datacenter Infrastructure & Fleet Index|Datacenter Infrastructure & Fleet]]

This is a background concept on which ML systems reasoning depends; that classification does not make it optional.

## Book Passages

These are explicitly recorded related passages from the upstream draft alignment; they do not certify complete coverage.

No explicit passage alignment is recorded for this concept. Subject reading pointers are available in its browsing home.

## Conditional Relationships

These are the taxonomy's draft editorial relationships. Read each relationship with its condition; an outgoing link is not a prerequisite claim.

- Corrects bit errors on the links of [[02 Concepts/Stack/Hardware & Accelerators/Scale Up Interconnect|Scale Up Interconnect]]. **Condition:** When high-speed SerDes links run a FEC code on every hop, adding decoding delay to each.

- Absorbs, within its correction capability, the raw errors of [[02 Concepts/Stack/Datacenter Infrastructure & Fleet/Link Signal Degradation and Flaps|Link Signal Degradation and Flaps]]. **Condition:** When the error rate stays within the code's correction budget.

## Search Terms

Upstream search terms may be related terms rather than exact synonyms: FEC; link-layer FEC.

## Source

[Canonical Taxonomy](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/taxonomy.yml) · [Passage Alignment](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/mlsysbook-alignment.yml)

Taxonomy definitions and relationship wording: CC BY 4.0, with attribution to the Machine Learning Systems curriculum by Vijay Janapa Reddi and contributors. The textbook retains its separate license.
