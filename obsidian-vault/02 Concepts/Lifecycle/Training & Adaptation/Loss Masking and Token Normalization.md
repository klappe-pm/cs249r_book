---
title: Loss Masking and Token Normalization
type: concept
tags:
- Type/Concept
- Group/Lifecycle
- Topic/Adaptation_Fine_Tuning_Prompting_Transfer
source_repository: https://github.com/klappe-pm/cs249r_book
source_commit: de87c0103806d7bfb1c677dbb77a2b92fa00c298
source_path: taxonomy/taxonomy.yml
source_label: Loss masking and token normalization
taxonomy_id: mlsys.loss-masking
taxonomy_status: draft
taxonomy_version: 0.4-draft
---

# Loss Masking and Token Normalization

Excluding prompt, tool-output, and other non-target tokens from the training loss, and choosing how remaining token losses are averaged across turns and sequences.

## Browsing Home

[[02 Concepts/Lifecycle/Training & Adaptation/Adaptation Fine Tuning, Prompting & Transfer Subject|Adaptation Fine Tuning, Prompting & Transfer]] → [[02 Concepts/Lifecycle/Training & Adaptation/Training & Adaptation Index|Training & Adaptation]]

## Book Passages

These are explicitly recorded related passages from the upstream draft alignment; they do not certify complete coverage.

- [[01 Books/Volume III - Agentic Systems/05 Learning from Trajectories/16 Trajectory Fine-Tuning/V3-16.05 Observation Loss Masking#^sec-vol3-fine-tuning-loss-masking|V3-16.05 Observation Loss Masking]] — Loss mask. [Exact Source Passage](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/books/vol3/16_fine_tuning/16_fine_tuning.qmd#L217).

## Conditional Relationships

These are the taxonomy's draft editorial relationships. Read each relationship with its condition; an outgoing link is not a prerequisite claim.

- Is a configuration step in [[02 Concepts/Lifecycle/Training & Adaptation/Supervised Fine Tuning|Supervised Fine Tuning]]. **Condition:** Examples contain non-target tokens such as prompts or tool output.

- Defines which tokens contribute to [[02 Concepts/Lifecycle/Training & Adaptation/Training Loss|Training Loss]]. **Condition:** Sequences and turns vary in length.

- Locates assistant spans through [[02 Concepts/Foundations/Models & Architectures/Chat Template|Chat Template]]. **Condition:** When non-target tokens are identified by role markers in the rendered sequence.

## Search Terms

Upstream search terms may be related terms rather than exact synonyms: prompt masking; assistant-only loss.

## Source

[Canonical Taxonomy](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/taxonomy.yml) · [Passage Alignment](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/mlsysbook-alignment.yml)

Taxonomy definitions and relationship wording: CC BY 4.0, with attribution to the Machine Learning Systems curriculum by Vijay Janapa Reddi and contributors. The textbook retains its separate license.
