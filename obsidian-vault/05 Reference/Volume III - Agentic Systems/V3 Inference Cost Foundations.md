---
title: V3 Inference Cost Foundations
type: Reference
volume: 3
chapter: 0
publication_status: In Development
source_repository: https://github.com/klappe-pm/cs249r_book
source_commit: de87c0103806d7bfb1c677dbb77a2b92fa00c298
source_path: books/vol3/backmatter/appendix_inference.qmd
source_anchor: sec-vol3-appendix-inference
source_mode: Source-Correlated Published HTML
tags:
- Type/Reference
- Book/Volume_3
rendered_source_url: https://mlsysbook.ai/vol3/backmatter/appendix_inference.html
---

# V3 Inference Cost Foundations

[[Home|Home]] · [[01 Books/Volume III - Agentic Systems/Volume 3 Overview|Volume Overview]]

^sec-vol3-appendix-inference

This appendix supplies the serving arithmetic behind model-call latency, attention-state storage, and resource occupancy. It provides reusable estimates for comparing prompt processing with generation, sizing retained state, and separating average demand from capacity guarantees. Each estimate states its assumptions so that a reader can substitute another model, serving configuration, or workload without treating the reference values as universal performance claims.

## How to Use This Appendix

^how-to-use-this-appendix

Start from the agent-level question in [[05 Reference/Volume III - Agentic Systems/V3 Inference Cost Foundations#^tbl-appdx-inference-lookup|table 1]] and jump to the section that derives its answer. Each entry states the simplifying assumptions behind its floor or pool estimate so that a reader can calibrate it against measured serving telemetry.

| If you need to know…                                                                 | Jump to…                                                                                                            | What you get                                                                                |
|:-------------------------------------------------------------------------------------|:--------------------------------------------------------------------------------------------------------------------|:--------------------------------------------------------------------------------------------|
| When output generation and prompt processing have different per-token costs          | [[05 Reference/Volume III - Agentic Systems/V3 Inference Cost Foundations#^sec-vol3-appendix-inference-roofline\|section 1.1]]    | Conditional compute and bandwidth floors, not measured service latency                      |
| When attention work matters in long-context prefill                                  | [[05 Reference/Volume III - Agentic Systems/V3 Inference Cost Foundations#^sec-vol3-appendix-inference-roofline\|section 1.1]]    | The attention term and the length at which it matches the weight term                       |
| How batching changes amortized serving time and per-stream latency                   | [[05 Reference/Volume III - Agentic Systems/V3 Inference Cost Foundations#^sec-vol3-appendix-inference-roofline\|section 1.1]]    | Weight reuse across streams and the limits of a weight-only estimate                        |
| How sampling placement, grammar masks, and speculative verification add work         | [[05 Reference/Volume III - Agentic Systems/V3 Inference Cost Foundations#^sec-vol3-appendix-inference-decode-loop\|section 1.2]] | Transfer and storage formulas, plus the conditions for exact speculative sampling           |
| How much memory a trajectory’s context occupies, and how attention design changes it | [[05 Reference/Volume III - Agentic Systems/V3 Inference Cost Foundations#^sec-vol3-appendix-inference-kv-cache\|section 1.3]]    | Bytes per token from model geometry, multi-head versus grouped versus multi-query attention |
| How tool waits change live state and how load changes waiting                        | [[05 Reference/Volume III - Agentic Systems/V3 Inference Cost Foundations#^sec-vol3-appendix-inference-queueing\|section 1.4]]    | Little’s law with matched boundaries and a scoped single-server waiting approximation       |
| Which model, accelerator, and node values the book assumes                           | [[05 Reference/Volume III - Agentic Systems/V3 Inference Cost Foundations#^sec-vol3-appendix-inference-assumptions\|section 1.5]] | The reference inputs, ready to substitute                                                   |

Table 1: **Question-to-Derivation Lookup**: Agent-level questions and the sections that derive their answers.

^tbl-appdx-inference-lookup

## Cost Asymmetry Between Input Prefill and Output Generation

^sec-vol3-appendix-inference-roofline

Prompt processing can reuse a model’s weights across many token positions, whereas unbatched generation uses those weights for one new position at a time. That difference can make prefill arithmetic-bound and decode bandwidth-bound. Neither regime follows from the phase name alone. Prompt length, batching, attention traffic, and the serving implementation determine which resource limits an actual call. A weight-only estimate isolates the reuse effect before adding those complications.

A model call processes the uncached prompt during prefill and generates new tokens during decode. Both phases use the same weights, but the reference calculation yields a ratio of about 295 between the unbatched weight-transfer floor per output token and the arithmetic floor per prompt token. We compare these conditional floors to explain the bandwidth constraint (principle [[01 Books/Volume III - Agentic Systems/01 The Model/V3 Model Principles#^pri-vol3-memory-bandwidth-decoding|2]]), not to predict the ratio of measured call latencies or token prices.

### The Roofline

^the-roofline

Adding more floating-point units to an accelerator does not speed up single-stream token generation when the chip spends most of each step waiting for weight bytes to arrive from high-bandwidth memory. An accelerator has two limits, the rate ${R_{\text{peak}}}$ at which it performs arithmetic (operations per second) and the rate ${\text{BW}}$ at which its memory delivers data (bytes per second). A computation’s **arithmetic intensity** ${I}$ is the number of operations it performs per byte it moves. The roofline model ([[05 Reference/Volume III - Agentic Systems/V3 Inference Cost Foundations#^ref-williams2009|Williams et al. 2009]]) gives a performance ceiling ${R_{\text{attain}}}$ from whichever limit binds first:

$$
{R_{\text{attain}}} = \min\left( {R_{\text{peak}}}, \; {I} \cdot {\text{BW}} \right)
$$

The two ceilings meet at the ridge point ${I_{\text{ridge}}} = {R_{\text{peak}}} / {\text{BW}}$. Below the ridge, bandwidth supplies the lower ceiling; above it, arithmetic supplies the lower ceiling. Actual performance can fall below either ceiling because of implementation and scheduling overhead. For the reference accelerator at 8-bit precision, ${R_{\text{peak}}}$ = 1,979 trillion operations per second and ${\text{BW}}$ = 3.35 TB/s, so ${I_{\text{ridge}}} \approx$ 591 operations per byte.

### Prefill and Decode

^prefill-and-decode

A dense transformer with ${P}$ active parameters performs about $2{P}$ weight-related operations per token, one multiply and one add per weight. Its weight payload is ${P}\,{s_{\text{elem,W}}}$ bytes, where ${s_{\text{elem,W}}}$ is bytes per parameter. The approximation counts this payload once per pass; prefill and decode differ in how many tokens share that read. Sparse activation and weight reuse from another cache level require a different traffic count.

In the weight-only model, prefill shares each weight read across ${S}$ prompt positions, giving intensity $2{P} {S} / ({P}\,{s_{\text{elem,W}}}) = 2{S}/{s_{\text{elem,W}}}$. When that intensity exceeds the ridge and arithmetic approaches the stated peak, the per-token time approaches the following floor. Small prompts, kernel tiling, attention, and additional memory traffic can invalidate those assumptions.

$$
{t_{\text{prefill}}} \approx \frac{2{P}}{{R_{\text{peak}}}} \tag{1}
$$

^eq-appdx-prefill-time

Ordinary decode for one stream generates one token per pass, with each token depending on the preceding prefix. If the weights must be read from the modeled memory on every pass, the weight-only intensity is $2/{s_{\text{elem,W}}}$, or 2 operations per byte at 8-bit precision, about 0.34 percent of the ridge. Streaming those weights imposes a time floor even before attention-state traffic and overhead:

$$
{t_{\text{decode}}} \ge \frac{{P}\,{s_{\text{elem,W}}}}{{\text{BW}}} \tag{2}
$$

^eq-appdx-shuttle-floor

For the reference model, with ${P}$ = 70.6 billion parameters at 8-bit precision, [[05 Reference/Volume III - Agentic Systems/V3 Inference Cost Foundations#^eq-appdx-shuttle-floor|equation 2]] gives a decode floor of 21.1 ms per output token, and [[05 Reference/Volume III - Agentic Systems/V3 Inference Cost Foundations#^eq-appdx-prefill-time|equation 1]] gives about 71 µs per prompt token. In the following comparison only, the time symbols denote these weight-only estimates rather than observed times:

$$
\frac{{t_{\text{decode}}}}{{t_{\text{prefill}}}} = \frac{{P}\,{s_{\text{elem,W}}} / {\text{BW}}}{2{P} / {R_{\text{peak}}}} = \frac{{R_{\text{peak}}} \, {s_{\text{elem,W}}}}{2 {\text{BW}}} = \frac{{s_{\text{elem,W}}}}{2} \, {I_{\text{ridge}}} \tag{3}
$$

^eq-appdx-decode-prefill-ratio

which is 295 for the reference configuration. Model size cancels in this approximation because both estimates count the same dense-model weights. The result assumes weight-dominated unbatched decode, peak-rate prefill, and negligible attention and serving overhead; it is not a measured ratio shared by every model on the accelerator. Within that model, the same number gives the number of tokens per pass at which arithmetic time meets weight-transfer time, a threshold used in the batching and speculative-decoding estimates below.

The estimate separates two quantities an agent engineer can influence. Shorter output reduces generation work, and avoiding repeated processing of an unchanged input prefix reduces prefill work. Which change matters more depends on the request lengths, serving configuration, and measurement boundary; token counts alone do not determine a service bill. **[[01 Books/Volume III - Agentic Systems/01 The Model/02 The Foundation Model/V3-02.09 The Cost of a Model Call#^sec-vol3-foundation-model-cost|The Cost of a Model Call]]** prices a bounded example under explicit assumptions. A localized edit illustrates the output-side choice by omitting unchanged file contents, without implying that every compact serialization improves task success.

### Long Contexts

^long-contexts

Attention adds prefill work that grows with the context itself, which the weight-only floor in [[05 Reference/Volume III - Agentic Systems/V3 Inference Cost Foundations#^eq-appdx-prefill-time|equation 1]] omits. The token at position ${s}$ compares its query with ${s}$ earlier keys and combines ${s}$ earlier values, about $4 {N_L} d {s}$ operations for a model with ${N_L}$ layers and width ${d}$. Summed over a causal prefill of ${S}$ tokens, attention adds about $2 {N_L} d {S}^2$ operations to the $2{P} {S}$ of the weights, so

$$
{T_{\text{prefill}}}({S}) \approx \frac{2{P} {S} + 2 {N_L} d {S}^2}{{R_{\text{peak}}}} \tag{4}
$$

^eq-appdx-prefill-long

The quadratic term equals the linear one at ${S}^* = {P} / ({N_L} {d})$, about 108,000 tokens for the reference model, with ${N_L}$ = 80 and ${d}$ = 8,192. At 32,768 tokens, attention adds about 30 percent to the prefill arithmetic, and beyond ${S}^*$ it dominates. Under this fixed-throughput approximation, prefill time grows faster than linearly with length. Observed time to first token also depends on queueing, reuse, and the serving schedule. The logical selection problem in **[[01 Books/Volume III - Agentic Systems/02 Agent Memory/04 Context Engineering/V3-04.04 Usable Working Context#^sec-vol3-context-engineering-physics|Usable Working Context]]** determines which information the request needs; the estimate here prices the processing work without establishing an optimal context length or task-quality threshold.

### Batching and the Fleet’s Cost per Token

^batching-and-the-fleets-cost-per-token

A server can batch decode steps from several trajectories. If one weight read serves ${B}$ streams, the step produces one token for each stream. Ignoring the attention state each stream also reads, the time of one step is

$$
{t_{\text{step}}}({B}) \approx \max\left( \frac{{P}\,{s_{\text{elem,W}}}}{{\text{BW}}}, \; \frac{2 {P} {B}}{{R_{\text{peak}}}} \right) \tag{5}
$$

^eq-appdx-batched-step

and the step stays at the memory-bound floor until ${B}$ reaches ${R_{\text{peak}}}\,{s_{\text{elem,W}}} / 2{\text{BW}}$, the ratio of [[05 Reference/Volume III - Agentic Systems/V3 Inference Cost Foundations#^eq-appdx-decode-prefill-ratio|equation 3]]. Within this weight-only approximation, adding streams up to that threshold leaves step time unchanged, while step time divided by the number of generated tokens falls as $1/{B}$ toward $2{P}/{R_{\text{peak}}}$. This is amortized serving time, not the latency of one stream or the price charged by a service. Repeated input adds prefill work when the prefix cannot be reused, but the bill also depends on utilization and the service’s accounting rules.

A trajectory cannot batch a future call whose input depends on an observation it has not received. Its current call can nevertheless share a physical serving batch with calls from other trajectories. That batching can change queueing and per-step latency; a dependent client stream is not evidence that the server runs at batch size one. The weight-only estimate also omits attention-state traffic. Each stream reads its own keys and values, approximately ${S} \cdot {m_{\text{token}}}$ bytes for a context of ${S}$ tokens ([[05 Reference/Volume III - Agentic Systems/V3 Inference Cost Foundations#^sec-vol3-appendix-inference-kv-cache|section 1.3]]). Long contexts can therefore bind bandwidth or capacity before the arithmetic threshold in [[05 Reference/Volume III - Agentic Systems/V3 Inference Cost Foundations#^eq-appdx-batched-step|equation 5]] is reached. [[05 Reference/Volume III - Agentic Systems/V3 Inference Cost Foundations#^sec-vol3-appendix-inference-queueing|Section 1.4]] relates resident state to the number of live trajectories.

### Chunked Prefill

^chunked-prefill

A large admitted prefill can delay decode work sharing its execution resources. Chunked prefill divides that work into bounded token slices that the scheduler can interleave or co-schedule with decodes ([[05 Reference/Volume III - Agentic Systems/V3 Inference Cost Foundations#^ref-agrawal2024sarathi|Agrawal et al. 2024]]). The token budget limits admitted token positions, not elapsed iteration time; realized gaps and prompt-completion time depend on context lengths, batching, resource contention, and implementation overhead. The weight-only estimate in [[05 Reference/Volume III - Agentic Systems/V3 Inference Cost Foundations#^eq-appdx-batched-step|equation 5]] explains one opportunity for amortization, not a latency guarantee. **[[01 Books/Volume III - Agentic Systems/02 Agent Memory/05 KV Cache Management/V3-05.07 Chunked Prefill Scheduling#^sec-vol3-kvcache-chunked-prefill|Chunked Prefill Scheduling]]** develops the policy trade-off.

## Decode-Loop Mechanics

^sec-vol3-appendix-inference-decode-loop

Token selection, optional grammar constraints, and speculative verification add work beyond the model’s forward pass. Their placement determines which data crosses a device boundary and which dependencies remain on the generation path. The formulas below separate payload sizes from synchronization and computation costs; a small payload alone does not establish a low latency.

### Where Token Sampling Runs

^where-token-sampling-runs

Copying a 128,000-entry floating-point logit vector across a host bus on every decode step of a multi-stream batch moves tens of megabytes per second before a single token is chosen. At each step the model produces one logit per vocabulary entry. Let $|{\mathcal{V}}|$ be the vocabulary size and ${s_{\text{logit}}}$ the bytes stored per logit. One vector occupies $|{\mathcal{V}}|{s_{\text{logit}}}$ bytes. If ${B}$ streams each emit ${R}$ tokens per second and transfer one full vector per token to a host sampler, the logit payload rate is ${B} {R}|{\mathcal{V}}|{s_{\text{logit}}}$ bytes per second. Batching transfers can reduce the number of transfer operations, but not that payload under these assumptions.

Sampling on the accelerator permits an interface that transfers only the selected token identifier. If each identifier occupies ${s_{\text{id}}}$ bytes, its payload rate is ${B} {R} {s_{\text{id}}}$, giving a payload ratio of $|{\mathcal{V}}|{s_{\text{logit}}}/{s_{\text{id}}}$. Neither expression counts protocol framing, requested log probabilities, or synchronization. Those costs must be measured on the actual path before choosing a placement. The calculation concerns an internal serving interface, not the application response format. A service may decode and buffer tokens into response chunks whose boundaries need not match tokens; **[[01 Books/Volume III - Agentic Systems/01 The Model/02 The Foundation Model/V3-02.06 The Invocation Contract#^sec-vol3-foundation-model-contract|The Invocation Contract]]** specifies how the runtime handles that response.

### Grammar Masks

^grammar-masks

A grammar-constrained decoder needs the legal tokens for its current parser state at every step (**[[01 Books/Volume III - Agentic Systems/01 The Model/02 The Foundation Model/V3-02.08 Grammar-Guided Decoding#^sec-vol3-foundation-model-grammar-constrained|Grammar-Guided Decoding]]**). With one bit per vocabulary entry, a dense mask occupies $\lceil |{\mathcal{V}}|/8 \rceil$ bytes. If the constraint has a finite-state representation with state set ${Q}$, a byte-aligned dense table needs $|{Q}|\lceil |{\mathcal{V}}|/8 \rceil$ bytes, excluding transitions and metadata. This formula lets us compare a proposed vocabulary and state count with the memory budget without assuming that every grammar has a small finite-state representation.

Whether the table fits and remains resident in on-chip cache depends on the accelerator and competing working sets. Precomputation permits lookup and filtering during sampling, but table size alone establishes neither the lookup latency nor a required device placement.

A host-mediated implementation may instead transfer the selected token to a host process, advance its grammar state, and return the next mask before sampling continues. The cost depends on the implementation and on how much work overlaps model evaluation. Recursive grammars require additional parser state, while compressed structures and precomputation can reduce masking work. The legal-token mask must be available when selection uses it. **[[05 Reference/Volume III - Agentic Systems/V3 Typed Tool Interfaces#^sec-vol3-app-b-logit-masking|When Constrained Decoding Pays for Itself]]** considers when constraining is worth its cost. **[[05 Reference/Volume III - Agentic Systems/V3 Mathematical Foundations#^sec-vol3-appendix-math-dfa|Finite-state constrained decoding]]** gives the masking argument, whose complete-output guarantee requires reaching an accepting state under the specified grammar and decoder assumptions. An interrupted legal prefix need not parse as a complete object.

### Speculative Decoding

^speculative-decoding

Because single-stream decoding reads every target-model weight to emit one token, a smaller draft model can propose ${k}$ candidate tokens in serial so the target model verifies all ${k}$ in a single weight read. Exact speculative sampling preserves the specified target distribution while checking those draft positions in one target-model pass ([[05 Reference/Volume III - Agentic Systems/V3 Inference Cost Foundations#^ref-leviathan2023fast|Leviathan et al. 2023]]; [[05 Reference/Volume III - Agentic Systems/V3 Inference Cost Foundations#^ref-chen2023accelerating|Chen et al. 2023]]). A draft distribution ${q}$ proposes ${k}$ tokens ${\tilde{x}}_1, \dots, {\tilde{x}}_k$ autoregressively. The target computes the distributions needed to verify them and to sample after the full draft. Both ${p}$ and ${q}$ below are normalized distributions at the same prefix after their sampling transformations, including any grammar masks. Scanning left to right, candidate ${\tilde{x}}_j$ is accepted with probability

$$
{\alpha_{\text{spec}, j}} = \min\left(1, \frac{{p}({\tilde{x}}_j \mid \cdot)}{{q}({\tilde{x}}_j \mid \cdot)}\right) \tag{6}
$$

^eq-appdx-spec-accept

At the first rejection, the remaining drafts are discarded and one replacement token is drawn from the normalized residual distribution

$$
{p_{\text{res}}}({v}) = \frac{\max\left(0,\; {p}({v}) - {q}({v})\right)}{\sum_{{w} \in {\mathcal{V}}} \max\left(0,\; {p}({w}) - {q}({w})\right)} \tag{7}
$$

^eq-appdx-spec-residual

If every draft is accepted, the sampler draws one bonus token from the target distribution after the full draft. Otherwise, [[05 Reference/Volume III - Agentic Systems/V3 Inference Cost Foundations#^eq-appdx-spec-residual|equation 7]] applies at the first rejected position; its denominator is positive when rejection has positive probability. Together with [[05 Reference/Volume III - Agentic Systems/V3 Inference Cost Foundations#^eq-appdx-spec-accept|equation 6]], this rule preserves the target sequence distribution under exact sampling and consistent prefix state. It does not promise the same sample for the same random seed. Termination or an output limit may shorten an iteration that otherwise emits between one and ${k}+1$ tokens.

Weight reuse in [[05 Reference/Volume III - Agentic Systems/V3 Inference Cost Foundations#^eq-appdx-batched-step|equation 5]] explains why verification can cost less than separate target passes. Actual benefit depends on draft cost, acceptance, attention traffic, batch composition, and verification overhead. Those terms can erase the saving; the weight-only threshold is not a speedup guarantee. **[[01 Books/Volume III - Agentic Systems/06 Agents at Scale/19 Agent Economics/V3-19.05 Critical-Path Latency#^sec-vol3-agent-economics-speculative|When speculative decoding pays off]]** compares the resulting work and latency at the trajectory boundary.

## The Size of the Attention State

^sec-vol3-appendix-inference-kv-cache

For the full-attention decoder considered here, generation uses keys and values associated with earlier token positions. The serving system caches those derived vectors rather than recomputing them at each step. **[[01 Books/Volume III - Agentic Systems/01 The Model/02 The Foundation Model/V3-02.05 Autoregressive Generation#^sec-vol3-foundation-model-autoregressive|Autoregressive Generation]]** introduces this reuse within a call; the storage estimate here follows from the model’s geometry and retained sequence length.

### Bytes per Token

^bytes-per-token

Every token appended to an agent’s working context adds a fixed slice of key and value vectors to accelerator memory across every transformer layer. For a decoder with ${N_L}$ layers, ${H_{\text{KV}}}$ key-value heads per layer, head dimension ${d_{\text{head}}}$, and ${s_{\text{elem,KV}}}$ bytes per stored element, each token stores one key vector and one value vector per layer and key-value head:

$$
{m_{\text{token}}} = 2 \cdot {N_L} \cdot {H_{\text{KV}}} \cdot {d_{\text{head}}} \cdot {s_{\text{elem,KV}}} \tag{8}
$$

^eq-appdx-kv-cache-token-size

and a context of ${S}$ tokens occupies

$$
{M_{\text{KV}}} = {S} \cdot {m_{\text{token}}}
$$

For the reference model, with ${N_L}$ = 80, ${H_{\text{KV}}}$ = 8, ${d_{\text{head}}}$ = 128, and 16-bit storage, ${m_{\text{token}}}$ = 327,680 bytes, so a 32,768-token context occupies about 10.7 GB. **[[01 Books/Volume III - Agentic Systems/02 Agent Memory/05 KV Cache Management/V3-05.03 The Footprint of Retained Attention State#^sec-vol3-kvcache-geometry|The Footprint of Retained Attention State]]** turns this into the number of trajectories one node can hold.

### Attention Designs

^attention-designs

The number of key-value heads is a design choice that changes ${m_{\text{token}}}$ directly. Multi-head attention gives every query head its own keys and values. Multi-query attention shares one key-value head across all query heads ([[05 Reference/Volume III - Agentic Systems/V3 Inference Cost Foundations#^ref-shazeer2019fast|Shazeer 2019]]). Grouped-query attention sits between them by sharing each key-value head across a group of query heads ([[05 Reference/Volume III - Agentic Systems/V3 Inference Cost Foundations#^ref-ainslie2023gqa|Ainslie et al. 2023]]). Holding the reference model’s layer count and head dimension fixed shows how sharing key-value heads scales both the per-token payload and a long trajectory’s footprint ([[05 Reference/Volume III - Agentic Systems/V3 Inference Cost Foundations#^tbl-appdx-kv-cache-scaling|table 2]]).

| Design                      |     Key-value heads     | Bytes per token (16-bit) | At 32,768 tokens |
|:----------------------------|:-----------------------:|:------------------------:|:----------------:|
| **Multi-head attention**    | 64 (one per query head) |        2,621,440         |     85.9 GB      |
| **Grouped-query attention** |            8            |         327,680          |     10.7 GB      |
| **Multi-query attention**   |            1            |          40,960          |     1.34 GB      |

Table 2: **Attention State by Attention Design**: Bytes of keys and values per token, and for one long agent context, for the reference model’s layers and head dimension under three attention designs. Storing keys and values at 8 bits halves every entry.

^tbl-appdx-kv-cache-scaling

Storing each key and value element at 8 rather than 16 bits halves the element payload, to 163,840 bytes per token for the grouped design, before scale, metadata, or layout overhead. Lower precision and selective removal of entries require task-quality and implementation validation. The remaining cache alone does not recover a discarded entry, although retained inputs and compatible configuration may permit recomputation. These storage approximations are distinct from changing the model architecture (**[[01 Books/Volume III - Agentic Systems/02 Agent Memory/05 KV Cache Management/V3-05.03 The Footprint of Retained Attention State#^sec-vol3-kvcache-geometry|The Footprint of Retained Attention State]]**).

### Occupancy During a Tool Wait

^occupancy-during-a-tool-wait

Memory occupancy depends on how much is held and for how long. A trajectory whose attention state stays resident through a tool wait of length ${T_{\text{wait}}}$ occupies

$$
{O_{\text{mem}}} = {M_{\text{KV}}} \cdot {T_{\text{wait}}}
$$

byte-seconds while generating nothing. When a tool wait exceeds the active generation interval and holds the same footprint, idle occupancy exceeds active occupancy. The relevant inputs are the actual retained bytes and their holding interval. The retain, evict, recompute, or offload decision of **[[01 Books/Volume III - Agentic Systems/02 Agent Memory/05 KV Cache Management/V3-05.08 Paused-State Policies#^sec-vol3-kvcache-swapping|Paused-State Policies]]** is therefore a per-wait decision rather than a fixed property of agents.

### Paged Storage

^paged-storage

Reserving a contiguous region for each trajectory’s maximum context leaves unused capacity when its retained length is below that cap. Paged storage divides a pool into interchangeable fixed blocks of ${S_{\text{blk}}}$ tokens and maps each trajectory’s positions to blocks through a table ([[05 Reference/Volume III - Agentic Systems/V3 Inference Cost Foundations#^ref-kwon2023|Kwon et al. 2023]]). Allocation on demand removes variable-extent external fragmentation within that pool; it does not eliminate metadata, temporary allocations, or unused final-block slots. If sequence lengths have uniformly distributed remainders modulo ${S_{\text{blk}}}$, the mean unused tail payload is

$$
\mathbb{E}[\text{waste}] \approx \frac{{S_{\text{blk}}} - 1}{2} \cdot {m_{\text{token}}}
$$

per sequence. Without that distributional assumption, the unconditional bound is at most ${S_{\text{blk}}} - 1$ unused token slots in a final block. Compatible blocks can also be shared, allowing branches and requests with a common prefix to use one physical copy under the serving system’s ownership rules (**[[01 Books/Volume III - Agentic Systems/02 Agent Memory/05 KV Cache Management/V3-05.05 Paged KV Allocation#^sec-vol3-kvcache-pagedattention|Paged KV Allocation]]**).

## Queueing for Trajectories

^sec-vol3-appendix-inference-queueing

An agent can remain live while it consumes no accelerator execution time. A retained cache, sandbox lease, and harness record can each span a different interval of that trajectory. Capacity estimates therefore begin by choosing the resource and its acquisition-to-release boundary. Little’s law relates average occupancy to that boundary; a separate queueing model estimates waiting under stated arrival and service assumptions.

### Continuous Batching

^continuous-batching

A server batches decode steps from many trajectories ([[05 Reference/Volume III - Agentic Systems/V3 Inference Cost Foundations#^eq-appdx-batched-step|equation 5]]). In a fixed-membership batch, finished requests cannot be replaced until the batch drains, although their results need not be withheld. Continuous batching admits and retires requests at iteration boundaries ([[05 Reference/Volume III - Agentic Systems/V3 Inference Cost Foundations#^ref-yu2022orca|Yu et al. 2022]]). A returning trajectory can enter a later iteration when memory, token budgets, and scheduling policy permit; a released slot does not promise admission on the immediately following step.

Batch slots are not independent servers. Their occupants share weight reads, arithmetic, memory bandwidth, and iteration time, so one request can change another’s service rate. Little’s law still applies to a stable measured boundary, but the number of slots cannot be substituted for the number of independent servers in a queueing formula. Predicting delay requires a model or measurements that capture the batching policy and workload mix.

### Little’s Law with Tool Waits

^littles-law-with-tool-waits

Suppose an agent trajectory spends 20 s waiting on a sandbox or database tool for every 4 s of model execution. Then six times as many trajectories sit alive in the system as are actively running on accelerators. For a stable system with well-defined finite long-run averages, the mean number of items inside a boundary equals their entry rate times their mean time inside that same boundary ([[05 Reference/Volume III - Agentic Systems/V3 Inference Cost Foundations#^ref-little1961|Little 1961]]):

$$
{Q_{\text{req}}} = {\lambda_{\text{arr}}} \cdot {T_{\text{lat}}} \tag{9}
$$

^eq-appdx-littles-law

A trajectory of ${H}$ turns spends each turn in a model call and then in a tool, so its trajectory duration is

$$
{T_{\text{traj}}} = \sum_{t=0}^{{H}-1} \left( {T_{\text{model}}}^{(t)} + {T_{\text{tool}}}^{(t)} \right)
$$

under the simplifying assumption that model calls and tool operations run sequentially, with no additional approval, queueing, or runtime delay. As a worked case, let trajectories start at 2 per second, each running 15 turns of 4 s of model time and 20 s of tool time. Each lives 360 s, about 6 minutes, so [[05 Reference/Volume III - Agentic Systems/V3 Inference Cost Foundations#^eq-appdx-littles-law|equation 9]], in its trajectory form ${N_{\text{traj}}} = {\lambda_{\text{traj}}}\,\mathbb{E}[{T_{\text{traj}}}]$, gives 720 live trajectories. Only 17 percent of each trajectory’s time is spent in a model call, so on average 120 of them are calling the model at any moment.

The gap between those two numbers measures the effect of holding state through tool waits in this workload. If every live trajectory keeps a 32,768-token context resident, the attention state totals about 7.7 TB, about 15 nodes’ worth of the reference pool of [[05 Reference/Volume III - Agentic Systems/V3 Inference Cost Foundations#^sec-vol3-appendix-inference-assumptions|section 1.5]]. Holding the same footprint only during the stipulated model-call intervals gives about 2.4 nodes’ worth. This worked case assumes an unchanged context footprint and no extra waiting, so its averages compare two retention policies rather than determining peak provisioning or proving that the serving system can sustain the offered rate. Reloading or recomputing on resumption adds time and work omitted from this comparison, and recomputing those intervals may change the averages; **[[01 Books/Volume III - Agentic Systems/02 Agent Memory/05 KV Cache Management/V3-05.08 Paused-State Policies#^sec-vol3-kvcache-swapping|Paused-State Policies]]** develops that policy choice.

Harness records and sandbox leases require their own acquisition rates and holding times, not the whole trajectory lifetime by default. If footprints vary, average memory occupancy follows the byte-time held by each arrival, rather than an unqualified product of mean footprint and mean lifetime. Headroom and admission additionally require variability, reclamation behavior, and resource-specific limits (**[[01 Books/Volume III - Agentic Systems/06 Agents at Scale/19 Agent Economics/V3-19.07 Capacity for Trajectories#^sec-vol3-agent-economics-capacity|Capacity for Trajectories]]**, **[[01 Books/Volume III - Agentic Systems/03 Tool Use/08 Agent Sandboxes/V3-08.09 Sandbox Pools and Reset#^sec-vol3-sandboxes-pooling|Sandbox Pools and Reset]]**).

### Load Sensitivity of Waiting

^load-sensitivity-of-waiting

A single-server queue isolates how variability and load contribute to waiting. Consider first-come, first-served service with independent, identically distributed interarrival times, independent, identically distributed service times, independence between the two sequences, finite variances, and utilization ${\rho_{\text{serv}}} < 1$. Let $\mathbb{E}[{T_{\text{svc}}}]$ be mean service time and ${c_{a}}^2$ and ${c_{s}}^2$ the squared coefficients of variation of interarrival and service times. Kingman’s heavy-traffic result motivates the following finite-load approximation to mean waiting time; it is not an identity or a tail bound.

$$
{W_{q}} \approx \frac{{c_{a}}^2 + {c_{s}}^2}{2} \cdot \frac{{\rho_{\text{serv}}}}{1 - {\rho_{\text{serv}}}} \cdot \mathbb{E}[{T_{\text{svc}}}]
$$

With interarrival variability ${c_{a}}^2$ = 2 and service variability ${c_{s}}^2$ = 1, the variability factor is 1.5. Substitution gives approximate waits of 1.5, 3.5, and 13.5 service times at 50, 70, and 90 percent utilization. These are selected comparison points, not a universal utilization knee or an operating recommendation.

Batching, correlated fan-out, retries, and state-dependent service rates can violate the model. Infinite service-time variance also invalidates the finite-variance calculation. The derivation and its limits follow the single-server heavy-traffic analysis of Boon et al. ([[05 Reference/Volume III - Agentic Systems/V3 Inference Cost Foundations#^ref-boon2023heavy|2023]]); multiple-server pools need a separately justified model. Measured deadline compliance, workload mix, and admission policy determine usable capacity. **[[05 Reference/Volume III - Agentic Systems/V3 Mathematical Foundations#^sec-vol3-appendix-math-queueing|Heavy-tailed queueing theory]]** distinguishes mean waiting from tail behavior.

### How Many Trajectories Fit in Accelerator Memory

^how-many-trajectories-fit-in-accelerator-memory

Even when a multi-GPU node has enough compute to batch dozens of decode streams, high-bandwidth memory fills up as soon as the resident trajectories’ contexts exceed the KV pool. For a server with memory ${M_{\text{HBM}}}$, weights of ${P}\,{s_{\text{elem,W}}}$ bytes (16-bit here, whereas the time floors assume 8-bit weights), and a runtime reserve ${M_{\text{runtime}}}$, the memory left for attention state is

$$
{M_{\text{pool}}} = {M_{\text{HBM}}} - {P}\,{s_{\text{elem,W}}} - {M_{\text{runtime}}} \tag{10}
$$

^eq-appdx-mdynamic

and a mean-footprint estimate for contexts of average length ${\bar{S}}$ is

$$
{B_{\max}} = \left\lfloor \frac{{M_{\text{pool}}}}{{\bar{S}} \cdot {m_{\text{token}}}} \right\rfloor \tag{11}
$$

^eq-appdx-max-batch

An average footprint does not guarantee that a particular set of requests fits. For the reference node and equal-length unshared contexts, [[05 Reference/Volume III - Agentic Systems/V3 Inference Cost Foundations#^eq-appdx-mdynamic|equation 10]] leaves 526.0 GB and [[05 Reference/Volume III - Agentic Systems/V3 Inference Cost Foundations#^eq-appdx-max-batch|equation 11]] gives 48 resident contexts at 32,768 tokens, before allocator overhead and additional headroom. This is the payload bound derived in **[[01 Books/Volume III - Agentic Systems/02 Agent Memory/05 KV Cache Management/V3-05.03 The Footprint of Retained Attention State#^sec-vol3-kvcache-geometry|The Footprint of Retained Attention State]]**, not an admission or throughput guarantee. When a new allocation cannot fit, the service may queue or reject work, reclaim dormant state, or move or drop eligible state.

A restricted comparison estimates reconstruction of ${S}$ tokens by the linear weight-work term $2{P} {S}/{R_{\text{peak}}}$ and reload by ${S} \cdot {m_{\text{token}}} / {\text{BW}_{\text{link}}}$. Both estimates assume the stated sustained compute and transfer rates. The comparison omits the attention term of [[05 Reference/Volume III - Agentic Systems/V3 Inference Cost Foundations#^eq-appdx-prefill-long|equation 4]], queueing, allocation, and other overhead. Within that model alone, reconstruction has the smaller estimated duration when

$$
\frac{2 {P}}{{R_{\text{peak}}}} < \frac{{m_{\text{token}}}}{{\text{BW}_{\text{link}}}}
$$

The cancellation of context length follows from those two linear estimates, not from a general property of serving latency. The pause policy in **[[01 Books/Volume III - Agentic Systems/02 Agent Memory/05 KV Cache Management/V3-05.08 Paused-State Policies#^sec-vol3-kvcache-swapping|Paused-State Policies]]** additionally considers uniquely reclaimable state, competing demand, resumption likelihood, host and link resources, and the permitted resume delay.

## Reference Values

^sec-vol3-appendix-inference-assumptions

The worked estimates use the MLSysIM entries `Models.Language.Llama3_70B`, `Hardware.Cloud.H100`, and `Systems.Nodes.DGX_H100`. These identify a reference configuration, not a current-product recommendation. Auditing or substituting those estimates requires separating the registry-backed model and hardware inputs from the local precision and reserve assumptions ([[05 Reference/Volume III - Agentic Systems/V3 Inference Cost Foundations#^tbl-appdx-hardware-constants|table 3]]). The ratio of [[05 Reference/Volume III - Agentic Systems/V3 Inference Cost Foundations#^eq-appdx-decode-prefill-ratio|equation 3]] isolates weight reuse; [[05 Reference/Volume III - Agentic Systems/V3 Inference Cost Foundations#^eq-appdx-kv-cache-token-size|equation 8]] sizes the attention payload.

The two calculations use different placement boundaries. Per-token floors use one accelerator’s compute rate and bandwidth with 8-bit weights. The memory pool, by contrast, aggregates 8 accelerators, totaling 687.2 GB, and subtracts one 16-bit model copy and a node-wide reserve. Because that pool estimate assumes a feasible sharding arrangement without counting communication time or per-device imbalance, multiplying memory capacity does not establish an equivalent latency speedup. Memory quantities below use decimal GB consistently with the pool arithmetic, rather than the accelerator’s branded capacity label.

| Quantity                                       | Symbol                                   | Reference value                          | Used in                                 |
|:-----------------------------------------------|:-----------------------------------------|:-----------------------------------------|:----------------------------------------|
| **Parameters**                                 | ${P}$                                    | 70.6 billion                             | Per-token floors, weights in memory     |
| **Layers**                                     | ${N_L}$                                  | 80                                       | Attention state, long-context prefill   |
| **Model width**                                | ${d}$                                    | 8,192                                    | Long-context prefill                    |
| **Query heads / key-value heads**              | ${N_{\text{heads}}}$ / ${H_{\text{KV}}}$ | 64 / 8                                   | Attention state by design               |
| **Head dimension**                             | ${d_{\text{head}}}$                      | 128                                      | Attention state                         |
| **Weight precision for time floors**           | ${s_{\text{elem,W}}}$                    | 1 byte (8-bit)                           | Decode floor, ridge-to-ratio conversion |
| **Key-value precision**                        | ${s_{\text{elem,KV}}}$                   | 2 bytes (16-bit)                         | Attention state                         |
| **Accelerator memory bandwidth**               | ${\text{BW}}$                            | 3.35 TB/s                                | Decode floor, ridge point               |
| **Accelerator peak rate, 8-bit**               | ${R_{\text{peak}}}$                      | 1,979 trillion operations per second     | Prefill floor, ridge point              |
| **Memory per accelerator**                     | None                                     | 85.9 GB                                  | Component of node memory pool           |
| **Accelerators per node**                      | ${n_{\text{acc}}}$                       | 8                                        | Node memory pool                        |
| **Ridge point**                                | ${I_{\text{ridge}}}$                     | 591 operations per byte                  | Where passes turn arithmetic-bound      |
| **Decode floor per output token**              | ${t_{\text{decode}}}$                    | 21.1 ms                                  | Call latency                            |
| **Weight-only prefill floor per prompt token** | ${t_{\text{prefill}}}$                   | 71 µs                                    | Conditional arithmetic estimate         |
| **Attention state per token**                  | ${m_{\text{token}}}$                     | 327,680 bytes                            | Memory per trajectory                   |
| **Attention-state pool per node**              | ${M_{\text{pool}}}$                      | 526.0 GB (16-bit weights, 20 GB reserve) | Trajectories per node                   |

Table 3: **Reference Serving Values**: Registry-backed model and hardware inputs, local precision and reserve assumptions, and derived quantities. The time floors use one accelerator; the attention-state pool uses aggregate node memory.

^tbl-appdx-hardware-constants

Back to top

## Source References

^source-references

Williams, Samuel, Andrew Waterman, and David Patterson. 2009. “Roofline: An Insightful Visual Performance Model for Multicore Architectures.” *Communications of the ACM* 52 (4): 65–76. https://doi.org/10.1145/1498765.1498785.

^ref-williams2009

Agrawal, Amey, Nitin Kedia, Ashish Panwar, Jayashree Mohan, Nipun Kwatra, Bhargav S. Gulavani, Alexey Tumanov, and Ramachandran Ramjee. 2024. “Taming Throughput-Latency Tradeoff in LLM Inference with Sarathi-Serve.” *18th USENIX Symposium on Operating Systems Design and Implementation (OSDI 24)*, 117–34.

^ref-agrawal2024sarathi

Leviathan, Yaniv, Matan Kalman, and Yossi Matias. 2023. “Fast Inference from Transformers via Speculative Decoding.” *Proceedings of the 40th International Conference on Machine Learning* 202: 19274–86.

^ref-leviathan2023fast

Chen, C., S. Borgeaud, G. Irving, J.-B. Lespiau, L. Sifre, and J. Jumper. 2023. “Accelerating Large Language Model Decoding with Speculative Sampling.” *arXiv Preprint arXiv:2302.01318*.

^ref-chen2023accelerating

Shazeer, Noam. 2019. “Fast Transformer Decoding: One Write-Head Is All You Need.” *arXiv Preprint arXiv:1911.02150*.

^ref-shazeer2019fast

Ainslie, Joshua, James Lee-Thorp, Michiel de Jong, Yury Zemlyanskiy, Federico Lebr’on, and Sumit Sanghai. 2023. “GQA: Training Generalized Multi-Query Transformer Models from Multi-Head Checkpoints.” *Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing (EMNLP)*.

^ref-ainslie2023gqa

Kwon, Woosuk, Zhuohan Li, Siyuan Zhuang, Ying Sheng, Lianmin Zheng, Cody Hao Yu, Joseph Gonzalez, Hao Zhang, and Ion Stoica. 2023. “Efficient Memory Management for Large Language Model Serving with PagedAttention.” *Proceedings of the 29th Symposium on Operating Systems Principles*, 611–26. https://doi.org/10.1145/3600006.3613165.

^ref-kwon2023

Yu, Gyeong-In, Joo Seong Jeong, Geon-Woo Kim, Soojeong Kim, and Byung-Gon Chun. 2022. “Orca: A Distributed Serving System for Transformer-Based Generative Models.” *16th USENIX Symposium on Operating Systems Design and Implementation (OSDI 22)*, 521–38.

^ref-yu2022orca

Little, John D. C. 1961. “A Proof for the Queuing Formula: $L = \lambda W$.” *Operations Research* 9 (3): 383–87. https://doi.org/10.1287/opre.9.3.383.

^ref-little1961

Boon, Marko A. A., Augustus J. E. M. Janssen, and Johan S. H. van Leeuwaarden. 2023. “Heavy-Traffic Single-Server Queues and the Transform Method.” *Indagationes Mathematicae* 34 (5): 1014–37. https://doi.org/10.1016/j.indag.2023.02.004.

^ref-boon2023heavy

## Source

[Repository Source](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/books/vol3/backmatter/appendix_inference.qmd) · [Original License](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/LICENSE.md)

[Rendered Reading Snapshot](https://mlsysbook.ai/vol3/backmatter/appendix_inference.html#sec-vol3-appendix-inference). Rendering provenance is recorded in the import manifest.
