---
title: V2 Single-Machine Foundations
type: Reference
volume: 2
chapter: 0
publication_status: Preview
source_repository: https://github.com/klappe-pm/cs249r_book
source_commit: de87c0103806d7bfb1c677dbb77a2b92fa00c298
source_path: books/vol2/backmatter/appendix_dam.qmd
source_anchor: sec-appdx-dam-taxonomy
source_mode: Source-Correlated Published HTML
tags:
- Type/Reference
- Book/Volume_2
rendered_source_url: https://mlsysbook.ai/vol2/backmatter/appendix_dam.html
---

# V2 Single-Machine Foundations

[[Home|Home]] · [[01 Books/Volume II - Scaling/Volume 2 Overview|Volume Overview]]

^sec-appdx-dam-taxonomy

Every fleet is built from single machines, and this book assumes that the reader already reasons fluently about one of them. This appendix restates that single-machine foundation in reference form so that a reader who meets the prerequisites only loosely can work every calculation in the book without another text. It collects the Data, Algorithm, and Machine (D·A·M) diagnostic framework and the iron law it rests on, arithmetic intensity and the roofline bound, the accelerator memory hierarchy, the kernel-level levers that shorten a single device’s step, the byte accounting of mixed-precision training, and the arithmetic of transformer training and inference. The chapters build the fleet-scale Compute, Communication, and Coordination (C$^3$) framework on this base.

**Learning Objectives**

- Classify single-machine bottlenecks by dominant Data, Algorithm, or Machine axis while recognizing mixed causes
- Map optimization techniques to their D·A·M intersection zone to understand which axes they span
- Apply the iron law equation to quantitatively diagnose performance problems
- Distinguish between memory-bound and compute-bound workloads using arithmetic intensity and the roofline bound
- Calculate the per-parameter memory of mixed-precision training and the FLOPs of transformer training and decoding
- Select appropriate profiling tools and optimization strategies for each Data, Algorithm, or Machine axis
- Evaluate system health using D·A·M scorecard metrics (I/O overhead, active parameters, MFU)

^callout-learning-objectives--1-1-28bd1d0b

## How to Use This Appendix

^how-to-use-this-appendix

This appendix is a reference for single-node performance and for the single-machine quantities that fleet-scale arguments take as given. Start from the symptom or the missing quantity:

- **When a single accelerator is slow**: Use the iron law mapping ([[05 Reference/Volume II - Scaling/V2 Single-Machine Foundations#^sec-appdx-dam-taxonomy-iron-law-mapping|section 1.2]]) and the bottleneck diagnostic ([[05 Reference/Volume II - Scaling/V2 Single-Machine Foundations#^sec-appdx-dam-taxonomy-bottleneck-diagnostic|section 1.3.2]]) to decide which term binds.
- **When deciding whether a kernel is memory bound or compute bound**: Use the roofline bound ([[05 Reference/Volume II - Scaling/V2 Single-Machine Foundations#^sec-appdx-dam-taxonomy-roofline|section 1.3.1]]).
- **When a byte must cross a memory boundary**: Use the memory hierarchy ([[05 Reference/Volume II - Scaling/V2 Single-Machine Foundations#^sec-appdx-dam-taxonomy-memory-hierarchy|section 1.4]]) to see which tier sets its cost.
- **When a trace shows many short kernels, launch gaps, or attention intermediates written to device memory**: Use the kernel-level levers ([[05 Reference/Volume II - Scaling/V2 Single-Machine Foundations#^sec-appdx-dam-taxonomy-kernel-levers|section 1.5]]).
- **When sizing model state**: Use the training memory accounting ([[05 Reference/Volume II - Scaling/V2 Single-Machine Foundations#^sec-appdx-dam-taxonomy-training-memory|section 1.6]]) for bytes per parameter.
- **When estimating training compute or decode cost**: Use transformer arithmetic ([[05 Reference/Volume II - Scaling/V2 Single-Machine Foundations#^sec-appdx-dam-taxonomy-transformer-arithmetic|section 1.7]]).

When training is slow on a single GPU, check utilization, data wait time, and model FLOPs utilization (MFU), then map each to its Data, Algorithm, or Machine axis. When serving misses a latency target, identify whether the regime is latency-bound (overhead), memory-bound (weight/KV movement), or compute-bound. When cost is exploding, use the D·A·M rubric to ensure that effort targets the dominant term, not a nonbottleneck.

The Data · Algorithm · Machine (D·A·M) taxonomy is the diagnostic framework for single-node ML systems engineering: it formalizes how information flow, mathematical logic, and physical execution interact across three diagnostic axes,[[05 Reference/Volume II - Scaling/V2 Single-Machine Foundations#^fn1|¹]] while recognizing that real systems can involve mixed causes or interactions between axes.

## Diagnostic Summary

^sec-appdx-dam-taxonomy-diagnostic-summary

When performance stalls or behavior degrades on a single node, the first diagnostic question is whether the flow of work is blocked by memory movement, arithmetic volume, or hardware throughput. The D·A·M taxonomy maps these three failure modes directly to the iron law of ML systems, the single-machine equation that **[[01 Books/Volume II - Scaling/00 Introduction/01 Introduction/V2-01.06 The C³ Taxonomy and Foundations of Scale#^sec-vol2-introduction-fleet-law|The Fleet Law]]** restates before extending it to the Fleet Law. Each axis plays a distinct role, binds on a distinct physical quantity (bandwidth, operations, or peak throughput), and answers to its own high-leverage optimization ([[05 Reference/Volume II - Scaling/V2 Single-Machine Foundations#^tbl-v2-dam-components-ref|table 1]]).

| **Axis**          |          **Role**          |     **Physical constraint**      | **High-leverage optimization** |
|:------------------|:--------------------------:|:--------------------------------:|:------------------------------:|
| **Data (D)**      | **Information** (The Fuel) |    Bandwidth (${\text{BW}}$)     |   I/O Pipeline Optimization    |
| **Algorithm (A)** | **Logic** (The Blueprint)  |        Operations (${O}$)        |       Model Compression        |
| **Machine (M)**   |  **Physics** (The Engine)  | Throughput (${R_{\text{peak}}}$) |     Hardware Acceleration      |

Table 1: **D·A·M Axis Reference**: Each axis maps to a distinct physical constraint and a high-impact optimization strategy. Start diagnosis here: identify which constraint is binding, then follow the optimization lever.

^tbl-v2-dam-components-ref

The three axes seldom bind in isolation. Pruning weights to cut operations can fragment memory access, and a denser storage format that saves bytes can saturate the host CPUs that must decode it before the accelerator sees any data. Because an intervention on one axis shifts pressure onto the other two, diagnosis has to account for the regions where axes overlap. [[05 Reference/Volume II - Scaling/V2 Single-Machine Foundations#^fig-appdx-dam-taxonomy|Figure 1]] draws the three axes as overlapping sets. Each circle carries the factor its axis contributes to [[05 Reference/Volume II - Scaling/V2 Single-Machine Foundations#^eq-appdx-dam-iron-law-product|equation 1]], and each pairwise overlap names the question its two axes must answer together. Data and Algorithm decide what the model learns from, Data and Machine decide how information moves, and Algorithm and Machine decide how computation executes efficiently. A bottleneck that sits in an overlap needs a fix that respects both of its axes, and the center, where all three meet, is the domain of ML systems engineering.

![[90 Assets/Volume II/Shared Figures/Dam Taxonomy 19c61af01a.svg]]

Figure 1: **The D·A·M Intersection Landscape**: Each circle is one diagnostic axis (Data, information; Algorithm, logic; Machine, physics), labeled with the factor it contributes to execution time in [[05 Reference/Volume II - Scaling/V2 Single-Machine Foundations#^eq-appdx-dam-iron-law-product|equation 1]]. Each pairwise overlap names the question its two axes must answer jointly (what to learn from, how to move information, and how to execute efficiently). At the center, where all three meet, is ML systems engineering.

^fig-appdx-dam-taxonomy

## Iron Law Mapping

^sec-appdx-dam-taxonomy-iron-law-mapping

When a training step or serving request runs slower than expected on a single GPU, the first question is whether the time went to moving bytes, executing arithmetic, or waiting on dispatch overhead. The iron law answers that question in two steps. The first step factors execution time along the three D·A·M axes. A task processes some number of samples (examples in vision or tabular workloads, tokens in language models), each sample costs some number of operations, and the machine takes some time to complete each operation. By dimensional cancellation, total execution time ${T}$ (seconds) is the product of these three factors ([[05 Reference/Volume II - Scaling/V2 Single-Machine Foundations#^eq-appdx-dam-iron-law-product|equation 1]]):

$$
{T} = \underbrace{\left(\frac{\text{Samples}}{\text{Task}}\right)}_{\text{Data (D)}} \times \underbrace{\left(\frac{\text{FLOPs}}{\text{Sample}}\right)}_{\text{Algorithm (A)}} \times \underbrace{\left(\frac{\text{Seconds}}{\text{FLOP}}\right)}_{\text{Machine (M)}} \tag{1}
$$

^eq-appdx-dam-iron-law-product

The first two factors fix the total arithmetic work ${O}$. Training a model with ${P}$ parameters on ${D}$ tokens costs roughly $6{P}{D}$ operations across the forward and backward passes ([[05 Reference/Volume II - Scaling/V2 Single-Machine Foundations#^eq-appdx-dam-training-flops|equation 4]]), and inference costs roughly $2{P}$ operations per token in the forward pass. The third factor is the realized time per operation, and no real machine achieves its datasheet value of $1/{R_{\text{peak}}}$.

The second step explains the gap. Executing an operation requires moving its operands through memory and interconnect, driving the arithmetic units at some realized utilization, and paying fixed control costs. Assuming these three costs occur in sequence, the iron law unpacks execution time into their sum ([[05 Reference/Volume II - Scaling/V2 Single-Machine Foundations#^eq-appdx-dam-iron-law-sum|equation 2]]):

$$
{T}= \underbrace{ \frac{{D_{\text{vol}}}}{{\text{BW}}} }_{\text{Memory time}} + \underbrace{ \frac{{O}}{{R_{\text{peak}}} \cdot {\eta_{\text{hw}}}} }_{\text{Compute time}} + \underbrace{ {L_{\text{lat}}} }_{\text{Overhead}} \tag{2}
$$

^eq-appdx-dam-iron-law-sum

Data enters the two equations in different units. In [[05 Reference/Volume II - Scaling/V2 Single-Machine Foundations#^eq-appdx-dam-iron-law-product|equation 1]], the Data factor counts logical samples or tokens. In [[05 Reference/Volume II - Scaling/V2 Single-Machine Foundations#^eq-appdx-dam-iron-law-sum|equation 2]], ${D_{\text{vol}}}$ counts the physical bytes that cross a memory or interconnect bus, which include model weights, activations, cached sequence state, and gradients as well as the inputs themselves. Batch-1 decode of a language model shows how far apart the two can be. The task processes a single token, yet ${D_{\text{vol}}}$ spans the gigabytes of weights streamed from high-bandwidth memory to produce it.

Algorithm and Machine share the compute term and are separated by which variable the engineer controls. Reducing the total operations (${O}$) is an algorithm lever, while improving the hardware’s peak throughput (${R_{\text{peak}}}$) or utilization (${\eta_{\text{hw}}}$) is a machine lever. The memory term belongs to no single axis. The Data axis sets how many inputs move, the Algorithm axis sets how many weights and activations move with them, and the Machine axis supplies the bandwidth ${\text{BW}}$ that carries them.

### D·A·M Coordination from Sum to Max

^sec-appdx-dam-taxonomy-dam-coordination-sum-max

The additive iron law represents **sequential execution**, the worst case where Data, Algorithm, and Machine take turns. Overlap can move the sum toward a max, with perfect overlap defining the ideal lower bound:

$$
{T_{\text{sequential}}}= \frac{{D_{\text{vol}}}}{{\text{BW}}} + \frac{{O}}{{R_{\text{peak}}} \cdot {\eta_{\text{hw}}}} + {L_{\text{lat}}} \quad \xrightarrow{\text{overlap}} \quad {T_{\text{pipelined}}}\geq \max\left(\frac{{D_{\text{vol}}}}{{\text{BW}}},\; \frac{{O}}{{R_{\text{peak}}} \cdot {\eta_{\text{hw}}}}\right) + {L_{\text{lat}}}
$$

The systems engineer’s job is to make these components run in parallel, not in series. Prefetching, separate CUDA streams, asynchronous gradient synchronization, and double buffering each let one axis proceed while another is in flight ([[05 Reference/Volume II - Scaling/V2 Single-Machine Foundations#^tbl-v2-dam-overlap|table 2]]).

| **Technique**           |  **D·A·M axes overlapped**   | **Implementation**                                                                              |
|:------------------------|:----------------------------:|:------------------------------------------------------------------------------------------------|
| **Prefetching**         |         D overlaps M         | DataLoader with `prefetch_factor`, `pin_memory=True`                                            |
| **CUDA Streams**        |         D overlaps M         | Separate streams for H2D transfer and compute                                                   |
| **Async Gradient Sync** | M (communication) overlaps A | Overlap gradient AllReduce with remaining backward computation as gradient buckets become ready |
| **Double Buffering**    |         D overlaps M         | Fill buffer ${i}+1$ while computing on buffer ${i}$                                             |

Table 2: **D·A·M Overlap Techniques**: Each technique allows one D·A·M axis to execute while another is in flight, converting the iron law’s additive terms into overlapped terms.

^tbl-v2-dam-overlap

## Arithmetic Intensity Boundary

^sec-appdx-dam-taxonomy-arithmetic-intensity-boundary

This overlap view still leaves one practical question: whether a workload is waiting on bytes or on FLOPs. The boundary between Data (memory bound) and Machine (compute bound) is not arbitrary; it is defined mathematically by the arithmetic intensity[[05 Reference/Volume II - Scaling/V2 Single-Machine Foundations#^fn2|²]] (${I}$) of the workload.

The symptoms below are screening signals, not diagnoses. A workload whose arithmetic intensity sits left of ${R_{\text{peak}}}/{\text{BW}}$ cannot keep the accelerator fed with enough useful work per byte. Raw utilization must still be read alongside memory-bandwidth utilization, data-loader wait, kernel occupancy, and trace gaps.

- **Low GPU utilization** ($<$ 80 percent): Screen for data, CPU, or launch starvation. Confirm with data-loader wait, host CPU saturation, memory-bandwidth counters, and timeline gaps.
- **High GPU utilization** ($>$ 95 percent): Treat this as machine bound only if compute units are busy and memory bandwidth is not saturated. If memory bandwidth is saturated, the bottleneck is still on the Data/Machine boundary.
- **If batch size is 1**: Treat this as a warning that latency or launch overhead may matter. For large language model (LLM) decode, batch-1 execution is often memory-bandwidth bound unless traces show dispatch gaps.
- **If arithmetic intensity is below the ridge point** (about 295.2 FLOP/byte on H100): The workload is likely memory bound (Data/Machine boundary).

### The Roofline Bound

^sec-appdx-dam-taxonomy-roofline

Arithmetic intensity is a property of the workload and its implementation, not of the hardware. A large matrix multiply reuses each weight it loads across many multiply-accumulates and so has high intensity. An element-wise operation, or the generation of a single token, uses each loaded value only once or twice. The ridge point belongs to a simple upper bound on single-device throughput, the Roofline Model ([[05 Reference/Volume II - Scaling/V2 Single-Machine Foundations#^ref-williams2009|Williams et al. 2009]]). A kernel with arithmetic intensity ${I}$, running on a device with peak compute rate ${R_{\text{peak}}}$ and memory bandwidth ${\text{BW}}$, can attain at most

$$
{R_{\text{attain}}}({I}) = \min\!\left({R_{\text{peak}}},\; {I}\times {\text{BW}}\right) \tag{3}
$$

^eq-appdx-dam-roofline

On log-log axes, the bound is a bandwidth roof of slope one (${I}\times {\text{BW}}$) that meets a flat compute roof (${R_{\text{peak}}}$) at the ridge point ${I_{\text{ridge}}} = {R_{\text{peak}}}/{\text{BW}}$. Left of the ridge, a kernel is memory bound, and only more bandwidth or fewer bytes per operation raises its ceiling. Right of the ridge, it is compute bound, and only a faster or better-used datapath helps. In D·A·M terms, the bandwidth roof belongs to the Data axis, the compute roof to the Machine axis, and the Algorithm axis decides where on the intensity axis the kernel sits. The roofline is a ceiling, not a prediction. A kernel far below both roofs is limited by something the model omits, such as launch overhead, synchronization, or low occupancy. **[[01 Books/Volume II - Scaling/01 The Fleet/02 Compute Infrastructure/V2-02.04 The Memory Wall#^fig-roofline-landscape|The H100 Roofline Landscape]]** draws both roofs for an H100 and places decode, prefill, and training workloads against them.

For an H100, the book’s hardware constants give a dense FP16 peak of 989 TFLOP/s and a high-bandwidth memory (HBM) bandwidth of 3.35 TB/s, which places the ridge at about 295.2 FLOP/byte. Batch-1 decode of a 7-billion-parameter language model stored in 16-bit precision performs about two operations per parameter for each generated token (one multiply and one add). It must read every two-byte weight once, so its intensity is about 1 FLOP/byte. [[05 Reference/Volume II - Scaling/V2 Single-Machine Foundations#^eq-appdx-dam-roofline|Equation 3]] then caps attainable throughput at 3.35 TFLOP/s, roughly 0.3 percent of peak, however well the kernels are written. Serving ${B}$ sequences in one decode step reuses each loaded weight ${B}$ times and raises the intensity to roughly ${B}$ FLOP/byte, until key-value cache traffic, which grows with batch size and context length, begins to dominate the bytes moved. That arithmetic is why batching is the first lever of every serving system. **[[05 Reference/Volume II - Scaling/V2 Fleet Foundations#^sec-appdx-fleet-foundations-comm-compute-ratio|The communication-computation ratio]]** carries the same reasoning to the network, where interconnect bandwidth takes the place of HBM bandwidth.

### Bottleneck Diagnostic

^sec-appdx-dam-taxonomy-bottleneck-diagnostic

Each optimization shortens only one term of the iron law, so adding peak FLOP/s to a memory-bound kernel or adding memory bandwidth to a compute-bound kernel leaves step time unchanged while wasting engineering effort ([[05 Reference/Volume II - Scaling/V2 Single-Machine Foundations#^tbl-v2-bottleneck-actions|table 3]]).

| **If the workload is…** |                 **Dominant term**                  | **Optimization that works**                                             | **Optimization that is wasted**                    |
|:------------------------|:--------------------------------------------------:|:------------------------------------------------------------------------|:---------------------------------------------------|
| **Memory-Bound**        |           ${D_{\text{vol}}}/{\text{BW}}$           | Quantization, pruning, batching, kernel fusion, higher memory bandwidth | More peak FLOP/s alone                             |
| **Compute-Bound**       | ${O}/({R_{\text{peak}}} \cdot {\eta_{\text{hw}}})$ | Better kernels, Tensor Cores, faster GPU, lower precision               | More memory bandwidth (not binding)                |
| **Latency-Bound**       |                 ${L_{\text{lat}}}$                 | Batching requests, kernel fusion, async dispatch                        | Neither compute nor bandwidth (overhead dominates) |

Table 3: **What Works vs. What Is Wasted**: Optimizing the wrong term yields limited improvement and poor cost efficiency. A memory-bound model will not speed up from more peak FLOP/s alone; it needs higher arithmetic intensity, less data movement, or a faster memory subsystem.

^tbl-v2-bottleneck-actions

## Accelerator Memory Hierarchy

^sec-appdx-dam-taxonomy-memory-hierarchy

An accelerator is a fast arithmetic engine surrounded by memories that trade bandwidth for capacity, and most performance arguments in this book reduce to the question of which boundary a byte must cross. Nearest the compute units, registers and on-chip shared memory (SRAM) hold the operands of the kernel that is executing, backed by a shared on-chip L2 cache (50 MB on an H100). Beyond the die, HBM holds the model’s working state (80 GB at 3.35 TB/s on an H100). Host memory is reached over PCIe at 64 GB/s per direction, roughly 52× less than HBM, and local NVMe storage sits below host memory.

A kernel whose working set stays on chip runs near arithmetic speed; one that streams operands from HBM is bounded by the roofline above; one that must reach host memory or storage is slower still. The **memory wall**, the widening gap between arithmetic throughput and the bandwidth that feeds it, is the single-machine form of the constraint that reappears at fleet scale as the network wall. A multi-accelerator node adds a scale-up fabric between devices (NVLink, at 450 GB/s per direction on an H100), and the scale-out network adds tiers beyond the node. **[[05 Reference/Volume II - Scaling/V2 Fleet Foundations#^sec-appdx-fleet-foundations-numbers-to-know|Numbers Every Fleet Engineer Should Know]]** tabulates those tiers.

## Kernel-Level Levers

^sec-appdx-dam-taxonomy-kernel-levers

Four techniques shorten one device’s step without changing the model’s mathematics. Each removes a different cost in the iron law of [[05 Reference/Volume II - Scaling/V2 Single-Machine Foundations#^sec-appdx-dam-taxonomy-iron-law-mapping|section 1.2]], and each counts as a gain only when a measured trace confirms it. The four differ in which term they remove, what limits them, and what evidence a trace shows ([[05 Reference/Volume II - Scaling/V2 Single-Machine Foundations#^tbl-appdx-dam-kernel-levers|table 4]]).

### Fusion

^sec-appdx-dam-taxonomy-kernel-levers-fusion

**Operator fusion** combines consecutive operations into one kernel, so an intermediate result stays in registers or shared memory instead of being written to HBM and read back by the next kernel. It shrinks the data volume ${D_{\text{vol}}}$ of the data term and removes one launch per fused operation from the overhead term ${L_{\text{lat}}}$. The common kinds are chains of element-wise operations, an element-wise operation fused with a reduction such as a normalization, and operator-specific fusions such as a matrix multiply that applies its bias and activation before writing its output. Fusion stops paying when the live values of the combined kernel exceed the registers and shared memory available, which lowers occupancy or spills to memory, and when a reduction needs results from every thread block. A trace confirms it with fewer kernels and fewer HBM bytes before the step time falls.

### Tiling and IO-Aware Attention

^sec-appdx-dam-taxonomy-kernel-levers-tiling

**Tiling** sizes blocks of a computation to fit on-chip memory, so each operand fetched from HBM feeds many operations and arithmetic intensity rises. IO-aware attention such as FlashAttention applies the idea to attention. It computes the scores block by block, keeping a running maximum and sum for the softmax, so the full matrix of scores between every pair of positions is never written to HBM. The workspace grows linearly with sequence length rather than quadratically. The price is extra rescaling arithmetic and, in training, recomputing the scores in the backward pass. Decode processes one query row per step and has no quadratic intermediate, so its fused attention kernel is a single pass over the KV cache. Tiling reduces ${D_{\text{vol}}}$ and frees HBM capacity for the KV cache and larger batches.

### Graph Replay

^sec-appdx-dam-taxonomy-kernel-levers-replay

**Graph replay**, offered on NVIDIA GPUs as CUDA Graphs, records a stable sequence of kernels and memory copies once and then submits the whole sequence with one request in later steps. It removes the host-dispatch part of ${L_{\text{lat}}}$, which matters when many short kernels leave launch gaps between them, as in batch-one decode. A captured graph replays only the shapes, memory addresses, and control flow it recorded, so a server keeps one graph per shape bucket, and decode captures more easily than prefill, whose shapes vary with prompt length. Replay fuses nothing. The same kernels run with the gaps between them removed, which a timeline shows directly.

### Compilation

^sec-appdx-dam-taxonomy-kernel-levers-compilation

**Graph compilation** automates the three levers above. A compiler captures the program as a graph, rewrites and decomposes its operations, fuses them, selects or generates a kernel for each fused group (often by timing candidates, which is called autotuning), and plans memory. Just-in-time compilers keep the eager programming model, ahead-of-time inference engines specialize the program to a declared range of shapes, and tile-level kernel languages let an engineer write a fusion the compiler missed. Compilation reduces both ${D_{\text{vol}}}$ and ${L_{\text{lat}}}$, at the cost of build and warmup time, regions split at graph breaks where the compiler cannot capture the program, and recompilation when a new shape arrives. **[[01 Books/Volume II - Scaling/03 The Fleet in Production/09 Fleet Efficiency/V2-09.10 Trading Between Factors#^sec-performance-engineering-compilation-overhead|Compilation builds]]** prices that cost across a fleet and finds when it pays back.

| **Lever**                         | **Removes**                                         | **Iron-law term**        | **Main limit**                            | **Trace evidence**                        |
|:----------------------------------|:----------------------------------------------------|:-------------------------|:------------------------------------------|:------------------------------------------|
| **Fusion**                        | HBM round-trips of intermediates; kernel launches   | Data volume; overhead    | Register and shared-memory pressure       | Fewer kernels and fewer HBM bytes         |
| **Tiling and IO-aware attention** | Repeated HBM fetches; materialized attention scores | Data volume              | Rescaling arithmetic; recomputation       | Fewer HBM bytes; smaller attention memory |
| **Graph replay**                  | Host dispatch of each kernel                        | Overhead                 | Fixed shapes, addresses, and control flow | Launch gaps disappear from the timeline   |
| **Compilation**                   | All three, applied automatically                    | Data volume and overhead | Build time; graph breaks; recompilation   | Fewer, fused kernels after warmup         |

Table 4: **Kernel-Level Levers**: Each lever shortens a different term of one device’s step, so a trace must show that term moving before a step-time gain counts.

^tbl-appdx-dam-kernel-levers

*Introduction to Machine Learning Systems* develops these mechanisms in full, for a reader who wants more than this recap. Here, the four rows of [[05 Reference/Volume II - Scaling/V2 Single-Machine Foundations#^tbl-appdx-dam-kernel-levers|table 4]] serve as the checklist for verifying whether a local optimization has moved the intended iron-law term.

## Numeric Precision and Training Memory

^sec-appdx-dam-taxonomy-training-memory

Whether a large model fits in an 80 GB H100 memory bank or must be partitioned across dozens of accelerators depends on how many bytes each parameter and optimizer state occupies. In the number formats listed in the notation conventions at the front of the book, FP32 occupies 4 bytes, BF16 and FP16 occupy 2, and FP8 and INT8 occupy one. **Mixed-precision training** runs the forward and backward passes in a 16-bit format for speed and memory, while it keeps an FP32 master copy of the weights so that small updates are not lost to rounding. The Adaptive Moment Estimation (Adam) optimizer adds two FP32 moment estimates per parameter. [[05 Reference/Volume II - Scaling/V2 Single-Machine Foundations#^tbl-appdx-dam-training-state|Table 5]] totals the resulting bytes per parameter.

| **State**              | **Format** | **Bytes per parameter** | **In a resumable checkpoint** |
|:-----------------------|:----------:|:-----------------------:|:-----------------------------:|
| **Working weights**    |    BF16    |            2            |              Yes              |
| **Gradients**          |    BF16    |            2            |   No (recomputed on resume)   |
| **Master weights**     |    FP32    |            4            |              Yes              |
| **Adam moments (two)** |    FP32    |            8            |              Yes              |
| **Total**              |            |   16 (training state)   |           14 bytes            |

Table 5: **Mixed-Precision Adam Memory per Parameter**: Persistent training state before activations, framework metadata, and communication buffers. The checkpoint omits gradients because a resumed run recomputes them in its first step.

^tbl-appdx-dam-training-state

For Archetype A, the 175B-parameter dense model the chapters use as their running instance, the training state is 2.8 TB and a resumable checkpoint is 2.45 TB. A single H100 offers 80 GB of HBM (a binary nameplate, about 85.9 GB in decimal units), so the persistent state alone requires at least 33 devices before a single activation is stored. That floor is why the model state must be partitioned across devices, which **[[01 Books/Volume II - Scaling/02 Distributed ML/06 Distributed Training/V2-06 Distributed Training#^sec-distributed-training-systems|Distributed Training]]** develops. Serving the same model needs only the 16-bit weights, 350 GB, plus the key-value cache.

Activations are the other large consumer of training memory. The intermediate tensors that the backward pass needs grow with batch size, sequence length, hidden width, and depth, and for long sequences they can exceed the parameter state. **Activation checkpointing** stores only selected activations and recomputes the rest during the backward pass, trading additional compute for memory.

## Transformer Arithmetic

^sec-appdx-dam-taxonomy-transformer-arithmetic

Most worked examples in this book use decoder-only transformers, and three counting rules cover nearly all of their arithmetic. The symbols follow the book’s deep learning notation, with ${P}$ parameters, ${D}$ training tokens, ${N_L}$ layers, hidden dimension ${d}$, and sequence length ${S}$.

Each transformer layer holds four ${d}\times {d}$ attention projections and a feed-forward block that expands to $4{d}$ and back, about $12{d}^2$ weights in total. A model thus has roughly ${P}\approx 12 {N_L} {d}^2$ parameters excluding embeddings. GPT-3 has ${N_L} =$ 96 and ${d}=$ 12,288, which gives 173.9B against its published 175B.

Every weight contributes one multiply and one add per token, so a forward pass costs about $2{P}$ FLOPs per token. The backward pass computes gradients with respect to both activations and weights and costs about twice the forward pass, so training costs about $6{P}$ FLOPs per token and

$$
{O_{\text{train}}} \approx 6{P} {D} \tag{4}
$$

^eq-appdx-dam-training-flops

in total. For GPT-3, trained on 300 billion tokens, [[05 Reference/Volume II - Scaling/V2 Single-Machine Foundations#^eq-appdx-dam-training-flops|equation 4]] gives 3.15 × 10²³ FLOPs, within 1 percent of the reported 3.14 × 10²³ FLOPs. The rule omits the attention-score products, which add at most about ${S}/(6{d})$ to the weight FLOPs, or 2.8 percent for GPT-3 at ${S}=$ 2,048. That fraction stays small while the context is short compared with the hidden width and grows with long contexts.

Serving an autoregressive model has two phases with different physics. *Prefill* processes the whole prompt at once as matrix-matrix products, so its arithmetic intensity is high and it tends to be compute bound. *Decode* generates one token per step for each sequence as matrix-vector products; at batch size 1 it reads every weight to perform two FLOPs per weight, the memory-bound regime that the roofline example above quantifies. To avoid recomputing attention over the whole prefix at every step, decode stores each layer’s keys and values in a **key-value (KV) cache** of $2 {N_L} {d}\, {s_{\text{elem}}}$ bytes per token for standard multihead attention, or 4.72 MB per token for GPT-3 in FP16. **[[05 Reference/Volume II - Scaling/V2 Inference Foundations#^sec-appdx-inference-scale-kv-cache-fundamentals-2ccd|KV cache fundamentals]]** sizes that cache against device memory.

## Tooling Map

^sec-appdx-dam-taxonomy-tooling-map

Back-of-envelope byte and FLOP counts narrow the likely bottleneck, but hardware and runtime counters must confirm which iron-law term actually binds before an engineer rewrites a kernel or data pipeline. Each D·A·M axis is exposed by a distinct set of profiling utilities and primary metrics ([[05 Reference/Volume II - Scaling/V2 Single-Machine Foundations#^tbl-v2-dam-tooling|table 6]]).

| **Axis**      |        **Key metric**         |     **Primary tool**     |      **Secondary tool**       |
|:--------------|:-----------------------------:|:------------------------:|:-----------------------------:|
| **Data**      |   Batch Load and Wait Time    | Framework profiler trace | `iostat`, `pidstat` (I/O/CPU) |
| **Algorithm** |      FLOPs, Model Depth       |     PyTorch Profiler     |   DeepSpeed Flops Profiler    |
| **Machine**   | GPU Utilization, SM Occupancy |      Nsight Compute      |     DCGM, Nsight Systems      |

Table 6: **D·A·M Tooling Map**: Profiling utilities for diagnosing bottlenecks along each D·A·M axis.

^tbl-v2-dam-tooling

## D·A·M Scorecard

^sec-appdx-dam-taxonomy-dam-scorecard

The efficiency ratios in [[05 Reference/Volume II - Scaling/V2 Single-Machine Foundations#^tbl-v2-dam-scorecard|table 7]] grade a system’s performance against its theoretical limit. This report card is anchored by MFU,[[05 Reference/Volume II - Scaling/V2 Single-Machine Foundations#^fn3|³]] the ratio of achieved model FLOP/s to the hardware’s theoretical peak FLOP/s. The MFU grades are illustrative targets for compute-dominated training; memory-bound or latency-bound workloads must be judged against their attainable roofline and service-level objective (SLO) latency.

| **Axis**      |           **Metric**           |                                  **Definition**                                  | **Failing grade**  | **Passing grade**  |
|:--------------|:------------------------------:|:--------------------------------------------------------------------------------:|:------------------:|:------------------:|
| **Data**      |        **I/O Overhead**        |              $\frac{\text{Data Wait Time}}{\text{Total Step Time}}$              |      $>$ 10%       |       $<$ 1%       |
| **Algorithm** | **Compression/Sparsity Ratio** | $\frac{\text{Effective or active parameters}}{\text{Dense baseline parameters}}$ | Workload-dependent | Workload-dependent |
| **Machine**   |            **MFU**             |            $\frac{\text{achieved model FLOP/s}}{\text{peak FLOP/s}}$             |      $<$ 30%       |      $>$ 50%       |

Table 7: **The D·A·M Efficiency Rubric**: Use these three numbers to characterize single-machine maturity.

^tbl-v2-dam-scorecard

## Scaling the Taxonomy from Node to Fleet

^sec-appdx-dam-taxonomy-scaling

These single-node grades become most useful when they are carried forward into distributed design. The D·A·M taxonomy is the diagnostic baseline for a single machine, but as systems scale from a single node to the machine learning fleet, each axis undergoes a qualitative transformation.

### The Evolution of Constraints

^the-evolution-of-constraints

Crossing the node boundary replaces local bus limits and single-device failure rates with cluster-wide fabric and power limits. Scaling from one node to a fleet changes the kind of constraint on every axis, not only its size ([[05 Reference/Volume II - Scaling/V2 Single-Machine Foundations#^tbl-appendix-dam-axis-node-to-fleet|table 8]]).

| **Axis**          | **Node-level focus (D·A·M)** | **Fleet-scale transformation**                                                                                                |
|:------------------|:----------------------------:|:------------------------------------------------------------------------------------------------------------------------------|
| **Data (D)**      |  I/O Bandwidth (Disk/PCIe)   | **The communication wall**: the bottleneck shifts from local storage to the bisection bandwidth of the network fabric.        |
| **Algorithm (A)** |    Model Depth/Ops Count     | **The parallelism strategy**: the logic now includes how computation is partitioned across ${N}$ devices (3D parallelism).    |
| **Machine (M)**   |      Peak TFLOP/s, HBM       | **The power and reliability wall**: the constraint is no longer just silicon speed, but watts per rack and cluster-wide MTBF. |

Table 8: **D·A·M Constraints from Node to Fleet**: How each axis of the D·A·M taxonomy shifts when scaling from a single node to a multi-node fleet. The node-level focus (left) gives way to a qualitatively different fleet-scale constraint (right); the bottleneck migrates from local resource to global coordination cost.

^tbl-appendix-dam-axis-node-to-fleet

### Bridging to C³

^bridging-to-c3

While D·A·M diagnoses the *components* of a single node, the C$^3$ taxonomy (**[[05 Reference/Volume II - Scaling/V2 The C³ Taxonomy#^sec-appdx-c3-taxonomy|The C^3 Taxonomy]]**) diagnoses the *interactions* of the fleet. Each of its three dimensions inherits a specific piece of the single-machine diagnostic model:

1.  **Compute (${C}_1$)** inherits the Algorithm and Machine axes, now evaluated per device after the work is partitioned across ${N}$ devices.
2.  **Communication (${C}_2$)** inherits the Data axis, but is governed by network bandwidth, topology, and, over long distances, the speed of light rather than by local I/O alone.
3.  **Coordination (${C}_3$)** makes coordination costs explicit at fleet scale. Synchronization, checkpoints, and failure recovery also occur on one node, but distribution expands their scope and couples them to other machines.

This progression exposes cases where higher single-node MFU comes at the expense of scaling efficiency, so the complete fleet outcome can determine the choice. The node is optimized to serve the fleet.

## Summary

^sec-appdx-dam-taxonomy-summary

The D·A·M taxonomy provides the diagnostic baseline for every ML systems analysis. By isolating the bottleneck to Data, Algorithm, or Machine, practitioners ensure that optimization efforts target the binding constraint. The memory hierarchy, the byte accounting of mixed-precision training, and the transformer counting rules supply the quantities that fleet-scale arguments take as given. This single-node discipline is the prerequisite for the fleet-scale engineering addressed throughout this book.

**Key Takeaways: Single-machine diagnostic heuristics**

- **Identify the dominant axis**: Decide whether Data, Algorithm, or Machine is the binding constraint before proposing any optimization.
- **Profile arithmetic intensity**: Arithmetic intensity, read against the roofline’s ridge point, quantitatively distinguishes between Data-bound and Machine-bound regimes.
- **Use the iron law**: The iron law transforms vague symptoms into specific term-based bottlenecks.
- **Count bytes and FLOPs per parameter**: Mixed-precision Adam training holds 16 bytes per parameter (14 in a checkpoint), and dense transformer training costs about $6{P} {D}$ FLOPs. These two rules size most memory and compute budgets in the chapters.
- **Grade with the scorecard**: The Data-Algorithm-Machine scorecard standardizes “good” performance before moving to fleet scale.

^callout-takeaways--1-2-89c9892c

Back to top

## Source References

^source-references

Williams, Samuel, Andrew Waterman, and David Patterson. 2009. “Roofline: An Insightful Visual Performance Model for Multicore Architectures.” *Communications of the ACM* 52 (4): 65–76. https://doi.org/10.1145/1498765.1498785.

^ref-williams2009

## Footnotes

^footnotes

<sup>1</sup> **MECE (mutually exclusive, collectively exhaustive)**: A classification principle from management consulting (popularized by McKinsey) requiring that categories do not overlap and together cover every possibility. Applied to systems engineering, it is useful as an idealized decomposition, but D·A·M bottlenecks often overlap in practice. A kernel can be simultaneously memory-bound, synchronization-heavy, and poorly matched to available hardware.

^fn1

<sup>2</sup> **Arithmetic intensity**: The ratio of floating-point operations to bytes transferred (FLOP/byte). It determines whether a workload is memory-bound or compute-bound by comparison against the hardware’s *ridge point* (${R_{\text{peak}}}/{\text{BW}}$).

^fn2

<sup>3</sup> **MFU (model FLOPs utilization)**: Counts only *useful* model computation in the numerator. Gradient synchronization, memory management, and other overhead within the measurement window remain in elapsed time and lower the reported ratio.

^fn3

## Source

[Repository Source](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/books/vol2/backmatter/appendix_dam.qmd) · [Original License](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/LICENSE.md)

[Rendered Reading Snapshot](https://mlsysbook.ai/vol2/backmatter/appendix_dam.html#sec-appdx-dam-taxonomy). Rendering provenance is recorded in the import manifest.
