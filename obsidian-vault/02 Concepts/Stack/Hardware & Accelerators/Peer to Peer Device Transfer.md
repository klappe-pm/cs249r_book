---
title: Peer to Peer Device Transfer
type: concept
tags:
- Type/Concept
- Group/Stack
- Topic/Host_Device_Scale_Up_Interconnect
source_repository: https://github.com/klappe-pm/cs249r_book
source_commit: de87c0103806d7bfb1c677dbb77a2b92fa00c298
source_path: taxonomy/taxonomy.yml
source_label: Peer-to-peer device transfer
taxonomy_id: mlsys.peer-to-peer-transfer
taxonomy_status: draft
taxonomy_version: 0.4-draft
---

# Peer to Peer Device Transfer

Direct memory access between accelerators, or between accelerators and NICs or storage, without staging data through host memory.

## Browsing Home

[[02 Concepts/Stack/Hardware & Accelerators/Host Device & Scale Up Interconnect Subject|Host Device & Scale Up Interconnect]] → [[02 Concepts/Stack/Hardware & Accelerators/Hardware & Accelerators Index|Hardware & Accelerators]]

## Book Passages

These are explicitly recorded related passages from the upstream draft alignment; they do not certify complete coverage.

No explicit passage alignment is recorded for this concept. Subject reading pointers are available in its browsing home.

## Conditional Relationships

These are the taxonomy's draft editorial relationships. Read each relationship with its condition; an outgoing link is not a prerequisite claim.

- Bypasses host staging on [[02 Concepts/Stack/Hardware & Accelerators/Host Device Interconnect|Host Device Interconnect]]. **Condition:** Devices, drivers, and topology support direct transfers.

- Moves data between accelerators over [[02 Concepts/Stack/Hardware & Accelerators/Scale Up Interconnect|Scale Up Interconnect]]. **Condition:** When transfers are carried by dedicated accelerator-to-accelerator scale-up links rather than over the host link.

## Search Terms

Upstream search terms may be related terms rather than exact synonyms: GPUDirect.

## Source

[Canonical Taxonomy](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/taxonomy.yml) · [Passage Alignment](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/mlsysbook-alignment.yml)

Taxonomy definitions and relationship wording: CC BY 4.0, with attribution to the Machine Learning Systems curriculum by Vijay Janapa Reddi and contributors. The textbook retains its separate license.
