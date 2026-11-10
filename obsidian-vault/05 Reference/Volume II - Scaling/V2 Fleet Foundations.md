---
title: V2 Fleet Foundations
type: Reference
volume: 2
chapter: 0
publication_status: Preview
source_repository: https://github.com/klappe-pm/cs249r_book
source_commit: de87c0103806d7bfb1c677dbb77a2b92fa00c298
source_path: books/vol2/backmatter/appendix_fleet.qmd
source_anchor: sec-appdx-fleet-foundations
source_mode: Source-Correlated Published HTML
tags:
- Type/Reference
- Book/Volume_2
rendered_source_url: https://mlsysbook.ai/vol2/backmatter/appendix_fleet.html
---

# V2 Fleet Foundations

[[Home|Home]] · [[01 Books/Volume II - Scaling/Volume 2 Overview|Volume Overview]]

^sec-appdx-fleet-foundations

Single-node performance engineering centers on memory hierarchy latencies and roofline ridge points. The moment a job spans multiple machines, network latency replaces cache latency, component failure becomes a statistical certainty, and interconnect bandwidth dictates scaling efficiency. This appendix gathers the fleet-scale constants, scaling laws, and thermal limits that underpin the book’s multi-node chapters, giving readers the physical baselines needed to reason about cluster-scale infrastructure. In C³ terms, these numbers define the physical scale on which compute capacity, communication bandwidth, and coordination overhead become measurable.

## How to Use This Appendix

^how-to-use-this-appendix

This appendix is designed as a reference when translating fleet-scale design questions into specific physical constraints and identifying available optimization levers. The five routing bullets below map common engineering questions to the sections that follow.

- **When evaluating inter-node communication**: Consult [[05 Reference/Volume II - Scaling/V2 Fleet Foundations#^sec-appdx-fleet-foundations-numbers-to-know|section 1.2]] for the bandwidth and latency hierarchy.
- **When sizing GPU allocations**: Consult [[05 Reference/Volume II - Scaling/V2 Fleet Foundations#^sec-appdx-fleet-foundations-scaling-physics|section 1.3]] to analyze why doubling accelerator counts does not halve training time.
- **When calculating cluster reliability**: Check [[05 Reference/Volume II - Scaling/V2 Fleet Foundations#^sec-appdx-fleet-foundations-numbers-to-know|section 1.2]] for mean time between failures (MTBF) tables and failure probability models.
- **When evaluating power and cooling limits**: Consult [[05 Reference/Volume II - Scaling/V2 Fleet Foundations#^sec-appdx-fleet-foundations-thermal-power|section 1.4]] for power density ceilings and cooling constraints.
- **When budgeting runtime overhead**: Use [[05 Reference/Volume II - Scaling/V2 Fleet Foundations#^sec-appdx-fleet-foundations-numbers-to-know|section 1.2]] for the four overhead categories that erode useful wall time.

## The Three System Paradigms

^sec-appdx-fleet-foundations-system-paradigms

Machine learning infrastructure at scale inherits design DNA from two distinct computing lineages and then breaks the assumptions of both. A designer must understand where ML systems borrow from high-performance computing (HPC) and where they borrow from warehouse-scale computing (WSC) to choose the right design trade-offs. A system architect who treats ML training as “just HPC” will build infrastructure that cannot tolerate failures. One who treats it as “just web services” will build infrastructure that cannot sustain the tight coupling that synchronous training demands.

### High-Performance Computing

^high-performance-computing

HPC systems descend from the supercomputer tradition, where the design goal is to maximize FLOP/s on tightly coupled simulations such as weather modeling, molecular dynamics, and nuclear physics. Because every node participates in lockstep, these clusters rely on specialized interconnects (InfiniBand), low-latency fabrics, and homogeneous hardware. Their fault tolerance follows the **checkpoint/restart** model: if one node fails, the entire job stops, rolls back to the last checkpoint, and resumes from that saved state. Batch schedulers such as Slurm allocate rigid resource shapes (“512 nodes for 24 hours”), treating nodes as individually tracked “pets.”

### Warehouse-Scale Computing

^warehouse-scale-computing

WSC systems descend from the web services tradition, aiming instead to maximize queries per second across loosely coupled services such as search, email, and social media. Because requests are independent, these fleets mix hardware generations over commodity Ethernet and rely on **redundancy** for fault tolerance: when a node fails, a load balancer reroutes traffic to another replica without the user noticing. Dynamic schedulers such as Kubernetes and Borg bin-pack workloads elastically across interchangeable, expendable “cattle” nodes.

### The ML Fleet as Hybrid Architecture

^the-ml-fleet-as-hybrid-architecture

ML systems require the computational throughput of HPC to train large models with synchronous gradient updates, yet they must operate at the scale and failure rates of WSC, where thousands of accelerators run for weeks. This tension produces a hybrid architecture that borrows selectively from both lineages.

Training workloads are synchronous and bandwidth-hungry like HPC jobs, whereas long-running fleet operations demand WSC-style fault tolerance, and inference workloads reverse the blend by pairing WSC latency sensitivity with HPC compute density. To serve both regimes, the network fuses TCP/IP control planes with InfiniBand or NVLink data planes. Fault tolerance combines checkpoint/restart with **elastic training** strategies where supported, which allow jobs to adjust resource allocations even when resharding, state restoration, or worker restarts remain necessary. Scheduling pairs all-or-nothing gang allocation for training with dynamic preemption and replacement. ML fleets therefore cannot adopt either HPC or WSC patterns wholesale; they combine elements from each according to the workload phase, as the design trade-offs across the three paradigms in [[05 Reference/Volume II - Scaling/V2 Fleet Foundations#^tbl-fleet-paradigm-comparison|table 1]] show.

| **Dimension**   |   **HPC (supercomputer)**   |  **WSC (web cloud)**  | **ML fleet (AI cluster)**                |
|:----------------|:---------------------------:|:---------------------:|:-----------------------------------------|
| **Philosophy**  |       Maximize FLOP/s       |     Maximize QPS      | Maximize Model Quality per Dollar/Watt   |
| **Coupling**    |         Tight (MPI)         |   Loose (RPC/HTTP)    | Hybrid (NCCL + RPC)                      |
| **State**       |       Stateful (RAM)        | Stateless (DB-backed) | Semi-Stateful (Checkpoints + KV Cache)   |
| **Network**     |      Latency-optimized      |  Bandwidth-optimized  | Bisection-bandwidth critical             |
| **Bottleneck**  | Compute throughput (FLOP/s) |    I/O (Disk/Net)     | Fabric or HBM, by workload phase         |
| **Fault model** |     Checkpoint/Restart      |  Redundancy/Replicas  | Checkpoint/restart + optional elasticity |
| **Scheduling**  |        Batch (Slurm)        |  Orchestration (K8s)  | Gang + preemption                        |
| **Node model**  |       Pets (tracked)        |  Cattle (expendable)  | Pets during job, cattle between jobs     |

Table 1: **Three System Paradigms**: ML fleets inherit design DNA from both HPC and WSC but break assumptions of each. Training resembles HPC (tight coupling), inference resembles WSC (elastic serving), and fault tolerance is a hybrid of both.

^tbl-fleet-paradigm-comparison

Five single-machine models reappear throughout the distributed chapters, each extended by a fleet-scale term. **[[05 Reference/Volume II - Scaling/V2 Single-Machine Foundations#^sec-appdx-dam-taxonomy|The D·A·M Taxonomy]]** states the single-machine forms; the list below records only what changes at scale.

- **Iron law** (${T}\approx {D_{\text{vol}}}/{\text{BW}} + {O}/({R_{\text{peak}}} \cdot {\eta_{\text{hw}}}) + {L_{\text{lat}}}$, **[[05 Reference/Volume II - Scaling/V2 Single-Machine Foundations#^sec-appdx-dam-taxonomy-iron-law-mapping|Iron Law Mapping]]**): At fleet scale, the data-movement term expands to include inter-node communication, and the Fleet Law replaces the single-machine sum.
- **Roofline Model** (**[[05 Reference/Volume II - Scaling/V2 Single-Machine Foundations#^sec-appdx-dam-taxonomy-roofline|The roofline bound]]**): At fleet scale, a third ceiling appears. **Network-bound** workloads are limited by inter-node bandwidth, which the communication-computation ratio in [[05 Reference/Volume II - Scaling/V2 Fleet Foundations#^sec-appdx-fleet-foundations-comm-compute-ratio|section 1.3.3]] measures.
- **Amdahl’s Law**: Caps strong-scaling speedup at $1/{r}$ for serial fraction ${r}$ ([[05 Reference/Volume II - Scaling/V2 Fleet Foundations#^ref-amdahl1967|Amdahl 1967]]). At fleet scale, the serial fraction includes synchronization barriers, exposed collective communication, and pipeline bubbles ([[05 Reference/Volume II - Scaling/V2 Fleet Foundations#^sec-appdx-fleet-foundations-amdahls-fleet|section 1.3.2]]).
- **Training state rule** (**[[05 Reference/Volume II - Scaling/V2 Single-Machine Foundations#^sec-appdx-dam-taxonomy-training-memory|Numeric Precision and Training Memory]]**): Mixed-precision training with the Adaptive Moment Estimation (Adam) optimizer holds about 16 bytes per parameter during training and about 14 bytes per parameter in a resumable checkpoint, before activations and framework metadata. At fleet scale, this footprint determines how model state is partitioned across devices (ZeRO, tensor parallelism, pipeline parallelism).
- **Little’s Law** (${Q_{\text{req}}} = {\lambda_{\text{arr}}} {T_{\text{lat}}}$) ([[05 Reference/Volume II - Scaling/V2 Fleet Foundations#^ref-little1961|Little 1961]]): Relates in-flight requests to arrival rate and time in system. At fleet scale, it sizes the number of serving replicas behind a load balancer (**[[05 Reference/Volume II - Scaling/V2 Inference Foundations#^sec-appdx-inference-scale-queuing-theory-batched-inference-bbf0|Queuing theory for batched inference]]**).

The transition from single-machine to fleet-scale reasoning requires extending these models with new dimensions: network topology, failure probability, and coordination overhead. The numbers in the next section provide the quantitative foundation for that extension.

------------------------------------------------------------------------

## Numbers Every Fleet Engineer Should Know

^sec-appdx-fleet-foundations-numbers-to-know

Crossing a server chassis boundary drops per-direction interconnect bandwidth by nearly an order of magnitude from intra-node NVLink to inter-node InfiniBand, while scaling a job from one node to thousands of accelerators shrinks the expected interval between hardware failures from years to hours. Just as single-machine analysis depends on a set of core numbers within each node, fleet-scale engineering is governed by the ratios and scaling behaviors that operate between nodes. Because hardware ratios shift across generations and failure rates depend on the assumed fault model, the reference values below provide baseline sanity checks while the accompanying equations show how to substitute different system assumptions.

**Systems Perspective 1.1: Node-level numbers for fleet reasoning**

Fleet reasoning depends on a few node-level numbers that directly affect fleet design. The training state rule of about 14 bytes per parameter describes common Adam checkpoint state, with larger footprints when gradients, activations, metadata, or extra optimizer buffers are included. NVLink vs. high-bandwidth memory (HBM) bandwidth informs intra-node parallelism placement. Peak FLOP/s and HBM capacity feed model FLOPs utilization (MFU), effective FLOP/s, batch sizing, and model sharding. [[05 Reference/Volume II - Scaling/V2 Fleet Foundations#^tbl-fleet-numbers-quick-ref|Table 2]] and the communication numbers below give inter-node and current-generation values. The memory hierarchy and roofline ridge points within a node (**[[05 Reference/Volume II - Scaling/V2 Single-Machine Foundations#^sec-appdx-dam-taxonomy-memory-hierarchy|Accelerator Memory Hierarchy]]**) provide the necessary baseline. Those node-level baselines make the fleet-level ratios easier to interpret.

**Systems Perspective 1.2: Three fleet numbers that matter most**

- **Bandwidth gap**: NVLink per-direction bandwidth within a node is ~9× faster than an InfiniBand NDR port between nodes. This ratio determines where parallelism boundaries belong, with model parallelism within a node and data parallelism across nodes.
- **MTBF scaling**: A cluster’s mean time between failures is the single-component mean time to failure (MTTF) divided by the number of components ($1/{N}$ scaling). At 100,000 GPUs, expect a failure every 30 minutes.
- **Effective utilization**: After MFU, scaling efficiency, and overhead losses compound, a cluster with 1,024 GPUs delivers roughly 34.0 percent of its peak FLOP/s as useful training work.

Back-of-envelope checks need only the condensed values in [[05 Reference/Volume II - Scaling/V2 Fleet Foundations#^tbl-fleet-numbers-quick-ref|table 2]]. Design and debugging work should use the detailed tables in each subsection.

| **Category**               | **Number**                                                                               | **Use**                                                                                                                                                                           |
|:---------------------------|:-----------------------------------------------------------------------------------------|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Communication**          | NVLink per-direction bandwidth ~9× IB NDR                                                | Parallelism boundary (in-node vs. cross-node)                                                                                                                                     |
| **Communication**          | IB NDR ~50 GB/s, ~5 μs one-way                                                           | Inter-node bandwidth and latency                                                                                                                                                  |
| **Compute**                | MFU 30–50%, ${\eta_{\text{scaling}}}$ ~83% @ 1K, ~56% @ 8K                               | Effective FLOP/s and scaling sanity checks                                                                                                                                        |
| **Coordination**           | MTBF 8K: ~366.2 min; 100K: ~30 min                                                       | Failure expectation and checkpoint cadence                                                                                                                                        |
| **Coordination**           | 175B checkpoint ~2,450 GB (14 B/param common Adam state)                                 | Recovery and storage sizing                                                                                                                                                       |
| **Coordination**           | ~77% of wall time left after overheads                                                   | Wall-clock utilization                                                                                                                                                            |
| **Power & sustainability** | AI rack ~70 kW; air limit ~30 kW                                                         | Cooling feasibility for the installed configuration                                                                                                                               |
| **Power & sustainability** | PUE liquid ~1.06, typical ~1.55; 10,000 H100s at 700 W ≈ 7 MW GPU-only proxy, before PUE | GPU-only proxy; add other IT loads before facility sizing (see [[05 Reference/Volume II - Scaling/V2 Fleet Foundations#^sec-appdx-fleet-foundations-thermal-power\|section 1.4]]) |

Table 2: **Numbers Every Fleet Engineer Should Know (Quick Reference)**: One-page summary of the fleet-scale reference numbers in this section. See [[05 Reference/Volume II - Scaling/V2 Fleet Foundations#^tbl-fleet-bandwidth-hierarchy|table 3]] and [[05 Reference/Volume II - Scaling/V2 Fleet Foundations#^tbl-fleet-latency-hierarchy|table 4]] for communication, [[05 Reference/Volume II - Scaling/V2 Fleet Foundations#^tbl-fleet-scaling-efficiency|table 5]] for compute, and [[05 Reference/Volume II - Scaling/V2 Fleet Foundations#^tbl-fleet-mtbf|table 6]] for coordination.

^tbl-fleet-numbers-quick-ref

### Invariant Scaling Ratios

^invariant-scaling-ratios

Three structural relationships govern how bandwidth, reliability, and collective communication behave as a cluster grows: the intra-to-inter-node bandwidth gap, the $1/{N}$ scaling of system MTBF, and the asymptotic per-GPU volume of Ring AllReduce. Because hardware ratios shift across generations, their numerical values must be re-evaluated for each target system.

#### Network Hierarchy Ratio

^network-hierarchy-ratio

The bandwidth gap between intra-node and inter-node communication is an important architectural comparison. Chip-to-chip links (NVLink, ICI) connect through short, wide, dedicated paths on a shared substrate. Inter-node links (InfiniBand, Ethernet) must traverse cables, switches, and protocol stacks. These design differences often favor intra-node bandwidth, but lane counts, multiple network ports, and topology determine the actual ratio.

Currently, NVLink 4.0 provides 9× more per-direction bandwidth than an InfiniBand NDR port. The ratio compares one accelerator’s aggregate intra-node connectivity with one network port; it is not a universal constant. Parallelism placement must compare the workload’s traffic with the sustained bandwidth actually provisioned at each boundary.

#### System MTBF Scaling

^system-mtbf-scaling

For ${N}$ independent components under a constant-failure-rate assumption, system MTBF ([[05 Reference/Volume II - Scaling/V2 Fleet Foundations#^eq-fleet-mtbf-system|equation 1]]) scales inversely with component count:

$$
{\text{MTBF}_{\text{system}}} = \frac{{\text{MTTF}_{\text{component}}}}{{N}} \tag{1}
$$

^eq-fleet-mtbf-system

Under this model the relation is exact rather than approximate. Doubling the cluster size halves the time between failures. At 100,000 GPUs with a per-GPU MTTF of 50,000 hours, the cluster experiences a GPU failure every 30 minutes. No fault tolerance strategy can avoid this; the question is how quickly the system recovers.

#### AllReduce Overhead Scaling

^allreduce-overhead-scaling

The bandwidth-optimal Ring AllReduce algorithm transfers $2({N_{\text{GPU}}}-1){M}/{N_{\text{GPU}}}$ bytes per participant, where ${M}$ is the collective payload size and ${N_{\text{GPU}}}$ is the number of participating GPUs ([[05 Reference/Volume II - Scaling/V2 Fleet Foundations#^ref-patarasuk2009|Patarasuk and Yuan 2009]]). As ${N_{\text{GPU}}}$ grows large, this approaches $2{M}$ per GPU, so the per-GPU bandwidth term is nearly independent of the number of GPUs; aggregate cluster traffic still grows with the number of participants. This is why Ring AllReduce scales well in the bandwidth term. The latency term, however, grows as $2({N_{\text{GPU}}}-1) \times {\alpha}$, making latency the bottleneck for small messages on large rings. This trade-off motivates hierarchical AllReduce strategies that use Ring AllReduce within nodes and Tree AllReduce across nodes.

### Communication Numbers

^communication-numbers

Whether a parallelism strategy can exchange activations on every layer or must amortize gradient updates across microbatches depends on which tier of the network hierarchy its traffic crosses. Each step down the hierarchy trades lower per-link bandwidth and higher one-way latency for larger physical reach across racks and data centers.

The bandwidth cliff between intra-node fabrics and scale-out network ports decides where tensor, pipeline, and data-parallel traffic must stay local ([[05 Reference/Volume II - Scaling/V2 Fleet Foundations#^tbl-fleet-bandwidth-hierarchy|table 3]]).

| **Interconnect**       | **Bandwidth** | **Typical role**                            |
|:-----------------------|:-------------:|:--------------------------------------------|
| **NVLink 4.0 (H100)**  |   450 GB/s    | Tensor/pipeline parallelism within a node   |
| **TPU v5p ICI**        |  1,200 GB/s   | Intra-pod model parallelism (Google)        |
| **PCIe Gen5 x16**      |    64 GB/s    | CPU-GPU data transfer, NIC attachment       |
| **IB GXDR (1.6 Tb/s)** |   200 GB/s    | Next-gen inter-node (2026+)                 |
| **IB XDR (800 Gb/s)**  |   100 GB/s    | Inter-node standard (2025+)                 |
| **IB NDR (400 Gb/s)**  |    50 GB/s    | Current inter-node standard for AI clusters |
| **IB HDR (200 Gb/s)**  |    25 GB/s    | Previous-gen inter-node                     |
| **RoCE v2 (100 Gb/s)** |   12.5 GB/s   | Budget clusters, inference fleets           |

Table 3: **Communication Bandwidth Hierarchy**: Per-direction bandwidth drops by roughly 9× crossing from intra-node (NVLink) to inter-node (InfiniBand). This ratio compares the H100 NVLink one-way rate against one InfiniBand NDR port and determines parallelism placement.

^tbl-fleet-bandwidth-hierarchy

One-way latency across interconnect tiers ([[05 Reference/Volume II - Scaling/V2 Fleet Foundations#^tbl-fleet-latency-hierarchy|table 4]]) determines whether synchronous collective operations are viable. Whereas microsecond-scale fabrics support per-step gradient synchronization, wide-area links require asynchronous or amortized updates.

| **Interconnect**      | **One-way latency** | **Implication**                                    |
|:----------------------|:-------------------:|:---------------------------------------------------|
| **InfiniBand NDR**    |        ~5 μs        | Low enough for synchronous AllReduce               |
| **InfiniBand HDR**    |        ~7 μs        | Adequate for most training topologies              |
| **RoCE v2**           |       ~10 μs        | Acceptable for data parallelism                    |
| **TCP/IP (Ethernet)** |       ~50 μs        | Higher overhead; workload-dependent viability      |
| **Cross-data-center** | ~40,000 μs (40 ms)  | Distance-dependent floor; amortize synchronization |

Table 4: **Communication Latency Hierarchy**: Latency determines whether synchronous training is feasible. TCP/IP is roughly 10× slower than InfiniBand NDR, raising synchronization cost in latency-sensitive configurations. The cross-data-center row is the speed-of-light floor for an illustrative 8,000 km fiber path.

^tbl-fleet-latency-hierarchy

These latency differences favor low-latency fabrics for frequent synchronization. Cross-data-center training must amortize transfers, place pipeline boundaries carefully, or relax synchronization when its learning algorithm permits.

### Compute Numbers

^compute-numbers

Raw peak FLOP/s is a necessary but misleading metric for fleet capacity planning. Single-device execution losses and additional scaling losses reduce effective throughput. Multiplying the two is valid only when their measurement windows exclude overlapping costs. Understanding these losses transforms fleet sizing from guesswork into engineering.

MFU measures what fraction of peak FLOP/s a training workload actually achieves. Well-optimized large-model training on current hardware achieves 30–50 percent MFU. The gap comes from memory stalls, kernel launch overhead, pipeline bubbles, and suboptimal operator fusion. These are workload-dependent reference values. Fleet-step MFU already includes in-step communication and pipeline losses; a separate scaling factor applies only to a single-device baseline that excludes those losses.

Scaling efficiency (${\eta_{\text{scaling}}}$) measures how much useful computation survives as accelerators are added. Modeled scaling efficiency for the 175B reference job ([[05 Reference/Volume II - Scaling/V2 Fleet Foundations#^tbl-fleet-scaling-efficiency|table 5]]) shows how per-GPU throughput erodes as cluster size grows at a fixed global batch.

| **Cluster size** | **Scaling efficiency (${\eta_{\text{scaling}}}$)** | **Implication**                                  |
|:-----------------|:--------------------------------------------------:|:-------------------------------------------------|
| **32 GPUs**      |                        ~90%                        | Near-linear regime; book convention, not modeled |
| **256 GPUs**     |                        ~87%                        | Tensor-parallel communication is the main loss   |
| **1,024 GPUs**   |                        ~83%                        | Pipeline fill and drain become visible           |
| **8,192 GPUs**   |                        ~56%                        | Pipeline bubble dominates at a fixed batch       |

Table 5: **Scaling Efficiency by Cluster Size**: Modeled for the 175B reference job (eight-way tensor and eight-way pipeline parallelism, HDR InfiniBand, fixed GPT-3 batch); the 32-GPU row is a book convention. These values are not a universal function of cluster size, since workload, parallelism, batch, fabric, and baseline measurement determine the observed loss.

^tbl-fleet-scaling-efficiency

Past a few thousand GPUs the fixed per-step costs of pipeline fill and drain dominate, which is why production systems grow the global batch, interleave pipeline stages, and overlap collectives with compute. Systems built this way, such as MegaScale, report near-linear scaling on thousands of GPUs ([[05 Reference/Volume II - Scaling/V2 Fleet Foundations#^ref-jiang2024megascale|Jiang et al. 2024]]).

### Coordination Numbers

^coordination-numbers

At fleet scale, coordination (failure recovery, checkpointing, and maintenance) consumes a measurable fraction of wall-clock time. These numbers quantify the costs of keeping a large cluster running.

#### Failure Rates by Cluster Size

^failure-rates-by-cluster-size

Cluster MTBF scaling ([[05 Reference/Volume II - Scaling/V2 Fleet Foundations#^tbl-fleet-mtbf|table 6]], calculated for a per-GPU MTTF of 50,000 hours) dictates the required checkpoint frequency. As accelerator counts grow from hundreds to tens of thousands, the interval between expected hardware interruptions shrinks from days to minutes.

| **Cluster size** | **MTBF (GPU-only)** | **Minutes**  | **$\Pr(\text{failure})$ in 24 hours** |
|:-----------------|:-------------------:|:------------:|:-------------------------------------:|
| **256 GPUs**     |       195.3 h       | 11,718.8 min |                 11.6%                 |
| **2,048 GPUs**   |       24.4 h        | 1,464.8 min  |                 62.6%                 |
| **8,192 GPUs**   |        6.1 h        |  366.2 min   |                  98%                  |
| **100,000 GPUs** |       0.50 h        |    30 min    |                 100%                  |

Table 6: **MTBF and Failure Probability by Cluster Size**: GPU-only failure model with per-GPU MTTF of 50,000 hours. Real clusters also experience NIC, PSU, cable, and switch failures, so these GPU-only intervals overstate the true cluster MTBF. The probability column uses $\Pr(\geq 1\ \text{failure}) = 1 - e^{-{t}/{\text{MTBF}}}$ for ${t}= 24$ hours.

^tbl-fleet-mtbf

Failure is no longer an edge case at 8,192 GPUs and above. GPU-only MTBF is about 366.2 min at 8,192 GPUs, and the probability of at least one GPU failure within 24 hours is 98 percent. Fault tolerance is not optional at fleet scale; it is a prerequisite for completing any long-running training job. **[[01 Books/Volume II - Scaling/02 Distributed ML/07 Fault Tolerance/V2-07 Fault Tolerance#^sec-fault-tolerance-reliability|Fault Tolerance]]** covers the mechanisms in detail.

#### Checkpoint Sizes

^checkpoint-sizes

Checkpointing is the primary recovery mechanism, and its storage footprint grows linearly with model parameter count. A common mixed-precision Adam checkpoint serializes 14 bytes per parameter (2 bytes for BF16 weights and 12 bytes for FP32 master weights, momentum, and variance), which sets both total checkpoint capacity and write duration at a given storage bandwidth ([[05 Reference/Volume II - Scaling/V2 Fleet Foundations#^tbl-fleet-checkpoint-sizes|table 7]]). Gradients are normally transient and recomputed after restore rather than serialized as durable checkpoint state.

| **Model size**      | **Checkpoint size** | **Write time @ 100 GB/s** |
|:--------------------|:-------------------:|:-------------------------:|
| **7B parameters**   |        98 GB        |          0.98 s           |
| **70B parameters**  |       980 GB        |           9.8 s           |
| **175B parameters** |      2,450 GB       |          24.5 s           |
| **1T parameters**   |        14 TB        |          2.3 min          |

Table 7: **Checkpoint Sizes by Model Scale**: Uses 14 bytes/parameter for common mixed-precision Adam checkpoint state. Write time assumes 100 GB/s aggregate storage bandwidth. Asynchronous checkpointing (**[[01 Books/Volume II - Scaling/02 Distributed ML/07 Fault Tolerance/V2-07 Fault Tolerance#^sec-fault-tolerance-reliability|Fault Tolerance]]**) can overlap writes with training, reducing the visible overhead.

^tbl-fleet-checkpoint-sizes

#### Overhead Budgets

^overhead-budgets

Failure recovery and checkpointing are only part of the wall-clock budget. At fleet scale, [[05 Reference/Volume II - Scaling/V2 Fleet Foundations#^tbl-fleet-overhead-budgets|table 8]] separates four recurring categories of overhead that consume time not spent on useful training.

| **Overhead category**   | **Typical budget** | **Lever**                                |
|:------------------------|:------------------:|:-----------------------------------------|
| **Pipeline bubbles**    |        ~5%         | Increase microbatches per pipeline stage |
| **Checkpointing**       |        ~3%         | Async checkpointing, faster storage      |
| **Failure recovery**    |        ~10%        | Faster detection, elastic rescheduling   |
| **Maintenance windows** |        ~5%         | Rolling upgrades, live migration         |

Table 8: **Overhead Budgets for Fleet-Scale Training**: These are fractions of wall-clock time, and failure recovery is the largest of the four. Combined additively, the share of wall time left is $\approx 1.0 - (0.05 + 0.03 + 0.10 + 0.05) = 0.77 \approx 77\%$. Pipeline bubbles lie inside retained steps and are a program goodput loss, while the other three fall outside the steps, so this share is not a single goodput factor.

^tbl-fleet-overhead-budgets

#### Power and Sustainability Numbers

^power-and-sustainability-numbers

Fleet-scale capacity planning and sustainability reporting require a few power numbers that every fleet engineer should know. At fleet scale, the key numbers are **rack power density**, **power usage effectiveness (PUE)**, and the **air-cooling limit**, which determine where construction is feasible and what the facility load will be ([[05 Reference/Volume II - Scaling/V2 Fleet Foundations#^tbl-appendix-fleet-power-cooling-reference|table 9]]).

| **Quantity**               | **Typical value** | **Use**                                                     |
|:---------------------------|:-----------------:|:------------------------------------------------------------|
| **Traditional rack**       |       12 kW       | Baseline for non-AI data centers                            |
| **AI rack (current gen)**  |       70 kW       | Evaluate cooling capacity                                   |
| **AI rack (high-density)** |      100 kW       | Direct-to-chip liquid                                       |
| **Air cooling limit**      |  ~30 kW per rack  | Illustrative configuration limit; verify installed capacity |
| **PUE (liquid-cooled AI)** |       ~1.06       | Best case: facility load ≈ IT load                          |
| **PUE (best air-cooled)**  |       ~1.12       | Hyperscale best practice                                    |
| **PUE (industry average)** |       ~1.55       | Sanity check for cost/carbon                                |
| **H100 TDP**               |   700 W per GPU   | GPU-only proxy: 10,000 $\times$ 700 W = 7 MW                |

Table 9: **Power and Cooling Reference Numbers**: Rack power densities, air-cooling limits, and PUE values that govern fleet-scale capacity planning and sustainability reporting. Each row pairs a typical value with the engineering decision it informs.

^tbl-appendix-fleet-power-cooling-reference

A GPU-only power proxy (MW) = (number of GPUs $\times$ thermal design power (TDP) per GPU)/$10^6$ excludes host CPUs, memory, storage, and networking. Facility load = total IT load $\times$ PUE; applying PUE to the GPU-only proxy omits those other IT loads and is not a complete facility budget. A 10,000-GPU H100 cluster at 700 W each gives a 7 MW GPU-only proxy; multiplying by PUE 1.55 gives 10.8 MW before accounting for the other IT loads. [[05 Reference/Volume II - Scaling/V2 Fleet Foundations#^sec-appdx-fleet-foundations-thermal-power|Section 1.4]] carries this power arithmetic into facility overhead, and **[[01 Books/Volume II - Scaling/04 The Responsible Fleet/15 Sustainable AI/V2-15 Sustainable AI#^sec-sustainable-ai|Sustainable AI]]** converts it into carbon and cost.

### Current Hardware Reference (C. 2025–2026)

^current-hardware-reference-c--20252026-f5c8be65

Frontier accelerators from the 2025–2026 generation provide the point-in-time per-chip specifications needed for back-of-envelope fleet sizing ([[05 Reference/Volume II - Scaling/V2 Fleet Foundations#^tbl-fleet-hardware-ref|table 10]]), illustrating how compute throughput, memory capacity, and interconnect bandwidth evolve at different rates across vendors.

| **Spec**             |     **NVIDIA B200**     |                                                   **AMD MI300X**                                                    |                                                    **Google TPU v6e**                                                    |
|:---------------------|:-----------------------:|:-------------------------------------------------------------------------------------------------------------------:|:------------------------------------------------------------------------------------------------------------------------:|
| **BF16/FP16 Peak**   |      2,250 TFLOP/s      |                                                    1,307 TFLOP/s                                                    |                                                       918 TFLOP/s                                                        |
| **Memory Bandwidth** |         8 TB/s          |                                                      5.30 TB/s                                                      |                                                        1.64 TB/s                                                         |
| **HBM Capacity**     |         180 GB          |                                                       192 GB                                                        |                                                          32 GB                                                           |
| **Intra-Node Link**  | 1,800 GB/s (NVLink 5.0) | 896 GB/s (Infinity Fabric) ([[05 Reference/Volume II - Scaling/V2 Fleet Foundations#^ref-amd2023mi300x\|AMD 2023]]) | 800 GB/s (ICI) ([[05 Reference/Volume II - Scaling/V2 Fleet Foundations#^ref-googleCloudTpuV6eDocs\|Google Cloud 2026]]) |
| **TDP**              |         1,000 W         |                                                        750 W                                                        |                                                      Not published                                                       |

Table 10: **Fleet-Scale Hardware Reference (c. 2025–2026)**: Per-accelerator specifications for the 2025–2026 generations. The B200, MI300X, and TPU v6e (Trillium) represent the frontier of fleet-scale compute density and memory bandwidth. Intra-node link rates are bidirectional aggregates per accelerator. Google does not publish a per-chip TDP for the TPU v6e.

^tbl-fleet-hardware-ref

At the cluster level, a single DGX H100 SuperPOD scalable unit packages 32 DGX H100 nodes (256 H100 GPUs) ([[05 Reference/Volume II - Scaling/V2 Fleet Foundations#^ref-nvidia2023dgxSuperpodH100|NVIDIA 2023]]), whereas full data-center deployments link dozens of such pods together. Meta’s Grand Teton clusters reach 24,576 H100 GPUs ([[05 Reference/Volume II - Scaling/V2 Fleet Foundations#^ref-meta2024genaiInfrastructure|Meta Engineering 2024]]), Google’s Tensor Processing Unit (TPU) v5p pods scale to 8,960 chips, and the largest announced clusters as of 2025 exceed 100,000 accelerators.

------------------------------------------------------------------------

## Scaling Physics

^sec-appdx-fleet-foundations-scaling-physics

When a training job expands from a single 8-GPU server to thousands of accelerators across a fabric, network transfers, synchronization barriers, and pipeline bubbles consume a growing share of each step. The reference numbers in [[05 Reference/Volume II - Scaling/V2 Fleet Foundations#^sec-appdx-fleet-foundations-numbers-to-know|section 1.2]] describe what individual links and devices can deliver; scaling physics explains how much of that capacity survives as devices are added. Reasoning starts from the ceiling on a single accelerator (the roofline) and extends it to the cluster through three models: Amdahl’s Law for fleet serial overhead, the communication-computation ratio, and weak scaling.

### From the Accelerator Roofline to the Fleet

^sec-appdx-fleet-foundations-roofline

Fleet performance rests on per-accelerator performance. **[[05 Reference/Volume II - Scaling/V2 Single-Machine Foundations#^sec-appdx-dam-taxonomy-roofline|The roofline bound]]** states the single-accelerator roofline, ${R_{\text{attain}}} = \min({R_{\text{peak}}}, {I}\times {\text{BW}})$, and its ridge point ${I_{\text{ridge}}} = {R_{\text{peak}}}/{\text{BW}}$, which is about 295.2 FLOP/byte for an H100. A kernel below the ridge is memory bound, and a kernel above it is compute bound.

The roofline is a single-accelerator bound, but its logic is what scales. At fleet level the binding bandwidth is no longer HBM but the interconnect, and the bytes moved are the gradients and activations crossing the network. The ratio of network time to local arithmetic time is the communication-computation ratio ([[05 Reference/Volume II - Scaling/V2 Fleet Foundations#^sec-appdx-fleet-foundations-comm-compute-ratio|section 1.3.3]]), the roofline of the fleet and the lens the rest of this section applies.

On a real cluster, that shift from HBM bandwidth to network and synchronization limits shows up directly in step throughput: when a training job provisioned with 4,096 GPUs achieves only 2.5× the throughput of a 1,024-GPU run, the implied scaling efficiency is about 51.9 percent at the larger size. The three subsections that follow separate whether that loss comes from an unavoidable Amdahl serial fraction, an unfavorable communication-computation ratio, or a fixed-problem strong-scaling regime.

### Amdahl’s Law at Fleet Scale

^sec-appdx-fleet-foundations-amdahls-fleet

When a distributed training loop spends 10 percent of every step waiting on exposed AllReduce collectives, pipeline bubbles, or checkpoint flushes, adding thousands of extra GPUs cannot accelerate the fixed job by more than 10$\times$. Amdahl’s Law establishes that the maximum speedup of a parallel system is limited by its serial fraction ${r}$. At fleet scale, the “serial fraction” includes more than sequential code; it covers every operation that forces all ${N}$ GPUs to wait:

- **AllReduce synchronization**: All GPUs must complete their gradient computation before any can proceed.
- **Pipeline bubbles**: The warmup and cooldown phases of pipeline parallelism leave stages idle.
- **Checkpoint writes**: Even asynchronous checkpoints contend for storage bandwidth.
- **Python-level overhead**: Single-threaded operations in the training loop (data loading, metric logging).

To see the fleet-scale implications, consider a training workload where 10 percent of wall-clock time is spent in synchronization, communication, and other serial overhead. Amdahl’s Law gives the following speedups:

- With 32 GPUs: 7.8× speedup (~24 percent scaling efficiency)
- With 256 GPUs: 9.7× speedup (diminishing returns begin)
- With 1,024 GPUs: 9.9× speedup (approaching the ceiling)
- With 8,192 GPUs: 10× speedup (nearly at the Amdahl limit)
- With ${N}\to \infty$: capped at 10×

With 10 percent serial overhead, no amount of hardware can deliver more than 10× speedup on this fixed workload. This is why fleet-scale training does not add more GPUs to the same problem. It scales the problem (weak scaling) to keep the serial fraction small relative to the total work.

**Systems Perspective 1.3: The compound overhead trap**

The 10 percent serial fraction above is optimistic. In practice, fleet-scale serial overhead accumulates from multiple sources: 5 percent pipeline bubbles + 3 percent checkpointing + 10 percent failure recovery + 5 percent maintenance. These are not all strictly serial in the Amdahl sense (some overlap with computation), but they illustrate how quickly small per-category overheads compound into significant throughput loss.

### The Communication-Computation Ratio

^sec-appdx-fleet-foundations-comm-compute-ratio

When 256 GPUs train a 350M-parameter model over InfiniBand, gradient AllReduce takes three times longer than the forward and backward passes combined, leaving the accelerators idle for most of the step. Any distributed training strategy must determine whether computation between synchronization points takes long enough to hide the communication. [[05 Reference/Volume II - Scaling/V2 Fleet Foundations#^eq-comm-compute-ratio|Equation 2]] defines the **communication-computation ratio** (${\rho}$) that answers this directly:

$$
{\rho}= \frac{{T_{\text{comm}}}({N})}{{T_{\text{compute}}}/{N}} \tag{2}
$$

^eq-comm-compute-ratio

When ${\rho}< 1$, computation takes longer than communication; hiding that communication still requires independent work and sufficient resources. When ${\rho}> 1$, the system is communication bound, and GPUs spend more time waiting for data than computing on it.

The ratio is the time-domain form of the **communication intensity** (CI) defined in **[[01 Books/Volume II - Scaling/00 Introduction/01 Introduction/V2-01.03 From Single Node to Fleet#^sec-vol2-introduction-ci-ratio|Communication intensity (the CI ratio)]]**, the bytes a step moves across the network per FLOP it executes locally. If each device moves ${M}$ bytes across the network per step at effective network bandwidth ${\text{BW}_{\text{network}}}$ and executes its ${O}$ local FLOPs at realized rate ${R}$, then in the bandwidth-dominated regime

$$
{\rho}\approx \frac{{M}/{\text{BW}_{\text{network}}}}{{O}/{R}} = {\text{CI}} \times \frac{{R}}{{\text{BW}_{\text{network}}}}, \qquad {\text{CI}} = \frac{{M}}{{O}} \tag{3}
$$

^eq-fleet-ci-rho

[[05 Reference/Volume II - Scaling/V2 Fleet Foundations#^eq-fleet-ci-rho|Equation 3]] shows that exposed communication begins when ${\text{CI}}$ exceeds ${\text{BW}_{\text{network}}}/{R}$, the network counterpart of the roofline ridge point. Because a device executes far more FLOP/s than its network link moves bytes per second, that threshold is a small fraction of a byte per FLOP, and a faster accelerator lowers it further. An accelerator upgrade alone can therefore turn a compute-bound job into a communication-bound one.

Communication-to-computation ratios across representative scenarios ([[05 Reference/Volume II - Scaling/V2 Fleet Foundations#^tbl-fleet-comm-comp|table 11]]) reveal why the parallelism strategy must match the workload’s arithmetic footprint. Comparing a multi-billion-parameter model against a smaller architecture on the same interconnect shows how quickly collective synchronization can overtake local compute.

| **Scenario**                              | **${T_{\text{comm}}}({N})$**          | **${T_{\text{compute}}}/{N}$** | **${\rho}$** |
|:------------------------------------------|:--------------------------------------|:------------------------------:|:------------:|
| **Data parallel, 7B model, 256 GPUs**     | 560.4 ms (AllReduce over IB NDR)      |         ~5 s (fwd+bwd)         |     0.11     |
| **Data parallel, 340M model, 256 GPUs**   | 29.6 ms (AllReduce over IB NDR)       |        ~10 ms (fwd+bwd)        |      3       |
| **Ideal one-way 16 MB transfer (NVLink)** | ~0.04 ms (bandwidth-only lower bound) |       ~1 ms (one layer)        |    0.036     |

Table 11: **Communication-Computation Ratio (${\rho}$)**: When ${\rho}\ll 1$, communication can potentially be hidden if dependencies permit. When ${\rho}\gg 1$, the system is communication-bound and GPUs sit idle waiting for data. The NVLink row is a bandwidth-only point-to-point lower bound; a tensor-parallel collective also incurs topology, latency, and contention costs.

^tbl-fleet-comm-comp

The 7B model on 256 GPUs achieves ${\rho}=$ 0.11, so communication takes about 11.2 percent as long as computation, which can be partially overlapped. The 340M model on the same cluster has ${\rho}=$ 3. Communication dominates, which makes this configuration communication-bound. The solution is either to use fewer GPUs (reduce ${N}$ in the AllReduce) or to increase the computation per step (larger batch size, gradient accumulation). For the single 16 MB point-to-point payload, the ideal bandwidth-only lower bound is ${\rho}=$ 0.036, which is not a tensor-parallel collective model and cannot by itself establish whether an implementation is compute-bound.

### Weak Scaling at Fleet Scale

^sec-appdx-fleet-foundations-weak-scaling-fleet

Provisioning 8,192 GPUs to finish a fixed 7B-parameter training run faster quickly hits Amdahl’s synchronization wall. Using those same 8,192 GPUs to train a 70B- or 700B-parameter model keeps per-device arithmetic work high enough to amortize communication. Amdahl’s Law paints a pessimistic picture because it assumes a fixed problem size. In practice, fleet-scale training often follows **weak scaling**: the problem size (tokens, data, model parameters) grows proportionally with the number of GPUs. Gustafson’s Law captures this more optimistic view ([[05 Reference/Volume II - Scaling/V2 Fleet Foundations#^ref-gustafson1988|Gustafson 1988]]).

Weak scaling reflects how fleets are actually used, not merely a mathematical convenience. Engineers do not use 8,192 GPUs to train a 7B model faster; they use them to train a 70B or 700B model in reasonable time. As models and training batches grow, engineers often increase the compute performed between synchronization points. For dense Transformers, compute is commonly estimated as about 6$\times$ parameters $\times$ tokens, while gradient communication scales with parameter bytes. The communication-computation ratio ${\rho}$ therefore depends on batch size, sequence length, accumulation, and parallelism layout rather than on parameter count alone.

**Systems Perspective 1.4: The compound loss of fleet utilization**

A 1,024-GPU H100 cluster has a peak aggregate throughput of 1,012,736 TFLOP/s. This illustrative decomposition keeps the factors disjoint: MFU represents per-device kernel and memory efficiency, scaling efficiency represents distributed communication and pipeline losses, and runtime goodput represents checkpointing, failure recovery, and maintenance. The effective throughput is:

$$
{R_{\text{eff}}} = {N}{R_{\text{peak}}} \times {\text{MFU}} \times {\eta_{\text{scaling}}} \times {\eta_{\text{runtime}}}
$$

$$
= 1,012,736 TFLOP/s \times 0.50 \times 0.83 \times 0.82 \approx 344,634.1 \text{ TFLOP/s}
$$

The cluster delivers 34.0 percent of its peak FLOP/s as useful training work. The remaining 66.0 percent is explained by retained factors of 50 percent MFU, 83 percent scaling efficiency, and 82 percent runtime goodput.

These losses reflect the physics of fleet-scale computation rather than a failure of engineering. Additional GPUs can increase useful throughput while reducing efficiency, but the gain must be measured against smaller configurations. The goal is not to reach 100 percent utilization; the goal is to deliver trained models faster than any smaller configuration could.

## Thermal and Power Physics

^sec-appdx-fleet-foundations-thermal-power

A cluster design calling for 10,000 H100 GPUs at 700 W each represents a 7 MW GPU-only power proxy and draws 10.8 MW of facility power at a typical PUE of 1.55, the electrical load of a small town even before adding host CPUs, memory, storage, and networking inside the IT boundary. Because every watt of electrical power delivered to silicon converts to heat that must be removed, thermal and power limits govern where a cluster can be built, how densely accelerators can be packed into each rack, and what the facility will cost to operate. A cluster that is architecturally sound in software and networking but exceeds its power-delivery or heat-removal envelope cannot be deployed.

### Power Density Wall

^sec-appdx-fleet-foundations-power-density

The shift from traditional data center workloads to AI training has multiplied the power each rack draws, and [[05 Reference/Volume II - Scaling/V2 Fleet Foundations#^tbl-fleet-power-density-fleet|table 12]] quantifies the gap. As accelerator TDPs climb toward a kilowatt per chip, standard air-cooled server rooms quickly run out of thermal headroom.

| **Configuration**             | **Power per rack** | **Cooling implication**                     |
|:------------------------------|:------------------:|:--------------------------------------------|
| **Traditional data center**   |       12 kW        | Standard air cooling sufficient             |
| **AI cluster (current gen)**  |       70 kW        | Evaluate cooling capacity                   |
| **AI cluster (high-density)** |       100 kW       | Evaluate direct-to-chip cooling             |
| **Air cooling limit**         |       ~30 kW       | Illustrative forced-air configuration limit |

Table 12: **Power Density: Traditional vs. AI Workloads**: AI racks consume roughly 5.8× the power of traditional racks. The ~30 kW air-cooling value is a configuration reference, not a universal physical ceiling. Higher rack density requires checking the installed airflow, heat exchangers, and server cooling design.

^tbl-fleet-power-density-fleet

The 5.8× increase in rack power density between traditional and AI workloads is a binding constraint on facility design, not merely an engineering challenge. Existing data centers built for 12 kW racks cannot be “retrofitted” with AI hardware. The electrical distribution, cooling infrastructure, and floor loading must all be redesigned. This is why new AI-focused data centers are being built from the ground up with liquid cooling as the baseline assumption.

### The Energy Hierarchy at Scale

^sec-appdx-fleet-foundations-energy-hierarchy

In a data center at the 2023 industry-average PUE, delivering 1 MW of electrical power to GPU racks requires another 580 kW to run the chillers, fans, and power conversion equipment that keep the room operating. PUE measures facility energy overhead: total facility energy divided by IT equipment energy ([[05 Reference/Volume II - Scaling/V2 Fleet Foundations#^ref-thegreengrid2007pue|The Green Grid 2007]]; [[05 Reference/Volume II - Scaling/V2 Fleet Foundations#^ref-davis2022uptime|Uptime Institute 2022]]). A PUE of 1.0 would mean all facility energy is delivered to IT equipment; values above 1.0 represent overhead for cooling, power conversion, lighting, and other facility systems. Cooling technology drives much of that overhead, so PUE falls from legacy enterprise facilities to liquid-cooled AI data centers ([[05 Reference/Volume II - Scaling/V2 Fleet Foundations#^tbl-fleet-pue-fleet|table 13]]).

| **Data center type**             | **PUE** | **Overhead per MW of IT load** |
|:---------------------------------|:-------:|:------------------------------:|
| **Liquid-cooled AI data center** |  1.06   | 60 kW cooling + infrastructure |
| **Best-in-class air-cooled**     |  1.12   |        120 kW overhead         |
| **Industry average (2022)**      |  1.55   |        550 kW overhead         |
| **Industry average (2023)**      |  1.58   |        580 kW overhead         |

Table 13: **Power usage effectiveness by facility type**: Lower is better. The listed PUE values are facility scenarios. Direct liquid cooling can reduce heat-removal overhead, but PUE also depends on climate, heat rejection, power conversion, and load. The gap between the 2023 industry average (1.58) and liquid-cooled (1.06) represents about a 32.9 percent reduction in total facility power at fixed IT load; the non-IT overhead drops from 0.58 MW to 0.06 MW per MW of IT load.

^tbl-fleet-pue-fleet

For fleet-scale cost calculations, PUE directly multiplies the electricity bill. A 10 MW IT load in a data center at the 2023 industry average (PUE 1.58) requires 15.8 MW total. The same load in a liquid-cooled facility (PUE 1.06) requires only 10.6 MW, a savings of 5.2 MW. For a facility that runs continuously at the reference on-premises electricity price of \$0.07/kWh, that difference is worth about \$3.2M per year. **[[01 Books/Volume II - Scaling/04 The Responsible Fleet/15 Sustainable AI/V2-15 Sustainable AI#^sec-sustainable-ai|Sustainable AI]]** covers the full sustainability implications.

------------------------------------------------------------------------

## Summary

^summary

Fleet scale changes every constraint a single machine imposes. ML fleets combine the tight coupling of high-performance computing for training with the elastic fault tolerance of warehouse-scale computing for serving, and they cannot adopt either tradition wholesale. NVLink provides about 9× more per-direction bandwidth than an InfiniBand NDR port, which is why bandwidth-hungry parallelism stays inside the node. Cluster MTBF scales as $1/{N}$, so at 8,192 GPUs a GPU fails about every 366.2 minutes, with 98 percent probability of at least one failure in 24 hours. After disjoint factors for MFU (about 50 percent), scaling efficiency (about 83 percent), and runtime goodput (about 82 percent), a 1,024-GPU cluster delivers about 34.0 percent of peak FLOP/s as useful work.

Three considerations govern the design response. The communication-computation ratio ${\rho}$ indicates the potential for overlap and the pressure from communication; dependencies and available resources determine how much communication can be hidden behind computation. Weak scaling, which grows the problem with the fleet, preserves useful work per device, while strong scaling remains the right choice when the goal is to finish fixed work sooner. Rack power density, about 5.8× the traditional reference for current AI racks, determines the cooling design, subject to the installed heat-removal capacity rather than a universal threshold.

Back to top

## Source References

^source-references

Amdahl, Gene M. 1967. “Validity of the Single Processor Approach to Achieving Large Scale Computing Capabilities.” *Proceedings of the April 18-20, 1967, Spring Joint Computer Conference on - AFIPS ’67 (Spring)*, AFIPS ’67 (spring), 483–85. https://doi.org/10.1145/1465482.1465560.

^ref-amdahl1967

Little, John D. C. 1961. “A Proof for the Queuing Formula: $L = \lambda W$.” *Operations Research* 9 (3): 383–87. https://doi.org/10.1287/opre.9.3.383.

^ref-little1961

Patarasuk, Pitch, and Xin Yuan. 2009. “Bandwidth Optimal All-Reduce Algorithms for Clusters of Workstations.” *Journal of Parallel and Distributed Computing* 69 (2): 117–24. https://doi.org/10.1016/j.jpdc.2008.09.002.

^ref-patarasuk2009

Jiang, Ziheng, Haibin Lin, Yinmin Zhong, Qi Huang, Yangrui Chen, Zhi Zhang, Yanghua Peng, et al. 2024. “MegaScale: Scaling Large Language Model Training to More Than 10,000 GPUs.” *21st USENIX Symposium on Networked Systems Design and Implementation (NSDI 24)*, 745–60.

^ref-jiang2024megascale

AMD. 2023. *AMD Instinct MI300X Accelerators*. AMD product documentation.

^ref-amd2023mi300x

Google Cloud. 2026. *TPU v6e*.

^ref-googleCloudTpuV6eDocs

NVIDIA. 2023. *NVIDIA DGX SuperPOD: Next Generation Scalable Infrastructure for AI Leadership*. RA-11333-001 V11. NVIDIA.

^ref-nvidia2023dgxSuperpodH100

Meta Engineering. 2024. *Building Meta’s GenAI Infrastructure*. Engineering at Meta Blog.

^ref-meta2024genaiInfrastructure

Gustafson, John L. 1988. “Reevaluating Amdahl’s Law.” *Communications of the ACM* 31 (5): 532–33. https://doi.org/10.1145/42411.42415.

^ref-gustafson1988

The Green Grid. 2007. *Green Grid Data Center Power Efficiency Metrics: PUE and DCIE*. The Green Grid.

^ref-thegreengrid2007pue

Uptime Institute. 2022. *Uptime Institute Global Data Center Survey 2022*. Uptime Institute.

^ref-davis2022uptime

## Source

[Repository Source](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/books/vol2/backmatter/appendix_fleet.qmd) · [Original License](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/LICENSE.md)

[Rendered Reading Snapshot](https://mlsysbook.ai/vol2/backmatter/appendix_fleet.html#sec-appdx-fleet-foundations). Rendering provenance is recorded in the import manifest.
