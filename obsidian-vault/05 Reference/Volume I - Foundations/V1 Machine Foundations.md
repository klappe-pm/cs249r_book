---
title: V1 Machine Foundations
type: Reference
volume: 1
chapter: 0
publication_status: Released
source_repository: https://github.com/klappe-pm/cs249r_book
source_commit: de87c0103806d7bfb1c677dbb77a2b92fa00c298
source_path: books/vol1/backmatter/appendix_machine.qmd
source_anchor: sec-appdx-machine-foundations
source_mode: Source-Correlated Published HTML
tags:
- Type/Reference
- Book/Volume_1
rendered_source_url: https://mlsysbook.ai/vol1/backmatter/appendix_machine.html
---

# V1 Machine Foundations

[[Home|Home]] · [[01 Books/Volume I - Foundations/Volume 1 Overview|Volume Overview]]

^sec-appdx-machine-foundations

A datasheet reports peak throughput, and a workload almost never reaches it. Closing that gap requires knowing which physical limit execution reaches first: memory bandwidth, arithmetic throughput, fixed overhead, or energy. This appendix collects the hardware models, ratios, and order-of-magnitude values used for single-node estimates in the book, so that chapter estimates can be checked against them. Architecture essentials support readers encountering memory hierarchies and hardware cost models for the first time. Familiarity with undergraduate computer architecture is helpful but not required.

## How to Use This Appendix

^how-to-use-this-appendix

This appendix is designed as a reference. When diagnosing performance issues, use it to translate a vague symptom (“it is slow”) into a specific constraint (“bandwidth bound at batch size one”) and then choose the lever that addresses it. Each need in [[05 Reference/Volume I - Foundations/V1 Machine Foundations#^tbl-appdx-machine-lookup|table 1]] leads to the section that carries the model or worked template and to the chapter that applies it to the book’s workloads.

| **Need**                                                          | **Reference Section**                                                                                                                                   | **Applied In**                                                                                                                                                                        |
|:------------------------------------------------------------------|:--------------------------------------------------------------------------------------------------------------------------------------------------------|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Sanity-check feasibility with orders of magnitude**             | [[05 Reference/Volume I - Foundations/V1 Machine Foundations#^sec-appdx-machine-foundations-numbers-know-b531\|section 1.1]]                               | **[[01 Books/Volume I - Foundations/01 Foundations/02 System Paradigms/V1-02.05 System Balance and Hardware#^sec-ml-systems-system-balance-hardware-96ab\|System Balance and Hardware]]**                                 |
| **Compare access times across memory, links, and storage**        | [[05 Reference/Volume I - Foundations/V1 Machine Foundations#^sec-appdx-machine-foundations-latencies-every-programmer-know-e89f\|section 1.1.1]]          | **[[01 Books/Volume I - Foundations/03 Optimization/11 Hardware Acceleration/V1-11.06 Memory Systems#^sec-hardware-acceleration-memory-hierarchy-1839\|Memory hierarchy]]**                                          |
| **Decide whether a kernel is compute or bandwidth bound**         | [[05 Reference/Volume I - Foundations/V1 Machine Foundations#^sec-appdx-machine-foundations-roofline-model-2529\|section 1.2.1]]                           | **[[01 Books/Volume I - Foundations/03 Optimization/11 Hardware Acceleration/V1-11.07 Performance Bounds#^sec-hardware-acceleration-roofline-model-42ff\|Performance Bounds]]**                                          |
| **Check that a performance equation is consistent**               | [[05 Reference/Volume I - Foundations/V1 Machine Foundations#^sec-appdx-machine-foundations-dimensional-analysis-76b3\|section 1.2.2]]                     | **[[01 Books/Volume I - Foundations/00 Introduction/01 Introduction/V1-01.08 Iron Law of ML Systems#^sec-introduction-iron-law-ml-systems-c32a\|Iron Law of ML Systems]]**                                                |
| **Predict whether more accelerators shorten a run**               | [[05 Reference/Volume I - Foundations/V1 Machine Foundations#^sec-appdx-machine-foundations-amdahls-law-gustafsons-law-b741\|section 1.2.3]]               | **[[01 Books/Volume I - Foundations/02 Development/08 Model Training/V1-08.08 Scaling Training Systems#^sec-model-training-singlenode-multigpu-training-c87f\|Single-node multi-GPU training]]**                                     |
| **Estimate the wall-clock time of a training run**                | [[05 Reference/Volume I - Foundations/V1 Machine Foundations#^sec-appdx-machine-foundations-training-time-equation-7c3e\|section 1.2.4]]                   | **[[01 Books/Volume I - Foundations/02 Development/08 Model Training/V1-08.03 Training-Time Law#^sec-model-training-iron-law-training-performance-a53f\|Training-Time Law]]**                                                 |
| **Size request concurrency for a serving target**                 | [[05 Reference/Volume I - Foundations/V1 Machine Foundations#^sec-appdx-machine-foundations-littles-law-21a3\|section 1.2.5]]                              | **[[01 Books/Volume I - Foundations/04 Deployment/13 Model Serving/V1-13.05 Queuing Theory#^sec-model-serving-littles-law-9352\|Little's Law]]**                                                               |
| **Explain why data movement dominates energy**                    | [[05 Reference/Volume I - Foundations/V1 Machine Foundations#^sec-appdx-machine-foundations-memory-hierarchy-2278\|section 1.3.1]]                         | **[[01 Books/Volume I - Foundations/03 Optimization/11 Hardware Acceleration/V1-11.06 Memory Systems#^sec-hardware-acceleration-memory-hierarchy-1839\|Memory hierarchy]]**                                          |
| **Separate latency-dominated from bandwidth-dominated transfers** | [[05 Reference/Volume I - Foundations/V1 Machine Foundations#^sec-appdx-machine-foundations-bandwidth-vs-latency-5320\|section 1.3.2]]                     | **[[01 Books/Volume I - Foundations/03 Optimization/11 Hardware Acceleration/V1-11.06 Memory Systems#^sec-hardware-acceleration-hostaccelerator-communication-bb7a\|Host-accelerator communication]]**               |
| **Place a device class by compute, memory, and power**            | [[05 Reference/Volume I - Foundations/V1 Machine Foundations#^sec-appdx-machine-foundations-ai-hardware-cheat-sheet-modern-reference-4dc1\|section 1.3.3]] | **[[01 Books/Volume I - Foundations/03 Optimization/11 Hardware Acceleration/V1-11.12 Choosing an Accelerator#^sec-hardware-acceleration-choosing-accelerator-6b2d\|Choosing an Accelerator]]**                               |
| **Choose a numerical format**                                     | [[05 Reference/Volume I - Foundations/V1 Machine Foundations#^sec-appdx-machine-foundations-floatingpoint-format-comparison-1836\|section 1.4.1]]          | **[[01 Books/Volume I - Foundations/03 Optimization/10 Model Compression/V1-10.04 Numerical Precision Changing How Values Are Stored#^sec-model-compression-numerical-format-comparison-8fa2\|Numerical formats]]**                              |
| **Map floating-point values to integers**                         | [[05 Reference/Volume I - Foundations/V1 Machine Foundations#^sec-appdx-machine-foundations-integer-quantization-5442\|section 1.4.2]]                     | **[[01 Books/Volume I - Foundations/03 Optimization/10 Model Compression/V1-10.04 Numerical Precision Changing How Values Are Stored#^sec-model-compression-quantization-precision-cd46\|Numerical Precision: Changing How Values Are Stored]]** |

Table 1: **Where to Look**: Each need maps to the section of this appendix that carries the model or worked template and to the chapter that applies it to the book’s workloads.

^tbl-appdx-machine-lookup

Conventions used here follow the book-wide notation (for example, ${B}$ is reserved for batch size and ${\text{BW}}$ for bandwidth). The values in this appendix are ratios and orders of magnitude, which change slowly because they follow from physics and circuit design. The dated specifications of particular accelerators, links, and storage devices change with every product generation. **[[05 Reference/Volume I - Foundations/V1 System Assumptions#^sec-appdx-system-assumptions|System Assumptions]]** tabulates them so a reader can substitute current values without disturbing the relationships here.

## Numbers to Know

^sec-appdx-machine-foundations-numbers-know-b531

In general systems engineering, Jeff Dean’s “Latency Numbers Every Programmer Should Know”[[05 Reference/Volume I - Foundations/V1 Machine Foundations#^fn1|¹]] gave developers a shared set of order-of-magnitude anchors for reasoning about cache misses, disk seeks, and network round trips before writing code. Machine learning systems rest on a parallel hierarchy of physical ratios: fetching a 32-bit weight from off-chip DRAM costs hundreds of times more energy and roughly a thousand times more latency than reading it from a register, a gap that no compiler flag can erase. Although absolute timings and wattages shift with every process node and workload, the relative gaps across memory tiers, precision widths, and fiber links remain stable across hardware generations. Memorizing those relationships turns back-of-envelope sizing into a fast sanity check on any design.

**Systems Perspective 1.1: Three numbers that matter most**

- **Energy ratio**: In the cited 45 nm reference, a 32-bit DRAM read uses ~581× the energy of one FP16 multiply.
- **Training-state footprint**: Model weights (2 bytes FP16) + gradients (2 bytes FP16) + master weights (4 bytes FP32) + optimizer states for Adaptive Moment Estimation (Adam) at 8 bytes. That totals 16 bytes per parameter, so Llama 3 8B (8.03B parameters) needs 128.5 GB to start full training, more than one accelerator’s memory.
- **Fiber propagation limit**: Light travels about 200 km/ms in fiber, so propagation sets a floor on every round trip.

### Reference Relationships

^reference-relationships

The numbers above mix two kinds of quantities: invariant physical or arithmetic bounds, such as propagation delay in fiber and bytes per parameter, and technology-specific energy ratios that shift with each process node while preserving their ordering. The three tables below separate those reference anchors into propagation latency, memory-to-compute energy cost, and model-sizing arithmetic.

#### Speed of Light

^speed-of-light

No network upgrade or routing optimization can deliver a cross-country round trip in 5 ms when light in fiber takes roughly 40 ms to make the journey. Each approximate round trip in [[05 Reference/Volume I - Foundations/V1 Machine Foundations#^tbl-speed-of-light-ref|table 2]] carries that irreducible propagation component.

| **Distance**           | **Round-Trip Latency** | **Implication**                      |
|:-----------------------|:----------------------:|:-------------------------------------|
| **Same data center**   |         ~1 ms          | Distributed training feasible        |
| **Cross-country (US)** |         ~40 ms         | Reduces the remaining request budget |
| **Cross-Atlantic**     |         ~60 ms         | Further reduces the request budget   |
| **Cross-Pacific**      |        ~100 ms         | Data locality is critical            |

Table 2: **Speed of Light Reference**: Light in fiber travels ~200 km/ms. These approximate round trips include reducible overhead; only propagation is irreducible.

^tbl-speed-of-light-ref

#### Energy Hierarchy

^energy-hierarchy

Moving data across wires costs far more energy than computing on it once it arrives in an arithmetic unit. Raising reuse per byte therefore pays off across every hardware generation ([[05 Reference/Volume I - Foundations/V1 Machine Foundations#^tbl-energy-ratios-ref|table 3]]).[[05 Reference/Volume I - Foundations/V1 Machine Foundations#^fn2|²]]

| **Relationship**                  | **Reference Ratio** | **Source and Interpretation**                                             |
|:----------------------------------|:-------------------:|:--------------------------------------------------------------------------|
| **DRAM access vs. FP16 multiply** |        ~581×        | Horowitz 45 nm; wire capacitance scales with distance                     |
| **FP32 vs. INT8 energy**          |        ~18×         | Horowitz 45 nm; bit width determines switching energy                     |
| **FP32 vs. FP16 energy**          |        ~3.4×        | Horowitz 45 nm; narrower arithmetic reduces switching and datapath energy |
| **L1 SRAM vs. register**          |         ~5×         | Illustrative on-chip hierarchy anchor; distance to the arithmetic unit    |

Table 3: **Energy Reference Ratios**: The first three ratios use Horowitz’s 45 nm measurements; the L1/register ratio is an illustrative on-chip hierarchy anchor.

^tbl-energy-ratios-ref

#### Scaling Rules

^scaling-rules

Memory and compute requirements for training and inference follow from a few arithmetic relationships ([[05 Reference/Volume I - Foundations/V1 Machine Foundations#^tbl-scaling-rules-ref|table 4]]).[[05 Reference/Volume I - Foundations/V1 Machine Foundations#^fn3|³]] The examples use Llama 3 8B. **[[01 Books/Volume I - Foundations/02 Development/08 Model Training/V1-08.04 Computation and Memory Costs of Training#^sec-model-training-optimization-algorithm-system-implications-f9f2|System cost of optimizer state]]** derives the 16 bytes per parameter of training state and why switching to 16-bit arithmetic does not shrink it.

| **Rule**                          |             **Formula**              |        **Example (Llama 3 8B)**         |
|:----------------------------------|:------------------------------------:|:---------------------------------------:|
| **Inference memory (FP16)**       |      2 bytes$\times$ parameters      |                 16.1 GB                 |
| **Inference memory (INT8)**       |      1 byte$\times$ parameters       |                 8.0 GB                  |
| **Training memory (Adam)**        |     16 bytes$\times$ parameters      |                128.5 GB                 |
| **Inference FLOPs (transformer)** |   ~2$\times$ parameters per token    |          16.1 GFLOP per token           |
| **Training FLOPs**                | ~6$\times$ parameters$\times$ tokens | $4.8 \times 10^{22}$ FLOPs on 1T tokens |

Table 4: **Scaling Rules**: These are arithmetic, not hardware-specific. Training memory includes FP16 weights (2 bytes), FP16 gradients (2 bytes), FP32 master weights (4 bytes), and Adam optimizer states (8 bytes for momentum + variance).

^tbl-scaling-rules-ref

### The Latency Hierarchy

^sec-appdx-machine-foundations-latencies-every-programmer-know-e89f

Distance costs time. Each step away from the arithmetic units, from registers through on-chip cache, off-chip memory, device and host links, the network, and storage, multiplies the wait for the first byte. The largest jumps come from crossing a physical boundary ([[05 Reference/Volume I - Foundations/V1 Machine Foundations#^tbl-memory-ratios-ref|table 5]]). If a register access took ten seconds, a read from accelerator memory would take hours and a read from local flash storage would take weeks.

| **Tier**                            | **Latency (Decade)** | **Relative to a Register** | **If a Register Access Took 10 s** |
|:------------------------------------|:--------------------:|:--------------------------:|:----------------------------------:|
| **Register**                        |       0.1–1 ns       |         1$\times$          |             10 seconds             |
| **L1 cache**                        |       1–10 ns        |             3×             |            33.3 seconds            |
| **L2 cache**                        |       1–10 ns        |            10×             |            2.2 minutes             |
| **Accelerator memory (HBM)**        |     100–1,000 ns     |            900×            |             2.5 hours              |
| **Accelerator-to-accelerator link** |     100–1,000 ns     |           2,000×           |             4.6 hours              |
| **Host link (PCIe)**                |       1–10 μs        |           3,000×           |             9.3 hours              |
| **Network fabric**                  |       1–10 μs        |          20,000×           |              1.9 days              |
| **Local flash storage (NVMe)**      |     100–1,000 μs     |          300,000×          |             38.6 days              |

Table 5: **The Latency Hierarchy**: Access latency by tier, as the decade that contains it, as a multiple of a register access (rounded to one significant figure), and on a human time scale where one register access takes ten seconds. The largest gaps come from crossing physical boundaries: off-chip memory, device and host links, network fabric, and storage.

^tbl-memory-ratios-ref

Bandwidth falls along the same path. On the reference accelerator, high-bandwidth memory delivers about 52× the bandwidth of the host link, and a network access costs about 18× the latency of an accelerator-memory access. Data that must cross the host link or the network should cross it once and be reused many times on the device.

### Illustrative Latency Budgets

^illustrative-latency-budgets

Hardware access latencies span nanoseconds to milliseconds, but the application decides how much total delay a response can tolerate: an autonomous braking controller must act within milliseconds while a batch training job can run for days ([[05 Reference/Volume I - Foundations/V1 Machine Foundations#^tbl-latency-targets-ref|table 6]]). These targets reflect safety envelopes, human perception thresholds, and service-level objectives rather than universal hardware limits. **[[01 Books/Volume I - Foundations/04 Deployment/13 Model Serving/V1-13.04 Request Lifecycle#^sec-model-serving-latency-budget-ef40|The latency budget]]** shows how a serving system divides such an end-to-end budget among its stages.

| **Application**        | **Budget** | **Constraint**                       |
|:-----------------------|:----------:|:-------------------------------------|
| **Autonomous braking** |  \<10 ms   | At 100 km/h, 10 ms = 28 cm of travel |
| **Voice assistant**    |  \<100 ms  | Human perception of “instant”        |
| **Web search**         |  \<200 ms  | User patience threshold              |
| **Video streaming**    |   \<1 s    | Buffer tolerance                     |
| **Batch training**     | hours–days | Throughput dominates latency         |

Table 6: **Illustrative Latency Targets**: Production requirements depend on the application and its service-level objectives.

^tbl-latency-targets-ref

**Systems Perspective 1.2: A note on terminology: GPUs and accelerators**

Throughout this book, “accelerator” is the general term for hardware acceleration. The principles of roofline analysis, memory hierarchies, numerical precision, and performance modeling apply to GPUs, Tensor Processing Units (TPUs), NPUs, application-specific integrated circuits, and other specialized AI accelerators. Vendor-specific features such as CUDA and NVLink are identified explicitly.

**[[05 Reference/Volume I - Foundations/V1 System Assumptions#^sec-appdx-assumptions-accelerator-specifications-7a21|Accelerator Specifications]]** tabulates the dated specifications for these accelerators, including the NVIDIA H100 that serves as the book’s reference machine. Those device peaks, together with the reference latencies, energy ratios, and application budgets in this section, supply the raw inputs for back-of-envelope checks, but raw specifications alone do not reveal which resource limits a workload. Turning hardware numbers into a bottleneck diagnosis requires compact analytical models that relate workload demand to machine ceilings.

## Physics of Computing

^sec-appdx-machine-foundations-physics-computing-c77f

An accelerator rated at hundreds of teraflops can still spend most of a training step waiting on memory reads, serial host dispatch, or in-flight request state. Raw hardware specifications (FLOP/s, bytes per second, watts) bound each resource in isolation, yet without analytical models an engineer cannot tell whether a slow kernel is compute-bound or bandwidth-bound, verify that a time equation is dimensionally consistent, predict whether doubling the accelerator count will halve training time, or size serving concurrency from arrival rate and latency. Four foundational models turn those hardware limits into quantitative checks.

### The Roofline Model

^sec-appdx-machine-foundations-roofline-model-2529

A kernel that achieves 1 percent of an accelerator’s peak FLOP/s may be poorly written, or it may already be saturating the memory bus at the physical limit of the chip. The Roofline Model ([[05 Reference/Volume I - Foundations/V1 Machine Foundations#^ref-williams2009|Williams et al. 2009]]) separates those two cases by bounding how fast a workload can run on a given hardware target according to whether it runs out of compute or memory bandwidth first.

Every operation has an **arithmetic intensity**: the ratio of computations performed to bytes moved from memory. Matrix multiplication achieves high arithmetic intensity because each loaded element is reused across multiple multiply-accumulate steps. In contrast, element-wise operations like rectified linear unit (ReLU) have low intensity because each element is fetched from memory, evaluated once, and written back. Plotting achievable performance against arithmetic intensity yields the roofline ([[05 Reference/Volume I - Foundations/V1 Machine Foundations#^fig-roofline|figure 1]]): a diagonal memory-bandwidth ceiling rises linearly from the origin until it meets the horizontal peak-compute ceiling at the ridge point. A workload’s arithmetic intensity determines which ceiling governs execution, and therefore whether optimizations must target memory traffic or arithmetic throughput.

![[90 Assets/Volume I/Shared Figures/Generated Figure f6adab1b5a.svg]]

Figure 1: **The Roofline Model**: The sloped memory-bandwidth ceiling and horizontal peak-compute ceiling meet at the ridge point. Plotting a workload by arithmetic intensity identifies which roofline ceiling applies.

^fig-roofline

The **ridge point** determines the hardware’s balance. Formally, when computation and data movement overlap completely (the overlapped form of the iron law), idealized wall-clock time is bounded below by the critical path:

$$
{T}\geq \max\left( \frac{{O}}{{R_{\text{peak}}}}, \frac{{D_{\text{vol}}}}{{\text{BW}}} \right)
$$

 Attainable throughput ${R_{\text{attain}}} = {O}/ {T}$ is therefore bounded by:

$$
{R_{\text{attain}}} \leq \frac{{O}}{\max\left( \frac{{O}}{{R_{\text{peak}}}}, \frac{{D_{\text{vol}}}}{{\text{BW}}} \right)} = \min\left( {R_{\text{peak}}}, \frac{{O}}{{D_{\text{vol}}}} \times {\text{BW}} \right) = \min({R_{\text{peak}}}, {I}\times {\text{BW}})
$$

 where ${I}= {O}/ {D_{\text{vol}}}$ is the arithmetic intensity measured at the DRAM interface. The ridge point ${I_{\text{ridge}}}$ is the transition intensity where the compute and bandwidth ceilings meet:

$$
{R_{\text{peak}}} = {I_{\text{ridge}}} \times {\text{BW}} \implies {I_{\text{ridge}}} = \frac{{R_{\text{peak}}}}{{\text{BW}}}
$$

 If a workload’s arithmetic intensity falls below ${I_{\text{ridge}}}$, it is bandwidth-bound (the roofline literature says memory-bound). Above that value, it is compute bound. The memory-bound regime is the bandwidth-bound archetype of **[[01 Books/Volume I - Foundations/01 Foundations/02 System Paradigms/V1-02.04 Analyzing Workloads#^sec-ml-systems-workload-archetypes-fd10|Workload archetypes]]**, whose lighthouse is GPT-2 decode. The compute-bound regime is the compute-bound archetype, whose lighthouse is ResNet-50. **[[01 Books/Volume I - Foundations/03 Optimization/11 Hardware Acceleration/V1-11.07 Performance Bounds#^sec-hardware-acceleration-roofline-model-42ff|Performance Bounds]]** develops both regimes and the levers that move a workload between them.

**Systems Perspective 1.3: Batch size controls arithmetic intensity**

For matrix multiplications, arithmetic intensity scales with the batch dimension. For ${\mathbf{Y}}= {\mathbf{X}}{\mathbf{W}}$, where ${\mathbf{X}}$ is $({B}\times {d_{\text{in}}})$ and ${\mathbf{W}}$ is $({d_{\text{in}}}\times {d_{\text{out}}})$:

- **FLOPs**: $2 \times {B}\times {d_{\text{in}}} \times {d_{\text{out}}}$ (multiply-adds).
- **Bytes**: Moving ${\mathbf{X}}$, ${\mathbf{W}}$, and ${\mathbf{Y}}$ costs approximately ${s_{\text{elem}}}({B}{d_{\text{in}}} + {d_{\text{in}}}{d_{\text{out}}} + {B}{d_{\text{out}}})$ bytes.

Doubling ${B}$ doubles FLOPs while weight traffic stays nearly constant when weights dominate, increasing arithmetic intensity. This is why batching often helps inference serving (**[[01 Books/Volume I - Foundations/04 Deployment/13 Model Serving/V1-13.06 Throughput Optimization#^sec-model-serving-batching-helps-f1dc|Why batching helps]]** develops the serving side, including the latency it adds). Activation traffic, cache behavior, shape, precision, and the ridge point still determine whether it reaches the compute ceiling.

#### A Concrete Example: the H100 Analysis

^sec-appdx-machine-foundations-concrete-example-a100-analysis-5b30

Consider an NVIDIA H100, the book’s reference machine, with dense FP16 Tensor Core performance of 989 TFLOP/s and HBM3 bandwidth of 3.35 TB/s. The ridge point is 989 TFLOP/s/3.35 TB/s = 295.2 FLOP/byte (the Tera prefixes cancel, yielding FLOP/byte).

Two common operations fall on opposite sides of that ridge. General matrix multiply (GEMM) on two square matrices of size 4096 by 4096 has arithmetic intensity of approximately 1,365 FLOP/byte, so 1,365 FLOP/byte \> 295.2 FLOP/byte and the operation is compute bound. An element-wise ReLU on an FP16 tensor performs 1 comparison while reading 2 bytes and writing 2 bytes (4 bytes total), yielding an arithmetic intensity of only $1/4 =$ 0.25 FLOP/byte. Because 0.25 FLOP/byte $\ll$ 295.2 FLOP/byte, the operation is severely bandwidth-bound, achieving only about 0.08 percent of peak FLOP/s. This contrast is why frameworks fuse an element-wise operation into the preceding matrix multiply, so the intermediate result never makes a round trip through memory. **[[01 Books/Volume I - Foundations/02 Development/07 ML Frameworks/V1-07.04 Execution from Graphs to Kernels#^sec-ml-frameworks-execution-strategy-matters-memory-wall-1ce8|The memory wall and kernel fusion]]** develops fusion and the launch overhead it removes.

Precision moves the ridge. At INT8 the H100’s peak rate doubles to 1,979 TOPS while its memory bandwidth stays fixed, so the ridge rises to about 591 operations per byte. A convolution layer that sits above the FP16 ridge can fall below the INT8 ridge, which is why quantized ResNet-50 inference can turn bandwidth bound on the same chip (**[[01 Books/Volume I - Foundations/03 Optimization/11 Hardware Acceleration/V1-11.07 Performance Bounds#^sec-hardware-acceleration-hardware-balance|Hardware ridge points]]**).

### Dimensional Analysis

^sec-appdx-machine-foundations-dimensional-analysis-76b3

In the roofline calculation, dividing peak throughput ($\text{FLOP/s}$) by memory bandwidth ($\text{bytes/s}$) cancels seconds and leaves $\text{FLOP/byte}$. Dividing byte volume directly by $\text{FLOP/s}$ or adding milliseconds of network delay to seconds of compute, by contrast, produces a quantity whose units do not reduce to time, turning a back-of-envelope estimate into a silent category error. Before plugging numbers into any performance equation, **dimensional analysis** verifies that the equation is **dimensionally homogeneous**, meaning every additive or equated term resolves to the same units.

Consider both levels of the iron law of ML systems (principle [[01 Books/Volume I - Foundations/02 Development/V1 Development Principles#^pri-iron-law|3]]) introduced in **[[01 Books/Volume I - Foundations/00 Introduction/01 Introduction/V1-01.08 Iron Law of ML Systems#^sec-introduction-iron-law-ml-systems-c32a|Iron Law of ML Systems]]**. First, in the multiplicative D·A·M form (**[[01 Books/Volume I - Foundations/00 Introduction/01 Introduction/V1-01.08 Iron Law of ML Systems#^eq-intro-dam-iron-law|equation 1.2]]**), intermediate units cancel across the three factors to leave seconds per task:

$$
{T}[\text{s}] = \frac{\text{Samples}}{\text{Task}} \times \frac{\text{FLOPs}}{\text{Sample}} \times \frac{\text{s}}{\text{FLOP}} = \frac{\text{s}}{\text{Task}}
$$

Second, for serialized execution phases (**[[01 Books/Volume I - Foundations/00 Introduction/01 Introduction/V1-01.08 Iron Law of ML Systems#^eq-intro-iron-law|equation 1.3]]**), every additive term must resolve to time (seconds):

$$
{T}[\text{s}] = \underbrace{ \frac{{D_{\text{vol}}} [\text{bytes}]}{{\text{BW}} [\text{bytes/s}]} }_{\text{seconds}} + \underbrace{ \frac{{O}[\text{FLOPs}]}{{R_{\text{peak}}} [\text{FLOP/s}] \cdot {\eta_{\text{hw}}} [1]} }_{\text{seconds}} + \underbrace{ {L_{\text{lat}}} [\text{s}] }_{\text{seconds}}
$$

- **Data term**: $\frac{\text{bytes}}{\text{bytes/s}} = \text{bytes} \times \frac{\text{s}}{\text{bytes}} = \text{s}$
- **Compute term**: $\frac{\text{FLOPs}}{\text{FLOP/s}} = \text{FLOPs} \times \frac{\text{s}}{\text{FLOP}} = \text{s}$
- **Latency term**: Already in seconds.

The equation is physically consistent. Apply this technique to any systems equation: if the dimensions do not match, the formula is wrong. “FLOPs” and “Bandwidth” cannot be traded directly because they have different units. Any such trade-off must convert through time, as the iron law does.

Once a single-device time equation is dimensionally sound, the next question is how its terms behave when work is partitioned across multiple processors.

### Amdahl’s Law and Gustafson’s Law

^sec-appdx-machine-foundations-amdahls-law-gustafsons-law-b741

Doubling the number of accelerators on a training job can either shorten the wall-clock time of a fixed batch or process twice as many tokens in the same time window, and serial overhead limits those two choices very differently. **Amdahl’s law** and **Gustafson’s law** formalize the two regimes according to what they hold fixed: Amdahl’s law bounds how much faster a *fixed* task can run (optimizing latency), whereas Gustafson’s law bounds how much *more* work can be completed in a fixed time budget (optimizing throughput).

#### Strong Scaling (Amdahl’s Law)

^sec-appdx-machine-foundations-strong-scaling-amdahls-law-c6c2

When an engineer splits a fixed training batch or a single inference query across more accelerators to reduce step latency, only the parallelizable matrix math shrinks; host dispatch, barrier synchronization, and sequential aggregation remain fixed. **Strong scaling** measures how much faster such a fixed-size problem runs as processors are added, and Amdahl’s law ([[05 Reference/Volume I - Foundations/V1 Machine Foundations#^ref-amdahl1967|Amdahl 1967]]) states that the serial fraction of the task sets a hard ceiling on the resulting speedup.[[05 Reference/Volume I - Foundations/V1 Machine Foundations#^fn4|⁴]] Let ${T}(1) = 1$ be normalized single-processor execution time, composed of serial fraction $1-{f_{\text{parallel}}}$ and parallelizable fraction ${f_{\text{parallel}}}$. If ${N_{\text{workers}}}$ processors execute the parallel fraction with linear scaling and zero communication overhead, execution time on ${N_{\text{workers}}}$ processors is:

$$
{T}({N_{\text{workers}}}) = (1-{f_{\text{parallel}}}) + \frac{{f_{\text{parallel}}}}{{N_{\text{workers}}}}
$$

 The resulting theoretical speedup is:

$$
\text{Speedup}({N_{\text{workers}}}) = \frac{{T}(1)}{{T}({N_{\text{workers}}})} = \frac{1}{(1-{f_{\text{parallel}}}) + \frac{{f_{\text{parallel}}}}{{N_{\text{workers}}}}}
$$

As ${N_{\text{workers}}} \to \infty$, the term $\frac{{f_{\text{parallel}}}}{{N_{\text{workers}}}} \to 0$, and the speedup converges to $1/(1-{f_{\text{parallel}}})$. To see Amdahl’s Law in action, suppose 5 percent of a training step is serial overhead (for example, Python global interpreter lock (GIL), kernel launch latency) and 95 percent is parallelizable matrix math:

- With ${N_{\text{workers}}}=1$, speedup is 1.
- With ${N_{\text{workers}}}=$ 8, speedup is 1/(0.05 + 0.95/8) ≈ 5.9×.
- With ${N_{\text{workers}}} \to \infty$, speedup is capped at 1/0.05 = 20×.

No matter how many accelerators are added, this fixed workload cannot run faster than 20×. The same ceiling limits a single-node optimization. **[[01 Books/Volume I - Foundations/03 Optimization/12 Benchmarking/V1-12.04 Benchmarking Granularity#^sec-benchmarking-endtoend-vs-component-latency-9952|End-to-end vs. component latency]]** applies it to a measured pipeline, where an unchanged preprocessing stage caps the gain from a faster model.

#### Weak Scaling (Gustafson’s Law)

^sec-appdx-machine-foundations-weak-scaling-gustafsons-law-eb7e

Rather than adding accelerators to finish a small, fixed dataset in milliseconds, large-model training grows the dataset and global batch size alongside the cluster so that more work completes in the same wall-clock window. **Weak scaling** measures how much larger a problem can become while holding runtime fixed as processors are added.[[05 Reference/Volume I - Foundations/V1 Machine Foundations#^fn5|⁵]] For ${N_{\text{workers}}}$ processors, let $1-{f_{\text{parallel}}}$ be the serial fraction of execution time measured on those processors for the scaled workload, and ${f_{\text{parallel}}}$ the parallel fraction. Gustafson’s law ([[05 Reference/Volume I - Foundations/V1 Machine Foundations#^ref-gustafson1988|Gustafson 1988]]) derives “scaled speedup” by asking how long that scaled problem would take on a single processor. On ${N_{\text{workers}}}$ processors, normalized runtime is ${T}({N_{\text{workers}}}) = (1-{f_{\text{parallel}}}) + {f_{\text{parallel}}} = 1$. Executing the same total work on a single processor requires running the parallel fraction sequentially, taking ${T}(1) = (1-{f_{\text{parallel}}}) + {N_{\text{workers}}} \cdot {f_{\text{parallel}}} = {N_{\text{workers}}} - (1-{f_{\text{parallel}}})({N_{\text{workers}}}-1)$. The resulting scaled speedup is:

$$
\text{Scaled Speedup}({N_{\text{workers}}}) = \frac{{T}(1)}{{T}({N_{\text{workers}}})} = {N_{\text{workers}}} - (1-{f_{\text{parallel}}})({N_{\text{workers}}} - 1)
$$

Because the parallel part grows linearly with ${N_{\text{workers}}}$ while the serial fraction $1-{f_{\text{parallel}}}$ remains fixed, weak scaling can keep efficiency high as the problem grows. Using the same 5 percent serial overhead ($1-{f_{\text{parallel}}}$ = 0.05), Gustafson’s Law tells a different story:

- With ${N_{\text{workers}}}=1$, speedup is 1.
- With ${N_{\text{workers}}}=$ 8, Scaled Speedup is 8 − 0.05 $\times$ (7) = 8 − 0.35 = 7.65×.
- With ${N_{\text{workers}}}=$ 1000, Scaled Speedup is 1000 − 0.05 $\times$ (999) ≈ 950×.

In weak scaling, efficiency remains high because the useful work (training the model) scales up to dwarf the fixed overheads. **[[01 Books/Volume I - Foundations/02 Development/08 Model Training/V1-08.08 Scaling Training Systems#^sec-model-training-singlenode-multigpu-training-c87f|Single-node multi-GPU training]]** shows how data-parallel training uses weak scaling to keep accelerators busy as the cluster grows.

### The Training-Time Equation

^sec-appdx-machine-foundations-training-time-equation-7c3e

Weak scaling explains why large training runs grow the dataset rather than shrink the wall-clock time, but budgeting a run still requires translating billions of parameters and tokens into days on a specific cluster. The **training-time equation** combines model size, token count, accelerator count, peak rate, and sustained hardware utilization into that wall-clock estimate, which **[[01 Books/Volume I - Foundations/02 Development/08 Model Training/V1-08.03 Training-Time Law#^sec-model-training-iron-law-training-performance-a53f|Training-Time Law]]** applies to the book’s training workloads.

**Napkin Math 1.1: The training time equation**

**Problem**: How long does dense-transformer training take for a stated model size, token count, accelerator count, peak rate, and utilization?

**Math**:

$$
{T}\approx \frac{6 \cdot {P}\cdot {D}}{{N_{\text{GPU}}} \cdot {R_{\text{peak}}} \cdot {\eta_{\text{hw}}}}
$$

**Variables**:

- **Training FLOP factor**: The factor 6 derives from $2{P}\text{ FLOP/token}$ for the forward pass and $4{P}\text{ FLOP/token}$ for the backward pass ($2{P}$ for activation gradients and $2{P}$ for weight gradients), yielding $6{P} {D}\text{ FLOPs}$ total across ${D}$ training tokens.
- **${P}$**: Number of model parameters.
- **${D}$**: Number of training tokens.
- **${N_{\text{GPU}}}$**: Number of accelerators.
- **${R_{\text{peak}}}$**: Peak FLOP/s of one accelerator.
- **${\eta_{\text{hw}}}$**: Hardware utilization, typically 30 percent–50 percent in this training estimate.

**Example**: Training a 1B parameter model on 20B tokens using 1 H100 (989 TFLOP/s) at 40 percent utilization. $\text{Total FLOPs} = 6 \times 1 \times 10^{9} \times 2 \times 10^{10} = 1.2 \times 10^{20} \text{ FLOPs}$. $\text{Throughput} = 1 \times (9.89 \times 10^{14}) \times 0.40 \approx 3.956 \times 10^{14} \text{ FLOP/s}$. ${T} = \frac{1.2 \times 10^{20}}{3.956 \times 10^{14}} \approx 303,336.7 \text{ seconds} \approx 5,055.6 \text{ minutes}$.

**Systems insight**: Under these assumptions, training takes about 3.5 days. In D·A·M terms, this equation is the macroscopic product of Data (${D}$ tokens), Algorithm ($6{P}\text{ FLOPs/token}$), and Machine ($({N_{\text{GPU}}} \cdot {R_{\text{peak}}} \cdot {\eta_{\text{hw}}})^{-1}\text{ s/FLOP}$). Doubling the token count doubles the time, while doubling the accelerator count or the utilization halves it.

### Little’s Law

^sec-appdx-machine-foundations-littles-law-21a3

Whereas the training-time equation sizes a batch job whose total token volume is known up front, an online inference server receives a continuous stream of queries, and every in-flight request holds working state in memory until its response completes. An accelerator can therefore exhaust its memory capacity from concurrent request state before its arithmetic units saturate. For capacity planning in stable inference systems, **Little’s law** ([[05 Reference/Volume I - Foundations/V1 Machine Foundations#^ref-little1961|Little 1961]]) relates long-run mean concurrency (${Q_{\text{req}}}$), mean arrival rate (${\lambda_{\text{arr}}}$), and mean time in system (${T_{\text{lat}}}$):[[05 Reference/Volume I - Foundations/V1 Machine Foundations#^fn6|⁶]]

$$
{Q_{\text{req}}} = {\lambda_{\text{arr}}} \times {T_{\text{lat}}}
$$

The law follows from operational conservation of requests over any observation interval $[0, {T_{\text{obs}}}]$. Let ${A}({t})$ denote cumulative arrivals and ${C}({t})$ cumulative completions, so the instantaneous in-flight queue occupancy is ${Q}({t}) = {A}({t}) - {C}({t})$. The average number of requests in the system over $[0, {T_{\text{obs}}}]$ is ${\bar{Q}}= \frac{1}{{T_{\text{obs}}}}\int_0^{{T_{\text{obs}}}} {Q}({t})\,d{t}$. The total accumulated request-time $\int_0^{{T_{\text{obs}}}} {Q}({t})\,d{t}$ equals the sum of residence times $\sum_{i=1}^{{N}({T_{\text{obs}}})} {W}_i$ of all ${N}({T_{\text{obs}}})$ requests completed by time ${T_{\text{obs}}}$ (plus boundary terms that vanish as ${T_{\text{obs}}}\to \infty$). Dividing both sides by ${T_{\text{obs}}}$:

$$
{\bar{Q}}= \frac{1}{{T_{\text{obs}}}}\int_0^{{T_{\text{obs}}}} {Q}({t})\,d{t}= \frac{{N}({T_{\text{obs}}})}{{T_{\text{obs}}}} \cdot \frac{1}{{N}({T_{\text{obs}}})}\sum_{i=1}^{{N}({T_{\text{obs}}})} {W}_i
$$

 In the limit as ${T_{\text{obs}}}\to \infty$ for a stable queue, $\lim_{{T_{\text{obs}}}\to\infty} \frac{{N}({T_{\text{obs}}})}{{T_{\text{obs}}}} = {\lambda_{\text{arr}}}$ and $\lim_{{N}\to\infty} \frac{1}{{N}}\sum_{i=1}^{N} {W}_i = {T_{\text{lat}}}$. These limits yield ${Q_{\text{req}}} = {\lambda_{\text{arr}}} \times {T_{\text{lat}}}$ regardless of arrival distribution or service-time distribution. Because the identity requires no Poisson-arrival or exponential-service assumption, it applies directly to heavy-tailed large language model (LLM) generation workloads so long as the queue is stationary.

To see this in practice, consider sustaining 1,000 QPS with 50 ms average latency. The law dictates that the system must support 1000 $\times$ 0.05 s = 50 concurrent requests.

That concurrency sizes worker pools, but sizing device memory needs another assumption. If every in-system request simultaneously holds 1 GB of device state, the average population implies 50 GB; queued requests may instead stay in host memory or share batched state. If 24 device slots (${Q_{\text{req,max}}}$, the most requests the device can hold at once) each remain occupied for 50 ms, their throughput proxy is ${Q_{\text{req,max}}}/{T_{\text{lat}}} = 24/0.05 = 480 \text{ QPS}$. Little’s law alone does not fix a maximum. Device capacity does.

Serving systems use this relation to size request concurrency, and **[[01 Books/Volume I - Foundations/04 Deployment/13 Model Serving/V1-13.05 Queuing Theory#^sec-model-serving-littles-law-9352|Little's Law]]** pairs it with a queueing model to show how latency degrades as utilization nears saturation. Together, these physics-based models (roofline, Amdahl, Gustafson, and Little) locate *where* a bottleneck lies. Acting on that diagnosis requires the hardware structures that impose the bounds: the memory hierarchy, the links that move data between tiers, and the classes of hardware that package them.

## Computer Architecture Essentials

^sec-appdx-machine-foundations-computer-architecture-essentials-10c2

A kernel can run at a small fraction of an accelerator’s advertised peak when data movement, insufficient parallelism, synchronization, launch overhead, or software inefficiency stands in the way. Physics sets the theoretical ceilings. Computer architecture defines the machinery that determines how close a real workload can get to them, across three structures: the memory hierarchy and its energy cost, the paths that move data between tiers, and the class of hardware that packages both.

### The Memory Hierarchy

^sec-appdx-machine-foundations-memory-hierarchy-2278

Computer systems rely on tiered storage architectures because no single physical medium simultaneously provides large storage capacity and the lowest access latency. Faster, smaller, and costlier tiers sit close to the arithmetic units; larger and cheaper tiers sit farther away ([[05 Reference/Volume I - Foundations/V1 Machine Foundations#^fig-memory-hierarchy|figure 2]]). When data movement sits on the critical execution path, staging tensors into the upper tiers avoids the orders-of-magnitude latency penalties of off-chip DRAM and persistent storage that [[05 Reference/Volume I - Foundations/V1 Machine Foundations#^tbl-memory-ratios-ref|table 5]] quantifies.

![[90 Assets/Volume I/Shared Figures/Generated Figure b21282f4c6.svg]]

Figure 2: **The Memory Hierarchy**: Performance depends on data proximity. Accessing HBM is roughly 900× slower than registers; accessing SSD is roughly 300,000× slower.

^fig-memory-hierarchy

The memory hierarchy limits ML systems in both time and energy. Each access farther from the arithmetic units costs more energy, because the signal must drive longer, higher-capacitance wires ([[05 Reference/Volume I - Foundations/V1 Machine Foundations#^tbl-hierarchy-energy-ref|table 7]]). **[[01 Books/Volume I - Foundations/03 Optimization/11 Hardware Acceleration/V1-11.06 Memory Systems#^sec-hardware-acceleration-memory-hierarchy-1839|Memory hierarchy]]** shows how accelerator design stages data in the upper tiers to avoid the off-chip cost.

| **Tier**            | **Technology** | **Energy per 32-bit Access** | **Relative to a Register** |
|:--------------------|:--------------:|:----------------------------:|:--------------------------:|
| **Register**        |   Flip-flops   |            0.1 pJ            |         1$\times$          |
| **L1 cache**        |      SRAM      |            0.5 pJ            |             5×             |
| **L2 cache**        |      SRAM      |             2 pJ             |            20×             |
| **Off-chip memory** |    DRAM/HBM    |            640 pJ            |           6,400×           |

Table 7: **Energy Across the Memory Hierarchy**: Energy per 32-bit access in the cited 45 nm reference technology. The DRAM value is the Horowitz measurement; the register and SRAM values are illustrative hierarchy anchors. Absolute values fall with each process node, but the ordering and the gap between on-chip and off-chip access persist.

^tbl-hierarchy-energy-ref

Energy explains why data should stay high in the hierarchy. The table gives per-access costs, so the energy of a whole workload also depends on how many accesses reach each tier and how often data is reused. How long a transfer between tiers takes depends on two distinct properties of the path it crosses.

### Bandwidth Versus Latency

^sec-appdx-machine-foundations-bandwidth-vs-latency-5320

Widening a data link tenfold barely changes the delivery time of a small inference request or control message, yet it cuts the transfer time of a multi-gigabyte model checkpoint nearly tenfold. Bandwidth (throughput once bytes are flowing) and latency (the fixed delay before the first byte arrives) govern those two regimes as distinct constraints. For data volume ${D_{\text{vol}}}$ sent over effective bandwidth ${\text{BW}}$ with fixed path latency ${L_{\text{lat}}}$, and assuming the latency and serialization costs do not overlap, total transfer time is:

$$
{T}= {L_{\text{lat}}} + \frac{{D_{\text{vol}}}}{{\text{BW}}}
$$

The crossover point is the transfer size where the two terms are equal:

$$
{n^*} = {L_{\text{lat}}} \times {\text{BW}}
$$

For transfers below ${n^*}$ (for example, small request or control messages), latency dominates. For transfers above it (for example, loading weights), bandwidth dominates.

Consider sending data over a 10 Gb/s link with 10 ms base request/response latency. The crossover size is 12.5 MB, so the dominant term depends on which side of that threshold the transfer falls.

- **Latency-dominated packet (1 KB)**: Transmission time is 1 KB $\times$ 8/10 Gb/s ≈ 0.8 μs. Total time is approximately 10 ms + 0.8 μs ≈ 10 ms. **Result**: Fixed path and protocol latency dominates; propagation is one component.
- **Bandwidth-dominated checkpoint (1 GB)**: Transmission time is $1\text{ GB} \times 8/10\text{ Gbps} \approx 800\text{ ms}$. Total time is $\approx 10\text{ ms} + 800\text{ ms} = 810\text{ ms}$. **Result**: Base latency is negligible; bandwidth is the bottleneck.

How much bandwidth, compute, and memory capacity sit on either side of those links depends on the target form factor, which ranges from liquid-cooled data center racks to milliwatt sensor boards.

### Accelerator Classes

^sec-appdx-machine-foundations-ai-hardware-cheat-sheet-modern-reference-4dc1

A model trained on a 700 W data center accelerator cannot be dropped onto a battery-powered phone or a microcontroller with a few hundred kilobytes of SRAM without redesigning the workload around the target’s physical envelope. The deployment paradigms of **[[01 Books/Volume I - Foundations/01 Foundations/02 System Paradigms/V1-02.02 Four Deployment Regimes Across Nine Orders of Magnitude#^sec-ml-systems-deployment-paradigm-framework-0d25|Four Deployment Regimes Across Nine Orders of Magnitude]]** run on four hardware classes whose peak throughput, memory bandwidth, memory capacity, and power budgets span orders of magnitude ([[05 Reference/Volume I - Foundations/V1 Machine Foundations#^tbl-accelerator-classes-ref|table 8]]). Each range covers representative devices in its class rather than any single product; **[[05 Reference/Volume I - Foundations/V1 System Assumptions#^sec-appdx-assumptions-accelerator-matrix-c4d0|Master accelerator matrix]]** tabulates the individual chips.

| **Class**                  |   **Peak Rate**   | **Memory Bandwidth** | **Memory Capacity** |  **Power**  |   **Ridge Point**   |
|:---------------------------|:-----------------:|:--------------------:|:-------------------:|:-----------:|:-------------------:|
| **Datacenter accelerator** | 100–2,000 TFLOP/s |      0.9–8 TB/s      |      30–200 GB      | 300–1,000 W |  100–300 FLOP/byte  |
| **Edge module**            |   4–300 TFLOP/s   |      8–200 GB/s      |       1–70 GB       |   2–60 W    | 100–1,000 FLOP/byte |
| **Mobile SoC**             |   20–40 TFLOP/s   |      50–80 GB/s      |       9–10 GB       |     5 W     |  300–700 FLOP/byte  |
| **Microcontroller**        |  60–500 MFLOP/s   |     60–700 MB/s      |      0.2–4 MB       |  5–400 mW   |   0.2–6 FLOP/byte   |

Table 8: **Accelerator Classes**: Order-of-magnitude ranges across representative devices in each class, rounded to one significant figure. Peak rate is the dense rate at each device’s native ML precision (FP16 or BF16 for data center accelerators, mostly INT8 for edge, mobile, and microcontroller parts), so compare rates within a class rather than across classes. The ridge point is peak rate divided by memory bandwidth.

^tbl-accelerator-classes-ref

Two patterns stand out across these classes. First, they span roughly 7 orders of magnitude in peak rate and 5 in power, so a model sized for one class rarely runs unchanged on another. Second, ridge points sit in the hundreds of FLOP per byte from data center to mobile, which leaves the same low-intensity operations bandwidth bound on all three. A microcontroller’s ridge, by contrast, sits within a few FLOP per byte, which makes nearly every layer of a keyword-spotting model compute bound and shifts the limiting constraint to the power budget. **[[01 Books/Volume I - Foundations/03 Optimization/11 Hardware Acceleration/V1-11.12 Choosing an Accelerator#^sec-hardware-acceleration-choosing-accelerator-6b2d|Choosing an Accelerator]]** applies these classes to the choice of accelerator. Moving between classes also changes which numerical formats the hardware supports natively, and numerical precision directly controls *how much* data must move.

## Numerical Representations

^sec-appdx-machine-foundations-numerical-representations-c889

Halving a tensor’s representation from 32 bits to 16 bits cuts its memory footprint and bandwidth traffic in half and doubles peak Tensor Core throughput on the same silicon, yet choosing the wrong 16-bit layout can cause small gradients to underflow to zero during training. Because the numerical format fixes both how many bytes each value occupies and how much energy each arithmetic operation costs, choosing among FP32, BF16, FP16, FP8, and INT8 is a direct trade-off between statistical fidelity and hardware throughput.

### Floating-Point Formats

^sec-appdx-machine-foundations-floatingpoint-format-comparison-1836

A gradient of magnitude $10^{-6}$ survives in 16-bit brain floating point (BF16) but flushes to zero in standard 16-bit IEEE floating point (FP16), even though both formats occupy two bytes. IEEE 754 standards and AI-specific floating-point representations divide a fixed bit budget between a sign bit, an exponent field that sets **dynamic range** (the span of representable magnitudes), and a mantissa field that sets **precision** (the granularity of values within that range). Operational ranges and typical uses differ by format ([[05 Reference/Volume I - Foundations/V1 Machine Foundations#^tbl-numerical-formats|table 9]]), and the bit partitions of FP32, BF16, FP16, and INT8 show where each format spends its bits ([[05 Reference/Volume I - Foundations/V1 Machine Foundations#^fig-float-formats|figure 3]]). BF16 retains FP32’s full 8-bit exponent field, preserving the same dynamic range while truncating the mantissa to 7 bits, whereas FP16 widens the mantissa to 10 bits at the cost of a narrower 5-bit exponent.

| **Format** | **Bits** | **Exponent** | **Mantissa** |                 **Dynamic Range**                  | **Typical Use Case**                           |
|:-----------|:--------:|:------------:|:------------:|:--------------------------------------------------:|:-----------------------------------------------|
| **FP32**   |    32    |      8       |      23      |            $\sim 10^{-38}$ to $10^{38}$            | Training (full precision), reference inference |
| **FP16**   |    16    |      5       |      10      | Normal: $6.10 \times 10^{-5}$–$6.55 \times 10^{4}$ | Training often with loss scaling, inference    |
| **BF16**   |    16    |      8       |      7       |             FP32 normal exponent range             | Training, usually without loss scaling         |
| **FP8**    |    8     |    4 or 5    |    3 or 2    |                       Varies                       | Training/inference on supported hardware       |
| **INT8**   |    8     |     N/A      |     N/A      |                    -128 to 127                     | Inference after quantization                   |

Table 9: **Numerical Format Comparison**: Each format trades off precision, dynamic range, memory footprint, and compute throughput.

^tbl-numerical-formats

![[90 Assets/Volume I/Shared Figures/Generated Figure 42944a94ad.svg]]

Figure 3: **Numerical Format Bit Layouts**: A visual comparison of how FP32, BF16, FP16, and INT8 allocate their bits.

^fig-float-formats

BF16[[05 Reference/Volume I - Foundations/V1 Machine Foundations#^fn7|⁷]] ([[05 Reference/Volume I - Foundations/V1 Machine Foundations#^ref-google-bfloat16-3450e2b6|Wang and Kanwar 2019]]; [[05 Reference/Volume I - Foundations/V1 Machine Foundations#^ref-kalamkar2019|Kalamkar et al. 2019]]) occupies the same 16-bit storage class as FP16, yet the two formats behave very differently during training. Because BF16 allocates three more bits to the exponent than FP16, nominal bit width alone does not predict whether a training run will need gradient scaling.

**Systems Perspective 1.4: The dynamic range wall**

The choice of numerical format is a direct application of the iron law of ML systems (principle [[01 Books/Volume I - Foundations/02 Development/V1 Development Principles#^pri-iron-law|3]]). Reducing precision from FP32 to BF16 or FP16 halves the data volume term, potentially doubling throughput on memory-bound workloads. However, the *type* of 16-bit format determines the engineering complexity:

- **Dynamic range (the exponent)**: BF16 preserves the eight-bit exponent of FP32 and therefore the same normal exponent range ([[05 Reference/Volume I - Foundations/V1 Machine Foundations#^ref-kalamkar2019|Kalamkar et al. 2019]]).
- **Precision (the mantissa)**: FP16 has a larger 10-bit mantissa than BF16 (7 bits), offering higher precision for values within its range. Its five-bit exponent, however, raises underflow risk. FP16 training therefore often uses **loss scaling**, an operational step that multiplies gradients by a large constant to keep more values representable ([[05 Reference/Volume I - Foundations/V1 Machine Foundations#^ref-micikevicius2017mixed|Micikevicius et al. 2018]]). **[[01 Books/Volume I - Foundations/02 Development/08 Model Training/V1-08.07 Pipeline Optimizations#^sec-model-training-mixedprecision-training-9218|Mixed-precision training]]** develops the full mixed-precision recipe.
- **Energy efficiency**: INT8 operations can be substantially more efficient than floating-point equivalents because they move less data and use simpler integer arithmetic paths. Moving to INT8 for inference is a primary lever for deploying neural networks under tight memory, latency, or power budgets ([[05 Reference/Volume I - Foundations/V1 Machine Foundations#^ref-jacob2018|Jacob et al. 2018]]; [[05 Reference/Volume I - Foundations/V1 Machine Foundations#^ref-krishnamoorthi2018quantizing|Krishnamoorthi 2018]]). **[[01 Books/Volume I - Foundations/03 Optimization/10 Model Compression/V1-10.04 Numerical Precision Changing How Values Are Stored#^sec-model-compression-numerical-format-comparison-8fa2|Numerical formats]]** compares the formats on accuracy cost and hardware support.

### Integer Quantization

^sec-appdx-machine-foundations-integer-quantization-5442

Storing weights and activations in 32-bit floating point spends four bytes per value and drives wide floating-point multipliers when 256 discrete levels often suffice for inference accuracy. Quantization cuts that cost by mapping continuous floating-point values to discrete integers, typically INT8, using either a symmetric or an asymmetric mapping to assign the floating-point range to 256 integer codes.

For symmetric quantization, let ${\alpha_{\text{sym}}}= \max |{x}|$ over the calibrated range, assume ${x}$ is clipped to $[-{\alpha_{\text{sym}}}, {\alpha_{\text{sym}}}]$, and set the scale ${s}= {\alpha_{\text{sym}}}/127$. The signed INT8 code is:

$$
{x_q} = \text{round}\left(\frac{{x}}{{s}}\right)
$$

This symmetric mapping works well for weight distributions centered around zero, whereas asymmetric quantization handles distributions that are not centered (common after ReLU, which produces only nonnegative values) by shifting the range before scaling. Let ${\alpha}$ and ${\beta}$ bound the calibrated range, clip ${x}$ to $[{\alpha}, {\beta}]$, and set the scale ${s}= ({\beta}- {\alpha})/255$. A common unsigned 8-bit mapping is:

$$
{x_q} = \text{round}\left(\frac{{x}- {\alpha}}{{s}}\right)
$$

The choice between symmetric and asymmetric quantization depends on the tensor’s distribution and has measurable accuracy implications. **[[01 Books/Volume I - Foundations/03 Optimization/10 Model Compression/V1-10.04 Numerical Precision Changing How Values Are Stored#^sec-model-compression-quantization-precision-cd46|Numerical Precision: Changing How Values Are Stored]]** develops calibration, granularity, and the accuracy cost of each mapping on the book’s workloads. Together with the floating-point formats, integer quantization completes the machine-level levers that determine how many bytes each operation moves and how much energy each arithmetic step consumes.

## Summary

^summary

Machine-side diagnosis begins with units, ceilings, and working sets. The roofline model and the iron law identify which ceiling limits performance, and Amdahl’s and Gustafson’s laws, the memory hierarchy, the accelerator classes, and the numerical formats explain the gap between a measurement and that ceiling.

Treat peak specifications as ceilings, not predictions. Compare a measurement with the relevant ceiling, then trace the remaining gap to utilization, data movement, runtime overhead, architecture, or software. A back-of-envelope estimate is useful when it states its assumptions and units and makes the next measurement obvious. Chip specifications age with every product generation; the relationships here outlast them.

Back to top

## Source References

^source-references

Scott, Colin. 2012. “Numbers Every Programmer Should Know by Year.”

^ref-scott2012latency

Horowitz, Mark. 2014. “1.1 Computing’s Energy Problem (and What We Can Do about It).” *2014 IEEE International Solid-State Circuits Conference Digest of Technical Papers (ISSCC)*, 10–14. https://doi.org/10.1109/isscc.2014.6757323.

^ref-horowitz2014

Williams, Samuel, Andrew Waterman, and David Patterson. 2009. “Roofline: An Insightful Visual Performance Model for Multicore Architectures.” *Communications of the ACM* 52 (4): 65–76. https://doi.org/10.1145/1498765.1498785.

^ref-williams2009

Amdahl, Gene M. 1967. “Validity of the Single Processor Approach to Achieving Large Scale Computing Capabilities.” *Proceedings of the April 18-20, 1967, Spring Joint Computer Conference on - AFIPS ’67 (Spring)*, AFIPS ’67 (spring), 483–85. https://doi.org/10.1145/1465482.1465560.

^ref-amdahl1967

Gustafson, John L. 1988. “Reevaluating Amdahl’s Law.” *Communications of the ACM* 31 (5): 532–33. https://doi.org/10.1145/42411.42415.

^ref-gustafson1988

Little, John D. C. 1961. “A Proof for the Queuing Formula: $L = \lambda W$.” *Operations Research* 9 (3): 383–87. https://doi.org/10.1287/opre.9.3.383.

^ref-little1961

Wang, Shibo, and Pankaj Kanwar. 2019. *BFloat16: The Secret to High Performance on Cloud TPUs*.

^ref-google-bfloat16-3450e2b6

Krishnamoorthi, Raghuraman. 2018. “Quantizing Deep Convolutional Networks for Efficient Inference: A Whitepaper.” *arXiv Preprint arXiv:1806.08342* abs/1806.08342.

^ref-krishnamoorthi2018quantizing

Jacob, Benoit, Skirmantas Kligys, Bo Chen, Menglong Zhu, Matthew Tang, Andrew Howard, Hartwig Adam, and Dmitry Kalenichenko. 2018. “Quantization and Training of Neural Networks for Efficient Integer-Arithmetic-Only Inference.” *2018 IEEE/CVF Conference on Computer Vision and Pattern Recognition*, 2704–13. https://doi.org/10.1109/cvpr.2018.00286.

^ref-jacob2018

Micikevicius, Paulius, Sharan Narang, Jonah Alben, Gregory Diamos, Erich Elsen, David Garcia, Boris Ginsburg, et al. 2018. “Mixed Precision Training.” *International Conference on Learning Representations (ICLR)*.

^ref-micikevicius2017mixed

Kalamkar, Dhiraj, Dheevatsa Mudigere, Naveen Mellempudi, Dipankar Das, Kunal Banerjee, Sasikanth Avancha, Dharma Teja Vooturi, et al. 2019. *A Study of BFLOAT16 for Deep Learning Training*.

^ref-kalamkar2019

## Footnotes

^footnotes

<sup>1</sup> **Jeff Dean**: A Google Senior Fellow and one of the architects of MapReduce, BigTable, and TensorFlow. His latency numbers, originally presented with Peter Norvig around 2010, became a canonical reference for systems engineers; Colin Scott’s interactive visualization shows that the *hierarchy* of latencies has stayed stable across hardware generations ([[05 Reference/Volume I - Foundations/V1 Machine Foundations#^ref-scott2012latency|Scott 2012]]).

^fn1

<sup>2</sup> **Energy hierarchy sources**: The DRAM and arithmetic values come from Horowitz ([[05 Reference/Volume I - Foundations/V1 Machine Foundations#^ref-horowitz2014|2014]]) (45 nm). The L1 SRAM/register ratio is an illustrative hierarchy anchor, not a Horowitz measurement. The headline ratio compares a 32-bit DRAM access with a 16-bit floating-point multiply. Both the absolute values and the ratio vary with process, circuit, memory technology, and operand width; wire distance helps explain why movement remains expensive.

^fn2

<sup>3</sup> **Training memory (Adam)**: The 16 bytes/parameter rule assumes mixed-precision training with Adam. ZeRO optimization can reduce per-accelerator memory by sharding optimizer states across accelerators, but the total memory across all accelerators remains ~16× parameters.

^fn3

<sup>4</sup> **Gene Amdahl (1922–2015)**: A legendary computer architect at IBM, where he was the chief architect of the System/360. He later founded Amdahl Corporation to compete with IBM in the mainframe market.

^fn4

<sup>5</sup> **John Gustafson**: A computer scientist known for his work in parallel computing and for introducing the Unum (universal number) format. His law was a direct response to the perceived “limits” of Amdahl’s Law when applied to massive scale.

^fn5

<sup>6</sup> **John Little**: An Institute Professor at MIT and a pioneer in the field of operations research. His law, proved in 1961, is fundamental to queuing theory and is used across fields from manufacturing to computer network analysis.

^fn6

<sup>7</sup> **BF16 (brain floating point 16)**: Originally introduced with Google TPU v2 and later adopted by Intel, Arm, and NVIDIA, BF16 became a common training format across accelerator ecosystems. Its adoption made format support in hardware, kernels, and distributed-training libraries a portability concern rather than a vendor-specific feature.

^fn7

## Source

[Repository Source](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/books/vol1/backmatter/appendix_machine.qmd) · [Original License](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/LICENSE.md)

[Rendered Reading Snapshot](https://mlsysbook.ai/vol1/backmatter/appendix_machine.html#sec-appdx-machine-foundations). Rendering provenance is recorded in the import manifest.
