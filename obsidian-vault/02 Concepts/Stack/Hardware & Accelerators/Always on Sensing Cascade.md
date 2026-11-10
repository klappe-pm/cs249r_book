---
title: Always on Sensing Cascade
type: concept
tags:
- Type/Concept
- Group/Stack
- Topic/Edge_Embedded_Hardware
source_repository: https://github.com/klappe-pm/cs249r_book
source_commit: de87c0103806d7bfb1c677dbb77a2b92fa00c298
source_path: taxonomy/taxonomy.yml
source_label: Always-on sensing cascade
taxonomy_id: mlsys.always-on-cascade
taxonomy_status: draft
taxonomy_version: 0.4-draft
---

# Always on Sensing Cascade

Using a low-power sensing or inference stage to wake a more expensive stage only when needed, cutting continuous-monitoring energy at the risk of missed triggers and wake latency.

## Browsing Home

[[02 Concepts/Stack/Hardware & Accelerators/Edge & Embedded Hardware Subject|Edge & Embedded Hardware]] → [[02 Concepts/Stack/Hardware & Accelerators/Hardware & Accelerators Index|Hardware & Accelerators]]

## Book Passages

These are explicitly recorded related passages from the upstream draft alignment; they do not certify complete coverage.

No explicit passage alignment is recorded for this concept. Subject reading pointers are available in its browsing home.

## Conditional Relationships

These are the taxonomy's draft editorial relationships. Read each relationship with its condition; an outgoing link is not a prerequisite claim.

- Keeps the main application processor asleep until triggered using [[02 Concepts/Stack/Hardware & Accelerators/Duty Cycling and Sleep States|Duty Cycling and Sleep States]]. **Condition:** While the low-power island continuously monitors raw sensor streams.

- Applies the staged escalation of [[02 Concepts/Lifecycle/Deployment & Serving/Model Cascade|Model Cascade]]. **Condition:** When the wake-up stage is itself a small model rather than a sensing circuit.

- Rejects background frames on low-power hardware to lower the average [[02 Concepts/Qualities/Sustainability & Cost/Energy per Inference|Energy per Inference]]. **Condition:** Averaged per sensed frame over long idle intervals, not per main-model inference.

## Search Terms

Upstream search terms may be related terms rather than exact synonyms: wake-word cascade; sensor-hub gating; event-triggered inference; trigger-based inference; motion-triggered inference.

## Source

[Canonical Taxonomy](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/taxonomy.yml) · [Passage Alignment](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/mlsysbook-alignment.yml)

Taxonomy definitions and relationship wording: CC BY 4.0, with attribution to the Machine Learning Systems curriculum by Vijay Janapa Reddi and contributors. The textbook retains its separate license.
