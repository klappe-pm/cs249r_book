---
title: Stateless Model Serving
type: concept
tags:
- Type/Concept
- Group/Lifecycle
- Topic/Serving_Architectures
source_repository: https://github.com/klappe-pm/cs249r_book
source_commit: de87c0103806d7bfb1c677dbb77a2b92fa00c298
source_path: taxonomy/taxonomy.yml
source_label: Stateless model serving
taxonomy_id: mlsys.stateless-serving-function
taxonomy_status: draft
taxonomy_version: 0.4-draft
---

# Stateless Model Serving

Exporting a model as a stateless function from request inputs to prediction, so any replica can serve any request and replicas scale horizontally.

## Browsing Home

[[02 Concepts/Lifecycle/Deployment & Serving/Serving Architectures Subject|Serving Architectures]] → [[02 Concepts/Lifecycle/Deployment & Serving/Deployment & Serving Index|Deployment & Serving]]

## Book Passages

These are explicitly recorded related passages from the upstream draft alignment; they do not certify complete coverage.

No explicit passage alignment is recorded for this concept. Subject reading pointers are available in its browsing home.

## Conditional Relationships

These are the taxonomy's draft editorial relationships. Read each relationship with its condition; an outgoing link is not a prerequisite claim.

- Lets replicas be added or removed for [[02 Concepts/Lifecycle/Deployment & Serving/Autoscaling|Autoscaling]]. **Condition:** No request depends on replica-local state.

- Exposes its interface as [[02 Concepts/Foundations/Models & Architectures/Model Signature|Model Signature]]. **Condition:** Inputs and outputs are declared at export.

## Search Terms

Upstream search terms may be related terms rather than exact synonyms: stateless serving function.

## Source

[Canonical Taxonomy](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/taxonomy.yml) · [Passage Alignment](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/mlsysbook-alignment.yml)

Taxonomy definitions and relationship wording: CC BY 4.0, with attribution to the Machine Learning Systems curriculum by Vijay Janapa Reddi and contributors. The textbook retains its separate license.
