---
title: Flash Write Endurance
type: concept
tags:
- Type/Concept
- Group/Qualities
- Topic/Hardware_Faults_Silent_Data_Corruption
source_repository: https://github.com/klappe-pm/cs249r_book
source_commit: de87c0103806d7bfb1c677dbb77a2b92fa00c298
source_path: taxonomy/taxonomy.yml
source_label: Flash write endurance
taxonomy_id: mlsys.flash-endurance
taxonomy_status: draft
taxonomy_version: 0.4-draft
---

# Flash Write Endurance

Flash memory cells wear out after a limited number of program and erase cycles, which bounds how often embedded and edge devices can write logs, checkpoints, or model updates; wear leveling spreads writes to extend life.

## Browsing Home

[[02 Concepts/Qualities/Reliability & Fault Tolerance/Hardware Faults & Silent Data Corruption Subject|Hardware Faults & Silent Data Corruption]] → [[02 Concepts/Qualities/Reliability & Fault Tolerance/Reliability & Fault Tolerance Index|Reliability & Fault Tolerance]]

## Book Passages

These are explicitly recorded related passages from the upstream draft alignment; they do not certify complete coverage.

No explicit passage alignment is recorded for this concept. Subject reading pointers are available in its browsing home.

## Conditional Relationships

These are the taxonomy's draft editorial relationships. Read each relationship with its condition; an outgoing link is not a prerequisite claim.

- Bounds the frequency of [[02 Concepts/Lifecycle/Deployment & Serving/Over the Air Model Update|Over the Air Model Update]]. **Condition:** Updates and logs are written to on-device flash.

- Limits the write budget of [[02 Concepts/Stack/Hardware & Accelerators/Microcontroller Class Device|Microcontroller Class Device]]. **Condition:** The device stores weights and data in flash.

## Search Terms

Upstream search terms may be related terms rather than exact synonyms: flash wear-out; wear leveling; program/erase cycles.

## Source

[Canonical Taxonomy](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/taxonomy.yml) · [Passage Alignment](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/mlsysbook-alignment.yml)

Taxonomy definitions and relationship wording: CC BY 4.0, with attribution to the Machine Learning Systems curriculum by Vijay Janapa Reddi and contributors. The textbook retains its separate license.
