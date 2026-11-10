---
title: Energy Harvesting Intermittent Computing
type: concept
tags:
- Type/Concept
- Group/Stack
- Topic/Edge_Embedded_Hardware
source_repository: https://github.com/klappe-pm/cs249r_book
source_commit: de87c0103806d7bfb1c677dbb77a2b92fa00c298
source_path: taxonomy/taxonomy.yml
source_label: Energy-harvesting intermittent computing
taxonomy_id: mlsys.intermittent-computing
taxonomy_status: draft
taxonomy_version: 0.4-draft
---

# Energy Harvesting Intermittent Computing

Running inference on devices powered by harvested energy that lose power unpredictably, which requires checkpointing progress to nonvolatile memory so computation resumes rather than restarts.

## Browsing Home

[[02 Concepts/Stack/Hardware & Accelerators/Edge & Embedded Hardware Subject|Edge & Embedded Hardware]] → [[02 Concepts/Stack/Hardware & Accelerators/Hardware & Accelerators Index|Hardware & Accelerators]]

## Book Passages

These are explicitly recorded related passages from the upstream draft alignment; they do not certify complete coverage.

No explicit passage alignment is recorded for this concept. Subject reading pointers are available in its browsing home.

## Conditional Relationships

These are the taxonomy's draft editorial relationships. Read each relationship with its condition; an outgoing link is not a prerequisite claim.

- Typically runs on [[02 Concepts/Stack/Hardware & Accelerators/Microcontroller Class Device|Microcontroller Class Device]]. **Condition:** On energy-harvesting deployments built around microcontroller-class processors.

- Requires fine-grained [[02 Concepts/Qualities/Reliability & Fault Tolerance/Recovery Checkpoint|Recovery Checkpoint]]. **Condition:** Power can fail mid-inference.

## Search Terms

Upstream search terms may be related terms rather than exact synonyms: energy harvesting; batteryless inference; intermittent inference.

## Source

[Canonical Taxonomy](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/taxonomy.yml) · [Passage Alignment](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/mlsysbook-alignment.yml)

Taxonomy definitions and relationship wording: CC BY 4.0, with attribution to the Machine Learning Systems curriculum by Vijay Janapa Reddi and contributors. The textbook retains its separate license.
