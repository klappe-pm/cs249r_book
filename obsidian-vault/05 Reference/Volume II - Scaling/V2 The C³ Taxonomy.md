---
title: V2 The C³ Taxonomy
type: Reference
volume: 2
chapter: 0
publication_status: Preview
source_repository: https://github.com/klappe-pm/cs249r_book
source_commit: de87c0103806d7bfb1c677dbb77a2b92fa00c298
source_path: books/vol2/backmatter/appendix_c3.qmd
source_anchor: sec-appdx-c3-taxonomy
source_mode: Published HTML With Restored Source Headings
tags:
- Type/Reference
- Book/Volume_2
rendered_source_url: https://mlsysbook.ai/vol2/backmatter/appendix_c3.html
---

# V2 The C³ Taxonomy

[[Home|Home]] · [[01 Books/Volume II - Scaling/Volume 2 Overview|Volume Overview]]

^sec-appdx-c3-taxonomy

In a distributed training cluster, “it is slow” is even less informative than on a single machine. A job can stall because accelerators are underutilized (Compute), gradient synchronization saturates interconnects (Communication), or checkpointing and recovery delay progress (Coordination). This appendix extends single-node diagnostics to fleet-scale infrastructure, providing the C$^3$ scorecard used throughout the book to isolate the binding bottleneck across distributed systems.

## How to Use This Appendix

^how-to-use-this-appendix

This appendix is designed as a symptom-first reference for fleet-scale diagnosis. Start with the observed failure mode, form a hypothesis about which C$^3$ axis dominates, and select the measurement that confirms or falsifies that hypothesis:

- **When training throughput is low**: Check model FLOPs utilization (MFU), communication fraction, and runtime goodput in the diagnostic summary ([[05 Reference/Volume II - Scaling/V2 The C³ Taxonomy#^sec-appdx-c3-taxonomy-diagnostic-summary|section 1.2]]) and traffic light thresholds ([[05 Reference/Volume II - Scaling/V2 The C³ Taxonomy#^sec-appdx-c3-taxonomy-traffic-light|section 1.4.7]]) to isolate the compute, communication, or coordination axis.
- **When scaling efficiency drops as GPUs are added**: Use the Fleet Law decomposition ([[05 Reference/Volume II - Scaling/V2 The C³ Taxonomy#^sec-appdx-c3-taxonomy-fleet-law|section 1.3]]) and the intersection landscape ([[05 Reference/Volume II - Scaling/V2 The C³ Taxonomy#^sec-appdx-c3-taxonomy-intersection-landscape|section 1.4]]) to identify which noncompute term grew.
- **When a production job stalls, restarts, or fires hardware alerts**: Match the symptom in the troubleshooting matrix ([[05 Reference/Volume II - Scaling/V2 The C³ Taxonomy#^sec-appdx-c3-taxonomy-production-troubleshooting|section 1.6]]), select a profiler from the tooling map ([[05 Reference/Volume II - Scaling/V2 The C³ Taxonomy#^sec-appdx-c3-taxonomy-tooling-map|section 1.7]]), or trace silicon counters through the telemetry decision tree ([[05 Reference/Volume II - Scaling/V2 The C³ Taxonomy#^sec-appdx-c3-diagnostic-tree|section 1.9]]).
- **When translating a scaling-law compute budget into cluster capacity**: Use the C$^3$ scorecard ([[05 Reference/Volume II - Scaling/V2 The C³ Taxonomy#^sec-appdx-c3-taxonomy-scorecard|section 1.8]]) and the effective FLOP/s model ([[05 Reference/Volume II - Scaling/V2 The C³ Taxonomy#^sec-appdx-c3-taxonomy-scaling-laws|section 1.10]]) so optimization effort targets the dominant loss term rather than a nonbottleneck.

## From D·A·M to C³

^sec-appdx-c3-taxonomy-from-dam

Where the single-machine D·A·M framework (**[[05 Reference/Volume II - Scaling/V2 Single-Machine Foundations#^sec-appdx-dam-taxonomy|The D·A·M Taxonomy]]**) diagnoses bottlenecks within one node (data starvation, algorithmic overhead, or hardware saturation), a distributed job can stall even when every individual node is healthy. The **C$^3$ taxonomy** is the diagnostic framework for fleet-scale ML systems engineering. It isolates the dominant cluster-level axis across Compute (whether the accelerators are doing useful math), Communication (whether the network is moving data fast enough), and Coordination (whether the system is spending too much time on synchronization, failure recovery, and scheduling), along with the intersections between them. Rather than replacing D·A·M, C$^3$ extends each single-machine axis to the new failure modes that appear when a workload spans a fleet ([[05 Reference/Volume II - Scaling/V2 The C³ Taxonomy#^tbl-c3-dam-mapping|table 1]]).

| **D·A·M axis** | **Single-machine concern**          | **C$^3$ extension**  | **What changes at fleet scale**                                                                                      |
|:---------------|:------------------------------------|:---------------------|:---------------------------------------------------------------------------------------------------------------------|
| **Data**       | Host disk $\to$ GPU memory pipeline | Communication        | Data movement crosses network fabrics; AllReduce, AllGather, and pipeline transfers dominate                         |
| **Algorithm**  | Operator choice, autograd graph     | Compute/Coordination | Workload must be partitioned (${N}$-way sharding); communication-to-compute ratio determines scaling                 |
| **Machine**    | SM occupancy, HBM bandwidth         | Coordination         | Single-device faults become cluster-wide stragglers; failure recovery, scheduling, and power density constrain ${N}$ |

Table 1: **Mapping D·A·M to C$^3$**: How single-machine diagnostic concerns generalize to fleet-scale challenges.

^tbl-c3-dam-mapping

The most important row in [[05 Reference/Volume II - Scaling/V2 The C³ Taxonomy#^tbl-c3-dam-mapping|table 1]] is the last one. On a single machine, the overhead term (${L_{\text{lat}}}$) in the iron law is typically small, consisting of kernel launch latency, Python dispatch, and synchronization barriers. At fleet scale, coordination becomes an axis in its own right: checkpoint writes, failure detection and recovery, pipeline bubble overhead, scheduler preemptions, and maintenance windows collectively consume a significant fraction of wall time. Coordination is the axis that single-machine diagnosis lacks, and much of this book is devoted to it.

## Diagnostic Summary

^sec-appdx-c3-taxonomy-diagnostic-summary

When a distributed training job runs below expected throughput, the symptom appears first as idle tensor cores, exposed collective transfers, or frequent barrier and restart stalls. Matching that symptom to the C$^3$ axis that constrains the fleet links each physical bottleneck directly to its headline metric and highest-leverage optimization ([[05 Reference/Volume II - Scaling/V2 The C³ Taxonomy#^tbl-c3-diagnostic-summary|table 2]]).

| **C$^3$ axis**              | **Physical constraint**                                               | **Symptoms**                                                                    | **Key metric**                                                                                                           | **High-leverage optimization**                                                                                                                                                                                                                                                                                                                             |
|:----------------------------|:----------------------------------------------------------------------|:--------------------------------------------------------------------------------|:-------------------------------------------------------------------------------------------------------------------------|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Compute (${C_1}$)**       | Arithmetic throughput (${R_{\text{peak}}} \times {\eta_{\text{hw}}}$) | Low MFU, GPU utilization below 80%, poor per-GPU performance                    | MFU (Model FLOPs Utilization)                                                                                            | Kernel-level levers (**[[05 Reference/Volume II - Scaling/V2 Single-Machine Foundations#^sec-appdx-dam-taxonomy-kernel-levers\|Kernel-Level Levers]]**), mixed precision, program goodput levers (**[[01 Books/Volume II - Scaling/03 The Fleet in Production/09 Fleet Efficiency/V2-09.08 Recovering Program Goodput#^sec-performance-engineering-program-goodput\|Recovering Program Goodput]]**) |
| **Communication (${C_2}$)** | Network bandwidth (${\text{BW}_{\text{network}}}$)                    | High AllReduce time, low scaling efficiency, communication \> 30% of step       | Scaling efficiency (${\eta_{\text{scaling}}}$), communication fraction (${T_{\text{comm}}}({N})/{T_{\text{step}}}({N})$) | Gradient compression, overlap compute/communication, topology optimization (**[[01 Books/Volume II - Scaling/02 Distributed ML/05 Collective Communication/V2-05 Collective Communication#^sec-collective-communication\|Collective Communication]]**)                                                                                                                           |
| **Coordination (${C_3}$)**  | Synchronization overhead and failure recovery                         | Low runtime goodput, frequent restarts, large pipeline bubbles, scheduler churn | Runtime goodput (${\eta_{\text{runtime}}} \approx {T_{\text{useful}}}/{T_{\text{wall}}}$)                                | Async checkpointing, elastic training, faster failure detection (**[[01 Books/Volume II - Scaling/02 Distributed ML/07 Fault Tolerance/V2-07 Fault Tolerance#^sec-fault-tolerance-reliability\|Fault Tolerance]]**)                                                                                                                                                              |

Table 2: **C$^3$ Diagnostic Summary**: Each axis maps to a distinct physical constraint and a high-impact optimization strategy. Start diagnosis here: identify which constraint binds, then follow the optimization pointer to the relevant chapter.

^tbl-c3-diagnostic-summary

## The Fleet Law

^sec-appdx-c3-taxonomy-fleet-law

Under ideal partitioning of fixed work, the same classification can be written as a time budget for each distributed step. The Fleet Law, introduced in **[[01 Books/Volume II - Scaling/00 Introduction/01 Introduction/V2-01.06 The C³ Taxonomy and Foundations of Scale#^sec-vol2-introduction-fleet-law|The Fleet Law]]**, decomposes every distributed training step into the distributed-step time budget:

$$
{T_{\text{step}}}({N}) = \frac{{T_{\text{compute}}}}{{N}} + {T_{\text{comm}}}({N}) + {T_{\text{sync}}}({N}) - {T_{\text{overlap}}}
$$

This equation is the fleet-scale counterpart of the iron law. Where the iron law decomposes single-machine execution into data movement, compute, and overhead, the Fleet Law decomposes distributed execution into local arithmetic, network data transfer, and synchronization logic. The diagnostic strategy is identical: measure each term, identify which dominates, and direct engineering effort at the dominant term.

### Component Decomposition

^sec-appdx-c3-taxonomy-component-decomposition

Each Fleet Law term maps to specific measurable activities that can be isolated in a timeline trace or cluster telemetry log. By attributing every millisecond of step duration to one of four terms, engineers can tell whether hardware is doing useful math, moving bytes across wires, or waiting on barriers:

- **${T_{\text{compute}}}/{N}$**: Forward pass, backward pass, and optimizer step, all local arithmetic after distribution across ${N}$ devices. Governed by MFU and per-GPU kernel efficiency. Improvements come from better kernels, mixed precision, and operator fusion.
- **${T_{\text{comm}}}({N})$**: AllReduce of gradients, AllGather of parameters (in FSDP/ZeRO), activation transfers in tensor/pipeline parallelism. Governed by network bandwidth and collective algorithm choice. Improvements come from gradient compression, hierarchical collectives, and compute-communication overlap.
- **${T_{\text{sync}}}({N})$**: Synchronization barriers, checkpoint writes, failure detection and recovery, pipeline bubble idle time, scheduler preemptions, and maintenance windows. Governed by cluster reliability and orchestration software. Improvements come from asynchronous checkpointing, elastic training, and faster failure detection.
- **${T_{\text{overlap}}}$**: Communication or coordination time hidden behind useful arithmetic. Governed by scheduling and implementation overlap.

Operational events may be amortized into the step budget or accounted for separately in runtime goodput. The same checkpoint or recovery delay must not appear in both. The compute-time fraction follows:

$$
{f_{\text{compute}}} = \frac{{T_{\text{compute}}}/{N}}{{T_{\text{step}}}({N})}
$$

When ${f_{\text{compute}}}$ drops below 0.5, the fleet spends more time on communication and coordination than on useful arithmetic. This compute-time fraction is not total fleet efficiency; useful fleet efficiency also depends on MFU, scaling efficiency, and goodput. The C$^3$ taxonomy identifies which noncompute term is responsible.

## C³ Intersections

^sec-appdx-c3-taxonomy-intersection-landscape

In a production cluster, a stalled training step rarely comes from a single isolated resource; a slow collective can idle tensor cores while a synchronous checkpoint write blocks both the GPUs and the network fabric. The Venn diagram in [[05 Reference/Volume II - Scaling/V2 The C³ Taxonomy#^fig-appdx-c3-taxonomy|figure 1]] maps how distributed execution spans the node substrate (${C_1}$), the networking backbone (${C_2}$), and the orchestration layer (${C_3}$). Because real bottlenecks arise at the pairwise and central boundaries where two or more of these dimensions compound, diagnosing them requires mapping observed symptoms back to the governing intersection and the engineering techniques that address it ([[05 Reference/Volume II - Scaling/V2 The C³ Taxonomy#^tbl-c3-intersections|table 3]]).

![[90 Assets/Volume II/01 Introduction/C3 Taxonomy ff4f6b4e02.svg]]

Figure 1: **The C$^3$ Intersection Landscape**: Each circle is one operational dimension (Compute, ${C_1}$, the node substrate; Communication, ${C_2}$, the network backbone; Coordination, ${C_3}$, the orchestration layer), labeled with the Fleet Law term it contributes to step time. Each pairwise overlap names the interaction between two dimensions (hiding network latency behind computation, preserving training progress against failure, and synchronizing collectives). At the center, where all three meet, is fleet ML systems engineering.

^fig-appdx-c3-taxonomy

| **Zone**                                                                           | **Name**                            | **Key techniques**                                                                                              | **Book coverage**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
|:-----------------------------------------------------------------------------------|:------------------------------------|:----------------------------------------------------------------------------------------------------------------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Compute (${C_1}$)**                                                              | The Node Substrate                  | Operator fusion, mixed precision (FP8/BF16), MFU optimization, local NVMe staging                               | **[[01 Books/Volume II - Scaling/01 The Fleet/02 Compute Infrastructure/V2-02 Compute Infrastructure#^sec-compute-infrastructure\|Compute Infrastructure]]**, **[[01 Books/Volume II - Scaling/01 The Fleet/04 Data Storage/V2-04 Data Storage#^sec-data-storage\|Data Storage]]**, **[[01 Books/Volume II - Scaling/03 The Fleet in Production/09 Fleet Efficiency/V2-09 Fleet Efficiency#^sec-performance-engineering\|Fleet Efficiency]]**, **[[05 Reference/Volume II - Scaling/V2 Single-Machine Foundations#^sec-appdx-dam-taxonomy-kernel-levers\|Kernel-Level Levers]]** |
| **Communication (${C_2}$)**                                                        | The Networking Backbone             | Rail-optimized Clos topologies, RoCEv2/InfiniBand fabrics, collective algorithms                                | **[[01 Books/Volume II - Scaling/01 The Fleet/03 Network Fabrics/V2-03 Network Fabrics#^sec-network-fabrics\|Network Fabrics]]**, **[[01 Books/Volume II - Scaling/02 Distributed ML/05 Collective Communication/V2-05 Collective Communication#^sec-collective-communication\|Collective Communication]]**                                                                                                                                                                                                                                               |
| **Coordination (${C_3}$)**                                                         | The Orchestration Layer             | Gang scheduling (Slurm, Kubernetes, Ray), state consensus, heartbeat failure detection                          | **[[01 Books/Volume II - Scaling/02 Distributed ML/07 Fault Tolerance/V2-07 Fault Tolerance#^sec-fault-tolerance-reliability\|Fault Tolerance]]**, **[[01 Books/Volume II - Scaling/02 Distributed ML/08 Fleet Orchestration/V2-08 Fleet Orchestration#^sec-fleet-orchestration\|Fleet Orchestration]]**, **[[01 Books/Volume II - Scaling/03 The Fleet in Production/12 ML Operations at Scale/V2-12 ML Operations at Scale#^sec-ops-scale\|ML Operations at Scale]]**                                                                                                                                                 |
| **Compute $\cap$ Communication (${C_1}\cap {C_2}$)**                               | Hiding Network Latency              | 1F1B pipelining, CUDA stream compute-comm overlap, comm-to-compute ratio (${\rho}$) tuning, wire compression    | **[[01 Books/Volume II - Scaling/02 Distributed ML/05 Collective Communication/V2-05 Collective Communication#^sec-collective-communication\|Collective Communication]]**, **[[01 Books/Volume II - Scaling/02 Distributed ML/06 Distributed Training/V2-06 Distributed Training#^sec-distributed-training-systems\|Distributed Training]]**                                                                                                                                                                                                                   |
| **Compute $\cap$ Coordination (${C_1}\cap {C_3}$)**                                | Preserving Progress Against Failure | Non-blocking async checkpointing, pipeline bubble reduction, in-memory recompute vs. rollback, fast node drain  | **[[01 Books/Volume II - Scaling/02 Distributed ML/07 Fault Tolerance/V2-07 Fault Tolerance#^sec-fault-tolerance-reliability\|Fault Tolerance]]**, **[[01 Books/Volume II - Scaling/02 Distributed ML/08 Fleet Orchestration/V2-08 Fleet Orchestration#^sec-fleet-orchestration\|Fleet Orchestration]]**                                                                                                                                                                                                                                                       |
| **Communication $\cap$ Coordination (${C_2}\cap {C_3}$)**                          | Collective Synchronization          | Straggler mitigation, hierarchical collectives (NVLink vs. IB), bounded staleness, topology-aware rank mapping  | **[[01 Books/Volume II - Scaling/02 Distributed ML/05 Collective Communication/V2-05 Collective Communication#^sec-collective-communication\|Collective Communication]]**, **[[01 Books/Volume II - Scaling/02 Distributed ML/07 Fault Tolerance/V2-07 Fault Tolerance#^sec-fault-tolerance-reliability\|Fault Tolerance]]**                                                                                                                                                                                                                                   |
| **Compute $\cap$ Communication $\cap$ Coordination (${C_1}\cap {C_2}\cap {C_3}$)** | Fleet ML Systems Engineering        | Fleet Law decomposition, 4D parallelism (DP+TP+PP+EP), memory sharding (FSDP2, ZeRO-3), ML productivity goodput | **[[01 Books/Volume II - Scaling/02 Distributed ML/06 Distributed Training/V2-06 Distributed Training#^sec-distributed-training-systems\|Distributed Training]]**, **[[01 Books/Volume II - Scaling/03 The Fleet in Production/10 Serving at Scale/V2-10 Serving at Scale#^sec-inference-scale\|Serving at Scale]]**, **[[01 Books/Volume II - Scaling/03 The Fleet in Production/11 Edge Intelligence/V2-11 Edge Intelligence#^sec-edge-intelligence\|Edge Intelligence]]**                                                                                                                                         |

Table 3: **C$^3$ Intersection Reference**: Each zone maps specific techniques to the axes they span and the chapters that cover them. The pairwise intersections require reasoning about two domains simultaneously; the center requires all three.

^tbl-c3-intersections

### Compute $\cap$ Communication

^sec-appdx-c3-taxonomy-comp-comm

When a GPU finishes its backward pass in 40 ms but waits 60 ms for an AllReduce collective to return gradients over the network, its tensor cores sit idle even though both the compute kernels and the links are working as specified. This intersection governs whether the system can hide communication behind computation. The communication-to-compute ratio (${\rho}= {T_{\text{comm}}}({N})/({T_{\text{compute}}}/{N})$) is the key diagnostic metric (**[[05 Reference/Volume II - Scaling/V2 Fleet Foundations#^sec-appdx-fleet-foundations-comm-compute-ratio|The communication-computation ratio]]**). When ${\rho}< 1$, computation takes longer than communication and there is enough arithmetic duration to hide the transfer in principle; dependencies and resource contention determine whether that overlap is achievable. When ${\rho}> 1$, GPUs complete their local work before the network delivers the next round of operands, and the system becomes communication-bound.

In a GPU trace, this bottleneck appears as exposed communication intervals where tensor cores sit idle awaiting collective completion (such as `ncclKernel_AllReduce` or `ncclKernel_AllGather`). Engineering at this intersection focuses on overlap and compression. Engineers launch AllReduce during the backward pass before all gradients are finalized, pipeline activation transfers in 1F1B schedules, and increase microbatch sizes or gradient accumulation steps to dilute communication frequency. They also apply wire quantization to reduce payload bytes, while accounting for metadata, codec time, and numerical error (**[[01 Books/Volume II - Scaling/02 Distributed ML/05 Collective Communication/V2-05 Collective Communication#^sec-collective-communication|Collective Communication]]**, **[[01 Books/Volume II - Scaling/02 Distributed ML/06 Distributed Training/V2-06 Distributed Training#^sec-distributed-training-systems|Distributed Training]]**).

### Compute $\cap$ Coordination

^sec-appdx-c3-taxonomy-comp-coord

A 1,024-GPU cluster that pauses every thirty minutes to flush a multi-terabyte checkpoint to shared storage turns expensive arithmetic capacity into idle wait time. This intersection captures the idle compute caused by orchestration and resilience mechanisms. While compute engines should remain saturated with arithmetic, coordination overhead repeatedly forces hardware into idle states. Three distinct mechanisms govern this intersection:

1.  **Pipeline bubbles**: In pipeline parallelism (PP), stages idle during pipeline fill (warmup) and drain (cooldown). For ${N_{\text{PP}}}$ pipeline stages and ${m}$ microbatches, the bubble fraction ${b_{\text{pipe}}} = ({N_{\text{PP}}} - 1)/({N_{\text{PP}}} - 1 + {m})$ (**[[05 Reference/Volume II - Scaling/V2 Communication Foundations#^sec-appdx-comm-foundations-bubble-fraction|Bubble fraction]]**) is accelerator time lost to idling; more microbatches or interleaved schedules shrink it.
2.  **Checkpoint stalls**: Synchronous checkpoint writes that block the training loop to serialize terabytes of weights and optimizer states convert expensive compute time into storage wait time. Asynchronous checkpointing mitigates this by snapshotting host-pinned or local Non-Volatile Memory Express (NVMe) memory in milliseconds, delegating remote persistence to background I/O threads.
3.  **Recovery rollback**: When a node fails in an ${N}$-device cluster, training halts and rolls back to the last valid checkpoint, squandering the arithmetic executed since that snapshot. Minimizing the failure blast radius through fast health heartbeats and dynamic node replacement bounds this compute loss (**[[01 Books/Volume II - Scaling/02 Distributed ML/07 Fault Tolerance/V2-07 Fault Tolerance#^sec-fault-tolerance-reliability|Fault Tolerance]]**, **[[01 Books/Volume II - Scaling/02 Distributed ML/08 Fleet Orchestration/V2-08 Fleet Orchestration#^sec-fleet-orchestration|Fleet Orchestration]]**).

### Communication $\cap$ Coordination

^sec-appdx-c3-taxonomy-comm-coord

When a single GPU or network link drops packets or throttles its clock during an AllReduce collective, every other rank in the group must wait at the dependency boundary before the next step can proceed. This intersection captures the synchronization cost embedded in network communication. A collective operation (AllReduce, AllGather, ReduceScatter) moves data over physical wires (${C_2}$) while creating dependencies among its participating ranks (${C_3}$). It need not impose a separate cluster-wide barrier, but a delayed contribution can prevent dependent outputs from becoming ready.

The governing failure mode is that one slow participant paces the whole collective. If a single GPU or link experiences packet drops, thermal throttling, or ECC retry delays, every other GPU in the collective waits, transforming a localized degradation into a cluster-wide halt. At fleet scale (${N}\ge 10{,}000$), tail latency dominates the barrier time, because the probability that at least one node straggles approaches unity ($1 - (1 - {p_{\text{straggle}}})^{N}\to 1$). Engineering at this intersection focuses on decoupling synchronization from raw communication. Hierarchical collectives isolate high-bandwidth intra-node NVLink domains from inter-node InfiniBand fabrics. Bounded-staleness asynchronous training absorbs transient tail latency. Topology-aware gang scheduling aligns collective communication rings with physical spine-leaf switch rails (**[[01 Books/Volume II - Scaling/02 Distributed ML/05 Collective Communication/V2-05 Collective Communication#^sec-collective-communication|Collective Communication]]**, **[[01 Books/Volume II - Scaling/02 Distributed ML/07 Fault Tolerance/V2-07 Fault Tolerance#^sec-fault-tolerance-reliability|Fault Tolerance]]**).

### Fleet-Scale ML Systems Engineering

^sec-appdx-c3-taxonomy-triple-intersection

Partitioning a 405-billion-parameter model across 16,384 GPUs requires fitting shard states into high-bandwidth memory (HBM) (${C_1}$), matching tensor and pipeline traffic to intra-node NVLink and inter-node InfiniBand bandwidths (${C_2}$), and keeping pipeline bubbles and checkpoint stalls from consuming wall-clock time (${C_3}$). At the center (${C_1}\cap {C_2}\cap {C_3}$), all three constraints converge simultaneously. This is the discipline of **fleet-scale ML systems engineering**. Systems engineers at this center do not optimize a single accelerator or a single network switch; they manage the trade-offs of the distributed machine as an integrated whole. The central engineering challenges encompass three coupled design problems:

- **4D parallelism co-design**: Balancing data parallelism (DP), tensor parallelism (TP), pipeline parallelism (PP), and expert parallelism (EP) so that memory consumption fits within accelerator HBM (${C_1}$), high-frequency communications map to intra-node NVLink and low-frequency communications map to inter-node fabrics (${C_2}$), and pipeline bubbles and barrier dependencies are minimized (${C_3}$).
- **Memory sharding vs. communication volume**: Frameworks like PyTorch FSDP2 and DeepSpeed ZeRO-3 eliminate memory redundancy (${C_1}$) by partitioning model states across workers, but pay for it with repeated AllGather communication (${C_2}$) and state coordination metadata (${C_3}$).
- **ML productivity goodput**: ML productivity goodput (MPG), the fraction of a fleet’s capacity-time that becomes useful work, is the product of scheduling goodput (${\eta_{\text{scheduling}}}$), runtime goodput (${\eta_{\text{runtime}}}$), and program goodput (${\eta_{\text{program}}}$) (**[[01 Books/Volume II - Scaling/03 The Fleet in Production/09 Fleet Efficiency/V2-09.03 ML Goodput#^sec-performance-engineering-goodput-family|One word, several measures]]**). These factors cut across the C$^3$ axes rather than mapping one to one onto them. Communication overlap and shorter pipeline bubbles improve program goodput, while checkpointing and recovery, which are Coordination costs, determine runtime goodput.

### C³ Coordination and Overlap

^sec-appdx-c3-taxonomy-coordination-overlap

Just as single-node execution transforms the additive iron law into a maximum bounded by dependencies (**[[05 Reference/Volume II - Scaling/V2 Single-Machine Foundations#^sec-appdx-dam-taxonomy-dam-coordination-sum-max|D·A·M coordination from sum to max]]**), overlap at fleet scale transforms the Fleet Law (**[[01 Books/Volume II - Scaling/00 Introduction/01 Introduction/V2-01.06 The C³ Taxonomy and Foundations of Scale#^eq-fleet-law|equation 1.3]]**) by maximizing ${T_{\text{overlap}}}$. Pipeline schedules, separate communication streams, asynchronous checkpoints, hierarchical collectives, and double-buffered data streaming each hide one C$^3$ axis behind another ([[05 Reference/Volume II - Scaling/V2 The C³ Taxonomy#^tbl-c3-overlap|table 4]]).

| **Technique**                      | **C$^3$ overlap**        | **Mechanism**                                                                                            | **Implementation**                                                                                                                                                                                                                                                           |
|:-----------------------------------|:-------------------------|:---------------------------------------------------------------------------------------------------------|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **1F1B Pipeline Schedule**         | ${C_1}$ overlaps ${C_2}$ | Interleaves forward and backward microbatches to overlap cross-stage activation transfer with arithmetic | Microbatch queue scheduling (**[[01 Books/Volume II - Scaling/02 Distributed ML/06 Distributed Training/V2-06 Distributed Training#^sec-distributed-training-systems\|Distributed Training]]**)                                                                                                    |
| **CUDA Stream Decoupling**         | ${C_1}$ overlaps ${C_2}$ | Launches non-blocking AllGather or AllReduce on separate communication streams concurrently with GEMMs   | Dedicated NCCL streams (**[[01 Books/Volume II - Scaling/02 Distributed ML/05 Collective Communication/V2-05 Collective Communication#^sec-collective-communication\|Collective Communication]]**)                                                                                                 |
| **Async Checkpointing**            | ${C_1}$ overlaps ${C_3}$ | Fast in-memory or local NVMe snapshot while GPU arithmetic resumes immediately                           | Background host thread flushes to storage (**[[01 Books/Volume II - Scaling/01 The Fleet/04 Data Storage/V2-04 Data Storage#^sec-data-storage\|Data Storage]]**, **[[01 Books/Volume II - Scaling/02 Distributed ML/07 Fault Tolerance/V2-07 Fault Tolerance#^sec-fault-tolerance-reliability\|Fault Tolerance]]**) |
| **Hierarchical Collectives**       | ${C_2}$ overlaps ${C_3}$ | Partitions collective into local NVLink reduction and inter-node fabric transfer, isolating tail jitter  | Hierarchical NCCL communicators (**[[01 Books/Volume II - Scaling/02 Distributed ML/05 Collective Communication/V2-05 Collective Communication#^sec-collective-communication\|Collective Communication]]**)                                                                                        |
| **Double-Buffered Data Streaming** | ${C_1}$ overlaps ${C_2}$ | Prefetches and decompresses next batch shard in pinned host memory while GPUs compute current batch      | Host pinned memory + async H2D transfer (**[[01 Books/Volume II - Scaling/01 The Fleet/04 Data Storage/V2-04 Data Storage#^sec-data-storage\|Data Storage]]**)                                                                                                                                |

Table 4: **C$^3$ Overlap Techniques**: System techniques that hide communication or coordination behind useful computation, maximizing ${T_{\text{overlap}}}$ in the Fleet Law.

^tbl-c3-overlap

### Storage as the Persistent Substrate

^sec-appdx-c3-taxonomy-storage-substrate

A common diagnostic question is why Storage does not appear as a fourth explicit coordinate in the C$^3$ taxonomy or as an independent ${T_{\text{storage}}}$ term in the Fleet Law. The physical data center is procured around Compute, Network, and Storage (**[[01 Books/Volume II - Scaling/01 The Fleet/04 Data Storage/V2-04 Data Storage#^sec-data-storage|Data Storage]]**), yet at runtime storage devices execute no model arithmetic. Storage overhead therefore manifests dynamically through the three C$^3$ dimensions:

- **In Compute (${C_1}$)**: High-throughput local NVMe drives function as the tier-3 extension of the accelerator memory hierarchy (below SRAM and HBM), serving parameter offloading (ZeRO-Offload) and activation spilling.
- **In Communication (${C_2}$)**: Remote dataset streaming from parallel file systems (Lustre, GPFS) or object stores (S3, Ceph) shares cluster network bandwidth and network interface card (NIC) capacity with collective communication traffic.
- **In Coordination (${C_3}$)**: Durable distributed storage provides the persistent state anchor required for checkpoint serialization, node failover, and job rescheduling.

When storage latency stalls a training run, profilers identify the symptom not as raw disk latency, but either as a network communication bottleneck (${C_2}$, dataset starvation) or as a blocking coordination barrier (${C_3}$, synchronous checkpoint flush). Storage is the persistent substrate supporting all three dimensions, rather than a separate term in the step execution budget.

## Rules of Thumb

^sec-appdx-c3-taxonomy-rules-of-thumb

In the middle of a production incident, fast heuristics narrow the search space before a profiler is needed. These thresholds provide that first line of defense.

### The C³ Traffic Light

^sec-appdx-c3-taxonomy-traffic-light

Each C$^3$ axis has one headline metric, and its value against two thresholds sorts the axis into green, yellow, or red ([[05 Reference/Volume II - Scaling/V2 The C³ Taxonomy#^tbl-c3-traffic-light|table 5]]). Comparing observed MFU, communication fraction, and runtime goodput against these bands immediately isolates which subsystem warrants a deeper trace.

| **C$^3$ axis**    | **Green (healthy)**     | **Yellow (investigate)** | **Red (bottleneck)**    |
|:------------------|:------------------------|:-------------------------|:------------------------|
| **Compute**       | MFU $>$ 50%             | MFU 30%–50%              | MFU $<$ 30%             |
| **Communication** | Comm fraction $<$ 20%   | Comm fraction 20–40%     | Comm fraction $>$ 40%   |
| **Coordination**  | Runtime goodput $>$ 90% | Runtime goodput 75–90%   | Runtime goodput $<$ 75% |

Table 5: **C$^3$ Traffic Light**: Quick triage thresholds for fleet-scale diagnosis. Green means the axis is healthy; yellow means it deserves investigation; red means it is the likely bottleneck. These thresholds assume well-optimized large-model training on current-generation hardware.

^tbl-c3-traffic-light

### The Bottleneck Diagnostic Table

^sec-appdx-c3-taxonomy-bottleneck-table

An optimization pays only when it shortens the term that binds: upgrading to faster GPUs in a communication-bound fleet or adding network bandwidth to a compute-bound fleet leaves step time flat ([[05 Reference/Volume II - Scaling/V2 The C³ Taxonomy#^tbl-c3-bottleneck-actions|table 6]]).

| **If the fleet is…**    |     **Dominant term**      | **Optimization that works**                                                              | **Optimization that is wasted**                                                        |
|:------------------------|:--------------------------:|:-----------------------------------------------------------------------------------------|:---------------------------------------------------------------------------------------|
| **Compute-bound**       | ${T_{\text{compute}}}/{N}$ | Better kernels, mixed precision, operator fusion, next-gen accelerators                  | More network bandwidth (GPUs are not waiting on the network)                           |
| **Communication-bound** |  ${T_{\text{comm}}}({N})$  | Gradient compression, compute-comm overlap, hierarchical collectives, InfiniBand upgrade | Faster GPUs (they spend a larger share of each step waiting for the network)           |
| **Coordination-bound**  |  ${T_{\text{sync}}}({N})$  | Async checkpointing, elastic training, faster failure detection, fewer pipeline stages   | Faster arithmetic alone; faster networks help only transfer-related coordination costs |

Table 6: **What Works vs. What Is Wasted at Fleet Scale**: Optimizing a nondominant C$^3$ axis yields limited improvement and often worsens cost efficiency. A communication-bound fleet will gain little from faster GPUs until AllReduce and other communication bottlenecks are addressed.

^tbl-c3-bottleneck-actions

## C³ Case Studies

^sec-appdx-c3-taxonomy-case-studies

In production, two clusters with the same slow step time can require opposite fixes depending on whether the stall comes from low per-GPU kernel utilization, exposed gradient synchronization, or frequent recovery restarts. The three cases below isolate one dominant C$^3$ axis at a time and trace the diagnosis from initial symptom to targeted fix.

### Case 1 on the Underutilized Compute Fleet

^sec-appdx-c3-taxonomy-case-1

#### Symptom

^symptom

An engineering team provisions 4,096 H100 GPUs for a large language model training run. The training loop runs without errors, but the PyTorch Profiler shows MFU of only 15 percent. The network profiler shows communication accounts for less than 10 percent of step time. The cluster is running but barely working.

#### Diagnosis

^diagnosis

The **Compute** axis is the leading hypothesis to investigate. With 15 percent MFU, 85 percent of the fleet’s peak capacity is not credited to useful model FLOPs. Low exposed communication makes local execution a useful starting point; kernel traces and host-side waits must distinguish inefficient arithmetic from data starvation or unobserved coordination gaps.

#### The Fix

^the-fix

If traces confirm inefficient local execution, target the compute axis across 4,096 accelerators to raise per-device kernel utilization. Three adjustments recover most of the missing arithmetic throughput:

- **Mixed precision**: Ensure BF16/FP8 Tensor Cores are engaged. A common culprit is FP32 fallback in normalization layers or loss computation.
- **Operator fusion**: Use `torch.compile` or similar just-in-time (JIT) compilation to fuse element-wise operations and reduce kernel launch overhead.
- **Batch size tuning**: If per-GPU batch size is too small, the matrix multiplications have insufficient arithmetic intensity to saturate the Tensor Cores.

Raising MFU from 15 percent to 50 percent on the same hardware delivers 50 percent/15 percent = 3.3× more useful work, the equivalent of tripling the fleet without buying a single GPU. Because communication is already below 10 percent of step time, all of that per-device gain translates directly into faster step completion.

### Case 2 on the Communication Wall

^sec-appdx-c3-taxonomy-case-2

#### Symptom

^symptom-1

A 512-GPU data-parallel training run achieves 45 percent illustrative compute-phase efficiency during compute kernels on each GPU, which is good per-device kernel efficiency. Wall-clock MFU over the full step (including AllReduce) is only 20.2 percent because AllReduce consumes 55 percent of every training step. Scaling from 64 GPUs to 512 GPUs yields only 4× speedup instead of the expected 8×, or 50 percent scaling efficiency.

#### Diagnosis

^diagnosis-1

The **Communication** axis dominates. Each GPU has healthy compute-phase efficiency, but more than half the step time is spent synchronizing gradients across the network. The system is **Communication-Bound**: adding more GPUs can worsen the exposed communication fraction. Under fixed-work scaling, local computation shrinks while the collective retains startup and transfer costs.

#### The Fix

^the-fix-1

Target the communication axis without touching the per-GPU computation. Three network-level interventions shrink or hide the exposed collective time:

- **Compute-communication overlap**: Launch AllReduce during the backward pass rather than waiting until it completes. Modern frameworks (FSDP, DeepSpeed) support this natively.
- **Gradient compression**: Apply Top-k sparsification or quantization to reduce the bytes crossing the network by 10–100$\times$.
- **Hierarchical collectives**: Use intra-node NVLink for the first reduction stage, then inter-node InfiniBand only for cross-node aggregation, reducing inter-node participants relative to a flat rank-level algorithm. Actual traffic savings depend on the collective layout, NIC allocation, and topology.

If communication were eliminated entirely, throughput would increase by 2.2× (Amdahl’s Law applied to the 45 percent compute fraction). Realistically, reducing communication from 55 percent to 20 percent of step time would recover most of the lost scaling.

### Case 3 on Coordination Overhead

^sec-appdx-c3-taxonomy-case-3

#### Symptom

^symptom-2

A 10,000-GPU training run shows 40 percent compute-phase model FLOPs utilization per device, measured only while kernels execute, and communication accounts for only 15 percent of step time. Both figures look healthy. Yet only 60 percent of wall time is left after the run’s coordination overheads. That share is not a goodput factor, because it mixes losses that belong to different factors. Pipeline bubbles lie inside retained steps and are a program goodput loss, while checkpoints, recovery, maintenance, and preemption fall outside the steps (**[[01 Books/Volume II - Scaling/03 The Fleet in Production/09 Fleet Efficiency/V2-09.03 ML Goodput#^sec-performance-engineering-goodput-boundaries|Accounting boundaries]]**). The remaining 40 percent of wall time is consumed by checkpoint writes, failure recovery restarts, pipeline bubble idle time, scheduler preemptions (17 percent of wall time), and maintenance windows.

#### Diagnosis

^diagnosis-2

The **Coordination** axis dominates. Although per-GPU computation and inter-node communication are both efficient, nonproductive overhead consumes 40 percent of wall time. Scheduler preemptions take 17 percent, and failure recovery takes 10 percent (because at 10,000 GPUs, GPU failures occur about every 5 hours). Pipeline bubbles take 5 percent, checkpoint writes take 3 percent, and maintenance windows take 5 percent. Because faster arithmetic alone cannot recover this lost time, checkpoint bandwidth, recovery mechanisms, and scheduling must be evaluated against the specific overhead each can reduce.

#### The Fix

^the-fix-2

Target the coordination axis so that orchestration and fault-recovery events stop idling the healthy accelerators. Four operational changes attack both the in-step bubble losses and the out-of-step downtime:

- **Asynchronous checkpointing**: Overlap checkpoint writes with the next training step, reducing visible checkpoint overhead from 3 percent to near zero.
- **Elastic training**: When a node fails, shrink the job and continue rather than halting all 10,000 GPUs for recovery. This converts the 10 percent failure recovery cost into a smaller throughput reduction.
- **Pipeline schedule optimization**: Switch from GPipe to an interleaved 1F1B schedule to reduce bubble fraction, or increase microbatch count per pipeline flush.
- **Faster failure detection**: Reduce heartbeat timeout from 30 seconds to 5 seconds with hardware-level health monitoring, cutting the idle time between failure occurrence and recovery initiation.

## Production Troubleshooting

^sec-appdx-c3-taxonomy-production-troubleshooting

Each common fleet-scale failure mode first shows up as a user-visible symptom, and that symptom points to the C$^3$ axis most likely responsible (sometimes two), a measurement that confirms it, and an action ([[05 Reference/Volume II - Scaling/V2 The C³ Taxonomy#^tbl-c3-troubleshooting|table 7]]). Operators can match an observed cluster symptom to its primary C$^3$ axis, run the listed diagnostic check, and apply the corresponding engineering fix.

| **Symptom**                                    |    **C$^3$ axis**     | **Diagnostic question**                                                      | **Measurement**                                                 | **Action**                                                             |
|:-----------------------------------------------|:---------------------:|:-----------------------------------------------------------------------------|:----------------------------------------------------------------|:-----------------------------------------------------------------------|
| **Low MFU despite fast network**               |      **Compute**      | Are Tensor Cores engaged? Is batch size sufficient for arithmetic intensity? | Per-GPU kernel trace (Nsight/PyTorch Profiler)                  | Enable mixed precision, increase per-GPU batch size                    |
| **Throughput plateaus when adding GPUs**       |   **Communication**   | Does AllReduce time grow faster than computation shrinks?                    | NCCL trace, ${\rho}$ ratio                                      | Gradient compression, hierarchical collectives, overlap                |
| **Frequent job restarts**                      |   **Coordination**    | What is the cluster MTBF? Is detection fast enough?                          | Failure logs, MTBF calculation                                  | Elastic training, faster detection, smaller blast radius               |
| **High GPU-hours but slow progress**           |   **Coordination**    | What fraction of GPU-hours produce useful training steps?                    | Runtime goodput (${T_{\text{useful}}}/{T_{\text{wall}}}$)       | Async checkpointing, reduce pipeline stages, eliminate scheduler churn |
| **Scaling efficiency drops with cluster size** |    **Comm/Coord**     | Is the bottleneck network bandwidth or synchronization barriers?             | Separate ${T_{\text{comm}}}({N})$ from ${T_{\text{sync}}}({N})$ | If comm: compress or overlap. If coord: async methods                  |
| **Stragglers slow entire job**                 | **Comm $\cap$ Coord** | Is one node consistently last to reach the AllReduce barrier?                | Per-node step time histogram                                    | Straggler detection + replacement, bounded staleness, backup workers   |

Table 7: **C$^3$ Troubleshooting Matrix**: Root cause identification and remediation for common fleet-scale bottlenecks. Each row connects a user-visible symptom to the C$^3$ axis most likely responsible, reducing the search space before reaching for a profiler.

^tbl-c3-troubleshooting

## Tooling Map

^sec-appdx-c3-taxonomy-tooling-map

Confirming a candidate C$^3$ bottleneck requires inspecting the layer where that constraint lives: per-GPU kernel profilers for Compute, collective and fabric counters for Communication, and scheduler and goodput logs for Coordination ([[05 Reference/Volume II - Scaling/V2 The C³ Taxonomy#^tbl-c3-tooling|table 8]]).

| **C$^3$ axis**    |         **Key metric**         | **Primary tool**                               | **Secondary tool**                                         |
|:------------------|:------------------------------:|:-----------------------------------------------|:-----------------------------------------------------------|
| **Compute**       |    MFU, kernel utilization     | PyTorch Profiler (TensorBoard plugin)          | Nsight Compute (per-kernel roofline analysis)              |
| **Communication** | AllReduce time, ${\rho}$ ratio | NCCL debug logs (`NCCL_DEBUG=INFO`)            | Nsight Systems (timeline), `ibstat`/`perfquery` (IB)       |
| **Coordination**  | Runtime goodput, restart count | Cluster scheduler logs (Slurm, K8s event logs) | Custom goodput dashboards (for example, Google ML Goodput) |

Table 8: **C$^3$ Tooling Map**: Profiling utilities for diagnosing fleet-scale bottlenecks. Start with the primary tool for quick triage; use secondary tools for deep-dive analysis. Compute tools operate per-GPU; Communication tools operate at the network layer; Coordination tools operate at the cluster/job level.

^tbl-c3-tooling

## C³ Scorecard

^sec-appdx-c3-taxonomy-scorecard

Once profiling tools supply the raw counters, three fleet-level efficiency ratios extend the single-machine scorecard (**[[05 Reference/Volume II - Scaling/V2 Single-Machine Foundations#^sec-appdx-dam-taxonomy-dam-scorecard|D·A·M Scorecard]]**) to grade distributed cluster health against production thresholds ([[05 Reference/Volume II - Scaling/V2 The C³ Taxonomy#^tbl-c3-scorecard|table 9]]).

| **C$^3$ axis**    |                     **Metric**                     |                                                  **Definition**                                                  | **Failing grade** | **Passing grade** |
|:------------------|:--------------------------------------------------:|:----------------------------------------------------------------------------------------------------------------:|:-----------------:|:-----------------:|
| **Compute**       |                      **MFU**                       |                   $\frac{{O_{\text{useful}}}}{{N}{R_{\text{peak}}} \times {T_{\text{step}}}}$                    |      $<$ 30%      |      $>$ 50%      |
| **Communication** | **Scaling Efficiency** (${\eta_{\text{scaling}}}$) |                                         $\frac{{T_1}}{{N}\times {T_N}}$                                          |      $<$ 56%      |      $>$ 87%      |
| **Coordination**  |  **Runtime Goodput** (${\eta_{\text{runtime}}}$)   | $\frac{{T_{\text{useful}}}}{{T_{\text{wall}}}}$, retained steps at the job’s fault-free step rate over held time |      $<$ 75%      |      $>$ 90%      |

Table 9: **The C$^3$ Efficiency Rubric**: Use these three numbers to characterize fleet health. The MFU denominator uses aggregate fleet peak, written as ${N}{R_{\text{peak}}}$ when ${R_{\text{peak}}}$ is a per-device value. These illustrative thresholds guide investigation; passing all three does not prove that inexpensive optimizations are exhausted.

^tbl-c3-scorecard

## C³ Infrastructure Diagnostic Decision Tree and Fleet Diagnostic Scorecard

^sec-appdx-c3-diagnostic-tree

When step time suddenly doubles in the middle of a training run, on-call operators see raw hardware counters—elevated GPU temperatures, PCIe retry alerts, or InfiniBand pause frames—rather than a neatly labeled C$^3$ axis. Cluster operations teams need a systematic procedure for mapping those low-level hardware signals to the binding C$^3$ axis before taking remedial action.

### Telemetry Signal Mapping to C³ Axes

^sec-appdx-c3-telemetry-mapping

A degraded PCIe riser or a clogged cooling loop first surfaces in hardware counters across silicon, PCIe buses, thermal sensors, and network switches. Monitoring daemons collect four primary classes of low-level telemetry to catch these faults early:

- **MFU Drops**: Sudden or sustained drops in model FLOPs utilization below expected baselines.
- **PCIe AER (Advanced Error Reporting) Retries**: Non-fatal bus errors causing packet retries, link downgrades (e.g., PCIe Gen 5 $\to$ Gen 3), or host-to-device direct memory access (DMA) throttling.
- **Thermal Throttling**: GPU SM clock downclocking (e.g., 1.9 GHz $\to$ 1.1 GHz) triggered by junction thermal limits or cooling fan degradation.
- **InfiniBand Credit Stalls and PFC Pause Frames**: Priority flow control (PFC) pause frames, congestion notification packets (CNP), or switch buffer credit starvation.

### Diagnostic Decision Tree

^sec-appdx-c3-diagnostic-tree-details

Triage starts from whichever telemetry source shows the anomaly and narrows to the specific signal before naming the binding axis ([[05 Reference/Volume II - Scaling/V2 The C³ Taxonomy#^fig-c3-telemetry-decision-tree|figure 2]]). A node-side signal points to the compute axis, while a network-side signal separates fabric congestion, a communication cost, from a single straggler that holds every rank at the barrier, a coordination cost.

![[90 Assets/Volume II/Shared Figures/C3 Telemetry Decision Tree dd9f57982e.svg]]

Figure 2: **Telemetry-First Triage**: An anomaly is traced first to the telemetry source that shows it, then to the specific signal, and only then to the C$^3$ axis that binds. Thermal throttling and PCIe link degradation both lower per-device throughput and so point to compute, credit stalls point to communication, and a single rank that is always last points to coordination. The 85 °C threshold is illustrative.

^fig-c3-telemetry-decision-tree

### Structured Diagnostic Telemetry Table

^sec-appdx-c3-telemetry-table

Once the decision tree isolates the anomalous hardware or OS counter, pairing that counter with its physical subsystem lets automated health checks route the alert directly to the appropriate repair workflow ([[05 Reference/Volume II - Scaling/V2 The C³ Taxonomy#^tbl-c3-telemetry-diagnostic|table 10]]).

| **Telemetry signal**                   | **Hardware/OS counter**                                        | **Root cause**                                    | **C$^3$ axis**    | **Remediation action**                                                          |
|:---------------------------------------|:---------------------------------------------------------------|:--------------------------------------------------|:------------------|:--------------------------------------------------------------------------------|
| **MFU Drop with High GPU Temp**        | `gpu_temperature > 85°C`, `clocks_throttle_reasons.sw_thermal` | Thermal throttling reduces GPU SM clock speed     | **Compute**       | Check coolant flow, replace thermal interface material (TIM), adjust fan curves |
| **MFU Drop with Low Host-GPU BW**      | `pcie_aer_correctable_errors`, `pcie_link_width < x16`         | PCIe link degradation/retries due to signal noise | **Compute**       | Reseat GPU/PCIe riser card, clean PCIe edge connectors, replace cable           |
| **AllReduce Stalls with Pause Frames** | `PFC_PAUSE_XOFF_FRAMES`, `infiniband_credit_stalls`            | Network fabric congestion, IB buffer exhaustion   | **Communication** | Enable adaptive routing (AR), rebalance ECMP hashing, tune NCCL buffer size     |
| **NCCL Barrier Timeout/Hang**          | `NCCL_DEBUG=INFO` log `Unhandled CUDA error`, `heartbeat_miss` | Single-node straggler or silent kernel hang       | **Coordination**  | Drain degraded node, isolate via node health check script, trigger fast restart |
| **High Step Overhead with Idle GPU**   | `nvlink_throughput == 0`, `fs_write_latency > 1s`              | Blocking synchronous checkpoint write to storage  | **Coordination**  | Switch to asynchronous double-buffered checkpointing or host RAM staging        |

Table 10: **C$^3$ Telemetry Diagnostic Mapping**: Direct mapping from silicon-level telemetry signals to the binding C$^3$ axis and its remediation.

^tbl-c3-telemetry-diagnostic

### Fleet Diagnostic Scorecard

^sec-appdx-c3-dam-scorecard

The fleet diagnostic scorecard in [[05 Reference/Volume II - Scaling/V2 The C³ Taxonomy#^tbl-c3-dam-scorecard|table 11]] carries each single-node Data, Algorithm, and Machine (D·A·M) concern to the fleet telemetry that exposes it, the C$^3$ axes it affects, and a target benchmark. Each row links a single-node resource category to the cluster-level telemetry signal and target benchmark that govern distributed execution.

| **D·A·M axis**             | **Fleet telemetry signal**                                                   | **C$^3$ axis**                 | **Target efficiency benchmark**                                                         |
|:---------------------------|:-----------------------------------------------------------------------------|:-------------------------------|:----------------------------------------------------------------------------------------|
| **Data ($\text{D}$)**      | Network fabric RX/TX saturation, storage write I/O wait times                | **Communication/Coordination** | I/O wait time $< 2\%$ of step time; NCCL ring bandwidth $> 85\%$ of fabric peak         |
| **Algorithm ($\text{A}$)** | Pipeline bubble idle fraction, partitioning imbalance across stages          | **Compute/Coordination**       | Pipeline bubble fraction $< 20\%$ under the balanced-stage model                        |
| **Machine ($\text{M}$)**   | Model FLOPs utilization (MFU), PCIe AER errors, thermal and power throttling | **Compute**                    | MFU $>$ 50%; thermal throttle events $= 0$; PCIe link width held at maximum (Gen 5 x16) |

Table 11: **Fleet Diagnostic Scorecard**: Each single-node D·A·M concern maps to the fleet telemetry that exposes it and to the C$^3$ axes it affects.

^tbl-c3-dam-scorecard

## Scaling Laws Through the C³ Lens

^sec-appdx-c3-taxonomy-scaling-laws

Scaling laws are usually written in algorithmic FLOPs, but a training fleet delivers only the useful FLOPs that survive utilization, communication, and coordination losses. Translating a scaling-law target into C$^3$ terms means removing its hidden perfect-systems assumption and replacing peak FLOP/s with effective FLOP/s, the usable throughput that connects model-quality forecasts to real cluster capacity.

### The Ideal-System Assumption in Scaling Laws

^sec-appdx-c3-taxonomy-scaling-laws-assumption

Scaling laws ([[05 Reference/Volume II - Scaling/V2 The C³ Taxonomy#^ref-kaplan2020scaling|Kaplan et al. 2020]]; [[05 Reference/Volume II - Scaling/V2 The C³ Taxonomy#^ref-hoffmann2022chinchilla|Hoffmann et al. 2022]]) and their successors predict model quality as a function of algorithmic training compute. They usually abstract away systems efficiency: wall-clock time, accelerator peak FLOP/s, compute-phase efficiency, communication overhead, and scheduler losses appear later when teams provision hardware to deliver the target compute budget. In C$^3$ terms, scaling-law FLOPs must be converted into raw fleet capacity after compute-phase, distributed-step, and runtime-goodput losses.

The gap between scaling-law predictions and observed training outcomes is, in large part, a C$^3$ gap. A team that budgets $10^{24}$ peak hardware FLOPs of capacity will deliver fewer useful model FLOPs after three multiplicative losses: per-GPU compute-phase efficiency, inter-node scaling efficiency (${\eta_{\text{scaling}}}$), and runtime goodput.

### The Effective FLOP/S Concept

^sec-appdx-c3-taxonomy-effective-flops

A fleet’s **effective FLOP/s** is the usable throughput after compounding three disjoint C$^3$ efficiency factors across the cluster:

$$
{R_{\text{eff}}} = ({N}{R_{\text{peak}}}) \times \underbrace{{\text{MFU}}}_{\text{Compute}} \times \underbrace{{\eta_{\text{scaling}}}}_{\text{Distributed step}} \times \underbrace{{\eta_{\text{runtime}}}}_{\text{Runtime goodput}}
$$

MFU, the single-device baseline, measures useful model arithmetic against peak throughput only while local computation is active. This compute-phase factor is not the step-averaged fleet MFU of [[05 Reference/Volume II - Scaling/V2 The C³ Taxonomy#^tbl-c3-scorecard|table 9]], whose ${T_{\text{step}}}$ denominator already includes the in-step losses that ${\eta_{\text{scaling}}}$ counts, so the product does not count them twice. Scaling efficiency captures communication and other distributed-step losses, including pipeline bubbles. Runtime goodput captures time outside those measured steps, including checkpointing, failure recovery, scheduler preemptions, and maintenance. These disjoint measurement windows prevent the same loss from being counted twice, while a concrete estimate makes the multiplicative loss visible at fleet scale.

**Systems Perspective 1.1: Compound C³ loss on a 100,000-GPU cluster**

Consider a 100,000-GPU H100 cluster with 98,900 PFLOP/s of peak aggregate throughput. After the three disjoint C$^3$ efficiency factors:

$$
\text{Effective} = 98,900 PFLOP/s \times 0.50 \times 0.56 \times 0.65 \approx 17999.8 PFLOP/s
$$

The fleet delivers 18.2 percent of its peak capacity as useful training work. The **compound C$^3$ loss**, the ratio of peak to effective compute, is 5.5×, so achieving a given effective compute budget requires 5.5× the raw hardware. The compute phase retains a 50 percent efficiency factor, and the distributed step retains a 56 percent scaling factor (using the modeled 8,192-GPU tier as an illustrative proxy that includes pipeline losses). Runtime goodput retains a 65 percent factor after checkpoints, failures, scheduler preemptions, and maintenance.

These losses reflect the physics of fleet-scale computation rather than a failure of engineering. The C$^3$ taxonomy quantifies where the losses occur so that optimization effort targets the dominant term.

## Summary

^sec-appdx-c3-taxonomy-summary

The C$^3$ taxonomy provides a systematic framework for diagnosing fleet-scale bottlenecks. Each axis maps to a distinct physical constraint: arithmetic throughput and MFU bound compute; network bandwidth and collective algorithm efficiency bound communication; and synchronization overhead, failure recovery, and operational losses bound coordination. The Fleet Law quantifies these constraints, enabling systematic diagnosis. Use the C$^3$ traffic light for quick triage, the bottleneck diagnostic table to choose the right lever, and the C$^3$ scorecard to grade fleet health.

**Key Takeaways: Where to look first at fleet scale**

- **Every fleet-scale bottleneck has a dominant C$^3$ axis**: Compute, Communication, or Coordination, with many real bottlenecks spanning intersections. Identify the dominant axis before optimizing.
- **Measure the C$^3$ scorecard**: Compare MFU, scaling efficiency, and goodput with workload-specific baselines. The displayed thresholds screen for problems; traces must confirm the cause before selecting an optimization.
- **The compound C$^3$ loss is multiplicative**: Peak FLOP/s $\times$ compute-phase efficiency $\times$ scaling efficiency $\times$ runtime goodput = effective FLOP/s. The illustrative 100,000-GPU case retains ~18.2 percent of peak.
- **Coordination is the new axis**: Single-node overhead remains relevant, while distribution adds cross-machine dependencies. The coordination case attributes 40 percent of its modeled budget to checkpoints, failures, pipeline bubbles, scheduling, and maintenance.
- **Optimizing the wrong C$^3$ axis yields limited improvement**: Faster GPUs cannot fix a communication-bound fleet by themselves; faster networks help coordination only where transfer time, such as checkpoint I/O, contributes to that overhead.

^callout-takeaways--1-1-e48ac2b4

Back to top

## Source References

^source-references

Kaplan, Jared, Sam McCandlish, Tom Henighan, Tom B. Brown, Benjamin Chess, Rewon Child, Scott Gray, Alec Radford, Jeffrey Wu, and Dario Amodei. 2020. “Scaling Laws for Neural Language Models.” *ArXiv Preprint* abs/2001.08361.

^ref-kaplan2020scaling

Hoffmann, Jordan, Sebastian Borgeaud, Arthur Mensch, Elena Buchatskaya, Trevor Cai, Eliza Rutherford, Diego de Las Casas, et al. 2022. “Training Compute-Optimal Large Language Models.” *Advances in Neural Information Processing Systems (NeurIPS)* 35: 30016–30. https://doi.org/10.52202/068431-2176.

^ref-hoffmann2022chinchilla

## Source

[Repository Source](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/books/vol2/backmatter/appendix_c3.qmd) · [Original License](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/LICENSE.md)

[Rendered Reading Snapshot](https://mlsysbook.ai/vol2/backmatter/appendix_c3.html#sec-appdx-c3-taxonomy). Rendering provenance is recorded in the import manifest.
