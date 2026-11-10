---
title: Supervised Fine Tuning
type: concept
tags:
- Type/Concept
- Group/Lifecycle
- Topic/Adaptation_Fine_Tuning_Prompting_Transfer
source_repository: https://github.com/klappe-pm/cs249r_book
source_commit: de87c0103806d7bfb1c677dbb77a2b92fa00c298
source_path: taxonomy/taxonomy.yml
source_label: Supervised fine-tuning
taxonomy_id: mlsys.supervised-fine-tuning
taxonomy_status: draft
taxonomy_version: 0.4-draft
---

# Supervised Fine Tuning

Continued training of a pretrained model on input-output demonstrations, such as instruction-response pairs, to shape task behavior.

## Browsing Home

[[02 Concepts/Lifecycle/Training & Adaptation/Adaptation Fine Tuning, Prompting & Transfer Subject|Adaptation Fine Tuning, Prompting & Transfer]] → [[02 Concepts/Lifecycle/Training & Adaptation/Training & Adaptation Index|Training & Adaptation]]

## Book Passages

These are explicitly recorded related passages from the upstream draft alignment; they do not certify complete coverage.

No explicit passage alignment is recorded for this concept. Subject reading pointers are available in its browsing home.

## Conditional Relationships

These are the taxonomy's draft editorial relationships. Read each relationship with its condition; an outgoing link is not a prerequisite claim.

- Can cause [[02 Concepts/Lifecycle/Training & Adaptation/Catastrophic Forgetting|Catastrophic Forgetting]]. **Condition:** Holds when fine-tuning data are narrow relative to pretraining and no replay or regularization is used.

- Is a kind of [[02 Concepts/Lifecycle/Training & Adaptation/Supervised Learning|Supervised Learning]]. **Condition:** Holds when training uses input-output demonstrations as targets.

- Implements [[02 Concepts/Lifecycle/Training & Adaptation/Transfer Learning|Transfer Learning]]. **Condition:** Applies when a pretrained model is adapted to a new task or behavior.

- Renders every example through [[02 Concepts/Foundations/Models & Architectures/Chat Template|Chat Template]]. **Condition:** For conversational or tool-using fine-tuning data turned into tokens before loss computation.

- Trains compliance on curated borderline-benign requests, reducing [[02 Concepts/Qualities/Safety & Assurance/Over Refusal|Over Refusal]]. **Condition:** The curated set must be reviewed so it does not also teach compliance on harmful requests.

## Search Terms

Upstream search terms may be related terms rather than exact synonyms: SFT; instruction tuning.

## Source

[Canonical Taxonomy](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/taxonomy.yml) · [Passage Alignment](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/mlsysbook-alignment.yml)

Taxonomy definitions and relationship wording: CC BY 4.0, with attribution to the Machine Learning Systems curriculum by Vijay Janapa Reddi and contributors. The textbook retains its separate license.
