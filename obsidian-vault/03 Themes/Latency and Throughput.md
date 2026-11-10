---
title: Latency and Throughput
type: theme
tags:
- Type/Theme
- Theme/Latency_and_Throughput
source_repository: https://github.com/klappe-pm/cs249r_book
source_commit: de87c0103806d7bfb1c677dbb77a2b92fa00c298
source_path: taxonomy/taxonomy.yml
editorial_scope: Curated Navigation Lens
---

# Latency and Throughput

Compare response-time budgets, queueing, batching, and useful serving capacity under an explicit workload.

This curated navigation lens is an editorial association, not a claim of dependency or equivalence.

## Concepts

- [[02 Concepts/Lifecycle/Deployment & Serving/Tail Latency|Tail Latency]] — A high quantile of a defined request-latency distribution.
- [[02 Concepts/Foundations/Workloads & Requirements/Latency Budget|Latency Budget]] — An allocation of an end-to-end latency target across the stages of a request path, such as network, preprocessing, inference, and postprocessing.
- [[02 Concepts/Lifecycle/Deployment & Serving/Latency Percentiles|Latency Percentiles]] — Summarizing a latency distribution by percentiles such as p50, p95, and p99, so that a service is judged by the experience of most requests and of the slow tail rather than by the mean.
- [[02 Concepts/Foundations/Quantitative System Models/Latency Throughput Curve|Latency Throughput Curve]] — The relationship between offered load and latency, in which queueing delay grows sharply as utilization approaches capacity.
- [[02 Concepts/Lifecycle/Deployment & Serving/Request Throughput|Request Throughput]] — The number of requests, or tokens, a serving system completes per unit time at a stated load and latency target.
- [[02 Concepts/Lifecycle/Deployment & Serving/Request Batching|Request Batching]] — Executing requests together to share work or improve resource use.
- [[02 Concepts/Lifecycle/Deployment & Serving/Continuous Batching|Continuous Batching]] — Scheduling at each generation iteration so finished sequences leave and new requests join a running batch.
- [[02 Concepts/Foundations/Quantitative System Models/Queueing Delay|Queueing Delay]] — Time a request waits for a resource before receiving service.
- [[02 Concepts/Foundations/Workloads & Requirements/Service Level Objective|Service Level Objective]] — A target for a defined service measure over a specified population and window.
- [[02 Concepts/Lifecycle/Deployment & Serving/SLO Goodput|SLO Goodput]] — The rate of useful completed work that satisfies the specified quality and service criteria.
- [[02 Concepts/Lifecycle/Deployment & Serving/Inter Token Latency|Inter Token Latency]] — The time between consecutive output tokens or chunks delivered to a streaming client, whose distribution, not only its mean, exposes decode stalls that an average time per output token hides.
- [[02 Concepts/System Types/Embodied & Physical Systems/Perception Latency Budget|Perception Latency Budget]] — The share of a robot's sense-to-act deadline allotted to sensing and perception, which bounds model size, input resolution, and frame rate on the onboard computer.

## Connected Book Passages

- [[01 Books/Volume I - Foundations/03 Optimization/12 Benchmarking/V1-12.07 Inference Benchmarks#^sec-benchmarking-latency-tail-latency-5cde|V1-12.07 Inference Benchmarks]]
- [[01 Books/Volume I - Foundations/04 Deployment/13 Model Serving/V1-13.04 Request Lifecycle#^sec-model-serving-request-lifecycle-d9c6|V1-13.04 Request Lifecycle]]
- [[01 Books/Volume I - Foundations/04 Deployment/13 Model Serving/V1-13.05 Queuing Theory#^sec-model-serving-utilizationlatency-relationship-a2f0|V1-13.05 Queuing Theory]]
- [[01 Books/Volume I - Foundations/04 Deployment/13 Model Serving/V1-13.06 Throughput Optimization#^sec-model-serving-batching-tax|V1-13.06 Throughput Optimization]]
- [[01 Books/Volume I - Foundations/04 Deployment/13 Model Serving/V1-13.10 LLM Serving#^sec-model-serving-continuous-batching-8bb6|V1-13.10 LLM Serving]]
- [[01 Books/Volume II - Scaling/03 The Fleet in Production/10 Serving at Scale/V2-10.04 SLO Goodput and the Serving Tax#^sec-inference-scale-fundamental-inversion-training-vs-inference-8834|V2-10.04 SLO Goodput and the Serving Tax]]
- [[01 Books/Volume II - Scaling/03 The Fleet in Production/10 Serving at Scale/V2-10.07 Batching Strategies at Scale#^sec-inference-scale-physics-batching-efficiency-curve-021c|V2-10.07 Batching Strategies at Scale]]
- [[01 Books/Volume II - Scaling/03 The Fleet in Production/12 ML Operations at Scale/V2-12.06 CI CD for ML at Scale#^sec-ops-scale-end-to-end-evaluation-contract|V2-12.06 CI CD for ML at Scale]]

## Navigation

[[00 Navigation/Topic Index|Topic Index]]
