---
title: V2 System Assumptions
type: Reference
volume: 2
chapter: 0
publication_status: Preview
source_repository: https://github.com/klappe-pm/cs249r_book
source_commit: de87c0103806d7bfb1c677dbb77a2b92fa00c298
source_path: books/vol2/backmatter/appendix_assumptions.qmd
source_anchor: sec-appdx-fleet-system-assumptions
source_mode: Source-Correlated Published HTML
tags:
- Type/Reference
- Book/Volume_2
rendered_source_url: https://mlsysbook.ai/vol2/backmatter/appendix_assumptions.html
---

# V2 System Assumptions

[[Home|Home]] · [[01 Books/Volume II - Scaling/Volume 2 Overview|Volume Overview]]

^sec-appdx-fleet-system-assumptions

Every quantitative example in this book, from cluster failure rates to collective-communication costs to carbon footprint estimates, uses a specific set of assumed numbers: canonical cluster sizes, fabric bandwidths, accelerator reliability, power usage effectiveness, regional carbon intensity, and model utilization ranges. This appendix collects those fleet-scale assumptions in one place so the book’s arithmetic can be audited, checked against chapter napkin math, or substituted into worked examples.

## How to Use This Appendix

^how-to-use-this-appendix

Use this appendix to verify a fleet-scale estimate, swap in an alternative assumption (for example, NDR vs. HDR fabric, Quebec vs. Poland carbon intensity, or a different model FLOPs utilization (MFU)), or identify which numerical constants a chapter calculation depends on. Locate the relevant section, read the `Value` and `Unit` columns, and substitute those values into target arithmetic:

- **When auditing or substituting the baseline 175B training job**: Use [[05 Reference/Volume II - Scaling/V2 System Assumptions#^sec-appdx-fleet-reference-workload|section 1.1]] and the Foundational Hardware Recap section.
- **When scaling a calculation across cluster sizes or network fabrics**: Use the Cluster Reference Configurations, Network and Interconnect Specifications, and Communication Model Parameters sections.
- **When estimating failure frequency or recovery downtime**: Use the component lifetime and recovery tables in the Reliability Assumptions section.
- **When pricing power, water, carbon, or cloud infrastructure**: Use the Sustainability Assumptions and Economic Assumptions sections.
- **When discounting peak FLOP/s to delivered throughput or checking units and sources**: Use the Capacity Planning Assumptions and Unit Conventions sections, and trace each constant’s evidence class in [[05 Reference/Volume II - Scaling/V2 System Assumptions#^sec-appdx-fleet-assumption-provenance|section 1.2]].

Three worked estimates in napkin math [1.1](https://mlsysbook.ai/vol2/backmatter/appendix_assumptions.html#nbk-appendix-assumptions-quick-calculations-constants) combine these constants to calculate cluster failure rate, AllReduce time, and monthly carbon footprint. Hardware and link bandwidths are ceilings unless a chapter states an effective-bandwidth discount; treat the tables as this edition’s shared assumption sheet rather than immutable physical laws.

**Napkin Math 1.1: Quick calculations with these assumptions**

These tables support quick distributed-systems napkin math. Three examples show how several assumptions combine.

**Problem**: How many GPU failures should a large training cluster expect per day?

**Variables**: Use a cluster of 8,192 GPUs and an individual GPU mean time to failure (MTTF) of 50,000 hours.

**Math**: The GPU failure rate is 8,192 GPUs/50,000 hours $\approx$ 0.16 failures/hour, or roughly 3.9 failures/day.

**Result**: This estimate excludes network interface card (NIC), PSU, and cable failures. At 100,000 GPUs, the GPU-only rate is approximately 48 failures/day; adding NIC, PSU, and cable failures, whose MTTFs appear in [[05 Reference/Volume II - Scaling/V2 System Assumptions#^tbl-fleet-mttf|table 6]], raises the operational incident stream further.

**Systems insight**: At fleet scale, failure becomes a continuous background process rather than an exceptional event.

**Problem**: How long does one AllReduce of the gradients of a 70B model take?

**Variables**: Use BF16 parameters and InfiniBand NDR with a nominal byte rate of 50 GB/s per port.

**Math**: The gradient payload is 70 $\times 10^9 \times$ 2 bytes = 140 GB. The ring AllReduce napkin estimate is 2 $\times$ 140 GB/50 GB/s $\approx$ 5.6 s.

**Result**: The collective can consume a significant fraction of a training step.

**Systems insight**: Pipeline and tensor parallelism exist partly to shrink the gradient volume each rank must communicate.

**Problem**: What is the monthly carbon footprint of a 10,000-GPU training run, and how much does the grid change it?

**Variables**: Each H100 draws 700 W at thermal design power (TDP). Use power usage effectiveness (PUE) 1.12, Quebec grid intensity 20 g/kWh, and Poland grid intensity 820 g/kWh.

**Math**: A GPU-only facility-power proxy is 10,000 GPUs $\times$ 700 W $\times$ 1.12 = 7.84 MW. In Quebec, 7.84 MW $\times$ 720 h/month $\times$ 20 g/kWh = 112.9 t CO$_2$ per month.

**Result**: The same run in Poland emits 4,628.7 t, a 41× difference.

**Systems insight**: Grid carbon intensity can dominate the emissions difference for the same hardware, model, and training duration. This proxy excludes host, memory, network, and storage power; total IT power must include those loads before applying PUE for a complete facility estimate.

## Foundational Hardware Recap

^foundational-hardware-recap

Before a fleet calculation can attribute a slowdown to collective communication or stragglers, it needs the compute, memory-bandwidth, capacity, and thermal ceilings of one accelerator in isolation. The book’s primary single-node reference is the NVIDIA H100 ([[05 Reference/Volume II - Scaling/V2 System Assumptions#^tbl-fleet-foundation-recap|table 1]]), and **[[05 Reference/Volume II - Scaling/V2 Single-Machine Foundations#^sec-appdx-dam-taxonomy|The D·A·M Taxonomy]]** derives the single-machine quantities built on these specifications, including the ridge point, the memory hierarchy, and the per-parameter memory of training.

| **Category** |      **Assumption**       |   **Value**   |
|:-------------|:-------------------------:|:-------------:|
| Compute      | H100 FP16 peak throughput |  989 TFLOP/s  |
| Compute      | H100 FP8 peak throughput  | 1,979 TFLOP/s |
| Memory       |      HBM3 bandwidth       |   3.35 TB/s   |
| Memory       |       HBM3 capacity       |     80 GB     |
| Thermal      |            TDP            |     700 W     |

Table 1: **Single-Node H100 Assumptions**: Peak specs from ([[05 Reference/Volume II - Scaling/V2 System Assumptions#^ref-choquette2023|Choquette 2023]]) and NVIDIA H100 documentation. These values provide the ${R_{\text{peak}}}$ and ${\text{BW}}$ baselines for iron-law calculations.

^tbl-fleet-foundation-recap

## Reference Workload

^sec-appdx-fleet-reference-workload

Single-accelerator ceilings turn into concrete multi-node requirements as soon as a model’s training state exceeds the capacity of one H100. Where a chapter needs a concrete training job, it uses the Archetype A running instance that **[[01 Books/Volume II - Scaling/00 Introduction/01 Introduction/V2-01.07 The Fleet Stack and the Lighthouse Archetypes#^sec-introduction-archetype-gpt4llama3-b02f|Archetype A (GPT-4/Llama-3)]]** fixes ([[05 Reference/Volume II - Scaling/V2 System Assumptions#^tbl-fleet-archetype-a|table 2]]), so that any calculation built on that baseline can be audited or rerun with a different model or cluster. A chapter that studies a different model or cluster size says so explicitly.

| **Assumption**                       |            **Value**             |
|:-------------------------------------|:--------------------------------:|
| Model parameters (dense transformer) |               175B               |
| Training state per parameter         |             16 bytes             |
| Total training state                 |              2.8 TB              |
| Resumable checkpoint per parameter   |             14 bytes             |
| Resumable checkpoint size            |             2.45 TB              |
| Reference cluster                    | 1,024 H100 GPUs (128 nodes of 8) |

Table 2: **Archetype A Running Instance**: Mixed-precision training with the Adam optimizer (BF16 weights and gradients, FP32 master weights, two FP32 Adam moments); the checkpoint omits gradients. **[[05 Reference/Volume II - Scaling/V2 Single-Machine Foundations#^sec-appdx-dam-taxonomy-training-memory|Numeric Precision and Training Memory]]** derives the per-parameter bytes. The reference cluster is the book’s 1,024-GPU training cluster; the canonical cluster tiers below illustrate how behavior changes as scale departs from it.

^tbl-fleet-archetype-a

## Cluster Reference Configurations

^cluster-reference-configurations

A communication or fault-tolerance design that works cleanly on the 1,024-GPU Archetype A reference cluster can be unnecessary on a 256-GPU research allocation yet fail completely on a 100,000-GPU hyperscale fleet. Four **canonical cluster tiers** (256, 2,048, 8,192, and 100,000 GPUs) therefore anchor how system behavior changes across scale ([[05 Reference/Volume II - Scaling/V2 System Assumptions#^tbl-fleet-cluster-sizes|table 3]]). They are editorial reference points aligned with common research-lab, production, large-training, and hyperscale fleets, not measurements from a single deployment, and chapters derive node counts, failure rates, and network requirements from these baselines and the assumptions in subsequent tables.

| **Assumption**                        | **Value** | **Unit** |
|:--------------------------------------|:---------:|:--------:|
| Small cluster GPU count (256 tier)    |    256    |   GPUs   |
| Medium cluster GPU count (2,048 tier) |   2,048   |   GPUs   |
| Large cluster GPU count (8,192 tier)  |   8,192   |   GPUs   |
| Mega cluster GPU count (100,000 tier) |  100,000  |   GPUs   |

Table 3: **Canonical Cluster Sizes**: Book-convention tier sizes for fleet-scale examples. At 8 per node: 32 nodes, 256 nodes, 1,024 nodes, and 12,500 nodes. Failure handling shifts from exception to steady state between the 256- and 8,192-GPU tiers ([[05 Reference/Volume II - Scaling/V2 System Assumptions#^ref-kokolis2025|Kokolis et al. 2025]]).

^tbl-fleet-cluster-sizes

The relationship between cluster size and system behavior is not linear. A 256-GPU cluster might go days between failures; a 100,000-GPU cluster experiences multiple failures per hour. This nonlinearity is why **[[01 Books/Volume II - Scaling/02 Distributed ML/07 Fault Tolerance/V2-07 Fault Tolerance#^sec-fault-tolerance-reliability|Fault Tolerance]]** and **[[01 Books/Volume II - Scaling/02 Distributed ML/08 Fleet Orchestration/V2-08 Fleet Orchestration#^sec-fleet-orchestration|Fleet Orchestration]]** treat failure as a continuous background process rather than an exceptional event. The network fabric determines whether gradient synchronization across those nodes takes milliseconds or seconds and whether pipeline parallelism is viable across node boundaries.

## Network and Interconnect Specifications

^network-and-interconnect-specifications

Distributed training and inference are bottlenecked by data movement between machines as often as by computation within them. The network assumptions fix bandwidth and latency for every interconnect tier, from NVLink/PCIe within a node ([[05 Reference/Volume II - Scaling/V2 System Assumptions#^ref-nvidia2017gpu|NVIDIA Corporation 2017]], [[05 Reference/Volume II - Scaling/V2 System Assumptions#^ref-NVIDIA2020|2020]]; [[05 Reference/Volume II - Scaling/V2 System Assumptions#^ref-choquette2023|Choquette 2023]]), through InfiniBand, remote direct memory access (RDMA), and Ethernet fabrics ([[05 Reference/Volume II - Scaling/V2 System Assumptions#^ref-infiniband2000spec|InfiniBand Trade Association 2000]]; [[05 Reference/Volume II - Scaling/V2 System Assumptions#^ref-gangidi2024rdma|Gangidi et al. 2024]]; [[05 Reference/Volume II - Scaling/V2 System Assumptions#^ref-nvidia2026quantumX800|NVIDIA 2026]]; [[05 Reference/Volume II - Scaling/V2 System Assumptions#^ref-ethernetAlliance2025roadmap|Ethernet Alliance 2025]]), to the speed-of-light WAN floor (physics identity).

### Intra-Node Interconnects

^intra-node-interconnects

Splitting a single transformer layer across eight GPUs inside a server requires an all-reduce on every forward and backward pass, which is viable at hundreds of gigabytes per second over NVLink but stalls over a host PCIe bus. Those intra-node bandwidths and latencies ([[05 Reference/Volume II - Scaling/V2 System Assumptions#^tbl-fleet-intra-node|table 4]]) determine which fine-grained parallelism strategies must remain within the node boundary.

| **Assumption**                  | **Value** | **Unit** |
|:--------------------------------|:---------:|:--------:|
| NVLink bandwidth (V100)         |    300    |   GB/s   |
| NVLink bandwidth (A100)         |    600    |   GB/s   |
| NVLink bandwidth (H100)         |    900    |   GB/s   |
| PCIe Gen3 bandwidth (V100 host) |   15.75   |   GB/s   |
| PCIe Gen4 bandwidth (A100 host) |    32     |   GB/s   |
| PCIe Gen5 bandwidth (H100 host) |    64     |   GB/s   |
| NVLink one-way latency          |    500    |    ns    |
| PCIe Gen5 one-way latency       |   1000    |    ns    |

Table 4: **Intra-Node Interconnect Bandwidth and Latency**: NVLink/PCIe peaks from vendor documentation ([[05 Reference/Volume II - Scaling/V2 System Assumptions#^ref-nvidia2017gpu|NVIDIA Corporation 2017]], [[05 Reference/Volume II - Scaling/V2 System Assumptions#^ref-NVIDIA2020|2020]]; [[05 Reference/Volume II - Scaling/V2 System Assumptions#^ref-choquette2023|Choquette 2023]]). The displayed NVLink rates are bidirectional aggregates; PCIe rates are per direction. Comparing like-for-like per-direction rates gives an NVLink/PCIe ratio of 7–10×, informing placement of communication-intensive tensor parallelism.

^tbl-fleet-intra-node

### Inter-Node Interconnects

^inter-node-interconnects

Once data crosses the node boundary, bandwidth drops by an order of magnitude and latency increases by 5–10$\times$. This cliff shapes every decision about parallelism strategy. Operations that require frequent, fine-grained communication (tensor parallelism) stay within the node, while operations with coarser communication patterns (data parallelism, pipeline parallelism) span nodes. To accommodate the different conventions used across chapters, [[05 Reference/Volume II - Scaling/V2 System Assumptions#^tbl-fleet-inter-node|table 5]] catalogs both the bit-rate and byte-rate forms of each fabric.

| **Assumption**                           | **Value** | **Unit** |
|:-----------------------------------------|:---------:|:--------:|
| InfiniBand HDR link bandwidth (bit rate) |    200    |   Gb/s   |
| InfiniBand HDR bandwidth (byte rate)     |    25     |   GB/s   |
| InfiniBand NDR link bandwidth (bit rate) |    400    |   Gb/s   |
| InfiniBand NDR bandwidth (byte rate)     |    50     |   GB/s   |
| InfiniBand XDR bandwidth (byte rate)     |    100    |   GB/s   |
| 400 GbE bandwidth (byte rate)            |    50     |   GB/s   |
| 800 GbE bandwidth (byte rate)            |    100    |   GB/s   |
| 100 GbE RoCE bandwidth (byte rate)       |   12.5    |   GB/s   |
| InfiniBand one-way latency               |   5000    |    ns    |

Table 5: **Inter-Node Network Bandwidth and Latency**: Fabric link rates from ([[05 Reference/Volume II - Scaling/V2 System Assumptions#^ref-infiniband2000spec|InfiniBand Trade Association 2000]]) and product-line specifications. The 9× NVLink-vs-NDR gap explains topology-aware parallelism (**[[01 Books/Volume II - Scaling/02 Distributed ML/05 Collective Communication/V2-05 Collective Communication#^sec-collective-communication|Collective Communication]]**, **[[01 Books/Volume II - Scaling/02 Distributed ML/06 Distributed Training/V2-06 Distributed Training#^sec-distributed-training-systems|Distributed Training]]**).

^tbl-fleet-inter-node

### Wide-Area Network

^wide-area-network

Cross-region communication introduces latency floors set by the speed of light in optical fiber. For a 5,000 km link (roughly New York to London), the minimum one-way latency is 5,000 km/200,000 km/s = 25 ms, orders of magnitude higher than intra-data-center latency. This physical constraint is why geo-distributed training uses asynchronous methods or careful placement of pipeline stages, and why federated learning (**[[01 Books/Volume II - Scaling/03 The Fleet in Production/11 Edge Intelligence/V2-11 Edge Intelligence#^sec-edge-intelligence|Edge Intelligence]]**) tolerates stale gradients. Network specifications define how fast data moves across links and regions, but a multi-thousand-node training job can sustain those transfer rates only while every participating accelerator, network card, and switch remains healthy.

## Reliability Assumptions

^reliability-assumptions

At fleet scale, component failures are statistical certainties rather than exceptional events. The reliability assumptions here fix MTTF for each major component class in a data-center GPU node and the time to detect and recover from failures. These values drive analysis in **[[01 Books/Volume II - Scaling/02 Distributed ML/07 Fault Tolerance/V2-07 Fault Tolerance#^sec-fault-tolerance-reliability|Fault Tolerance]]** and scheduling in **[[01 Books/Volume II - Scaling/02 Distributed ML/08 Fleet Orchestration/V2-08 Fleet Orchestration#^sec-fleet-orchestration|Fleet Orchestration]]**. Deeper failure modeling appears in **[[05 Reference/Volume II - Scaling/V2 Reliability Foundations#^sec-appdx-reliability-foundations|Reliability Foundations]]**.

### Component MTTF

^component-mttf

A single data-center GPU runs for tens of thousands of hours on average before failing, yet combining eight GPUs and eight NICs per server across a thousand nodes turns multi-year component lifetimes into a cluster interruption every few hours. The steady-state component MTTFs in [[05 Reference/Volume II - Scaling/V2 System Assumptions#^tbl-fleet-mttf|table 6]] exclude the early “infant mortality” period after deployment and the late “wear-out” period beyond rated lifetime, drawing on large-GPU research-cluster analysis ([[05 Reference/Volume II - Scaling/V2 System Assumptions#^ref-kokolis2025|Kokolis et al. 2025]]), TPUv4 supercomputer resiliency and operations ([[05 Reference/Volume II - Scaling/V2 System Assumptions#^ref-zu2024tpuv4|Zu et al. 2024]]), and warehouse-scale machine design ([[05 Reference/Volume II - Scaling/V2 System Assumptions#^ref-barroso2019|Barroso et al. 2019]]).

| **Assumption**                     | **Value** | **Unit** |
|:-----------------------------------|:---------:|:--------:|
| GPU MTTF                           |  50,000   |  hours   |
| NIC MTTF                           |  150,000  |  hours   |
| PSU MTTF                           |  100,000  |  hours   |
| PCIe switch MTTF                   |  200,000  |  hours   |
| HBM MTTF                           |  200,000  |  hours   |
| Top-of-rack switch MTTF            |  300,000  |  hours   |
| Optical cable and transceiver MTTF |  50,000   |  hours   |

Table 6: **Component Mean Time to Failure**: Steady-state MTTF anchors from ([[05 Reference/Volume II - Scaling/V2 System Assumptions#^ref-kokolis2025|Kokolis et al. 2025]]; [[05 Reference/Volume II - Scaling/V2 System Assumptions#^ref-zu2024tpuv4|Zu et al. 2024]]; [[05 Reference/Volume II - Scaling/V2 System Assumptions#^ref-barroso2019|Barroso et al. 2019]]). Combined DGX H100 node MTBF $\approx$ 4,687.5 h (195.3 d) for 8 GPUs and 8 NICs in series, the same node composition as the MTBF cascade in **[[05 Reference/Volume II - Scaling/V2 Reliability Foundations#^sec-appdx-reliability-foundations-mtbf-cascade|The MTBF cascade]]**. The node’s 6 PSUs run 4+2 redundant, so no single PSU failure stops it and they add no term. The PCIe switch and HBM rows are node components that series model leaves out, and the top-of-rack switch and cable rows are network failures outside the node. Counting any of them would shorten the interval between interruptions a job sees.

^tbl-fleet-mttf

### Recovery Time Assumptions

^recovery-time-assumptions

When one of those components fails, the cluster loses wall-clock time not only to replaying steps since the last snapshot, but also to expiring the heartbeat timer, allocating a replacement node, and streaming the checkpoint back from storage. [[05 Reference/Volume II - Scaling/V2 System Assumptions#^tbl-fleet-recovery|Table 7]] lists the detection, rescheduling, and storage-bandwidth assumptions used in checkpoint interval optimization (the Young-Daly formula in **[[01 Books/Volume II - Scaling/02 Distributed ML/07 Fault Tolerance/V2-07.09 Checkpointing and Progress Preservation#^sec-fault-tolerance-young-daly|The Young-Daly checkpoint interval]]**) and effective throughput calculations throughout this book.

| **Assumption**                         | **Value** | **Unit** |
|:---------------------------------------|:---------:|:--------:|
| Failure detection timeout (heartbeat)  |    30     | seconds  |
| Job reschedule delay                   |    60     | seconds  |
| Checkpoint write bandwidth (aggregate) |    100    |   GB/s   |

Table 7: **Recovery Time Parameters**: Design assumptions for heartbeat, reschedule, and checkpoint-write bandwidth (Young-Daly context ([[05 Reference/Volume II - Scaling/V2 System Assumptions#^ref-young1974|Young 1974]]; [[05 Reference/Volume II - Scaling/V2 System Assumptions#^ref-daly2006|Daly 2006]])). Recovery before replay $\approx$ detect + reschedule + checkpoint size divided by storage bandwidth; for a 70B-parameter model with a 14-byte-per-parameter checkpoint, about 99.8 s per failure.

^tbl-fleet-recovery

Together with [[05 Reference/Volume II - Scaling/V2 System Assumptions#^tbl-fleet-mttf|table 6]], these recovery parameters determine how much wall time is lost when hardware fails. Even on fault-free steps, however, distributed training stalls whenever workers synchronize gradients or activations across the network.

## Communication Model Parameters

^communication-model-parameters

A small control message or fine-grained collective pays a per-message software and fabric launch delay on every hop even on a 400 Gbps link, whereas a multi-gigabyte gradient synchronization is governed by sustained byte rate. The book’s communication models capture both regimes with the ${\alpha}$-${\beta}$ framework, ${T}({n}) = {\alpha}+ {n}/{\beta}$, where ${\alpha}$ is startup latency and ${\beta}$ is sustained bandwidth ([[05 Reference/Volume II - Scaling/V2 System Assumptions#^ref-hockney1994|Hockney 1994]]). [[05 Reference/Volume II - Scaling/V2 System Assumptions#^tbl-fleet-alpha-beta|Table 8]] lists values from fabric specifications, vendor product documentation, and large-cluster training studies ([[05 Reference/Volume II - Scaling/V2 System Assumptions#^ref-infiniband2000spec|InfiniBand Trade Association 2000]]; [[05 Reference/Volume II - Scaling/V2 System Assumptions#^ref-gangidi2024rdma|Gangidi et al. 2024]]; [[05 Reference/Volume II - Scaling/V2 System Assumptions#^ref-nvidia2026quantumX800|NVIDIA 2026]]; [[05 Reference/Volume II - Scaling/V2 System Assumptions#^ref-ethernetAlliance2025roadmap|Ethernet Alliance 2025]]; [[05 Reference/Volume II - Scaling/V2 System Assumptions#^ref-jiang2024megascale|Jiang et al. 2024]]), feeding the collective-communication models in **[[01 Books/Volume II - Scaling/02 Distributed ML/05 Collective Communication/V2-05 Collective Communication#^sec-collective-communication|Collective Communication]]** and parallelism comparisons in **[[01 Books/Volume II - Scaling/02 Distributed ML/06 Distributed Training/V2-06 Distributed Training#^sec-distributed-training-systems|Distributed Training]]**.

| **Assumption**                                 | **Value** | **Unit** |
|:-----------------------------------------------|:---------:|:--------:|
| InfiniBand NDR startup latency (${\alpha}$)    |    1.5    |    us    |
| InfiniBand NDR sustained bandwidth (${\beta}$) |    50     |   GB/s   |
| InfiniBand HDR startup latency (${\alpha}$)    |    2–5    |    us    |
| InfiniBand HDR sustained bandwidth (${\beta}$) |    25     |   GB/s   |
| RoCE startup latency (${\alpha}$)              |   5–10    |    us    |
| RoCE sustained bandwidth (${\beta}$)           |   12.5    |   GB/s   |
| TCP startup latency (${\alpha}$)               |    50     |    us    |

Table 8: **Communication Model Parameters (${\alpha}$-${\beta}$)**: ${\alpha}$ (startup) and ${\beta}$ (bandwidth) from fabric specifications and measured cluster studies ([[05 Reference/Volume II - Scaling/V2 System Assumptions#^ref-infiniband2000spec|InfiniBand Trade Association 2000]]; [[05 Reference/Volume II - Scaling/V2 System Assumptions#^ref-jiang2024megascale|Jiang et al. 2024]]). Every ${\alpha}$ is an effective per-message launch latency that includes the communication library’s software stack, the convention of **[[01 Books/Volume II - Scaling/02 Distributed ML/05 Collective Communication/V2-05.06 Pricing Collectives by Rounds and Chunks#^tbl-interconnect-parameters|Interconnect Performance Parameters]]**, so it differs from the fabric’s end-to-end one-way latency in [[05 Reference/Volume II - Scaling/V2 System Assumptions#^tbl-fleet-inter-node|table 5]]. The InfiniBand NDR value is the single anchor used in the book’s collective models. The 33× NDR-vs-TCP gap explains why RDMA fabrics dominate synchronous training.

^tbl-fleet-alpha-beta

### AllReduce Cost Model

^allreduce-cost-model

Synchronizing a ${M}$-byte gradient buffer across ${N}$ data-parallel ranks via ring AllReduce transmits $2({N}-1){M}/{N}$ bytes per rank, which approaches $2{M}$ bytes per rank as ${N}$ grows. [[05 Reference/Volume II - Scaling/V2 System Assumptions#^tbl-fleet-allreduce|Table 9]] lists the asymptotic bandwidth factor and node-boundary count used in AllReduce cost estimation.

| **Assumption**                  | **Value** |    **Unit**     |
|:--------------------------------|:---------:|:---------------:|
| Ring AllReduce bandwidth factor |     2     | (dimensionless) |
| GPUs per node                   |     8     |    GPUs/node    |

Table 9: **AllReduce Cost Parameters**: Ring AllReduce factor of 2 from the standard ring algorithm ([[05 Reference/Volume II - Scaling/V2 System Assumptions#^ref-gibiansky2017baidu|Gibiansky 2017]]). The DGX H100 node (8 GPUs per node) sets the intra-node versus inter-node boundary in hierarchical collectives.

^tbl-fleet-allreduce

Compute, network, and reliability constants determine how long a training or serving job runs on the cluster; operating that cluster in a real data center also requires budgeting the electrical power, cooling water, and grid carbon consumed by the surrounding facility.

## Sustainability Assumptions

^sustainability-assumptions

The environmental impact of fleet-scale ML depends on three factors: how much power the facility draws beyond the IT equipment (PUE), how much water the cooling system consumes (water usage effectiveness (WUE)), and how much carbon the local grid emits per kilowatt-hour. The sustainability assumptions here support **[[01 Books/Volume II - Scaling/04 The Responsible Fleet/15 Sustainable AI/V2-15 Sustainable AI#^sec-sustainable-ai|Sustainable AI]]** and total-cost-of-ownership estimates in **[[01 Books/Volume II - Scaling/03 The Fleet in Production/12 ML Operations at Scale/V2-12 ML Operations at Scale#^sec-ops-scale|ML Operations at Scale]]**.

### Power Usage Effectiveness

^power-usage-effectiveness

A 10,000-GPU cluster drawing megawatts of IT power requires additional megawatts for the chillers, fans, and power distribution that keep the accelerators within their thermal envelope. That facility overhead is captured by PUE, the ratio of total facility power to IT equipment power (**[[01 Books/Volume II - Scaling/04 The Responsible Fleet/15 Sustainable AI/V2-15.05 Energy Measurement and Modeling#^eq-pue|equation 15.2]]**), where a PUE of 1.0 would mean zero energy beyond the IT equipment itself. The reference tiers in [[05 Reference/Volume II - Scaling/V2 System Assumptions#^tbl-fleet-pue|table 10]] represent illustrative facility scenarios rather than universal bounds of a cooling technology.

| **Assumption**                     | **Value** | **Unit** |
|:-----------------------------------|:---------:|:--------:|
| PUE (liquid-cooled, best in class) |   1.06    | (ratio)  |
| PUE (best air-cooled)              |   1.12    | (ratio)  |
| PUE (industry average, 2022)       |   1.55    | (ratio)  |
| PUE (industry average, 2023)       |   1.58    | (ratio)  |

Table 10: **Power usage effectiveness tiers**: Illustrative PUE tiers from hyperscale surveys and Green Grid definitions ([[05 Reference/Volume II - Scaling/V2 System Assumptions#^ref-davis2022uptime|Uptime Institute 2022]]; [[05 Reference/Volume II - Scaling/V2 System Assumptions#^ref-thegreengrid2007pue|The Green Grid 2007]]). Industry-average (2023) vs. liquid-cooled gap: 49.1 percent more facility power for the same IT load.

^tbl-fleet-pue

### Water Usage Effectiveness

^water-usage-effectiveness

Evaporative cooling towers achieve low PUE by evaporating water to reject heat, whereas a closed liquid loop limits water loss at the rack while still depending on the heat-rejection system outside that loop. To quantify that cooling trade-off, WUE measures liters of water consumed per kilowatt-hour of IT energy ([[05 Reference/Volume II - Scaling/V2 System Assumptions#^ref-thegreengrid2011wue|The Green Grid 2011]]), and [[05 Reference/Volume II - Scaling/V2 System Assumptions#^tbl-fleet-wue|table 11]] separates air-cooled, evaporative, and closed-loop liquid reference tiers.

| **Assumption**            | **Value** | **Unit** |
|:--------------------------|:---------:|:--------:|
| WUE (air-cooled)          |    1.8    |  L/kWh   |
| WUE (evaporative cooling) |    1.8    |  L/kWh   |
| WUE (closed-loop liquid)  |     0     |  L/kWh   |

Table 11: **Water usage effectiveness tiers**: Illustrative WUE tiers for cooling-class comparisons ([[05 Reference/Volume II - Scaling/V2 System Assumptions#^ref-thegreengrid2011wue|The Green Grid 2011]]; [[05 Reference/Volume II - Scaling/V2 System Assumptions#^ref-davis2022uptime|Uptime Institute 2022]]). Evaporative example at 10 MW IT load: 432,000 L/day.

^tbl-fleet-wue

### Regional Carbon Intensity

^regional-carbon-intensity

The same training run emits vastly different amounts of CO$_2$ depending on the grid that supplies its electricity. [[05 Reference/Volume II - Scaling/V2 System Assumptions#^tbl-fleet-carbon|Table 12]] lists regional grid carbon intensities from IEA and Canadian government emissions-factor data ([[05 Reference/Volume II - Scaling/V2 System Assumptions#^ref-iea2024emissionsFactors|International Energy Agency 2024]]; [[05 Reference/Volume II - Scaling/V2 System Assumptions#^ref-canada2026emissionFactors|Environment and Climate Change Canada 2026]]), rounded for napkin math. These values are central to location-aware scheduling in **[[01 Books/Volume II - Scaling/04 The Responsible Fleet/15 Sustainable AI/V2-15 Sustainable AI#^sec-sustainable-ai|Sustainable AI]]**.

| **Assumption**                     | **Value** | **Unit** |
|:-----------------------------------|:---------:|:--------:|
| Grid carbon intensity (Norway)     |    10     | gCO2/kWh |
| Grid carbon intensity (Quebec)     |    20     | gCO2/kWh |
| Grid carbon intensity (France)     |    50     | gCO2/kWh |
| Grid carbon intensity (EU average) |    270    | gCO2/kWh |
| Grid carbon intensity (US average) |    429    | gCO2/kWh |
| Grid carbon intensity (Poland)     |    820    | gCO2/kWh |

Table 12: **Regional Grid Carbon Intensity**: Grid carbon intensity in gCO$_2$/kWh, anchored to emissions-factor data ([[05 Reference/Volume II - Scaling/V2 System Assumptions#^ref-iea2024emissionsFactors|International Energy Agency 2024]]; [[05 Reference/Volume II - Scaling/V2 System Assumptions#^ref-canada2026emissionFactors|Environment and Climate Change Canada 2026]]) and ordered from low (Norway) to high (Poland). Location alone changes carbon intensity by 82×, often more than an algorithmic change saves.

^tbl-fleet-carbon

### Power Density

^power-density

Packing eight high-wattage accelerators and their host and network hardware into a server chassis pushes AI racks far past the thermal load of conventional enterprise racks. Whether liquid cooling is required depends on the installed heat-removal capacity, airflow, and server design rather than a universal rack-power threshold, and [[05 Reference/Volume II - Scaling/V2 System Assumptions#^tbl-fleet-power-density|table 13]] lists the reference rack power levels used in **[[01 Books/Volume II - Scaling/01 The Fleet/02 Compute Infrastructure/V2-02 Compute Infrastructure#^sec-compute-infrastructure|Compute Infrastructure]]** and **[[01 Books/Volume II - Scaling/04 The Responsible Fleet/15 Sustainable AI/V2-15 Sustainable AI#^sec-sustainable-ai|Sustainable AI]]**, anchored to current AI power-and-cooling product disclosures ([[05 Reference/Volume II - Scaling/V2 System Assumptions#^ref-dell2026powercool|Dell Technologies 2026]]; [[05 Reference/Volume II - Scaling/V2 System Assumptions#^ref-schneider2024ai132kw|Schneider Electric 2024]]).

| **Assumption**                       | **Value** | **Unit** |
|:-------------------------------------|:---------:|:--------:|
| Rack power (traditional enterprise)  |    12     |    kW    |
| Rack power (AI, typical)             |    70     |    kW    |
| Rack power (AI, high density)        |    100    |    kW    |
| Air-cooling practical limit per rack |    30     |    kW    |

Table 13: **Rack Power Density**: Illustrative rack-power tiers and air-cooling limit ([[05 Reference/Volume II - Scaling/V2 System Assumptions#^ref-davis2022uptime|Uptime Institute 2022]]; [[05 Reference/Volume II - Scaling/V2 System Assumptions#^ref-dell2026powercool|Dell Technologies 2026]]; [[05 Reference/Volume II - Scaling/V2 System Assumptions#^ref-schneider2024ai132kw|Schneider Electric 2024]]). The listed AI rack scenarios (70 kW–100 kW) exceed the illustrative 30 kW air-cooling reference; the feasible limit depends on the installed system.

^tbl-fleet-power-density

These sustainability constants quantify the megawatts, water volume, and carbon emissions of operating a fleet; converting those physical resource draws and accelerator allocations into project budgets requires unit prices for compute hours, electricity, and network egress.

## Economic Assumptions

^economic-assumptions

A multi-week training run on thousands of GPUs or a global serving tier streaming responses across regions accumulates millions of dollars in compute rental, facility electricity, and network egress charges. The prices in [[05 Reference/Volume II - Scaling/V2 System Assumptions#^tbl-fleet-economic|table 14]] provide illustrative hyperscaler-order rates (2024–2025 magnitude) for total cost of ownership (TCO) ratio analysis in **[[01 Books/Volume II - Scaling/03 The Fleet in Production/12 ML Operations at Scale/V2-12 ML Operations at Scale#^sec-ops-scale|ML Operations at Scale]]** and **[[01 Books/Volume II - Scaling/03 The Fleet in Production/10 Serving at Scale/V2-10 Serving at Scale#^sec-inference-scale|Serving at Scale]]**, not quotes for a specific contract.

| **Assumption**                  | **Value** |  **Unit**  |
|:--------------------------------|:---------:|:----------:|
| Fleet GPU-hour reference price  |     2     |  dollar/h  |
| Cloud GPU training rental rate  |     4     |  dollar/h  |
| Cloud GPU inference rental rate |    2.5    |  dollar/h  |
| Cloud electricity price         |   0.12    | dollar/kWh |
| Cloud egress price per GB       |   0.09    | dollar/GB  |

Table 14: **Fleet-Scale Economic Parameters**: Illustrative GPU-hour, electricity, and egress rates for TCO examples (substitute contract pricing for absolute budgets). The fleet GPU-hour reference is the price per in-service accelerator-hour used by this book’s fleet cost examples; the cloud rental rates are public list-price anchors for comparison.

^tbl-fleet-economic

Pricing an accelerator-hour settles what a cluster allocation costs per unit of wall time, but converting that hourly spend into delivered training progress requires discounting datasheet peak FLOP/s by kernel utilization, multi-node scaling efficiency, and operational downtime.

## Capacity Planning Assumptions

^capacity-planning-assumptions

Multiplying a cluster’s GPU count by the H100’s datasheet peak FLOP/s overstates delivered training throughput by more than a factor of three, because single-device kernel inefficiency, multi-node communication stalls, and out-of-step operational downtime each take a cut. The capacity-planning assumptions quantify the fraction of peak hardware performance that real workloads sustain on one device (MFU), how efficiently that performance scales as more machines are added (scaling efficiency), and what share of wall time is lost to operational pauses. Because these factors compound across the fleet, the planning equation is multiplicative:

$$
{R_{\text{eff}}} = {N}{R_{\text{peak}}} \times {\text{MFU}} \times {\eta_{\text{scaling}}} \times (1 - {f_{\text{overhead}}})
$$

Here ${R_{\text{eff}}}$ is effective fleet throughput, ${N}{R_{\text{peak}}}$ is nominal cluster peak throughput. MFU is the single-device baseline measured over productive steps. ${\eta_{\text{scaling}}}$ captures the additional in-step losses from distribution, including communication and pipeline bubbles. ${f_{\text{overhead}}}$ removes only out-of-step checkpoint, recovery, and maintenance time. These windows must be disjoint: measured fleet-step MFU already includes scaling losses, so it must not be multiplied by scaling efficiency again. The three subsections that follow fix those factors in order.

### Model FLOPs Utilization

^model-flops-utilization

Even on a single accelerator, memory-bandwidth stalls, kernel launch gaps, and non-matmul operations prevent a model from sustaining datasheet peak throughput. MFU measures useful model FLOP/s divided by hardware peak FLOP/s over a stated measurement window, so an MFU of 0.50 means the workload achieves half of peak FLOP/s; synchronization and idle time within that window lower MFU even though they contribute no model FLOPs. [[05 Reference/Volume II - Scaling/V2 System Assumptions#^tbl-fleet-mfu|Table 15]] lists the reference MFU ranges used in training time and cost estimates throughout this book.

| **Assumption**               | **Value** |  **Unit**  |
|:-----------------------------|:---------:|:----------:|
| Training MFU (low end)       |    0.3    | (fraction) |
| Training MFU (high end)      |    0.5    | (fraction) |
| Inference MFU (batch size 1) |   0.05    | (fraction) |
| Inference MFU (batched)      |    0.4    | (fraction) |

Table 15: **Model FLOPs utilization ranges**: Training MFU 0.3–0.5 from large-model training reports ([[05 Reference/Volume II - Scaling/V2 System Assumptions#^ref-chowdhery2022palm|Chowdhery et al. 2022]]; [[05 Reference/Volume II - Scaling/V2 System Assumptions#^ref-narayanan2021|Narayanan et al. 2021]]); inference batch-1 MFU 5 percent from ([[05 Reference/Volume II - Scaling/V2 System Assumptions#^ref-pope2023efficiently|Pope et al. 2023]]) (memory-bound decode).

^tbl-fleet-mfu

### Scaling Efficiency

^scaling-efficiency

Expanding a job from one node to hundreds of nodes adds gradient synchronization and pipeline bubble stalls that stretch each step beyond its single-device baseline. Scaling efficiency ${\eta_{\text{scaling}}} = {T_1}/({N}\times {T_N})$ measures how much of the added compute actually reduces training time, and [[05 Reference/Volume II - Scaling/V2 System Assumptions#^tbl-fleet-scaling|table 16]] lists the tiers this book plans with. From 256 GPUs up, these values match MLSysIM’s modeled efficiency curve for the 175B reference job at a fixed GPT-3 global batch. They extend the multi-GPU scaling sweep of **[[01 Books/Volume II - Scaling/02 Distributed ML/08 Fleet Orchestration/V2-08.08 Elastic Scheduling#^fig-fleet-orchestration-scaling-efficiency-curve|figure]]** in **[[01 Books/Volume II - Scaling/02 Distributed ML/08 Fleet Orchestration/V2-08 Fleet Orchestration#^sec-fleet-orchestration|Fleet Orchestration]]** out to 8,192 accelerators. The 32-GPU tier is a book convention, since one tensor- and pipeline-parallel replica of that job needs 64 GPUs. Production systems retain more at scale by training with a larger global batch and, where they pipeline, by interleaving stages. Published large language model (LLM) training runs built this way report near-linear scaling on thousands of accelerators ([[05 Reference/Volume II - Scaling/V2 System Assumptions#^ref-jiang2024megascale|Jiang et al. 2024]]; [[05 Reference/Volume II - Scaling/V2 System Assumptions#^ref-chowdhery2022palm|Chowdhery et al. 2022]]).

| **Assumption**                  | **Value** |  **Unit**  |
|:--------------------------------|:---------:|:----------:|
| Scaling efficiency (32 GPUs)    |    0.9    | (fraction) |
| Scaling efficiency (256 GPUs)   |   0.87    | (fraction) |
| Scaling efficiency (1,024 GPUs) |   0.83    | (fraction) |
| Scaling efficiency (8,192 GPUs) |   0.56    | (fraction) |

Table 16: **Scaling Efficiency by Cluster Size**: Planning ${\eta_{\text{scaling}}}$ tiers. The 256- to 8,192-GPU values are MLSysIM’s model of the 175B reference job at a fixed global batch, and the 32-GPU value is a book convention. At 8,192 GPUs, 4,587.5 effective GPUs of 8,192 nominal.

^tbl-fleet-scaling

### Overhead Budgets

^overhead-budgets

Real training jobs spend a fraction of wall time on noncompute activities: pipeline bubble idle time, checkpoint writes, failure recovery, and scheduled maintenance. [[05 Reference/Volume II - Scaling/V2 System Assumptions#^tbl-fleet-overhead|Table 17]] lists the overhead budgets assumed throughout this book. When measured as nonoverlapping fractions of the same wall-time window, these fractions are additive: total overhead at fleet scale is approximately 5 percent + 3 percent + 10 percent + 5 percent = 23 percent, leaving 77 percent outside these listed overhead categories. This combined budget includes pipeline bubbles; the multiplicative planning equation excludes them from its operational factor ${f_{\text{overhead}}}$ because scaling efficiency ${\eta_{\text{scaling}}}$ already accounts for them.

| **Assumption**                             | **Value** |  **Unit**  |
|:-------------------------------------------|:---------:|:----------:|
| Wall-time overhead (pipeline bubbles)      |   0.05    | (fraction) |
| Wall-time overhead (checkpointing)         |   0.03    | (fraction) |
| Wall-time overhead (failure recovery)      |    0.1    | (fraction) |
| Wall-time overhead (scheduled maintenance) |   0.05    | (fraction) |

Table 17: **Overhead Budgets (Fraction of Wall Time)**: Book-convention wall-time fractions for pipeline bubbles, checkpointing, failure recovery, and maintenance, engineering targets, not physical constants. Combined 23 percent overhead $\Rightarrow$ 23.1 days of effective work in a 30-day run.

^tbl-fleet-overhead

Combining hardware peaks, link rates, reliability intervals, facility power, dollar rates, and utilization fractions in a single calculation requires a consistent set of dimensional prefixes and unit aliases.

## Unit Conventions

^unit-conventions

Combining an accelerator memory capacity in gigabytes, a checkpoint payload in terabytes, and a link rate in gigabits per second produces silent factor-of-eight or base-2-versus-base-10 errors unless every table shares one dimensional system. Every quantitative example in this book therefore follows the unit conventions in [[05 Reference/Volume II - Scaling/V2 System Assumptions#^tbl-fleet-units|table 18]], where each row gives the multiplier ${k}$ in `1 alias` $=$ ${k}$ `base`. Data prefixes use decimal SI ($\text{KB} = 10^3$ bytes, not 1024). Throughput quantities (FLOP/s, GB/s) combine these aliases with time; adding incompatible dimensions (bytes to FLOP/s) is a category error in napkin math, not a unit conversion.

Hardware capacity labels are the one deliberate exception. Reference tables may retain vendor nameplate numbers and labels; the byte budgets used in calculations follow the device assumptions stored in the book’s hardware registry. For example, the book models an 80 GB accelerator with $80 \times 2^{30}$ bytes, so a node of eight such devices holds $640 \times 2^{30}$ bytes rather than $640 \times 10^9$. These are modeled capacity assumptions, not universal guarantees inferred from the labels. Every other data quantity, including model footprints, KV-cache sizes, checkpoint volumes, and collective payloads, uses those decimal SI prefixes. Where a worked example subtracts a computed footprint from a device capacity, the stored capacity byte budget is converted to decimal units alongside the footprint so that the arithmetic printed on the page is the arithmetic a reader can reproduce.

| **Alias** | **Multiplier** | **Base unit** |
|:----------|:--------------:|:-------------:|
| `byte`    |       1        |     byte      |
| `KB`      |      1000      |     byte      |
| `MB`      |     1e+06      |     byte      |
| `GB`      |     1e+09      |     byte      |
| `TB`      |     1e+12      |     byte      |
| `PB`      |     1e+15      |     byte      |
| `flop`    |       1        |     flop      |
| `GFLOPs`  |     1e+09      |     flop      |
| `TFLOPs`  |     1e+12      |     flop      |
| `ZFLOPs`  |     1e+21      |     flop      |
| `param`   |       1        |     param     |
| `Mparam`  |     1e+06      |     param     |
| `Gbps`    |     1e+09      |     bit/s     |
| `NS`      |     1e-09      |    second     |
| `US`      |     1e-06      |    second     |
| `MS`      |     0.001      |    second     |
| `second`  |       1        |    second     |
| `hour`    |      3600      |    second     |
| `day`     |     86400      |    second     |
| `joule`   |       1        |     joule     |
| `watt`    |       1        |     watt      |
| `meter`   |       1        |     meter     |

Table 18: **Unit Conventions**: Decimal SI aliases and scale factors (book convention). Throughput forms (FLOP/s, GB/s) divide work or data by time using the same conventions.

^tbl-fleet-units

Two fleet-scale conventions deserve emphasis beyond the table because they recur in almost every cross-node or facility calculation:

- Network bandwidth appears in both bit-rate (Gbps) and byte-rate (GB/s). Divide by 8 to convert Gbps to GB/s (for example, 400 Gb/s = 50 GB/s for InfiniBand NDR). Chapters use whichever form fits the calculation; byte-rate is usually easier for transfer-time estimates.
- Carbon intensity uses gCO$_2$/kWh (grams of CO$_2$ per kilowatt-hour). Multiply total energy (kWh) by regional carbon intensity to get emissions in grams, then divide by $10^6$ for metric tons.

## Assumption Provenance

^sec-appdx-fleet-assumption-provenance

The reference tables in this appendix mix H100 datasheet ceilings, empirical failure rates from warehouse-scale fleets, modeled MLSysIM scaling curves, and illustrative cloud rental rates, and treating all four as interchangeable measurements would misstate what an estimate proves. Each section therefore carries an explicit source classification and primary bibliography in [[05 Reference/Volume II - Scaling/V2 System Assumptions#^tbl-fleet-assumption-provenance-catalog|table 19]], separating empirical hardware measurements from modeled scaling profiles and editorial conventions so a reader can see which numbers change with a hardware generation and which reflect a deployment choice.

| **Appendix section**                 | **Source type**                   | **Primary references**                                                                                                                                                                                                                                                                                                                                                                                                               |
|:-------------------------------------|:----------------------------------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| H100 recap                           | Vendor datasheet peak             | ([[05 Reference/Volume II - Scaling/V2 System Assumptions#^ref-choquette2023\|Choquette 2023]])                                                                                                                                                                                                                                                                                                                                 |
| Reference workload (Archetype A)     | Book convention                   | GPT-3-class dense model; byte widths from the notation conventions                                                                                                                                                                                                                                                                                                                                                                   |
| Cluster tiers                        | Book convention                   | ([[05 Reference/Volume II - Scaling/V2 System Assumptions#^ref-kokolis2025\|Kokolis et al. 2025]]) (scale context)                                                                                                                                                                                                                                                                                                              |
| Network fabrics                      | Vendor specs; InfiniBand standard | ([[05 Reference/Volume II - Scaling/V2 System Assumptions#^ref-nvidia2017gpu\|NVIDIA Corporation 2017]], [[05 Reference/Volume II - Scaling/V2 System Assumptions#^ref-NVIDIA2020\|2020]]; [[05 Reference/Volume II - Scaling/V2 System Assumptions#^ref-choquette2023\|Choquette 2023]]; [[05 Reference/Volume II - Scaling/V2 System Assumptions#^ref-infiniband2000spec\|InfiniBand Trade Association 2000]]) |
| Reliability (MTTF)                   | Fleet studies                     | ([[05 Reference/Volume II - Scaling/V2 System Assumptions#^ref-kokolis2025\|Kokolis et al. 2025]]; [[05 Reference/Volume II - Scaling/V2 System Assumptions#^ref-zu2024tpuv4\|Zu et al. 2024]]; [[05 Reference/Volume II - Scaling/V2 System Assumptions#^ref-barroso2019\|Barroso et al. 2019]])                                                                                                                     |
| Recovery times                       | Design assumptions                | ([[05 Reference/Volume II - Scaling/V2 System Assumptions#^ref-young1974\|Young 1974]]; [[05 Reference/Volume II - Scaling/V2 System Assumptions#^ref-daly2006\|Daly 2006]])                                                                                                                                                                                                                                               |
| Communication (${\alpha}$-${\beta}$) | Fabric specs; training at scale   | ([[05 Reference/Volume II - Scaling/V2 System Assumptions#^ref-infiniband2000spec\|InfiniBand Trade Association 2000]]; [[05 Reference/Volume II - Scaling/V2 System Assumptions#^ref-jiang2024megascale\|Jiang et al. 2024]])                                                                                                                                                                                             |
| AllReduce model                      | Algorithm identity                | ([[05 Reference/Volume II - Scaling/V2 System Assumptions#^ref-gibiansky2017baidu\|Gibiansky 2017]])                                                                                                                                                                                                                                                                                                                            |
| Sustainability (PUE/WUE/rack power)  | Industry surveys                  | ([[05 Reference/Volume II - Scaling/V2 System Assumptions#^ref-davis2022uptime\|Uptime Institute 2022]]; [[05 Reference/Volume II - Scaling/V2 System Assumptions#^ref-thegreengrid2007pue\|The Green Grid 2007]])                                                                                                                                                                                                         |
| Carbon intensity                     | Grid statistics                   | ([[05 Reference/Volume II - Scaling/V2 System Assumptions#^ref-iea2024emissionsFactors\|International Energy Agency 2024]]; [[05 Reference/Volume II - Scaling/V2 System Assumptions#^ref-canada2026emissionFactors\|Environment and Climate Change Canada 2026]])                                                                                                                                                         |
| Cloud economics                      | Illustrative rates                | Editorial (2024–2025 order of magnitude)                                                                                                                                                                                                                                                                                                                                                                                             |
| MFU                                  | Published LLM training            | ([[05 Reference/Volume II - Scaling/V2 System Assumptions#^ref-chowdhery2022palm\|Chowdhery et al. 2022]]; [[05 Reference/Volume II - Scaling/V2 System Assumptions#^ref-narayanan2021\|Narayanan et al. 2021]]; [[05 Reference/Volume II - Scaling/V2 System Assumptions#^ref-pope2023efficiently\|Pope et al. 2023]])                                                                                               |
| Scaling efficiency                   | MLSysIM model; book convention    | Context: ([[05 Reference/Volume II - Scaling/V2 System Assumptions#^ref-jiang2024megascale\|Jiang et al. 2024]]; [[05 Reference/Volume II - Scaling/V2 System Assumptions#^ref-chowdhery2022palm\|Chowdhery et al. 2022]])                                                                                                                                                                                                 |
| Overhead budgets                     | Book convention                   | Editorial engineering targets                                                                                                                                                                                                                                                                                                                                                                                                        |
| Unit conventions                     | Decimal SI; book notation         | Editorial                                                                                                                                                                                                                                                                                                                                                                                                                            |

Table 19: **Fleet Assumption Provenance Catalog**: Quick map from appendix section to source class and bibliography.

^tbl-fleet-assumption-provenance-catalog

## Summary

^summary

Fleet-scale back-of-envelope estimates stay comparable across chapters only when they draw from a single shared assumption sheet. Every napkin-math calculation in this book traces to a row in the reference tables of this appendix, and [[05 Reference/Volume II - Scaling/V2 System Assumptions#^tbl-fleet-assumption-provenance-catalog|table 19]] records whether that row comes from a datasheet, a fleet study, an MLSysIM model, an illustrative rate, or a book convention. Reliability rows set the failure clock, with failure a steady-state condition at 10,000 or more GPUs (**[[05 Reference/Volume II - Scaling/V2 Reliability Foundations#^sec-appdx-reliability-foundations|Reliability Foundations]]** models it in depth). Communication rows decide whether synchronous training is viable, and the 33× startup-latency gap between InfiniBand NDR and TCP explains why training clusters favor RDMA fabrics. Sustainability rows expose location as a lever, since grid carbon intensity differs by 82× between Norway and Poland. Capacity rows bridge peak hardware to useful throughput. At 8,192 GPUs, about 56 percent of ideal scaling is realized for the reference job at a fixed batch, and the listed overheads consume about 23 percent of wall time. When a deployment differs in fabric, region, MFU, or cluster size, substitute its values and re-evaluate the corresponding formulas.

Back to top

## Source References

^source-references

Hockney, Roger W. 1994. “The Communication Challenge for MPP: Intel Paragon and Meiko CS-2.” *Parallel Computing* 20 (3): 389–98. https://doi.org/10.1016/s0167-8191(06)80021-9.

^ref-hockney1994

Gangidi, Adi, Rui Miao, Sandeep Hebbani, Gaya Nagarajan, Omar Baldonado, Lixin Gao, Hany Morsy Goes, et al. 2024. “RDMA over Ethernet for Distributed AI Training at Meta Scale.” *Proceedings of the ACM SIGCOMM 2024 Conference*, 56–69. https://doi.org/10.1145/3651890.3672233.

^ref-gangidi2024rdma

NVIDIA. 2026. *NVIDIA Quantum-X800 InfiniBand Platform*. NVIDIA product documentation.

^ref-nvidia2026quantumX800

Ethernet Alliance. 2025. *2025 Ethernet Roadmap*. Ethernet Alliance roadmap.

^ref-ethernetAlliance2025roadmap

The Green Grid. 2011. *Water Usage Effectiveness (WUE): A Green Grid Data Center Sustainability Metric*. White Paper 35. The Green Grid.

^ref-thegreengrid2011wue

Dell Technologies. 2026. *Data Center Power and Cooling Solutions*.

^ref-dell2026powercool

Schneider Electric. 2024. *Schneider Electric Announces New Solutions to Address the Energy and Sustainability Challenges Spurred by AI*.

^ref-schneider2024ai132kw

Choquette, Jack. 2023. “NVIDIA Hopper H100 GPU: Scaling Performance.” *IEEE Micro* 43 (3): 9–17. https://doi.org/10.1109/mm.2023.3256796.

^ref-choquette2023

Kokolis, Apostolos, Michael Kuchnik, John Hoffman, Adithya Kumar, Parth Malani, Faye Ma, Zach DeVito, Shubho Sengupta, Kalyan Saladi, and Carole-Jean Wu. 2025. “Revisiting Reliability in Large-Scale Machine Learning Research Clusters.” *2025 IEEE International Symposium on High Performance Computer Architecture (HPCA)*, 1259–74. https://doi.org/10.1109/hpca61900.2025.00096.

^ref-kokolis2025

NVIDIA Corporation. 2017. *NVIDIA Tesla V100 GPU Architecture*. NVIDIA Whitepaper.

^ref-nvidia2017gpu

NVIDIA Corporation. 2020. *NVIDIA A100 Tensor Core GPU Architecture*. NVIDIA Whitepaper, V1.0.

^ref-NVIDIA2020

InfiniBand Trade Association. 2000. *InfiniBand Architecture Specification Volume 1*. InfiniBand Trade Association.

^ref-infiniband2000spec

Zu, Y., A. Ghaffarkhah, H.-V. Dang, B. Towles, S. Hand, S. Huda, A. Bello, et al. 2024. “Resiliency at Scale: Managing Google’s TPUv4 Machine Learning Supercomputer.” *21st USENIX Symposium on Networked Systems Design and Implementation (NSDI 24)*, 761–74.

^ref-zu2024tpuv4

Barroso, Luiz André, Urs Hölzle, and Parthasarathy Ranganathan. 2019. *The Datacenter as a Computer: Designing Warehouse-Scale Machines*. Synthesis Lectures on Computer Architecture. Springer International Publishing. https://doi.org/10.1007/978-3-031-01761-2.

^ref-barroso2019

Young, John W. 1974. “A First Order Approximation to the Optimum Checkpoint Interval.” *Communications of the ACM* 17 (9): 530–31. https://doi.org/10.1145/361147.361115.

^ref-young1974

Daly, J. T. 2006. “A Higher Order Estimate of the Optimum Checkpoint Interval for Restart Dumps.” *Future Generation Computer Systems* 22 (3): 303–12. https://doi.org/10.1016/j.future.2004.11.016.

^ref-daly2006

Jiang, Ziheng, Haibin Lin, Yinmin Zhong, Qi Huang, Yangrui Chen, Zhi Zhang, Yanghua Peng, et al. 2024. “MegaScale: Scaling Large Language Model Training to More Than 10,000 GPUs.” *21st USENIX Symposium on Networked Systems Design and Implementation (NSDI 24)*, 745–60.

^ref-jiang2024megascale

Gibiansky, A. 2017. *Bringing HPC Techniques to Deep Learning*. Baidu Research Technical Blog.

^ref-gibiansky2017baidu

Uptime Institute. 2022. *Uptime Institute Global Data Center Survey 2022*. Uptime Institute.

^ref-davis2022uptime

The Green Grid. 2007. *Green Grid Data Center Power Efficiency Metrics: PUE and DCIE*. The Green Grid.

^ref-thegreengrid2007pue

International Energy Agency. 2024. *Emissions Factors 2024*.

^ref-iea2024emissionsFactors

Environment and Climate Change Canada. 2026. *Emission Factors and Reference Values*.

^ref-canada2026emissionFactors

Chowdhery, Aakanksha, Sharan Narang, Jacob Devlin, Maarten Bosma, Gaurav Mishra, Adam Roberts, Paul Barham, et al. 2022. “PaLM: Scaling Language Modeling with Pathways.” *arXiv Preprint arXiv:2204.02311*.

^ref-chowdhery2022palm

Narayanan, Deepak, Mohammad Shoeybi, Jared Casper, Patrick LeGresley, Mostofa Patwary, Vijay Korthikanti, Dmitri Vainbrand, et al. 2021. “Efficient Large-Scale Language Model Training on GPU Clusters Using Megatron-LM.” *Proceedings of the International Conference for High Performance Computing, Networking, Storage and Analysis*, 1–15. https://doi.org/10.1145/3458817.3476209.

^ref-narayanan2021

Pope, Reiner, Sholto Douglas, Aakanksha Chowdhery, Jacob Devlin, James Bradbury, Jonathan Heek, Kefan Xiao, Shivani Agrawal, and Jeff Dean. 2023. “Efficiently Scaling Transformer Inference.” *Proceedings of Machine Learning and Systems (MLSys)* 5: 606–24.

^ref-pope2023efficiently

## Source

[Repository Source](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/books/vol2/backmatter/appendix_assumptions.qmd) · [Original License](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/LICENSE.md)

[Rendered Reading Snapshot](https://mlsysbook.ai/vol2/backmatter/appendix_assumptions.html#sec-appdx-fleet-system-assumptions). Rendering provenance is recorded in the import manifest.
