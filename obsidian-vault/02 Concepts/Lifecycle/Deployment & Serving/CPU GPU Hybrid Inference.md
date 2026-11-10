---
title: CPU GPU Hybrid Inference
type: concept
tags:
- Type/Concept
- Group/Lifecycle
- Topic/LLM_Generative_Inference
source_repository: https://github.com/klappe-pm/cs249r_book
source_commit: de87c0103806d7bfb1c677dbb77a2b92fa00c298
source_path: taxonomy/taxonomy.yml
source_label: CPU-GPU hybrid inference
taxonomy_id: mlsys.cpu-gpu-hybrid-inference
taxonomy_status: draft
taxonomy_version: 0.4-draft
---

# CPU GPU Hybrid Inference

Splitting inference so the host CPU computes some operations, such as attention or rarely active neurons, from host memory when model or KV state exceeds accelerator memory.

## Browsing Home

[[02 Concepts/Lifecycle/Deployment & Serving/LLM & Generative Inference Subject|LLM & Generative Inference]] → [[02 Concepts/Lifecycle/Deployment & Serving/Deployment & Serving Index|Deployment & Serving]]

## Book Passages

These are explicitly recorded related passages from the upstream draft alignment; they do not certify complete coverage.

No explicit passage alignment is recorded for this concept. Subject reading pointers are available in its browsing home.

## Conditional Relationships

These are the taxonomy's draft editorial relationships. Read each relationship with its condition; an outgoing link is not a prerequisite claim.

- Computes on the host instead of moving state back as in [[02 Concepts/Lifecycle/Deployment & Serving/KV Cache Offloading and Tiering|KV Cache Offloading and Tiering]]. **Condition:** Host memory holds state that exceeds accelerator capacity.

- Offloads selected operators to [[02 Concepts/Stack/Hardware & Accelerators/CPU Execution Architecture|CPU Execution Architecture]]. **Condition:** Model or KV state exceeds accelerator memory.

## Search Terms

Upstream search terms may be related terms rather than exact synonyms: host-assisted inference; CPU offloaded attention.

## Source

[Canonical Taxonomy](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/taxonomy.yml) · [Passage Alignment](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/mlsysbook-alignment.yml)

Taxonomy definitions and relationship wording: CC BY 4.0, with attribution to the Machine Learning Systems curriculum by Vijay Janapa Reddi and contributors. The textbook retains its separate license.
