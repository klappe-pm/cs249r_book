---
title: Integration Testing
type: concept
tags:
- Type/Concept
- Group/Lifecycle
- Topic/ML_Testing_Debugging
source_repository: https://github.com/klappe-pm/cs249r_book
source_commit: de87c0103806d7bfb1c677dbb77a2b92fa00c298
source_path: taxonomy/taxonomy.yml
source_label: Integration testing
taxonomy_id: mlsys.integration-testing
taxonomy_status: draft
taxonomy_version: 0.4-draft
---

# Integration Testing

Testing interactions among assembled components against stated interface and behavior expectations.

## Browsing Home

[[02 Concepts/Lifecycle/Model Evaluation & Testing/ML Testing & Debugging Subject|ML Testing & Debugging]] → [[02 Concepts/Lifecycle/Model Evaluation & Testing/Model Evaluation & Testing Index|Model Evaluation & Testing]]

## Book Passages

These are explicitly recorded related passages from the upstream draft alignment; they do not certify complete coverage.

No explicit passage alignment is recorded for this concept. Subject reading pointers are available in its browsing home.

## Conditional Relationships

These are the taxonomy's draft editorial relationships. Read each relationship with its condition; an outgoing link is not a prerequisite claim.

- Requires expectations from a [[02 Concepts/Lifecycle/Model Evaluation & Testing/Test Oracle|Test Oracle]]. **Condition:** The oracle may be partial, probabilistic, or human-assisted and only covers declared properties and tested cases.

- Can expose [[02 Concepts/Lifecycle/Data Engineering/Training Serving Skew|Training Serving Skew]]. **Condition:** Tests compare relevant preprocessing and model interfaces across representative paths; untested distributions or deployment differences can remain.

- Tests compatibility within [[02 Concepts/Lifecycle/MLOps & Operations/Dependency Environment|Dependency Environment]]. **Condition:** Test environments must represent the target packages, binaries, resources, and configuration; passing one environment does not validate all others.

- Checks callers against [[02 Concepts/Foundations/Models & Architectures/Model Signature|Model Signature]]. **Condition:** Callers and the artifact agree on input and output names, types, and shapes.

## Source

[Canonical Taxonomy](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/taxonomy.yml) · [Passage Alignment](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/mlsysbook-alignment.yml)

Taxonomy definitions and relationship wording: CC BY 4.0, with attribution to the Machine Learning Systems curriculum by Vijay Janapa Reddi and contributors. The textbook retains its separate license.
