---
title: Communication to Computation Ratio
type: concept
tags:
- Type/Concept
- Group/Foundations
- Topic/Roofline_Performance_Models_Simulation
source_repository: https://github.com/klappe-pm/cs249r_book
source_commit: de87c0103806d7bfb1c677dbb77a2b92fa00c298
source_path: taxonomy/taxonomy.yml
source_label: Communication-to-computation ratio
taxonomy_id: mlsys.communication-intensity
taxonomy_status: draft
taxonomy_version: 0.4-draft
---

# Communication to Computation Ratio

The bytes a parallel plan must exchange per unit of local arithmetic, which, set against link bandwidth and the accelerator's FLOP rate, says whether a stage is communication-bound in the same way arithmetic intensity says whether a kernel is memory-bound.

## Browsing Home

[[02 Concepts/Foundations/Quantitative System Models/Roofline, Performance Models & Simulation Subject|Roofline, Performance Models & Simulation]] → [[02 Concepts/Foundations/Quantitative System Models/Quantitative System Models Index|Quantitative System Models]]

## Book Passages

These are explicitly recorded related passages from the upstream draft alignment; they do not certify complete coverage.

No explicit passage alignment is recorded for this concept. Subject reading pointers are available in its browsing home.

## Conditional Relationships

These are the taxonomy's draft editorial relationships. Read each relationship with its condition; an outgoing link is not a prerequisite claim.

- Together with link bandwidth bounds [[02 Concepts/Foundations/Quantitative System Models/Parallel Scaling Efficiency|Parallel Scaling Efficiency]]. **Condition:** When the exchange is not fully overlapped with computation.

## Search Terms

Upstream search terms may be related terms rather than exact synonyms: bytes communicated per FLOP; communication intensity.

## Source

[Canonical Taxonomy](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/taxonomy.yml) · [Passage Alignment](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/mlsysbook-alignment.yml)

Taxonomy definitions and relationship wording: CC BY 4.0, with attribution to the Machine Learning Systems curriculum by Vijay Janapa Reddi and contributors. The textbook retains its separate license.
