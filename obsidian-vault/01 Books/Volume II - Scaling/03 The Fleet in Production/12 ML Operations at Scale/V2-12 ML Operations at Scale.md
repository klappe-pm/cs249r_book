---
title: V2-12 ML Operations at Scale
type: Chapter
volume: 2
chapter: 12
publication_status: Preview
source_repository: https://github.com/klappe-pm/cs249r_book
source_commit: de87c0103806d7bfb1c677dbb77a2b92fa00c298
source_path: books/vol2/12_ops_scale/12_ops_scale.qmd
source_anchor: sec-ops-scale
source_mode: Source-Correlated Published HTML
tags:
- Type/Chapter
- Book/Volume_2
rendered_source_url: https://mlsysbook.ai/vol2/12_ops_scale/12_ops_scale.html
---

# V2-12 ML Operations at Scale

[[Home|Home]] · [[01 Books/Volume II - Scaling/Volume 2 Overview|Volume Overview]]

^sec-ops-scale

[Lecture slides](https://mlsysbook.ai/slides/vol2.html#ch-12) for this chapter

![[90 Assets/Volume II/12 Ops Scale/Cover Ops Scale Blueprint Labeled f3903dce58.webp]]

*Fleet operations platform blueprint where many model-service lanes share observability, deployment, policy, and capacity control layers.*

## Chapter Sections

- [[01 Books/Volume II - Scaling/03 The Fleet in Production/12 ML Operations at Scale/V2-12.01 Purpose|V2-12.01 Purpose]]
- [[01 Books/Volume II - Scaling/03 The Fleet in Production/12 ML Operations at Scale/V2-12.02 Why a Model Fleet Needs a Control Plane|V2-12.02 Why a Model Fleet Needs a Control Plane]]
- [[01 Books/Volume II - Scaling/03 The Fleet in Production/12 ML Operations at Scale/V2-12.03 The N-Models Problem|V2-12.03 The N-Models Problem]]
- [[01 Books/Volume II - Scaling/03 The Fleet in Production/12 ML Operations at Scale/V2-12.04 Governance of State and Change|V2-12.04 Governance of State and Change]]
- [[01 Books/Volume II - Scaling/03 The Fleet in Production/12 ML Operations at Scale/V2-12.05 Feature Store Operations|V2-12.05 Feature Store Operations]]
- [[01 Books/Volume II - Scaling/03 The Fleet in Production/12 ML Operations at Scale/V2-12.06 CI CD for ML at Scale|V2-12.06 CI CD for ML at Scale]]
- [[01 Books/Volume II - Scaling/03 The Fleet in Production/12 ML Operations at Scale/V2-12.07 Monitoring at Scale|V2-12.07 Monitoring at Scale]]
- [[01 Books/Volume II - Scaling/03 The Fleet in Production/12 ML Operations at Scale/V2-12.08 Production Debugging and Incident Response|V2-12.08 Production Debugging and Incident Response]]
- [[01 Books/Volume II - Scaling/03 The Fleet in Production/12 ML Operations at Scale/V2-12.09 Platform Engineering|V2-12.09 Platform Engineering]]
- [[01 Books/Volume II - Scaling/03 The Fleet in Production/12 ML Operations at Scale/V2-12.10 Fleet Economics and Utilization|V2-12.10 Fleet Economics and Utilization]]
- [[01 Books/Volume II - Scaling/03 The Fleet in Production/12 ML Operations at Scale/V2-12.11 Organizational Operation and Learning|V2-12.11 Organizational Operation and Learning]]
- [[01 Books/Volume II - Scaling/03 The Fleet in Production/12 ML Operations at Scale/V2-12.12 Case Studies|V2-12.12 Case Studies]]
- [[01 Books/Volume II - Scaling/03 The Fleet in Production/12 ML Operations at Scale/V2-12.13 Fallacies and Pitfalls|V2-12.13 Fallacies and Pitfalls]]
- [[01 Books/Volume II - Scaling/03 The Fleet in Production/12 ML Operations at Scale/V2-12.14 Summary|V2-12.14 Summary]]
- [[01 Books/Volume II - Scaling/03 The Fleet in Production/12 ML Operations at Scale/V2-12.15 Self-Check Answers|V2-12.15 Self-Check Answers]]
- [[01 Books/Volume II - Scaling/03 The Fleet in Production/12 ML Operations at Scale/V2-12.16 Source References|V2-12.16 Source References]]
- [[01 Books/Volume II - Scaling/03 The Fleet in Production/12 ML Operations at Scale/V2-12.17 Footnotes|V2-12.17 Footnotes]]

Next: [[01 Books/Volume II - Scaling/03 The Fleet in Production/12 ML Operations at Scale/V2-12.01 Purpose|V2-12.01 Purpose]]

## Source

[Repository Source](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/books/vol2/12_ops_scale/12_ops_scale.qmd) · [Original License](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/LICENSE.md)

[Rendered Reading Snapshot](https://mlsysbook.ai/vol2/12_ops_scale/12_ops_scale.html#sec-ops-scale). Rendering provenance is recorded in the import manifest.

<!-- Semantic Navigation: Begin -->

## Connected Concepts

Explicit upstream passage alignments:

- [[02 Concepts/Lifecycle/MLOps & Operations/Model Registry|Model Registry]]
- [[02 Concepts/Lifecycle/MLOps & Operations/Release Gate|Release Gate]]
- [[02 Concepts/Foundations/Workloads & Requirements/Service Level Objective|Service Level Objective]]
- [[02 Concepts/Lifecycle/MLOps & Operations/Staged Rollout|Staged Rollout]]

## Related Themes

- [[03 Themes/Constraints Drive Architecture|Constraints Drive Architecture]]
- [[03 Themes/Latency and Throughput|Latency and Throughput]]

## Earlier Connections

The source concept map records these touches connections. They are reading connections, not prerequisite requirements.

- [[01 Books/Volume II - Scaling/00 Introduction/01 Introduction/V2-01 Introduction|V2-01 Introduction]] — Fleet Law; Naming the efficiency measure; Compute-optimal allocation.
- [[01 Books/Volume II - Scaling/01 The Fleet/02 Compute Infrastructure/V2-02 Compute Infrastructure|V2-02 Compute Infrastructure]] — Rack power wall; Arithmetic per watt at fixed precision; Node aggregates private memories; Pod sizing from the training budget.
- [[01 Books/Volume II - Scaling/01 The Fleet/03 Network Fabrics/V2-03 Network Fabrics|V2-03 Network Fabrics]] — Bisection bandwidth and topology economics; Fabric sharing and isolation; Fabric behavior under load.
- [[01 Books/Volume II - Scaling/01 The Fleet/04 Data Storage/V2-04 Data Storage|V2-04 Data Storage]] — Versioned artifacts and commit boundaries.
- [[01 Books/Volume II - Scaling/02 Distributed ML/06 Distributed Training/V2-06 Distributed Training|V2-06 Distributed Training]] — Sharded data parallelism.
- [[01 Books/Volume II - Scaling/02 Distributed ML/07 Fault Tolerance/V2-07 Fault Tolerance|V2-07 Fault Tolerance]] — Fleet failure rate; Young-Daly checkpoint interval; Recovery-time budget and fencing; Gray failure detection; Serving replication sized to state.
- [[01 Books/Volume II - Scaling/02 Distributed ML/08 Fleet Orchestration/V2-08 Fleet Orchestration|V2-08 Fleet Orchestration]] — Utilization tiers; Quota guarantees bounded by reclaim; Interruption economics.
- [[01 Books/Volume II - Scaling/03 The Fleet in Production/09 Fleet Efficiency/V2-09 Fleet Efficiency|V2-09 Fleet Efficiency]] — ML goodput.
- [[01 Books/Volume II - Scaling/03 The Fleet in Production/10 Serving at Scale/V2-10 Serving at Scale|V2-10 Serving at Scale]] — Prefill-decode interference and chunked prefill; Serving cost dominance; SLO goodput and the serving tax; Batch formation trades waiting for reuse; Phase-aware autoscaling and cold start; Token-denominated tenant isolation.
- [[01 Books/Volume II - Scaling/03 The Fleet in Production/11 Edge Intelligence/V2-11 Edge Intelligence|V2-11 Edge Intelligence]] — Participation selection; Adaptive fleet release policy.

[Chapter Concept Map](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/books/vol2/12_ops_scale/ops_scale_concepts.yml)

## Continuing Connections

The source concept map records these previews connections. They are reading connections, not prerequisite requirements.

- [[01 Books/Volume II - Scaling/04 The Responsible Fleet/13 Security & Privacy/V2-13 Security & Privacy|V2-13 Security & Privacy]] — ML threat model.
- [[01 Books/Volume II - Scaling/04 The Responsible Fleet/14 Robust AI/V2-14 Robust AI|V2-14 Robust AI]] — Shift taxonomy; Drift alert to model update; Robustness per failure class.
- [[01 Books/Volume II - Scaling/04 The Responsible Fleet/15 Sustainable AI/V2-15 Sustainable AI|V2-15 Sustainable AI]] — Operational carbon chain.
- [[01 Books/Volume II - Scaling/04 The Responsible Fleet/16 Responsible AI/V2-16 Responsible AI|V2-16 Responsible AI]] — Fairness criteria conflict; Assurance case.

[Chapter Concept Map](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/books/vol2/12_ops_scale/ops_scale_concepts.yml)

<!-- Semantic Navigation: End -->
