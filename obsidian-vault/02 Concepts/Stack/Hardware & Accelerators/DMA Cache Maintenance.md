---
title: DMA Cache Maintenance
type: concept
tags:
- Type/Concept
- Group/Stack
- Topic/Edge_Embedded_Hardware
- Context/Background
source_repository: https://github.com/klappe-pm/cs249r_book
source_commit: de87c0103806d7bfb1c677dbb77a2b92fa00c298
source_path: taxonomy/taxonomy.yml
source_label: DMA cache maintenance
taxonomy_id: mlsys.dma-cache-maintenance
taxonomy_status: draft
taxonomy_version: 0.4-draft
---

# DMA Cache Maintenance

Cleaning and invalidating processor caches around DMA transfers on hardware without coherent DMA, with buffers aligned to cache lines, so a device and the CPU do not read stale copies of a shared buffer; each maintenance step adds latency.

## Browsing Home

[[02 Concepts/Stack/Hardware & Accelerators/Edge & Embedded Hardware Subject|Edge & Embedded Hardware]] → [[02 Concepts/Stack/Hardware & Accelerators/Hardware & Accelerators Index|Hardware & Accelerators]]

This is a background concept on which ML systems reasoning depends; that classification does not make it optional.

## Book Passages

These are explicitly recorded related passages from the upstream draft alignment; they do not certify complete coverage.

No explicit passage alignment is recorded for this concept. Subject reading pointers are available in its browsing home.

## Search Terms

Upstream search terms may be related terms rather than exact synonyms: cache clean and invalidate for DMA; DMA buffer synchronization.

## Source

[Canonical Taxonomy](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/taxonomy.yml) · [Passage Alignment](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/mlsysbook-alignment.yml)

Taxonomy definitions and relationship wording: CC BY 4.0, with attribution to the Machine Learning Systems curriculum by Vijay Janapa Reddi and contributors. The textbook retains its separate license.
