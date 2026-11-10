---
title: Parameter Efficient Adaptation
type: concept
tags:
- Type/Concept
- Group/Lifecycle
- Topic/Adaptation_Fine_Tuning_Prompting_Transfer
source_repository: https://github.com/klappe-pm/cs249r_book
source_commit: de87c0103806d7bfb1c677dbb77a2b92fa00c298
source_path: taxonomy/taxonomy.yml
source_label: Parameter-efficient adaptation
taxonomy_id: mlsys.peft
taxonomy_status: draft
taxonomy_version: 0.4-draft
---

# Parameter Efficient Adaptation

Adapting a model by changing a limited parameter subset or added parameterization.

## Browsing Home

[[02 Concepts/Lifecycle/Training & Adaptation/Adaptation Fine Tuning, Prompting & Transfer Subject|Adaptation Fine Tuning, Prompting & Transfer]] → [[02 Concepts/Lifecycle/Training & Adaptation/Training & Adaptation Index|Training & Adaptation]]

## Book Passages

These are explicitly recorded related passages from the upstream draft alignment; they do not certify complete coverage.

No explicit passage alignment is recorded for this concept. Subject reading pointers are available in its browsing home.

## Conditional Relationships

These are the taxonomy's draft editorial relationships. Read each relationship with its condition; an outgoing link is not a prerequisite claim.

- Implements [[02 Concepts/Lifecycle/Training & Adaptation/Transfer Learning|Transfer Learning]]. **Condition:** Parameter-efficient adaptation is one option, not all transfer learning.

- Shrinks trainable and optimizer state in [[02 Concepts/Lifecycle/Training & Adaptation/Training State|Training State]]. **Condition:** The method may select existing parameters or introduce new parameterizations; frozen parameters and activations can still remain resident.

- Freezes the base weights so adaptation cannot overwrite them, limiting [[02 Concepts/Lifecycle/Training & Adaptation/Catastrophic Forgetting|Catastrophic Forgetting]]. **Condition:** Holds when the adapter capacity is small relative to the base and base weights stay frozen.

## Search Terms

Upstream search terms may be related terms rather than exact synonyms: PEFT; adapter tuning; prefix tuning; prompt tuning; soft prompts.

## Source

[Canonical Taxonomy](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/taxonomy.yml) · [Passage Alignment](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/mlsysbook-alignment.yml)

Taxonomy definitions and relationship wording: CC BY 4.0, with attribution to the Machine Learning Systems curriculum by Vijay Janapa Reddi and contributors. The textbook retains its separate license.
