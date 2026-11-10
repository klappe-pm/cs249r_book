---
title: V2 Reliability Foundations
type: Reference
volume: 2
chapter: 0
publication_status: Preview
source_repository: https://github.com/klappe-pm/cs249r_book
source_commit: de87c0103806d7bfb1c677dbb77a2b92fa00c298
source_path: books/vol2/backmatter/appendix_reliability.qmd
source_anchor: sec-appdx-reliability-foundations
source_mode: Source-Correlated Published HTML
tags:
- Type/Reference
- Book/Volume_2
rendered_source_url: https://mlsysbook.ai/vol2/backmatter/appendix_reliability.html
---

# V2 Reliability Foundations

[[Home|Home]] · [[01 Books/Volume II - Scaling/Volume 2 Overview|Volume Overview]]

^sec-appdx-reliability-foundations

Individual accelerators fail rarely, but scaling to thousands of nodes multiplies component failure rates until interruption becomes a continuous operating condition. At cluster scale, mean time between failures (MTBF) drops from years to hours, turning failure recovery into a core execution path. This appendix collects the quantitative reliability calculations behind the book’s fault-tolerance chapters, deriving failure probabilities, Young-Daly optimal checkpoint intervals, and availability stacking models. In C$^3$ terms, it develops the coordination axis, where checkpointing, recovery, and availability determine how much of the fleet’s compute and communication becomes useful work.

## How to Use This Appendix

^how-to-use-this-appendix

This appendix serves as a reference for moving from intuition (“failures happen more often at scale”) to quantitative engineering decisions (“how often should one checkpoint?” or “how many spare nodes are needed?”). It translates component-level reliability metrics into cluster-wide checkpoint cadences and availability bounds.

The worked examples in this appendix use a 10,000-GPU training fleet, a larger variation on the 1,024-GPU Archetype A reference cluster, unless noted otherwise. The questions below map common operational problems to the sections that develop their analytical models:

- **“How often will something fail?”** Start with [[05 Reference/Volume II - Scaling/V2 Reliability Foundations#^sec-appdx-reliability-foundations-failure-probability|section 1.1]] and the MTBF cascade in [[05 Reference/Volume II - Scaling/V2 Reliability Foundations#^sec-appdx-reliability-foundations-mtbf-cascade|section 1.1.3]].
- **“Where does the $1/{N}$ come from?”** The probability tools in [[05 Reference/Volume II - Scaling/V2 Reliability Foundations#^sec-appdx-reliability-foundations-probability-tools|section 1.1.1]] derive it from independent exponential lifetimes.
- **“How often to checkpoint?”** Use the Young-Daly model in [[05 Reference/Volume II - Scaling/V2 Reliability Foundations#^sec-appdx-reliability-foundations-young-daly|section 1.2.1]] and the worked example in [[05 Reference/Volume II - Scaling/V2 Reliability Foundations#^sec-appdx-reliability-foundations-worked-example|section 1.2.3]].
- **“How much time is lost to recovery?”** See the recovery anatomy in [[05 Reference/Volume II - Scaling/V2 Reliability Foundations#^sec-appdx-reliability-foundations-recovery-anatomy|section 1.3.1]] and the runtime goodput loss in [[05 Reference/Volume II - Scaling/V2 Reliability Foundations#^sec-appdx-reliability-foundations-goodput|section 1.3.2]].
- **“When to use redundancy vs. checkpointing?”** Compare strategies in [[05 Reference/Volume II - Scaling/V2 Reliability Foundations#^sec-appdx-reliability-foundations-strategies|section 1.4.1]] and availability stacking in [[05 Reference/Volume II - Scaling/V2 Reliability Foundations#^sec-appdx-reliability-foundations-availability|section 1.4.2]].
- **“What if checkpoints are not cheap relative to MTBF?”** Use the higher-order interval in [[05 Reference/Volume II - Scaling/V2 Reliability Foundations#^sec-appdx-reliability-daly-2nd-order|section 1.5]].
- **“How can one flipped bit derail training?”** See the silent data corruption model in [[05 Reference/Volume II - Scaling/V2 Reliability Foundations#^sec-appdx-reliability-sdc-perturbation|section 1.6]].

## Failure Probability at Scale

^sec-appdx-reliability-foundations-failure-probability

Consider a training run on a 10,000-GPU cluster running for 30 days. The probability that at least one modeled node component fails during that time is effectively 100 percent. That answer determines whether the system needs fault tolerance as a core design requirement or as an optional feature.

Individual hardware components are reliable. A data center-grade GPU operates for tens of thousands of hours before failing. The physics of large-scale systems, however, works against reliability: every additional component is another opportunity for failure, and the aggregate failure rate scales linearly with component count. Component-level failure rates aggregate systematically into cluster-wide failure predictions.

### Probability Tools for Failure Analysis

^sec-appdx-reliability-foundations-probability-tools

A 10,000-GPU training job requires every accelerator and network card to stay healthy at the same time. At a 99.99 percent per-device daily survival rate, the job still has less than a 40 percent chance of finishing a single day uninterrupted. Four results from elementary probability carry that failure arithmetic throughout this book. Each assumes that components fail independently; correlated failures, such as a shared power feed or a common software bug, violate that assumption and must be modeled separately.

The first is the product rule for independent events. If a job needs all ${N}$ of its components and each is available with probability ${A_{\text{component}}}$, the job’s components are all available with probability

$$
{A_{\text{all}}}= {A_{\text{component}}}^{{N}} \approx e^{-{N}(1-{A_{\text{component}}})} \quad \text{for } {A_{\text{component}}} \text{ close to } 1 \tag{1}
$$

^eq-reliability-all-available

[[05 Reference/Volume II - Scaling/V2 Reliability Foundations#^eq-reliability-all-available|Equation 1]] is the **reliability collapse** behind the reliability gap in **[[01 Books/Volume II - Scaling/00 Introduction/01 Introduction/V2-01.05 Constraints of Scale#^sec-vol2-introduction-reliability-gap|The reliability gap]]**. A per-component availability that looks excellent in isolation decays exponentially in ${N}$.

The second is its complement, the probability that at least one of ${N}$ independent events occurs when each has probability ${p}$:

$$
\Pr(\text{at least one}) = 1-(1-{p})^{{N}} \approx {N} {p}\quad \text{when } {N} {p}\ll 1 \tag{2}
$$

^eq-reliability-at-least-one

The linear approximation in [[05 Reference/Volume II - Scaling/V2 Reliability Foundations#^eq-reliability-at-least-one|equation 2]] holds only while ${N} {p}$ is small; as ${N}$ grows, the probability approaches 1. This arithmetic is why one slow worker paces a large synchronous job. A delay that rarely strikes any one worker strikes some worker of a large synchronous job on almost every step.

The third is the exponential lifetime model. A component with constant failure rate ${\lambda}$ survives to time ${t}$ with probability $e^{-{\lambda} {t}}$ and has mean time to failure $1/{\lambda}$. The model is memoryless. A component that has run for a year is no more likely to fail in the next hour than a new one, which is why it describes the useful-life phase and not burn-in or wear-out. The earliest of ${N}$ independent exponential failures is itself exponential with rate ${N}{\lambda}$, so the time to the first failure among ${N}$ identical components has mean $1/({N}{\lambda})$. That single fact is the origin of the $1/{N}$ scaling of system MTBF in [[05 Reference/Volume II - Scaling/V2 Reliability Foundations#^eq-mtbf-cluster|equation 5]].

The fourth is the Poisson count. Under the same model, the number of failures in an interval ${T}$ is Poisson distributed with mean ${T}/{\text{MTBF}}$, so the probability of no failure is $e^{-{T}/{\text{MTBF}}}$. [[05 Reference/Volume II - Scaling/V2 Reliability Foundations#^eq-failure-probability|Equation 6]] below is the complement of that event, and the expected number of failures per day in [[05 Reference/Volume II - Scaling/V2 Reliability Foundations#^tbl-mtbf-cluster|table 2]] is the Poisson mean.

### Component Failure Rates

^sec-appdx-reliability-foundations-component-rates

A single data center GPU fails roughly once every 5.7 years of continuous operation, a rate of about 0.00002 failures per hour that is too small to write conveniently in engineering tables. Reliability engineers therefore characterize components using two complementary metrics. The **failure in time (FIT)** rate counts failures per $10^9$ device-hours of operation, a unit chosen because individual components fail so rarely that failures-per-hour would produce inconveniently small numbers. The reciprocal quantity, **mean time to failure (MTTF)**, calculates average lifetime in hours ([[05 Reference/Volume II - Scaling/V2 Reliability Foundations#^eq-mttf-from-fit|equation 3]]):

$$
{\text{MTTF}} = \frac{10^9}{\text{FIT}} \tag{3}
$$

^eq-mttf-from-fit

Reference FIT rates and MTTF values ([[05 Reference/Volume II - Scaling/V2 Reliability Foundations#^tbl-component-fit|table 1]]) characterize component reliability in typical GPU training nodes, grounded in large-fleet and warehouse-scale experience ([[05 Reference/Volume II - Scaling/V2 Reliability Foundations#^ref-kokolis2025|Kokolis et al. 2025]]; [[05 Reference/Volume II - Scaling/V2 Reliability Foundations#^ref-zu2024tpuv4|Zu et al. 2024]]; [[05 Reference/Volume II - Scaling/V2 Reliability Foundations#^ref-barroso2019|Barroso et al. 2019]]). These values assume the steady-state “useful life” phase of the bathtub curve, where the failure rate is approximately constant, dominated neither by infant mortality (early life) nor by wear-out (end of life) ([[05 Reference/Volume II - Scaling/V2 Reliability Foundations#^ref-klutke2003|Klutke et al. 2003]]).

| **Component**     | **FIT rate** |   **MTTF**    | **MTTF (years)** |  **Typical failure mode**   |
|:------------------|:------------:|:-------------:|:----------------:|:---------------------------:|
| **GPU**           |    20,000    | 50,000 hours  |    5.7 years     | Die defect, thermal fatigue |
| **HBM**           |    5,000     | 200,000 hours |    22.8 years    | Bit-flip accumulation, TSV  |
| **NIC**           |   6,666.7    | 150,000 hours |    17.1 years    |   Transceiver degradation   |
| **PSU**           |    10,000    | 100,000 hours |    11.4 years    |       Capacitor aging       |
| **PCIe Switch**   |    5,000     | 200,000 hours |    22.8 years    |  Solder joint, ESD damage   |
| **Optical Cable** |    20,000    | 50,000 hours  |    5.7 years     | Fiber bend, connector wear  |
| **ToR Switch**    |   3,333.3    | 300,000 hours |    34.2 years    |  ASIC failure, fan bearing  |

Table 1: **Component Failure Rates**: Order-of-magnitude reference FIT/MTTF in the steady-state useful-life phase. Informed by large-GPU research-cluster analysis ([[05 Reference/Volume II - Scaling/V2 Reliability Foundations#^ref-kokolis2025|Kokolis et al. 2025]]), TPUv4 supercomputer resiliency and operations ([[05 Reference/Volume II - Scaling/V2 Reliability Foundations#^ref-zu2024tpuv4|Zu et al. 2024]]), and warehouse-scale machine design ([[05 Reference/Volume II - Scaling/V2 Reliability Foundations#^ref-barroso2019|Barroso et al. 2019]]).

^tbl-component-fit

Each component in isolation appears highly reliable; a GPU lasts 5.7 years on average. The difficulty begins with how a node behaves when many such components operate simultaneously.

### The MTBF Cascade

^sec-appdx-reliability-foundations-mtbf-cascade

If one GPU or one network card inside an eight-GPU server fails during a synchronous collective, the entire server drops out of the training step just as surely as if its motherboard had lost power. The following model therefore treats a compute node as a series system, in which any modeled component failure interrupts it. A component enters the sum only when its failure alone stops the node, so redundant power supplies, spare links, and recoverable device errors stay out of it. For independent components with constant failure rates, [[05 Reference/Volume II - Scaling/V2 Reliability Foundations#^eq-mtbf-node|equation 4]] sums the individual rates into the node-level failure rate:

$$
\frac{1}{{\text{MTBF}_{\text{node}}}} = \frac{{G_{\text{node}}}}{{\text{MTTF}_{\text{GPU}}}} + \frac{{n_{\text{nic}}}}{{\text{MTTF}_{\text{nic}}}} + \frac{{n_{\text{psu}}}}{{\text{MTTF}_{\text{psu}}}} + \cdots \tag{4}
$$

^eq-mtbf-node

Think of each component as a ticking clock counting down to failure. A DGX H100 node with 8 GPUs and 8 network interface cards (NICs) has 16 independent clocks, and the node fails when the first clock reaches zero. More clocks mean a shorter expected wait. The node’s 6 power supply units (PSUs) add no clocks. They run as a 4+2 redundant set, so the node keeps full performance with 2 of them failed, and a failed unit is normally replaced long before enough others fail to stop the node.

For a cluster of ${N_{\text{nodes}}}$ identical nodes, the same series-system logic applies one level up. As [[05 Reference/Volume II - Scaling/V2 Reliability Foundations#^eq-mtbf-cluster|equation 5]] shows, cluster MTBF divides the single-node MTBF by the number of nodes:

$$
{\text{MTBF}_{\text{system}}} = \frac{{\text{MTBF}_{\text{node}}}}{{N_{\text{nodes}}}} \tag{5}
$$

^eq-mtbf-cluster

Reliability degrades linearly with component count at each level, and the levels compound, which is the **MTBF cascade**. A node with 4,687.5 hours MTBF sounds reliable. A cluster of 1,250 such nodes has an MTBF of 3.75 hours, so a failure every few hours is the expected steady state. [[05 Reference/Volume II - Scaling/V2 Reliability Foundations#^tbl-mtbf-cluster|Table 2]] carries that arithmetic across fleet sizes, with aggregate MTBF falling in inverse proportion to GPU count.

| **Cluster GPUs** | **Nodes** | **Cluster MTBF** | **Expected failures/day** |
|:-----------------|:---------:|:----------------:|:-------------------------:|
| **256**          |    32     |   146.5 hours    |            0.2            |
| **1,024**        |    128    |    36.6 hours    |            0.7            |
| **2,048**        |    256    |    18.3 hours    |            1.3            |
| **8,192**        |   1,024   |    4.6 hours     |            5.2            |
| **10,000**       |   1,250   |    3.8 hours     |            6.4            |
| **100,000**      |  12,500   |   22.5 minutes   |            64             |

Table 2: **Cluster MTBF by Scale**: As cluster size grows, the aggregate MTBF shrinks proportionally. At 10,000 GPUs, failures occur every few hours; at 100,000 GPUs, they occur continuously. Node configuration (DGX H100): 8 GPUs and 8 NICs per node in the series sum; its 6 PSUs are 4+2 redundant and add no term.

^tbl-mtbf-cluster

The transition from hundreds of GPUs to tens of thousands is a qualitative regime shift. About 6.1 days pass between failures at 256 GPUs. A 10,000-GPU cluster, in contrast, expects multiple failures per shift. At 100,000 GPUs, failures become a continuous background condition in which the system is never fully healthy.

### Probability of Failure During a Job

^sec-appdx-reliability-foundations-job-failure

A cluster MTBF of a few hours tells an operator how often nodes drop out on average, but a training team scheduling a 7-day or 30-day run needs the probability that at least one failure will interrupt that fixed window. Under the exponential failure model (constant failure rate), [[05 Reference/Volume II - Scaling/V2 Reliability Foundations#^eq-failure-probability|equation 6]] gives the probability of at least one failure during a job of duration ${T_{\text{job}}}$ as the complement of the Poisson zero-failure probability over that window:

$$
\Pr(\geq 1\ \text{failure}) = 1 - e^{-{T_{\text{job}}}/{\text{MTBF}}} \tag{6}
$$

^eq-failure-probability

When ${T_{\text{job}}}\gg {\text{MTBF}}$, this probability approaches 1 rapidly, and it does so sooner on a larger cluster, whose MTBF is shorter ([[05 Reference/Volume II - Scaling/V2 Reliability Foundations#^tbl-failure-prob|table 3]]).

| **Cluster GPUs** | **1 day (24 h)** | **1 week (168 h)** | **30 days (720 h)** |
|:-----------------|:----------------:|:------------------:|:-------------------:|
| **256**          |      15.1%       |       68.2%        |        99.3%        |
| **1,024**        |      48.1%       |       99.0%        |      \> 99.9%       |
| **2,048**        |      73.0%       |      \> 99.9%      |      \> 99.9%       |
| **8,192**        |      99.5%       |      \> 99.9%      |      \> 99.9%       |
| **10,000**       |      99.8%       |      \> 99.9%      |      \> 99.9%       |
| **100,000**      |     \> 99.9%     |      \> 99.9%      |      \> 99.9%       |

Table 3: **Probability of at Least One Failure**: For large clusters and multi-day jobs, failure is a near-certainty. Any system operating in the bottom-right region of this table must treat fault tolerance as a core design requirement, not an optimization.

^tbl-failure-prob

For any cluster above a few thousand GPUs running jobs longer than a day, the probability of experiencing at least one failure is effectively 100 percent. This is why **[[01 Books/Volume II - Scaling/02 Distributed ML/07 Fault Tolerance/V2-07 Fault Tolerance#^sec-fault-tolerance-reliability|Fault Tolerance]]** treats fault tolerance as an architectural requirement rather than a defensive measure.

The exponential failure model assumes a constant failure rate, which holds during the steady-state useful-life phase. During burn-in (first few hundred hours) and wear-out (approaching end-of-life), failure rates are higher. In practice, fleet operators observe that newly deployed nodes show 2–3$\times$ higher failure rates in their first week, making burn-in testing essential before admitting nodes to production clusters. Because failures will interrupt long training jobs, the practical question is how to minimize the lost progress.

------------------------------------------------------------------------

## Checkpoint Optimization

^sec-appdx-reliability-foundations-checkpoint-optimization

On a 10,000-GPU cluster that fails every few hours, pausing all 10,000 accelerators to flush a multi-terabyte state snapshot to shared storage stalls training, yet spacing snapshots hours apart sacrifices thousands of GPU-hours of progress whenever a node drops out. Choosing a checkpoint cadence therefore trades guaranteed write overhead against expected rework after a crash ([[05 Reference/Volume II - Scaling/V2 Reliability Foundations#^ref-young1974|Young 1974]]; [[05 Reference/Volume II - Scaling/V2 Reliability Foundations#^ref-daly2006|Daly 2006]]).

### The Young-Daly Model

^sec-appdx-reliability-foundations-young-daly

During a synchronous checkpoint, writing state to storage takes time ${T_{\text{write}}}$ (the **checkpoint cost**), during which no useful training occurs. Extending the interval between checkpoints amortizes that pause, but a failure that arrives at a random point inside the interval destroys on average half the interval’s work. [[05 Reference/Volume II - Scaling/V2 Reliability Foundations#^eq-young-daly|Equation 7]] states the **Young-Daly formula** that minimizes the sum of those two expected losses:

$$
{T^\ast_{\text{ckpt}}} = \sqrt{2 \times {T_{\text{write}}} \times {\text{MTBF}_{\text{system}}}} \tag{7}
$$

^eq-young-daly

where ${T_{\text{write}}}$ is the checkpoint write time in seconds and ${\text{MTBF}_{\text{system}}}$ is the cluster or job-level system MTBF in seconds.

The intuition behind [[05 Reference/Volume II - Scaling/V2 Reliability Foundations#^eq-young-daly|equation 7]] is geometric-mean-like. When checkpoints are cheap relative to the MTBF (${T_{\text{write}}} \ll {\text{MTBF}_{\text{system}}}$, the common case), the optimal interval sits between the two time scales. If checkpoints took zero time, the optimal cadence would be every step. If the system never failed, no checkpoints would be required. The square root interpolates between those extremes.

The formula assumes that failures follow an exponential distribution (memoryless property) and that checkpoint cost ${T_{\text{write}}}$ is small compared to ${\text{MTBF}_{\text{system}}}$. Correlated outages, changing hazard rates, long writes, and asynchronous persistence can require a more detailed model. Under the first-order assumptions, evaluating [[05 Reference/Volume II - Scaling/V2 Reliability Foundations#^eq-young-daly|equation 7]] for a concrete model requires only the cluster MTBF and the write duration ${T_{\text{write}}}$, which is set by the serialized state volume and storage bandwidth.

### Checkpoint Sizing

^sec-appdx-reliability-foundations-checkpoint-sizing

Resuming a mixed-precision training run after a node failure requires restoring not only the low-precision weights used in the forward pass, but also the full-precision master weights and optimizer moments accumulated across prior steps, which multiplies the serialized footprint and sets the write time ${T_{\text{write}}}$ in [[05 Reference/Volume II - Scaling/V2 Reliability Foundations#^eq-young-daly|equation 7]]. For common mixed-precision training checkpoints with the adaptive moment estimation (Adam) optimizer, each parameter requires approximately 14 bytes of persistent state:

- 2 bytes for BF16 model weights
- 4 bytes for FP32 master weights
- 4 bytes for FP32 first moment (Adam ${m}$)
- 4 bytes for FP32 second moment (Adam ${v}$)

[[05 Reference/Volume II - Scaling/V2 Reliability Foundations#^eq-checkpoint-size|Equation 8]] aggregates these per-parameter costs into the total checkpoint footprint. The resulting byte volume scales linearly with model parameter count:

$$
\text{Checkpoint Size} = {P}\times 14 \text{ bytes/parameter} \tag{8}
$$

^eq-checkpoint-size

Here, ${P}$ is the number of trainable model parameters whose persistent optimizer and weight state must be serialized. Transient activation buffers and unsharded temporary workspaces are excluded because they are recomputed after restore.

Mixed-precision Adam checkpoint sizing ([[05 Reference/Volume II - Scaling/V2 Reliability Foundations#^tbl-checkpoint-size|table 4]]) demonstrates how state scales from manageable gigabytes to frontier-scale terabytes. Even with high-bandwidth parallel storage, serializing these footprints requires tens of seconds to several minutes per snapshot:

| **Model size** | **Checkpoint size** | **Write time at 100 GB/s** |
|:---------------|:-------------------:|:--------------------------:|
| **7B**         |        98 GB        |           0.98 s           |
| **13B**        |       182 GB        |            2 s             |
| **70B**        |       980 GB        |            10 s            |
| **175B**       |      2,450 GB       |            24 s            |
| **1T**         |      14,000 GB      |           140 s            |

Table 4: **Checkpoint Sizes for Mixed-Precision Adam Training**: Each parameter requires about 14 bytes of persistent checkpoint state (model weights, FP32 master weights, and optimizer moments); gradients are normally transient and recomputed after restore rather than serialized as durable checkpoint state. Write times assume 100 GB/s aggregate storage bandwidth.

^tbl-checkpoint-size

At frontier scale (175B+ parameters), these sizes reach the terabyte range. This makes checkpoint write time a significant cost that directly affects the Young-Daly optimal interval. The checkpoint strategies in **[[01 Books/Volume II - Scaling/02 Distributed ML/07 Fault Tolerance/V2-07 Fault Tolerance#^sec-fault-tolerance-reliability|Fault Tolerance]]** discuss techniques for reducing ${T_{\text{write}}}$ (asynchronous checkpointing, incremental deltas, and distributed storage), all of which improve the Young-Daly result by shrinking the ${T_{\text{write}}}$ factor under the square root.

### Calculating the Optimal Checkpoint Interval

^sec-appdx-reliability-foundations-worked-example

Combining the checkpoint write time with the 10,000-GPU MTBF gives a concrete checkpoint cadence. The worked example below walks through the two-step calculation and shows how doubling the cluster size shifts the optimum.

**Napkin Math 1.1: Young-Daly: 175B model on a 10,000-GPU cluster**

**Setup**: Consider training a 175B-parameter model on a 10,000-GPU cluster. The cluster MTBF is 3.75 hours ([[05 Reference/Volume II - Scaling/V2 Reliability Foundations#^tbl-mtbf-cluster|table 2]]). The checkpoint size is 2,450 GB, and the parallel storage system writes at 100 GB/s.

**Step 1**: Checkpoint write time (${T_{\text{write}}}$).

$$
T_{\text{write}} = \frac{\text{Checkpoint Size}}{\text{Write Bandwidth}} = \frac{2,450 \text{ GB}}{100 \text{ GB/s}} = 24.5 \text{ s}
$$

**Step 2**: Apply the Young-Daly formula ([[05 Reference/Volume II - Scaling/V2 Reliability Foundations#^eq-young-daly|equation 7]]).

$$
T^\ast_{\text{ckpt}} = \sqrt{2 \times T_{\text{write}} \times \text{MTBF}_{\text{system}}} = \sqrt{2 \times 24.5 \text{ s} \times 3.75 \text{ h} \times 3{,}600 \text{ s/h}} = 13.6 \text{ min}
$$

**Interpretation**: The optimal checkpoint interval is approximately 14 minutes. The overhead from checkpointing alone is ${T_{\text{write}}}/{T^\ast_{\text{ckpt}}} \approx$ 3.0 percent of training time.

**Systems insight**: If the cluster were doubled to 20,000 GPUs, the MTBF would halve and the optimal interval would shrink to 9.6 minutes. The system therefore checkpoints more frequently because failures happen more often. Larger clusters are faster but must interrupt themselves more often to protect progress, which is the tension at scale.

When ${T_{\text{write}}}$ approaches ${\text{MTBF}_{\text{system}}}$ (checkpoint cost approaches MTBF), checkpoint and rework overheads become so large that checkpoint/restart alone may fail to maintain useful forward progress, requiring the alternative strategies in [[05 Reference/Volume II - Scaling/V2 Reliability Foundations#^sec-appdx-reliability-foundations-strategies|section 1.4.1]]. Even when ${T_{\text{write}}} \ll {\text{MTBF}_{\text{system}}}$, the Young-Daly cadence prices only the periodic write pause and the average step replay after a fault; a real cluster outage also stalls on failure detection, node replacement, and checkpoint reload before replay can begin.

------------------------------------------------------------------------

## Recovery Budgets

^sec-appdx-reliability-foundations-recovery-budgets

When a node drops out of a 10,000-GPU training step, every surviving accelerator idles while the control plane times out the dead heartbeat, allocates a replacement node, streams terabytes of checkpoint state back into GPU memory, and recomputes the steps lost since the last snapshot. Pricing how much wall-clock capacity those interruptions consume requires decomposing the outage into its constituent phases and translating the total stall time into runtime goodput.

### The Anatomy of Recovery Time

^sec-appdx-reliability-foundations-recovery-anatomy

A single hardware fault triggers four sequential recovery phases between the instant a worker stalls and the moment the job returns to new training steps. [[05 Reference/Volume II - Scaling/V2 Reliability Foundations#^eq-reliability-recovery-time|Equation 9]] sums them into total recovery time:

$$
{T_{\text{recovery}}}= {T_{\text{detect}}}+ {T_{\text{restart}}} + {T_{\text{load}}} + {T_{\text{replay}}} \tag{9}
$$

^eq-reliability-recovery-time

The terms are all durations: failure detection, replacement scheduling, checkpoint reload, and replay of lost training work since the last checkpoint. Their sum is the wall-clock time before the job returns to productive training.

[[05 Reference/Volume II - Scaling/V2 Reliability Foundations#^tbl-recovery-anatomy|Table 5]] breaks recovery into the phases that determine how long the cluster remains below full productivity after a failure. Because detection, rescheduling, checkpoint reload, and replay appear as separate rows, the table shows which operational bottlenecks dominate total downtime.

| **Phase**                         | **Typical duration** | **What happens**                                                                                                                                                                                                   |
|:----------------------------------|:--------------------:|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **${T_{\text{detect}}}$**         |         30 s         | Heartbeat timeout expires; worker declared failed (confirmation adds to the budget in **[[01 Books/Volume II - Scaling/02 Distributed ML/07 Fault Tolerance/V2-07 Fault Tolerance#^sec-fault-tolerance-reliability\|Fault Tolerance]]**) |
| **${T_{\text{restart}}}$**        |         60 s         | Replacement node allocated from spare pool                                                                                                                                                                         |
| **${T_{\text{load}}}$**           |        24.5 s        | Checkpoint read from storage into GPU memory                                                                                                                                                                       |
| **${T_{\text{replay}}}$**         |       ~6.8 min       | Recompute training steps since last checkpoint                                                                                                                                                                     |
| **Total ${T_{\text{recovery}}}$** |        ~9 min        | System fully productive again                                                                                                                                                                                      |

Table 5: **Recovery Time Breakdown**: Each phase contributes to the total time between failure and full-speed resumption. For the 10,000-GPU, 175B-model scenario, replay dominates because it recomputes work lost since the last checkpoint.

^tbl-recovery-anatomy

In this sequence, replay time ${T_{\text{replay}}}$ typically dominates and is controlled directly by the checkpoint interval, since on average half the interval must be replayed. This creates a reinforcing loop with the Young-Daly formula. Shorter intervals mean less replay but more checkpoint overhead, and the formula finds the minimum of this sum. The other phases offer distinct engineering levers. More aggressive heartbeat intervals shorten ${T_{\text{detect}}}$, at the cost of false positives. Preallocated hot spare nodes shorten ${T_{\text{restart}}}$ through the fleet orchestration policies covered in **[[01 Books/Volume II - Scaling/02 Distributed ML/08 Fleet Orchestration/V2-08 Fleet Orchestration#^sec-fleet-orchestration|Fleet Orchestration]]**. Higher storage bandwidth or smaller checkpoints shorten ${T_{\text{load}}}$, which motivates the compression and sharding techniques discussed in **[[01 Books/Volume II - Scaling/02 Distributed ML/07 Fault Tolerance/V2-07 Fault Tolerance#^sec-fault-tolerance-reliability|Fault Tolerance]]**.

### Runtime Goodput Under Failures

^sec-appdx-reliability-foundations-goodput

Every minute a cluster spends writing a periodic snapshot or executing the four-phase recovery pipeline of [[05 Reference/Volume II - Scaling/V2 Reliability Foundations#^tbl-recovery-anatomy|table 5]] is billed wall-clock allocation that advances the final model by zero training steps. Comparing the **committed step rate** (the steps a checkpoint retains for the final model) against the **fault-free step rate** (the rate the configured cluster could sustain without checkpoint or recovery interruptions) defines the runtime goodput of a job whose only losses are checkpoints and failures:

$$
{\eta_{\text{runtime}}} \approx \frac{\text{Committed Useful-Step Rate}}{\text{Fault-Free Step Rate}} \approx \frac{{T_{\text{useful}}}}{{T_{\text{wall}}}}
$$

**[[01 Books/Volume II - Scaling/03 The Fleet in Production/09 Fleet Efficiency/V2-09.06 Runtime Goodput#^sec-performance-engineering-runtime-goodput|Runtime Goodput]]** defines runtime goodput as one factor of ML goodput and also charges startup and input stalls to it, which this appendix does not model. The modeled gap between the two rates comes from two sources:

1.  **Checkpoint overhead** ($\sim$ 3.0 percent): Training pauses during each checkpoint write.
2.  **Recovery and rework overhead** ($\sim$ 3.9 percent): Time lost to detection, rescheduling, reloading, and replaying work discarded after each failure.

At 10,000-GPU scale, failures and checkpointing together can consume a substantial fraction of wall time. If they consume a fraction ${f_{\text{overhead}}}$, a fixed amount of useful work takes $1/(1-{f_{\text{overhead}}})$ times its fault-free duration, not merely that duration plus ${f_{\text{overhead}}}$ of it. The fleet orchestration strategies in **[[01 Books/Volume II - Scaling/02 Distributed ML/08 Fleet Orchestration/V2-08 Fleet Orchestration#^sec-fleet-orchestration|Fleet Orchestration]]** and **[[01 Books/Volume II - Scaling/03 The Fleet in Production/12 ML Operations at Scale/V2-12 ML Operations at Scale#^sec-ops-scale|ML Operations at Scale]]** focus on narrowing this gap, because every percentage point of overhead recovered saves dollars and shortens training time.

**Systems Perspective 1.1: The hidden cost of scale**

A common misconception is that doubling cluster size halves training time. In practice, doubling from 5,000 to 10,000 GPUs halves the MTBF and increases failure-related overhead. The effective speedup is less than 2$\times$, and at extreme scale, adding more GPUs can actually increase wall-clock time if the fault tolerance mechanisms cannot keep pace. The serial overhead of recovery bounds the benefit of parallelism, a reliability analogue of Amdahl’s Law.

------------------------------------------------------------------------

## Strategy Selection

^sec-appdx-reliability-foundations-strategy-selection

Pausing a 10,000-GPU batch training job for several minutes to reload a checkpoint and replay lost steps is an acceptable throughput tax, whereas stalling a live inference service for even a few seconds violates user-facing latency contracts and drops production traffic. Because batch training and online serving tolerate interruption on completely different time scales, fleet architectures choose among checkpoint/restart, active redundancy, and elastic resizing according to the recovery latency, spare capacity, and state-management complexity each workload can afford.

### Checkpoint/Restart Vs. Redundancy Vs. Elastic Training

^sec-appdx-reliability-foundations-strategies

Whether a fault-tolerance mechanism can pause the entire job to replay work, must fail over within milliseconds, or must continue on a shrunk allocation when replacement nodes are unavailable separates the three primary recovery architectures. **Checkpoint/restart** periodically saves full system state and rolls back to the last checkpoint after failure. It is the workhorse of large-scale training: conceptually simple, well-understood, and effective when MTBF is much larger than checkpoint cost. The weakness is that recovery requires stopping all workers and replaying lost computation.

**Redundancy** maintains alternate copies of state or computation. A surviving serving replica can take over only when routing, readiness, capacity, and the required request state meet the latency budget. Dedicated duplicate or triplicate execution costs 2–3$\times$ the compute resources; active-active serving instead shares normal traffic across replicas while reserving failover headroom. The justified overhead depends on the workload and recovery contract.

**Elastic training** allows a job to resume with fewer workers when the smaller allocation can hold its state and support its parallel decomposition. Membership changes can still require a coordinated restart and checkpoint reload; TorchElastic restarts the worker group. Workers may be added back when capacity becomes available. The recovery path must restore missing shards, preserve data coverage, and either preserve the effective batch size or validate a changed optimization policy. Elasticity can reduce waiting for replacement capacity, but does not guarantee a shorter interruption. The three strategies trade recovery latency against resource overhead and implementation complexity, and each fits a different workload ([[05 Reference/Volume II - Scaling/V2 Reliability Foundations#^tbl-strategy-comparison|table 6]]).

| **Criterion**         | **Checkpoint/restart** |     **Redundancy**      |        **Elastic training**         |
|:----------------------|:----------------------:|:-----------------------:|:-----------------------------------:|
| **Recovery latency**  |    Minutes (replay)    | Milliseconds (failover) |    Restart and resize dependent     |
| **Resource overhead** | ~3–13% (storage + IO)  |   100–200% (replicas)   | Resize and standby policy dependent |
| **Workload fit**      |    Training (batch)    |    Serving (online)     |       Training (long-running)       |
| **Implementation**    |         Simple         |        Moderate         |               Complex               |
| **State management**  |   Periodic snapshots   | Continuous replication  |     Distributed with resharding     |
| **Failure mode**      |  Job pauses, replays   |   Transparent to user   |     Pause, restore, then resume     |

Table 6: **Fault Tolerance Strategy Comparison**: The latency and overhead ranges are illustrative, not guarantees; elasticity does not by itself require spare capacity. Real-world systems often combine strategies: checkpoint/restart for training with redundancy for the metadata service and checkpoint storage layer.

^tbl-strategy-comparison

### The Availability Stacking Formula

^sec-appdx-reliability-foundations-availability

A single serving replica with 99 percent availability (“two nines”) still accumulates more than 87 hours of downtime per year, far exceeding the outage budget of production inference endpoints that target 99.9 percent (“three nines”) or 99.99 percent (“four nines”) uptime. Redundancy closes that gap by running ${k}$ independent replicas so that surviving instances absorb traffic when one replica fails. Under an idealized model with reliable routing and enough capacity on any surviving replica, the system is unavailable only when all replicas are simultaneously down. [[05 Reference/Volume II - Scaling/V2 Reliability Foundations#^eq-availability-stacked|Equation 10]] captures this, with ${A_{\text{single}}}$ denoting the availability of a single replica and ${k}$ the number of replicas:

$$
{A_{\text{system}}}= 1 - (1 - {A_{\text{single}}})^{k} \tag{10}
$$

^eq-availability-stacked

Evaluating availability stacking with independent replicas ([[05 Reference/Volume II - Scaling/V2 Reliability Foundations#^tbl-availability-stacking|table 7]]) quantifies the gain from adding serving capacity. Each additional independent replica multiplies the outage probabilities together, cutting expected annual downtime by two orders of magnitude per replica at a 99 percent baseline.

| **Replicas ${k}$** | **System availability** | **Nines** | **Downtime per year** |
|:-------------------|:-----------------------:|:---------:|:---------------------:|
| **1**              |         99.00%          |    2.0    |      87.6 hours       |
| **2**              |        99.9900%         |    4.0    |     52.6 minutes      |
| **3**              |        99.9999%         |    6.0    |     31.5 seconds      |

Table 7: **Availability Stacking with Independent Replicas**: Starting from a single-replica availability of 99 percent, each additional replica dramatically reduces expected downtime. Assumes replica failures are independent.

^tbl-availability-stacking

Stacking independent redundant replicas achieves large availability gains. Two replicas that are each available 99 percent of the time yield 99.99 percent availability, reducing annual downtime from 87.6 hours to 52.6 minutes. This is why inference serving systems almost universally deploy multiple replicas behind a load balancer. The cost of an extra replica is small compared to the business value of four-nines availability.

The result, however, depends on the independence assumption. Correlated failures, such as power outages affecting an entire rack, software bugs triggered by a specific input, or network partitions isolating a failure domain, defeat availability stacking. This is why **[[01 Books/Volume II - Scaling/02 Distributed ML/07 Fault Tolerance/V2-07 Fault Tolerance#^sec-fault-tolerance-reliability|Fault Tolerance]]** emphasizes failure domain isolation: replicas must be placed in different racks, different power zones, and ideally different data centers to reduce shared failure modes. Placement alone does not eliminate common software, control-plane, or regional dependencies.

------------------------------------------------------------------------

## Checkpoint Intervals Beyond the First-Order Approximation

^sec-appdx-reliability-daly-2nd-order

When a multi-terabyte checkpoint takes several minutes to flush to shared storage and a 100,000-GPU cluster fails every half hour, the checkpoint write is no longer negligible next to the failure interval. The cluster can then suffer a second crash while still writing the snapshot. Young’s first-order approximation is most accurate when checkpoint time is small relative to the failure interval; Daly’s analysis develops higher-order checkpoint models for regimes where write time is a substantial fraction of MTBF ([[05 Reference/Volume II - Scaling/V2 Reliability Foundations#^ref-daly2006|Daly 2006]]). The simplified renewal model below shows why finite checkpoint time changes the optimum without claiming to reproduce Daly’s full recovery model.

### Renewal Model and Small-Cost Expansion

^sec-appdx-reliability-daly-proof

Suppose a worker fails halfway through flushing a 60-second checkpoint snapshot; the job loses both the training steps computed since the previous snapshot and the 30 seconds spent writing the incomplete checkpoint. Let ${T_{\text{ckpt}}}$ be useful compute time between completed checkpoints. Assume Poisson failures with rate $1/{\text{MTBF}_{\text{system}}}$, identical failure exposure during computation and writing, and zero detection, restart, or reload delay. A failed attempt loses its partial progress and repeats the interval. The expected elapsed time to complete one uninterrupted compute-plus-checkpoint attempt is:

$$
\mathbb{E}[{T_{\text{total}}}] = {\text{MTBF}_{\text{system}}} \left( e^{\frac{{T_{\text{ckpt}}} + {T_{\text{write}}}}{{\text{MTBF}_{\text{system}}}}} - 1 \right) \tag{11}
$$

^eq-daly-total-time

Writing ${T_{\text{att}}}= {T_{\text{ckpt}}} + {T_{\text{write}}}$ for the attempt duration, the renewal equation is $\mathbb{E}[{T_{\text{total}}}] = \mathbb{E}[\min({F}, {T_{\text{att}}})] + \Pr({F}< {T_{\text{att}}}) \mathbb{E}[{T_{\text{total}}}]$, where ${F}$ is an exponential failure time. Since $\mathbb{E}[\min({F}, {T_{\text{att}}})] = {\text{MTBF}_{\text{system}}} (1 - e^{-{T_{\text{att}}}/{\text{MTBF}_{\text{system}}}})$, solving the equation gives [[05 Reference/Volume II - Scaling/V2 Reliability Foundations#^eq-daly-total-time|equation 11]]. Expanding the exponential through its quadratic term then gives the wasted time per completed interval:

$$
\mathbb{E}[{T_{\text{total}}}] - {T_{\text{ckpt}}} \approx {T_{\text{write}}} + \frac{({T_{\text{ckpt}}} + {T_{\text{write}}})^2}{2 \cdot {\text{MTBF}_{\text{system}}}} \tag{12}
$$

^eq-daly-wasted-time

When ${T_{\text{write}}}/{\text{MTBF}_{\text{system}}}$ is small, dividing [[05 Reference/Volume II - Scaling/V2 Reliability Foundations#^eq-daly-wasted-time|equation 12]] by ${T_{\text{ckpt}}}$ leaves the leading terms ${T_{\text{write}}}/{T_{\text{ckpt}}} + {T_{\text{ckpt}}}/(2 \cdot {\text{MTBF}_{\text{system}}})$ of the wasted-time fraction. Minimizing those terms recovers Young’s interval $\sqrt{2 \cdot {T_{\text{write}}} \cdot {\text{MTBF}_{\text{system}}}}$. For finite checkpoint costs, differentiate the unexpanded elapsed time per unit useful work, $\mathbb{E}[{T_{\text{total}}}]/{T_{\text{ckpt}}}$, instead. Its stationary point satisfies:

$$
e^{({T^\ast_{\text{ckpt}}} + {T_{\text{write}}})/{\text{MTBF}_{\text{system}}}}\left(1 - \frac{{T^\ast_{\text{ckpt}}}}{{\text{MTBF}_{\text{system}}}}\right) = 1, \qquad 0 < {T^\ast_{\text{ckpt}}} < {\text{MTBF}_{\text{system}}} \tag{13}
$$

^eq-daly-2nd-order-tau

For positive checkpoint cost, the equivalent derivative numerator

$$
e^{({T_{\text{ckpt}}} + {T_{\text{write}}})/{\text{MTBF}_{\text{system}}}}({T_{\text{ckpt}}}/{\text{MTBF}_{\text{system}}} - 1) + 1
$$

increases from a negative value at zero to a positive value at ${\text{MTBF}_{\text{system}}}$. A one-dimensional root search on [[05 Reference/Volume II - Scaling/V2 Reliability Foundations#^eq-daly-2nd-order-tau|equation 13]] therefore finds the unique optimum of this simplified model.

#### Choosing the Appropriate Approximation

^choosing-the-appropriate-approximation

The first-order formula is a useful planning estimate when writes are short compared with MTBF. When that condition fails, use a model that includes the deployment’s checkpoint semantics, recovery delays, and failure exposure. The numerical condition in [[05 Reference/Volume II - Scaling/V2 Reliability Foundations#^eq-daly-2nd-order-tau|equation 13]] covers only the stated zero-restart-delay renewal model; asynchronous writes and correlated failures require different assumptions. All of these checkpoint and redundancy models assume that a hardware fault announces itself by stopping a worker or failing a health check, yet some of the most damaging faults at fleet scale corrupt tensor values silently without halting execution.

------------------------------------------------------------------------

## Silent Data Corruption in Attention

^sec-appdx-reliability-sdc-perturbation

Not all hardware faults manifest as explicit system crashes, ECC double-bit errors, or kernel traps. **Silent data corruption (SDC)** occurs when single-bit errors or arithmetic logic unit (ALU) faults slip past parity checks, corrupting tensor values in SRAM, high-bandwidth memory (HBM), or register files without triggering an exception. In deep learning workloads, SDC is particularly dangerous because single corrupted floating-point values propagate through non-linear operations, destabilizing fleet-wide training ([[05 Reference/Volume II - Scaling/V2 Reliability Foundations#^ref-dixit2021silent|Dixit et al. 2021]]).

### Exponent Bit Flip Model in FP16

^sec-appdx-reliability-sdc-fp16-model

Consider an IEEE 754 half-precision floating-point (FP16) tensor element representing a query entry ${q_{im}}$, activation value, or weight matrix entry. FP16 allocates 16 total bits: 1 sign bit (${s}$), 5 exponent bits (${e}$), and 10 mantissa bits (${m}$). For a finite normal value, with exponent field $1 \le {e}\le 30$, the scalar ${x}$ represented by the bitstring $({s}, {e}, {m})$ is given by:

$$
{x}= (-1)^{s}\times 2^{{e}- 15} \times \left(1 + \frac{{m}}{1024}\right)
$$

Suppose a cosmic ray, voltage drop, or SRAM failure causes a single bit flip in the most significant exponent bit (bit 14). The exponent value changes from ${e}$ to ${e'} = {e}\pm 16$:

$$
{x_{\text{corrupt}}}= (-1)^{s}\times 2^{({e}\pm 16) - 15} \times \left(1 + \frac{{m}}{1024}\right) = {x}\times 2^{\pm 16}
$$

If both the original and corrupted exponent fields encode finite normal values, the magnitude increases by a factor of $2^{16}=65{,}536$ or decreases by its reciprocal. Exponent fields of zero or all ones instead invoke the subnormal, zero, infinity, or NaN encodings, so the displayed normal-value formula does not apply.

### Softmax Saturation and Error Propagation

^sec-appdx-reliability-sdc-softmax-explosion

When a single-bit exponent flip inflates one query entry by a factor of $65{,}536$, the dot products in that token’s attention row can jump by orders of magnitude and collapse its softmax distribution onto a single key. To trace how that perturbation propagates through one attention head, let ${\mathbf{S}} = {\mathbf{Q}}{\mathbf{K}}^T/\sqrt{{d_{\text{head}}}} \in \mathbb{R}^{{S}\times {S}}$ be the pre-softmax score matrix for sequence length ${S}$ and head dimension ${d_{\text{head}}}$. Suppose an SDC event corrupts one element of token row ${i}$ of the query matrix ${\mathbf{Q}}$, and write the resulting perturbation as ${\Delta}{\mathbf{Q}}$, with only that element nonzero:

$$
{\mathbf{S}_{\text{corrupt}}} = \frac{({\mathbf{Q}}+ {\Delta}{\mathbf{Q}}) {\mathbf{K}}^T}{\sqrt{{d_{\text{head}}}}} = {\mathbf{S}} + {\Delta}{\mathbf{S}}
$$

where ${\Delta}{\mathbf{S}}$ is nonzero only in row ${i}$, with entries ${\Delta} {S_{ij}} = {\Delta}{\mathbf{q}}_i \cdot {\mathbf{k}}_j/\sqrt{{d_{\text{head}}}}$ for the corrupted query row ${\Delta}{\mathbf{q}}_i$ and key row ${\mathbf{k}}_j$. Passing the perturbed score row through the normalization step shifts the entire row’s attention weights. The attention probability perturbation for token row ${i}$ is therefore:

$$
{\Delta}{\mathbf{a}}_i = \operatorname{softmax}\left( {\mathbf{S}_{i, \cdot}} + {\Delta}{\mathbf{S}_{i, \cdot}} \right) - \operatorname{softmax}\left( {\mathbf{S}_{i, \cdot}} \right)
$$

A large corrupted query component can strongly change several attention logits, with the signs and magnitudes determined by the corresponding key components. If one resulting logit exceeds every other logit by an increasingly large margin, the attention distribution approaches a one-hot vector:

$$
\operatorname{softmax}({\mathbf{S}_{i, \cdot}} + {\Delta}{\mathbf{S}_{i, \cdot}})_j \to 1, \qquad \operatorname{softmax}({\mathbf{S}_{i, \cdot}} + {\Delta}{\mathbf{S}_{i, \cdot}})_{k \neq j} \to 0
$$

This is a conditional saturation limit, not an inevitable consequence of a bit flip. The selected key depends on the corrupted logits; a corrupted query element does not identify one corrupted key. The softmax derivative is $\partial {p}_j/\partial {S_{ik}} = {p}_j({\delta}_{jk}-{p}_k)$, which tends toward zero under saturation rather than diverging. Other paths through the computation can still produce large or nonfinite activations and gradients. If invalid state enters the optimizer or a collective, it can propagate across ranks. Detection and recovery must therefore verify state before resuming from a clean checkpoint.

------------------------------------------------------------------------

## Summary

^summary

Failure is a physical constraint of scale. Under independent, constant component failure rates, a single GPU’s mean lifetime is 5.7 years. Yet the modeled 10,000-GPU cluster fails on average every 3.75 hours, because node failure rates sum across components and cluster MTBF divides by node count. The probability that a job is interrupted grows with its duration relative to that interval, so long runs on large clusters must plan for recovery rather than hope to avoid it.

Recovery has four modeled phases (detection, rescheduling, reloading, and replay), and replay is controlled by the checkpoint interval. The Young-Daly formula ${T^\ast_{\text{ckpt}}} = \sqrt{2 {T_{\text{write}}} \, {\text{MTBF}_{\text{system}}}}$ (principle [[01 Books/Volume II - Scaling/02 Distributed ML/V2 Distributed ML Principles#^pri-young-daly|13]]) balances write overhead against expected rework when writes are short compared with the MTBF. [[05 Reference/Volume II - Scaling/V2 Reliability Foundations#^sec-appdx-reliability-daly-2nd-order|Section 1.5]] examines finite-cost effects under a simplified renewal model. Checkpoint/restart suits batch training, redundancy suits latency-sensitive serving, and elastic training sits between them. Independent replicas reduce unavailability multiplicatively, to $(1-{A_{\text{single}}})^{k}$ for ${k}$ replicas, but only to the extent that failure-domain isolation keeps their failures independent.

Back to top

## Source References

^source-references

Klutke, G., P. C. Kiessler, and M. A. Wortman. 2003. “A Critical Look at the Bathtub Curve.” *IEEE Transactions on Reliability* 52 (1): 125–29. https://doi.org/10.1109/tr.2002.804492.

^ref-klutke2003

Kokolis, Apostolos, Michael Kuchnik, John Hoffman, Adithya Kumar, Parth Malani, Faye Ma, Zach DeVito, Shubho Sengupta, Kalyan Saladi, and Carole-Jean Wu. 2025. “Revisiting Reliability in Large-Scale Machine Learning Research Clusters.” *2025 IEEE International Symposium on High Performance Computer Architecture (HPCA)*, 1259–74. https://doi.org/10.1109/hpca61900.2025.00096.

^ref-kokolis2025

Zu, Y., A. Ghaffarkhah, H.-V. Dang, B. Towles, S. Hand, S. Huda, A. Bello, et al. 2024. “Resiliency at Scale: Managing Google’s TPUv4 Machine Learning Supercomputer.” *21st USENIX Symposium on Networked Systems Design and Implementation (NSDI 24)*, 761–74.

^ref-zu2024tpuv4

Barroso, Luiz André, Urs Hölzle, and Parthasarathy Ranganathan. 2019. *The Datacenter as a Computer: Designing Warehouse-Scale Machines*. Synthesis Lectures on Computer Architecture. Springer International Publishing. https://doi.org/10.1007/978-3-031-01761-2.

^ref-barroso2019

Young, John W. 1974. “A First Order Approximation to the Optimum Checkpoint Interval.” *Communications of the ACM* 17 (9): 530–31. https://doi.org/10.1145/361147.361115.

^ref-young1974

Daly, J. T. 2006. “A Higher Order Estimate of the Optimum Checkpoint Interval for Restart Dumps.” *Future Generation Computer Systems* 22 (3): 303–12. https://doi.org/10.1016/j.future.2004.11.016.

^ref-daly2006

Dixit, H. D., S. Pendharkar, M. Beadon, C. Mason, T. Chakravarthy, B. Muthiah, and S. Sankar. 2021. *Silent Data Corruptions at Scale*. arXiv preprint arXiv:2102.11245.

^ref-dixit2021silent

## Source

[Repository Source](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/books/vol2/backmatter/appendix_reliability.qmd) · [Original License](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/LICENSE.md)

[Rendered Reading Snapshot](https://mlsysbook.ai/vol2/backmatter/appendix_reliability.html#sec-appdx-reliability-foundations). Rendering provenance is recorded in the import manifest.
