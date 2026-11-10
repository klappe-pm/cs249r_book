---
title: V2-02 Compute Infrastructure
type: Chapter
volume: 2
chapter: 2
publication_status: Preview
source_repository: https://github.com/klappe-pm/cs249r_book
source_commit: de87c0103806d7bfb1c677dbb77a2b92fa00c298
source_path: books/vol2/02_compute_infrastructure/02_compute_infrastructure.qmd
source_anchor: sec-compute-infrastructure
source_mode: Source-Correlated Published HTML
tags:
- Type/Chapter
- Book/Volume_2
rendered_source_url: https://mlsysbook.ai/vol2/02_compute_infrastructure/02_compute_infrastructure.html
---

# V2-02 Compute Infrastructure

[[Home|Home]] · [[01 Books/Volume II - Scaling/Volume 2 Overview|Volume Overview]]

^sec-compute-infrastructure

[Lecture slides](https://mlsysbook.ai/slides/vol2.html#ch-02) for this chapter

![[90 Assets/Volume II/02 Compute Infrastructure/Cover Compute Infrastructure Blueprint Labeled 6d1b2e19af.webp]]

*Layered compute infrastructure cutaway from accelerator chip and HBM to server nodes, racks, power delivery, and cooling loops.*

## Chapter Sections

- [[01 Books/Volume II - Scaling/01 The Fleet/02 Compute Infrastructure/V2-02.01 Purpose|V2-02.01 Purpose]]
- [[01 Books/Volume II - Scaling/01 The Fleet/02 Compute Infrastructure/V2-02.02 The Infrastructure Walls|V2-02.02 The Infrastructure Walls]]
- [[01 Books/Volume II - Scaling/01 The Fleet/02 Compute Infrastructure/V2-02.03 The Accelerator|V2-02.03 The Accelerator]]
- [[01 Books/Volume II - Scaling/01 The Fleet/02 Compute Infrastructure/V2-02.04 The Memory Wall|V2-02.04 The Memory Wall]]
- [[01 Books/Volume II - Scaling/01 The Fleet/02 Compute Infrastructure/V2-02.05 Sustained Compute and Precision|V2-02.05 Sustained Compute and Precision]]
- [[01 Books/Volume II - Scaling/01 The Fleet/02 Compute Infrastructure/V2-02.06 The Node|V2-02.06 The Node]]
- [[01 Books/Volume II - Scaling/01 The Fleet/02 Compute Infrastructure/V2-02.07 The Rack|V2-02.07 The Rack]]
- [[01 Books/Volume II - Scaling/01 The Fleet/02 Compute Infrastructure/V2-02.08 The Pod|V2-02.08 The Pod]]
- [[01 Books/Volume II - Scaling/01 The Fleet/02 Compute Infrastructure/V2-02.09 Accelerator Selection for Fleet Workloads|V2-02.09 Accelerator Selection for Fleet Workloads]]
- [[01 Books/Volume II - Scaling/01 The Fleet/02 Compute Infrastructure/V2-02.10 Infrastructure Technologies That Move the Walls|V2-02.10 Infrastructure Technologies That Move the Walls]]
- [[01 Books/Volume II - Scaling/01 The Fleet/02 Compute Infrastructure/V2-02.11 Fallacies and Pitfalls|V2-02.11 Fallacies and Pitfalls]]
- [[01 Books/Volume II - Scaling/01 The Fleet/02 Compute Infrastructure/V2-02.12 Summary|V2-02.12 Summary]]
- [[01 Books/Volume II - Scaling/01 The Fleet/02 Compute Infrastructure/V2-02.13 Self-Check Answers|V2-02.13 Self-Check Answers]]
- [[01 Books/Volume II - Scaling/01 The Fleet/02 Compute Infrastructure/V2-02.14 Source References|V2-02.14 Source References]]
- [[01 Books/Volume II - Scaling/01 The Fleet/02 Compute Infrastructure/V2-02.15 Footnotes|V2-02.15 Footnotes]]

Next: [[01 Books/Volume II - Scaling/01 The Fleet/02 Compute Infrastructure/V2-02.01 Purpose|V2-02.01 Purpose]]

## Source

[Repository Source](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/books/vol2/02_compute_infrastructure/02_compute_infrastructure.qmd) · [Original License](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/LICENSE.md)

[Rendered Reading Snapshot](https://mlsysbook.ai/vol2/02_compute_infrastructure/02_compute_infrastructure.html#sec-compute-infrastructure). Rendering provenance is recorded in the import manifest.

<!-- Semantic Navigation: Begin -->

## Connected Concepts

Explicit upstream passage alignments:

- [[02 Concepts/Stack/Hardware & Accelerators/Memory Capacity|Memory Capacity]]
- [[02 Concepts/Stack/Datacenter Infrastructure & Fleet/Rack Power Density|Rack Power Density]]

## Related Themes

- [[03 Themes/Constraints Drive Architecture|Constraints Drive Architecture]]
- [[03 Themes/Memory and Bandwidth|Memory and Bandwidth]]

## Earlier Connections

The source concept map records these touches connections. They are reading connections, not prerequisite requirements.

- [[01 Books/Volume II - Scaling/00 Introduction/01 Introduction/V2-01 Introduction|V2-01 Introduction]] — Scale moment; Scaling laws as the demand curve; Compute-optimal allocation; C3 taxonomy; Fleet Law; Reliability gap.

[Chapter Concept Map](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/books/vol2/02_compute_infrastructure/compute_infrastructure_concepts.yml)

## Continuing Connections

The source concept map records these previews connections. They are reading connections, not prerequisite requirements.

- [[01 Books/Volume II - Scaling/01 The Fleet/03 Network Fabrics/V2-03 Network Fabrics|V2-03 Network Fabrics]] — Alpha-beta model; RDMA reliable-delivery contract; Traffic-matched topology; Bisection bandwidth and topology economics.
- [[01 Books/Volume II - Scaling/01 The Fleet/04 Data Storage/V2-04 Data Storage|V2-04 Data Storage]] — Input delivery budget.
- [[01 Books/Volume II - Scaling/02 Distributed ML/05 Collective Communication/V2-05 Collective Communication|V2-05 Collective Communication]] — Ring AllReduce and the bandwidth bound; Data-movement energy per boundary.
- [[01 Books/Volume II - Scaling/02 Distributed ML/06 Distributed Training/V2-06 Distributed Training|V2-06 Distributed Training]] — Sharded data parallelism; Pipeline parallelism bubble; Tensor parallelism in the fast domain.
- [[01 Books/Volume II - Scaling/02 Distributed ML/07 Fault Tolerance/V2-07 Fault Tolerance|V2-07 Fault Tolerance]] — Fleet failure rate; Gray failure detection; Recovery-time budget and fencing.
- [[01 Books/Volume II - Scaling/02 Distributed ML/08 Fleet Orchestration/V2-08 Fleet Orchestration|V2-08 Fleet Orchestration]] — Topology-aware placement.
- [[01 Books/Volume II - Scaling/03 The Fleet in Production/09 Fleet Efficiency/V2-09 Fleet Efficiency|V2-09 Fleet Efficiency]] — Program goodput.
- [[01 Books/Volume II - Scaling/03 The Fleet in Production/10 Serving at Scale/V2-10 Serving at Scale|V2-10 Serving at Scale]] — Prefill-decode interference and chunked prefill.
- [[01 Books/Volume II - Scaling/03 The Fleet in Production/11 Edge Intelligence/V2-11 Edge Intelligence|V2-11 Edge Intelligence]] — Update working set within the background allowance.
- [[01 Books/Volume II - Scaling/03 The Fleet in Production/12 ML Operations at Scale/V2-12 ML Operations at Scale|V2-12 ML Operations at Scale]] — Utilization as the economic invariant.
- [[01 Books/Volume II - Scaling/04 The Responsible Fleet/15 Sustainable AI/V2-15 Sustainable AI|V2-15 Sustainable AI]] — Facility overhead boundary.

[Chapter Concept Map](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/books/vol2/02_compute_infrastructure/compute_infrastructure_concepts.yml)

<!-- Semantic Navigation: End -->
