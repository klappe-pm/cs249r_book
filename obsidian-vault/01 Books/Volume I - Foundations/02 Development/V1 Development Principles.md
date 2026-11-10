---
title: V1 Development Principles
type: Part
volume: 1
chapter: 0
publication_status: Released
source_repository: https://github.com/klappe-pm/cs249r_book
source_commit: de87c0103806d7bfb1c677dbb77a2b92fa00c298
source_path: books/vol1/parts/build_principles.qmd
source_anchor: development-principles
source_mode: Source-Correlated Published HTML
tags:
- Type/Part
- Book/Volume_1
rendered_source_url: https://mlsysbook.ai/vol1/parts/build_principles.html
---

# V1 Development Principles

[[Home|Home]] · [[01 Books/Volume I - Foundations/Volume 1 Overview|Volume Overview]]

^development-principles

Building a machine learning system requires more than assembling model components; it requires managing the flow of information and energy through silicon. Part I fixed where a system can run, when its constraints must be known, and how its data is delivered, and it established that data is both the program and a physical anchor of every ML system. With that anchor in place, Part II turns to the algorithm-machine interaction, asking *how* mathematical models are co-designed around the physical limits of the hardware that must execute them. The bitter lesson favors general methods that absorb more computation, but every such method must still fit the machine that runs it. The principles here begin with the accounting that determines why certain architectures succeed while others fail at scale. That accounting, the iron law, has been in use since the introduction; it is stated here as a principle because every chapter of this part measures its decisions against it.

**Principle 3: The iron law of ML systems**

**Decomposition**: Let ${T}$ denote idealized wall-clock time in seconds. Across the D·A·M axes, workload time factors as ${T} = (\text{Samples/Task}) \times (\text{FLOPs/Sample}) \times (\text{Seconds/FLOP})$, where the first two factors multiply to fix total floating-point operations ${O}$. In physical terms, ${D_{\text{vol}}}$ is data volume in bytes, ${\text{BW}}$ is the effective bandwidth of the relevant memory or network path in bytes/s, ${R_{\text{peak}}}$ is peak compute rate in FLOP/s, ${\eta_{\text{hw}}}$ is dimensionless hardware utilization efficiency, and ${L_{\text{lat}}}$ is fixed latency overhead in seconds (such as a kernel launch or network round trip). Unpacking how the machine executes those operations in these terms gives the serialized sum:

$$
{T}\approx \frac{{D_{\text{vol}}}}{{\text{BW}}} + \frac{{O}}{{R_{\text{peak}}} \cdot {\eta_{\text{hw}}}} + {L_{\text{lat}}}
$$

 The full treatment appears in **[[01 Books/Volume I - Foundations/00 Introduction/01 Introduction/V1-01.08 Iron Law of ML Systems#^sec-introduction-iron-law-ml-systems-c32a|Iron Law of ML Systems]]**.

When data movement and compute overlap on modern hardware, wall-clock time follows the critical path and cannot be shorter than the slower of those stages plus any fixed latency that remains outside the overlap. The practical lesson is about dominance, not unconditional summation.

**Implication**: Optimization is rarely free of trade-offs. Reducing one factor or term often shifts the bottleneck to another. For example, skipping zero-valued weights scattered irregularly through a model (unstructured sparsity) reduces $\text{FLOPs/Sample}$ and therefore executed arithmetic ${O}$. The model must then also store and read the positions of the surviving weights, however, and that index traffic can increase data-movement time $({D_{\text{vol}}}/{\text{BW}})$ and inflate realized $\text{Seconds/FLOP}$. An optimization improves wall-clock time only to the extent that it shortens the critical path on the target hardware.

^pri-iron-law

The iron law names the terms that govern execution time, but it does not say which term a given model will stress first. **[[01 Books/Volume I - Foundations/01 Foundations/02 System Paradigms/V1-02 System Paradigms#^sec-ml-systems|System Paradigms]]** examined the hardware’s side of that balance by bounding the bandwidth, peak compute, and latency each deployment tier offers. Choosing a model architecture makes the algorithmic side of the commitment before any code runs.

**Principle 4: The silicon contract**

**Heuristic**: The hardware fixes three time limits, a memory bandwidth ${\text{BW}}$, a peak compute rate ${R_{\text{peak}}}$, and a fixed overhead ${L_{\text{lat}}}$, along with a memory capacity that decides what fits at all. Every model architecture, in each workload regime, commits in advance to saturating one of those limits first.

- **ResNet-50**: Assumes high-density floating-point compute. In batched training or inference on accelerators, it is often compute bound: performance is limited by ${O}/({R_{\text{peak}}} \cdot {\eta_{\text{hw}}})$.
- **GPT-2/Llama**: Assumes high-bandwidth memory access during autoregressive decoding, which generates one token at a time and rereads every weight for each token. At small batch sizes, it is often bandwidth bound: performance is limited by ${D_{\text{vol}}}/{\text{BW}}$.
- **DLRM**: Assumes large embedding tables and sparse lookups. It is shaped by both capacity and bandwidth: performance depends on whether embedding tables fit in the available memory hierarchy and how quickly sparse accesses can be served.

**Implication**: Designing a model without knowing which hardware resource it will saturate is like designing a bridge without knowing the strength of the steel. The design must target the bottleneck.

^pri-silicon-contract

Together, the iron law and the silicon contract frame every design decision in Part II. **[[01 Books/Volume I - Foundations/02 Development/05 Neural Computation/V1-05 Neural Computation#^sec-neural-computation|Neural Computation]]** counts the operations, activations, and gradients that a neural model commits the machine to. **[[01 Books/Volume I - Foundations/02 Development/06 Network Architectures/V1-06 Network Architectures#^sec-network-architectures|Network Architectures]]** shows how arranging those computations sets a model’s arithmetic intensity, and with it the architecture’s side of the contract. **[[01 Books/Volume I - Foundations/02 Development/07 ML Frameworks/V1-07 ML Frameworks#^sec-ml-frameworks|ML Frameworks]]** follows the translation of model operations into hardware execution and locates the fixed overhead that translation spends. **[[01 Books/Volume I - Foundations/02 Development/08 Model Training/V1-08 Model Training#^sec-model-training|Model Training]]** then repeats the resulting step many thousands of times, until memory, time, and cost budgets decide what one machine can train.

Back to top

## Source

[Repository Source](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/books/vol1/parts/build_principles.qmd) · [Original License](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/LICENSE.md)

[Rendered Reading Snapshot](https://mlsysbook.ai/vol1/parts/build_principles.html#development-principles). Rendering provenance is recorded in the import manifest.
