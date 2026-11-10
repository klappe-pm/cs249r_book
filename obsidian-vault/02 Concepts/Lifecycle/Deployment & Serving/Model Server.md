---
title: Model Server
type: concept
tags:
- Type/Concept
- Group/Lifecycle
- Topic/Serving_Architectures
source_repository: https://github.com/klappe-pm/cs249r_book
source_commit: de87c0103806d7bfb1c677dbb77a2b92fa00c298
source_path: taxonomy/taxonomy.yml
source_label: Model server
taxonomy_id: mlsys.model-server
taxonomy_status: draft
taxonomy_version: 0.4-draft
---

# Model Server

A service that loads model artifacts and executes inference requests behind a network interface, managing versions, batching, and resources.

## Browsing Home

[[02 Concepts/Lifecycle/Deployment & Serving/Serving Architectures Subject|Serving Architectures]] → [[02 Concepts/Lifecycle/Deployment & Serving/Deployment & Serving Index|Deployment & Serving]]

## Book Passages

These are explicitly recorded related passages from the upstream draft alignment; they do not certify complete coverage.

No explicit passage alignment is recorded for this concept. Subject reading pointers are available in its browsing home.

## Conditional Relationships

These are the taxonomy's draft editorial relationships. Read each relationship with its condition; an outgoing link is not a prerequisite claim.

- Hosts [[02 Concepts/Lifecycle/Deployment & Serving/Request Batching|Request Batching]]. **Condition:** Holds for servers that queue concurrent requests to batch them on shared accelerators.

- Validates requests against [[02 Concepts/Foundations/Models & Architectures/Model Signature|Model Signature]]. **Condition:** The server decodes and checks requests using the artifact's declared inputs and outputs.

- Loads and executes [[02 Concepts/Foundations/Models & Architectures/Model Artifact|Model Artifact]]. **Condition:** Holds for any server that loads serialized weights and graph at startup or on version change.

## Search Terms

Upstream search terms may be related terms rather than exact synonyms: inference server.

## Source

[Canonical Taxonomy](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/taxonomy.yml) · [Passage Alignment](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/mlsysbook-alignment.yml)

Taxonomy definitions and relationship wording: CC BY 4.0, with attribution to the Machine Learning Systems curriculum by Vijay Janapa Reddi and contributors. The textbook retains its separate license.
