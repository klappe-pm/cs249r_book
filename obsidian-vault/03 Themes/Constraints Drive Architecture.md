---
title: Constraints Drive Architecture
type: theme
tags:
- Type/Theme
- Theme/Constraints_Drive_Architecture
source_repository: https://github.com/klappe-pm/cs249r_book
source_commit: de87c0103806d7bfb1c677dbb77a2b92fa00c298
source_path: taxonomy/taxonomy.yml
editorial_scope: Curated Navigation Lens
---

# Constraints Drive Architecture

Trace how workload requirements, resource budgets, and deployment limits shape model and system choices.

This curated navigation lens is an editorial association, not a claim of dependency or equivalence.

## Concepts

- [[02 Concepts/Foundations/Workloads & Requirements/System Requirements|System Requirements]] — Measurable desired behavior and constraints for a specified workload.
- [[02 Concepts/Foundations/Workloads & Requirements/Service Level Objective|Service Level Objective]] — A target for a defined service measure over a specified population and window.
- [[02 Concepts/Foundations/Workloads & Requirements/Latency Budget|Latency Budget]] — An allocation of an end-to-end latency target across the stages of a request path, such as network, preprocessing, inference, and postprocessing.
- [[02 Concepts/Stack/Hardware & Accelerators/Memory Capacity|Memory Capacity]] — Available storage for concurrently resident state and intermediates.
- [[02 Concepts/Stack/Hardware & Accelerators/On Device Memory Budget|On Device Memory Budget]] — The flash and SRAM limits that bound a deployed model's stored weights and peak activation memory on embedded hardware.
- [[02 Concepts/Foundations/Workloads & Requirements/Pareto Frontier|Pareto Frontier]] — The set of configurations for which no objective, such as accuracy, latency, or cost, can improve without worsening another.
- [[02 Concepts/Foundations/Quantitative System Models/Roofline Bound|Roofline Bound]] — A performance bound combining a compute ceiling with an intensity-dependent bandwidth ceiling.
- [[02 Concepts/Foundations/Quantitative System Models/Arithmetic Intensity|Arithmetic Intensity]] — Arithmetic work per byte transferred at a specified memory boundary.
- [[02 Concepts/Stack/Hardware & Accelerators/Compute Throughput|Compute Throughput]] — The sustainable rate of a specified arithmetic workload on an execution resource.

## Connected Book Passages

- [[01 Books/Volume I - Foundations/01 Foundations/02 System Paradigms/V1-02.02 Four Deployment Regimes Across Nine Orders of Magnitude#^sec-ml-systems-deployment-paradigm-framework-0d25|V1-02.02 Four Deployment Regimes Across Nine Orders of Magnitude]]
- [[01 Books/Volume I - Foundations/01 Foundations/03 ML Lifecycle/V1-03.06 Stage 1 Problem Definition#^sec-ml-workflow-balancing-competing-constraints-b92a|V1-03.06 Stage 1 Problem Definition]]
- [[01 Books/Volume I - Foundations/03 Optimization/11 Hardware Acceleration/V1-11.07 Performance Bounds#^sec-hardware-acceleration-roofline-model-3e1a|V1-11.07 Performance Bounds]]
- [[01 Books/Volume I - Foundations/03 Optimization/12 Benchmarking/V1-12.07 Inference Benchmarks#^sec-benchmarking-latency-tail-latency-5cde|V1-12.07 Inference Benchmarks]]
- [[01 Books/Volume I - Foundations/04 Deployment/13 Model Serving/V1-13.04 Request Lifecycle#^sec-model-serving-request-lifecycle-d9c6|V1-13.04 Request Lifecycle]]
- [[01 Books/Volume II - Scaling/01 The Fleet/02 Compute Infrastructure/V2-02.04 The Memory Wall#^sec-compute-memory-wall|V2-02.04 The Memory Wall]]
- [[01 Books/Volume II - Scaling/03 The Fleet in Production/12 ML Operations at Scale/V2-12.06 CI CD for ML at Scale#^sec-ops-scale-end-to-end-evaluation-contract|V2-12.06 CI CD for ML at Scale]]

## Navigation

[[00 Navigation/Topic Index|Topic Index]]
