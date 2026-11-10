---
title: Hardware Aware NAS
type: concept
tags:
- Type/Concept
- Group/Qualities
- Topic/Hardware_Aware_Model_Design
source_repository: https://github.com/klappe-pm/cs249r_book
source_commit: de87c0103806d7bfb1c677dbb77a2b92fa00c298
source_path: taxonomy/taxonomy.yml
source_label: Hardware-aware NAS
taxonomy_id: mlsys.hardware-aware-nas
taxonomy_status: draft
taxonomy_version: 0.4-draft
---

# Hardware Aware NAS

Architecture search whose objective includes latency, energy, or memory measured or predicted on the target device rather than proxy counts such as FLOPs.

## Browsing Home

[[02 Concepts/Qualities/Performance, Efficiency & Benchmarking/Hardware Aware Model Design Subject|Hardware Aware Model Design]] → [[02 Concepts/Qualities/Performance, Efficiency & Benchmarking/Performance, Efficiency & Benchmarking Index|Performance, Efficiency & Benchmarking]]

## Book Passages

These are explicitly recorded related passages from the upstream draft alignment; they do not certify complete coverage.

No explicit passage alignment is recorded for this concept. Subject reading pointers are available in its browsing home.

## Conditional Relationships

These are the taxonomy's draft editorial relationships. Read each relationship with its condition; an outgoing link is not a prerequisite claim.

- Specializes [[02 Concepts/Qualities/Performance, Efficiency & Benchmarking/Neural Architecture Search|Neural Architecture Search]]. **Condition:** When the search objective includes a cost measured or predicted on the target platform.

- Optimizes measured [[02 Concepts/Qualities/Performance, Efficiency & Benchmarking/Execution Time|Execution Time]]. **Condition:** When latency on the target device is measured or predicted directly, since FLOP counts can rank architectures differently from real latency.

- Searches within [[02 Concepts/Stack/Hardware & Accelerators/On Device Memory Budget|On Device Memory Budget]]. **Condition:** The search treats flash and SRAM limits as hard constraints on candidate models.

- Uses latency predictors from [[02 Concepts/Foundations/Quantitative System Models/Analytical Performance Model|Analytical Performance Model]]. **Condition:** When on-device measurement of every candidate is too slow, so a calibrated cost model ranks candidates.

## Search Terms

Upstream search terms may be related terms rather than exact synonyms: platform-aware NAS.

## Source

[Canonical Taxonomy](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/taxonomy.yml) · [Passage Alignment](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/mlsysbook-alignment.yml)

Taxonomy definitions and relationship wording: CC BY 4.0, with attribution to the Machine Learning Systems curriculum by Vijay Janapa Reddi and contributors. The textbook retains its separate license.
