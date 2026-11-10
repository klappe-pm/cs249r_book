---
title: Inference Compute and Memory Estimate
type: concept
tags:
- Type/Concept
- Group/Foundations
- Topic/Workload_Characterization
source_repository: https://github.com/klappe-pm/cs249r_book
source_commit: de87c0103806d7bfb1c677dbb77a2b92fa00c298
source_path: taxonomy/taxonomy.yml
source_label: Inference compute and memory estimate
taxonomy_id: mlsys.inference-compute-estimate
taxonomy_status: draft
taxonomy_version: 0.4-draft
---

# Inference Compute and Memory Estimate

Approximating dense transformer inference as about two FLOPs per parameter per token, plus KV-cache bytes from layers, KV heads, head dimension, context length, batch, and precision.

## Browsing Home

[[02 Concepts/Foundations/Workloads & Requirements/Workload Characterization Subject|Workload Characterization]] → [[02 Concepts/Foundations/Workloads & Requirements/Workloads & Requirements Index|Workloads & Requirements]]

## Book Passages

These are explicitly recorded related passages from the upstream draft alignment; they do not certify complete coverage.

No explicit passage alignment is recorded for this concept. Subject reading pointers are available in its browsing home.

## Conditional Relationships

These are the taxonomy's draft editorial relationships. Read each relationship with its condition; an outgoing link is not a prerequisite claim.

- Sizes [[02 Concepts/Lifecycle/Deployment & Serving/KV Cache|KV Cache]]. **Condition:** Dense attention with known layers, KV heads, head dimension, context, and precision.

- Is the per-token inference case of [[02 Concepts/Foundations/Workloads & Requirements/Operation and Byte Accounting|Operation and Byte Accounting]]. **Condition:** The model is a dense transformer served autoregressively.

- Estimates the parameter and KV portions of [[02 Concepts/Foundations/Workloads & Requirements/Memory Footprint|Memory Footprint]]. **Condition:** When parameter bytes follow from count and precision and KV bytes from layers, KV heads, head dimension, context, batch, and precision; runtime buffers and activations are excluded.

## Search Terms

Upstream search terms may be related terms rather than exact synonyms: 2N FLOPs per token; KV-cache sizing.

## Source

[Canonical Taxonomy](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/taxonomy.yml) · [Passage Alignment](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/mlsysbook-alignment.yml)

Taxonomy definitions and relationship wording: CC BY 4.0, with attribution to the Machine Learning Systems curriculum by Vijay Janapa Reddi and contributors. The textbook retains its separate license.
