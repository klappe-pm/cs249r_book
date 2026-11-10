---
title: V2 Distributed ML Principles
type: Part
volume: 2
chapter: 0
publication_status: Preview
source_repository: https://github.com/klappe-pm/cs249r_book
source_commit: de87c0103806d7bfb1c677dbb77a2b92fa00c298
source_path: books/vol2/parts/distributed_ml_principles.qmd
source_anchor: distributed-ml-principles
source_mode: Source-Correlated Published HTML
tags:
- Type/Part
- Book/Volume_2
rendered_source_url: https://mlsysbook.ai/vol2/parts/distributed_ml_principles.html
---

# V2 Distributed ML Principles

[[Home|Home]] · [[01 Books/Volume II - Scaling/Volume 2 Overview|Volume Overview]]

^distributed-ml-principles

Wiring thousands of accelerators together with high-speed switches and parallel storage does not by itself make them train one model. Without distributed coordination, replicas diverge, partitioned layers stall on missing activations, and a single failed GPU halts the entire cluster. If Part I built the physical substrate, Part II establishes the logic of distribution: the algorithms, protocols, and coordination strategies that make a collection of independent accelerators behave as one machine. The same physics that set the rates in Part I explains why adding accelerators does not always yield linear speedups, and why communication, not computation, is often the hidden bottleneck.

At this scale, the engineering challenge is a trade-off between parallelization and coordination. Partitioning a model reduces per-device memory pressure but requires exchanging intermediate results across partitions. Replicating a model across workers instead requires coordinating their updates. Adding nodes can reduce training time while exposing a job to more component failures, decreasing its mean time between failures (MTBF) when an individual failure interrupts the job. Fault tolerance therefore becomes part of the execution design. These principles decompose the communication cost that the Fleet Law exposes (**[[01 Books/Volume II - Scaling/00 Introduction/01 Introduction/V2-01.06 The C³ Taxonomy and Foundations of Scale#^sec-vol2-introduction-fleet-law|The Fleet Law]]**) and add the reliability cost of scale.

The following principles preview the trade-offs developed in Part II, and the chapters establish when each mechanism helps and how to measure its cost. The first pressure is the economics of scale itself. Frontier capability demands compute, and each improvement costs more than the last, as the scaling laws of **[[01 Books/Volume II - Scaling/00 Introduction/01 Introduction/V2-01.04 AI Scaling Laws#^sec-vol2-intro-ai-scaling-laws-a043|AI Scaling Laws]]** showed. Part I priced the supply of that compute; the first principle states the demand in the form that later chapters cite.

**Principle 9: The empirical scaling law**

**Invariant**: Within empirically validated regimes, foundation-model loss (${\mathcal{L}}$) follows approximate power-law relationships with a resource quantity ${X}$ such as training compute, dataset size, or parameter count. The exponent ${\alpha_{\text{scale}}}$ depends on the fitted regime. The single-resource simplification used to illustrate diminishing returns is:

$$
{\mathcal{L}}({X}) \propto {X}^{-{\alpha_{\text{scale}}}}
$$

**Implication**: Within a fixed scaling regime, reducing loss further requires increasing resources. The diminishing return helps explain the move from single-server training to warehouse-scale clusters. Architecture, data quality, and training methods can change that regime, so a fitted scaling relation guides resource planning without guaranteeing improvements on every task.

^pri-universal-scaling

That demand for scale turns each training step into a negotiation between faster local work and slower global coordination. Splitting a batch or a model across more workers shrinks the arithmetic each device performs, but it also introduces network transfers and barrier waits that grow with cluster size.

**Principle 10: The fleet law (distributed step-time model)**

**Invariant**: Under ideal partitioning of a fixed amount of work across ${N}$ workers or accelerators, the step-time model adds computation, communication, and synchronization, then subtracts the portion hidden by overlap, with $0 \le {T_{\text{overlap}}} \le \min\!\left(\frac{{T_{\text{compute}}}}{{N}}, {T_{\text{comm}}}({N}) + {T_{\text{sync}}}({N})\right)$.

$$
{T_{\text{step}}}({N}) = \frac{{T_{\text{compute}}}}{{N}} + {T_{\text{comm}}}({N}) + {T_{\text{sync}}}({N}) - {T_{\text{overlap}}}
$$

**Implication**: Scaling is a race between parallelizable compute (which shrinks with ${N}$ under ideal partitioning), communication overhead, and synchronization overhead. To scale efficiently, algorithms must reduce or amortize ${T_{\text{comm}}}({N})$ and ${T_{\text{sync}}}({N})$ (for example, through gradient accumulation, which alters the effective batch and convergence regime, or through compression, which can introduce numerical error). They must also maximize ${T_{\text{overlap}}}$ through communication hiding and pipelined execution.

^pri-distributed-step-time

For data parallelism, the AllReduce that combines every worker’s gradients sets the size of the Fleet Law’s communication term. Because every replica must receive the full sum of gradients before advancing its weights, the volume moved per rank approaches a constant floor even as more workers join the job.

**Principle 11: The AllReduce bandwidth bound**

**Invariant**: An AllReduce of a ${M}$-byte tensor across ${N}$ ranks, built from point-to-point transfers, must send at least $2({N}-1){M}/{N}$ bytes from some rank. Ring AllReduce meets that bound, at the price of a startup term that grows linearly with ${N}$:

$$
{T_{\text{ring}}} = 2({N}-1){\alpha} + 2\frac{{N}-1}{{N}}\frac{{M}}{{\beta}}
$$

**Implication**: The bandwidth term approaches $2{M}/{\beta}$ and stops shrinking as workers are added, while each worker’s share of the compute keeps shrinking, so under pure data parallelism communication eventually dominates the step. Tree and hierarchical schedules give up some of the ring’s byte efficiency for fewer startup rounds when messages are small or ${N}$ is large.

^pri-allreduce-bandwidth-bound

The Fleet Law and the AllReduce bound predict the time of one step; the scaling efficiency bound measures how far the resulting speedup falls short of ideal. Comparing multi-device runtime against a single-device baseline turns those exposed communication and synchronization terms into a direct measure of cluster return on investment.

**Principle 12: The scaling efficiency bound**

**Invariant**: For a fixed amount of training work, adding nodes reduces the computation assigned to each node, but the communication and synchronization terms of the Fleet Law limit the resulting speedup.

$$
{\eta_{\text{scaling}}} = \frac{{T_1}}{{N}\times {T_N}}
$$

 Here, ${T_1}$ and ${T_N}$ are the times to complete the same work on one and ${N}$ devices, respectively. The ratio measures achieved speedup as a fraction of ideal linear speedup.

**Implication**: Perfect linear scaling (${\eta_{\text{scaling}}} = 1.0$) is the ideal baseline, not a practical target. Real systems fall short of it by an amount that depends on the workload, the fabric, and the parallelism layout. Under pure data parallelism the shortfall grows with ${N}$ because the compute term keeps shrinking while the ring’s bandwidth term stays near $2{M}/{\beta}$, the scaling wall of data parallelism. A statistical limit applies as well, because beyond the critical batch size added data-parallel width buys little further loss reduction. The gap between ${\eta_{\text{scaling}}} = 1.0$ and the achieved efficiency captures losses from communication and coordination as well as load imbalance or other limits on parallel execution.

^pri-scaling-efficiency

Even when communication and coordination are tuned, a larger fleet fails often enough that progress itself must be protected. Without periodic state snapshots, a single device or link failure discards every step completed since the run began.

**Principle 13: The Young-Daly checkpoint interval**

**Invariant**: The first-order checkpoint model balances the cost of writing the checkpoint (${T_{\text{write}}}$) against the expected cost of reworking lost progress due to system-level failures (${\text{MTBF}_{\text{system}}}$). For long runs with approximately constant failure rates and checkpoint write times small relative to MTBF, its optimal checkpoint interval (${T^\ast_{\text{ckpt}}}$) is:

$$
{T^\ast_{\text{ckpt}}} = \sqrt{2 \cdot {T_{\text{write}}} \cdot {\text{MTBF}_{\text{system}}}}
$$

**Implication**: Checkpointing consumes time and storage bandwidth. When more participating components reduce job MTBF, the model favors shorter intervals, and the overhead at the optimum grows roughly as the square root of the component count; faster checkpoint writes can reduce that overhead. Correlated failures, variable write times, and recovery requirements need additional analysis before the interval becomes an operational schedule.

^pri-young-daly

Fault tolerance illustrates why reducing one cost requires checking the others. Saving more often reduces expected rework but increases storage traffic.

**Principle 14: The displacement of overhead**

**Invariant**: Distributed ML optimizations often relocate overhead among Compute, Communication, and Coordination (the C$^3$ taxonomy). Reducing one term can increase another, so designs must evaluate all three.

**Implication**: Asynchronous training can eliminate global coordination barriers (${T_{\text{sync}}}({N}) \to 0$) but may introduce gradient staleness that shows up as additional training iterations (${T_{\text{compute}}} \uparrow$). Pipeline parallelism can reduce communication volume relative to finer-grained model partitioning but adds pipeline bubble time (${T_{\text{sync}}}({N}) \uparrow$). The C$^3$ taxonomy reveals where each design pays its overhead.

^pri-conservation-overhead

Accounting for overhead inside one job leaves a fleet-level question open, because many jobs compete for the same machines and a share of the fleet is worth something only if the job can run on it. Granting accelerators without the interconnect topology, power, or storage bandwidth a synchronous workload requires only strands those devices in an unusable allocation.

**Principle 15: The feasibility-before-fairness principle**

**Invariant**: A gang allocation for a synchronous job requires atomic allocation (every member is granted at once) and topology-feasible placement (the members sit within the interconnect domains the job’s parallelism requires) to complete training steps. Its power and I/O allocation must also support the rate of progress promised at admission. Missing required gang members or placement can prevent execution; insufficient power or I/O capacity can reduce progress below the admitted rate.

**Implication**: Fairness policies such as dominant-resource fairness divide useful progress, so they can choose only among feasible allocations. A scheduler must first enumerate the feasible bundles and only then apply its fairness policy to them; a fair share of accelerators on which the job cannot run is idle capacity charged to a tenant. Feasibility constraints can deliberately leave accelerators idle, and that idle capacity is the price of keeping every admitted job productive.

^pri-feasibility-before-fairness

Part II develops these previews in dependency order. Collective communication establishes how groups of workers combine and redistribute information across the fabric and what each exchange costs. Distributed training then partitions a workload and decides which of those exchanges its partitions must make. Fault tolerance protects the resulting progress against failure, and fleet orchestration allocates shared resources to jobs with those communication and recovery needs, admitting only allocations the jobs can actually use. Orchestration decides how much of the fleet a job actually holds, and fault tolerance decides how much of that held time becomes retained progress. In Fleet Law terms, collective communication shrinks ${T_{\text{comm}}}({N})$ and enlarges ${T_{\text{overlap}}}$. Distributed training decides how ${T_{\text{compute}}}/{N}$ is divided and what ${T_{\text{comm}}}({N})$ that division incurs. Fault tolerance and orchestration bound the synchronization and recovery time that no partitioning can remove. The same chapters also set the fleet-level envelope for serving, since replicas draw on the same scheduler, share the same failure rates, and need the same recovery machinery. Together, they develop the algorithmic and operational discipline that turns the physical fleet of Part I into a working distributed system.

Back to top

## Source

[Repository Source](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/books/vol2/parts/distributed_ml_principles.qmd) · [Original License](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/LICENSE.md)

[Rendered Reading Snapshot](https://mlsysbook.ai/vol2/parts/distributed_ml_principles.html#distributed-ml-principles). Rendering provenance is recorded in the import manifest.
