---
title: V2 Communication Foundations
type: Reference
volume: 2
chapter: 0
publication_status: Preview
source_repository: https://github.com/klappe-pm/cs249r_book
source_commit: de87c0103806d7bfb1c677dbb77a2b92fa00c298
source_path: books/vol2/backmatter/appendix_communication.qmd
source_anchor: sec-appdx-communication-foundations
source_mode: Source-Correlated Published HTML
tags:
- Type/Reference
- Book/Volume_2
rendered_source_url: https://mlsysbook.ai/vol2/backmatter/appendix_communication.html
---

# V2 Communication Foundations

[[Home|Home]] · [[01 Books/Volume II - Scaling/Volume 2 Overview|Volume Overview]]

^sec-appdx-communication-foundations

Distributed training spends a substantial fraction of execution time synchronizing gradients, redistributing activations, and routing tokens across network fabrics. Rather than cluttering chapter text with step-by-step proofs, this appendix provides the quantitative communication cost models used throughout the book: point-to-point formulations (${\alpha}$-${\beta}$ and LogGP), collective execution bounds (AllReduce, AllGather, ReduceScatter, AllToAll), pipeline bubble math, and gradient compression thresholds.

## How to Use This Appendix

^how-to-use-this-appendix

This appendix is designed as a reference when translating a distributed training symptom (“AllReduce is slow,” “pipeline bubbles are killing throughput,” “should we compress gradients?”) into a quantitative diagnosis. Conventions used here follow the book-wide notation. ${\alpha}$ denotes per-message startup latency, and ${\beta}$ denotes link bandwidth in bytes per second. ${n}$ denotes point-to-point message size, and ${n^*}$ denotes the ${\alpha}$-${\beta}$ crossover point. ${N}$ denotes the number of participating GPUs, and ${M}$ denotes collective payload size in bytes.

- **When AllReduce is slow**: Use [[05 Reference/Volume II - Scaling/V2 Communication Foundations#^sec-appdx-comm-foundations-collective-complexity|section 1.2]] to compute the expected time and compare ring vs. tree costs.
- **When choosing ring vs. tree**: Use [[05 Reference/Volume II - Scaling/V2 Communication Foundations#^sec-appdx-comm-foundations-algorithm-selection|section 1.3]] and the crossover analysis to match algorithm to message size.
- **When pipeline bubbles dominate**: Use [[05 Reference/Volume II - Scaling/V2 Communication Foundations#^sec-appdx-comm-foundations-pipeline-arithmetic|section 1.4]] to compute bubble fraction and determine the required microbatch count.
- **When gradient compression is proposed**: Use [[05 Reference/Volume II - Scaling/V2 Communication Foundations#^sec-appdx-comm-foundations-compression|section 1.5]] to run the break-even calculation before committing engineering effort.

## The ${\alpha}$-${\beta}$ Communication Model

^sec-appdx-comm-foundations-alpha-beta

**Systems Perspective 1.1: Why this matters**

The time a gradient synchronization takes across 256 GPUs must be estimated before a cluster topology is chosen. The ${\alpha}$-${\beta}$ model plays the role of a roofline for networks, giving a first-order prediction of transfer time from two hardware parameters and the message size.

Every point-to-point transfer on a network follows the same pattern: the sender pays a fixed startup cost to initiate the message, then transmits the payload at a rate determined by the link’s bandwidth. This two-parameter model captures the essential physics of network communication. Specifically, the **${\alpha}$-${\beta}$ model** ([[05 Reference/Volume II - Scaling/V2 Communication Foundations#^eq-alpha-beta|equation 1]]) predicts the time to transfer a point-to-point message of ${n}$ bytes:

$$
{T}({n}) = {\alpha}+ \frac{{n}}{{\beta}} \tag{1}
$$

^eq-alpha-beta

Here ${\alpha}$ is the **startup latency** (seconds), the fixed cost of initiating a message including software overhead, network interface card (NIC) processing, and routing setup. ${\beta}$ is the **link bandwidth** (bytes/s), the sustained data rate after startup. ${n}$ is the **message size** (bytes). The model decomposes every transfer into exactly two costs: a per-message cost (${\alpha}$) paid regardless of size, and a per-byte cost (${n}/{\beta}$) that scales linearly with the payload. This decomposition drives all the algorithm selection decisions in [[05 Reference/Volume II - Scaling/V2 Communication Foundations#^sec-appdx-comm-foundations-algorithm-selection|section 1.3]], and the baseline ${\alpha}$ and ${\beta}$ parameters span more than an order of magnitude across intra-node NVLink and PCIe, inter-node InfiniBand and RoCE fabrics, and kernel TCP stacks ([[05 Reference/Volume II - Scaling/V2 Communication Foundations#^tbl-alpha-beta-params|table 1]]).

| **Interconnect**              | **${\alpha}$ (latency)** | **${\beta}$ (bandwidth)** | **Typical role**                 |
|:------------------------------|:------------------------:|:-------------------------:|:---------------------------------|
| **NVLink 4.0 (H100)**         |          1–2 μs          |         450 GB/s          | Intra-node GPU-to-GPU            |
| **PCIe Gen5**                 |          2–5 μs          |          64 GB/s          | CPU-GPU, NIC-GPU                 |
| **InfiniBand NDR (400 Gb/s)** |          1.5 μs          |          50 GB/s          | Inter-node (high-end clusters)   |
| **InfiniBand HDR (200 Gb/s)** |          2–5 μs          |          25 GB/s          | Inter-node (previous generation) |
| **RoCE v2 (100 Gb/s)**        |         5–10 μs          |         12.5 GB/s         | Inter-node (Ethernet clusters)   |
| **TCP/IP (Ethernet)**         |          50 μs           |          Varies           | Control plane, non-RDMA fallback |

Table 1: **${\alpha}$-${\beta}$ Parameters by Interconnect**: Effective startup latency and sustained bandwidth for interconnects used in ML clusters. ${\alpha}$ follows the convention of **[[01 Books/Volume II - Scaling/02 Distributed ML/05 Collective Communication/V2-05.06 Pricing Collectives by Rounds and Chunks#^tbl-interconnect-parameters|Interconnect Performance Parameters]]** in **[[01 Books/Volume II - Scaling/02 Distributed ML/05 Collective Communication/V2-05 Collective Communication#^sec-collective-communication|Collective Communication]]**, the effective per-message launch latency including the communication library’s software stack, which is why it reaches microseconds even on NVLink. The InfiniBand NDR entry is the single anchor that every worked example in this appendix uses, and it lies inside that table’s NDR range. The ${\beta}$ column uses one-way or per-direction bandwidth, so the H100 NVLink entry is half of the 900 GB/s bidirectional aggregate specification. NVLink and PCIe operate within a node; InfiniBand and RoCE operate between nodes. TCP latency is dominated by kernel software stack overhead.

^tbl-alpha-beta-params

### Latency-Dominated Vs. Bandwidth-Dominated Regimes

^sec-appdx-comm-foundations-regimes

Sending a 64-byte control flag over InfiniBand NDR takes nearly the same five microseconds as sending a 64 KB tensor, whereas a 100 MB gradient shard spends almost all of its transfer time streaming bytes at line rate. That contrast separates the ${\alpha}$-${\beta}$ model into two operating regimes: for small messages, the startup latency ${\alpha}$ dominates and the link spends most of its time initiating transfers, whereas for large messages, the bandwidth term ${n}/{\beta}$ dominates and the startup cost becomes negligible. The **crossover message size** ${n^*}$, defined by [[05 Reference/Volume II - Scaling/V2 Communication Foundations#^eq-crossover|equation 2]], is the point where both terms contribute equally:

$$
{n^*} = {\alpha}\times {\beta} \tag{2}
$$

^eq-crossover

Below ${n^*}$, communication is **latency dominated**: sending more small messages wastes time on repeated startups. Above ${n^*}$, communication is **bandwidth dominated**: payload transfer dominates; reducing bytes or increasing effective bandwidth can lower its cost.

**Napkin Math 1.1: Worked example: Crossover on InfiniBand NDR**

**Setup**: InfiniBand NDR has ${\alpha}$ = 1.5 μs and ${\beta}$ = 50 GB/s.

**Question**: At what message size does the bandwidth term equal the latency term?

**Math**:

${n^*} = {\alpha}\times {\beta}=$ 1.5 μs $\times$ 50 GB/s $=$ 75 KB

**Analysis**: Messages smaller than 75 KB are latency dominated on IB NDR. Gradient tensors from a single layer of a large model are typically 10–100 MB, well above this threshold. Control messages, heartbeats, and barrier synchronizations, however, are well below it.

**Systems insight**: This is why NCCL and Gloo batch small gradient tensors into larger “buckets” before launching AllReduce. Sending each tensor individually would pay the 1.5 μs startup cost hundreds of times per iteration instead of a handful.

### The LogGP Model Extension

^sec-appdx-comm-foundations-loggp

The ${\alpha}$-${\beta}$ model assumes a message is a single, atomic transfer. In practice, networks pipeline messages: a sender can inject a new packet before the previous one has been fully received. The **LogGP model** ([[05 Reference/Volume II - Scaling/V2 Communication Foundations#^ref-alexandrov1995|Alexandrov et al. 1995]]) extends LogP with a long-message gap parameter:

- **${g}$ (gap)**: The minimum interval between consecutive message injections at the sender. This models the NIC’s injection rate limit.
- **${o_{\text{send}}}$, ${o_{\text{recv}}}$ (overhead)**: The CPU time consumed by the processor to initiate or complete a message, during which it cannot do useful compute.

For a long message of ${n}$ bytes, LogGP models transfer time by separating network transit from endpoint processor overhead and per-byte injection gaps:

$$
{T_{\text{long}}}({n}) \approx {o_{\text{send}}} + {L_{\text{LogGP}}} + ({n}- 1){G}+ {o_{\text{recv}}}
$$

Here ${L_{\text{LogGP}}}$ is the network latency, ${o_{\text{send}}}$ and ${o_{\text{recv}}}$ are sender and receiver overheads, ${G}$ is the gap per byte for long messages, and ${g}$ controls the minimum interval between consecutive message injections. Informal alpha-beta-style approximations can be useful for ML profiling, but the standard LogGP model keeps these gap parameters distinct from a simple bandwidth term.

In most ML training scenarios, the ${\alpha}$-${\beta}$ model is sufficient because gradient tensors are large enough that pipelining effects are secondary to raw bandwidth. The LogGP model becomes important when analyzing the overhead of many small control messages or when modeling the interaction between communication and computation overlap, situations that arise in fine-grained pipeline parallelism and asynchronous gradient updates. Whereas the ${\alpha}$-${\beta}$ and LogGP equations describe single point-to-point transfers, collective operations in which all GPUs participate compose multiple point-to-point transfers, and their cost formulas derive directly from the model above.

## Collective Operation Complexity

^sec-appdx-comm-foundations-collective-complexity

**Systems Perspective 1.2: Why this matters**

Every distributed training step ends with a collective synchronization. The cost of that collective, rather than the cost of the matrix multiplies, often determines whether scaling from 8 GPUs to 256 is feasible. Understanding the exact complexity of each collective reveals which parallelism strategy (data, tensor, pipeline, expert) will dominate wall time at a given scale.

When ${N}$ GPUs synchronize gradients, reconstruct sharded weights, or route tokens at the end of a computation phase, the collective primitive coordinates a multi-step schedule of point-to-point transfers across every participating rank. Each collective therefore has a characteristic bandwidth term (how many bytes traverse the bottleneck link) and latency term (how many sequential message steps must complete). The formulas below use the **bandwidth-optimal ring algorithm** unless otherwise noted; [[05 Reference/Volume II - Scaling/V2 Communication Foundations#^sec-appdx-comm-foundations-algorithm-selection|section 1.3]] discusses when other algorithms are preferable.

### AllReduce

^sec-appdx-comm-foundations-allreduce

AllReduce is the workhorse of data-parallel training: every GPU starts with a local gradient tensor of size ${M}$ bytes and ends with the globally reduced (summed) result. The ring algorithm decomposes AllReduce into a ReduceScatter phase followed by an AllGather phase. Ring AllReduce time is given by [[05 Reference/Volume II - Scaling/V2 Communication Foundations#^eq-ring-allreduce|equation 3]]:

$$
{T_{\text{ring}}} = 2 \cdot \frac{{N}- 1}{{N}} \cdot \frac{{M}}{{\beta}} + 2({N}- 1) \cdot {\alpha} \tag{3}
$$

^eq-ring-allreduce

The factor $2({N}-1)/{N}$ approaches 2 as ${N}$ grows. Each rank sends that factor times ${M}$ bytes and receives the same amount. With full-duplex links, sending and receiving overlap; ${\beta}$ is the effective bandwidth in one direction, so sent-plus-received bytes must not be divided by that one-direction rate. The latency term grows linearly with ${N}$, which makes the ring algorithm expensive in latency for large GPU counts.

Tree AllReduce trades that linear latency growth for logarithmic depth. [[05 Reference/Volume II - Scaling/V2 Communication Foundations#^eq-tree-allreduce|Equation 4]] charges both the bandwidth and the latency term once per tree level, $2 \log_2 {N}$ times in total:

$$
{T_{\text{tree}}} = 2 \log_2 {N}\cdot \frac{{M}}{{\beta}} + 2 \log_2 {N}\cdot {\alpha} \tag{4}
$$

^eq-tree-allreduce

This unsegmented tree algorithm trades bandwidth efficiency for latency efficiency: the latency term grows as $\log_2 {N}$ instead of ${N}$, but the bandwidth term sends the full message ${M}$ at each tree level instead of ${M}/{N}$ chunks. Comparing the two formulas shows why large payloads favor ring topologies while small control synchronizations favor trees.

**Napkin Math 1.2: Worked example: Ring vs. tree AllReduce**

**Setup**: 256 H100 GPUs connected via InfiniBand NDR (${\alpha}$ = 1.5 μs, ${\beta}$ = 50 GB/s). The gradient tensor is 1 GB (a 500M-parameter model in FP16).

**Question**: How long does AllReduce take with ring vs. tree?

**Ring AllReduce**:

${T_{\text{ring}}} \approx$ 40.6 ms

**Tree AllReduce**:

${T_{\text{tree}}} \approx$ 320 ms

**Analysis**: For this 1 GB message, ring AllReduce takes 40.6 ms, and tree takes 320 ms. The ring is significantly faster because it distributes the bandwidth load across all links. The tree’s logarithmic latency advantage is negligible compared to its bandwidth penalty for large messages.

**Systems insight**: For the large gradient tensors typical of data-parallel training, ring (or ring-based) algorithms dominate. This unsegmented tree model favors small messages. Production tree variants can pipeline or partition messages and must be evaluated with their own cost models.

### AllGather

^sec-appdx-comm-foundations-allgather

AllGather is the complement of ReduceScatter: each GPU starts with a ${M_{\text{coll}}}/{N}$-sized shard and ends with the complete ${M_{\text{coll}}}$-byte tensor. It is the core communication primitive in fully sharded data parallelism (FSDP) for reconstructing parameters before each forward pass, and in tensor parallelism for reassembling split activations. Ring AllGather execution time ([[05 Reference/Volume II - Scaling/V2 Communication Foundations#^eq-allgather|equation 5]]) requires half the transfer volume of AllReduce:

$$
{T_{\text{allgather}}}= \frac{{N}- 1}{{N}} \cdot \frac{{M_{\text{coll}}}}{{\beta}} + ({N}- 1) \cdot {\alpha} \tag{5}
$$

^eq-allgather

For this comparison, the full gathered tensor has the same byte size as each rank’s AllReduce input payload. In this model, AllGather takes half the communication time of AllReduce for that matched tensor size and link parameters: it uses one ring pass instead of two. Local reduction work and implementation overheads can change the measured ratio.

### ReduceScatter

^sec-appdx-comm-foundations-reducescatter

ReduceScatter is the dual of AllGather: each GPU starts with a full ${M_{\text{coll}}}$-byte tensor and ends with a ${M_{\text{coll}}}/{N}$-sized shard that contains the globally reduced values for that shard. It is the gradient synchronization primitive in FSDP and ZeRO, replacing the full AllReduce with a cheaper operation when each GPU only needs its own parameter shard’s gradient. Ring ReduceScatter execution time ([[05 Reference/Volume II - Scaling/V2 Communication Foundations#^eq-reducescatter|equation 6]]) provides the gradient sharding primitive:

$$
{T_{\text{reducescatter}}}= \frac{{N}- 1}{{N}} \cdot \frac{{M_{\text{coll}}}}{{\beta}} + ({N}- 1) \cdot {\alpha} \tag{6}
$$

^eq-reducescatter

The symmetry with [[05 Reference/Volume II - Scaling/V2 Communication Foundations#^eq-allgather|equation 5]] is not a coincidence: ring AllReduce decomposes into one ReduceScatter followed by one AllGather, and the costs add up exactly to [[05 Reference/Volume II - Scaling/V2 Communication Foundations#^eq-ring-allreduce|equation 3]]. Because each phase traverses the ring once, sharded data-parallel schemes that defer the AllGather until the next forward pass cut immediate post-backward communication in half.

### AllToAll

^sec-appdx-comm-foundations-alltoall

AllToAll is the most general collective: each GPU sends a distinct ${M}/{N}$-sized chunk to every other GPU, and receives a distinct chunk from each. It is the routing primitive for mixture-of-experts (MoE) architectures, where tokens must be dispatched to the correct expert and the results gathered back. Pairwise-exchange AllToAll execution time ([[05 Reference/Volume II - Scaling/V2 Communication Foundations#^eq-alltoall|equation 7]]) trades personalized data chunks across peers:

$$
{T_{\text{alltoall}}}= \frac{{N}- 1}{{N}} \cdot \frac{{M}}{{\beta}} + ({N}- 1) \cdot {\alpha} \tag{7}
$$

^eq-alltoall

Although the formula matches AllGather and ReduceScatter in form, the communication pattern is structurally different. AllToAll is a personalized exchange in which each GPU sends different data to each peer, which makes it harder to overlap with computation and much more sensitive to network bisection congestion.

### Broadcast

^sec-appdx-comm-foundations-broadcast

Broadcast sends a single ${M}$-byte tensor from one root GPU to all ${N}- 1$ others. It is used for distributing initial model weights, updated learning rates, and configuration changes during training. Tree Broadcast execution time ([[05 Reference/Volume II - Scaling/V2 Communication Foundations#^eq-broadcast|equation 8]]) scales logarithmically with the participating GPU count:

$$
{T_{\text{broadcast}}}= \log_2 {N}\left({\alpha}+ \frac{{M}}{{\beta}}\right) \tag{8}
$$

^eq-broadcast

Broadcast is structurally asymmetric (one sender, many receivers), which makes a tree topology natural. In an unsegmented tree broadcast, the full ${M}$-byte payload is forwarded at each tree level, so both the latency and bandwidth terms appear along the $\log_2 {N}$-level critical path. Segmented or scatter-allgather broadcast variants can reduce the bandwidth term, but they require a different algorithm-specific model.

### Collective Complexity Summary

^collective-complexity-summary

With the individual formulas in place, [[05 Reference/Volume II - Scaling/V2 Communication Foundations#^tbl-collective-summary|table 2]] provides a compact reference for comparing the cost structure of each collective operation. Checking the bandwidth and latency columns side by side shows how each collective scales as either payload size or device count grows.

| **Operation**            |                     **Bandwidth term**                      |      **Latency term**       |       **Primary use case**       |
|:-------------------------|:-----------------------------------------------------------:|:---------------------------:|:--------------------------------:|
| **AllReduce (Ring)**     |    $2 \cdot \frac{{N}-1}{{N}} \cdot \frac{{M}}{{\beta}}$    |  $2({N}-1) \cdot {\alpha}$  |   Data-parallel gradient sync    |
| **AllReduce (Tree)**     |           $2\log_2 {N}\cdot \frac{{M}}{{\beta}}$            | $2\log_2 {N}\cdot {\alpha}$ |        Small-message sync        |
| **AllGather (Ring)**     | $\frac{{N}-1}{{N}} \cdot \frac{{M_{\text{coll}}}}{{\beta}}$ |  $({N}-1) \cdot {\alpha}$   |  FSDP parameter reconstruction   |
| **ReduceScatter (Ring)** | $\frac{{N}-1}{{N}} \cdot \frac{{M_{\text{coll}}}}{{\beta}}$ |  $({N}-1) \cdot {\alpha}$   |   FSDP/ZeRO gradient sharding    |
| **AllToAll (Pairwise)**  |        $\frac{{N}-1}{{N}} \cdot \frac{{M}}{{\beta}}$        |  $({N}-1) \cdot {\alpha}$   |        MoE expert routing        |
| **Broadcast (Tree)**     |            $\log_2 {N}\cdot \frac{{M}}{{\beta}}$            | $\log_2 {N}\cdot {\alpha}$  | Weight distribution, config sync |

Table 2: **Collective Operation Cost Summary**: Bandwidth and latency terms for ring, tree, and pairwise-exchange algorithms. The bandwidth term determines cost for large messages (gradients, parameters); the latency term determines cost for small messages (scalars, barriers). ${N}$ = GPU count, ${M}$ = per-rank input payload in bytes, and ${M_{\text{coll}}}$ = full tensor size in bytes for AllGather and ReduceScatter.

^tbl-collective-summary

Two patterns emerge from this table. First, the ring and pairwise-exchange models contain the $({N}-1)/{N}$ factor, which approaches 1 for large ${N}$. Per-rank communication therefore approaches a constant multiple of the relevant size: about $2{M}$ for ring AllReduce, about ${M_{\text{coll}}}$ for ring AllGather or ReduceScatter, and about ${M}$ for pairwise AllToAll. Aggregate traffic still scales with the number of ranks. Second, the latency term grows linearly with ${N}$ for ring algorithms but logarithmically for tree algorithms, creating the algorithm selection trade-off analyzed next.

## Algorithm Selection

^sec-appdx-comm-foundations-algorithm-selection

**Systems Perspective 1.3: Why this matters**

NCCL automatically selects a collective algorithm based on message size and GPU topology, but understanding why it chooses ring for large messages and tree for small ones helps diagnose when the auto-selection is suboptimal and how to structure communication to stay in the efficient regime.

### Ring Vs. Tree Vs. Recursive Halving-Doubling

^sec-appdx-comm-foundations-ring-vs-tree

Sending a 1 GB gradient tensor across 256 GPUs favors an algorithm that spreads bytes across every link, whereas synchronizing a 4-byte scalar loss flag favors an algorithm that finishes in the fewest hop steps. The ring algorithm minimizes bandwidth usage but pays a latency cost that grows linearly with ${N}$. The tree algorithm minimizes latency but wastes bandwidth because it sends the full message at each level. Recursive halving-doubling splits the difference: it uses halving (like a tree) for the reduce phase and doubling for the gather phase, achieving near-optimal bandwidth with $\mathcal{O}(\log {N})$ latency steps.

The decision boundary between ring and tree depends on both message size and participant count. For the power-of-two case modeled by [[05 Reference/Volume II - Scaling/V2 Communication Foundations#^eq-ring-allreduce|equation 3]] and [[05 Reference/Volume II - Scaling/V2 Communication Foundations#^eq-tree-allreduce|equation 4]], equating the two times gives the crossover in [[05 Reference/Volume II - Scaling/V2 Communication Foundations#^eq-ring-tree-crossover|equation 9]], which [[05 Reference/Volume II - Scaling/V2 Communication Foundations#^tbl-algorithm-selection|table 3]] translates into practical selection rules across payload regimes:

$$
{M_{\text{crossover}}}({N}) = {n^*} \times \frac{({N}-1)-\log_2 {N}}{\log_2 {N}-({N}-1)/{N}}, \qquad {n^*}={\alpha}{\beta} \tag{9}
$$

^eq-ring-tree-crossover

- **${M}> {M_{\text{crossover}}}({N})$** (large gradients): The ring has the lower modeled cost because its smaller bandwidth coefficient outweighs its additional startup steps.
- **${M}< {M_{\text{crossover}}}({N})$** (barriers, scalars): The tree has the lower modeled cost because its logarithmic startup term outweighs its additional bandwidth cost.
- **${M}\approx {M_{\text{crossover}}}({N})$** (medium tensors): The two modeled costs are similar, so benchmark them alongside recursive halving-doubling on the target topology.

| **Regime**                                   |               **Ring**                |                 **Tree**                 | **Recursive halving-doubling**                              |
|:---------------------------------------------|:-------------------------------------:|:----------------------------------------:|:------------------------------------------------------------|
| **${M}> {M_{\text{crossover}}}({N})$**       | Lower cost under the displayed models |          Higher bandwidth term           | Candidate with near-optimal bandwidth and logarithmic steps |
| **${M}< {M_{\text{crossover}}}({N})$**       |      Higher linear startup term       |  Lower cost under the displayed models   | Candidate with logarithmic startup steps                    |
| **${M}\approx {M_{\text{crossover}}}({N})$** |   Benchmark on the target topology    |     Benchmark on the target topology     | Benchmark on the target topology                            |
| **Power-of-2 ${N}$**                         |          Works for any ${N}$          | Matches the displayed $\log_2 {N}$ model | Requires ${N}= 2^{m}$                                       |

Table 3: **Algorithm Selection Guide**: Strengths and weaknesses of ring, tree, and recursive halving-doubling relative to the participant-dependent ring-tree crossover ${M_{\text{crossover}}}({N})$ in [[05 Reference/Volume II - Scaling/V2 Communication Foundations#^eq-ring-tree-crossover|equation 9]].

^tbl-algorithm-selection

### Hierarchical AllReduce

^sec-appdx-comm-foundations-hierarchical

Modern clusters have a two-level topology: GPUs within a node are connected by NVLink (450 GB/s), while nodes are connected by InfiniBand (50 GB/s). Hierarchical AllReduce exploits this asymmetry in three phases:

1.  **Intra-node reduce** (NVLink): Each node reduces its 8 local GPUs to a single result using NVLink’s 450 GB/s bandwidth. This is fast because NVLink’s per-direction rate is 9× that of an InfiniBand NDR port.
2.  **Inter-node AllReduce** (InfiniBand): An AllReduce combines the per-node results across nodes. Only one representative per 8 local GPUs participates, so the inter-node ring has one-eighth as many participants as a flat GPU-level ring.
3.  **Intra-node broadcast** (NVLink): Each node broadcasts the global result to its 8 local GPUs.

The hierarchical approach reduces the inter-node ring size from all GPUs to one representative per 8 local GPUs, cutting the latency-step term by about 8$\times$ while keeping local aggregation on fast intra-node links. The inter-node representative still exchanges the full reduced tensor; the gain is not a universal reduction of payload bytes by the number of local GPUs. NCCL selects among topology-aware algorithms such as Ring, Tree, CollNet variants, NVLS/NVLSTree, and PAT based on the collective, message size, topology, architecture, and version. Hierarchical communication is common on multi-node systems but is not a universal default. The cost structure of collectives lets an engineer reason about data-parallel overhead. Pipeline parallelism, in contrast, introduces a different kind of overhead, idle time caused by the sequential dependency between pipeline stages.

## Pipeline Arithmetic

^sec-appdx-comm-foundations-pipeline-arithmetic

**Systems Perspective 1.4: Why this matters**

Pipeline parallelism splits a model across multiple GPUs so that each GPU holds only a fraction of the layers. The trade-off is **bubble time**: idle cycles where GPUs wait for activations or gradients from upstream or downstream stages. Quantifying the bubble fraction reveals whether pipeline parallelism is worth the complexity at a given scale.

### Bubble Fraction

^sec-appdx-comm-foundations-bubble-fraction

When a model is split across eight pipeline stages, Stage 8 sits idle while Stages 1 through 7 compute the first microbatch’s forward pass, and Stage 1 sits idle again while the pipeline drains at the end of the step. In a pipeline with ${N_{\text{PP}}}$ stages and ${m}$ microbatches, [[05 Reference/Volume II - Scaling/V2 Communication Foundations#^eq-pipeline-bubble|equation 10]] defines the **bubble fraction** as the proportion of total GPU-time spent idle:

$$
{b_{\text{pipe}}} = \frac{{N_{\text{PP}}} - 1}{{N_{\text{PP}}} - 1 + {m}} \tag{10}
$$

^eq-pipeline-bubble

For balanced stages with negligible transfer overhead, this formula applies to both GPipe (where all forward passes complete before any backward pass begins) and 1F1B (one-forward-one-backward interleaving). The 1F1B schedule has the same asymptotic bubble fraction but uses less peak memory because it retires microbatches earlier.

The bubble fraction depends on the ratio of stages to microbatches, so adding more microbatches for a fixed number of stages amortizes the pipeline fill and drain across more useful work. As a rule of thumb, keeping bubble overhead at or below 20 percent requires ${m}\geq 4({N_{\text{PP}}} - 1)$, while staying strictly below 20 percent requires ${m}> 4({N_{\text{PP}}} - 1)$. The practical rule ${m}\geq 4{N_{\text{PP}}}$ is a convenient conservative target across typical stage depths and microbatch counts ([[05 Reference/Volume II - Scaling/V2 Communication Foundations#^tbl-pipeline-bubble|table 4]]).

| **Pipeline stages (${N_{\text{PP}}}$)** | **${m}$ = 8** | **${m}$ = 16** | **${m}$ = 32** | **${m}$ = 64** |
|:----------------------------------------|:-------------:|:--------------:|:--------------:|:--------------:|
| **${N_{\text{PP}}}$ = 4**               |     27.3%     |     15.8%      |      8.6%      |      4.5%      |
| **${N_{\text{PP}}}$ = 8**               |     46.7%     |     30.4%      |     17.9%      |      9.9%      |

Table 4: **Pipeline Bubble Fraction**: Percentage of GPU-time lost to pipeline bubbles for various stage counts and microbatch counts. The conservative choice ${m}\geq 4{N_{\text{PP}}}$ keeps the modeled fraction below 20 percent.

^tbl-pipeline-bubble

Deeper pipelines require proportionally more microbatches to maintain high accelerator utilization. When activation memory bounds limit the microbatch count, systems must adopt alternative scheduling strategies to mitigate bubble overhead.

### Interleaved Scheduling

^sec-appdx-comm-foundations-interleaved

When activation memory prevents a team from increasing ${m}$, splitting each GPU’s layer assignment into smaller nonconsecutive model chunks lets the first microbatch reach the last device after fewer layers per stage. **Interleaved scheduling** (used in Megatron-LM) assigns ${V}$ virtual stages to each physical GPU instead of one, so the pipeline has ${N_{\text{PP}}} \times {V}$ virtual stages while the bubble numerator retains the physical stage count ${N_{\text{PP}}}$, as [[05 Reference/Volume II - Scaling/V2 Communication Foundations#^eq-interleaved-bubble|equation 11]] shows:

$$
{b_{\text{interleaved}}}= \frac{{N_{\text{PP}}} - 1}{{N_{\text{PP}}} - 1 + {m}\times {V}} \tag{11}
$$

^eq-interleaved-bubble

The microbatch term in the denominator is multiplied by ${V}$ compared to [[05 Reference/Volume II - Scaling/V2 Communication Foundations#^eq-pipeline-bubble|equation 10]], so the bubble reduction approaches ${V}$ when ${m}$ dominates ${N_{\text{PP}}} - 1$. For ${N_{\text{PP}}}$ = 8, ${m}$ = 16, and ${V}$ = 4, the bubble fraction drops from 30.4 percent to 9.9 percent, a 3.1× reduction that comes at the cost of more frequent, smaller communication between stages.

Interleaved scheduling highlights a recurring theme in distributed ML: communication granularity is a tunable knob. Smaller, more frequent transfers improve overlap and reduce idle time, but increase the aggregate latency overhead. The same trade-off governs gradient compression.

## Compression Economics

^sec-appdx-comm-foundations-compression

**Systems Perspective 1.5: Why this matters**

Gradient compression promises to reduce communication volume by 10–1000$\times$, making AllReduce nearly free. Compression, however, has overhead (encoding and decoding time), and it only helps if that overhead is smaller than the communication time it saves. A quick break-even analysis prevents wasted effort on compression schemes that will not actually speed up training.

### The Compression Equation

^sec-appdx-comm-foundations-compression-equation

Compressing a 1 GB gradient tensor down to 16 MB cuts network transfer time on a 256-GPU ring from 40 ms to less than 2 ms, but only if the GPU kernels that quantize or sparsify the tensor finish in less than the 38 ms saved. Gradient compression replaces the original ${M}$-byte gradient with a compressed representation of size ${M}/{r_{\text{comp}}}$, where ${r_{\text{comp}}}$ is the compression ratio. [[05 Reference/Volume II - Scaling/V2 Communication Foundations#^eq-compression-total|Equation 12]] expresses the total time with compression:

$$
{T_{\text{compressed}}} = {T_{\text{encode}}} + {T_{\text{transfer}}}\!\left(\frac{{M}}{{r_{\text{comp}}}}\right) + {T_{\text{decode}}} \tag{12}
$$

^eq-compression-total

Compression is beneficial when ${T_{\text{compressed}}} < {T_{\text{transfer}}}({M})$ and the reduced precision or sparsity does not slow model convergence. Rearranging this inequality yields the break-even condition in [[05 Reference/Volume II - Scaling/V2 Communication Foundations#^eq-compression-breakeven|equation 13]]:

$$
{T_{\text{encode}}} + {T_{\text{decode}}} < {T_{\text{transfer}}}({M}) - {T_{\text{transfer}}}\!\left(\frac{{M}}{{r_{\text{comp}}}}\right) \tag{13}
$$

^eq-compression-breakeven

In the bandwidth-dominated regime (${M}\gg {n^*}$), the communication time scales linearly with message size, and the right-hand side simplifies to approximately ${T_{\text{transfer}}}({M}) \times (1 - 1/{r_{\text{comp}}})$. For high compression ratios (${r_{\text{comp}}} \gg 1$), this approaches ${T_{\text{transfer}}}({M})$, so compression is worthwhile as long as the codec overhead is less than the uncompressed communication time.

**Napkin Math 1.3: Worked example: Is compression worth it?**

**Setup**: Ring AllReduce of a 1 GB gradient across 256 H100 GPUs on InfiniBand NDR, taking 40.6 ms uncompressed. Assume a collective-compatible compressed representation achieves 64× compression with 2 ms total encode + decode overhead.

**Question**: Does compression reduce the total AllReduce time?

**Math**:

- Uncompressed AllReduce: 40.6 ms
- Compressed communication: 1.4 ms
- Total with compression: 3.4 ms
- Speedup: 12×

**Result**: Compression shortens communication time by 12×. The 2 ms codec overhead is a small fraction of the 40.6 ms uncompressed baseline.

**Systems insight**: Compression saves communication time under the assumed payload ratio, codec cost, and unchanged collective structure. Independent top-k selections do not generally preserve that structure: sparse indices, differing supports, and merge operations must also be modeled. Lossy compression can require more iterations to reach the same accuracy, negating a per-iteration gain.

Break-even codec overhead limits ([[05 Reference/Volume II - Scaling/V2 Communication Foundations#^tbl-compression-breakeven|table 5]]) scale with compression ratio and uncompressed AllReduce time. Higher compression ratios tolerate larger codec overheads, up to the bandwidth-dependent portion of the uncompressed collective. These break-even limits show that gradient compression delivers the highest net benefit on lower-bandwidth interconnects where transfer times dominate. On high-speed fabrics, the tolerable codec overhead budget is tightly constrained and requires lightweight quantization or sparsification algorithms.

| **Compression ratio (${r_{\text{comp}}}$)** | **AllReduce = 10 ms (max codec overhead)** | **AllReduce = 40 ms (max codec overhead)** | **AllReduce = 100 ms (max codec overhead)** |
|:--------------------------------------------|:------------------------------------------:|:------------------------------------------:|:-------------------------------------------:|
| **4$\times$**                               |                    6.9                     |                    29.4                    |                    74.4                     |
| **16$\times$**                              |                    8.7                     |                    36.8                    |                    93.0                     |
| **64$\times$**                              |                    9.1                     |                    38.6                    |                    97.7                     |
| **256$\times$**                             |                    9.2                     |                    39.1                    |                    98.8                     |

Table 5: **Compression Break-Even Thresholds**: Maximum tolerable codec overhead (encode + decode) for compression to reduce total time, computed as the actual collective-time difference ${T_{\text{transfer}}}({M})-{T_{\text{transfer}}}({M}/{r_{\text{comp}}})$. The shared startup latency cancels, so even at high compression ratios it is not part of the codec budget.

^tbl-compression-breakeven

## Summary

^summary

The communication models in this appendix rest on two hardware parameters, the startup latency ${\alpha}$ and the bandwidth ${\beta}$ of the ${\alpha}$-${\beta}$ model (principle [[01 Books/Volume II - Scaling/01 The Fleet/V2 Fleet Principles#^pri-alpha-beta-model|5]]). They also rest on two workload parameters, the payload (${n}$ or ${M}$) and, for collectives, the participant count ${N}$. The crossover size ${n^*} = {\alpha}{\beta}$ separates latency-dominated from bandwidth-dominated transfers. Ring collectives carry a $({N}-1)/{N}$ bandwidth factor and a latency term linear in ${N}$, while tree algorithms trade bandwidth for logarithmic latency, so message size relative to the crossover ${M_{\text{crossover}}}({N})$ selects the algorithm. Pipeline parallelism adds the bubble fraction ${b_{\text{pipe}}} = ({N_{\text{PP}}}-1)/({N_{\text{PP}}}-1+{m})$, which the rule ${m}\geq 4{N_{\text{PP}}}$ keeps below 20 percent. Gradient compression pays only when codec overhead is smaller than the communication time it saves and convergence is unaffected. Measuring ${\alpha}$ and ${\beta}$ for a cluster therefore yields a first-order prediction of its communication overhead.

Back to top

## Source References

^source-references

Alexandrov, Albert D., Mihai F. Ionescu, Klaus E. Schauser, and Chris J. Scheiman. 1995. “LogGP: Incorporating Long Messages into the LogP Model—One Step Closer Towards a Realistic Model for Parallel Computation.” *Proceedings of the Seventh Annual ACM Symposium on Parallel Algorithms and Architectures - SPAA ’95* 30: 95–105. https://doi.org/10.1145/215399.215427.

^ref-alexandrov1995

## Source

[Repository Source](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/books/vol2/backmatter/appendix_communication.qmd) · [Original License](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/LICENSE.md)

[Rendered Reading Snapshot](https://mlsysbook.ai/vol2/backmatter/appendix_communication.html#sec-appdx-communication-foundations). Rendering provenance is recorded in the import manifest.
