---
title: On Device Inference Runtime
type: concept
tags:
- Type/Concept
- Group/Lifecycle
- Topic/On_Device_Edge_Deployment
source_repository: https://github.com/klappe-pm/cs249r_book
source_commit: de87c0103806d7bfb1c677dbb77a2b92fa00c298
source_path: taxonomy/taxonomy.yml
source_label: On-device inference runtime
taxonomy_id: mlsys.on-device-runtime
taxonomy_status: draft
taxonomy_version: 0.4-draft
---

# On Device Inference Runtime

An interpreter or compiled engine that executes models locally on personal or embedded devices, including inside browsers, under the target environment's memory, operator, and execution limits.

## Browsing Home

[[02 Concepts/Lifecycle/Deployment & Serving/On Device & Edge Deployment Subject|On Device & Edge Deployment]] → [[02 Concepts/Lifecycle/Deployment & Serving/Deployment & Serving Index|Deployment & Serving]]

## Book Passages

These are explicitly recorded related passages from the upstream draft alignment; they do not certify complete coverage.

No explicit passage alignment is recorded for this concept. Subject reading pointers are available in its browsing home.

## Conditional Relationships

These are the taxonomy's draft editorial relationships. Read each relationship with its condition; an outgoing link is not a prerequisite claim.

- Delegates operators across [[02 Concepts/Stack/Hardware & Accelerators/Heterogeneous Mobile SoC|Heterogeneous Mobile SoC]]. **Condition:** The runtime partitions supported operators onto the NPU, GPU, or DSP and falls back to CPU.

- Requires [[02 Concepts/Lifecycle/Deployment & Serving/Model Conversion|Model Conversion]]. **Condition:** Holds because runtimes accept only their own formats and operator sets.

- Delegates supported operators to [[02 Concepts/Stack/Hardware & Accelerators/On Device Neural Accelerator|On Device Neural Accelerator]]. **Condition:** Applies when the device has an accelerator and a delegate for it.

- Delegates subgraphs through [[02 Concepts/Stack/Frameworks, Compilers & Runtimes/Execution Providers and Operator Fallback|Execution Providers and Operator Fallback]]. **Condition:** The target device exposes an NPU, GPU, or DSP backend with partial operator coverage.

- Executes fully integer operator graphs through [[02 Concepts/Qualities/Performance, Efficiency & Benchmarking/Integer Only Inference|Integer Only Inference]]. **Condition:** When the runtime targets an embedded device without a floating-point unit.

## Search Terms

Upstream search terms may be related terms rather than exact synonyms: browser inference runtime; WebGPU inference; WebAssembly inference.

## Source

[Canonical Taxonomy](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/taxonomy.yml) · [Passage Alignment](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/mlsysbook-alignment.yml)

Taxonomy definitions and relationship wording: CC BY 4.0, with attribution to the Machine Learning Systems curriculum by Vijay Janapa Reddi and contributors. The textbook retains its separate license.
