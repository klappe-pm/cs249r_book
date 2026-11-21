---
title: V1 Algorithm Foundations
type: Reference
volume: 1
chapter: 0
publication_status: Released
source_repository: https://github.com/klappe-pm/cs249r_book
source_commit: de87c0103806d7bfb1c677dbb77a2b92fa00c298
source_path: books/vol1/backmatter/appendix_algorithm.qmd
source_anchor: sec-appdx-algorithm-foundations
source_mode: Source-Correlated Published HTML
tags:
- Type/Reference
- Book/Volume_1
rendered_source_url: https://mlsysbook.ai/vol1/backmatter/appendix_algorithm.html
---

# V1 Algorithm Foundations

[[Home|Home]] · [[01 Books/Volume I - Foundations/Volume 1 Overview|Volume Overview]]

^sec-appdx-algorithm-foundations

A profile showing low utilization is often misdiagnosed as a hardware limit when the cause is algorithmic: a matrix multiply shape that underfills matrix arithmetic units, a layout that breaks contiguity, or activation memory held for backpropagation. This appendix collects the computational complexity models, memory footprint derivations, numerical-stability rules, and proofs that the book’s performance chapters lean on. With them, readers can evaluate algorithmic trade-offs before committing code to accelerators. It assumes familiarity with linear algebra and with the iron law introduced early in the book.

## How to Use This Appendix

^how-to-use-this-appendix

This appendix is designed as a reference. Reach for it when translating a profiler symptom (“slow matmul,” “shape mismatch,” “OOM during training”) into a concrete computational or memory cause. Each symptom or need maps to one section ([[05 Reference/Volume I - Foundations/V1 Algorithm Foundations#^tbl-appdx-algorithm-lookup|table 1]]), and conventions throughout follow the book-wide notation (for example, ${B}$ is reserved for batch size and ${\text{BW}}$ denotes bandwidth). Every section names the chapter that teaches its concept in context; the chapter carries the argument, and this appendix carries the derivation or the reference formula.

| **Symptom or need**                                                   | **Section**                                                                                                                                             |
|:----------------------------------------------------------------------|:--------------------------------------------------------------------------------------------------------------------------------------------------------|
| A general matrix multiply (GEMM) runs far below peak throughput       | [[05 Reference/Volume I - Foundations/V1 Algorithm Foundations#^sec-appdx-algorithm-foundations-general-matrix-multiply-gemm-b55d\|section 1.1.3]]         |
| Sparsity is proposed to save memory or compute                        | [[05 Reference/Volume I - Foundations/V1 Algorithm Foundations#^sec-appdx-algorithm-foundations-sparse-matrix-formats-0bd0\|section 1.1.4]]                |
| A layer’s parameters and FLOPs are needed before hardware is chosen   | [[05 Reference/Volume I - Foundations/V1 Algorithm Foundations#^sec-appdx-algorithm-foundations-computational-complexity-cheat-sheet-0c6c\|section 1.1.5]] |
| Tensor code fails on shape or contiguity, or a copy dominates a loop  | [[05 Reference/Volume I - Foundations/V1 Algorithm Foundations#^sec-appdx-algorithm-foundations-shapes-strides-1aea\|section 1.2.1]]                       |
| A broadcast allocates a much larger tensor than intended              | [[05 Reference/Volume I - Foundations/V1 Algorithm Foundations#^sec-appdx-algorithm-foundations-broadcasting-ec16\|section 1.2.2]]                         |
| Gradients look wrong, or the backward pass costs more than expected   | [[05 Reference/Volume I - Foundations/V1 Algorithm Foundations#^sec-appdx-algorithm-foundations-backpropagation-algorithm-93f7\|section 1.3.2]]            |
| Training runs out of memory                                           | [[05 Reference/Volume I - Foundations/V1 Algorithm Foundations#^sec-appdx-algorithm-foundations-true-cost-training-memory-e54e\|section 1.3.3]]            |
| A chain of elementwise operations is memory bound                     | [[05 Reference/Volume I - Foundations/V1 Algorithm Foundations#^sec-appdx-algorithm-foundations-operator-fusion-5d73\|section 1.3.4.2]]                    |
| Softmax overflows, or the loss becomes NaN in reduced precision       | [[05 Reference/Volume I - Foundations/V1 Algorithm Foundations#^sec-appdx-data-foundations-logits-numerical-stability-13e2\|section 1.3.5]]                |
| A bound on gradient cost relative to the forward pass                 | [[05 Reference/Volume I - Foundations/V1 Algorithm Foundations#^sec-appdx-algorithm-baur-strassen\|section 1.4.1]]                                         |
| Attention memory or traffic grows with sequence length                | [[05 Reference/Volume I - Foundations/V1 Algorithm Foundations#^sec-appdx-algorithm-flash-attention\|section 1.4.2]]                                       |
| A compute budget must be split between parameters and training tokens | [[05 Reference/Volume I - Foundations/V1 Algorithm Foundations#^sec-appdx-algorithm-chinchilla-derivation\|section 1.4.3]]                                 |

Table 1: **Where to Look**: Each row pairs a profiler symptom or a design question with the section that carries its derivation or reference formula.

^tbl-appdx-algorithm-lookup

Neural networks turn linear algebra into learned behavior. Matrices transform activations, tensor layouts determine how data move through memory, and backpropagation carries error signals through the resulting computation. These foundations support the deep learning treatment in **[[01 Books/Volume I - Foundations/02 Development/05 Neural Computation/V1-05 Neural Computation#^sec-neural-computation|Neural Computation]]**, the framework internals in **[[01 Books/Volume I - Foundations/02 Development/07 ML Frameworks/V1-07 ML Frameworks#^sec-ml-frameworks|ML Frameworks]]**, and the training strategies in **[[01 Books/Volume I - Foundations/02 Development/08 Model Training/V1-08 Model Training#^sec-model-training|Model Training]]**.

## Linear Algebra

^sec-appdx-algorithm-foundations-linear-algebra-c937

Frameworks such as PyTorch hide raw linear algebra behind single function calls, yet changing a layer’s width or a serving request’s batch size can shift the underlying matrix operations from compute-bound execution to a bandwidth-bound stall without altering a line of model logic. While **[[05 Reference/Volume I - Foundations/V1 Machine Foundations#^sec-appdx-machine-foundations-numerical-representations-c889|Numerical Representations]]** establishes how individual numbers are represented in bits, the primitives below govern how those numbers are combined into contractions, inner products, and dense or sparse matrix multiplies.

**Systems Perspective 1.1: Why this matters**

Many dense neural networks, especially transformers and large convolutional neural networks, spend most of their compute in matrix multiplication or GEMM-like kernels. A self-attention block executes query, key, value, and output projection GEMMs alongside two attention-matrix products for scores and weighted values, and the layer’s feed-forward block adds two or three more. Because those kernels dominate execution, GEMM performance characteristics explain why batch size governs throughput, why aligned layer dimensions run faster than unaligned ones, and whether a dense workload will be compute bound or bandwidth bound before any profiler trace runs.

### Tensor Operations and Einsum Notation

^sec-appdx-algorithm-foundations-tensor-operations-notation-2758

Tensor operations in deep learning contract across batch, head, sequence, and hidden dimensions at once. Einstein summation[[05 Reference/Volume I - Foundations/V1 Algorithm Foundations#^fn1|¹]] notation writes those contractions as a single index string rather than a chain of nested loops and transposes (implemented as `torch.einsum` in PyTorch and `np.einsum` in NumPy). Matrix multiplication ${\mathbf{C}}= {\mathbf{A}}{\mathbf{B}}$ becomes:

$$
{C_{ij}} = \sum_k {A_{ik}} {B_{kj}}
$$

In einsum notation, this is `ik,kj->ij`. The same notation handles batched multi-head attention, `bhid,bhjd->bhij` (batch ${b}$, head ${h}$, query sequence ${i}$, key sequence ${j}$, and head dimension ${d}$). The head dimension ${d}$ appears in both inputs but not in the output, so it is the index that is summed.

### The Dot Product as Similarity

^sec-appdx-algorithm-foundations-dot-product-similarity-7957

Summing over that shared head dimension ${d}$ for a single query vector and a single key vector is a dot product, the primitive that scores how closely two token embeddings or feature vectors align. The sum ${\mathbf{a}}\cdot {\mathbf{b}}= \sum {a}_i {v}_i$ grows when the vectors point in the same direction and vanishes when they are orthogonal because it equals $\|{\mathbf{a}}\| \|{\mathbf{b}}\| \cos {\phi}$. For nonzero vectors, its sign distinguishes acute, right, and obtuse angles, while its magnitude scales with both vector norms.

In attention mechanisms, query (${\mathbf{Q}}$) and key (${\mathbf{K}}$) vectors are dot-produced to compute a similarity score that determines how much each token attends to every other token. The resulting attention weights are then used to form a weighted combination of value (${\mathbf{V}}$) vectors, so every token can draw on every other token. **[[01 Books/Volume I - Foundations/02 Development/06 Network Architectures/V1-06.07 Attention Dynamic Processing#^sec-network-architectures-attention-mechanisms-dynamic-pattern-processing-22df|Attention: Dynamic Processing]]** develops attention itself, including the cost of computing one score for every query-key pair.

### General Matrix Multiply (GEMM)

^sec-appdx-algorithm-foundations-general-matrix-multiply-gemm-b55d

Evaluating those dot products across every query-key pair at once, or projecting a batch of activations through a dense layer, packs individual inner products into a general matrix multiply (GEMM).[[05 Reference/Volume I - Foundations/V1 Algorithm Foundations#^fn2|²]] Whether that GEMM saturates an accelerator’s Tensor Cores or stalls on memory bandwidth depends on its three dimensions: for matrices of size ${M}{\times}{K}$ and ${K}{\times}{N}$, a GEMM performs $2{M} {N} {K}$ floating-point operations (counting multiply-accumulate as two operations).

The arithmetic intensity of GEMM scales linearly with matrix dimension. For square ${N}{\times}{N}$ matrices in FP16 (2 bytes/element), the ideal ${\beta}=0$ bound reads ${\mathbf{A}}$ and ${\mathbf{B}}$ once and writes ${\mathbf{C}}$ once:

$$
\text{Intensity} = \frac{{O}}{{D_{\text{vol}}}} = \frac{2{N}^3}{3{N}^2 \times 2} = \frac{{N}}{3}\text{ FLOP/byte}
$$

Reading the old ${\mathbf{C}}$ when ${\beta}\ne 0$ changes the intensity to ${N}/4$ FLOP/byte. Three consequences follow for GEMM execution:

- **Larger batches can improve efficiency**: Batching increases effective matrix dimensions when it forms larger GEMMs or enables reuse; merely queuing independent small GEMMs does not raise intensity.
- **Aligned dimensions help**: Hardware Tensor Cores are optimized for precision- and architecture-specific tile multiples. Dimensions that align with these multiples avoid padding overhead and improve kernel efficiency, but they do not need to be powers of two.
- **Small matrices are inefficient**: A square GEMM with ${N} =$ 64 has intensity 64/3 ≈ 21.3 FLOP/byte, well below the ridge point of the book’s reference accelerator, the H100 (295.2 FLOP/byte). Its roofline cap is ~7.2 percent of peak; launch and tiling overhead can lower realized throughput. **[[01 Books/Volume I - Foundations/03 Optimization/11 Hardware Acceleration/V1-11.07 Performance Bounds#^sec-hardware-acceleration-roofline-model-42ff|Performance Bounds]]** derives the ridge point and the compute-bound and bandwidth-bound regimes on either side of it, which is the comparison each of these consequences relies on.

### Sparse Matrix Formats

^sec-appdx-algorithm-foundations-sparse-matrix-formats-0bd0

Dense GEMM assumes every weight or feature entry carries signal, yet recommendation tables and heavily pruned weight matrices can be 90 to 99 percent zeros, where a dense tensor wastes gigabytes of memory and bandwidth storing and reading values that contribute nothing to the output. Specialized sparse storage formats avoid storing those zeros and let kernels skip them. The **compressed sparse row (CSR)** format represents a sparse matrix with three arrays:

- `Values`: The nonzero elements, stored in row order
- `Col_Idx`: The column index of each nonzero element
- `Row_Ptr`: The starting position in `Values` for each row (length = num_rows + 1)

CSR is useful for sparse feature matrices in recommendation pipelines and for pruned model weights. For a matrix with ${n_{\text{elem}}}$ elements, ${n_{\text{rows}}}$ rows, and ${n_{\text{nz}}}$ nonzeros, CSR uses $\mathcal{O}({n_{\text{nz}}}+ {n_{\text{rows}}})$ storage instead of $\mathcal{O}({n_{\text{elem}}})$; when ${n_{\text{nz}}}$ is large relative to ${n_{\text{rows}}}$, this is often summarized as $\mathcal{O}({n_{\text{nz}}})$.

To see the trade-off concretely, consider a vocabulary embedding matrix with 100,000 rows and 10,000 columns (1B parameters):

- **Dense (FP32)**: 1B parameters $\times$ 4 bytes each = 4 GB.
- **Sparse** (1 percent density): CSR stores roughly 10M entries $\times$ (4-byte value + 4-byte column index), plus one row pointer per row and a final pointer, totaling ≈ 80.4 MB.
- **Result**: A 50× reduction in memory footprint, fitting a model that would otherwise trigger an out-of-memory (OOM) error.

The saving holds only at low density. Each stored nonzero carries its index, so at high density CSR occupies more memory than the dense tensor it replaces. **[[01 Books/Volume I - Foundations/03 Optimization/10 Model Compression/V1-10.05 Hardware Implementation Changing How the Model Executes#^sec-model-compression-sparse-break-even-7e4a|Storage and execution break-even]]** finds that break-even density for pruned weights, and **[[01 Books/Volume I - Foundations/03 Optimization/11 Hardware Acceleration/V1-11.05 Compute Units#^sec-hardware-acceleration-nm-structured-sparsity-mechanics-9a71|N:M structured sparsity mechanics]]** shows the fixed pattern of two nonzeros in every four that an accelerator datapath decodes without a general index.

### Operation Cost Reference

^sec-appdx-algorithm-foundations-computational-complexity-cheat-sheet-0c6c

Each common layer type reduces to the GEMMs and elementwise operations above, so its parameter count and forward-pass FLOPs follow from its shapes ([[05 Reference/Volume I - Foundations/V1 Algorithm Foundations#^tbl-tensor-op-ref|table 2]]). Given layer dimensions and input shapes, the formulas give first-order estimates of model size and compute before hardware is provisioned. The attention row is the one to watch. Sequence length contributes an ${S}^2$ term, while hidden dimension contributes ${d}^2$ projection work, so long-context models can shift the dominant cost without changing the parameter count.

| **Layer type**                |                       **Output shape**                        |                                    **Parameters (${P}$)**                                    |                                               **FLOPs (per forward pass)**                                                |
|:------------------------------|:-------------------------------------------------------------:|:--------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------------------:|
| **Linear**                    |                   $({B}, {d_{\text{out}}})$                   |       ${d_{\text{in}}} \times {d_{\text{out}}} + {d_{\text{out}}}$ if bias is enabled        |                               $2 \times {B}\times {d_{\text{in}}} \times {d_{\text{out}}}$                                |
| **Conv2D**                    | $({B}, {d_{\text{out}}}, {H_{\text{out}}}, {W_{\text{out}}})$ | ${K}^2 \times {d_{\text{in}}} \times {d_{\text{out}}} + {d_{\text{out}}}$ if bias is enabled | $2 \times {B}\times {H_{\text{out}}} \times {W_{\text{out}}} \times {K}^2 \times {d_{\text{in}}} \times {d_{\text{out}}}$ |
| **Multi-head self-attention** |                       $({B}, {S}, {d})$                       |            $4 \times {d}^2$, plus $4 \times {d}$ if projection biases are enabled            |                                          ${B}\times (4 {S}^2 {d}+ 8 {S} {d}^2)$                                           |
| **LayerNorm**                 |                       $({B}, {S}, {d})$                       |                     $2 \times {d}$ if affine scale and bias are enabled                      |                                          $\mathcal{O}({B}\times {S}\times {d})$                                           |

Table 2: **Deep Learning Tensor Primitives**: Summary of shapes, parameters, and FLOP counts. Note: ${B}$ is batch size, ${S}$ is sequence length, and ${K}$ is kernel size. The attention FLOPs include QKV projections and score interactions. The ${S}^2$ term applies to full-sequence training and prefill, while KV-cached generation is linear per token in cached context; ${d}^2$ projection work dominates at large hidden dimensions.

^tbl-tensor-op-ref

The formulas in [[05 Reference/Volume I - Foundations/V1 Algorithm Foundations#^tbl-tensor-op-ref|table 2]] specify *what* each layer computes and how many operations it performs. Expressing those computations in code raises a second question: how frameworks represent multidimensional arrays in flat memory without copying data unnecessarily.

## Tensor Programming Primitives

^sec-appdx-algorithm-foundations-tensor-programming-primitives-1400

Representing multidimensional arrays in flat memory without copying data is the job of *tensor programming*, the abstraction layer that translates linear algebra into array manipulations on hardware. When that representation is misunderstood, code fails in three characteristic ways: a shape mismatch crashes the run, a transposed tensor loses contiguity and runs at a small fraction of peak throughput, or an unintended broadcast silently allocates gigabytes of memory.

### Shapes, Strides, and Memory Layout

^sec-appdx-algorithm-foundations-shapes-strides-1aea

Transposing or reshaping a gigabyte matrix in PyTorch returns almost instantly because no elements move in memory: frameworks represent a tensor as a view over a flat storage buffer, described by shape, stride, dtype, and offset metadata rather than as a multidimensional array of pointers. Its shape specifies the logical dimensions of the tensor (for example, `(3, 4)`). Its stride defines how many elements to skip in storage to advance one step along each dimension. Only contiguous tensors store their logical elements in a single adjacent block.

Operations like `transpose()` or `view()` often change only the strides, not the data in memory. This is fast ($\mathcal{O}(1)$) but can lead to noncontiguous tensors that fail in kernels requiring contiguous data. In such cases, calling `contiguous()` on a tensor of ${N}$ elements forces an $\mathcal{O}({N})$ memory copy that can dominate runtime if triggered repeatedly inside a loop.

The order of the strides is the tensor’s memory layout. Row-major and column-major layouts of the same matrix differ only in which dimension has stride 1. That choice affects cache efficiency, because iterating along the stride-1 dimension touches contiguous memory locations, which is much faster than strided access.

A common optimization pattern is to materialize a transposed tensor once before repeated operations to ensure contiguous access in the hot loop. The one-time copy cost is amortized across many subsequent operations. **[[01 Books/Volume I - Foundations/02 Development/07 ML Frameworks/V1-07.06 Abstraction Tensors, Devices, and Operations#^sec-ml-frameworks-tensor-structure-dimensions-4a14|Rank, layout, and data type]]** introduces strides and layouts in the framework that manages them, and **[[01 Books/Volume I - Foundations/03 Optimization/11 Hardware Acceleration/V1-11.08 Hardware Mapping#^sec-hardware-acceleration-memoryefficient-tensor-layouts-e250|Memory-efficient tensor layouts]]** shows how the layout choice (channels-last versus channels-first) changes accelerator throughput for convolutions.

### Broadcasting

^sec-appdx-algorithm-foundations-broadcasting-ec16

Zero-copy stride manipulation also powers **broadcasting**, the rule that lets arithmetic operators combine tensors of different shapes without materializing duplicate copies of the smaller input. Frameworks compare dimensions from right to left and treat two dimensions as compatible when they are equal or when one of them is 1. A singleton dimension is then stretched virtually by setting its stride to zero. Yet an unintended singleton alignment, such as adding a $({B}, 1)$ column vector of predictions to a $({B},)$ row vector of targets, silently allocates a $({B}, {B})$ output matrix that can exhaust memory or corrupt a loss calculation.

Adding a $(3, 1)$ column tensor (${\mathbf{A}}$) to a $(1, 4)$ row tensor (${\mathbf{B}}$) expands both virtually across their complementary singleton dimensions and generates a $(3, 4)$ matrix of pairwise sums ${A}_i + {b}_j$ ([[05 Reference/Volume I - Foundations/V1 Algorithm Foundations#^fig-broadcasting-rules|figure 1]]). Dashed cell boundaries mark result elements whose operands are read through stride-0 views, so neither input is copied. Only the $(3, 4)$ output is allocated, and hardware repeatedly accesses identical input buffer addresses.

![[90 Assets/Volume I/Shared Figures/Broadcasting Rules 191f5f4e6e.svg]]

Figure 1: **Tensor Broadcasting Rules**: A (3,1) column and a (1,4) row broadcast across complementary dimensions, producing the pairwise sums in a (3,4) result.

^fig-broadcasting-rules

Consider a concrete case: tensor A has shape `(32, 1, 64)` and tensor B has shape `(1, 128, 64)`. Comparing dimensions right to left, 64 matches 64, then 1 stretches to 128, then 1 stretches to 32, yielding result shape `(32, 128, 64)`. Writing out the expanded shape before running catches silent logic bugs that accidentally allocate a large tensor (for example, a `(Batch, Batch)` matrix instead of an element-wise `(Batch)` vector).

Shapes, strides, and broadcasting govern how tensors flow through a model’s forward pass. Training adds a second requirement, computing how much each parameter contributed to the error. Backpropagation meets that requirement and imposes the memory costs quantified in the training-memory decomposition below.

## Mechanics of Learning

^sec-appdx-algorithm-foundations-mechanics-learning-24f6

Training a neural network takes roughly three times the compute of a forward pass and holds gigabytes of intermediate activations in memory until the backward sweep consumes them. The chain rule and reverse-mode automatic differentiation create both costs by saving forward intermediates to compute every parameter gradient in one backward sweep, while the resulting computational graph exposes where compilers can fuse memory-bound operations and where reduced-precision exponentials at the loss must be stabilized.

**Systems Perspective 1.2: Why this matters**

When training fails (loss goes to NaN, gradients explode, or memory runs out), understanding what backpropagation actually does is essential for diagnosing the problem. The backward graph supplies the mental model for reasoning about gradient flow and memory usage during training.

### The Chain Rule and Automatic Differentiation

^sec-appdx-algorithm-foundations-chain-rule-automatic-differentiation-e0eb

Updating a model with ${P}$ parameters requires the derivative of the scalar loss with respect to every weight, and perturbing one parameter at a time would cost ${P}$ forward passes per training step. Factoring the network as a composition of layers avoids that blowup. For a composed function ${y}= {f}({g}({x}))$, the derivative is $\frac{d{y}}{d{x}} = \frac{d{y}}{d{g}} \cdot \frac{d{g}}{d{x}}$, and for a three-layer network ${y}= {f}_3({f}_2({f}_1({x})))$, the chain rule extends to:

$$
\frac{\partial {y}}{\partial {x}} = \frac{\partial {f}_3}{\partial {f}_2} \cdot \frac{\partial {f}_2}{\partial {f}_1} \cdot \frac{\partial {f}_1}{\partial {x}}
$$

Each factor in this product is a local derivative, computed at one layer using only that layer’s inputs and outputs. This locality keeps the bookkeeping cheap: the entire network never needs to be differentiated as a monolithic function. Instead, each layer computes its own local derivative during the backward pass and multiplies it by the gradient flowing in from the layer above.

Modern frameworks use reverse-mode automatic differentiation, which computes gradients for all ${P}$ parameters in a single backward pass. Starting from the output and working backward (reverse mode) requires one pass regardless of the number of parameters. Starting from each input and working forward (forward mode) would require ${P}$ passes, one per parameter. This is why a training step is a small constant multiple of inference, commonly about 2–3$\times$ a forward pass for dense networks, rather than ${P}$ passes. **[[01 Books/Volume I - Foundations/02 Development/07 ML Frameworks/V1-07.05 Differentiation Automatic Gradient Computation#^sec-ml-frameworks-forward-reverse-mode-differentiation-f70a|Forward and reverse mode]]** shows how frameworks implement both modes and why training uses reverse mode.

### The Backpropagation Algorithm

^sec-appdx-algorithm-foundations-backpropagation-algorithm-93f7

Backpropagation[[05 Reference/Volume I - Foundations/V1 Algorithm Foundations#^fn3|³]] implements the chain rule efficiently through two passes: forward to compute outputs, backward to compute gradients. The gradient edges retrace forward dependencies, meaning each backward step requires intermediate activations retained from the corresponding forward operation. [[05 Reference/Volume I - Foundations/V1 Algorithm Foundations#^fig-backprop-graph|Figure 2]] traces these dual dataflow passes across a two-layer network. Solid gray arrows stage forward activations (${\mathbf{x}}\to {\mathbf{h}}\to {\hat{\mathbf{y}}}$) through weight parameters ${\mathbf{W}}_1$ and ${\mathbf{W}}_2$ to evaluate loss ${\mathcal{L}}$. Curved dashed red arrows propagate intermediate adjoints ($\frac{\partial {\mathcal{L}}}{\partial {\hat{\mathbf{y}}}}, \frac{\partial {\mathcal{L}}}{\partial {\mathbf{h}}}, \frac{\partial {\mathcal{L}}}{\partial {\mathbf{x}}}$) in reverse order.

![[90 Assets/Volume I/Shared Figures/Generated Figure c768208ae0.svg]]

Figure 2: **Backpropagation Computational Graph**: Solid gray arrows carry the forward computation from input ${\mathbf{x}}$ to loss ${\mathcal{L}}$, while dashed red arrows carry gradients backward along the same dependencies.

^fig-backprop-graph

#### Forward Pass

^forward-pass

Using row-vector activations, omitting biases, and retaining intermediate activations for backward execution, computation begins at input ${\mathbf{x}}$. Multiplying ${\mathbf{x}}$ by weight matrix ${\mathbf{W}}_1$ yields hidden activation ${\mathbf{h}}$, which the execution runtime caches for backward differentiation. Multiplying ${\mathbf{h}}$ by ${\mathbf{W}}_2$ produces network output ${\hat{\mathbf{y}}}$, which is similarly cached. Finally, comparing ${\hat{\mathbf{y}}}$ to the target label produces scalar loss ${\mathcal{L}}$.

At this point, forward evaluation is complete, and memory holds input ${\mathbf{x}}$, cached activation ${\mathbf{h}}$, cached prediction ${\hat{\mathbf{y}}}$, and loss ${\mathcal{L}}$. For large models, these retained activation tensors frequently dominate overall memory consumption.

#### Backward Pass

^backward-pass

Gradient propagation begins backward from scalar loss ${\mathcal{L}}$. The loss function evaluates $\frac{\partial {\mathcal{L}}}{\partial {\hat{\mathbf{y}}}}$, the error gradient with respect to the network prediction, which starts the backward pass.

Because ${\hat{\mathbf{y}}} = {\mathbf{h}}\cdot {\mathbf{W}}_2$, the matrix chain rule yields two gradients at this layer:

$$
\frac{\partial {\mathcal{L}}}{\partial {\mathbf{W}}_2} = {\mathbf{h}}^T \cdot \frac{\partial {\mathcal{L}}}{\partial {\hat{\mathbf{y}}}} \qquad \text{(weight gradient—used to update } {\mathbf{W}}_2\text{)}
$$

$$
\frac{\partial {\mathcal{L}}}{\partial {\mathbf{h}}} = \frac{\partial {\mathcal{L}}}{\partial {\hat{\mathbf{y}}}} \cdot {\mathbf{W}}_2^T \qquad \text{(input gradient—passed backward to the previous layer)}
$$

Computing $\frac{\partial {\mathcal{L}}}{\partial {\mathbf{W}}_2}$ requires cached activation ${\mathbf{h}}$ from the forward pass. Activations must remain resident in memory because every layer’s weight gradient depends directly on that layer’s input.

Continuing backward to the first layer, the linear relationship ${\mathbf{h}}= {\mathbf{x}}\cdot {\mathbf{W}}_1$ produces:

$$
\frac{\partial {\mathcal{L}}}{\partial {\mathbf{W}}_1} = {\mathbf{x}}^T \cdot \frac{\partial {\mathcal{L}}}{\partial {\mathbf{h}}}
$$

Each backward step requires two operands: the gradient flowing in from downstream layers $\left(\frac{\partial {\mathcal{L}}}{\partial {\mathbf{h}}}\right)$ and that layer’s cached input (${\mathbf{x}}$). Consequently, the backward pass requires roughly 2$\times$ the forward pass FLOPs: each layer executes two matrix multiplications (one for the parameter gradient, one for the upstream activation gradient) rather than one. **[[01 Books/Volume I - Foundations/02 Development/05 Neural Computation/V1-05.05 Learning Process#^sec-neural-computation-gradient-computation-backpropagation-dacf|Gradient computation and backpropagation]]** teaches the algorithm step by step on a running network. The cached inputs that every backward step needs are the reason training memory exceeds model size, which the next section quantifies.

### Training Memory

^sec-appdx-algorithm-foundations-true-cost-training-memory-e54e

Because the backward pass holds those intermediate activations alongside weights, gradients, and optimizer buffers, training memory is the sum of four components rather than model size alone:

$$
{M_{\text{total}}} = {M_{\text{weights}}} + {M_{\text{gradients}}} + {M_{\text{optimizer}}} + {M_{\text{activations}}}
$$

For a standard Adaptive Moment Estimation (Adam) optimizer ([[05 Reference/Volume I - Foundations/V1 Algorithm Foundations#^ref-kingma2014adam|Kingma and Ba 2015]]) in mixed precision ([[05 Reference/Volume I - Foundations/V1 Algorithm Foundations#^ref-micikevicius2017mixed|Micikevicius et al. 2018]]):

- **Weights**: 2 bytes (FP16/BF16) or 4 bytes (FP32).
- **Gradients**: Same size as weights.
- **Optimizer State**: Adam moments require 8 bytes per parameter; an FP32 master copy adds another 4 bytes, giving 8–12 bytes per parameter.
- **Activations**: Activations typically dominate the dynamic memory footprint during training. A recomputation- or tiled-attention-friendly estimate scales as $\mathcal{O}({B}\times {S}\times {N_L} \times {d})$; a full no-recompute attention implementation also materializes attention-score tensors that scale with ${S}^2$.

To see how these four components interact on a single accelerator, consider a concrete language model. Once the static model state is allocated, the remaining device capacity sets a hard ceiling on the batch size that can run without recomputation.

**Napkin Math 1.1: Worked example: GPT-2 (1.5B) training memory**

**The model**: GPT-2 XL has ${P}=$ $1.5 \times 10^{9}$ parameters, 48 layers, hidden dimension ${d}=$ 1600.

**Model state (fixed per step)**:

- **Weights (BF16)**: $1.5 \times 10^{9}$ $\times$ 2 bytes = 3 GB
- **Gradients (BF16)**: $1.5 \times 10^{9}$ $\times$ 2 bytes = 3 GB
- **Optimizer (FP32 master + momentum + variance)**: $1.5 \times 10^{9}$ $\times$ 12 bytes = 18 GB
- **Total model state**: 24 GB, which fits on an 80 GB-class H100 (85.9 GB in decimal units) but leaves only 61.9 GB for activations.

**Activations (scale with batch)**:

Per-layer retained activations for this quick estimate are approximately $12 \times {B}\times {S}\times {d}$ BF16 elements, or $12 \times {B}\times {S}\times {d}\times 2$ bytes, where ${B}$ is batch size and ${S}$ is sequence length. The factor twelve accounts for the major intermediate tensors retained for backpropagation: input activations, QKV projections ($3{d}$), attention output, FFN intermediate ($4{d}$), and layer norm/dropout masks. This estimate assumes the implementation does not retain the full ${B}\times {N_{\text{heads}}} \times {S}^2$ attention-score tensor, as in recomputation- or tiled-attention-friendly accounting. With 48 layers, batch size 8, and sequence length 1024:

$$
48 \times 12 \times 8 \times 1024 \times 1600 \times 2\text{ bytes } \approx 15.1\text{ GB}
$$

**Systems insight**: Total memory reaches ~39.1 GB under this activation-accounting convention, which fits on one 85.9 GB accelerator. Each additional sample adds ~1.9 GB of activations, so under this quick estimate the remaining capacity fills near batch 32. At batch 64, activations grow to ~120.8 GB, well beyond it. The estimate omits smaller retained tensors such as dropout masks and softmax inputs. The full per-layer count of 34 bytes per token per hidden unit ([[05 Reference/Volume I - Foundations/V1 Algorithm Foundations#^ref-korthikanti2023activation|Korthikanti et al. 2023]]) fills the same room near batch 23, the limit **[[01 Books/Volume I - Foundations/02 Development/08 Model Training/V1-08.07 Pipeline Optimizations#^sec-model-training-putting-together-gpt2-optimization-walkthrough-def7|GPT-2 optimization walkthrough]]** works from. That crossover is the threshold where gradient checkpointing or another memory-saving method becomes necessary; its savings and recomputation overhead depend on checkpoint placement and implementation.

#### Activation Explosion

^sec-appdx-algorithm-foundations-activation-explosion-1da5

While weights are fixed ($\mathcal{O}({P})$), activations grow linearly with batch size and at least linearly with sequence length; implementations that materialize attention scores add an $\mathcal{O}({S}^2)$ component. As the worked example above shows, activation memory can quickly exceed the room left after model state. Gradient checkpointing[[05 Reference/Volume I - Foundations/V1 Algorithm Foundations#^fn4|⁴]] reduces this pressure by storing only selected activations and recomputing the rest during backpropagation ([[05 Reference/Volume I - Foundations/V1 Algorithm Foundations#^ref-chen2016training|Chen et al. 2016]]), and FlashAttention removes the quadratic term by tiling attention ([[05 Reference/Volume I - Foundations/V1 Algorithm Foundations#^ref-dao2022|Dao et al. 2022]]). The same decomposition provides a quick feasibility check: sum the per-parameter model state, add the activation term implied by batch size and sequence length, and compare the total against the accelerator’s capacity. **[[01 Books/Volume I - Foundations/02 Development/08 Model Training/V1-08.04 Computation and Memory Costs of Training#^sec-model-training-optimization-algorithms-c6a9|Optimizers and their memory]]** applies the model-state terms to optimizer choice, and **[[01 Books/Volume I - Foundations/02 Development/08 Model Training/V1-08.04 Computation and Memory Costs of Training#^sec-model-training-backpropagation-mechanics-0b64|Backpropagation and activation memory]]** develops the activation term, with **[[01 Books/Volume I - Foundations/02 Development/08 Model Training/V1-08.07 Pipeline Optimizations#^sec-model-training-activation-checkpointing-2ee1|Activation checkpointing]]** teaching the recomputation trade-off for the training loop.

### Computational Graphs and Optimization

^sec-appdx-algorithm-foundations-computational-graphs-optimization-ab43

Running a chain of small operations one kernel at a time forces every intermediate tensor out to high-bandwidth memory and back, even when the next operation immediately consumes it. Because the dependency structure exposed by backpropagation records which operations feed which, ML compilers can represent the model as a directed acyclic graph (DAG) and rewrite those memory round-trips before generating device code.

#### Static Single Assignment

^sec-appdx-algorithm-foundations-static-single-assignment-9e88

To transform a DAG safely, a compiler must know which write each read depends on. Static single-assignment (SSA) form makes those dependencies explicit by assigning each variable exactly once rather than overwriting tensor variables in place, enabling safe transformations such as operator fusion.

#### Operator Fusion

^sec-appdx-algorithm-foundations-operator-fusion-5d73

Without fusion, each operation in a chain like `MatMul → Add (bias) → ReLU` produces an intermediate tensor that is written to high-bandwidth memory (HBM) and then read back for the next operation. For elementwise operations like `Add` and `ReLU`, the compute is trivial (one FLOP per element) but the memory traffic is not (read the tensor, write it back). The arithmetic intensity of unfused elementwise operations is therefore close to zero, which makes them strongly memory bound.

Fusion combines consecutive operations into a single kernel that reads the input once, applies all operations in registers or shared memory, and writes the final result once. For a sequence of ${n_{\text{ops}}}$ elementwise operations on a tensor of ${N}$ elements of ${s_{\text{elem}}}$ bytes each, fusion reduces memory traffic from $2{n_{\text{ops}}} {N}{s_{\text{elem}}}$ bytes (each operation reads and writes) to $2{N}{s_{\text{elem}}}$ bytes (one read, one write), a ${n_{\text{ops}}}\times$ reduction. **[[01 Books/Volume I - Foundations/02 Development/07 ML Frameworks/V1-07.04 Execution from Graphs to Kernels#^sec-ml-frameworks-execution-strategy-matters-memory-wall-1ce8|The memory wall and kernel fusion]]** develops fusion as a framework decision, and **[[01 Books/Volume I - Foundations/03 Optimization/11 Hardware Acceleration/V1-11.08 Hardware Mapping#^sec-hardware-acceleration-kernel-fusion-7faf|Kernel fusion on the accelerator]]** shows the accelerator-side limits on how much a single kernel can fuse.

FlashAttention is fusion applied to attention. It computes the score, softmax, and value-product stages in SRAM tiles without materializing the full attention matrix in HBM, which reduces auxiliary attention memory from $\mathcal{O}({S}^2)$ to $\mathcal{O}({S})$ for a fixed head dimension ([[05 Reference/Volume I - Foundations/V1 Algorithm Foundations#^ref-dao2022|Dao et al. 2022]]). [[05 Reference/Volume I - Foundations/V1 Algorithm Foundations#^sec-appdx-algorithm-flash-attention|Section 1.4.2]] derives the traffic bound step by step, and **[[01 Books/Volume I - Foundations/02 Development/08 Model Training/V1-08.07 Pipeline Optimizations#^sec-model-training-flash-attention-ioaware-attention-optimization-3da0|FlashAttention: IO-aware attention optimization]]** applies the algorithm to training.

Fused and tiled kernels keep results exact while moving fewer bytes. The softmax at the end of the forward pass raises a different question, whether its results stay finite at all.

### Logits and Numerical Stability

^sec-appdx-data-foundations-logits-numerical-stability-13e2

A classifier’s forward pass ends in a softmax over the final layer’s outputs, and the cross-entropy loss is computed from that softmax. The softmax exponentiates those outputs, and the exponential of a large output exceeds the range of every reduced-precision format, so the softmax is a common overflow site in reduced-precision training.

Neural-network classifiers commonly output a vector of *logits*[[05 Reference/Volume I - Foundations/V1 Algorithm Foundations#^fn5|⁵]] ${\mathbf{z}}$ (unnormalized scores). For class index ${j}$, softmax normalizes ${z}_{{j}}$ over all class indices ${k}$ to produce a probability:

$$
\text{Softmax}({z}_{{j}}) = \frac{e^{{z}_{{j}}}}{\sum_{{k}} e^{{z}_{{k}}}}
$$

The problem is that if ${z}_{{j}}$ is large (for example, 100), the exponential $e^{{z}_{{j}}}$ overflows common training and inference formats such as FP32, BF16, and FP16. FP64 can represent this specific value, but production ML kernels rarely use FP64 for softmax. The fix is to subtract the largest logit before exponentiating, the log-sum-exp trick. The shift leaves the result mathematically unchanged and keeps every exponent at or below zero, as the worked example below illustrates for realistic logit values.[[05 Reference/Volume I - Foundations/V1 Algorithm Foundations#^fn6|⁶]]

**Napkin Math 1.2: Log-sum-exp in action**

**Setup**: A three-class classifier outputs logits ${\mathbf{z}}=$ $[100, 101, 102]$.

**Without the trick (naive softmax)**:

$$
\text{ $\exp(100) \approx 2.7 \times 10^{43}$, $\exp(101) \approx 7.3 \times 10^{43}$, $\exp(102) \approx 2.0 \times 10^{44}$}
$$

These numbers are representable in FP64 but overflow FP32 (max $\approx 3.4 \times 10^{38}$). With FP16 (max $\approx 65{,}504$), even $e^{12}$ overflows. Raw logits rarely reach magnitude 100, but large intermediate values do arise (for example, unscaled attention scores or overconfident outputs). Because FP16 and BF16 are the standard training precisions, a naive softmax risks overflow often enough that the stable form is used by default.

**With the trick**: Subtract ${m} = \max({\mathbf{z}}) =$ 102:

Shifted logits: ${\mathbf{z}}- {m} =$ $[-2, -1, 0]$

Exponentials: $\exp(-2) \approx 0.135$, $\exp(-1) \approx 0.368$, $\exp(0) = 1.0$

Sum = 1.503. LogSumExp = 102 $+ \log(1.503) = 102.408$.

Softmax: $[0.135/1.503,\; 0.368/1.503,\; 1.0/1.503] = [0.090,\; 0.245,\; 0.665]$

**Systems insight**: The exponentiated shifted values and the resulting softmax probabilities are in $[0, 1]$, so nothing overflows, even in FP16.

**[[01 Books/Volume I - Foundations/02 Development/05 Neural Computation/V1-05.05 Learning Process#^sec-neural-computation-crossentropy-classification-loss-functions-7def|Cross-entropy and classification loss functions]]** builds the cross-entropy loss on this stable softmax. The same maximum subtraction reappears, generalized to tiles of a long sequence, in the tiled-attention derivation of [[05 Reference/Volume I - Foundations/V1 Algorithm Foundations#^sec-appdx-algorithm-flash-attention|section 1.4.2]], one of the three proofs that close this appendix.

## Derivations

^sec-appdx-algorithm-foundations-derivations-4b1d

The earlier sections used three results that the chapters rely on without proof: that reverse-mode differentiation costs a small constant multiple of a forward pass rather than scaling with parameter count, that tiled attention can normalize across blocks without materializing an ${S} \times {S}$ matrix in HBM, and that a fixed training compute budget splits predictably between model parameters and dataset tokens. Each derivation below proves one of those bounds and states its systems consequence.

### Cost of Reverse-Mode Differentiation

^sec-appdx-algorithm-baur-strassen

Perturbing each of ${N}$ parameters one by one to measure its effect on the loss requires ${N}$ forward evaluations, yet backpropagation computes all ${N}$ partial derivatives of a scalar loss in a small constant multiple of a single forward pass, whether ${N}$ is a thousand or a hundred billion. Baur and Strassen proved in 1983 that this dimension-free ratio holds for any scalar function on a computational graph: computing a function together with its full gradient takes at most four times the operations of the function alone when every operation counts, and at most three times when only multiplications and divisions count ([[05 Reference/Volume I - Foundations/V1 Algorithm Foundations#^ref-baur1983complexity|Baur and Strassen 1983]]). The per-operation accounting below is simpler than their construction and proves the looser constant of five.

#### Statement

^sec-appdx-algorithm-baur-strassen-statement

Let ${f}: \mathbb{R}^{N}\to \mathbb{R}$ be a multivariate scalar-valued function represented as a computational graph ${G}= ({V}, {E})$ consisting of ${W}({f})$ elementary operations (additions, subtractions, multiplications, divisions, and unary functions such as $\exp, \ln, \sin, \sqrt{\cdot}$).

**Theorem 1.1: Cheap-gradient bound**

If a scalar function ${f}: \mathbb{R}^{N}\to \mathbb{R}$ can be computed in ${W}({f})$ elementary operations, then the full gradient vector $\nabla {f}({\mathbf{x}}) = \left(\frac{\partial {f}}{\partial {x}_1}, \frac{\partial {f}}{\partial {x}_2}, \dots, \frac{\partial {f}}{\partial {x_N}}\right)^T \in \mathbb{R}^{N}$ can be evaluated in total work $\text{Work}_{\text{Reverse}}({f}, \nabla {f})$ satisfying:

$$
\text{Work}_{\text{Reverse}}({f}, \nabla {f}) \le {C}\cdot {W}({f})
$$

 where ${C}\le 5$ is a universal constant independent of the input dimension ${N}$. Furthermore, the backward pass alone requires work $\text{Work}_{\text{Backward}}(\nabla {f}) \le 4 \cdot {W}({f})$.

#### Proof

^sec-appdx-algorithm-baur-strassen-proof

Let the computational graph ${G}= ({V}, {E})$ be topologically ordered with nodes ${v_{1-N}}, \dots, {v}_0, {v}_1$, ${v}_2, \dots, {v_W}$. The input variables are ${x}_{{m}} = {v_{i-N}}$ for ${m}\in \{1, \dots, {N}\}$ and the final output is ${f}({\mathbf{x}}) = {v_W}$. Each intermediate node ${v}_j$ is evaluated via a primitive operation:

$$
{v}_j = {\phi}_j\left( \{ {v}_k \mid {k}\in \text{Parents}({j}) \} \right)
$$

Define the *adjoint variable* ${\bar{v}}_i$ for every node ${v}_i$ as the partial derivative of the scalar output ${v_W}$ with respect to ${v}_i$:

$$
{\bar{v}}_i \triangleq \frac{\partial {f}}{\partial {v}_i} = \frac{\partial {v_W}}{\partial {v}_i}
$$

By the multivariate chain rule, the adjoint ${\bar{v}}_i$ is the sum of partial derivatives propagated from all successor nodes (children) that consume ${v}_i$:

$$
{\bar{v}}_i = \sum_{j \in \text{Children}(i)} {\bar{v}}_j \cdot \frac{\partial {v}_j}{\partial {v}_i}
$$

Reverse-mode automatic differentiation initializes ${\bar{v}_W} = 1$ and ${\bar{v}}_i = 0$ for all ${i}< {W}$, then traverses the nodes in reverse topological order from ${v_W}$ down to ${v}_1$. For each primitive node ${v}_j$, its fully accumulated adjoint ${\bar{v}}_j$ propagates error signals to its parent nodes ${v}_k$ (${k}\in \text{Parents}({j})$) via:

$$
{\bar{v}}_k \gets {\bar{v}}_k + {\bar{v}}_j \cdot \frac{\partial {v}_j}{\partial {v}_k}
$$

We bound the backward cost one operation type at a time:

1.  **Addition/Subtraction (${v}_j = {v}_i \pm {v}_k$)**:
    - Local derivatives: $\frac{\partial {v}_j}{\partial {v}_i} = 1$, $\frac{\partial {v}_j}{\partial {v}_k} = \pm 1$.
    - Backward updates: ${\bar{v}}_i \gets {\bar{v}}_i + {\bar{v}}_j$ and ${\bar{v}}_k \gets {\bar{v}}_k \pm {\bar{v}}_j$.
    - Cost: 2 additions in backward pass for 1 forward operation. Work ratio: $\text{Fwd}(1) + \text{Bwd}(2) = 3 \text{ OPs} \le 5 \cdot 1$.
2.  **Multiplication (${v}_j = {v}_i \cdot {v}_k$)**:
    - Local derivatives: $\frac{\partial {v}_j}{\partial {v}_i} = {v}_k$, $\frac{\partial {v}_j}{\partial {v}_k} = {v}_i$.
    - Backward updates: ${\bar{v}}_i \gets {\bar{v}}_i + {\bar{v}}_j \cdot {v}_k$ and ${\bar{v}}_k \gets {\bar{v}}_k + {\bar{v}}_j \cdot {v}_i$.
    - Cost: 2 multiplications + 2 additions = 4 operations in backward pass for 1 forward operation. Work ratio: $\text{Fwd}(1) + \text{Bwd}(4) = 5 \text{ OPs} \le 5 \cdot 1$.
3.  **Division (${v}_j = {v}_i/{v}_k$)**:
    - Local derivatives: $\frac{\partial {v}_j}{\partial {v}_i} = \frac{1}{{v}_k}$, $\frac{\partial {v}_j}{\partial {v}_k} = -\frac{{v}_i}{{v}_k^2} = -\frac{{v}_j}{{v}_k}$.
    - Backward updates: ${\bar{v}}_i \gets {\bar{v}}_i + \frac{{\bar{v}}_j}{{v}_k}$ and ${\bar{v}}_k \gets {\bar{v}}_k - \frac{{\bar{v}}_j \cdot {v}_j}{{v}_k}$.
    - Cost: Compute the quotient of the incoming adjoint and the denominator once, then reuse it in both updates. Add it to the numerator adjoint, and multiply it by the cached forward output before subtracting from the denominator adjoint. This requires 2 multiplications/divisions + 2 additions = 4 operations in backward pass for 1 forward operation. Work ratio: $\text{Fwd}(1) + \text{Bwd}(4) = 5 \text{ OPs} \le 5 \cdot 1$.
4.  **Unary transcendental operations (${v}_j = {\phi}({v}_i)$)**:
    - Local derivative: $\frac{\partial {v}_j}{\partial {v}_i} = {\phi}'({v}_i)$.
    - Backward update: ${\bar{v}}_i \gets {\bar{v}}_i + {\bar{v}}_j \cdot {\phi}'({v}_i)$.
    - For ${v}_j = \exp({v}_i)$, ${\phi}'({v}_i) = {v}_j$, requiring 1 multiplication + 1 addition = 2 OPs.
    - For ${v}_j = \ln({v}_i)$, ${\phi}'({v}_i) = 1/{v}_i$, requiring 1 division + 1 addition = 2 OPs.

Summing across all primitive nodes in ${G}$, every forward operation generates at most 4 backward operations:

$$
\text{Work}_{\text{Backward}}(\nabla {f}) \le 4 \cdot {W}({f})
$$

Adding the forward pass work ${W}({f})$ yields the total work bound:

$$
\text{Work}_{\text{Reverse}}({f}, \nabla {f}) = {W}({f}) + \text{Work}_{\text{Backward}}(\nabla {f}) \le 5 \cdot {W}({f}) \qquad\blacksquare
$$

**Systems Perspective 1.3: Why 175B-parameter large language models can be trained**

The independence of ${C}\le 5$ from input dimension ${N}$ is the mathematical reason deep learning works. Consider training a transformer model with ${P}= 175 \times 10^9$ parameters:

- **Forward pass**: Matrix multiplications ${\mathbf{Y}}= {\mathbf{X}}{\mathbf{W}}$ require $2{P}$ FLOPs per token.
- **Reverse-mode backward pass**: Computes both weight gradients $\frac{\partial {\mathcal{L}}}{\partial {\mathbf{W}}} = {\mathbf{X}}^T \frac{\partial {\mathcal{L}}}{\partial {\mathbf{Y}}}$ ($2{P}$ FLOPs) and input activation gradients $\frac{\partial {\mathcal{L}}}{\partial {\mathbf{X}}} = \frac{\partial {\mathcal{L}}}{\partial {\mathbf{Y}}} {\mathbf{W}}^T$ ($2{P}$ FLOPs), totaling $4{P}$ FLOPs per token.
- **Total training work**: $2{P}(\text{fwd}) + 4{P}(\text{bwd}) = 6{P}$ FLOPs per token. The backward compute factor is exactly $\frac{4{P}}{2{P}} = 2$, so forward plus backward costs three times the forward pass, within both the bound of ${C}\le 5$ proved here and Baur and Strassen’s sharper constant of four.

If we instead used forward-mode automatic differentiation (AD) or finite differences to compute $\nabla {f}\in \mathbb{R}^{P}$, evaluating each partial derivative separately would require ${P}$ forward passes: $\text{Work}_{\text{ForwardMode}}(\nabla {f}) = \mathcal{O}({P}\cdot {W}) = \mathcal{O}({P}^2)$ FLOPs. For ${P}= 175 \times 10^9$, that method would require $2 \times (175 \times 10^9)^2 \approx 6.1 \times 10^{22}$ FLOPs per token, ${P}$ times the forward-pass work and therefore prohibitive at this scale. Reverse-mode AD replaces this $\mathcal{O}({P})$ factor with a constant multiplier of 2 for the dense-layer accounting above.

Reverse mode achieves this constant factor by keeping the forward pass’s intermediate values for the backward sweep, which is why the training-memory decomposition in [[05 Reference/Volume I - Foundations/V1 Algorithm Foundations#^sec-appdx-algorithm-foundations-true-cost-training-memory-e54e|section 1.3.3]] carries an activation term. Attention adds an intermediate whose size grows with the square of the sequence length, the subject of the next derivation.

### Tiled Attention and Online Softmax

^sec-appdx-algorithm-flash-attention

Standard self-attention in transformers requires materializing an ${S}\times {S}$ attention score matrix in HBM, creating an $\mathcal{O}({S}^2)$ memory bandwidth bottleneck. FlashAttention ([[05 Reference/Volume I - Foundations/V1 Algorithm Foundations#^ref-dao2022|Dao et al. 2022]]) reduces this bottleneck by tiling query, key, and value matrices and recomputing attention using an online softmax recurrence without materializing intermediate scores to HBM. **[[01 Books/Volume I - Foundations/02 Development/08 Model Training/V1-08.07 Pipeline Optimizations#^sec-model-training-flash-attention-ioaware-attention-optimization-3da0|FlashAttention: IO-aware attention optimization]]** applies the algorithm to training. This subsection proves the online softmax recurrence it relies on and then its memory-traffic bound.

#### Memory Traffic of Standard Attention

^sec-appdx-algorithm-flash-attention-hbm-bottleneck

Given queries ${\mathbf{Q}}\in \mathbb{R}^{{S}\times {d_{\text{head}}}}$, keys ${\mathbf{K}}\in \mathbb{R}^{{S}\times {d_{\text{head}}}}$, and values ${\mathbf{V}}\in \mathbb{R}^{{S}\times {d_{\text{head}}}}$ for sequence length ${S}$ and head dimension ${d_{\text{head}}}$, standard attention evaluates:

$$
{\mathbf{S}}= {\mathbf{Q}}{\mathbf{K}}^T \in \mathbb{R}^{{S}\times {S}}, \qquad {\mathbf{A}}= \text{softmax}({\mathbf{S}}) \in \mathbb{R}^{{S}\times {S}}, \qquad {\mathbf{O}}= {\mathbf{A}}{\mathbf{V}}\in \mathbb{R}^{{S}\times {d_{\text{head}}}}
$$

To prevent numerical overflow, row-wise softmax subtracts the row maximum (the log-sum-exp shift of [[05 Reference/Volume I - Foundations/V1 Algorithm Foundations#^sec-appdx-data-foundations-logits-numerical-stability-13e2|section 1.3.5]]) ${m}_i = \max_{1 \le j \le {S}} {S_{ij}}$:

$$
{A_{ij}} = \frac{\exp({S_{ij}} - {m}_i)}{\sum_{k=1}^{S}\exp({S_{ik}} - {m}_i)}
$$

Standard GPU implementations execute this in three discrete kernel launches:

1.  Compute ${\mathbf{S}}= {\mathbf{Q}}{\mathbf{K}}^T$ in SRAM, then write ${\mathbf{S}}\in \mathbb{R}^{{S}\times {S}}$ to HBM (${\Theta}({S}^2)$ writes).
2.  Read ${\mathbf{S}}$ from HBM, compute row max ${m}$ and row sum ${z}$, compute ${\mathbf{A}}= \text{softmax}({\mathbf{S}})$, write ${\mathbf{A}}\in \mathbb{R}^{{S}\times {S}}$ to HBM (${\Theta}({S}^2)$ reads + writes).
3.  Read ${\mathbf{A}}$ and ${\mathbf{V}}$ from HBM, compute ${\mathbf{O}}= {\mathbf{A}}{\mathbf{V}}$, write ${\mathbf{O}}\in \mathbb{R}^{{S}\times {d_{\text{head}}}}$ to HBM (${\Theta}({S}^2 + {S}{d_{\text{head}}})$ reads + writes).

Total HBM memory traffic is ${\Theta}({S}^2 + {S}{d_{\text{head}}})$ elements. For ${S}=$ 8192, ${d_{\text{head}}} = 128$ in FP16, ${\mathbf{S}}$ requires $8192^2 \times 2 \text{ B} = 134 \text{ MB}$ per head per layer. Because modern GPUs have high compute throughput relative to HBM bandwidth, repeatedly reading and writing intermediate matrices ${\mathbf{S}}$ and ${\mathbf{A}}$ leaves GPU execution units memory-bound.

#### Online Softmax Recurrence

^sec-appdx-algorithm-flash-attention-online-softmax-proof

Tiling softmax is difficult because computing ${z}_i = \sum_{k=1}^{{S}} \exp({S_{ik}} - {m}_i)$ requires the global maximum ${m}_i$ across all ${S}$ keys. The online softmax recurrence solves this by incrementally updating normalization statistics as sub-blocks arrive.

**Theorem 1.2: Online softmax recurrence theorem**

Let a vector ${\mathbf{x}}\in \mathbb{R}^{n}$ be partitioned into two sub-vectors ${\mathbf{x}}^{(1)} \in \mathbb{R}^{{n}_1}$ and ${\mathbf{x}}^{(2)} \in \mathbb{R}^{{n}_2}$ with ${n}= {n}_1 + {n}_2$. Let the local statistics for block 1 be:

$$
{m}^{(1)} = \max_{1 \le j \le {n}_1} {x}_j^{(1)}, \qquad {z}^{(1)} = \sum_{j=1}^{{n}_1} \exp\left({x}_j^{(1)} - {m}^{(1)}\right)
$$

 and for block 2 be:

$$
{m}^{(2)} = \max_{1 \le j \le {n}_2} {x}_j^{(2)}, \qquad {z}^{(2)} = \sum_{j=1}^{{n}_2} \exp\left({x}_j^{(2)} - {m}^{(2)}\right)
$$

Then the combined maximum ${m^{\text{new}}}$, normalization sum ${z^{\text{new}}}$, and accumulated output vector ${\mathbf{O}^{\text{new}}}$ satisfy the exact recurrence relations:

$$
\begin{aligned} {m^{\text{new}}} &= \max\left({m}^{(1)}, {m}^{(2)}\right), \\ {z^{\text{new}}} &= {z}^{(1)} e^{{m}^{(1)} - {m^{\text{new}}}} + {z}^{(2)} e^{{m}^{(2)} - {m^{\text{new}}}}, \\ {\mathbf{O}^{\text{new}}} &= \frac{{z}^{(1)} e^{{m}^{(1)} - {m^{\text{new}}}}}{{z^{\text{new}}}} {\mathbf{O}}^{(1)} + \frac{e^{{m}^{(2)} - {m^{\text{new}}}}}{{z^{\text{new}}}} \sum_{j=1}^{{n}_2} e^{{x}_j^{(2)} - {m}^{(2)}} {\mathbf{V}}_j^{(2)}, \end{aligned}
$$

 where ${\mathbf{O}}^{(1)} = \frac{1}{{z}^{(1)}} \sum_{j=1}^{{n}_1} e^{{x}_j^{(1)} - {m}^{(1)}} {\mathbf{V}}_j^{(1)}$ is the partial output accumulated from block 1.

##### Denominator Recurrence

^denominator-recurrence

Expanding the combined sum ${z^{\text{new}}} = \sum_{j=1}^{n} e^{{x}_j - {m^{\text{new}}}}$:

$$
\begin{aligned} {z^{\text{new}}} &= \sum_{j=1}^{{n}_1} e^{{x}_j^{(1)} - {m^{\text{new}}}} + \sum_{j=1}^{{n}_2} e^{{x}_j^{(2)} - {m^{\text{new}}}} \\ &= \sum_{j=1}^{{n}_1} e^{\left({x}_j^{(1)} - {m}^{(1)}\right) + \left({m}^{(1)} - {m^{\text{new}}}\right)} + \sum_{j=1}^{{n}_2} e^{\left({x}_j^{(2)} - {m}^{(2)}\right) + \left({m}^{(2)} - {m^{\text{new}}}\right)} \\ &= e^{{m}^{(1)} - {m^{\text{new}}}} \underbrace{\sum_{j=1}^{{n}_1} e^{{x}_j^{(1)} - {m}^{(1)}}}_{{z}^{(1)}} + e^{{m}^{(2)} - {m^{\text{new}}}} \underbrace{\sum_{j=1}^{{n}_2} e^{{x}_j^{(2)} - {m}^{(2)}}}_{{z}^{(2)}} \\ &= {z}^{(1)} e^{{m}^{(1)} - {m^{\text{new}}}} + {z}^{(2)} e^{{m}^{(2)} - {m^{\text{new}}}}. \quad \blacksquare \end{aligned}
$$

##### Output Rescaling Recurrence

^output-rescaling-recurrence

The true normalized output over the concatenated sequence is ${\mathbf{O}^{\text{new}}} = \frac{1}{{z^{\text{new}}}} \sum_{j=1}^{n} e^{{x}_j - {m^{\text{new}}}} {\mathbf{V}}_j$:

$$
\begin{aligned} {\mathbf{O}^{\text{new}}} &= \frac{1}{{z^{\text{new}}}} \left[ \sum_{j=1}^{{n}_1} e^{{x}_j^{(1)} - {m^{\text{new}}}} {\mathbf{V}}_j^{(1)} + \sum_{j=1}^{{n}_2} e^{{x}_j^{(2)} - {m^{\text{new}}}} {\mathbf{V}}_j^{(2)} \right] \\ &= \frac{1}{{z^{\text{new}}}} \left[ e^{{m}^{(1)} - {m^{\text{new}}}} \sum_{j=1}^{{n}_1} e^{{x}_j^{(1)} - {m}^{(1)}} {\mathbf{V}}_j^{(1)} + e^{{m}^{(2)} - {m^{\text{new}}}} \sum_{j=1}^{{n}_2} e^{{x}_j^{(2)} - {m}^{(2)}} {\mathbf{V}}_j^{(2)} \right] \end{aligned}
$$

Noting that ${z}^{(1)} {\mathbf{O}}^{(1)} = \sum_{j=1}^{{n}_1} e^{{x}_j^{(1)} - {m}^{(1)}} {\mathbf{V}}_j^{(1)}$, we substitute this directly:

$$
{\mathbf{O}^{\text{new}}} = \frac{{z}^{(1)} e^{{m}^{(1)} - {m^{\text{new}}}}}{{z^{\text{new}}}} {\mathbf{O}}^{(1)} + \frac{e^{{m}^{(2)} - {m^{\text{new}}}}}{{z^{\text{new}}}} \sum_{j=1}^{{n}_2} e^{{x}_j^{(2)} - {m}^{(2)}} {\mathbf{V}}_j^{(2)}. \quad \blacksquare
$$

#### Memory Traffic of Tiled Attention

^sec-appdx-algorithm-flash-attention-complexity-proof

The recurrence lets each query tile be combined with one key-value tile at a time, so score tiles never need to leave SRAM. The remaining question is how many bytes then cross the HBM boundary.

Let ${M_{\text{SRAM}}}$ be the fast SRAM capacity (in words). Following Algorithm 1 of Dao et al. ([[05 Reference/Volume I - Foundations/V1 Algorithm Foundations#^ref-dao2022|2022]]), FlashAttention sets ${B_c} = \lfloor {M_{\text{SRAM}}}/(4{d_{\text{head}}}) \rfloor$ and ${B_r} = \min(\lfloor {M_{\text{SRAM}}}/(4{d_{\text{head}}}) \rfloor,{d_{\text{head}}})$. The proof abstracts constant factors and buffer reuse, using ${B_c}={\Theta}({M_{\text{SRAM}}}/{d_{\text{head}}})$, ${B_r}={\Theta}(\min({M_{\text{SRAM}}}/{d_{\text{head}}},{d_{\text{head}}}))$, and ${B_r}{B_c}=\mathcal{O}({M_{\text{SRAM}}})$ for the on-chip working set.

The algorithm partitions ${\mathbf{Q}}$ into ${T_r} = \lceil {S}/{B_r} \rceil$ blocks of size ${B_r} \times {d_{\text{head}}}$. It also partitions ${\mathbf{K}}, {\mathbf{V}}$ into ${T_c} = \lceil {S}/{B_c} \rceil$ blocks of size ${B_c} \times {d_{\text{head}}}$. The algorithm then executes two nested loops:

- **Outer loop** over ${j}= 1, \dots, {T_c}$: Load ${\mathbf{K}}_j$ and ${\mathbf{V}}_j$ into SRAM.
- **Inner loop** over ${i}= 1, \dots, {T_r}$: Load ${\mathbf{Q}}_i$, ${\mathbf{O}}_i$, and its softmax statistics; compute ${\mathbf{S}_{ij}} = {\mathbf{Q}}_i {\mathbf{K}}_j^T$ in SRAM; then update and write ${\mathbf{O}}_i$ and the statistics without materializing ${\mathbf{S}_{ij}}$ in HBM.

This loop order is the source of the I/O reduction. A key-value tile remains resident while the algorithm visits every query tile, so each element of ${\mathbf{K}}$ and ${\mathbf{V}}$ crosses the HBM boundary once. The query and output tiles must be revisited for each key-value block, but the ${B_r}\times {B_c}$ score tile is consumed on chip and discarded. Standard attention instead writes and rereads the full ${S}\times {S}$ score and probability matrices.

##### Total Memory Access Accounting

^total-memory-access-accounting

Total HBM accesses comprise two components. The first is key and value reads, where each element of ${\mathbf{K}}$ and ${\mathbf{V}}$ is loaded once (contributing $2{S}{d_{\text{head}}}$ accesses). The second is query, output, and statistics passes, where each of the ${T_c}$ column blocks reads all of ${\mathbf{Q}}$, reads and writes ${\mathbf{O}}$, and updates $\mathcal{O}({S})$ softmax statistics. The matrices dominate the statistics for head dimension ${d_{\text{head}}}\geq 1$, so each pass contributes ${\Theta}({S}{d_{\text{head}}})$ accesses and all passes contribute ${\Theta}({S}{d_{\text{head}}} {T_c})$.

Because ${T_c}=\lceil {S}/{B_c}\rceil={\Theta}({S}{d_{\text{head}}}/{M_{\text{SRAM}}})$, the total is

$$
\text{HBM}_{\text{Flash}} = {\Theta}\left({S}{d_{\text{head}}} + {S}{d_{\text{head}}} {T_c}\right) = {\Theta}\left({S}{d_{\text{head}}} + \frac{{S}^2 {d_{\text{head}}}^2}{{M_{\text{SRAM}}}}\right) = {\Theta}\left(\frac{{S}^2 {d_{\text{head}}}^2}{{M_{\text{SRAM}}}}\right),
$$

 where the final equality follows for ${d_{\text{head}}} \leq {M_{\text{SRAM}}}\leq {S}{d_{\text{head}}}$.

The bound counts communication rather than arithmetic. FlashAttention still evaluates the same dense score blocks and may recompute intermediate quantities during backpropagation; its advantage comes from keeping those intermediates out of HBM.

##### I/O Reduction Ratio

^io-reduction-ratio

Comparing standard attention I/O to FlashAttention I/O:

$$
\frac{\text{HBM}_{\text{Standard}}}{\text{HBM}_{\text{Flash}}} = \frac{{\Theta}({S}^2 + {S}{d_{\text{head}}})}{{\Theta}\left({S}{d_{\text{head}}} + \frac{{S}^2 {d_{\text{head}}}^2}{{M_{\text{SRAM}}}}\right)} = {\Theta}\left(\frac{{M_{\text{SRAM}}}}{{d_{\text{head}}}^2}\right) \quad \text{for } {S}\gg \max\left({d_{\text{head}}},\frac{{M_{\text{SRAM}}}}{{d_{\text{head}}}}\right)
$$

**Systems Perspective 1.4: A100 I/O reduction**

The asymptotic ratio ${M_{\text{SRAM}}}/{d_{\text{head}}}^2$ predicts how greater SRAM capacity can reduce HBM traffic, but hidden constants and kernel details prevent it from serving as an exact transfer count. In an NVIDIA A100 measurement, Dao et al. ([[05 Reference/Volume I - Foundations/V1 Algorithm Foundations#^ref-dao2022|2022]]) report the effect for a forward-and-backward attention workload with sequence length 1,024, head dimension 64, 16 heads, batch size 64, a key-padding mask, and no dropout:

- **Standard attention**: 35.3 GB of HBM reads and writes; 35.1 ms runtime.
- **FlashAttention**: 4.4 GB of HBM reads and writes; 11.7 ms runtime.

The measurements show the systems consequence of the I/O bound: substantially less HBM traffic coincides with lower runtime even though FlashAttention performs additional recomputation. They do not imply that every configuration becomes compute bound; tile size, sequence length, and kernel implementation determine the realized regime.

Tiling changes how many bytes cross the memory boundary for a fixed model. The last derivation applies the same accounting one level up and asks how large the model and its training set should be for a fixed compute budget.

### Compute-Optimal Scaling Laws

^sec-appdx-algorithm-chinchilla-derivation

Spending a fixed FLOP budget ${O}$ on a 175-billion-parameter model trained on 300 billion tokens leaves the model undertrained compared with a 70-billion-parameter model trained on 1.4 trillion tokens at the same compute cost. Minimizing parametric training loss under a fixed ${O} = 6{P}{D}$ constraint via Lagrange multipliers explains why, and it separates the earlier fit of Kaplan et al. ([[05 Reference/Volume I - Foundations/V1 Algorithm Foundations#^ref-kaplan2020scaling|2020]]) from the compute-optimal scaling of Hoffmann et al. ([[05 Reference/Volume I - Foundations/V1 Algorithm Foundations#^ref-hoffmann2022chinchilla|2022]]). **[[01 Books/Volume I - Foundations/03 Optimization/09 Data Selection/V1-09.03 Measuring Data Value#^sec-data-selection-computeoptimal-frontier-24ba|The compute-optimal frontier]]** uses the resulting frontier to test whether a training run is starved of data or of compute.

To match the rest of the book, the derivation writes model parameters as ${P}$, dataset size in tokens as ${D}$, and the training compute budget as ${O}$ total FLOPs, whereas Kaplan et al. ([[05 Reference/Volume I - Foundations/V1 Algorithm Foundations#^ref-kaplan2020scaling|2020]]) and Hoffmann et al. ([[05 Reference/Volume I - Foundations/V1 Algorithm Foundations#^ref-hoffmann2022chinchilla|2022]]) write ${N}$ for parameters and ${C}$ for compute. The fitted constants ${E}$, ${A}$, ${B}$, ${\alpha}$, and ${\beta}$ and the Lagrange multiplier ${\lambda}$ keep the papers’ letters and are local to this section, so ${E}$ is a loss rather than an energy and ${B}$ is a fitted constant rather than batch size.

#### Parametric Loss Surface

^sec-appdx-algorithm-chinchilla-loss-surface

The cross-entropy evaluation loss ${\mathcal{L}}({P}, {D})$ of an autoregressive transformer language model trained with ${P}$ non-embedding parameters on ${D}$ tokens is modeled by the power-law formulation:

$$
{\mathcal{L}}({P}, {D}) = {E}+ \frac{{A}}{{P}^{\alpha}} + \frac{{B}}{{D}^{\beta}}
$$

 where:

- ${E}$: Irreducible loss representing the entropy of natural language data.
- $\frac{{A}}{{P}^{\alpha}}$: Capacity bottleneck loss resulting from finite model parameters ${P}$.
- $\frac{{B}}{{D}^{\beta}}$: Dataset size bottleneck loss resulting from finite training tokens ${D}$.
- ${A}, {B}> 0$: Empirical scaling constants.
- ${\alpha}, {\beta}> 0$: Power-law scaling exponents for model size and dataset size, respectively.

#### Constrained Optimization

^sec-appdx-algorithm-chinchilla-lagrange

The total floating-point operations required to train a transformer with ${P}$ non-embedding parameters for ${D}$ tokens is given by

$$
{O}= 6 {P} {D}\text{ FLOPs},
$$

 where $2 {P} {D}$ accounts for the forward pass and $4 {P} {D}$ accounts for the backward pass.

Given a fixed training compute budget ${O}_0$, we formulate the constrained optimization problem to minimize the reducible loss ${\hat{\mathcal{L}}}({P}, {D}) = \frac{{A}}{{P}^{\alpha}} + \frac{{B}}{{D}^{\beta}}$:

$$
\min_{{P}, {D}} \left( \frac{{A}}{{P}^{\alpha}} + \frac{{B}}{{D}^{\beta}} \right) \quad \text{subject to} \quad {g}({P}, {D}) = 6 {P} {D}- {O}_0 = 0
$$

We construct the Lagrangian function ${\mathcal{L}_{\text{Lagrange}}}({P}, {D}, {\lambda})$:

$$
{\mathcal{L}_{\text{Lagrange}}}({P}, {D}, {\lambda}) = \frac{{A}}{{P}^{\alpha}} + \frac{{B}}{{D}^{\beta}} + {\lambda}(6 {P} {D}- {O}_0)
$$

Taking partial derivatives with respect to ${P}, {D}$, and ${\lambda}$ and setting them to zero yields:

$$
\frac{\partial {\mathcal{L}_{\text{Lagrange}}}}{\partial {P}} = -{\alpha} {A} {P}^{-{\alpha}- 1} + 6 {\lambda} {D}= 0 \implies {\alpha} {A} {P}^{-{\alpha}- 1} = 6 {\lambda} {D}, \tag{1}
$$

$$
\frac{\partial {\mathcal{L}_{\text{Lagrange}}}}{\partial {D}} = -{\beta} {B} {D}^{-{\beta}- 1} + 6 {\lambda} {P}= 0 \implies {\beta} {B} {D}^{-{\beta}- 1} = 6 {\lambda} {P}, \tag{2}
$$

$$
\frac{\partial {\mathcal{L}_{\text{Lagrange}}}}{\partial {\lambda}} = 6 {P} {D}- {O}_0 = 0. \tag{3}
$$

Multiplying Equation (1) by ${P}$ and Equation (2) by ${D}$ gives:

$$
{\alpha} {A} {P}^{-{\alpha}} = 6 {\lambda} {P} {D},
$$

$$
{\beta} {B} {D}^{-{\beta}} = 6 {\lambda} {P} {D}.
$$

Equating these expressions yields the power-law optimality condition:

$$
{\alpha} {A} {P}^{-{\alpha}} = {\beta} {B} {D}^{-{\beta}}.
$$

 This condition states that at the compute-optimal allocation, the marginal loss reduction per fractional increase in parameter count must equal the marginal loss reduction per fractional increase in dataset tokens.

#### Compute-Optimal Exponents

^sec-appdx-algorithm-chinchilla-exponents

From ${\alpha} {A} {P}^{-{\alpha}} = {\beta} {B} {D}^{-{\beta}}$, solving for ${D}$ in terms of ${P}$ yields:

$$
{D}^{\beta}= \left(\frac{{\beta} {B}}{{\alpha} {A}}\right) {P}^{\alpha}\implies {D}= \left(\frac{{\beta} {B}}{{\alpha} {A}}\right)^{1/{\beta}} {P}^{{\alpha}/{\beta}}.
$$

Substituting ${D}$ into the compute constraint ${O}= 6 {P} {D}$ gives:

$$
{O}= 6 {P}\left(\frac{{\beta} {B}}{{\alpha} {A}}\right)^{1/{\beta}} {P}^{{\alpha}/{\beta}} = 6 \left(\frac{{\beta} {B}}{{\alpha} {A}}\right)^{1/{\beta}} {P}^{\frac{{\alpha}+ {\beta}}{{\beta}}}.
$$

Solving explicitly for the compute-optimal parameter count ${P}^*({O})$:

$$
{P}^*({O}) = \left( \frac{{\alpha} {A}}{{\beta} {B}} \right)^{\frac{1}{{\alpha}+ {\beta}}} \left( \frac{{O}}{6} \right)^{\frac{{\beta}}{{\alpha}+ {\beta}}} \propto {O}^{\frac{{\beta}}{{\alpha}+ {\beta}}}.
$$

By symmetry, solving for the compute-optimal token count ${D}^*({O})$ yields:

$$
{D}^*({O}) = \left( \frac{{\beta} {B}}{{\alpha} {A}} \right)^{\frac{1}{{\alpha}+ {\beta}}} \left( \frac{{O}}{6} \right)^{\frac{{\alpha}}{{\alpha}+ {\beta}}} \propto {O}^{\frac{{\alpha}}{{\alpha}+ {\beta}}}.
$$

##### Empirical Exponents and the ${D}/{P}\approx 20$ Rule

^empirical-exponents-and-the-datasetsizeparametersapprox-20-rule

Fitting the parametric loss surface to over 400 experimental runs, Hoffmann et al. ([[05 Reference/Volume I - Foundations/V1 Algorithm Foundations#^ref-hoffmann2022chinchilla|2022]]) estimated ${\alpha}\approx 0.34$ and ${\beta}\approx 0.28$. Substituting these values gives exponents close to the paper’s parametric-model result:

$$
\frac{{\beta}}{{\alpha}+ {\beta}} \approx 0.45, \qquad \frac{{\alpha}}{{\alpha}+ {\beta}} \approx 0.55
$$

Thus the parametric model predicts:

$$
{P}^*({O}) \propto {O}^{0.45}, \qquad {D}^*({O}) \propto {O}^{0.55}
$$

The paper’s two direct empirical approaches report near-balanced exponents of $(0.50, 0.50)$ and $(0.49, 0.51)$, which motivate the common square-root shorthand. Under the parametric fit, however, ${D}^*/{P}^*$ grows slowly with compute rather than remaining strictly constant. Across the regime studied, roughly 20 training tokens per parameter is a useful Chinchilla heuristic, not a universal invariant.

**Systems Perspective 1.5: Kaplan vs. Chinchilla scaling**

The difference between Kaplan et al. ([[05 Reference/Volume I - Foundations/V1 Algorithm Foundations#^ref-kaplan2020scaling|2020]]) and Hoffmann et al. ([[05 Reference/Volume I - Foundations/V1 Algorithm Foundations#^ref-hoffmann2022chinchilla|2022]]) shows how the training schedule used in empirical fits can alter system design conclusions:

- **Kaplan scaling model**: Kaplan et al. ([[05 Reference/Volume I - Foundations/V1 Algorithm Foundations#^ref-kaplan2020scaling|2020]]) fit a different loss form with its own exponents and reported compute-optimal growth of ${P}\propto {O}^{0.73}$ and ${D}\propto {O}^{0.27}$. This split does not follow from substituting exponents into the two-term surface above. Kaplan’s split led the field to scale model sizes aggressively while holding training dataset sizes relatively small (e.g., GPT-3 175B trained on 300B tokens, giving ${D}/{P}=$ 1.71).
- **Methodological divergence**: Kaplan et al. ([[05 Reference/Volume I - Foundations/V1 Algorithm Foundations#^ref-kaplan2020scaling|2020]]) used a fixed token budget and learning-rate schedule across models. Hoffmann et al. ([[05 Reference/Volume I - Foundations/V1 Algorithm Foundations#^ref-hoffmann2022chinchilla|2022]]) matched the schedule to each training horizon and found that the earlier setup understated the value of training smaller models on more data.
- **Chinchilla revision**: Hoffmann et al. ([[05 Reference/Volume I - Foundations/V1 Algorithm Foundations#^ref-hoffmann2022chinchilla|2022]]) found near-balanced parameter and token scaling: its three approaches report exponent pairs of $(0.50, 0.50)$, $(0.49, 0.51)$, and $(0.46, 0.54)$ rather than one exact universal ratio.
- **Practical impact**: Chinchilla (70B parameters trained on 1.4T tokens, ${D}/{P}=$ 20) outperformed GPT-3 (175B parameters trained on 300B tokens) across downstream benchmarks while requiring 2.5× less compute during inference (inference cost scales with parameter count) and 2.5× lower weight memory at the same precision ([[05 Reference/Volume I - Foundations/V1 Algorithm Foundations#^ref-hoffmann2022chinchilla|Hoffmann et al. 2022]]).

Together, the three derivations bound the algorithmic costs that govern training at scale: reverse-mode differentiation keeps gradient compute within a small constant factor of the forward pass, tiled online softmax keeps attention memory traffic from growing quadratically in HBM, and constrained loss minimization balances parameter count against training tokens for a fixed FLOP budget.

## Summary

^summary

An algorithm becomes a systems workload through its shapes, operation graph, data dependencies, and numerical representation. Linear-algebra primitives, memory layouts, broadcasting, and sparse formats determine work, traffic, locality, and usable parallelism. Automatic differentiation and backpropagation add saved activations and backward computation. Computational graphs then expose opportunities for fusion and recomputation, and the log-sum-exp shift keeps the softmax at the loss finite in reduced precision. Among the derivations, the Baur–Strassen result bounds reverse-mode overhead, while FlashAttention shows how tiling and an online recurrence can reduce HBM traffic without changing attention semantics.

The same accounting connects kernels to scaling decisions. Compute-optimal scaling turns a fixed budget into a model-data allocation, but the fitted exponents remain empirical rather than universal. Before selecting an optimization, count the operations, the bytes moved, and the state saved for the backward pass.

Back to top

## Source References

^source-references

Lawson, Charles L., Richard J. Hanson, David R. Kincaid, and Fred T. Krogh. 1979. “Basic Linear Algebra Subprograms for Fortran Usage.” *ACM Transactions on Mathematical Software* 5 (3): 308–23. https://doi.org/10.1145/355841.355847.

^ref-lawson1979

Dongarra, Jack J., Jeremy Du Croz, Sven Hammarling, and Richard J. Hanson. 1988. “An Extended Set of FORTRAN Basic Linear Algebra Subprograms.” *ACM Transactions on Mathematical Software* 14 (1): 1–17. https://doi.org/10.1145/42288.42291.

^ref-dongarra1988

Werbos, Paul. 1974. “Beyond Regression: New Tools for Prediction and Analysis in the Behavioral Sciences.” PhD thesis, Harvard University.

^ref-werbos1974beyond

Linnainmaa, Seppo. 1970. “The Representation of the Cumulative Rounding Error of an Algorithm as a Taylor Expansion of the Local Rounding Errors.” Master's thesis, University of Helsinki.

^ref-linnainmaa1970representation

Rumelhart, David E., Geoffrey E. Hinton, and Ronald J. Williams. 1986. “Learning Representations by Back-Propagating Errors.” *Nature* 323 (6088): 533–36. https://doi.org/10.1038/323533a0.

^ref-rumelhart1986

Kingma, Diederik P., and Jimmy Ba. 2015. “Adam: A Method for Stochastic Optimization.” *3rd International Conference on Learning Representations (ICLR)*.

^ref-kingma2014adam

Micikevicius, Paulius, Sharan Narang, Jonah Alben, Gregory Diamos, Erich Elsen, David Garcia, Boris Ginsburg, et al. 2018. “Mixed Precision Training.” *International Conference on Learning Representations (ICLR)*.

^ref-micikevicius2017mixed

Korthikanti, Vijay Anand, Jared Casper, Sangkug Lym, Lawrence McAfee, Michael Andersch, Mohammad Shoeybi, and Bryan Catanzaro. 2023. “Reducing Activation Recomputation in Large Transformer Models.” *Proceedings of Machine Learning and Systems (MLSys)* 5: 341–53.

^ref-korthikanti2023activation

Chen, Tianqi, Bing Xu, Chiyuan Zhang, and Carlos Guestrin. 2016. “Training Deep Nets with Sublinear Memory Cost.” *arXiv Preprint arXiv:1604.06174*.

^ref-chen2016training

Baur, Walter, and Volker Strassen. 1983. “The Complexity of Partial Derivatives.” *Theoretical Computer Science* 22 (3): 317–30. https://doi.org/10.1016/0304-3975(83)90110-x.

^ref-baur1983complexity

Dao, T., D. Y. Fu, S. Ermon, A. Rudra, and C. Ré. 2022. “FlashAttention: Fast and Memory-Efficient Exact Attention with IO-Awareness.” *Advances in Neural Information Processing Systems (NeurIPS)* 35: 16344–59. https://doi.org/10.52202/068431-1189.

^ref-dao2022

Hoffmann, Jordan, Sebastian Borgeaud, Arthur Mensch, Elena Buchatskaya, Trevor Cai, Eliza Rutherford, Diego de Las Casas, et al. 2022. “Training Compute-Optimal Large Language Models.” *Advances in Neural Information Processing Systems (NeurIPS)* 35: 30016–30. https://doi.org/10.52202/068431-2176.

^ref-hoffmann2022chinchilla

Kaplan, Jared, Sam McCandlish, Tom Henighan, Tom B. Brown, Benjamin Chess, Rewon Child, Scott Gray, Alec Radford, Jeffrey Wu, and Dario Amodei. 2020. “Scaling Laws for Neural Language Models.” *ArXiv Preprint* abs/2001.08361.

^ref-kaplan2020scaling

## Footnotes

^footnotes

<sup>1</sup> **Einstein summation convention**: Repeated indices in a product are implicitly summed over, eliminating explicit summation signs. ML frameworks adopted the convention because it concisely expresses arbitrary tensor contractions in a single string.

^fn1

<sup>2</sup> **General matrix multiply (GEMM)**: The BLAS (Basic Linear Algebra Subprograms) family began with vector routines standardized in 1979 ([[05 Reference/Volume I - Foundations/V1 Algorithm Foundations#^ref-lawson1979|Lawson et al. 1979]]); GEMM was standardized later as a Level 3 routine ([[05 Reference/Volume I - Foundations/V1 Algorithm Foundations#^ref-dongarra1988|Dongarra et al. 1988]]). The “GE” prefix stands for “general,” as opposed to symmetric or triangular forms. GEMM computes ${\mathbf{C}}= {\alpha}{\mathbf{A}}{\mathbf{B}}+ {\beta}{\mathbf{C}}$ and is a performance-critical routine in deep learning. **[[01 Books/Volume I - Foundations/02 Development/08 Model Training/V1-08.04 Computation and Memory Costs of Training#^sec-model-training-matrix-operations-1f21|Matrix operations]]** explains how GEMM shapes determine training throughput.

^fn2

<sup>3</sup> **Backpropagation**: Short for “backward propagation of errors.” The algorithm was independently discovered multiple times, by Werbos ([[05 Reference/Volume I - Foundations/V1 Algorithm Foundations#^ref-werbos1974beyond|1974]]) and Linnainmaa ([[05 Reference/Volume I - Foundations/V1 Algorithm Foundations#^ref-linnainmaa1970representation|1970]]) for reverse-mode differentiation and by Rumelhart et al. ([[05 Reference/Volume I - Foundations/V1 Algorithm Foundations#^ref-rumelhart1986|1986]]) for neural network training. Its key insight is that computing gradients for all parameters requires one backward pass through the graph rather than one pass per parameter. [[05 Reference/Volume I - Foundations/V1 Algorithm Foundations#^sec-appdx-algorithm-baur-strassen|Section 1.4.1]] derives the constant-factor work bound and a representative dense-layer cost.

^fn3

<sup>4</sup> **Gradient checkpointing**: Trades compute for memory. Instead of storing all activations, only a subset (checkpoints) is kept, and the missing ones are recomputed during the backward pass. This reduces memory usage from storing every layer activation to roughly the square root of the layer count at the cost of ~33 percent more compute ([[05 Reference/Volume I - Foundations/V1 Algorithm Foundations#^ref-chen2016training|Chen et al. 2016]]).

^fn4

<sup>5</sup> **Logit**: Joseph Berkson coined the term in 1944 by analogy with *probit*. The logit function is the inverse of the logistic (sigmoid) function: $\text{logit}({p_{\text{sig}}}) = \log({p_{\text{sig}}}/(1-{p_{\text{sig}}}))$. In deep learning, “logits” refers more loosely to the raw, unnormalized output of the final linear layer before any activation function is applied.

^fn5

<sup>6</sup> **Log-sum-exp**: Implemented as `torch.logsumexp` in PyTorch and `scipy.special.logsumexp` in SciPy. It relies on the identity $\log\left(\sum e^{{z}_{{k}}}\right) = {m} + \log\left(\sum e^{{z}_{{k}} - {m}}\right)$, where ${m} = \max({z}_{{k}})$. Shifted values ${z}_{{k}} - {m}$ are $\le 0$, ensuring exponentials never overflow.

^fn6

## Source

[Repository Source](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/books/vol1/backmatter/appendix_algorithm.qmd) · [Original License](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/LICENSE.md)

[Rendered Reading Snapshot](https://mlsysbook.ai/vol1/backmatter/appendix_algorithm.html#sec-appdx-algorithm-foundations). Rendering provenance is recorded in the import manifest.
