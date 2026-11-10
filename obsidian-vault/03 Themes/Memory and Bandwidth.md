---
title: Memory and Bandwidth
type: theme
tags:
- Type/Theme
- Theme/Memory_and_Bandwidth
source_repository: https://github.com/klappe-pm/cs249r_book
source_commit: de87c0103806d7bfb1c677dbb77a2b92fa00c298
source_path: taxonomy/taxonomy.yml
editorial_scope: Curated Navigation Lens
---

# Memory and Bandwidth

Follow capacity, bandwidth, and data movement from hardware through training and generative inference.

This curated navigation lens is an editorial association, not a claim of dependency or equivalence.

## Concepts

- [[02 Concepts/Stack/Hardware & Accelerators/Memory Hierarchy|Memory Hierarchy]] — Arrangement of storage levels and transfer paths with differing capacity, latency, bandwidth, access control, and management mechanisms. The available levels depend on the platform.
- [[02 Concepts/Stack/Hardware & Accelerators/Memory Capacity|Memory Capacity]] — Available storage for concurrently resident state and intermediates.
- [[02 Concepts/Stack/Hardware & Accelerators/Memory Bandwidth|Memory Bandwidth]] — The sustainable rate at which bytes move across a specified memory interface.
- [[02 Concepts/Foundations/Workloads & Requirements/Memory Footprint|Memory Footprint]] — The peak memory a workload occupies, summed over parameters, activations, optimizer or cache state, and runtime buffers.
- [[02 Concepts/Stack/Hardware & Accelerators/Memory Wall|Memory Wall]] — The widening gap between processor arithmetic throughput and memory bandwidth or latency, which makes data movement the limiting factor.
- [[02 Concepts/Foundations/Quantitative System Models/Arithmetic Intensity|Arithmetic Intensity]] — Arithmetic work per byte transferred at a specified memory boundary.
- [[02 Concepts/Foundations/Quantitative System Models/Roofline Bound|Roofline Bound]] — A performance bound combining a compute ceiling with an intensity-dependent bandwidth ceiling.
- [[02 Concepts/Lifecycle/Deployment & Serving/KV Cache|KV Cache]] — Retained attention keys and values reused during autoregressive execution.
- [[02 Concepts/Qualities/Performance, Efficiency & Benchmarking/KV Cache Quantization|KV Cache Quantization]] — Storing attention keys and values at reduced precision, often with per-channel keys and per-token values, to raise batch size or context length under fixed memory.
- [[02 Concepts/Lifecycle/Training & Adaptation/Training State Offloading|Training State Offloading]] — Moving optimizer state, parameters, or activations from accelerator memory to host memory or storage between uses.
- [[02 Concepts/Stack/Frameworks, Compilers & Runtimes/IO Aware Attention Kernel|IO Aware Attention Kernel]] — An exact attention implementation that tiles queries, keys, and values through on-chip memory to avoid materializing the full score matrix in off-chip memory.
- [[02 Concepts/Foundations/Quantitative System Models/Data Movement Energy|Data Movement Energy]] — The energy cost of moving operands between storage levels, which grows with distance and typically exceeds the energy of the arithmetic performed on them.

## Connected Book Passages

- [[01 Books/Volume I - Foundations/01 Foundations/02 System Paradigms/V1-02.02 Four Deployment Regimes Across Nine Orders of Magnitude#^sec-ml-systems-deployment-paradigm-framework-0d25|V1-02.02 Four Deployment Regimes Across Nine Orders of Magnitude]]
- [[01 Books/Volume I - Foundations/03 Optimization/11 Hardware Acceleration/V1-11.07 Performance Bounds#^sec-hardware-acceleration-roofline-model-3e1a|V1-11.07 Performance Bounds]]
- [[01 Books/Volume I - Foundations/04 Deployment/13 Model Serving/V1-13.10 LLM Serving#^sec-model-serving-memory-kv-cache-d1ea|V1-13.10 LLM Serving]]
- [[01 Books/Volume II - Scaling/01 The Fleet/02 Compute Infrastructure/V2-02.04 The Memory Wall#^sec-compute-memory-wall|V2-02.04 The Memory Wall]]
- [[01 Books/Volume II - Scaling/03 The Fleet in Production/10 Serving at Scale/V2-10.08 Memory and Decode-Time Management#^sec-inference-scale-kv-cache-wall|V2-10.08 Memory and Decode-Time Management]]
- [[01 Books/Volume III - Agentic Systems/02 Agent Memory/05 KV Cache Management/V3-05.03 The Footprint of Retained Attention State#^sec-vol3-kvcache-geometry|V3-05.03 The Footprint of Retained Attention State]]
- [[01 Books/Volume IV - Physical AI/01 Machine Anatomy/03 The Cognitive Brain/V4-03.05 The Cost of a Fresh Evaluation#^sec-brain-memory-wall|V4-03.05 The Cost of a Fresh Evaluation]]

## Navigation

[[00 Navigation/Topic Index|Topic Index]]
