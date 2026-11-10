---
title: V1 Optimization Principles
type: Part
volume: 1
chapter: 0
publication_status: Released
source_repository: https://github.com/klappe-pm/cs249r_book
source_commit: de87c0103806d7bfb1c677dbb77a2b92fa00c298
source_path: books/vol1/parts/optimize_principles.qmd
source_anchor: optimization-principles
source_mode: Source-Correlated Published HTML
tags:
- Type/Part
- Book/Volume_1
rendered_source_url: https://mlsysbook.ai/vol1/parts/optimize_principles.html
---

# V1 Optimization Principles

[[Home|Home]] · [[01 Books/Volume I - Foundations/Volume 1 Overview|Volume Overview]]

^optimization-principles

A working model is rarely an efficient one. Part II established how to construct ML systems that respect physical constraints; Part III addresses how to meet real-world demands on time, memory, and energy. Efficiency is also what keeps the bitter lesson affordable, because models grow with the computation available while budgets and deployment envelopes do not. Each optimization navigates a frontier, improving one metric (accuracy, latency, energy) while managing the cost to others, and each is a form of co-design. Data selection shapes the workload the algorithm sees, while compression and acceleration trade mathematical structure for physical feasibility. The principles here are the bounds and cost models of efficiency, which determine *why* some models are fast and affordable while others are slow and prohibitively expensive.

**Principle 5: The Pareto frontier**

**Bound**: After objective directions are normalized, a feasible point lies on the Pareto frontier exactly when no other point is at least as good on every objective and strictly better on one. No feasible design lies beyond that frontier, so moving along it improves one objective only by worsening another.

- **Quantization**: Trades numerical precision for reduced memory footprint.
- **Pruning**: Trades model capacity for smaller representations and can improve speed when the resulting sparsity or removed structures are supported by the target hardware.
- **Distillation**: Trades training compute for inference efficiency.

**Implication**: Systems engineers navigate this frontier to find the operating point appropriate to a specific deployment environment. There is no universal optimum.

^pri-pareto-frontier

Navigating the Pareto frontier requires knowing *which* resource to optimize. Before selecting a technique, engineers must diagnose whether the workload is limited by computation, memory movement, or dispatch latency. Arithmetic intensity supplies the first test. The introduction derived its threshold, the ridge point, by setting the iron law’s memory term equal to its compute term, and Part II placed training kernels on either side of that threshold in a roofline plot. Here the roofline becomes an explicit rule for choosing an optimization.

**Principle 6: Arithmetic intensity law**

**Bound**: Attainable throughput (${R_{\text{attain}}}$) is no greater than the minimum of peak compute (${R_{\text{peak}}}$) and DRAM bandwidth (${\text{BW}}$) times operational intensity at the cache–DRAM boundary (${I}$) ([[01 Books/Volume I - Foundations/03 Optimization/V1 Optimization Principles#^ref-williams2009|Williams et al. 2009]]):

$$
{R_{\text{attain}}} \leq \min({R_{\text{peak}}}, {I}\times {\text{BW}})
$$

Operational intensity and DRAM bandwidth must both be measured at the cache–DRAM boundary; this ideal bound excludes launch, synchronization, and other fixed overheads.

**Implication**: Adding peak compute does not raise the ideal roofline bound for a bandwidth-bound kernel. Engineers must identify whether the bottleneck is compute, bandwidth, or another system term before selecting an optimization.

^pri-arithmetic-intensity

Many important ML kernels fall on the memory-bound side of the ridge point, especially low-reuse operations such as embedding lookup, normalization, softmax, depthwise convolution, and small-batch inference paths. Dense matrix multiplications and convolutions can instead be compute-bound when batching and hardware utilization are high. This split is a consequence of the memory wall: processor speed has historically outpaced memory bandwidth, and the cumulative gap has widened over three decades ([[01 Books/Volume I - Foundations/03 Optimization/V1 Optimization Principles#^ref-wulf1995|Wulf and McKee 1995]]; [[01 Books/Volume I - Foundations/03 Optimization/V1 Optimization Principles#^ref-gholami2024|Gholami et al. 2024]]). Neural networks, with their large weight tensors and uneven temporal locality, are especially vulnerable, so [[01 Books/Volume I - Foundations/03 Optimization/V1 Optimization Principles#^tbl-bottleneck-diagnostic|table 1]] maps each bottleneck regime to the optimizations that address its dominant term and the changes that leave it untouched.

| **If the workload is…** |                 **Dominant Term**                  | **Optimization That Works**                                                | **Optimization That is Wasted**  |
|:------------------------|:--------------------------------------------------:|:---------------------------------------------------------------------------|:---------------------------------|
| **Bandwidth-Bound**     |           ${D_{\text{vol}}}/{\text{BW}}$           | Quantization, pruning, batching                                            | Faster accelerator (more FLOP/s) |
| **Compute-Bound**       | ${O}/({R_{\text{peak}}} \cdot {\eta_{\text{hw}}})$ | Better kernels, Tensor Cores, faster accelerator                           | More memory bandwidth            |
| **Overhead-Bound**      |                 ${L_{\text{lat}}}$                 | Kernel fusion, async dispatch, bounded microbatching under the latency SLO | More FLOP/s or bandwidth alone   |

Table 1: **The Bottleneck Diagnostic**: Before optimizing, identify which iron law term dominates. Optimizing the wrong term leaves the dominant bottleneck unchanged and usually yields little or no end-to-end improvement.

^tbl-bottleneck-diagnostic

Wall-clock time is only one cost of crossing the memory wall; the energy required to move data off-chip exposes a second constraint. Even when a memory-bound kernel meets its latency target, fetching operands repeatedly from off-chip DRAM dominates the power budget on both battery-powered devices and data center racks.

**Principle 7: The energy-movement principle**

**Decomposition**: Total workload energy depends jointly on per-event energy and event counts. In the cited 45 nm reference, moving a 32-bit value from DRAM can cost roughly 100–1,000$\times$ more energy per event than a 32-bit floating-point operation, depending on operation type ([[01 Books/Volume I - Foundations/03 Optimization/V1 Optimization Principles#^ref-horowitz2014|Horowitz 2014]]). Here, ${D_{\text{vol}}}$ is bytes moved and ${O}$ is operations executed. The term ${E_{\text{move}}}$ denotes the energy per byte moved from DRAM, so one 32-bit access costs $4\,{E_{\text{move}}}$. The term ${E_{\text{compute}}}$ denotes the energy of one 32-bit floating-point operation in the cited 45 nm technology.

$$
{E_{\text{total}}} \approx {D_{\text{vol}}} \times {E_{\text{move}}} + {O}\times {E_{\text{compute}}}, \qquad 4\,{E_{\text{move}}} \gg {E_{\text{compute}}} \quad \text{for the cited reference}
$$

**Implication**: When memory movement dominates workload energy, optimization strategies should prioritize kernel fusion (avoiding intermediate off-chip traffic) and quantization (reducing data size); when computation dominates, reducing operation counts and improving arithmetic kernels remain central.

^pri-energy-movement

Even with perfect data locality and optimal bottleneck targeting, a final constraint limits how much speedup any optimization can deliver. The introduction stated Amdahl’s law for an inference pipeline whose preprocessing and postprocessing capped the gain from a faster model, and later chapters applied it case by case, to data-ingestion workers and to communication overhead in training. Stated as a principle, it bounds every optimization in this part.

**Principle 8: Amdahl's law**

**Bound**: The maximum speedup of a system is limited by the fraction of the workload that cannot be accelerated ([[01 Books/Volume I - Foundations/03 Optimization/V1 Optimization Principles#^ref-amdahl1967|Amdahl 1967]]). Here, ${f_{\text{parallel}}}$ is the fraction of baseline execution time accelerated and ${G}$ is that fraction’s speedup, either an accelerator’s gain ${G_{\text{accel}}}$ or a worker count ${N_{\text{workers}}}$. The fixed-work model assumes the remaining fraction is unchanged and the acceleration introduces no additional overhead.

$$
\text{Speedup} = \frac{1}{(1-{f_{\text{parallel}}}) + \frac{{f_{\text{parallel}}}}{{G}}}
$$

**Implication**: If 95 percent of a model runs 100$\times$ faster on an accelerator, the total system speedup is only about 16.8$\times$, and no accelerator, however fast, can push it past 20$\times$. This explains *why* data loading and preprocessing often become the ultimate bottlenecks in highly optimized systems.

^pri-amdahl

Part III applies these principles across the three multiplicative factors of the iron law in the order the D·A·M taxonomy suggests (**[[05 Reference/Volume I - Foundations/V1 The D·A·M Taxonomy#^sec-appdx-dam-taxonomy|The D·A·M Taxonomy]]** gives the full diagnostic framework). On the data axis, **[[01 Books/Volume I - Foundations/03 Optimization/09 Data Selection/V1-09 Data Selection#^sec-data-selection|Data Selection]]** asks first whether fewer samples can achieve the target quality ($\text{Samples/Task}$). Where algorithm meets machine, **[[01 Books/Volume I - Foundations/03 Optimization/10 Model Compression/V1-10 Model Compression#^sec-model-compression|Model Compression]]** asks whether each sample’s pass can use fewer operations or fewer bits per value ($\text{FLOPs/Sample}$ and ${D_{\text{vol}}}$). On the machine axis, **[[01 Books/Volume I - Foundations/03 Optimization/11 Hardware Acceleration/V1-11 Hardware Acceleration#^sec-hardware-acceleration|Hardware Acceleration]]** asks how to execute each remaining operation in less time ($\text{Seconds/FLOP}$). Each chapter ends with a favorable local number (a smaller dataset, a smaller model, or a kernel placed under its roofline), and **[[01 Books/Volume I - Foundations/03 Optimization/12 Benchmarking/V1-12 Benchmarking#^sec-benchmarking|Benchmarking]]** closes the loop by testing whether those predicted savings survive end-to-end execution without violating quality constraints.

Back to top

## Source References

^source-references

Williams, Samuel, Andrew Waterman, and David Patterson. 2009. “Roofline: An Insightful Visual Performance Model for Multicore Architectures.” *Communications of the ACM* 52 (4): 65–76. https://doi.org/10.1145/1498765.1498785.

^ref-williams2009

Wulf, Wm. A., and Sally A. McKee. 1995. “Hitting the Memory Wall: Implications of the Obvious.” *ACM SIGARCH Computer Architecture News* 23 (1): 20–24. https://doi.org/10.1145/216585.216588.

^ref-wulf1995

Gholami, Amir, Zhewei Yao, Sehoon Kim, Coleman Hooper, Michael W. Mahoney, and Kurt Keutzer. 2024. “AI and Memory Wall.” *IEEE Micro* 44 (3): 33–39. https://doi.org/10.1109/mm.2024.3373763.

^ref-gholami2024

Horowitz, Mark. 2014. “1.1 Computing’s Energy Problem (and What We Can Do about It).” *2014 IEEE International Solid-State Circuits Conference Digest of Technical Papers (ISSCC)*, 10–14. https://doi.org/10.1109/isscc.2014.6757323.

^ref-horowitz2014

Amdahl, Gene M. 1967. “Validity of the Single Processor Approach to Achieving Large Scale Computing Capabilities.” *Proceedings of the April 18-20, 1967, Spring Joint Computer Conference on - AFIPS ’67 (Spring)*, AFIPS ’67 (spring), 483–85. https://doi.org/10.1145/1465482.1465560.

^ref-amdahl1967

## Source

[Repository Source](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/books/vol1/parts/optimize_principles.qmd) · [Original License](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/LICENSE.md)

[Rendered Reading Snapshot](https://mlsysbook.ai/vol1/parts/optimize_principles.html#optimization-principles). Rendering provenance is recorded in the import manifest.
