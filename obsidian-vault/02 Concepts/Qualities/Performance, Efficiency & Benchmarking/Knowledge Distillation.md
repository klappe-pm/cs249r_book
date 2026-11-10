---
title: Knowledge Distillation
type: concept
tags:
- Type/Concept
- Group/Qualities
- Topic/Model_Compression
source_repository: https://github.com/klappe-pm/cs249r_book
source_commit: de87c0103806d7bfb1c677dbb77a2b92fa00c298
source_path: taxonomy/taxonomy.yml
source_label: Knowledge distillation
taxonomy_id: mlsys.distillation
taxonomy_status: draft
taxonomy_version: 0.4-draft
---

# Knowledge Distillation

Training a student to match output distributions or internal signals from a teacher model or ensemble, potentially reducing serving cost when the student is cheaper while requiring validation of retained quality.

## Browsing Home

[[02 Concepts/Qualities/Performance, Efficiency & Benchmarking/Model Compression Subject|Model Compression]] → [[02 Concepts/Qualities/Performance, Efficiency & Benchmarking/Performance, Efficiency & Benchmarking Index|Performance, Efficiency & Benchmarking]]

## Book Passages

These are explicitly recorded related passages from the upstream draft alignment; they do not certify complete coverage.

No explicit passage alignment is recorded for this concept. Subject reading pointers are available in its browsing home.

## Conditional Relationships

These are the taxonomy's draft editorial relationships. Read each relationship with its condition; an outgoing link is not a prerequisite claim.

- Produces a smaller student [[02 Concepts/Foundations/Models & Architectures/Neural Networks|Neural Networks]]. **Condition:** The student architecture and task evidence determine the actual trade-off.

- Reduces the serving memory footprint by producing a smaller student [[02 Concepts/Foundations/Workloads & Requirements/Memory Footprint|Memory Footprint]]. **Condition:** When the student architecture is smaller than the teacher and reaches acceptable quality on the target metric.

- Produces well-aligned draft models for [[02 Concepts/Lifecycle/Deployment & Serving/Speculative Decoding|Speculative Decoding]]. **Condition:** When the draft is distilled from the target model so its token distribution matches closely enough to raise acceptance rates.

- Can strip parameter-embedded [[02 Concepts/Qualities/Security & Privacy/Model Watermarking|Model Watermarking]]. **Condition:** For watermarks embedded in weights rather than in behavior on trigger inputs, since a distilled student has new weights.

## Themes

- [[03 Themes/Accuracy and Efficiency|Accuracy and Efficiency]]

## Source

[Canonical Taxonomy](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/taxonomy.yml) · [Passage Alignment](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/mlsysbook-alignment.yml)

Taxonomy definitions and relationship wording: CC BY 4.0, with attribution to the Machine Learning Systems curriculum by Vijay Janapa Reddi and contributors. The textbook retains its separate license.
