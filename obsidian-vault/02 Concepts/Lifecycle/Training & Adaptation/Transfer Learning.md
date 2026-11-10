---
title: Transfer Learning
type: concept
tags:
- Type/Concept
- Group/Lifecycle
- Topic/Adaptation_Fine_Tuning_Prompting_Transfer
source_repository: https://github.com/klappe-pm/cs249r_book
source_commit: de87c0103806d7bfb1c677dbb77a2b92fa00c298
source_path: taxonomy/taxonomy.yml
source_label: Transfer learning
taxonomy_id: mlsys.transfer-learning
taxonomy_status: draft
taxonomy_version: 0.4-draft
---

# Transfer Learning

Adapting representations or parameters learned from one setting to another.

## Browsing Home

[[02 Concepts/Lifecycle/Training & Adaptation/Adaptation Fine Tuning, Prompting & Transfer Subject|Adaptation Fine Tuning, Prompting & Transfer]] → [[02 Concepts/Lifecycle/Training & Adaptation/Training & Adaptation Index|Training & Adaptation]]

## Book Passages

These are explicitly recorded related passages from the upstream draft alignment; they do not certify complete coverage.

No explicit passage alignment is recorded for this concept. Subject reading pointers are available in its browsing home.

## Conditional Relationships

These are the taxonomy's draft editorial relationships. Read each relationship with its condition; an outgoing link is not a prerequisite claim.

- Increases exposure to [[02 Concepts/Qualities/Security & Privacy/Backdoor Attack|Backdoor Attack]]. **Condition:** When pretrained weights come from untrusted parties, since backdoors can survive fine-tuning on clean data.

- Shortens the target-task [[02 Concepts/Qualities/Performance, Efficiency & Benchmarking/Time to Train|Time to Train]]. **Condition:** When a suitable pretrained model exists and fine-tuning converges in far fewer steps than training from scratch.

## Source

[Canonical Taxonomy](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/taxonomy.yml) · [Passage Alignment](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/mlsysbook-alignment.yml)

Taxonomy definitions and relationship wording: CC BY 4.0, with attribution to the Machine Learning Systems curriculum by Vijay Janapa Reddi and contributors. The textbook retains its separate license.
