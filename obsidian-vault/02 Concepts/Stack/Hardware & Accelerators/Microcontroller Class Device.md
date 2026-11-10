---
title: Microcontroller Class Device
type: concept
tags:
- Type/Concept
- Group/Stack
- Topic/Edge_Embedded_Hardware
source_repository: https://github.com/klappe-pm/cs249r_book
source_commit: de87c0103806d7bfb1c677dbb77a2b92fa00c298
source_path: taxonomy/taxonomy.yml
source_label: Microcontroller-class device
taxonomy_id: mlsys.microcontroller
taxonomy_status: draft
taxonomy_version: 0.4-draft
---

# Microcontroller Class Device

A low-power processor with on-chip flash and kilobytes to a few megabytes of SRAM, typically without an operating system or virtual memory.

## Browsing Home

[[02 Concepts/Stack/Hardware & Accelerators/Edge & Embedded Hardware Subject|Edge & Embedded Hardware]] → [[02 Concepts/Stack/Hardware & Accelerators/Hardware & Accelerators Index|Hardware & Accelerators]]

## Book Passages

These are explicitly recorded related passages from the upstream draft alignment; they do not certify complete coverage.

No explicit passage alignment is recorded for this concept. Subject reading pointers are available in its browsing home.

## Conditional Relationships

These are the taxonomy's draft editorial relationships. Read each relationship with its condition; an outgoing link is not a prerequisite claim.

- Imposes [[02 Concepts/Stack/Hardware & Accelerators/On Device Memory Budget|On Device Memory Budget]]. **Condition:** Weights and activations must fit in on-chip flash and SRAM.

- Runs models through a lightweight [[02 Concepts/Lifecycle/Deployment & Serving/On Device Inference Runtime|On Device Inference Runtime]]. **Condition:** No operating system or virtual memory is available, so the runtime is statically linked and memory-planned.

- Runs models whose weights exceed on-chip SRAM via [[02 Concepts/Stack/Hardware & Accelerators/Execute in Place Weights|Execute in Place Weights]]. **Condition:** On microcontrollers whose flash is memory-mapped onto the processor bus.

## Search Terms

Upstream search terms may be related terms rather than exact synonyms: MCU; TinyML device.

## Source

[Canonical Taxonomy](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/taxonomy.yml) · [Passage Alignment](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/mlsysbook-alignment.yml)

Taxonomy definitions and relationship wording: CC BY 4.0, with attribution to the Machine Learning Systems curriculum by Vijay Janapa Reddi and contributors. The textbook retains its separate license.
