---
title: Sensor Interconnect Bandwidth
type: concept
tags:
- Type/Concept
- Group/Stack
- Topic/Edge_Embedded_Hardware
source_repository: https://github.com/klappe-pm/cs249r_book
source_commit: de87c0103806d7bfb1c677dbb77a2b92fa00c298
source_path: taxonomy/taxonomy.yml
source_label: Sensor interconnect bandwidth
taxonomy_id: mlsys.sensor-interconnect
taxonomy_status: draft
taxonomy_version: 0.4-draft
---

# Sensor Interconnect Bandwidth

The data rate of the links that carry sensor data into an embedded processor (MIPI CSI-2 for cameras, I2S for audio, SPI and I2C for low-rate sensors), which bounds the resolution, frame rate, and number of sensors a device can ingest.

## Browsing Home

[[02 Concepts/Stack/Hardware & Accelerators/Edge & Embedded Hardware Subject|Edge & Embedded Hardware]] → [[02 Concepts/Stack/Hardware & Accelerators/Hardware & Accelerators Index|Hardware & Accelerators]]

## Book Passages

These are explicitly recorded related passages from the upstream draft alignment; they do not certify complete coverage.

No explicit passage alignment is recorded for this concept. Subject reading pointers are available in its browsing home.

## Conditional Relationships

These are the taxonomy's draft editorial relationships. Read each relationship with its condition; an outgoing link is not a prerequisite claim.

- Bounds the resolution, frame rate, and sensor count available to [[02 Concepts/System Types/Embodied & Physical Systems/Robot Perception|Robot Perception]]. **Condition:** When raw sensor data streams into the onboard processor over MIPI, I2S, or SPI links rather than being pre-processed at the sensor.

## Search Terms

Upstream search terms may be related terms rather than exact synonyms: MIPI CSI-2; I2S; SPI bandwidth; camera link bandwidth.

## Source

[Canonical Taxonomy](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/taxonomy.yml) · [Passage Alignment](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/mlsysbook-alignment.yml)

Taxonomy definitions and relationship wording: CC BY 4.0, with attribution to the Machine Learning Systems curriculum by Vijay Janapa Reddi and contributors. The textbook retains its separate license.
