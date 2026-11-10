---
title: V2-04 Data Storage
type: Chapter
volume: 2
chapter: 4
publication_status: Preview
source_repository: https://github.com/klappe-pm/cs249r_book
source_commit: de87c0103806d7bfb1c677dbb77a2b92fa00c298
source_path: books/vol2/04_data_storage/04_data_storage.qmd
source_anchor: sec-data-storage
source_mode: Source-Correlated Published HTML
tags:
- Type/Chapter
- Book/Volume_2
rendered_source_url: https://mlsysbook.ai/vol2/04_data_storage/04_data_storage.html
---

# V2-04 Data Storage

[[Home|Home]] · [[01 Books/Volume II - Scaling/Volume 2 Overview|Volume Overview]]

^sec-data-storage

[Lecture slides](https://mlsysbook.ai/slides/vol2.html#ch-04) for this chapter

![[90 Assets/Volume II/04 Data Storage/Cover Data Storage Blueprint Labeled ed2a0e7b4b.webp]]

*Fleet storage fuel-line hierarchy where data moves from object storage through NVMe, DRAM, and HBM tiers into accelerator workers.*

## Chapter Sections

- [[01 Books/Volume II - Scaling/01 The Fleet/04 Data Storage/V2-04.01 Purpose|V2-04.01 Purpose]]
- [[01 Books/Volume II - Scaling/01 The Fleet/04 Data Storage/V2-04.02 The Fuel Line|V2-04.02 The Fuel Line]]
- [[01 Books/Volume II - Scaling/01 The Fleet/04 Data Storage/V2-04.03 How ML Workloads Invert Storage Assumptions|V2-04.03 How ML Workloads Invert Storage Assumptions]]
- [[01 Books/Volume II - Scaling/01 The Fleet/04 Data Storage/V2-04.04 The ML Storage Hierarchy|V2-04.04 The ML Storage Hierarchy]]
- [[01 Books/Volume II - Scaling/01 The Fleet/04 Data Storage/V2-04.05 The Data Pipeline Equation|V2-04.05 The Data Pipeline Equation]]
- [[01 Books/Volume II - Scaling/01 The Fleet/04 Data Storage/V2-04.06 GPUDirect Storage and the CPU Data-Copy Bypass|V2-04.06 GPUDirect Storage and the CPU Data-Copy Bypass]]
- [[01 Books/Volume II - Scaling/01 The Fleet/04 Data Storage/V2-04.07 Checkpoint Storage|V2-04.07 Checkpoint Storage]]
- [[01 Books/Volume II - Scaling/01 The Fleet/04 Data Storage/V2-04.08 Versioned Data and Commit Boundaries|V2-04.08 Versioned Data and Commit Boundaries]]
- [[01 Books/Volume II - Scaling/01 The Fleet/04 Data Storage/V2-04.09 Storage Economics|V2-04.09 Storage Economics]]
- [[01 Books/Volume II - Scaling/01 The Fleet/04 Data Storage/V2-04.10 Storage for Serving|V2-04.10 Storage for Serving]]
- [[01 Books/Volume II - Scaling/01 The Fleet/04 Data Storage/V2-04.11 Storage Technologies That Move Tiers|V2-04.11 Storage Technologies That Move Tiers]]
- [[01 Books/Volume II - Scaling/01 The Fleet/04 Data Storage/V2-04.12 Fallacies and Pitfalls|V2-04.12 Fallacies and Pitfalls]]
- [[01 Books/Volume II - Scaling/01 The Fleet/04 Data Storage/V2-04.13 Summary|V2-04.13 Summary]]
- [[01 Books/Volume II - Scaling/01 The Fleet/04 Data Storage/V2-04.14 Self-Check Answers|V2-04.14 Self-Check Answers]]
- [[01 Books/Volume II - Scaling/01 The Fleet/04 Data Storage/V2-04.15 Source References|V2-04.15 Source References]]
- [[01 Books/Volume II - Scaling/01 The Fleet/04 Data Storage/V2-04.16 Footnotes|V2-04.16 Footnotes]]

Next: [[01 Books/Volume II - Scaling/01 The Fleet/04 Data Storage/V2-04.01 Purpose|V2-04.01 Purpose]]

## Source

[Repository Source](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/books/vol2/04_data_storage/04_data_storage.qmd) · [Original License](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/LICENSE.md)

[Rendered Reading Snapshot](https://mlsysbook.ai/vol2/04_data_storage/04_data_storage.html#sec-data-storage). Rendering provenance is recorded in the import manifest.

<!-- Semantic Navigation: Begin -->

## Connected Concepts

Explicit upstream passage alignments:

- [[02 Concepts/Lifecycle/MLOps & Operations/Artifact Versioning|Artifact Versioning]]
- [[02 Concepts/Stack/Frameworks, Compilers & Runtimes/Input Prefetching|Input Prefetching]]
- [[02 Concepts/Qualities/Reliability & Fault Tolerance/Recovery Checkpoint|Recovery Checkpoint]]
- [[02 Concepts/Stack/Frameworks, Compilers & Runtimes/Training Input Pipeline|Training Input Pipeline]]

## Related Themes

- [[03 Themes/Reliability and Recovery|Reliability and Recovery]]

## Earlier Connections

The source concept map records these touches connections. They are reading connections, not prerequisite requirements.

- [[01 Books/Volume II - Scaling/00 Introduction/01 Introduction/V2-01 Introduction|V2-01 Introduction]] — Scaling laws as the demand curve; Compute-optimal allocation; Fleet Law; C3 taxonomy.
- [[01 Books/Volume II - Scaling/01 The Fleet/02 Compute Infrastructure/V2-02 Compute Infrastructure|V2-02 Compute Infrastructure]] — Node aggregates private memories; Capacity and bandwidth are separate tests.
- [[01 Books/Volume II - Scaling/01 The Fleet/03 Network Fabrics/V2-03 Network Fabrics|V2-03 Network Fabrics]] — Fabric sharing and isolation; RDMA reliable-delivery contract.

[Chapter Concept Map](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/books/vol2/04_data_storage/data_storage_concepts.yml)

## Continuing Connections

The source concept map records these previews connections. They are reading connections, not prerequisite requirements.

- [[01 Books/Volume II - Scaling/02 Distributed ML/06 Distributed Training/V2-06 Distributed Training|V2-06 Distributed Training]] — Sharded data parallelism; Sparse embedding sharding.
- [[01 Books/Volume II - Scaling/02 Distributed ML/07 Fault Tolerance/V2-07 Fault Tolerance|V2-07 Fault Tolerance]] — Young-Daly checkpoint interval; Consistent checkpoint cut; Silent data corruption verification.
- [[01 Books/Volume II - Scaling/03 The Fleet in Production/10 Serving at Scale/V2-10 Serving at Scale|V2-10 Serving at Scale]] — KV cache as admission budget; Phase-aware autoscaling and cold start.
- [[01 Books/Volume II - Scaling/03 The Fleet in Production/12 ML Operations at Scale/V2-12 ML Operations at Scale|V2-12 ML Operations at Scale]] — Feature consistency contract; Lifecycle TCO.

[Chapter Concept Map](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/books/vol2/04_data_storage/data_storage_concepts.yml)

<!-- Semantic Navigation: End -->
