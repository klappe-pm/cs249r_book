---
title: V2-10 Serving at Scale
type: Chapter
volume: 2
chapter: 10
publication_status: Preview
source_repository: https://github.com/klappe-pm/cs249r_book
source_commit: de87c0103806d7bfb1c677dbb77a2b92fa00c298
source_path: books/vol2/10_inference/10_inference.qmd
source_anchor: sec-inference-scale
source_mode: Source-Correlated Published HTML
tags:
- Type/Chapter
- Book/Volume_2
rendered_source_url: https://mlsysbook.ai/vol2/10_inference/10_inference.html
---

# V2-10 Serving at Scale

[[Home|Home]] · [[01 Books/Volume II - Scaling/Volume 2 Overview|Volume Overview]]

^sec-inference-scale

[Lecture slides](https://mlsysbook.ai/slides/vol2.html#ch-10) for this chapter

![[90 Assets/Volume II/10 Inference/Cover Inference Blueprint Labeled 11b288e744.webp]]

*Global inference blueprint where requests route through regional gateways, batching systems, cache pages, model shards, and fleet serving workers.*

## Chapter Sections

- [[01 Books/Volume II - Scaling/03 The Fleet in Production/10 Serving at Scale/V2-10.01 Purpose|V2-10.01 Purpose]]
- [[01 Books/Volume II - Scaling/03 The Fleet in Production/10 Serving at Scale/V2-10.02 Inference Cost and Serving Architecture|V2-10.02 Inference Cost and Serving Architecture]]
- [[01 Books/Volume II - Scaling/03 The Fleet in Production/10 Serving at Scale/V2-10.03 Limits of Single-Machine Serving|V2-10.03 Limits of Single-Machine Serving]]
- [[01 Books/Volume II - Scaling/03 The Fleet in Production/10 Serving at Scale/V2-10.04 SLO Goodput and the Serving Tax|V2-10.04 SLO Goodput and the Serving Tax]]
- [[01 Books/Volume II - Scaling/03 The Fleet in Production/10 Serving at Scale/V2-10.05 Serving Cost Dominance in Production|V2-10.05 Serving Cost Dominance in Production]]
- [[01 Books/Volume II - Scaling/03 The Fleet in Production/10 Serving at Scale/V2-10.06 Serving Workloads and the Serving Hierarchy|V2-10.06 Serving Workloads and the Serving Hierarchy]]
- [[01 Books/Volume II - Scaling/03 The Fleet in Production/10 Serving at Scale/V2-10.07 Batching Strategies at Scale|V2-10.07 Batching Strategies at Scale]]
- [[01 Books/Volume II - Scaling/03 The Fleet in Production/10 Serving at Scale/V2-10.08 Memory and Decode-Time Management|V2-10.08 Memory and Decode-Time Management]]
- [[01 Books/Volume II - Scaling/03 The Fleet in Production/10 Serving at Scale/V2-10.09 Prefill and Decode|V2-10.09 Prefill and Decode]]
- [[01 Books/Volume II - Scaling/03 The Fleet in Production/10 Serving at Scale/V2-10.10 Weight Quantization for Serving|V2-10.10 Weight Quantization for Serving]]
- [[01 Books/Volume II - Scaling/03 The Fleet in Production/10 Serving at Scale/V2-10.11 Model Sharding for Inference|V2-10.11 Model Sharding for Inference]]
- [[01 Books/Volume II - Scaling/03 The Fleet in Production/10 Serving at Scale/V2-10.12 Load Balancing and Request Routing|V2-10.12 Load Balancing and Request Routing]]
- [[01 Books/Volume II - Scaling/03 The Fleet in Production/10 Serving at Scale/V2-10.13 Multi-Tenancy and Isolation|V2-10.13 Multi-Tenancy and Isolation]]
- [[01 Books/Volume II - Scaling/03 The Fleet in Production/10 Serving at Scale/V2-10.14 Autoscaling and Capacity Control|V2-10.14 Autoscaling and Capacity Control]]
- [[01 Books/Volume II - Scaling/03 The Fleet in Production/10 Serving at Scale/V2-10.15 Global Inference Infrastructure|V2-10.15 Global Inference Infrastructure]]
- [[01 Books/Volume II - Scaling/03 The Fleet in Production/10 Serving at Scale/V2-10.16 Case Studies|V2-10.16 Case Studies]]
- [[01 Books/Volume II - Scaling/03 The Fleet in Production/10 Serving at Scale/V2-10.17 Fallacies and Pitfalls|V2-10.17 Fallacies and Pitfalls]]
- [[01 Books/Volume II - Scaling/03 The Fleet in Production/10 Serving at Scale/V2-10.18 Summary|V2-10.18 Summary]]
- [[01 Books/Volume II - Scaling/03 The Fleet in Production/10 Serving at Scale/V2-10.19 Self-Check Answers|V2-10.19 Self-Check Answers]]
- [[01 Books/Volume II - Scaling/03 The Fleet in Production/10 Serving at Scale/V2-10.20 Source References|V2-10.20 Source References]]
- [[01 Books/Volume II - Scaling/03 The Fleet in Production/10 Serving at Scale/V2-10.21 Footnotes|V2-10.21 Footnotes]]

Next: [[01 Books/Volume II - Scaling/03 The Fleet in Production/10 Serving at Scale/V2-10.01 Purpose|V2-10.01 Purpose]]

## Source

[Repository Source](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/books/vol2/10_inference/10_inference.qmd) · [Original License](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/LICENSE.md)

[Rendered Reading Snapshot](https://mlsysbook.ai/vol2/10_inference/10_inference.html#sec-inference-scale). Rendering provenance is recorded in the import manifest.

<!-- Semantic Navigation: Begin -->

## Connected Concepts

Explicit upstream passage alignments:

- [[02 Concepts/Lifecycle/Deployment & Serving/KV Cache|KV Cache]]
- [[02 Concepts/Lifecycle/Deployment & Serving/Request Batching|Request Batching]]
- [[02 Concepts/Lifecycle/Deployment & Serving/SLO Goodput|SLO Goodput]]

## Related Themes

- [[03 Themes/Latency and Throughput|Latency and Throughput]]
- [[03 Themes/Memory and Bandwidth|Memory and Bandwidth]]

## Earlier Connections

The source concept map records these touches connections. They are reading connections, not prerequisite requirements.

- [[01 Books/Volume II - Scaling/00 Introduction/01 Introduction/V2-01 Introduction|V2-01 Introduction]] — Fleet Law; Naming the efficiency measure.
- [[01 Books/Volume II - Scaling/01 The Fleet/02 Compute Infrastructure/V2-02 Compute Infrastructure|V2-02 Compute Infrastructure]] — Capacity and bandwidth are separate tests.
- [[01 Books/Volume II - Scaling/01 The Fleet/03 Network Fabrics/V2-03 Network Fabrics|V2-03 Network Fabrics]] — Alpha-beta model.
- [[01 Books/Volume II - Scaling/01 The Fleet/04 Data Storage/V2-04 Data Storage|V2-04 Data Storage]] — Hedged reads against storage tail latency.
- [[01 Books/Volume II - Scaling/02 Distributed ML/05 Collective Communication/V2-05 Collective Communication|V2-05 Collective Communication]] — Ring AllReduce and the bandwidth bound; AllToAll active bound.
- [[01 Books/Volume II - Scaling/02 Distributed ML/06 Distributed Training/V2-06 Distributed Training|V2-06 Distributed Training]] — Tensor parallelism in the fast domain; Pipeline parallelism bubble; Expert parallelism; Parallelism plan as joint placement; Sparse embedding sharding.
- [[01 Books/Volume II - Scaling/02 Distributed ML/07 Fault Tolerance/V2-07 Fault Tolerance|V2-07 Fault Tolerance]] — Serving replication sized to state; Graceful degradation ladder.
- [[01 Books/Volume II - Scaling/02 Distributed ML/08 Fleet Orchestration/V2-08 Fleet Orchestration|V2-08 Fleet Orchestration]] — Quota guarantees bounded by reclaim; Feasibility before fairness; Serving envelope and accelerator sharing; Interruption economics; Scheduling objectives and matched signals.
- [[01 Books/Volume II - Scaling/03 The Fleet in Production/09 Fleet Efficiency/V2-09 Fleet Efficiency|V2-09 Fleet Efficiency]] — ML goodput; Tensor-parallel collectives under contention; Reproducible measurement contract.

[Chapter Concept Map](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/books/vol2/10_inference/inference_concepts.yml)

## Continuing Connections

The source concept map records these previews connections. They are reading connections, not prerequisite requirements.

- [[01 Books/Volume II - Scaling/03 The Fleet in Production/11 Edge Intelligence/V2-11 Edge Intelligence|V2-11 Edge Intelligence]] — Adaptation method by budget term; Local training must earn its place.
- [[01 Books/Volume II - Scaling/03 The Fleet in Production/12 ML Operations at Scale/V2-12 ML Operations at Scale|V2-12 ML Operations at Scale]] — Staged rollout exposure budget.
- [[01 Books/Volume II - Scaling/04 The Responsible Fleet/13 Security & Privacy/V2-13 Security & Privacy|V2-13 Security & Privacy]] — Security controls priced on a C3 axis.

[Chapter Concept Map](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/books/vol2/10_inference/inference_concepts.yml)

<!-- Semantic Navigation: End -->
