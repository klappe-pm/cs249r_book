---
title: Compression Technique Composition
type: concept
tags:
- Type/Concept
- Group/Qualities
- Topic/Model_Compression
source_repository: https://github.com/klappe-pm/cs249r_book
source_commit: de87c0103806d7bfb1c677dbb77a2b92fa00c298
source_path: taxonomy/taxonomy.yml
source_label: Compression technique composition
taxonomy_id: mlsys.compression-composition
taxonomy_status: draft
taxonomy_version: 0.4-draft
---

# Compression Technique Composition

Applying several compression methods in a chosen sequence, whose interactions can reinforce or diminish their individual savings and must be evaluated jointly for quality and execution cost.

## Browsing Home

[[02 Concepts/Qualities/Performance, Efficiency & Benchmarking/Model Compression Subject|Model Compression]] → [[02 Concepts/Qualities/Performance, Efficiency & Benchmarking/Performance, Efficiency & Benchmarking Index|Performance, Efficiency & Benchmarking]]

## Book Passages

These are explicitly recorded related passages from the upstream draft alignment; they do not certify complete coverage.

No explicit passage alignment is recorded for this concept. Subject reading pointers are available in its browsing home.

## Conditional Relationships

These are the taxonomy's draft editorial relationships. Read each relationship with its condition; an outgoing link is not a prerequisite claim.

- Typically applies first [[02 Concepts/Qualities/Performance, Efficiency & Benchmarking/Pruning|Pruning]]. **Condition:** When sparsity is introduced before quantization so the quantizer calibrates on the surviving weights.

- Applies to the already-pruned or distilled model [[02 Concepts/Qualities/Performance, Efficiency & Benchmarking/Quantization|Quantization]]. **Condition:** When the bit-width is chosen after structure has been removed.

- Recovers quality lost by the other stages through [[02 Concepts/Qualities/Performance, Efficiency & Benchmarking/Knowledge Distillation|Knowledge Distillation]]. **Condition:** When a teacher is available to fine-tune the compressed student.

- Shapes, through the techniques chosen and their order, the attainable [[02 Concepts/Qualities/Performance, Efficiency & Benchmarking/Accuracy Efficiency Frontier|Accuracy Efficiency Frontier]]. **Condition:** When the frontier is measured over compressed variants rather than architectures.

## Search Terms

Upstream search terms may be related terms rather than exact synonyms: compression pipeline; pruning-quantization-distillation ordering; combined compression.

## Source

[Canonical Taxonomy](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/taxonomy.yml) · [Passage Alignment](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/mlsysbook-alignment.yml)

Taxonomy definitions and relationship wording: CC BY 4.0, with attribution to the Machine Learning Systems curriculum by Vijay Janapa Reddi and contributors. The textbook retains its separate license.
