---
title: V1 The D·A·M Taxonomy
type: Reference
volume: 1
chapter: 0
publication_status: Released
source_repository: https://github.com/klappe-pm/cs249r_book
source_commit: de87c0103806d7bfb1c677dbb77a2b92fa00c298
source_path: books/vol1/backmatter/appendix_dam.qmd
source_anchor: sec-appdx-dam-taxonomy
source_mode: Source-Correlated Published HTML
tags:
- Type/Reference
- Book/Volume_1
rendered_source_url: https://mlsysbook.ai/vol1/backmatter/appendix_dam.html
---

# V1 The D·A·M Taxonomy

[[Home|Home]] · [[01 Books/Volume I - Foundations/Volume 1 Overview|Volume Overview]]

^sec-appdx-dam-taxonomy

A system that runs slowly rarely announces why. An idle accelerator can stem from a starved input pipeline (Data), an algorithm with too little arithmetic intensity (Algorithm), or a saturated memory bus (Machine). This appendix maps profiler symptoms and measurements to the axis that limits execution, before optimization begins. Readers should arrive with the three axes from the opening chapters and the iron law that quantifies them.

## How to Use This Appendix

^how-to-use-this-appendix

Use the D·A·M taxonomy when a system misses a performance, cost, or quality target and the cause is not yet clear. Work through the framework in four passes:

1.  **State the symptom and operating budget**: Record the missed end-to-end target, workload, and deployment context.
2.  **Localize the candidate axis or boundary**: Use [[05 Reference/Volume I - Foundations/V1 The D·A·M Taxonomy#^tbl-dam-components-ref|table 2]] for a first pass and [[05 Reference/Volume I - Foundations/V1 The D·A·M Taxonomy#^tbl-dam-intersections|table 3]] when the evidence crosses axes.
3.  **Test the hypothesis**: Map the evidence to the iron law and arithmetic intensity, then gather confirming measurements with [[05 Reference/Volume I - Foundations/V1 The D·A·M Taxonomy#^tbl-dam-troubleshooting|table 5]] and [[05 Reference/Volume I - Foundations/V1 The D·A·M Taxonomy#^tbl-dam-tooling|table 6]].
4.  **Intervene and remeasure**: Choose a lever from [[05 Reference/Volume I - Foundations/V1 The D·A·M Taxonomy#^tbl-bottleneck-actions|table 7]], repeat the end-to-end measurement, and score the result with [[05 Reference/Volume I - Foundations/V1 The D·A·M Taxonomy#^tbl-dam-scorecard|table 8]]. If the target does not improve, revise the hypothesis.

[[05 Reference/Volume I - Foundations/V1 The D·A·M Taxonomy#^tbl-dam-lookup|Table 1]] maps each common need to the section that answers it. In every case the axis label is a hypothesis, not a verdict. The axes overlap, and a useful diagnosis may name both a dominant axis and a boundary effect.

| **Need**                                                     | **Section**                                                                                                                     |
|:-------------------------------------------------------------|:--------------------------------------------------------------------------------------------------------------------------------|
| Classify an optimization by the axis it acts on              | [[05 Reference/Volume I - Foundations/V1 The D·A·M Taxonomy#^sec-appdx-dam-taxonomy-diagnostic-summary-9f73\|section 1.1]]            |
| Reason about a technique that spans two or three axes        | [[05 Reference/Volume I - Foundations/V1 The D·A·M Taxonomy#^sec-appdx-dam-taxonomy-intersection-landscape-0d6e\|section 1.2]]        |
| Predict which iron-law term a change shortens                | [[05 Reference/Volume I - Foundations/V1 The D·A·M Taxonomy#^sec-appdx-dam-taxonomy-iron-law-mapping-05db\|section 1.3]]              |
| Explain why overlapping two stages saved little time         | [[05 Reference/Volume I - Foundations/V1 The D·A·M Taxonomy#^sec-appdx-dam-taxonomy-dam-coordination-sum-max-92bb\|section 1.3.2]]    |
| Decide whether a kernel is compute-bound or bandwidth-bound  | [[05 Reference/Volume I - Foundations/V1 The D·A·M Taxonomy#^sec-appdx-dam-taxonomy-arithmetic-intensity-boundary-7f5e\|section 1.4]] |
| Narrow a symptom such as low accelerator utilization quickly | [[05 Reference/Volume I - Foundations/V1 The D·A·M Taxonomy#^sec-appdx-dam-taxonomy-rules-thumb-f94f\|section 1.5.1]]                 |
| Find the measurement and tool that confirm a hypothesis      | [[05 Reference/Volume I - Foundations/V1 The D·A·M Taxonomy#^sec-appdx-dam-taxonomy-production-troubleshooting-02fb\|section 1.5.2]]  |
| Choose the lever that moves the limiting term                | [[05 Reference/Volume I - Foundations/V1 The D·A·M Taxonomy#^sec-appdx-dam-taxonomy-bottleneck-diagnostic-3fc9\|section 1.5.3]]       |
| Judge whether a measured system is efficient enough          | [[05 Reference/Volume I - Foundations/V1 The D·A·M Taxonomy#^sec-appdx-dam-taxonomy-dam-scorecard-94e9\|section 1.5.4]]               |
| Avoid optimizing the wrong axis                              | [[05 Reference/Volume I - Foundations/V1 The D·A·M Taxonomy#^sec-appdx-dam-taxonomy-antipatterns-72e1\|section 1.6]]                  |
| Follow a complete diagnosis on the reference accelerator     | [[05 Reference/Volume I - Foundations/V1 The D·A·M Taxonomy#^sec-appdx-dam-taxonomy-dam-case-studies-593f\|section 1.7]]              |
| Interpret a loss curve that stops improving as data grows    | [[05 Reference/Volume I - Foundations/V1 The D·A·M Taxonomy#^sec-appdx-dam-taxonomy-scaling-laws-vs-roofline-b290\|section 1.8]]      |

Table 1: **Need-to-Section Lookup**: Each row names a diagnostic need and the section of this appendix that answers it. Start from the need that matches the observed symptom.

^tbl-dam-lookup

## The Three Axes

^sec-appdx-dam-taxonomy-diagnostic-summary-9f73

When a training step stalls or a serving call misses its latency budget, the cause can sit in JPEG decoding on the host, quadratic attention work in the model, or a saturated memory bus on the accelerator. The taxonomy separates those causes along the three axes of the iron law of ML systems (**[[01 Books/Volume I - Foundations/00 Introduction/01 Introduction/V1-01.08 Iron Law of ML Systems#^sec-introduction-iron-law-ml-systems-c32a|Iron Law of ML Systems]]**). Data is what the model learns from and what the pipeline must deliver, Algorithm is the computation the model performs, and Machine is the hardware that executes that computation. [[05 Reference/Volume I - Foundations/V1 The D·A·M Taxonomy#^tbl-dam-components-ref|Table 2]] summarizes the role, primary physical constraint, and core optimization pathway for each axis.

| **Axis**          |              **Role**              |    **Physical Constraint**    | **High-Leverage Optimization**                                                                                                                      |
|:------------------|:----------------------------------:|:-----------------------------:|:----------------------------------------------------------------------------------------------------------------------------------------------------|
| **Data (D)**      |     What the model learns from     | Volume, quality, arrival rate | Data Selection (**[[01 Books/Volume I - Foundations/03 Optimization/09 Data Selection/V1-09 Data Selection#^sec-data-selection\|Data Selection]]**)                        |
| **Algorithm (A)** | The computation the model performs |  Operations and dependencies  | Model Compression (**[[01 Books/Volume I - Foundations/03 Optimization/10 Model Compression/V1-10 Model Compression#^sec-model-compression\|Model Compression]]**)         |
| **Machine (M)**   |   The hardware that executes it    |     Compute, memory, I/O      | Hardware Acceleration (**[[01 Books/Volume I - Foundations/03 Optimization/11 Hardware Acceleration/V1-11 Hardware Acceleration#^sec-hardware-acceleration\|Hardware Acceleration]]**) |

Table 2: **D·A·M Axis Reference**: Each axis maps to a constraint class and optimization strategy. Form a hypothesis, confirm it with measurements, then follow the chapter pointer.

^tbl-dam-components-ref

This first-pass separation is useful, but production systems rarely suffer from a single axis-centered bottleneck. More often, the problem sits at the boundary between two axes, as when a data format choice determines whether the accelerator can be saturated or a pruning strategy changes the memory access pattern. Handling these cases requires mapping the intersections.

## Axis Intersections

^sec-appdx-dam-taxonomy-intersection-landscape-0d6e

Pruning weights to cut Algorithm FLOPs can fragment Machine memory access, and changing a Data storage format can saturate host CPUs while trying to feed the accelerator. Because an intervention on one axis shifts pressure onto the other two, the conceptual Venn overlaps in **[[01 Books/Volume I - Foundations/00 Introduction/01 Introduction/V1-01.06 Defining ML Systems#^fig-ai-triad|The D·A·M Intersection Landscape]]** become an operational diagnostic triad of Data, Algorithm, and Machine joined by bidirectional coupling ([[05 Reference/Volume I - Foundations/V1 The D·A·M Taxonomy#^fig-dam-axis-triad|figure 1]]). To diagnose a production bottleneck, an engineer first identifies which axis currently limits the workload, then traces its two incident edges to predict how a candidate fix will alter memory, compute, or I/O demand across the system.

![[90 Assets/Volume I/01 Introduction/Generated Figure 969186f04d.svg]]

Figure 1: **The D·A·M Axis Triad**: A compact diagnostic view of Data, Algorithm, and Machine as three interdependent axes. The bidirectional links emphasize that an intervention on one axis changes the constraints on the other two.

^fig-dam-axis-triad

With the first-pass axis identified, the pairwise and three-way intersections expand into concrete engineering techniques and the chapters that teach them ([[05 Reference/Volume I - Foundations/V1 The D·A·M Taxonomy#^tbl-dam-intersections|table 3]]).

| **Zone**                                 | **Name**                   | **Key Techniques**                                           | **Book Coverage**                                                                                                                                                                                                                                                                                             |
|:-----------------------------------------|:---------------------------|:-------------------------------------------------------------|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Data**                                 | Information                | Storage formats, data quality, distributions                 | **[[01 Books/Volume I - Foundations/01 Foundations/04 Data Engineering/V1-04 Data Engineering#^sec-data-engineering\|Data Engineering]]**                                                                                                                                                                                           |
| **Algorithm**                            | Logic                      | Loss functions, architectures, gradients                     | **[[01 Books/Volume I - Foundations/02 Development/05 Neural Computation/V1-05 Neural Computation#^sec-neural-computation\|Neural Computation]]**, **[[01 Books/Volume I - Foundations/02 Development/06 Network Architectures/V1-06 Network Architectures#^sec-network-architectures\|Network Architectures]]**                                                            |
| **Data $\cap$ Algorithm**                | What to Learn From         | Data selection, curriculum learning, compute-optimal scaling | **[[01 Books/Volume I - Foundations/03 Optimization/09 Data Selection/V1-09 Data Selection#^sec-data-selection\|Data Selection]]**, **[[01 Books/Volume I - Foundations/02 Development/08 Model Training/V1-08 Model Training#^sec-model-training\|Model Training]]**                                                                                                  |
| **Data $\cap$ Machine**                  | How to Move Information    | I/O bandwidth, prefetching, data formats                     | **[[01 Books/Volume I - Foundations/01 Foundations/04 Data Engineering/V1-04 Data Engineering#^sec-data-engineering\|Data Engineering]]**, **[[01 Books/Volume I - Foundations/03 Optimization/11 Hardware Acceleration/V1-11 Hardware Acceleration#^sec-hardware-acceleration\|Hardware Acceleration]]**                                                              |
| **Algorithm $\cap$ Machine**             | How to Execute Efficiently | Quantization, pruning, kernel fusion, mixed precision        | **[[01 Books/Volume I - Foundations/02 Development/07 ML Frameworks/V1-07 ML Frameworks#^sec-ml-frameworks\|ML Frameworks]]**, **[[01 Books/Volume I - Foundations/03 Optimization/10 Model Compression/V1-10 Model Compression#^sec-model-compression\|Model Compression]]**                                                                                    |
| **Machine**                              | Physics                    | Silicon, memory hierarchy, peak FLOP/s                       | **[[01 Books/Volume I - Foundations/03 Optimization/11 Hardware Acceleration/V1-11 Hardware Acceleration#^sec-hardware-acceleration\|Hardware Acceleration]]**                                                                                                                                                                                   |
| **Data $\cap$ Algorithm $\cap$ Machine** | ML Systems Engineering     | Iron law, Roofline, training loops, serving                  | **[[01 Books/Volume I - Foundations/02 Development/08 Model Training/V1-08 Model Training#^sec-model-training\|Model Training]]**, **[[01 Books/Volume I - Foundations/04 Deployment/13 Model Serving/V1-13 Model Serving#^sec-model-serving\|Model Serving]]**, **[[01 Books/Volume I - Foundations/03 Optimization/12 Benchmarking/V1-12 Benchmarking#^sec-benchmarking\|Benchmarking]]** |

Table 3: **D·A·M Intersection Reference**: Each zone maps specific techniques to the axes they span and the chapters that cover them. The pairwise intersections require reasoning about two domains simultaneously; the center requires all three.

^tbl-dam-intersections

In the D·A·M acronym, Data, Algorithm, and Machine name the three diagnostic axes rather than single-letter algebraic variables; formal quantities follow the notation chapter, where ${D}$ denotes logical dataset size (samples or tokens) and ${D_{\text{vol}}}$ denotes physical data volume moved (bytes).

The axis-centered zones in [[05 Reference/Volume I - Foundations/V1 The D·A·M Taxonomy#^tbl-dam-intersections|table 3]] contain concepts that belong primarily to one axis: storage formats and distributions emphasize Data, loss functions and gradients emphasize Algorithm, and silicon physics and peak FLOP/s emphasize Machine. Single-domain expertise can introduce them, but deployed behavior may still depend on the other axes.

The pairwise intersections are where systems thinking begins. At ${\mathsf{Data}}\cap {\mathsf{Algorithm}}$ (*What to Learn From*), data selection, curriculum learning, active learning, and scaling laws ([[05 Reference/Volume I - Foundations/V1 The D·A·M Taxonomy#^sec-appdx-dam-taxonomy-scaling-laws-journey-4085|section 1.8.1]]) couple information content to algorithmic capacity, because adding data that the model cannot absorb wastes compute, while choosing architectures that outstrip available data wastes engineering time. That boundary governs statistical efficiency. At ${\mathsf{Data}}\cap {\mathsf{Machine}}$ (*How to Move Information*), the concern is physical delivery through I/O bandwidth, prefetching strategies, data formats, and the energy-movement invariant. Here data gravity manifests, because the cost of moving bytes through the memory hierarchy decides whether the machine stays fed. Once data reaches the device, ${\mathsf{Algorithm}}\cap {\mathsf{Machine}}$ (*How to Execute Efficiently*) links mathematical structure to hardware execution across quantization, pruning, kernel fusion, mixed precision, and computational graph optimization. It explains why a pruning scheme that cuts FLOPs while fragmenting memory access can still run slower on silicon.

The center, ${\mathsf{Data}}\cap {\mathsf{Algorithm}}\cap {\mathsf{Machine}}$, is where all three axes converge. The iron law, the roofline model, end-to-end training loops, serving pipelines, and holistic benchmarking all require simultaneous reasoning about data flow, algorithmic complexity, and hardware utilization. The intersections classify where a technique operates, but they do not say which axis actively throttles a workload. Isolating that axis requires translating these relationships into wall-clock execution time, which is the role of the iron law.

## Iron Law Mapping

^sec-appdx-dam-taxonomy-iron-law-mapping-05db

Placing quantization at the Algorithm/Machine intersection does not by itself tell an engineer how many milliseconds a 4-bit weight format will save, because the wall-clock gain depends on whether byte transfers, arithmetic, or kernel launches dominate the step. For any workload, the iron law turns the D·A·M axes into execution time ${T}$ (seconds) in two steps. First, at the workload level (**[[01 Books/Volume I - Foundations/00 Introduction/01 Introduction/V1-01.08 Iron Law of ML Systems#^eq-intro-dam-iron-law|equation 1.2]]**), time factors multiplicatively across the three axes:

$$
{T} = \underbrace{\left(\frac{\text{Samples}}{\text{Task}}\right)}_{\text{Data}} \times \underbrace{\left(\frac{\text{FLOPs}}{\text{Sample}}\right)}_{\text{Algorithm}} \times \underbrace{\left(\frac{\text{Seconds}}{\text{FLOP}}\right)}_{\text{Machine}}
$$

 where the product of the Data and Algorithm factors sets the total arithmetic work ${O} = (\text{Samples/Task}) \times (\text{FLOPs/Sample})$ in FLOPs. Second, for serialized execution phases (**[[01 Books/Volume I - Foundations/00 Introduction/01 Introduction/V1-01.08 Iron Law of ML Systems#^eq-intro-iron-law|equation 1.3]]**), unpacking how the machine executes those operations maps work across the D·A·M interfaces into three physical time terms. In these terms, ${D_{\text{vol}}}$ is bytes moved, ${\text{BW}}$ is bytes per second, ${R_{\text{peak}}}$ is peak throughput in FLOP/s, ${\eta_{\text{hw}}}$ is dimensionless hardware efficiency, and ${L_{\text{lat}}}$ is fixed overhead in seconds:

$$
{T}= \underbrace{ \frac{{D_{\text{vol}}}}{{\text{BW}}} }_{\text{Data/Machine}} + \underbrace{ \frac{{O}}{{R_{\text{peak}}} \cdot {\eta_{\text{hw}}}} }_{\text{Algorithm/Machine}} + \underbrace{ {L_{\text{lat}}} }_{\text{Cross-axis overhead}}
$$

Dividing this serialized decomposition by ${O}$ (and substituting arithmetic intensity ${I} = {O}/{D_{\text{vol}}}$) expresses the realized Machine factor ($\text{Seconds/FLOP}$) directly in terms of the three physical bottlenecks:

$$
\frac{\text{Seconds}}{\text{FLOP}} = \frac{{T}}{{O}} = \underbrace{\frac{1}{{I} \cdot {\text{BW}}}}_{\text{Memory time per FLOP}} + \underbrace{\frac{1}{{R_{\text{peak}}} \cdot {\eta_{\text{hw}}}}}_{\text{Compute time per FLOP}} + \underbrace{\frac{{L_{\text{lat}}}}{{O}}}_{\text{Overhead per FLOP}}
$$

Algorithm and Machine share the compute term, separated by which variable the engineer controls. Reducing the total operations (${O}$) is a Data or Algorithm lever, while reducing the realized time per operation ($\text{Seconds/FLOP}$) by raising peak throughput (${R_{\text{peak}}}$), utilization (${\eta_{\text{hw}}}$), or bandwidth (${\text{BW}}$) is a Machine lever. This per-FLOP expression also shows why training and inference occupy different regimes under the same law. In large-batch training, high arithmetic intensity (${I}$) and large operation counts (${O}$) shrink the first and third terms so $\text{Seconds/FLOP}$ approaches the compute term (**[[01 Books/Volume I - Foundations/02 Development/08 Model Training/V1-08.03 Training-Time Law#^sec-model-training-iron-law-training-performance-a53f|Training-Time Law]]**). In small-batch or single-token inference, low ${I}$ and small ${O}$ per request inflate the memory and overhead terms (**[[01 Books/Volume I - Foundations/04 Deployment/13 Model Serving/V1-13 Model Serving#^sec-model-serving|Model Serving]]**).

The dominant measured cost appears in one of these terms. A slow system may move too much data (${D_{\text{vol}}}$), lack bandwidth (${\text{BW}}$), execute too many operations (${O}$), fail to use the hardware’s peak capability (${\eta_{\text{hw}}}$), or pay cross-axis overhead (${L_{\text{lat}}}$). A workload whose time is dominated by ${L_{\text{lat}}}$ is overhead-bound: kernel launches, dispatch, and synchronization, not bytes or arithmetic, set its pace.

### Component Levers

^sec-appdx-dam-taxonomy-component-levers-d441

Once profiling isolates the largest time term, each axis offers a distinct set of engineering levers that shrink its numerator or raise its denominator:

- **Data lever**: Reducing the samples processed per task ($\text{Samples/Task}$, which shrinks ${O}$) or the moved bytes (${D_{\text{vol}}}$) through deduplication and selection, or increasing I/O bandwidth (${\text{BW}}$).
- **Algorithm lever**: Reducing operations per sample ($\text{FLOPs/Sample}$, and thus ${O}$) through pruning, distillation, or architectural refinement, or reducing the bytes each weight and activation occupies through lower-precision representation. Quantization is an Algorithm choice that shrinks the Data/Machine term ${D_{\text{vol}}}$ and may raise hardware throughput ${R_{\text{peak}}}$, lowering $\text{Seconds/FLOP}$ without reducing operation count.
- **Machine lever**: Lowering $\text{Seconds/FLOP}$ by increasing peak throughput (${R_{\text{peak}}}$), memory bandwidth (${\text{BW}}$), or the utilization factor (${\eta_{\text{hw}}}$) via kernel fusion and scheduling.

Shrinking individual terms is the first lever; hiding one term behind another is the second.

### From Sum to Max

^sec-appdx-dam-taxonomy-dam-coordination-sum-max-92bb

When a training step waits for each batch to finish copying across PCIe before launching the forward pass, data-transfer time and compute time add directly; prefetching the next batch while the accelerator computes the current one hides the shorter stage behind the longer one. The additive iron law represents this unpipelined, sequential execution. Let ${T_{\text{sequential}}}$ denote time without overlap and ${T_{\text{pipelined}}}$ denote measured time with overlap. Overlap can move the sum toward a max, but dependencies, contention, and incomplete overlap keep the measured time above this ideal lower bound:

$$
{T_{\text{sequential}}}= \frac{{D_{\text{vol}}}}{{\text{BW}}} + \frac{{O}}{{R_{\text{peak}}} \cdot {\eta_{\text{hw}}}} + {L_{\text{lat}}} \quad \xrightarrow{\text{overlap}} \quad {T_{\text{pipelined}}}\geq \max\left(\frac{{D_{\text{vol}}}}{{\text{BW}}}, \frac{{O}}{{R_{\text{peak}}} \cdot {\eta_{\text{hw}}}}\right) + {L_{\text{lat}}}
$$

Compute should overlap with data movement wherever dependencies allow. [[05 Reference/Volume I - Foundations/V1 The D·A·M Taxonomy#^tbl-dam-overlap|Table 4]] summarizes key D·A·M coordination techniques that overlap work across axes.

| **Technique**           | **D·A·M Axes Overlapped**    | **Implementation**                                             |
|:------------------------|:-----------------------------|:---------------------------------------------------------------|
| **Prefetching**         | D overlaps M                 | DataLoader with `prefetch_factor`, `pin_memory=True`           |
| **CUDA Streams**        | D overlaps M                 | Separate streams for H2D transfer and compute                  |
| **Async Gradient Sync** | M (communication) overlaps A | Overlap bucketed AllReduce with remaining backward computation |
| **Double Buffering**    | D overlaps M                 | Fill buffer N+1 while computing on buffer N                    |

Table 4: **D·A·M Overlap Techniques**: Each technique overlaps work across axes, moving sequentially added Data/Machine and Algorithm/Machine time toward their ideal lower bound: the larger of the two terms. Dependencies and contention limit realized overlap.

^tbl-dam-overlap

Overlaps provide the greatest relative speedup when the D·A·M time terms are reasonably balanced. If one term dominates (for example, a severely bandwidth-bound kernel), overlapping the smaller term with the larger yields negligible gain, because the max is still set by the same bottleneck. This balance occurs near ${D_{\text{vol}}}/{\text{BW}} \approx {O}/({R_{\text{peak}}} \cdot {\eta_{\text{hw}}})$. The overhead term ${L_{\text{lat}}}$ stays outside the max in either case.

**Systems Perspective 1.1: The overhead that cannot hide**

The unhidden latency term ${L_{\text{lat}}}$ (kernel launch, synchronization barriers, Python dispatch) contains serialization points that cannot be fully overlapped. Kernel fusion can reduce this term by combining operations, but it does not eliminate all launch, scheduling, or synchronization overhead.

The iron law separates data-movement time from compute time, but it does not by itself say which of the two sets the hardware ceiling for a given kernel.

## Arithmetic Intensity Boundary

^sec-appdx-dam-taxonomy-arithmetic-intensity-boundary-7f5e

Doubling an accelerator’s peak FLOP/s leaves a kernel no faster if the arithmetic units spend most of each cycle waiting for bytes from memory. Which side of that ceiling a kernel sits on is decided by its arithmetic intensity[[05 Reference/Volume I - Foundations/V1 The D·A·M Taxonomy#^fn1|¹]] (${I}$), the operations performed per byte moved between memory and compute. A kernel whose intensity falls below the hardware’s ridge point ${R_{\text{peak}}}/{\text{BW}}$ is **bandwidth-bound**, the regime the roofline literature calls *memory-bound*. This book keeps the bandwidth name so the regime is not confused with running out of memory capacity. A kernel above the ridge point is compute-bound.

The reference accelerator places the boundary concretely. An H100’s dense FP16 ridge point is about 295 FLOP/byte. GPT-2 XL decoding one token at batch one reads all 3 GB of its FP16 weights and reaches an arithmetic intensity of only about 1 FLOP/byte, more than two orders of magnitude below the ridge. With kernel launches captured into a replayable graph (**[[01 Books/Volume I - Foundations/02 Development/07 ML Frameworks/V1-07.04 Execution from Graphs to Kernels#^sec-ml-frameworks-hybrid-approaches-jit-compilation-8954|Graph capture and JIT compilation]]**), the weight read takes about 0.9 ms while the arithmetic needs about 3 μs, so a faster arithmetic unit would leave the per-token time unchanged. **[[01 Books/Volume I - Foundations/03 Optimization/11 Hardware Acceleration/V1-11.07 Performance Bounds#^sec-hardware-acceleration-roofline-model-42ff|Performance Bounds]]** develops the ridge point, hardware balance, and the regimes on either side of it. **[[05 Reference/Volume I - Foundations/V1 Machine Foundations#^sec-appdx-machine-foundations-roofline-model-2529|The Roofline model]]** carries the worked roofline template. **[[01 Books/Volume I - Foundations/04 Deployment/13 Model Serving/V1-13.10 LLM Serving#^sec-model-serving-decode-floor-7d3a|The decode floor]]** turns the weight read into the decode floor a serving system plans around.

The roofline gives an upper performance bound when traffic and achieved rates are measured consistently. During a production incident, screening heuristics point to the measurements to collect first, which is where diagnosis begins.

## Diagnosing a Bottleneck

^sec-appdx-dam-taxonomy-diagnosing-bottleneck-c4e1

When a benchmark or production service misses its target, diagnosis narrows the search in four passes. Fast screening heuristics come first, followed by confirming hardware counters and profiler traces, targeted interventions on the limiting term, and a stopping scorecard that decides when to stop optimizing.

### Screening Rules of Thumb

^sec-appdx-dam-taxonomy-rules-thumb-f94f

Under incident pressure there is rarely time to solve the full iron law. Quantitative heuristics narrow the search space quickly. The thresholds below are screening signals to check against profiler traces and hardware counters, not conclusions.

- **Low accelerator utilization (\< 80 percent)**: Screen for data, CPU, or launch starvation. Confirm with input-pipeline wait, host CPU saturation, memory-bandwidth counters, and trace gaps.
- **High accelerator utilization (\> 95 percent)**: Treat this as machine bound only if compute units are busy and memory bandwidth is not saturated. If memory bandwidth is saturated, the bottleneck is still on the Data/Machine boundary.
- **Batch size of one**: Treat this as a warning that launch or dispatch overhead may dominate; confirm with traces before labeling the algorithm itself the bottleneck.
- **Low arithmetic intensity (below ridge point)**: The workload is likely bandwidth-bound (Data/Machine boundary). The precise boundary is ${R_{\text{peak}}}/{\text{BW}}$ and depends on hardware and precision.
- **Development-production mismatch**: Treat data drift as one hypothesis alongside configuration, load, dependency, and runtime differences.

Common industry labels cross the axes. Bandwidth-bound execution sits on the Data/Machine boundary because both bytes moved and available bandwidth matter. Compute-bound execution couples Algorithm work with Machine throughput. Overhead-bound execution may reflect algorithmic serial depth, runtime dispatch, synchronization, or queueing. A screened candidate becomes a diagnosis only when a measurement confirms it.

### Confirming the Hypothesis

^sec-appdx-dam-taxonomy-production-troubleshooting-02fb

Once a screening heuristic flags a suspect axis, the next step is to collect the hardware counter or profiler trace that can confirm or falsify it. [[05 Reference/Volume I - Foundations/V1 The D·A·M Taxonomy#^tbl-dam-troubleshooting|Table 5]] maps common production failure modes to candidate axes and the measurements that validate them.

| **Symptom**                     | **Hypothesis**             | **Confirm With**                                  | **Act After Confirmation**                    |
|:--------------------------------|:---------------------------|:--------------------------------------------------|:----------------------------------------------|
| **Low Accelerator Utilization** | Data/host starvation       | Trace gaps; loader, CPU, storage, launch counters | Prefetch, parallelize, or cut launches.       |
| **High Latency (p99)**          | Algorithm/runtime/queue    | Phase p99 and queue depth                         | Optimize the dominant phase.                  |
| **High Training Cost**          | Low useful-work efficiency | MFU, communication, idle time                     | Reduce the largest loss or resize.            |
| **High Inter-GPU Overhead**     | Communication bound        | Device trace; collective gaps                     | Bucket AllReduce; tune data-parallel overlap. |
| **Out-of-Memory (OOM)**         | Algorithm/Machine fit      | Peak weights, states, activations                 | Checkpoint, shard, quantize, or shrink batch. |

Table 5: **D·A·M Diagnostic Matrix**: First hypotheses and measurements for common failures. Confirm the limiting component before intervening.

^tbl-dam-troubleshooting

Each measurement in the matrix comes from a concrete hardware or runtime counter, and [[05 Reference/Volume I - Foundations/V1 The D·A·M Taxonomy#^tbl-dam-tooling|table 6]] connects the D·A·M components to the profiling utilities that expose them (**[[01 Books/Volume I - Foundations/02 Development/08 Model Training/V1-08.06 Identifying Bottlenecks#^sec-model-training-identifying-bottlenecks-f57f|Identifying Bottlenecks]]** develops the top-down profiling method these tools serve).

| **Axis**      | **Key Metric**                        | **Primary Tool**         | **Secondary Tool**            |
|:--------------|:--------------------------------------|:-------------------------|:------------------------------|
| **Data**      | Batch Load and Wait Time              | Framework profiler trace | `iostat`, `pidstat` (I/O/CPU) |
| **Algorithm** | FLOPs, Model Depth                    | PyTorch Profiler         | DeepSpeed Flops Profiler      |
| **Machine**   | Accelerator Utilization, SM Occupancy | Nsight Compute           | `nvidia-smi`, Nsight Systems  |

Table 6: **D·A·M Tooling Map**: Profiling utilities for diagnosing bottlenecks along each D·A·M axis. Start with the primary tool for quick triage; use secondary tools for deep-dive analysis when the primary tool’s output is inconclusive.

^tbl-dam-tooling

### Acting on the Limiting Term

^sec-appdx-dam-taxonomy-bottleneck-diagnostic-3fc9

Once those counters confirm which term dominates, an intervention that speeds up any other term leaves end-to-end performance flat: adding peak FLOP/s to bandwidth-bound token decoding or adding memory bandwidth to compute-bound dense training does not move wall-clock time. [[05 Reference/Volume I - Foundations/V1 The D·A·M Taxonomy#^tbl-bottleneck-actions|Table 7]] covers the four regimes the book’s lighthouse workloads occupy, plus the overhead-bound regime that any of them enters when the fixed latency term dominates. The compute, bandwidth, and overhead rows are named by terms of the iron law. Capacity-bound and power-bound workloads are limited by preconditions the time equation assumes are already met, that the working set fits in memory and that the energy budget can pay for the run. Either can therefore decide feasibility before any time term is evaluated (**[[01 Books/Volume I - Foundations/01 Foundations/02 System Paradigms/V1-02.04 Analyzing Workloads#^sec-ml-systems-workload-archetypes-fd10|Workload archetypes]]**). For each regime, the table contrasts the interventions that yield end-to-end gains against those that waste engineering effort.

| **Regime**          |                 **Limiting Term**                  | **Lighthouse**                                        | **Optimization That Works**                                                                           | **Optimization That Is Wasted**                                            |
|:--------------------|:--------------------------------------------------:|:------------------------------------------------------|:------------------------------------------------------------------------------------------------------|:---------------------------------------------------------------------------|
| **Compute-bound**   | ${O}/({R_{\text{peak}}} \cdot {\eta_{\text{hw}}})$ | ResNet-50; MobileNetV2; GPT-2 XL training             | Better kernels, Tensor Cores, faster accelerator, lower precision                                     | More memory bandwidth (not the limiting term)                              |
| **Bandwidth-bound** |           ${D_{\text{vol}}}/{\text{BW}}$           | GPT-2 and Llama decode                                | Quantization; structured pruning; batching for weight reuse; fusion that removes intermediate traffic | Faster accelerator (more FLOP/s will not help)                             |
| **Overhead-bound**  |                 ${L_{\text{lat}}}$                 | Any workload served at batch one; small eager kernels | Batch within the latency budget; capture graphs; fuse or dispatch asynchronously; reduce serial depth | More compute or bandwidth unless the trace shows it limits time            |
| **Capacity-bound**  |   ${M_{\text{total}}}$ vs. ${M_{\text{device}}}$   | DLRM embedding tables                                 | Shard or offload tables; quantize; checkpoint activations; shrink the batch                           | More FLOP/s or bandwidth before the working set fits                       |
| **Power-bound**     |   ${E_{\text{total}}}$ per inference vs. budget    | Keyword spotting                                      | Integer arithmetic; fewer bytes moved per inference; duty cycling; smaller models                     | Higher peak FLOP/s that raises power without lowering energy per inference |

Table 7: **What Works vs. What Is Wasted**: Optimizing a nonbinding term yields little or no end-to-end improvement. A bandwidth-bound language model will not benefit from additional peak FLOP/s alone, though an accelerator with more memory bandwidth may help. Capacity and power limits act before time does, so they are checked first.

^tbl-bottleneck-actions

The lighthouse column names each regime’s home workload, and a workload can cross regimes. GPT-2’s decode is bandwidth-bound, yet its training is compute-bound ([[05 Reference/Volume I - Foundations/V1 The D·A·M Taxonomy#^sec-appdx-dam-taxonomy-case-3-compute-wall-machine-3a0a|section 1.7.3]]), and ResNet-50, compute-bound in its kernels, becomes input-bound when the data pipeline cannot keep pace ([[05 Reference/Volume I - Foundations/V1 The D·A·M Taxonomy#^sec-appdx-dam-taxonomy-case-1-starving-accelerator-data-9a56|section 1.7.1]]). **[[01 Books/Volume I - Foundations/02 Development/07 ML Frameworks/V1-07.04 Execution from Graphs to Kernels#^sec-ml-frameworks-dispatch-tax|Dispatch overhead in eager execution]]** develops the dispatch overhead behind the overhead-bound row, and **[[01 Books/Volume I - Foundations/03 Optimization/11 Hardware Acceleration/V1-11.11 Heterogeneous SoC Design#^sec-hardware-acceleration-power-thermal-management-6c00|Power and thermal management]]** develops the power envelope behind the last. A repaired system still needs a verdict on whether it is good enough, which is what the scorecard supplies.

### Scoring the System

^sec-appdx-dam-taxonomy-dam-scorecard-94e9

Raw profiler metrics (utilization percentages, FLOP counts, bandwidth measurements) mean little until compared with the workload’s targets. The efficiency indicators of the D·A·M scorecard in [[05 Reference/Volume I - Foundations/V1 The D·A·M Taxonomy#^tbl-dam-scorecard|table 8]] set those targets and show whether a repaired system can stop or must keep investigating. They are screening signals, not universal grades. Model FLOPs utilization (MFU)[[05 Reference/Volume I - Foundations/V1 The D·A·M Taxonomy#^fn2|²]] is especially useful for large-model training.

| **Axis**      | **Metric**     |                       **Definition**                       |    **Investigate**     |   **Strong Signal**   |
|:--------------|:---------------|:----------------------------------------------------------:|:----------------------:|:---------------------:|
| **Data**      | I/O Overhead   |  $\dfrac{\text{Data Wait Time}}{\text{Total Step Time}}$   |    $>$ 10% (screen)    |    $<$ 1% (strong)    |
| **Algorithm** | Avoidable Work |      Profiler or ablation finds redundant operations       |  Redundant work found  | End-to-end work falls |
| **Machine**   | MFU            | $\dfrac{\text{Achieved model FLOP/s}}{\text{Peak FLOP/s}}$ | $<$ 30% (large models) | $>$ 50% (same regime) |

Table 8: **D·A·M Screening Indicators**: Context-dependent signals for investigation, not universal grades.

^tbl-dam-scorecard

The four steps work only when they are followed in order. In practice, teams under deadline pressure skip the confirming step and optimize the wrong axis with confidence, and these failure modes are common enough to deserve their own names.

## Anti-Patterns

^sec-appdx-dam-taxonomy-antipatterns-72e1

Before committing to complex kernel optimizations, watch for these common traps that waste engineering cycles. Each anti-pattern arises when a team applies an expensive engineering lever to an axis that does not limit end-to-end execution:

- **The hardware crutch**: Buying faster accelerators (*Machine*) to fix a slow Python data loader (*Data*). The new hardware will idle faster.
- **The model twiddle**: Changing neural architectures (*Algorithm*) when the bottleneck is actually network bandwidth or disk I/O.
- **The premature optimizer**: Writing custom CUDA kernels (*Machine*) before verifying if the Algorithm is doing too many unnecessary operations.

Each anti-pattern follows the same root cause: acting before diagnosing. The case studies that follow show proper diagnosis on the reference accelerator, starting from a confusing symptom and narrowing to the limiting term, and the first of them puts a number on the hardware crutch.

## Case Studies on H100

^sec-appdx-dam-taxonomy-dam-case-studies-593f

The three cases below run the four-step workflow on an H100, the book’s reference accelerator. Each uses a lighthouse workload in a regime the chapters develop: ResNet-50 starved by its input pipeline, DLRM paying launch overhead at batch one, and GPT-2 XL training against the compute term. In each scenario, an initial utilization reading could easily point to the wrong axis until a second measurement isolates the true bottleneck.

### Case 1: the Starving Accelerator (Data)

^sec-appdx-dam-taxonomy-case-1-starving-accelerator-data-9a56

A team moves ResNet-50 training from an A100 to an H100 and sees no change in epoch time. A well-tuned A100 sustains about 3,200 images/s. At the same fraction of its higher peak the H100 would train about 10,100 images/s, yet `nvidia-smi` on the new machine shows utilization oscillating far below that. Screening flags low utilization, and the trace confirms the hypothesis, showing the accelerator idle in gaps while every loader process is saturated decoding JPEGs. With 9 workers each decoding and augmenting about 375 images/s, the pipeline delivers 3,375 images/s regardless of the accelerator, a rate that kept the A100 fully busy while leaving the H100 busy only about 33 percent of the time. Because the upgrade was the hardware crutch, the useful intervention lies upstream of the model. Balancing the H100 requires about 28 workers’ worth of decode throughput, supplied by adding loader parallelism where host cores allow and by moving decode onto the accelerator, as the supply-and-demand pipeline model in **[[01 Books/Volume I - Foundations/02 Development/08 Model Training/V1-08.05 Pipeline Architecture#^sec-model-training-data-pipeline-8e71|Data pipeline]]** develops.

### Case 2: the Latency Cliff (Cross-Axis)

^sec-appdx-dam-taxonomy-case-2-latency-cliff-algorithm-8ee2

A recommendation service on an H100 must rank 200 candidate items per request within a 10 ms p99 budget. It misses badly while accelerator utilization stays low, because the serving code scores each candidate with its own DLRM call at batch one. Screening flags the batch size, and a trace confirms an overhead-bound regime. Each call issues about 40 kernels at about 15 μs of dispatch and launch apiece, costing 0.6 ms before any device work happens. By contrast, reading 51.2 KB of embeddings takes only about 15.3 ns at high-bandwidth memory (HBM) bandwidth, and the multilayer perceptron (MLP) needs only about 2.1 ns of arithmetic. Because the ${L_{\text{lat}}}$ term exceeds the other two by more than four orders of magnitude, scoring candidates one at a time multiplies that fixed tax to about 120 ms. A faster accelerator or wider memory bus would shrink only the nanosecond terms. Instead, batching all candidates into one call pays the overhead once to bring the request to about 0.6 ms, while capturing the call as a graph shortens what remains. The cliff runs the other way too: with large tables the same model becomes capacity-bound, the embedding reads grow, and the measurements must be repeated. **[[01 Books/Volume I - Foundations/04 Deployment/13 Model Serving/V1-13.06 Throughput Optimization#^sec-model-serving-batching-helps-f1dc|Why batching helps]]** develops why batching amortizes this fixed cost and where the latency budget stops it.

### Case 3: the Compute Wall (Machine)

^sec-appdx-dam-taxonomy-case-3-compute-wall-machine-3a0a

A team trains GPT-2 XL on one H100 in TF32. Accelerator utilization is pinned near its maximum, memory-bandwidth counters are unsaturated, and the profiler reports MFU near 50 percent, the strong-signal end of the scorecard. Because the data path keeps the accelerator fed and the trace shows no dispatch gaps, the compute term dominates. GPT-2’s home regime in serving is bandwidth-bound decode, but training at batch reuses every weight across many tokens and crosses the ridge. The run needs about 1.5 ZFLOP of arithmetic, which at this efficiency takes about 70 days, so only levers on the compute term help while adding loader workers or memory bandwidth changes nothing. Lowering precision from TF32 to BF16 where numerically safe raises the H100’s Tensor Core peak by about 2× ([[05 Reference/Volume I - Foundations/V1 The D·A·M Taxonomy#^ref-choquette2023|Choquette 2023]]), cutting the run to about 35 days. Data parallelism across the 8 accelerators of one node then brings it to about 4 days before communication losses. **[[01 Books/Volume I - Foundations/02 Development/08 Model Training/V1-08.02 From One Step to a Training Run#^sec-model-training-running-example-training-gpt2-19cd|Running cases: GPT-2 XL and ResNet-50]]** develops this workload as the training running example, including the memory limits that decide what batch fits.

Taken together, the three cases show why the same utilization number can imply different next steps. Low utilization meant a starved pipeline in the first case and dispatch overhead in the second, while high utilization in the third meant the run was already doing useful work and only the compute term could shrink. The same discipline applies when the question is not how fast the system runs but how much better the model can get.

## Scaling Laws and the Roofline

^sec-appdx-dam-taxonomy-scaling-laws-vs-roofline-b290

The case studies diagnosed wall-clock bottlenecks, where the target is step time or serving latency. When a training run already executes at high hardware efficiency yet held-out loss flattens despite more GPUs and longer runs, the diagnostic question shifts from throughput ceilings to learning ceilings: whether the stall reflects the normal diminishing returns of scale or a data-quality floor that added compute cannot move.

### Scaling Laws

^sec-appdx-dam-taxonomy-scaling-laws-journey-4085

A team that doubles its training compute budget must decide whether to spend those extra FLOPs on more parameters or on more training tokens. Scaling laws[[05 Reference/Volume I - Foundations/V1 The D·A·M Taxonomy#^fn3|³]] guide that split with empirical power laws that predict how held-out loss changes as resources increase within the fitted regime. Two landmark results are Kaplan scaling ([[05 Reference/Volume I - Foundations/V1 The D·A·M Taxonomy#^ref-kaplan2020scaling|Kaplan et al. 2020]]), which studied loss against parameter count (${P}$), data (${D}$), and total operations (${O}$), and Chinchilla scaling ([[05 Reference/Volume I - Foundations/V1 The D·A·M Taxonomy#^ref-hoffmann2022chinchilla|Hoffmann et al. 2022]]). Chinchilla estimated a compute-optimal balance for the dense autoregressive language-model regime studied, often summarized as roughly 20 training tokens per parameter (${D}\approx 20{P}$). **[[05 Reference/Volume I - Foundations/V1 Algorithm Foundations#^sec-appdx-algorithm-chinchilla-derivation|Compute-optimal scaling laws]]** derives that balance from a parametric loss surface, so a reader can see where the tokens-per-parameter ratio comes from and which fitted exponents it depends on.

As planning tools, these fits estimate how held-out loss changes with compute inside the observed regime. They do not guarantee a task error-rate reduction or extrapolate unchanged across architectures and data distributions.

### The Information Roofline

^sec-appdx-dam-taxonomy-information-roofline-destination-6426

When held-out loss flattens below the fitted scaling trend while tokens, parameters, and compute keep growing, adding accelerators or parameters buys no further accuracy. The **information roofline** names this limit that data quality places on what a model can learn, the counterpart to the ceiling the roofline model places on how fast it computes. Because it is a diagnostic label rather than a quantitative law, that flattening pattern tells the team to examine the data before buying more hardware. Four checks separate the causes. Deduplicating the training set and remeasuring tests whether repeated examples inflated the apparent data volume. Auditing a sample of labels estimates label noise. Comparing per-slice validation loss exposes coverage gaps. Comparing the training and validation distributions detects shift. If loss resumes falling after cleaning or reweighting the data at fixed compute, data quality was the limit. If it does not, the cause lies in optimization, model capacity, or evaluation noise, and the scaling-law fit itself should be rechecked.

A data-quality limit is distinct from the theoretical floor on error. For classification under a fixed data distribution and loss, the Bayes error rate[[05 Reference/Volume I - Foundations/V1 The D·A·M Taxonomy#^fn4|⁴]] is that irreducible floor, not a ceiling. Noise, label ambiguity, coverage gaps, and distribution shift can create data-quality limits above that floor, but they do not define one universal slope or breakpoint.

Adding accelerators or parameters is futile only after measurements establish that data quality is the limit. Whether debugging a training step, evaluating hardware utilization, or planning a scaling campaign, measure which axis is the bottleneck before choosing a lever.

**Checkpoint 1.1: D·A·M diagnosis check**

1.  A training job shows 95 percent accelerator utilization but loss has plateaued for two epochs. Which D·A·M axes could be responsible, and why is utilization alone insufficient to distinguish them?
2.  Your colleague suggests adding more data loader workers to a job where `nvidia-smi` shows 98 percent GPU utilization. What trace evidence is needed before deciding whether this will help?
3.  An inference server meets its latency SLO at batch size 1 but fails at batch size 16. Which iron-law terms and queueing effects may have changed, and which measurements identify the limiting regime?

## Summary

^sec-appdx-dam-taxonomy-summary-1521

D·A·M localizes candidate causes across Data, Algorithm, and Machine. The iron law and arithmetic intensity translate those causes into time, operations, and bytes. The four-step workflow screens, confirms, acts on, and scores them across the four lighthouse regimes (compute-bound, bandwidth-bound, capacity-bound, and power-bound) and the overhead-bound regime that a deployment choice such as batch-one serving can create. The anti-patterns and the H100 case studies show what skipping or following that workflow costs. Scaling laws and the information roofline then separate observed improvement trajectories from data-quality limits. Use the framework as a loop rather than as a label.

**Key Takeaways: Where to look first**

- Begin with cross-axis hypotheses; a symptom rarely identifies its cause.
- Translate each hypothesis into the relevant iron-law term, or the capacity or power precondition, and a measurement that could falsify it.
- Use arithmetic intensity and the scorecard to identify the limiting constraint, not to assign universal grades.
- Apply the corresponding lever and remeasure end to end; a local gain that leaves the limiting term unchanged is not a system improvement.

^callout-takeaways--1-1-e48ac2b4

Back to top

## Source References

^source-references

Williams, Samuel, Andrew Waterman, and David Patterson. 2009. “Roofline: An Insightful Visual Performance Model for Multicore Architectures.” *Communications of the ACM* 52 (4): 65–76. https://doi.org/10.1145/1498765.1498785.

^ref-williams2009

Chowdhery, Aakanksha, Sharan Narang, Jacob Devlin, Maarten Bosma, Gaurav Mishra, Adam Roberts, Paul Barham, et al. 2022. “PaLM: Scaling Language Modeling with Pathways.” *arXiv Preprint arXiv:2204.02311*.

^ref-chowdhery2022palm

Choquette, Jack. 2023. “NVIDIA Hopper H100 GPU: Scaling Performance.” *IEEE Micro* 43 (3): 9–17. https://doi.org/10.1109/mm.2023.3256796.

^ref-choquette2023

Kaplan, Jared, Sam McCandlish, Tom Henighan, Tom B. Brown, Benjamin Chess, Rewon Child, Scott Gray, Alec Radford, Jeffrey Wu, and Dario Amodei. 2020. “Scaling Laws for Neural Language Models.” *ArXiv Preprint* abs/2001.08361.

^ref-kaplan2020scaling

Hoffmann, Jordan, Sebastian Borgeaud, Arthur Mensch, Elena Buchatskaya, Trevor Cai, Eliza Rutherford, Diego de Las Casas, et al. 2022. “Training Compute-Optimal Large Language Models.” *Advances in Neural Information Processing Systems (NeurIPS)* 35: 30016–30. https://doi.org/10.52202/068431-2176.

^ref-hoffmann2022chinchilla

Goodfellow, Ian, Yoshua Bengio, and Aaron Courville. 2016. *Deep Learning*. MIT Press.

^ref-goodfellow2016deep

## Footnotes

^footnotes

<sup>1</sup> **Arithmetic intensity**: This book uses the term for floating-point operations per byte transferred. Williams et al. ([[05 Reference/Volume I - Foundations/V1 The D·A·M Taxonomy#^ref-williams2009|2009]]) calls the measured DRAM quantity *operational intensity* in the Roofline Model. Comparing the workload ratio with the hardware ridge point (${R_{\text{peak}}}/{\text{BW}}$) gives an upper-bound diagnosis of bandwidth- versus compute-bound execution.

^fn1

<sup>2</sup> **MFU**: The ratio of achieved model FLOP/s to the hardware’s theoretical peak FLOP/s, introduced in the PaLM paper ([[05 Reference/Volume I - Foundations/V1 The D·A·M Taxonomy#^ref-chowdhery2022palm|Chowdhery et al. 2022]]). Unlike raw accelerator utilization (which counts any work the accelerator performs), MFU measures model computation rate relative to peak hardware throughput, so non-model work and system overhead are not counted as achieved model FLOPs. **[[01 Books/Volume I - Foundations/02 Development/08 Model Training/V1-08.06 Identifying Bottlenecks#^sec-model-training-identifying-bottlenecks-f57f|Identifying Bottlenecks]]** develops MFU as a training diagnostic.

^fn2

<sup>3</sup> **Scaling laws**: Empirical relationships, typically power laws with a fitted negative exponent, that predict model loss as a function of dataset size, parameter count, or compute budget. Kaplan et al. ([[05 Reference/Volume I - Foundations/V1 The D·A·M Taxonomy#^ref-kaplan2020scaling|2020]]) studied these relationships for neural language models at OpenAI; Hoffmann et al. ([[05 Reference/Volume I - Foundations/V1 The D·A·M Taxonomy#^ref-hoffmann2022chinchilla|2022]]) later estimated the compute-optimal training trade-off for its studied dense language-model regime. **[[01 Books/Volume I - Foundations/03 Optimization/09 Data Selection/V1-09.03 Measuring Data Value#^sec-data-selection-computeoptimal-frontier-24ba|The compute-optimal frontier]]** develops the compute-optimal frontier and its data-starvation diagnostic in detail.

^fn3

<sup>4</sup> **Bayes error rate**: The lowest achievable error rate under 0–1 loss for any classifier on a given data distribution, determined by class priors and the overlap between class-conditional distributions ([[05 Reference/Volume I - Foundations/V1 The D·A·M Taxonomy#^ref-goodfellow2016deep|Goodfellow et al. 2016]]). No amount of data, parameters, or compute can reduce error below this theoretical floor.

^fn4

## Source

[Repository Source](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/books/vol1/backmatter/appendix_dam.qmd) · [Original License](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/LICENSE.md)

[Rendered Reading Snapshot](https://mlsysbook.ai/vol1/backmatter/appendix_dam.html#sec-appdx-dam-taxonomy). Rendering provenance is recorded in the import manifest.
