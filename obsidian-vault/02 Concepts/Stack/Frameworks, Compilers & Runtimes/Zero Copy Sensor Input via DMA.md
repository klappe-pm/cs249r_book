---
title: Zero Copy Sensor Input via DMA
type: concept
tags:
- Type/Concept
- Group/Stack
- Topic/Data_Loading_Input_Pipelines
source_repository: https://github.com/klappe-pm/cs249r_book
source_commit: de87c0103806d7bfb1c677dbb77a2b92fa00c298
source_path: taxonomy/taxonomy.yml
source_label: Zero-copy sensor input via DMA
taxonomy_id: mlsys.zero-copy-dma
taxonomy_status: draft
taxonomy_version: 0.4-draft
---

# Zero Copy Sensor Input via DMA

Having sensors or peripherals write input directly into model input buffers by direct memory access, avoiding CPU copies between capture and inference.

## Browsing Home

[[02 Concepts/Stack/Frameworks, Compilers & Runtimes/Data Loading & Input Pipelines Subject|Data Loading & Input Pipelines]] → [[02 Concepts/Stack/Frameworks, Compilers & Runtimes/Frameworks, Compilers & Runtimes Index|Frameworks, Compilers & Runtimes]]

## Book Passages

These are explicitly recorded related passages from the upstream draft alignment; they do not certify complete coverage.

No explicit passage alignment is recorded for this concept. Subject reading pointers are available in its browsing home.

## Conditional Relationships

These are the taxonomy's draft editorial relationships. Read each relationship with its condition; an outgoing link is not a prerequisite claim.

- Removes copy time from [[02 Concepts/System Types/Embodied & Physical Systems/Feedback Delay|Feedback Delay]]. **Condition:** Sensor data feeds a latency-critical loop.

- Moves data arriving over [[02 Concepts/Stack/Hardware & Accelerators/Sensor Interconnect Bandwidth|Sensor Interconnect Bandwidth]]. **Condition:** The peripheral supports direct memory access.

- Stays correct on non-coherent hardware only with [[02 Concepts/Stack/Hardware & Accelerators/DMA Cache Maintenance|DMA Cache Maintenance]]. **Condition:** When the CPU accesses cached buffers that a sensor or accelerator also accesses by DMA without hardware coherence.

## Search Terms

Upstream search terms may be related terms rather than exact synonyms: DMA input buffers; zero-copy capture.

## Source

[Canonical Taxonomy](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/taxonomy.yml) · [Passage Alignment](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/mlsysbook-alignment.yml)

Taxonomy definitions and relationship wording: CC BY 4.0, with attribution to the Machine Learning Systems curriculum by Vijay Janapa Reddi and contributors. The textbook retains its separate license.
