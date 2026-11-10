---
title: Expert Offloading
type: concept
tags:
- Type/Concept
- Group/Lifecycle
- Topic/LLM_Generative_Inference
source_repository: https://github.com/klappe-pm/cs249r_book
source_commit: de87c0103806d7bfb1c677dbb77a2b92fa00c298
source_path: taxonomy/taxonomy.yml
source_label: Expert offloading
taxonomy_id: mlsys.expert-offloading
taxonomy_status: draft
taxonomy_version: 0.4-draft
---

# Expert Offloading

Keeping some mixture-of-experts weights in host memory or storage and fetching the experts a batch needs into accelerator memory, often prefetching predicted ones, which lets a model larger than accelerator memory run at the cost of transfers.

## Browsing Home

[[02 Concepts/Lifecycle/Deployment & Serving/LLM & Generative Inference Subject|LLM & Generative Inference]] → [[02 Concepts/Lifecycle/Deployment & Serving/Deployment & Serving Index|Deployment & Serving]]

## Book Passages

These are explicitly recorded related passages from the upstream draft alignment; they do not certify complete coverage.

No explicit passage alignment is recorded for this concept. Subject reading pointers are available in its browsing home.

## Conditional Relationships

These are the taxonomy's draft editorial relationships. Read each relationship with its condition; an outgoing link is not a prerequisite claim.

- Moves expert weights to the accelerator instead of computing on the host as in [[02 Concepts/Lifecycle/Deployment & Serving/CPU GPU Hybrid Inference|CPU GPU Hybrid Inference]]. **Condition:** When mixture-of-experts weights exceed accelerator memory and must stay partly in host memory.

- Prefetches the experts predicted by [[02 Concepts/Foundations/Models & Architectures/Expert Routing|Expert Routing]]. **Condition:** When routing for upcoming layers or batches can be predicted early enough to hide the transfer.

## Search Terms

Upstream search terms may be related terms rather than exact synonyms: MoE expert offloading; expert-weight offloading.

## Source

[Canonical Taxonomy](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/taxonomy.yml) · [Passage Alignment](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/mlsysbook-alignment.yml)

Taxonomy definitions and relationship wording: CC BY 4.0, with attribution to the Machine Learning Systems curriculum by Vijay Janapa Reddi and contributors. The textbook retains its separate license.
