---
title: Scaling and Coordination
type: theme
tags:
- Type/Theme
- Theme/Scaling_and_Coordination
source_repository: https://github.com/klappe-pm/cs249r_book
source_commit: de87c0103806d7bfb1c677dbb77a2b92fa00c298
source_path: taxonomy/taxonomy.yml
editorial_scope: Curated Navigation Lens
---

# Scaling and Coordination

Follow partitioning and synchronization costs across accelerator fleets and multi-agent systems.

This curated navigation lens is an editorial association, not a claim of dependency or equivalence.

## Concepts

- [[02 Concepts/Stack/Parallelism & Distributed Execution/Data Parallelism|Data Parallelism]] — Executing model replicas on different examples while coordinating learning state.
- [[02 Concepts/Stack/Parallelism & Distributed Execution/Tensor Parallelism|Tensor Parallelism]] — Partitioning a layer's tensors and operations across devices so each computes a slice, reducing per-device state while adding communication along the partitioned dimensions, usually within a fast scale-up domain.
- [[02 Concepts/Stack/Parallelism & Distributed Execution/Pipeline Parallelism|Pipeline Parallelism]] — Partitioning a computation into stages that process different microbatches concurrently.
- [[02 Concepts/Stack/Parallelism & Distributed Execution/Expert Parallelism|Expert Parallelism]] — Placing different experts of a mixture-of-experts layer on different devices and exchanging routed tokens among them.
- [[02 Concepts/Stack/Parallelism & Distributed Execution/Sequence and Context Parallelism|Sequence and Context Parallelism]] — Partitioning activations along the sequence dimension across devices, exchanging keys, values, or partial results so long sequences fit.
- [[02 Concepts/Stack/Parallelism & Distributed Execution/Hybrid Parallelism|Hybrid Parallelism]] — Combining data, tensor, pipeline, and other parallelism dimensions, mapped onto the hardware hierarchy so the most communication-intensive dimension uses the fastest links.
- [[02 Concepts/Stack/Parallelism & Distributed Execution/All Reduce|All Reduce]] — A collective in which every participant ends with the same reduction, usually the sum, of all participants' equal-shaped tensors, the operation that synchronizes gradients across replicas in data-parallel training.
- [[02 Concepts/Foundations/Quantitative System Models/Parallel Scaling Efficiency|Parallel Scaling Efficiency]] — Achieved speedup divided by the factor of added resources, measuring how much additional hardware turns into useful progress.
- [[02 Concepts/Stack/Datacenter Infrastructure & Fleet/Bisection Bandwidth|Bisection Bandwidth]] — The minimum total bandwidth across any cut dividing a network into two equal halves, bounding throughput of all-to-all and global exchanges.
- [[02 Concepts/System Types/Agentic Systems/Multi Agent Coordination Failure|Multi Agent Coordination Failure]] — Task failure arising from interaction among agents, such as mis-specified delegation, lost context at handoff, conflicting actions, or premature termination.

## Connected Book Passages

- [[01 Books/Volume II - Scaling/00 Introduction/01 Introduction/V2-01.06 The C³ Taxonomy and Foundations of Scale#^sec-vol2-introduction-fleet-law|V2-01.06 The C³ Taxonomy and Foundations of Scale]]
- [[01 Books/Volume II - Scaling/01 The Fleet/03 Network Fabrics/V2-03.06 Level 3 Switch and Topology#^sec-network-fabrics-topology|V2-03.06 Level 3 Switch and Topology]]
- [[01 Books/Volume II - Scaling/02 Distributed ML/06 Distributed Training/V2-06.04 Data Parallelism#^sec-distributed-training-systems-systems-data-parallelism-6132|V2-06.04 Data Parallelism]]
- [[01 Books/Volume II - Scaling/02 Distributed ML/06 Distributed Training/V2-06.06 Model Parallelism#^sec-distributed-training-systems-systems-pipeline-parallelism-8748|V2-06.06 Model Parallelism]]

## Navigation

[[00 Navigation/Topic Index|Topic Index]]
