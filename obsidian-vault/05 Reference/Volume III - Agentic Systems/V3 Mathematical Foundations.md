---
title: V3 Mathematical Foundations
type: Reference
volume: 3
chapter: 0
publication_status: In Development
source_repository: https://github.com/klappe-pm/cs249r_book
source_commit: de87c0103806d7bfb1c677dbb77a2b92fa00c298
source_path: books/vol3/backmatter/appendix_math.qmd
source_anchor: sec-vol3-appendix-math
source_mode: Source-Correlated Published HTML
tags:
- Type/Reference
- Book/Volume_3
rendered_source_url: https://mlsysbook.ai/vol3/backmatter/appendix_math.html
---

# V3 Mathematical Foundations

[[Home|Home]] · [[01 Books/Volume III - Agentic Systems/Volume 3 Overview|Volume Overview]]

^sec-vol3-appendix-math

This appendix supplies mathematical background for reasoning about agent trajectories, resource use, evaluation, and learning. It collects reusable models and derivations whose details would interrupt the chapters’ engineering arguments. Each entry identifies its assumptions and the decisions it can support, so a reader can check a result or adapt a calculation without treating an idealized model as a guarantee about a deployed agent.

## How to Use This Appendix

^how-to-use-this-appendix

Choose the reference problem rather than reading the entries in sequence. Each group isolates one family of formal models and points back to the chapter where the engineering decision is made:

- When context, observations, and progress signals are being confused with state or guarantees, [[05 Reference/Volume III - Agentic Systems/V3 Mathematical Foundations#^sec-vol3-appendix-math-trajectory-models|section 1.1]] separates their formal roles.
- When an output constraint or representation approximation needs a precise scope, [[05 Reference/Volume III - Agentic Systems/V3 Mathematical Foundations#^sec-vol3-appendix-math-representation-methods|section 1.2]] supplies the language, matrix, and geometric models.
- When long jobs or repeated work dominate cost, [[05 Reference/Volume III - Agentic Systems/V3 Mathematical Foundations#^sec-vol3-appendix-math-resource-models|section 1.3]] derives queueing and cadence relationships.
- When an evaluation or release claim needs statistical support, [[05 Reference/Volume III - Agentic Systems/V3 Mathematical Foundations#^sec-vol3-appendix-math-statistical-decisions|section 1.4]] identifies the experiment, estimator, and decision assumptions.
- When a trajectory-training result needs to be checked, [[05 Reference/Volume III - Agentic Systems/V3 Mathematical Foundations#^sec-vol3-appendix-math-learning-estimators|section 1.5]] gives the relevant gradients and conditional bounds.
- When adding workers or reviewers changes performance, [[05 Reference/Volume III - Agentic Systems/V3 Mathematical Foundations#^sec-vol3-appendix-math-coordination-models|section 1.6]] separates parallel speedup from correlated assessment error.

Each group is a lookup collection. Follow the entry’s return reference for the engineering decision in the main text; the derivation is optional depth, not a replacement for that decision.

## Trajectory Models

^sec-vol3-appendix-math-trajectory-models

A runtime can limit actions without knowing the complete environment state. These entries distinguish probabilistic state estimation, bounds on admitted steps, and the propagation of security labels.

### POMDP Formalization of Trajectories

^sec-vol3-appendix-math-pomdp

A tool result exposes only part of the environment an agent acts on. A partially observable Markov decision process (POMDP) separates that observation from the underlying state ([[05 Reference/Volume III - Agentic Systems/V3 Mathematical Foundations#^ref-kaelbling1998|Kaelbling et al. 1998]]). One discounted formulation is the tuple

$$
\langle {\mathsf{S}}, {\mathsf{A}}, {\mathsf{T}}, {\mathsf{R}}, {\Omega}, {\mathsf{O}}, {\gamma} \rangle
$$

with an initial-state distribution specified separately. Its components have distinct roles:

- ${\mathsf{S}}$ contains environment states, including relevant remote state and concurrent activity.
- ${\mathsf{A}}$ contains available actions.
- ${\mathsf{T}}$ determines the transition distribution ${p}({s'} \mid {s},{a})$ to the next state.
- ${\mathsf{R}}({s},{a})$ specifies the modeled reward.
- ${\Omega}$ contains possible observations.
- ${\mathsf{O}}({o} \mid {s'},{a})$ gives the observation distribution after an action and transition.
- ${\gamma} \in [0,1)$ discounts future rewards in this formulation.

The state must contain enough information for the assumed transition law to be Markov. A reward is a chosen objective signal, not a certificate of correctness or permission to act. Finite-horizon tasks can instead use an undiscounted objective with a declared terminal convention.

Let ${h}_t=({o}_0,{a}_0,{o}_1,\ldots,{a}_{t-1},{o}_{t})$ denote the interaction history before action ${a}_{t}$. The belief state is a probability distribution over environment states conditional on that history, not the history’s token representation:

$$
{b}_t({s})=\Pr({S}_t={s}\mid {h}_t).
$$

For a finite state space and an observation with positive probability, Bayes’ rule gives

$$
{b}_{t+1}({s'})= \frac{{\mathsf{O}}({o}_{t+1}\mid {s'},{a}_{t}) \sum_{{s}} {p}({s'}\mid {s},{a}_{t}){b}_t({s})} {\sum_{{\tilde{s}}}{\mathsf{O}}({o}_{t+1}\mid {\tilde{s}},{a}_{t}) \sum_{{s}} {p}({\tilde{s}}\mid {s},{a}_{t}){b}_t({s})}.
$$

The numerator predicts the next state and weights it by the received evidence; the denominator normalizes the distribution. A zero denominator signals an observation outside the assumed model’s support, not a valid posterior update.

A language-model agent usually acts from a selected context ${c}_{t}$, which can summarize or omit parts of ${h}_t$. Generated reasoning tokens can influence its policy, but do not become external observations merely by appearing in context. Neither ${c}_{t}$ nor a verbal confidence claim establishes that the agent represents a calibrated ${b}_t$. The formal model therefore clarifies what the implementation approximates; it does not prove that its context is sufficient. Observation freshness checks in **[[01 Books/Volume III - Agentic Systems/02 Agent Memory/04 Context Engineering/V3-04.08 Context Invalidation#^sec-vol3-context-engineering-context-rot|Context Invalidation]]** and plan revision in **[[01 Books/Volume III - Agentic Systems/01 The Model/03 Test-Time Compute/V3-03.06 Revising Candidate Plans#^sec-vol3-test-time-compute-planning-revision|Revising Candidate Plans]]** address the consequences of incomplete or outdated evidence.

### Ranking Functions and Progress Evidence

^sec-vol3-appendix-math-lyapunov

An agent loop that retries a failing test without a monotone counter can run indefinitely while appearing active on every turn. A ranking function establishes a finite bound on admitted steps under explicit transition assumptions. Suppose ${V}_t$ is a nonnegative integer and every admitted step decreases it by at least one:

$$
{V}_{t+1} \le {V}_t - 1.
$$

Then at most ${V}_0$ such steps can be admitted. An enforced remaining-step allowance is one example: decrement it when work is admitted and refuse another admission at zero. This bounds the count, not the duration of a step, task completion, or termination of previously dispatched remote work. Deadlines and outstanding-effect contracts remain separate (**[[01 Books/Volume III - Agentic Systems/04 The Agent Runtime/10 The Agent Harness/V3-10.10 Budgets and Ceilings#^sec-vol3-controlplane-accounting|Budgets and Ceilings]]**).

A task-progress measure has a different obligation: it must reflect the chosen task and observations. Useful investigation can leave candidate state unchanged, and an exploratory change can temporarily worsen a check result. Hash recurrence and stagnant metrics are therefore fallible signals for intervention, not ranking-function proofs (**[[01 Books/Volume III - Agentic Systems/04 The Agent Runtime/12 Failure Recovery/V3-12.07 Semantic Watchdogs#^sec-vol3-sagas-watchdogs|Semantic Watchdogs]]**).

Expected-drift arguments require an explicit stochastic stopping model and its assumptions. Merely adding a distance-to-goal term to remaining tokens or spending does not establish such a result, because the quantities have different units, their transitions need not share a monotonic direction, and a resource bound alone does not prove useful progress.

### Information Flow Security Lattice

^sec-vol3-appendix-math-lattice

When a prompt combines an authenticated operator instruction with an untrusted issue comment, the runtime needs a formal rule to decide which label governs the combined context. An **information-flow security lattice** expresses an ordering on security labels and operations for combining them:

$$
{\mathbb{L}} = \langle {\mathcal{S}_{\text{lab}}}, \sqsubseteq, \sqcup, \sqcap \rangle
$$

where ${\mathcal{S}_{\text{lab}}}$ is the set of security labels, $\sqsubseteq$ is the label ordering, $\sqcup$ is the join operator (least upper bound), and $\sqcap$ is the meet operator (greatest lower bound). A runtime must separately specify how this ordering governs each protected use or destination.

Integrity provenance and confidentiality answer different questions. Integrity concerns the evidence permitted to influence a decision; confidentiality concerns permitted recipients. As a small illustration of integrity-dependency propagation, let ${\iota} \in \{\text{Trusted}, \text{Untrusted}\}$ use this order:

$$
\text{Trusted} \sqsubset \text{Untrusted}
$$

Here `Trusted` means qualified under the policy for a specified use rather than universally true. An authenticated task instruction can establish permitted scope without certifying every factual assertion it contains. A protected runner’s observation can support a particular test result under its execution contract, whereas a README’s claim that the test passed cannot substitute for it. `Untrusted` records any dependency not so qualified, though this two-element example is not a complete policy for both integrity and confidentiality.

For a context ${c}_{t}$ containing labeled input segments ${x}_i$, a conservative aggregate label joins their dependencies:

$$
{\iota}({c}_{t}) = \bigsqcup_{i=1}^{|{c}_{t}|} {\iota}({x}_i)
$$

Under this conservative policy, selecting any untrusted input makes the aggregate carry untrusted provenance. The join summarizes tracked dependencies rather than measuring causal influence inside attention. Extraction into typed fields therefore does not clear provenance, and derived summaries or stored records retain the relevant dependencies. A trusted decision may endorse a particular use on stated evidence, while authorized release of confidential data remains a separate declassification decision. **[[01 Books/Volume III - Agentic Systems/03 Tool Use/09 Agent Security/V3-09.07 Information-Flow Policy#^sec-vol3-security-taint-tracking|Information-Flow Policy]]** applies these distinctions at the operation and destination boundary.

## Representation Methods

^sec-vol3-appendix-math-representation-methods

Constrained output, repository ranking, and compressed retrieval representations solve different problems. The results below expose the mathematical assumptions behind each mechanism and the limits of its guarantee.

### Finite-State Constrained Decoding

^sec-vol3-appendix-math-dfa

A structured tool proposal must remain a viable prefix of the permitted output language while it is generated. For a regular language, a deterministic finite automaton (DFA) can track that constraint ([[05 Reference/Volume III - Agentic Systems/V3 Mathematical Foundations#^ref-willard2023outlines|Willard and Louf 2023]]). Unbounded recursive nesting, as in general JSON syntax, is not a regular-language problem; it requires additional parser state. The finite-state model below applies to regular subsets or explicitly bounded structures.

Let the automaton be

$$
{\mathcal{D}}=\langle {Q},{\Sigma},{\delta},{q}_0,{F}\rangle,
$$

where ${Q}$ is a finite state set, ${\Sigma}=\{0,\ldots,255\}$ is the byte alphabet, ${\delta}:{Q}\times{\Sigma}\to {Q}$ is the transition function, ${q}_0$ is the initial state, and ${F}$ is the accepting set. Invalid transitions enter a rejecting sink. Its extension to byte strings satisfies

$$
{\delta}^*({q},{\epsilon})={q},\qquad {\delta}^*({q},{b} {u})={\delta}^*({\delta}({q},{b}),{u}).
$$

Assume each ordinary vocabulary token ${v}$ decodes to a fixed nonempty byte string ${s}({v})$, and handle special tokens separately. If a tokenizer uses context-dependent decoding, its state must also enter the constraint machine. Define ${Q_{\text{live}}}$ as the states from which some finite sequence of ordinary vocabulary tokens reaches ${F}$. A transition that merely avoids a syntax error is insufficient if no tokenized completion remains possible.

At state ${q}_t$, the permitted ordinary tokens are

$$
{\mathcal{V}_{\text{valid}}}({q}_t)= \{{v}:{\delta}^*({q}_t,{s}({v}))\in {Q_{\text{live}}}\}.
$$

Permit the end-of-sequence token only when ${q}_t\in {F}$. Mask all other disallowed special tokens. If ${\mathcal{V}_{\text{allow}}}({q}_t)$ includes the permitted ordinary tokens and any permitted end token, the masked logits and probabilities are

$$
{z'}_{t,{v}}= \begin{cases} {z_{t,v}}&{v}\in{\mathcal{V}_{\text{allow}}}({q}_t),\\ -\infty&{v}\notin{\mathcal{V}_{\text{allow}}}({q}_t), \end{cases} \qquad \Pr({x}_t={v}\mid {x_{<t}})= \frac{\exp({z'}_{t,{v}})}{\sum_{w}\exp({z'}_{t,{w}})}.
$$

This normalization requires at least one allowed token with finite logit. If later sampling filters eliminate all such tokens, decoding must report failure rather than normalize an empty support.

Starting from a live initial state, induction establishes that every admitted ordinary token preserves the possibility of a valid completion. A generation that ends with a permitted end token therefore belongs to the specified language. The argument does not guarantee termination within a token budget, nor does it preserve the unconstrained model’s sequence distribution. A cutoff can leave an incomplete prefix that must not be accepted as a complete tool proposal.

For a fixed finite automaton and tokenizer, token masks can be precomputed per state. The table removes repeated vocabulary–automaton traversal, not every cost of applying a mask or sampling; **[[05 Reference/Volume III - Agentic Systems/V3 Inference Cost Foundations#^sec-vol3-appendix-inference-decode-loop|Decode-Loop Mechanics]]** accounts for its placement beside the sampler. Syntactic acceptance still says nothing about whether the named object exists, the action is authorized, or the proposed operation satisfies the task.

### PageRank Symbol Graphing for Repository Maps

^sec-vol3-appendix-math-pagerank

To build a compact repository map within a token budget, a runtime can model the codebase as a directed graph $({V}, {E})$ of symbol definitions and references. Declare the edge direction before ranking: following references and following reverse dependencies answer different questions. Let ${A}_{ij}\ge0$ be the weight of an edge from symbol ${i}$ to symbol ${j}$, and let ${\mathbf{p}}$ be a nonnegative personalization vector whose entries sum to one. Normalize each nonempty row of ${\mathbf{A}}$ to a probability distribution; for a dangling symbol with no outgoing edge, use ${\mathbf{p}}^T$ as its row. The resulting matrix ${\mathbf{P}_{\text{graph}}}$ is row stochastic.

For a chosen damping factor $0\le {d}<1$, the personalized PageRank vector satisfies

$$
{\mathbf{r}}=(1-{d}){\mathbf{p}}+{d}{\mathbf{P}_{\text{graph}}}^T{\mathbf{r}}.
$$

Initialized with a probability vector, each iteration preserves nonnegativity and unit total mass. Because multiplication by ${\mathbf{P}_{\text{graph}}}^T$ is nonexpansive in the vector $1$-norm, the damped update contracts differences by at most ${d}$, giving a unique fixed point. Personalization can favor symbols implicated by the task, but this preference is an input to the ranking rather than evidence that a symbol is necessary.

Sorting symbols by score and packing them within a token budget produces one candidate repository map. **[[01 Books/Volume III - Agentic Systems/02 Agent Memory/06 Long-Term Memory/V3-06.08 Multi-Hop Retrieval#^sec-vol3-persistent-graphrag|Multi-Hop Retrieval]]** considers this ranking as an optional graph prioritizer; a runtime can pre-stage such a map under the policy described in **[[01 Books/Volume III - Agentic Systems/02 Agent Memory/06 Long-Term Memory/V3-06.05 Agentic Retrieval#^sec-vol3-long-term-memory-agentic-retrieval|Agentic Retrieval]]**. Ranking and packing do not guarantee that the selected symbols preserve a complete dependency path or supply the evidence a task needs.

### Truncated SVD and Low-Rank Attention Approximations

^sec-vol3-appendix-math-svd

An existing attention-state matrix can be approximated by a lower-rank matrix, trading storage for reconstruction error. The truncated singular value decomposition (SVD) gives an error bound for this approximation. It is not a derivation of learned latent-attention architectures or a guarantee about task quality; **[[01 Books/Volume III - Agentic Systems/02 Agent Memory/05 KV Cache Management/V3-05.03 The Footprint of Retained Attention State#^sec-vol3-kvcache-geometry|The Footprint of Retained Attention State]]** distinguishes those model-design and storage choices.

Let ${\mathbf{K}}^{(\ell)} \in \mathbb{R}^{{S} \times {d_{\text{head}}}}$ denote the uncompressed Key activation matrix for layer $\ell$ across an active sequence of ${S}$ tokens. The singular value decomposition factors ${\mathbf{K}}^{(\ell)}$ into orthogonal singular vectors:

$$
{\mathbf{K}}^{(\ell)} = {\mathbf{U}} {\boldsymbol{\Sigma}} {\mathbf{V}}^T = \sum_{i=1}^{\min({S}, {d_{\text{head}}})} {\sigma}_i {\mathbf{u}}_i {\mathbf{v}}_i^T
$$

where ${\mathbf{U}} \in \mathbb{R}^{{S} \times {S}}$ and ${\mathbf{V}} \in \mathbb{R}^{{d_{\text{head}}} \times {d_{\text{head}}}}$ are orthonormal basis matrices, and ${\boldsymbol{\Sigma}}$ contains ordered singular values ${\sigma}_1 \ge {\sigma}_2 \ge \dots \ge {\sigma_{\min(S, d_{\text{head}})}} \ge 0$.

A rank-${r}$ truncated SVD approximation ${\hat{\mathbf{K}}_r}^{(\ell)}$ retains the first ${r}$ singular components, with $0\le {r}\le {q}=\min({S},{d_{\text{head}}})$:

$$
{\hat{\mathbf{K}}_r}^{(\ell)} = {\mathbf{U}_r} {\boldsymbol{\Sigma}_r} {\mathbf{V}_r}^T = \sum_{i=1}^{{r}} {\sigma}_i {\mathbf{u}}_i {\mathbf{v}}_i^T
$$

By the classical **Eckart-Young-Mirsky Theorem**, the truncated matrix ${\hat{\mathbf{K}}_r}^{(\ell)}$ is the mathematically optimal rank-${r}$ approximation to ${\mathbf{K}}^{(\ell)}$ under both the spectral norm ($\|\cdot\|_2$) and the Frobenius norm ($\|\cdot\|_{F}$). Specifically, the minimum Frobenius reconstruction error is determined entirely by the discarded tail singular values:

$$
\min_{\operatorname{rank}({\mathbf{A}}) \le {r}} \|{\mathbf{K}}^{(\ell)} - {\mathbf{A}}\|_{F} = \|{\mathbf{K}}^{(\ell)} - {\hat{\mathbf{K}}_r}^{(\ell)}\|_{F} = \sqrt{\sum_{j={r}+1}^{{q}} {\sigma}_j^2}
$$

For a nonzero matrix, the fraction of total squared Frobenius norm, often called activation energy here, preserved by the rank-${r}$ approximation is

$$
{\eta_r} = \frac{\sum_{i=1}^{r} {\sigma}_i^2}{\sum_{i=1}^{{q}} {\sigma}_i^2}.
$$

The zero matrix has zero reconstruction error at every rank, but its energy fraction is undefined because the denominator is zero. For ${r}<{q}$, the spectral error is ${\sigma_{r+1}}$. Cauchy–Schwarz therefore bounds the error of each unscaled query–key dot product by $\|{\mathbf{q}}\|_2{\sigma_{r+1}}$; at ${r}={q}$ the error is zero. Scaled attention scores inherit the corresponding scaling factor.

A steeply decaying spectrum permits a small matrix reconstruction error. It does not establish a small error after attention normalization or preserve task acceptance. Measure the spectrum and the resulting behavior under the intended workload rather than selecting rank from energy retention alone.

### High-Dimensional Measure Concentration and the Curse of Dimensionality

^sec-vol3-appendix-math-curse-dimensionality

When an embedding dimension grows into the hundreds or thousands, the Euclidean distance from a query to its nearest candidate can approach the distance to its farthest candidate, weakening spatial-tree pruning in **[[01 Books/Volume III - Agentic Systems/02 Agent Memory/06 Long-Term Memory/V3-06.07 Dense and Hybrid Retrieval#^sec-vol3-persistent-dense-retrieval|Dense and Hybrid Retrieval]]**. To make the assumptions behind that behavior explicit, this section derives the volume of a ${D}$-dimensional Euclidean ball and examines conditions under which distance contrast deteriorates. These conditional geometric results are not a guarantee that every learned embedding collection defeats spatial indexes or requires approximate search.

#### Continuous Hypersphere Volume and Shell Concentration

^continuous-hypersphere-volume-and-shell-concentration

The volume of a ${D}$-dimensional Euclidean ball of radius ${r}$ is given by:

$$
{V_D}({r}) = \int_{\|{\mathbf{y}}\|_2 \le {r}} {d}{\mathbf{y}} = {r}^{D} \cdot {V_D}(1)
$$

To compute the unit ball volume ${V_D}(1)$, we integrate the separable Gaussian function $\exp(-\|{\mathbf{y}}\|_2^2)$ over all $\mathbb{R}^{D}$:

$$
\int_{\mathbb{R}^{D}} e^{-\|{\mathbf{y}}\|_2^2} {d}{\mathbf{y}} = \prod_{i=1}^{D} \int_{-\infty}^{\infty} e^{-{y}_i^2} d{y}_i = (\sqrt{\pi})^{D} = \pi^{{D}/2}
$$

Switching to spherical polar coordinates, with differential surface area ${S_{D-1}}({r}) = \frac{{d}}{d{r}} {V_D}({r}) = {D} \cdot {r}^{{D}-1} {V_D}(1)$:

$$
\int_{\mathbb{R}^{D}} e^{-\|{\mathbf{y}}\|_2^2} {d}{\mathbf{y}} = \int_0^\infty e^{-{r}^2} {S_{D-1}}({r}) d{r} = {D} \cdot {V_D}(1) \int_0^\infty {r}^{{D}-1} e^{-{r}^2} d{r}
$$

Applying the substitution ${u} = {r}^2$ ($d{u} = 2{r} d{r}$):

$$
\int_0^\infty {r}^{{D}-1} e^{-{r}^2} d{r} = \frac{1}{2} \int_0^\infty {u}^{\frac{{D}}{2} - 1} e^{-{u}} d{u} = \frac{1}{2} {\Gamma}\left(\frac{{D}}{2}\right)
$$

Equating the Cartesian and spherical integrals:

$$
\pi^{{D}/2} = {D} \cdot {V_D}(1) \cdot \frac{1}{2} {\Gamma}\left(\frac{{D}}{2}\right) = {V_D}(1) \cdot \frac{{D}}{2} {\Gamma}\left(\frac{{D}}{2}\right) = {V_D}(1) \cdot {\Gamma}\left(\frac{{D}}{2} + 1\right)
$$

Solving for ${V_D}(1)$ and scaling by ${r}^{D}$ yields the closed-form volume:

$$
{V_D}({r}) = \frac{\pi^{{D}/2}}{{\Gamma}\left(\frac{{D}}{2} + 1\right)} {r}^{D}
$$

For an outer shell of relative thickness ${\epsilon}$ ($0 < {\epsilon} < 1$), the volume of the inner sphere of radius ${r}(1 - {\epsilon})$ is ${V_D}({r}(1 - {\epsilon})) = (1 - {\epsilon})^{D} {V_D}({r})$. The fraction of total volume contained in the outer shell is:

$$
\frac{{V_D}({r}) - {V_D}({r}(1 - {\epsilon}))}{{V_D}({r})} = 1 - (1 - {\epsilon})^{D}
$$

As ${D}\to\infty$, $(1-{\epsilon})^{D}\to0$ exponentially fast for fixed positive ${\epsilon}$. This is a statement about uniform volume within a ball. It does not establish the distribution of learned embeddings, which can occupy a structured subset of their ambient space.

#### Vanishing Distance Contrast

^vanishing-distance-contrast

Distance concentration can reduce the relative contrast between the closest and farthest candidates ([[05 Reference/Volume III - Agentic Systems/V3 Mathematical Foundations#^ref-beyer1999nearest|Beyer et al. 1999]]). The following sufficient-condition argument makes the fixed-dataset-size assumption explicit; it does not say that a nearest neighbor ceases to exist.

Let ${\mathbf{x}}_1, \dots, {\mathbf{x}_N}$ be independent random vectors in $\mathbb{R}^{D}$ drawn from a distribution with finite moments, and let ${\mathbf{q}}$ be an independent query vector. Define ${D_{\min}}({N}, {D}) = \min_{1 \le i \le {N}} \|{\mathbf{x}}_i - {\mathbf{q}}\|_{p}$ and ${D_{\max}}({N}, {D}) = \max_{1 \le i \le {N}} \|{\mathbf{x}}_i - {\mathbf{q}}\|_{p}$.

Assume distances are positive almost surely, so the relative contrast has a nonzero denominator. Suppose each query–candidate distance has the same finite positive mean and finite variance at dimension ${D}$, with relative variance satisfying

$$
\lim_{{D} \to \infty} \frac{\operatorname{Var}(\|{\mathbf{x}} - {\mathbf{q}}\|_{p})}{\mathbb{E}[\|{\mathbf{x}} - {\mathbf{q}}\|_{p}]^2} = 0
$$

then for any fixed dataset size ${N}$ and any ${\epsilon_{\text{contrast}}} > 0$:

$$
\lim_{{D} \to \infty} \Pr\left( \frac{{D_{\max}}({N}, {D}) - {D_{\min}}({N}, {D})}{{D_{\min}}({N}, {D})} \le {\epsilon_{\text{contrast}}} \right) = 1
$$

To derive the result, let ${\mu_D}$ be the common mean distance. Chebyshev’s inequality bounds the probability that one distance differs from ${\mu_D}$ by more than ${\delta}{\mu_D}$ by its relative variance divided by ${\delta}^2$. A union bound over fixed ${N}$ makes the probability of any such deviation tend to zero. This step needs no independence between distances, which share the query. On the complementary event, with $0<{\delta}<1$,

$$
\frac{{D_{\max}}-{D_{\min}}}{{D_{\min}}} \le\frac{2{\delta}}{1-{\delta}}.
$$

Choosing ${\delta}$ small enough for the specified ${\epsilon_{\text{contrast}}}$ proves the displayed convergence. If ${N}$ grows with dimension, the union bound requires additional control over that growth.

Reduced contrast can weaken pruning based on distance bounds, but does not prove that every tree index must visit every leaf. Index geometry, intrinsic dimension, query distribution, and approximation tolerance determine the actual work. The engineering use of this result is to test those assumptions against the intended retrieval workload, not to infer index performance from ambient dimension alone.

## Resource Models

^sec-vol3-appendix-math-resource-models

Queueing and recovery estimates depend on which resource is held and which work must be repeated. These models make that boundary explicit before deriving a delay or a cadence.

### Heavy-Tailed Queueing Theory

^sec-vol3-appendix-math-queueing

Long service times delay later arrivals when a worker must finish its current task before admitting another. To isolate that effect, consider a stationary ${M}/{G}/1$ queue with Poisson arrivals at rate ${\lambda_{\text{arr}}}$, one first-come, first-served server, and independent, identically distributed service times ${T_{\text{svc}}}$ independent of the arrival process. Assume an unlimited waiting room, no abandonment, ${\rho_{\text{serv}}}={\lambda_{\text{arr}}}\mathbb{E}[{T_{\text{svc}}}]<1$, and a finite second moment. The Pollaczek–Khinchine mean waiting-time formula is

$$
\mathbb{E}[{T_{\text{queue}}}] = \frac{{\lambda_{\text{arr}}} \mathbb{E}[{T_{\text{svc}}}^2]}{2 (1 - {\rho_{\text{serv}}})}.
$$

The role of the second moment follows from residual service. A service interval of length ${s}$ contributes area ${s}^2/2$ under its remaining-service curve. Averaging these areas over time gives mean residual work ${\lambda_{\text{arr}}}\mathbb{E}[{T_{\text{svc}}}^2]/2$. A Poisson arrival sees that time average. The queued jobs ahead contribute $\mathbb{E}[{N_{\text{queue}}}]\mathbb{E}[{T_{\text{svc}}}]$, and Little’s law gives $\mathbb{E}[{N_{\text{queue}}}]={\lambda_{\text{arr}}}\mathbb{E}[{T_{\text{queue}}}]$. Thus

$$
\mathbb{E}[{T_{\text{queue}}}] =\frac{{\lambda_{\text{arr}}}\mathbb{E}[{T_{\text{svc}}}^2]}{2} +{\rho_{\text{serv}}}\mathbb{E}[{T_{\text{queue}}}],
$$

which yields the displayed formula. The derivation concerns waiting before service, not total response time or a tail percentile.

Heavy-tailed service can make the second moment large; an idealized model with finite mean but infinite second moment has infinite mean waiting time even at stable positive load. Agent systems need not satisfy the queue’s arrival or service assumptions. In particular, tool waits, batching, retries, and call-level admission change the service boundary. **[[01 Books/Volume III - Agentic Systems/04 The Agent Runtime/10 The Agent Harness/V3-10.09 Scheduling Concurrent Trajectories#^sec-vol3-controlplane-scheduling|Scheduling Concurrent Trajectories]]** uses that boundary to compare interference policies, while **[[01 Books/Volume III - Agentic Systems/06 Agents at Scale/19 Agent Economics/V3-19.07 Capacity for Trajectories#^sec-vol3-agent-economics-capacity|Capacity for Trajectories]]** separates worker, workspace, and cache holding times.

### Pareto Tail Models and Runtime Bounds

^sec-vol3-appendix-math-pareto

A task’s unconstrained demand can vary widely even when every individual model call has an output ceiling. An enforced turn limit bounds admitted trajectory steps; a deadline constrains a different quantity and depends on how outstanding work is handled. Tail modeling describes demand within those controls, not a reason to remove them.

For a continuous Pareto reference model ${X}$ with minimum ${x_{\min}}>0$ and index ${\alpha_{\text{tail}}}>0$,

$$
\Pr({X}>{x})=\left(\frac{{x_{\min}}}{{x}}\right)^{{\alpha_{\text{tail}}}}, \qquad {x}\ge {x_{\min}}.
$$

A measured integer step-count tail can approximate this shape over a stated range, but is not literally this continuous distribution. Integrating the tail gives a finite mean only for ${\alpha_{\text{tail}}}>1$ and a finite second moment only for ${\alpha_{\text{tail}}}>2$:

$$
\mathbb{E}[{X}]=\frac{{\alpha_{\text{tail}}} {x_{\min}}}{{\alpha_{\text{tail}}}-1}, \qquad \mathbb{E}[{X}^2]=\frac{{\alpha_{\text{tail}}} {x_{\min}}^2}{{\alpha_{\text{tail}}}-2}.
$$

Each expression applies only in its respective finite-moment range. For $1<{\alpha_{\text{tail}}}\le2$, the mean exists and the variance is infinite in the unbounded model. For ${\alpha_{\text{tail}}}\le1$, even the mean is infinite. A capped variable $\min({X},{x_{\max}})$ has finite moments for every finite ${x_{\max}}$; a finite observed tail cannot establish that an actual deployment has infinite variance.

Step count is also not service time. To use the queueing result in [[05 Reference/Volume III - Agentic Systems/V3 Mathematical Foundations#^sec-vol3-appendix-math-queueing|section 1.3.1]], the model must describe service at the selected resource boundary. Variable call lengths and external waits can change that distribution even at a fixed number of turns. Capacity planning therefore needs means for average load, measured tails for service targets, and explicit limits for admitted work. No single fitted tail index replaces those three obligations (principle [[01 Books/Volume III - Agentic Systems/06 Agents at Scale/V3 Agents at Scale Principles#^pri-vol3-trajectory-goodput|15]]).

### Verification Cadence Models

^sec-vol3-appendix-math-verification

Frequent verification consumes resources; delayed detection can waste subsequent work. A cadence model is useful only after identifying which failures a check detects and which work can safely be repeated. It does not schedule mandatory authorization or precondition checks, and it cannot reverse an external effect.

#### A Rare-Error Balance

^a-rare-error-balance

Consider ${N}$ useful generation steps with homogeneous generation cost ${C_{\text{gen}}}$ per step and verification cost ${C_{\text{ver}}}$ per check. Express both costs in the same unit, such as money or serial elapsed time; do not add money to latency. Suppose checks occur every ${m}$ steps, errors occur at constant rate ${\lambda_{\text{error}}}$ per useful step, and errors are rare within an interval. Assume each check detects the modeled error, the extra work between error and detection averages ${m}/2$ steps, and recovery costs ${C_{\text{recovery}}}$ per error independently of ${m}$.

Ignoring partial final intervals and repeated errors during recovery gives the first-order model

$$
{C}({m})\approx {N} {C_{\text{gen}}}+\frac{{N}}{{m}}{C_{\text{ver}}} +{N}{\lambda_{\text{error}}} \left(\frac{{m}}{2}{C_{\text{gen}}}+{C_{\text{recovery}}}\right).
$$

The two cadence-dependent terms vary in opposite directions. Differentiating their sum for positive continuous ${m}$ gives

$$
\frac{d{C}}{d{m}} =-\frac{{N} {C_{\text{ver}}}}{{m}^2} +\frac{{N}{\lambda_{\text{error}}} {C_{\text{gen}}}}{2}, \qquad {m}^*=\sqrt{\frac{2{C_{\text{ver}}}} {{\lambda_{\text{error}}} {C_{\text{gen}}}}}.
$$

Consequently, the relaxed verification count is ${K}^*={N}/{m}^*$. Independence from ${N}$ follows from the homogeneous, long-run assumptions, not from a universal property of agent tasks. Actual schedules use feasible integer intervals, handle the final partial block, and respect deadlines and mandatory checks. Error bursts, state-dependent check power, and correlated recovery attempts require a different model.

#### Restarting Complete Blocks

^restarting-complete-blocks

A second model assumes that any erroneous block must be generated again from its start. Partition ${N}$ useful steps into blocks of ${m}$ steps, with ${m}$ dividing ${N}$. Let each step succeed independently with probability $0<{p}<1$, each generation take ${T_{\text{step}}}>0$, and each block check take ${T_{\text{ver}}}>0$. A check perfectly distinguishes successful from failed blocks. Every retry starts from the same recoverable state, draws independent outcomes, and has the same duration; reset overhead is negligible. No attempt has an externally visible effect that a retry would duplicate.

The block succeeds with probability ${p}^{m}$, so its number of attempts is geometric with mean ${p}^{-{m}}$. The expected completion time is

$$
{T}({m})=\frac{{N}}{{m}}\, \frac{{m} {T_{\text{step}}}+{T_{\text{ver}}}}{{p}^{m}} ={N} {p}^{-{m}}\left({T_{\text{step}}}+\frac{{T_{\text{ver}}}}{{m}}\right).
$$

Set ${a}=-\ln {p}>0$. Differentiating $\ln {T}({m})$ gives the stationary equation and its positive root:

$$
{a} {T_{\text{step}}} {m}^2+{a} {T_{\text{ver}}} {m}-{T_{\text{ver}}}=0,
$$

$$
{m}^*= \frac{-{T_{\text{ver}}}+ \sqrt{{T_{\text{ver}}}^2+4{T_{\text{step}}} {T_{\text{ver}}}/{a}}} {2{T_{\text{step}}}}.
$$

The derivative changes from negative to positive at this root. Compare feasible integer block sizes rather than rounding blindly. When ${a} {T_{\text{ver}}}/{T_{\text{step}}}\ll1$, the leading approximation is

$$
{m}^*\approx\sqrt{\frac{{T_{\text{ver}}}}{{a} {T_{\text{step}}}}} \approx\sqrt{\frac{{T_{\text{ver}}}}{(1-{p}){T_{\text{step}}}}},
$$

where the second approximation additionally requires ${p}$ close to one. If ${p}=1$, this model favors the largest permitted block because no regeneration is needed.

The absent factor of two distinguishes complete-block regeneration from a model that charges only average lost or wasted work within an interval. These models cannot be interchanged merely because both have square-root optima. Checkpointing in **[[01 Books/Volume III - Agentic Systems/04 The Agent Runtime/11 Durable Execution/V3-11.05 Checkpoints#^sec-vol3-persistence-checkpointing|Checkpoints]]** often reconstructs recorded events instead of regenerating model actions; that runtime must use its actual reconstruction cost and unresolved-effect contract.

### Checkpoint Lost-Work Balance

^sec-vol3-appendix-math-daly

A checkpoint can reduce work that must be repeated after a failure, but saving it also interrupts useful execution. Young’s first-order model balances these terms ([[05 Reference/Volume III - Agentic Systems/V3 Mathematical Foundations#^ref-young1974|Young 1974]]). Let ${T_{\text{ckpt}}}>0$ be useful execution time between completed checkpoints, ${T_{\text{write}}}>0$ their fixed duration, and ${\text{MTBF}}$ the mean time between failures. Assume rare Poisson failures independent of progress, small checkpoint overhead, reliable saved state, and restart cost ${T_{\text{restart}}}$ independent of ${T_{\text{ckpt}}}$.

To first order, failures occur approximately uniformly within a useful-work interval, so each loses an average of ${T_{\text{ckpt}}}/2$ work. Ignoring failures during saving and recovery gives approximate overhead per unit useful time

$$
{w}({T_{\text{ckpt}}})\approx \frac{{T_{\text{write}}}}{{T_{\text{ckpt}}}} +\frac{{T_{\text{ckpt}}}}{2\,{\text{MTBF}}} +\frac{{T_{\text{restart}}}}{{\text{MTBF}}}.
$$

Differentiation isolates the cadence-dependent terms:

$$
{w}'({T_{\text{ckpt}}})=-\frac{{T_{\text{write}}}}{{T_{\text{ckpt}}}^2} +\frac{1}{2\,{\text{MTBF}}}, \qquad {w}''({T_{\text{ckpt}}})=\frac{2{T_{\text{write}}}}{{T_{\text{ckpt}}}^3}>0.
$$

The minimizing interval of this approximate cost function is therefore

$$
{T^\ast_{\text{ckpt}}}=\sqrt{2\,{T_{\text{write}}}\,{\text{MTBF}}}.
$$

Restart cost raises overhead but does not move this optimum because it is constant with respect to ${T_{\text{ckpt}}}$. A more complete model can include failures during saving and recovery; Daly ([[05 Reference/Volume III - Agentic Systems/V3 Mathematical Foundations#^ref-daly2006|2006]]) develops such refinements. They do not follow by adding restart time to ${T_{\text{write}}}$ in the displayed square root.

This calculation applies only when failure loses work that must be re-executed. A durable agent may instead reconstruct recorded state without resampling its past decisions. **[[01 Books/Volume III - Agentic Systems/04 The Agent Runtime/11 Durable Execution/V3-11.05 Checkpoints#^sec-vol3-persistence-checkpointing|Checkpoints]]** models that different cost. Neither a saved state nor this timing calculation rolls back committed external actions; their recovery protocol remains necessary.

## Statistical Decisions

^sec-vol3-appendix-math-statistical-decisions

A release decision requires a declared experiment and criterion. These entries separate sample planning, repeated-run estimands, sequential evidence, and cost-sensitive escalation.

### Statistical Planning and Bootstrap Intervals

^sec-vol3-appendix-math-bootstrap

Treating repeated runs of the same 20 tasks as 200 independent trials understates confidence-interval width and can make noise look like a release-ready gain. The sampling design determines which uncertainty calculation applies. **[[01 Books/Volume III - Agentic Systems/04 The Agent Runtime/13 Agent Evaluation/V3-13.06 Statistical Evaluation Rigor#^sec-vol3-evaluation-resampling|Tasks and repeated runs]]** distinguishes tasks from repeated runs, and **[[01 Books/Volume III - Agentic Systems/04 The Agent Runtime/13 Agent Evaluation/V3-13.06 Statistical Evaluation Rigor#^sec-vol3-evaluation-wilson|Confidence intervals for acceptance]]** separates a single proportion from a paired candidate–baseline difference. This section gives an approximate sample-size calculation for independent arms, states the paired-score interval that the chapter’s worksheet uses, and defines a bootstrap construction for a declared statistic that lacks an analytic interval.

#### Plan an Independent-Arm Comparison

^plan-an-independent-arm-comparison

Suppose two arms contain independent Bernoulli trials, with the same number ${n_{\text{arm}}}$ in each arm. Their hypothesized success probabilities are ${p}_1$ and ${p}_2$, with $0<{p}_1<{p}_2<1$. Let ${\Delta} {p}={p}_2-{p}_1$ and ${\bar{p}}=({p}_1+{p}_2)/2$. Under these assumptions, the difference of sample proportions has alternative variance

$$
\frac{{p}_1(1-{p}_1)+{p}_2(1-{p}_2)}{{n_{\text{arm}}}}.
$$

For a two-sided normal-approximation test with significance target ${\alpha_{\text{sig}}}$ and power target $1-{\beta}$, a common planning approximation places the positive rejection boundary ${z_{1-\alpha_{\text{sig}}/2}}\sqrt{2{\bar{p}}(1-{\bar{p}})/{n_{\text{arm}}}}$ below the alternative mean by ${z_{1-\beta}}$ alternative standard deviations. Here ${z_q}$ is the standard normal quantile at probability ${q}$. Solving that relation gives

$$
{N_{\text{arm}}}= \left\lceil \frac{\left[{z_{1-\alpha_{\text{sig}}/2}}\sqrt{2{\bar{p}}(1-{\bar{p}})}+ {z_{1-\beta}}\sqrt{{p}_1(1-{p}_1)+{p}_2(1-{p}_2)}\right]^2}{({\Delta} {p})^2} \right\rceil.
$$

This is the equal-arm normal approximation implemented in Brant’s independent-proportion planning calculator ([[05 Reference/Volume III - Agentic Systems/V3 Mathematical Foundations#^ref-brantProportionsCalculator|Brant, n.d.]]). It neglects the far rejection tail under the specified alternative and uses an approximate pooled null variance. It is not an exact power guarantee, a minimum sample size for every useful finding, or a test of already observed results. Rare outcomes, dependence, unequal allocation, missing labels, or a paired design require the corresponding design calculation. Increasing repeats on a fixed task does not create independent tasks.

**Napkin Math 1.1: Plan two independent arms**

**Problem**: For hypothetical success probabilities 0.30 and 0.35, what equal-arm sample count does the approximation give at significance target 0.05 and power target 0.80?

**Calculation**: Using rounded normal quantiles 1.96 and 0.84, then rounding the result upward, gives 1,375 independent trials per arm.

**Scope**: This plans a particular independent-arm experiment before its outcomes are observed. It does not establish that an observed difference is significant, and it does not apply to the paired repair comparison by ignoring its within-task dependence. Sampling and grader fidelity still limit the population claim.

^callout-notebook-1-1-50fb1010

#### Interval for a Paired Difference of Proportions

^sec-vol3-appendix-math-newcombe

Pairing changes the uncertainty of a difference. Each sampled task yields one baseline outcome and one candidate outcome, cross-classified as in **[[01 Books/Volume III - Agentic Systems/04 The Agent Runtime/13 Agent Evaluation/V3-13.06 Statistical Evaluation Rigor#^tbl-vol3-mcnemar-contingency|Paired task outcomes]]**: ${n}_{11}$ tasks accepted by both configurations, ${b}$ by the baseline only, ${c}$ by the candidate only, and ${n}_{00}$ by neither. The total is ${N}={n}_{11}+{b}+{c}+{n}_{00}$. The marginal estimates are ${\hat{p}_{\text{cand}}}=({n}_{11}+{c})/{N}$ and ${\hat{p}_{\text{base}}}=({n}_{11}+{b})/{N}$, so ${\hat{\Delta}}=({c}-{b})/{N}$. Both proportions are measured on the same tasks, and their sampling errors are correlated. An interval that treated them as independent arms would ignore that dependence.

Newcombe’s method 10 assembles the paired interval from the two single-proportion Wilson intervals ([[05 Reference/Volume III - Agentic Systems/V3 Mathematical Foundations#^ref-newcombe1998improved|Newcombe 1998]]). Let $[{l_{\text{cand}}},{u_{\text{cand}}}]$ and $[{l_{\text{base}}},{u_{\text{base}}}]$ be the intervals of **[[01 Books/Volume III - Agentic Systems/04 The Agent Runtime/13 Agent Evaluation/V3-13.06 Statistical Evaluation Rigor#^eq-wilson-interval|equation 13.2]]** for the two marginal counts at the same ${z}$, and write their distances from the point estimates as

$$
{\delta^-_{\text{cand}}}={\hat{p}_{\text{cand}}}-{l_{\text{cand}}},\quad {\delta^+_{\text{cand}}}={u_{\text{cand}}}-{\hat{p}_{\text{cand}}},\quad {\delta^-_{\text{base}}}={\hat{p}_{\text{base}}}-{l_{\text{base}}},\quad {\delta^+_{\text{base}}}={u_{\text{base}}}-{\hat{p}_{\text{base}}}.
$$

The within-pair dependence enters through a phi coefficient whose numerator is continuity corrected when it is positive:

$$
{\hat{\phi}}=\frac{{A}}{\sqrt{({n}_{11}+{c})({b}+{n}_{00})({n}_{11}+{b})({c}+{n}_{00})}},\qquad {A}=\begin{cases} \max({n}_{11}{n}_{00}-{b} {c}-{N}/2,\ 0), & {n}_{11}{n}_{00}>{b} {c},\\ {n}_{11}{n}_{00}-{b} {c}, & \text{otherwise}, \end{cases}
$$

with ${\hat{\phi}}=0$ when the denominator is zero. The difference is smallest when the candidate proportion is low and the baseline proportion is high, so the lower limit combines the candidate’s downward distance with the baseline’s upward distance, and the upper limit combines the opposite pair:

$$
{L_{\Delta}}={\hat{\Delta}}-\sqrt{\left({\delta^-_{\text{cand}}}\right)^2-2{\hat{\phi}}\,{\delta^-_{\text{cand}}}{\delta^+_{\text{base}}}+\left({\delta^+_{\text{base}}}\right)^2},
$$

$$
{U_{\Delta}}={\hat{\Delta}}+\sqrt{\left({\delta^+_{\text{cand}}}\right)^2-2{\hat{\phi}}\,{\delta^+_{\text{cand}}}{\delta^-_{\text{base}}}+\left({\delta^-_{\text{base}}}\right)^2}.
$$

Setting ${\hat{\phi}}=0$ discards the pairing. A positive ${\hat{\phi}}$, produced when tasks tend to receive the same verdict under both configurations, subtracts the covariance term and narrows the interval without changing either marginal count. Newcombe’s method 8 uses the same construction with an uncorrected ${\hat{\phi}}$; in his coverage evaluation, the correction of method 10 removed the most severe coverage shortfalls of method 8. The interval remains nominal and approximate. It assumes independently sampled tasks, one complete verdict per configuration on each task, a level fixed in advance, and a single look at the data. The worksheet in **[[01 Books/Volume III - Agentic Systems/04 The Agent Runtime/13 Agent Evaluation/V3-13.06 Statistical Evaluation Rigor#^sec-vol3-evaluation-paired|Paired outcome comparison]]** implements this construction and checks it against two of Newcombe’s published examples.

#### Bootstrap the Statistic at Its Sampling Unit

^bootstrap-the-statistic-at-its-sampling-unit

For a statistic without a convenient analytic interval, the nonparametric bootstrap approximates repeated sampling from the observed empirical distribution ([[05 Reference/Volume III - Agentic Systems/V3 Mathematical Foundations#^ref-efron1994bootstrap|Efron and Tibshirani 1994]]). Let ${y}_1,\ldots,{y}_{{m}}$ be the independent sampled units and ${\widehat{\theta}}$ the statistic computed from them. Draw ${m}$ units with replacement, recompute the statistic, and repeat this procedure ${B_{\text{boot}}}$ times. If a unit is a paired task record, keep both configurations’ outcomes together; independently resampling the two columns destroys the pairing. Clustered observations require a resampling design that preserves the relevant cluster dependence.

Let ${B_{\text{boot}}}\ge1$ be an integer. Denote replicate ${r}$ by ${\widehat{\theta}}^{*({r})}$ and sort the bootstrap statistics as ${\widehat{\theta}}^*_{(1)}\le\cdots\le{\widehat{\theta}}^*_{({B_{\text{boot}}})}$. Define their empirical quantile by

$$
{Q}^*({u})=\inf\left\{{x}:\frac{1}{{B_{\text{boot}}}} \sum_{{r}=1}^{{B_{\text{boot}}}}{\mathbf{1}}\{{\widehat{\theta}}^{*({r})}\le {x}\}\ge {u}\right\}, \qquad 0<{u}<1.
$$

Equivalently, ${Q}^*({u})={\widehat{\theta}}^*_{(\lceil {B_{\text{boot}}} {u}\rceil)}$. The one-based index lies between $1$ and ${B_{\text{boot}}}$, including for small resample counts; different software may use interpolated quantiles instead.

For $0<{\alpha_{\text{sig}}}<1$, the percentile interval with nominal coverage $1-{\alpha_{\text{sig}}}$ is

$$
[{Q}^*({\alpha_{\text{sig}}}/2),\ {Q}^*(1-{\alpha_{\text{sig}}}/2)].
$$

This definition makes the ordering and finite-resample quantile convention explicit. The SciPy bootstrap documentation ([[05 Reference/Volume III - Agentic Systems/V3 Mathematical Foundations#^ref-scipyBootstrap|The SciPy community, n.d.]]) describes percentile intervals and paired resampling; it also distinguishes percentile, basic, and bias-corrected methods. The construction is not a universal coverage guarantee. A small or unrepresentative sample, strong skew, dependence, or a statistic that behaves poorly under resampling can invalidate its interpretation. More bootstrap replicates reduce Monte Carlo variability conditional on the data; they do not supply missing tasks, repair missing outcomes, or establish an unobserved tail. The paired-score interval in **[[01 Books/Volume III - Agentic Systems/04 The Agent Runtime/13 Agent Evaluation/V3-13.06 Statistical Evaluation Rigor#^sec-vol3-evaluation-wilson|Confidence intervals for acceptance]]** is a separate method, not this bootstrap interval.

### Pass@${k}$ and Repeated-Run Consistency

^sec-vol3-appendix-math-pass-at-k

An agent that passes a repair benchmark once in ten tries supports a best-of-${k}$ selector, but fails four times out of five when deployed as a single-attempt autonomous workflow. To separate candidate availability from repeated-run reliability, fix one task, its initial-state distribution, the complete run policy, and a binary pass criterion. Suppose the runs are independent and identically distributed conditional on that task, with per-run pass probability ${p}$. Among ${n}\ge {k}\ge1$ fully graded runs, let ${c}$ pass. These are integer counts with $0\le {c}\le {n}$. Pending or unavailable labels require the declared missing-outcome policy rather than silent exclusion.

#### Average Over Candidate Subsets

^average-over-candidate-subsets

For every subset ${J}$ of ${k}$ run indices, let ${I_J}$ indicate that at least one member passed. Averaging these indicators over all $\binom {n} {k}$ subsets gives

$$
{\widehat{q}}_k=\frac{1}{\binom {n} {k}}\sum_{|{J}|=k}{I_J} =1-\frac{\binom{{n}-{c}}{{k}}}{\binom {n} {k}}.
$$

The failure numerator is zero when ${n}-{c}<{k}$. Each subset comprises ${k}$ conditionally independent runs, so $\mathbb{E}[{I_J}]=1-(1-{p})^{k}$. Linearity of expectation therefore establishes

$$
\mathbb{E}[{\widehat{q}}_k]=1-(1-{p})^{k}.
$$

The subset indicators need not be mutually independent for this expectation argument. Chen et al. ([[05 Reference/Volume III - Agentic Systems/V3 Mathematical Foundations#^ref-chen2021evaluating|2021]]) use this unbiased estimator for test-passing candidate availability. It does not establish that a deployed selector returns a passing candidate within its allowance; **[[01 Books/Volume III - Agentic Systems/01 The Model/03 Test-Time Compute/V3-03.04 Selecting from a Candidate Pool#^sec-vol3-test-time-compute-pass-at-k|Candidate availability under pass@k]]** develops that distinction. Generating ${n}={k}$ is valid, although its sampling variability must still be assessed.

#### Evaluate the Ratio without Factorials

^evaluate-the-ratio-without-factorials

For ${n}-{c}\ge {k}$, expand the failure ratio as

$$
\frac{\binom{{n}-{c}}{{k}}}{\binom {n} {k}} =\prod_{j=0}^{{k}-1}\frac{{n}-{c}-{j}}{{n}-{j}} =\prod_{j=0}^{{k}-1}\left(1-\frac{{c}}{{n}-{j}}\right).
$$

Direct floating-point factorials can overflow even when the final ratio lies in $[0,1]$. The product avoids those factorials. A log representation also avoids intermediate products of many small factors:

$$
{s_{\text{fail}}}=\sum_{j=0}^{{k}-1}\log\left(1-\frac{{c}}{{n}-{j}}\right), \qquad {\widehat{q}}_k=1-\exp({s_{\text{fail}}}).
$$

In floating-point code, `log1p(-c / (n-j))` and `-expm1(s_fail)` reduce cancellation when the ratio is close to one. Handle ${n}-{c}<{k}$ before taking logarithms, returning ${\widehat{q}}_k=1$; ${c}=0$ gives zero coverage. The arithmetic takes $\mathcal{O}({k})$ terms but still has finite-precision limits. Stable evaluation does not remove uncertainty in the measured pass probability.

#### Require Every Repeated Run to Pass

^require-every-repeated-run-to-pass

Let ${I_J^{\text{all}}}$ indicate that every run in subset ${J}$ passed. Counting successful subsets and applying the same expectation argument gives

$$
{\widehat{r}}_k=\frac{\binom {c} {k}}{\binom {n} {k}}, \qquad \mathbb{E}[{\widehat{r}}_k]={p}^{k}.
$$

The numerator is zero when ${c}<{k}$. Otherwise,

$$
{\widehat{r}}_k=\prod_{j=0}^{{k}-1}\frac{{c}-{j}}{{n}-{j}}.
$$

This is the task-level repeated-run estimator in **[[01 Books/Volume III - Agentic Systems/04 The Agent Runtime/13 Agent Evaluation/V3-13.06 Statistical Evaluation Rigor#^eq-pass-pow-k|equation 13.5]]**. For a declared task distribution with task-specific probabilities ${p}_i$, the population quantities are

$$
\operatorname{pass@}{k}=\mathbb{E}_i[1-(1-{p}_i)^{k}], \qquad \operatorname{pass}^{{k}}=\mathbb{E}_i[{p}_i^{k}].
$$

Average the task-level estimates with the declared task weights, not weights proportional to how many repeats a task received. Under independently sampled new tasks and independent runs, the probability that all ${k}$ new tasks pass is instead $(\mathbb{E}_i[{p}_i])^{k}$. That is a different experiment. Shared outages, retained state, or feedback-conditioned revisions can violate the conditional independence used here. **[[01 Books/Volume III - Agentic Systems/04 The Agent Runtime/13 Agent Evaluation/V3-13.06 Statistical Evaluation Rigor#^sec-vol3-evaluation-pass-k|Potential and repeated-run consistency]]** states which complete policy, criterion, task distribution and observation cutoff accompany these metrics.

### Wald’s Sequential Probability Ratio Test (SPRT) Decision Boundaries

^sec-vol3-appendix-math-sprt

Repeatedly peeking at a fixed-sample test after every canary task inflates the false-alarm rate, whereas waiting for the full sample delays halting a degraded rollout. To test accumulating labels without invalidating the error bounds, the sequential example in **[[01 Books/Volume III - Agentic Systems/04 The Agent Runtime/14 Operating Agents/V3-14.06 Staged Releases#^sec-vol3-evaluation-releases|Staged Releases]]** compares two specified Bernoulli distributions ([[05 Reference/Volume III - Agentic Systems/V3 Mathematical Foundations#^ref-wald1945sequential|Wald 1945]]), distinct from the chapter’s paired offline comparison. Let independent labels ${x}_i\in\{0,1\}$ have a stationary acceptance probability ${p}$, with the label and observation policy fixed in advance. The simple hypotheses are

$$
{H}_0:{p}={p}_0,\qquad {H}_1:{p}={p}_1,\qquad 0<{p}_1<{p}_0<1.
$$

Both probabilities are design inputs. Treating an estimated historical baseline as known without accounting for its uncertainty changes this model. With ${d}_n=\sum_{i=1}^{{n}}{x}_i$, use the chapter’s log-likelihood ratio in favor of the specified degradation:

$$
{\Lambda}_n=\sum_{i=1}^{{n}}\log\frac{\Pr({x}_i\mid {p}_1)}{\Pr({x}_i\mid {p}_0)} ={d}_n\log\frac{{p}_1}{{p}_0}+({n}-{d}_n)\log\frac{1-{p}_1}{1-{p}_0}.
$$

A pass adds a negative increment and a failure a positive one. Stop and select ${H}_1$ at ${\Lambda}_n\ge {u}$, select ${H}_0$ at ${\Lambda}_n\le {b_{\text{low}}}$, and otherwise continue, with ${b_{\text{low}}}<0<{u}$. A statistical selection is not itself production authorization. In particular, selecting ${p}_0$ against this particular ${p}_1$ does not establish general noninferiority or absence of harmful effects.

#### Separate Realized Errors from Design Targets

^separate-realized-errors-from-design-targets

For the untruncated test, write its realized errors as

$$
{\alpha_{*}} = \Pr_0(\text{select }{H}_1),\qquad {\beta_{*}} = \Pr_1(\text{select }{H}_0).
$$

Here $\Pr_{{h}}$ means probability under ${H}_{{h}}$. At an upper-boundary stopping path, its likelihood under ${H}_1$ is at least $e^{{u}}$ times that under ${H}_0$. Summing over all such paths gives

$$
1-{\beta_{*}}\ge e^{{u}} {\alpha_{*}}.
$$

Likewise, summing over lower-boundary paths gives

$$
{\beta_{*}}\le e^{{b_{\text{low}}}}(1-{\alpha_{*}}).
$$

These relations concern realized operating characteristics, not arbitrary target values. Neglecting boundary overshoot replaces the inequalities by equalities. Substituting desired errors ${\alpha_{\text{sig}}}$ and ${\beta}$ then yields Wald’s approximate boundaries

$$
{u}=\log\frac{1-{\beta}}{{\alpha_{\text{sig}}}},\qquad {b_{\text{low}}}=\log\frac{{\beta}}{1-{\alpha_{\text{sig}}}}, \qquad 0<{\alpha_{\text{sig}}},{\beta}<1,\quad{\alpha_{\text{sig}}}+{\beta}<1.
$$

The targets have the same meanings as in **[[01 Books/Volume III - Agentic Systems/04 The Agent Runtime/14 Operating Agents/V3-14.06 Staged Releases#^eq-vol3-release-sprt-boundaries|equation 14.3]]**: ${\alpha_{\text{sig}}}$ targets selecting degradation under ${p}_0$, and ${\beta}$ targets selecting ${p}_0$ under ${p}_1$. Discrete observations generally overshoot the boundaries. The approximation does not establish ${\alpha_{*}}\le{\alpha_{\text{sig}}}$ and ${\beta_{*}}\le{\beta}$ individually; Fischer and Ramdas ([[05 Reference/Volume III - Agentic Systems/V3 Mathematical Foundations#^ref-fischer2026improving|2026]]) analyze that limitation. Validate the operating characteristics under the selected model and actual stopping policy. A sample or time cap introduces another disposition, inconclusive, whose probability must not be folded into favorable selection.

#### Approximate the Number of Labels Until Either Decision

^approximate-the-number-of-labels-until-either-decision

Let ${N_{\text{stop}}}$ be the untruncated stopping sample count. Under ${H}_1$, the mean increment is

$$
{m}_1={p}_1\log\frac{{p}_1}{{p}_0}+(1-{p}_1)\log\frac{1-{p}_1}{1-{p}_0}>0.
$$

For these independent, bounded Bernoulli log increments and a stopping time with finite expectation, Wald’s identity gives $\mathbb{E}_1[{\Lambda}_{{N_{\text{stop}}}}]={m}_1\mathbb{E}_1[{N_{\text{stop}}}]$. If overshoot is neglected, the terminal expectation is approximately $(1-{\beta_{*}}){u}+{\beta_{*}} {b_{\text{low}}}$. Substituting the design target ${\beta}$ for the realized error gives the further planning approximation

$$
\mathbb{E}_1[{N_{\text{stop}}}]\approx\frac{(1-{\beta}){u}+{\beta} {b_{\text{low}}}}{{m}_1}.
$$

The mixture includes both terminal decisions, including mistaken selection of ${H}_0$, as in the average-sample-number expression of Hory and Hero ([[05 Reference/Volume III - Agentic Systems/V3 Mathematical Foundations#^ref-hory2004sequential|2004]], eq. 24). It is not the conditional expected sample count until a degradation alarm. **[[01 Books/Volume III - Agentic Systems/04 The Agent Runtime/14 Operating Agents/V3-14.06 Staged Releases#^sec-vol3-evaluation-releases|Staged Releases]]** computes this approximation and adds an explicit label-delay model; the time conversion does not follow from the probability test alone.

Changing task mix, correlated trials, outcome-dependent completion ordering or missing labels can invalidate the assumed stream. A protocol must state which labels become available and how their order and unresolved cases enter the analysis. Multiple monitored metrics, repeated restarts and hard operational tripwires also change the decision procedure. Expected sample count is neither a maximum traffic exposure nor a harm bound. Admission limits and the recovery of outstanding effects remain separate runtime obligations.

### Escalation Under Asymmetric Costs

^sec-vol3-appendix-math-escalation

Routing every borderline tool call to a human reviewer stalls throughput, whereas executing every borderline call automatically risks an unrecoverable external failure. When policy permits a choice between automatic execution and human review, an optional decision model can frame that trade-off as a binary decision under uncertainty with asymmetric costs. The approval gate in **[[01 Books/Volume III - Agentic Systems/04 The Agent Runtime/10 The Agent Harness/V3-10.08 Approval Gates#^sec-vol3-controlplane-hitl|Approval Gates]]** enforces the selected policy; it does not make prohibited actions eligible for a cost-based exception.

Let ${a}$ denote a proposed action, and let ${Y}=1$ indicate the modeled damaging outcome if it executes automatically; ${Y}=0$ means that particular damage does not occur, not necessarily that the task succeeds. The runtime estimates the conditional probability $\Pr({Y}=1\mid{\mathbf{x}},{a})$ from observable features ${\mathbf{x}}$. Write the estimate as ${\hat{p}}$; it need not equal the true probability.

We define the loss matrix ${\mathbf{L}}({d},{y})$ for decision ${d}\in\{\text{Auto},\text{Escalate}\}$. All costs use a common unit, with ${C_{\text{blast}}}>0$ and ${C_{\text{human}}}\ge0$; any latency penalty must be converted to that unit before addition. This simplified model assumes that review always prevents the modeled damage; the approval mechanism itself supplies no such guarantee:

- ${\mathbf{L}}(\text{Auto}, 0) = {C_{\text{compute}}}$: The direct token and compute cost of autonomous execution.
- ${\mathbf{L}}(\text{Auto}, 1) = {C_{\text{compute}}} + {C_{\text{blast}}}$: The compute cost plus the unrecoverable damage of external failure.
- ${\mathbf{L}}(\text{Escalate}, 0) = {C_{\text{compute}}} + {C_{\text{human}}}$: The compute cost plus human supervisor inspection latency and labor cost.
- ${\mathbf{L}}(\text{Escalate}, 1) = {C_{\text{compute}}} + {C_{\text{human}}}$: Human intervention prevents the failure, incurring only inspection cost.

Under risk-neutral Bayesian decision theory, the expected risk ${\mathcal{R}}({d} \mid {\hat{p}})$ of each action is:

$$
{\mathcal{R}}(\text{Auto} \mid {\hat{p}}) = (1 - {\hat{p}}) {C_{\text{compute}}} + {\hat{p}} ({C_{\text{compute}}} + {C_{\text{blast}}}) = {C_{\text{compute}}} + {\hat{p}} \cdot {C_{\text{blast}}}
$$

$$
{\mathcal{R}}(\text{Escalate} \mid {\hat{p}}) = {C_{\text{compute}}} + {C_{\text{human}}}
$$

Using the estimated probability, review has lower modeled expected cost exactly when

$$
{\hat{p}} \cdot {C_{\text{blast}}} > {C_{\text{human}}} \iff {\hat{p}} > \frac{{C_{\text{human}}}}{{C_{\text{blast}}}} \equiv {p_{\text{threshold}}}
$$

At equality, either decision has the same modeled cost. If review has a residual damaging-outcome probability, its expected loss needs that additional term; the displayed threshold no longer applies unchanged.

#### Uncertainty and a Separate Risk Constraint

^uncertainty-and-a-separate-risk-constraint

Estimation variance alone does not establish that ${\hat{p}}$ understates risk, nor does it supply a valid upper confidence bound. A bound must follow from a declared sampling model and coverage procedure. Even a valid pointwise bound can lose its advertised coverage when the runtime adaptively selects actions or encounters a different population.

If a procedure supplies an upper bound ${p_U}$ for the relevant conditional damage probability, replacing ${\hat{p}}$ by ${p_U}$ gives a conservative cost comparison on the event that the bound covers. The result is still a cost rule. It does not by itself prove a specified upper bound on the probability of an unhandled failure.

To see the distinction, suppose a policy separately requires automatic execution only where the true conditional probability satisfies ${p}({\mathbf{x}},{a})\le{\epsilon}$. Under the declared deployment distribution, that assumption yields

$$
\Pr({Y}=1,\ {d}=\text{Auto}) =\mathbb{E}[{\mathbf{1}}\{{d}=\text{Auto}\}{p}({\mathbf{x}},{a})] \le{\epsilon}\Pr({d}=\text{Auto})\le{\epsilon}.
$$

A confidence-bound implementation must account for failures of simultaneous coverage before claiming this result. Distribution shift, imperfect review, and dependence across repeated actions add further obligations. No expected-cost threshold replaces mandatory authority, precondition, or approval checks; **[[01 Books/Volume III - Agentic Systems/04 The Agent Runtime/12 Failure Recovery/V3-12.06 Irreversible Commitments#^sec-vol3-sagas-pivot|Irreversible Commitments]]** develops those checks for partial and uncertain outcomes.

## Learning Estimators

^sec-vol3-appendix-math-learning-estimators

A training update changes parameters using finite trajectory evidence. The derivations below distinguish parameterization, estimator properties, and conditional behavior bounds; none substitutes for evaluation of the resulting policy.

### LoRA Matrix Decomposition

^sec-vol3-appendix-math-lora

Updating every parameter of a 70-billion-parameter model for each specialized agent role multiplies both optimizer memory during training and checkpoint storage during serving. Low-rank adaptation (LoRA) avoids full-matrix updates by freezing the base weight matrix ${\mathbf{W}}_0 \in \mathbb{R}^{{d_{\text{out}}} \times {d_{\text{in}}}}$ and parameterizing the update with trainable factors ${\mathbf{B}} \in \mathbb{R}^{{d_{\text{out}}} \times {r}}$ and ${\mathbf{A}} \in \mathbb{R}^{{r} \times {d_{\text{in}}}}$, typically with ${r} \ll \min({d_{\text{out}}}, {d_{\text{in}}})$. With the scaling convention used in **[[01 Books/Volume III - Agentic Systems/05 Learning from Trajectories/16 Trajectory Fine-Tuning/V3-16.11 Parameter-Efficient Fine-Tuning#^sec-vol3-fine-tuning-peft|Parameter-Efficient Fine-Tuning]]**, the effective matrix is

$$
{\mathbf{W}} = {\mathbf{W}}_0 + {\Delta}{\mathbf{W}} = {\mathbf{W}}_0 + \frac{{\gamma}}{{r}} {\mathbf{B}}{\mathbf{A}}
$$

where ${\gamma}$ is a constant scaling hyperparameter.

During forward computation on an input activation vector ${\mathbf{x}}$:

$$
{\mathbf{h}} = {\mathbf{W}}_0 {\mathbf{x}} + {\Delta}{\mathbf{W}} {\mathbf{x}} = {\mathbf{W}}_0 {\mathbf{x}} + \frac{{\gamma}}{{r}} {\mathbf{B}} ({\mathbf{A}} {\mathbf{x}})
$$

A common initialization draws ${\mathbf{A}}$ from a Gaussian distribution ${\mathcal{N}}(0, {\sigma}^2)$ and sets ${\mathbf{B}}$ to zero, giving ${\Delta}{\mathbf{W}} = {\mathbf{0}}$ initially. This preserves this layer’s forward mapping when its other components and inputs are unchanged. The factors contain ${r}({d_{\text{out}}} + {d_{\text{in}}})$ trainable parameters rather than the base matrix’s ${d_{\text{out}}}{d_{\text{in}}}$. Sharing a base with several adapters is one deployment option, not an isolation boundary between their roles.

During backward propagation, gradients of the scalar loss ${\mathcal{L}}$ with respect to the adapter projection matrices ${\mathbf{A}}$ and ${\mathbf{B}}$ are computed using the matrix chain rule:

$$
\frac{\partial {\mathcal{L}}}{\partial {\mathbf{A}}} = \frac{{\gamma}}{{r}} {\mathbf{B}}^T \left( \frac{\partial {\mathcal{L}}}{\partial {\mathbf{h}}} \right) {\mathbf{x}}^T, \quad \frac{\partial {\mathcal{L}}}{\partial {\mathbf{B}}} = \frac{{\gamma}}{{r}} \left( \frac{\partial {\mathcal{L}}}{\partial {\mathbf{h}}} \right) ({\mathbf{x}}^T {\mathbf{A}}^T)
$$

The frozen base weights ${\mathbf{W}}_0$ receive zero gradient accumulation, eliminating optimizer state memory for ${\mathbf{W}}_0$ while preserving exact activation gradients $\frac{\partial {\mathcal{L}}}{\partial {\mathbf{x}}} = {\mathbf{W}}_0^T \left( \frac{\partial {\mathcal{L}}}{\partial {\mathbf{h}}} \right) + \frac{{\gamma}}{{r}} {\mathbf{A}}^T {\mathbf{B}}^T \left( \frac{\partial {\mathcal{L}}}{\partial {\mathbf{h}}} \right)$ to backpropagate through preceding layers. At the stated initialization, ${\mathbf{B}}={\mathbf{0}}$ makes the gradient of ${\mathbf{A}}$ zero, while the gradient of ${\mathbf{B}}$ can be nonzero. Updating ${\mathbf{B}}$ can therefore enable subsequent updates to both factors. Freezing the base eliminates its parameter-update state, not the need to propagate information through the layer or retain the activations required by the chosen backward implementation.

### Generalized Advantage Estimation and KL Divergence

^sec-vol3-appendix-math-rl

Scoring a 30-turn rollout solely by its raw terminal return injects every intermediate step’s noise into each token update, whereas relying on a one-step value estimate biases the update whenever the critic is inaccurate. Generalized advantage estimation (GAE) balances that bias and variance by combining observed rewards with an estimated value function ([[05 Reference/Volume III - Agentic Systems/V3 Mathematical Foundations#^ref-schulman2016high|Schulman et al. 2016]]). For a finite episode, let ${k}=0,\ldots,{H}-1$, let ${h}_k$ contain the interaction history and time, and let ${r}_k$ be the reward after action ${a}_k$. For discount ${\gamma}\in[0,1]$, define the remaining return and its conditional expectations:

$$
{R_{\geq k}}=\sum_{j=k}^{{H}-1}{\gamma}^{{j}-{k}}{r}_j,\qquad {V^{\pi}}({h}_k)=\mathbb E_\pi[{R_{\geq k}}\mid {h}_k],\qquad {Q^{\pi}}({h}_k,{a}_k)=\mathbb E_\pi[{R_{\geq k}}\mid {h}_k,{a}_k].
$$

The advantage is ${A^{\pi}}({h}_k,{a}_k)={Q^{\pi}}({h}_k,{a}_k)-{V^{\pi}}({h}_k)$. With an estimate ${\widehat{V}}$ and terminal value ${\widehat{V}}({h}_{{H}})=0$, the residual and finite-episode GAE recursion are

$$
{\delta}_k={r}_k+{\gamma}{\widehat{V}}({h}_{k+1})-{\widehat{V}}({h}_k),\qquad {\widehat{A}^{\text{GAE}}}_k=\sum_{\ell=0}^{{H}-1-{k}}({\gamma}{\lambda})^\ell{\delta}_{{k}+\ell} ={\delta}_k+{\gamma}{\lambda}{\widehat{A}^{\text{GAE}}}_{k+1},\qquad {\widehat{A}^{\text{GAE}}}_{{H}}=0.
$$

Here ${\lambda}\in[0,1]$. At ${\lambda}=1$, the sum telescopes to ${R_{\geq k}}-{\widehat{V}}({h}_k)$. At ${\lambda}=0$, it uses one residual, whose conditional expectation equals the advantage when the value function is exact. Approximate values introduce a bias–variance trade-off. A computational cutoff is not necessarily a terminal state; its bootstrap convention must match the objective. These estimators do not require an observed context to reveal the full environment state, but their conditioning information must be specified.

A reference-policy penalty answers a separate question: how different are two action distributions at the same input? For a fixed token prefix ${x}$, write ${p}({v})={\pi_\theta}({v}\mid {x})$ and ${q}({v})=\pi_{\text{ref}}({v}\mid {x})$. Assume positive probabilities on a common finite vocabulary. The exact divergence is

$$
{\mathcal{D}_{\text{KL}}}({p}\parallel {q})=\sum_{v} {p}({v})\log\frac{{p}({v})}{{q}({v})}.
$$

The nonnegative quantity ${d}({v})={q}({v})/{p}({v})-\log({q}({v})/{p}({v}))-1$ is a sample statistic, not the divergence itself. We can check its expectation directly:

$$
\mathbb E_{{v}\sim {p}}[{d}({v})] =\sum_{v} {q}({v})-\sum_{v} {p}({v})-\sum_{v} {p}({v})\log\frac{{q}({v})}{{p}({v})} ={\mathcal{D}_{\text{KL}}}({p}\parallel {q}).
$$

The sampling distribution matters. Tokens collected under an older behavior distribution are not samples from the current ${p}$ merely because both probabilities can be evaluated. At a fixed prefix, importance weighting by ${p}({v})/{b}({v})$ recovers this expectation from behavior distribution ${b}$ when the required support and integrability hold. It does not correct the distribution of prefixes by itself. A sampled training penalty must declare those choices rather than equating every token statistic with exact KL. Neither a penalty nor surrogate clipping grants authority or guarantees that optimization will preserve task behavior; **[[01 Books/Volume III - Agentic Systems/05 Learning from Trajectories/17 Reinforcement Learning from Verifiable Rewards/V3-17.06 Group Relative Policy Optimization#^sec-vol3-rlvr-grpo|Group Relative Policy Optimization]]** explains their role in the update.

### Credit Assignment Variance in Trajectory Optimization

^sec-vol3-appendix-math-credit-assignment

A long trajectory offers more opportunities for a reward to depend on earlier actions, but horizon alone does not determine gradient variance. Consider on-policy sampling with a terminal reward ${R}$, undiscounted finite horizon ${H}$, policy-independent environment dynamics, and a baseline ${b}_k({h}_k)$ fixed for the update and independent of the current sampled action conditional on its history. Under the regularity conditions for differentiating the trajectory expectation, a likelihood-ratio estimator is

$$
{\widehat{g}}=\sum_{k=0}^{{H}-1}\nabla_{\theta}\log{\pi_\theta}({a}_k\mid {h}_k)\,[{R}-{b}_k({h}_k)].
$$

Subtracting the baseline leaves the expectation unchanged because the conditional expected policy score is zero. The baseline changes the estimator, not the reward’s specification. A failed trajectory with ${R}=0$ has a negative multiplier only where its baseline is positive.

To inspect variance without conflating a vector covariance matrix with a scalar, fix a parameter-space direction ${u}$ and write

$$
{Z}_k={u}^T\nabla_{\theta}\log{\pi_\theta}({a}_k\mid {h}_k)\,[{R}-{b}_k({h}_k)].
$$

For finite second moments, the exact identity is

$$
\operatorname{Var}({u}^T{\widehat{g}}) =\sum_{k=0}^{{H}-1}\operatorname{Var}({Z}_k) +2\sum_{0\le k<j<{H}}\operatorname{Cov}({Z}_k,{Z}_j).
$$

Shared rewards and dependent interactions can produce nonzero cross terms, but their signs and magnitudes are not fixed by the number of turns. If every $\operatorname{Var}({Z}_k)\le{\sigma}^2$, Cauchy–Schwarz gives the conditional upper bound

$$
\operatorname{Var}({u}^T{\widehat{g}}) \le\left(\sum_{k=0}^{{H}-1}\sqrt{\operatorname{Var}({Z}_k)}\right)^2 \le {H}^2{\sigma}^2.
$$

This is an upper bound under a uniform variance assumption, not a prediction of quadratic growth. If cross terms vanish, the bound becomes ${H}{\sigma}^2$. More generally, the additional assumption $\lvert\operatorname{Cov}({Z}_k,{Z}_j)\rvert\le {C}{\alpha_{\text{corr}}}^{{j}-{k}}$ for constants ${C}\ge0$ and $0\le{\alpha_{\text{corr}}}<1$ gives

$$
\operatorname{Var}({u}^T{\widehat{g}}) \le {H}{\sigma}^2+2{C}\sum_{\ell=1}^{{H}-1}({H}-\ell){\alpha_{\text{corr}}}^\ell \le {H}\left({\sigma}^2+\frac{2{C}{\alpha_{\text{corr}}}}{1-{\alpha_{\text{corr}}}}\right).
$$

A discount factor or a dense step reward does not establish that covariance assumption. Replacing a terminal criterion with learned process scores can also change the objective and introduce assessment error. The engineering comparison in **[[01 Books/Volume III - Agentic Systems/05 Learning from Trajectories/17 Reinforcement Learning from Verifiable Rewards/V3-17.05 Credit Across Turns#^sec-vol3-rlvr-credit|Credit Across Turns]]** therefore asks what each estimator measures, how its uncertainty is assessed, and what obtaining its evidence costs. It does not infer sample efficiency from horizon or reward density alone.

### Conditional Error Bounds in Trajectory Imitation

^sec-vol3-appendix-math-compounding-error

A policy trained only on expert demonstrations can achieve a low single-step disagreement rate on reference states yet veer off course once its own first mistake takes it into states the expert never visited. Errors measured on reference-policy states differ from errors measured on learner-policy states (**[[01 Books/Volume III - Agentic Systems/05 Learning from Trajectories/16 Trajectory Fine-Tuning/V3-16.07 Exposure Bias#^sec-vol3-fine-tuning-exposure-bias|Exposure Bias]]**). To keep these apart, we derive both bounds for a finite horizon ${H}$, a deterministic reference policy $\pi^*$, and a possibly stochastic learner $\pi$ with the same initial-state distribution and environment dynamics. Neither bound predicts the realized cost of a particular agent.

Let ${d_\pi}^t$ be the state distribution before decision ${t}$ under $\pi$, and ${d_\pi}={H}^{-1}\sum_{t=1}^{H} {d_\pi}^t$. Include the relevant history in the state where needed. For immediate task cost ${C}({s},{a})\in[0,1]$, define

$$
{J}(\pi)=\sum_{t=1}^{H}\mathbb E_{{s}\sim {d_\pi}^t,\;{a}\sim\pi(\cdot\mid {s})}[{C}({s},{a})].
$$

Separately, let ${\mathcal{L}}({s},\pi)=\Pr_{{a}\sim\pi(\cdot\mid {s})}[{a}\ne\pi^*({s})]$. This disagreement loss is not necessarily the task cost or the token-level training loss.

#### Errors on Reference-Policy States

^errors-on-reference-policy-states

Write ${\epsilon}_t=\mathbb E_{{s}\sim {d_{\pi^*}}^t}[{\mathcal{L}}({s},\pi)]$ and ${\epsilon_E}={H}^{-1}\sum_t{\epsilon}_t$. Couple the two executions so they share environment randomness while their actions agree. Along a reference execution, draw hypothetical learner actions at each visited state. Until the first disagreement, these draws also describe the coupled learner.

By the union bound, the probability of at least one disagreement is at most $\sum_t{\epsilon}_t={H}{\epsilon_E}$. This argument needs no independence between disagreements. Before divergence, the coupled executions incur the same costs; afterward, their total cost difference is at most ${H}$. Therefore

$$
{J}(\pi)-{J}(\pi^*)\le {H}\Pr(\text{any disagreement}) \le \min\{{H},\;{H}^2{\epsilon_E}\}.
$$

This yields the expert-distribution bound of Ross et al. ([[05 Reference/Volume III - Agentic Systems/V3 Mathematical Foundations#^ref-ross2011reduction|2011]]), Theorem 2.1, with the additional trivial horizon cap. Marginal error bounds do not justify replacing the union bound by $1-(1-{\epsilon})^{H}$; that product requires further conditional-probability assumptions.

#### Errors on Learner-Policy States

^errors-on-learner-policy-states

Now let ${\epsilon_\pi}=\mathbb E_{{s}\sim {d_\pi}}[{\mathcal{L}}({s},\pi)]$. Define ${Q_t^{\pi^*}}({s},{a})$ as expected cost from step ${t}$ through ${H}$ after taking ${a}$ and then following $\pi^*$. Let

$$
{A_t^{\pi^*}}({s},{a})={Q_t^{\pi^*}}({s},{a})-{Q_t^{\pi^*}}({s},\pi^*({s})).
$$

Compare policies that switch from the learner to the reference after successively later steps. Their cost differences telescope, giving

$$
{J}(\pi)-{J}(\pi^*)= \sum_{t=1}^{H}\mathbb E_{{s}\sim {d_\pi}^t,\;{a}\sim\pi(\cdot\mid {s})} [{A_t^{\pi^*}}({s},{a})].
$$

Suppose ${A_t^{\pi^*}}({s},{a})\le {u}$ for every learner-reachable state and action, with ${u}\ge0$. The disadvantage is zero when the action agrees with the reference, so each expectation is at most ${u}$ times the corresponding disagreement probability. Thus

$$
{J}(\pi)-{J}(\pi^*)\le\min\{{H},\;{u} {H}{\epsilon_\pi}\},
$$

as in Theorem 2.2. Linear dependence on ${H}$ requires a horizon-independent ${u}$; in general, ${u}$ can grow with the remaining horizon. If the immediate cost itself is disagreement, the simpler identity ${J}(\pi)={H}{\epsilon_\pi}$ follows directly, but does not describe arbitrary task costs.

DAgger obtains reference labels at states visited during successive policy collections and aggregates the examples for supervised learning. Its guarantees also require the stated learning and sampling assumptions. Collecting such records alone neither proves a small population error for the released policy nor makes the distribution penalty vanish. The chapter uses these bounds to motivate coverage and evaluation, not to promise that a particular training method eliminates compounding errors.

## Coordination Models

^sec-vol3-appendix-math-coordination-models

More workers can shorten a task, and more reviewers can change an error probability. Both conclusions depend on the overhead and dependence models, not on agent count alone.

### Optimal Worker Count Under Amdahl’s Law with Coordination Overhead

^sec-vol3-appendix-math-amdahl

Adding parallel workers to a delegated task initially shortens elapsed time, but once handoff and reconciliation overhead grows faster than the parallel saving, each additional worker slows the trajectory down. **[[01 Books/Volume III - Agentic Systems/06 Agents at Scale/18 Multi-Agent Coordination/V3-18.03 The Delegation Trade-Off#^sec-vol3-multiagent-need|The Delegation Trade-Off]]** models the speedup of splitting work across ${N_{\text{workers}}}$ workers with a serial fraction and a coordination term (**[[01 Books/Volume III - Agentic Systems/06 Agents at Scale/18 Multi-Agent Coordination/V3-18.03 The Delegation Trade-Off#^eq-vol3-multiagent-speedup|equation 18.1]]**). To examine one possible scaling curve, suppose the normalized overhead is ${h}({N_{\text{workers}}})={\kappa_{\text{coh}}}({N_{\text{workers}}}-1)+{\beta_{\text{pair}}} {N_{\text{workers}}}({N_{\text{workers}}}-1)$. This assumption gives

$$
\text{Speedup}({N_{\text{workers}}}) = \frac{1}{{D}({N_{\text{workers}}})}, \qquad {D}({N_{\text{workers}}}) = (1 - {f_{\text{parallel}}}) + \frac{{f_{\text{parallel}}}}{{N_{\text{workers}}}} + {\kappa_{\text{coh}}} ({N_{\text{workers}}} - 1) + {\beta_{\text{pair}}} {N_{\text{workers}}} ({N_{\text{workers}}} - 1)
$$

where ${f_{\text{parallel}}} \in (0, 1]$ is the fraction of the fixed work that divides across workers. The nonnegative coefficients ${\kappa_{\text{coh}}}$ and ${\beta_{\text{pair}}}$, with ${\kappa_{\text{coh}}}+{\beta_{\text{pair}}}>0$, parameterize the assumed overhead. With ${\beta_{\text{pair}}}=0$ and ${f_{\text{parallel}}}=1-{\sigma_{\text{cont}}}$, $1/{D}$ is the universal scalability law of **[[01 Books/Volume III - Agentic Systems/06 Agents at Scale/18 Multi-Agent Coordination/V3-18.10 Benchmarking Against a Single Agent#^eq-vol3-multiagent-usl|equation 18.5]]**, so ${\kappa_{\text{coh}}}$ is its coherency coefficient. The term in ${\beta_{\text{pair}}}$ adds overhead that grows with the number of worker pairs. Their values are workload parameters, not universal properties of delegation. The physical domain is integer ${N_{\text{workers}}}\ge 1$; on this domain ${D}({N_{\text{workers}}})>0$ and ${D}(1)=1$. The following continuous relaxation identifies candidate worker counts to test.

Maximizing speedup on the physical domain means minimizing ${D}({N_{\text{workers}}})$. Extending the denominator to positive real ${N_{\text{workers}}}$ for differentiation gives

$$
\frac{d {D}}{d {N_{\text{workers}}}} = -\frac{{f_{\text{parallel}}}}{{N_{\text{workers}}}^2} + {\kappa_{\text{coh}}} + {\beta_{\text{pair}}} (2{N_{\text{workers}}} - 1)
$$

and setting the derivative to zero gives the stationary condition

$$
{P}({N_{\text{workers}}}) = 2{\beta_{\text{pair}}} {N_{\text{workers}}}^3 + ({\kappa_{\text{coh}}} - {\beta_{\text{pair}}}) {N_{\text{workers}}}^2 - {f_{\text{parallel}}} = 0
$$

1.  **Exactly one positive root.** The coefficients of ${P}({N_{\text{workers}}})$, in order, are $2{\beta_{\text{pair}}}$, ${\kappa_{\text{coh}}} - {\beta_{\text{pair}}}$, $0$, and $-{f_{\text{parallel}}}$. Whether ${\kappa_{\text{coh}}} - {\beta_{\text{pair}}}$ is positive or negative, the sequence of nonzero signs changes exactly once, so by Descartes’ rule of signs ${P}$ has exactly one positive real root ${N_{\text{workers}}}^*$. When ${\beta_{\text{pair}}} = 0$ the condition reduces to ${\kappa_{\text{coh}}} {N_{\text{workers}}}^2 = {f_{\text{parallel}}}$, so ${N_{\text{workers}}}^* = \sqrt{{f_{\text{parallel}}} / {\kappa_{\text{coh}}}}$, which with ${f_{\text{parallel}}}=1-{\sigma_{\text{cont}}}$ is the peak of **[[01 Books/Volume III - Agentic Systems/06 Agents at Scale/18 Multi-Agent Coordination/V3-18.10 Benchmarking Against a Single Agent#^eq-vol3-multiagent-usl-peak|equation 18.6]]**.
2.  **The denominator is strictly convex.** The second derivative,

$$
\frac{{d}^2 {D}}{d {N_{\text{workers}}}^2} = \frac{2{f_{\text{parallel}}}}{{N_{\text{workers}}}^3} + 2{\beta_{\text{pair}}},
$$

 is positive for every ${N_{\text{workers}}} > 0$, so ${N_{\text{workers}}}^*$ uniquely minimizes the extended denominator. If ${N_{\text{workers}}}^*<1$, the constrained minimum is at ${N_{\text{workers}}}=1$. Otherwise, evaluate the adjacent integers around ${N_{\text{workers}}}^*$, subject to available capacity. Maximizing the reciprocal outside the physical domain is unnecessary and need not be valid.

Under this assumed overhead, speedup eventually falls as concurrency grows. A split shortens modeled elapsed time only if ${D}({N_{\text{workers}}})<1$ at some feasible integer ${N_{\text{workers}}}>1$; that condition says nothing by itself about acceptance or cost. Fit any proposed overhead model to workload measurements, examine variation and fit error, and test its predictions at the contemplated worker counts. A stationary point is a scheduling hypothesis, not a deployment recommendation. **[[01 Books/Volume III - Agentic Systems/06 Agents at Scale/18 Multi-Agent Coordination/V3-18.10 Benchmarking Against a Single Agent#^sec-vol3-multiagent-evaluation|Benchmarking Against a Single Agent]]** makes the latter decision against the task’s objective and constraints.

### Correlated Failures in Multi-Agent Quorum Voting

^sec-vol3-appendix-math-correlated-quorum

When five model reviewers inspect the same subtly flawed patch, all five can approve it if the flaw exploits a blind spot shared across their prompts or training data. The voting example in **[[01 Books/Volume III - Agentic Systems/06 Agents at Scale/18 Multi-Agent Coordination/V3-18.07 Correlated Ensemble Failures#^sec-vol3-multiagent-consensus|Correlated Ensemble Failures]]** therefore models false approval of a candidate known to violate the assessed criterion, which is a different problem from a distributed consensus protocol choosing one value. To model the former, let ${X}_j=1$ indicate false approval by reviewer ${j}$, with an odd number ${N_{\text{workers}}}$ of reviewers. If these indicators are independent Bernoulli variables with common probability ${p}$, the majority false-approval probability is

$$
\Pr\left(\sum_{j=1}^{{N_{\text{workers}}}}{X}_j>\frac{{N_{\text{workers}}}}{2}\right) =\sum_{k=({N_{\text{workers}}}+1)/2}^{{N_{\text{workers}}}}\binom{{N_{\text{workers}}}}{{k}}{p}^{k}(1-{p})^{{N_{\text{workers}}}-{k}}.
$$

For ${p}<1/2$, this probability tends to zero as odd ${N_{\text{workers}}}$ increases. That conclusion depends on the stated joint model; knowing each reviewer’s marginal error rate is not enough.

A latent task propensity gives a different joint model. Let ${Q}$ denote the false-approval probability for a randomly selected candidate in the declared cohort, and assume ${X}_j\mid {Q}$ are independent Bernoulli variables with parameter ${Q}$. Conditional independence can describe separate samples at a fixed input even when the reviewers use identical weights. Across candidates with different propensities, however,

$$
\mathbb{E}[{X}_j]=\mathbb{E}[{Q}]={p},\qquad \operatorname{Cov}({X}_i,{X}_j)=\operatorname{Var}({Q})\quad ({i}\ne {j}).
$$

The covariance follows from conditional independence and the law of total covariance. Since each marginal indicator is Bernoulli with probability ${p}$, its variance is ${p}(1-{p})$. For $0<{p}<1$, the pairwise correlation is therefore

$$
{\rho}=\frac{\operatorname{Var}({Q})}{{p}(1-{p})}.
$$

This dependence arises from shared candidate difficulty in the model, not from an assertion that identical weights force dependent random draws at every fixed input. Communication between reviewers or other shared randomness would require an additional dependence model.

For the chapter’s illustrative beta mixture, assume ${Q}\sim\operatorname{Beta}({a},{b})$ with ${a},{b}>0$. Its mean and variance give

$$
{p}=\frac{{a}}{{a}+{b}},\qquad {\rho}=\frac{1}{{a}+{b}+1},\qquad {a}={p}\left(\frac{1}{{\rho}}-1\right),\qquad {b}=(1-{p})\left(\frac{1}{{\rho}}-1\right).
$$

The parameterization applies for $0<{p}<1$ and $0<{\rho}<1$. Independence is the limiting constant-propensity case, not a beta distribution with finite shape parameters and ${\rho}=0$. Define the beta function locally by

$$
\mathrm{B}({a},{b})=\int_0^1 {q}^{{a}-1}(1-{q})^{{b}-1}\,d{q}.
$$

Integrating the conditional binomial probability over ${Q}$ gives the beta-binomial distribution for the false-approval count ${N_{\text{fa}}}=\sum_j{X}_j$:

$$
\Pr({N_{\text{fa}}}={k})= \int_0^1 \binom{{N_{\text{workers}}}}{{k}}{q}^{k}(1-{q})^{{N_{\text{workers}}}-{k}} \frac{{q}^{{a}-1}(1-{q})^{{b}-1}}{\mathrm{B}({a},{b})}\,d{q} =\binom{{N_{\text{workers}}}}{{k}}\frac{\mathrm{B}({k}+{a},{N_{\text{workers}}}-{k}+{b})}{\mathrm{B}({a},{b})}.
$$

Summing over ${k}>{N_{\text{workers}}}/2$ yields the majority false-approval probability; the ${k}={N_{\text{workers}}}$ term gives unanimous false approval. These are consequences of the full mixture assumption. Other joint distributions can share the same ${p}$ and ${\rho}$ while producing different majority probabilities.

The asymptotic result also has a precise scope. Conditional on ${Q}={q}\ne1/2$, the sample fraction converges to ${q}$. The beta distribution has no point mass at $1/2$, so bounded convergence gives

$$
\lim_{\substack{{N_{\text{workers}}}\to\infty\\{N_{\text{workers}}}\ \text{odd}}} \Pr({N_{\text{fa}}}>{N_{\text{workers}}}/2)=\Pr({Q}>1/2) =\frac{1}{\mathrm{B}({a},{b})} \int_{1/2}^{1}{q}^{{a}-1}(1-{q})^{{b}-1}\,d{q}.
$$

In this model, adding reviewers cannot remove the cohort’s mass of candidates that most reviewers tend to approve incorrectly. The result is not a universal error floor for all model ensembles. Measure the actual review policy on the intended cohort, retain evidence about its errors, and keep runtime authorization and scoped acceptance checks distinct from the vote.

Back to top

## Source References

^source-references

Kaelbling, Leslie Pack, Michael L. Littman, and Anthony R. Cassandra. 1998. “Planning and Acting in Partially Observable Stochastic Domains.” *Artificial Intelligence* 101 (1–2): 99–134. https://doi.org/10.1016/S0004-3702(98)00023-X.

^ref-kaelbling1998

Willard, Brandon T., and Rémi Louf. 2023. “Efficient Guided Generation for Large Language Models.” *arXiv Preprint arXiv:2307.09702*.

^ref-willard2023outlines

Beyer, Kevin, Jonathan Goldstein, Raghu Ramakrishnan, and Uri Shaft. 1999. “When Is ‘Nearest Neighbor’ Meaningful?” *International Conference on Database Theory (ICDT)*, 217–35. https://doi.org/10.1007/3-540-49257-7_15.

^ref-beyer1999nearest

Young, John W. 1974. “A First Order Approximation to the Optimum Checkpoint Interval.” *Communications of the ACM* 17 (9): 530–31. https://doi.org/10.1145/361147.361115.

^ref-young1974

Daly, J. T. 2006. “A Higher Order Estimate of the Optimum Checkpoint Interval for Restart Dumps.” *Future Generation Computer Systems* 22 (3): 303–12. https://doi.org/10.1016/j.future.2004.11.016.

^ref-daly2006

Brant, Rollin. n.d. *Inference for Proportions: Comparing Two Independent Samples*. Power/sample size calculator, Department of Statistics, University of British Columbia.

^ref-brantProportionsCalculator

Newcombe, Robert G. 1998. “Improved Confidence Intervals for the Difference Between Binomial Proportions Based on Paired Data.” *Statistics in Medicine* 17 (22): 2635–50. https://doi.org/10.1002/(SICI)1097-0258(19981130)17:22\<2635::AID-SIM954\>3.0.CO;2-C.

^ref-newcombe1998improved

Efron, Bradley, and Robert J. Tibshirani. 1994. *An Introduction to the Bootstrap*. Routledge. https://doi.org/10.1201/9780429246593.

^ref-efron1994bootstrap

The SciPy community. n.d. *Scipy.stats.bootstrap*. SciPy documentation.

^ref-scipyBootstrap

Chen, Mark, Jerry Tworek, Heewoo Jun, Qiming Yuan, Henrique Ponde de Oliveira Pinto, Jared Kaplan, Harri Edwards, et al. 2021. “Evaluating Large Language Models Trained on Code.” *arXiv Preprint arXiv:2107.03374*.

^ref-chen2021evaluating

Wald, Abraham. 1945. “Sequential Tests of Statistical Hypotheses.” *The Annals of Mathematical Statistics* 16 (2): 117–86. https://doi.org/10.1214/aoms/1177731118.

^ref-wald1945sequential

Fischer, Lasse, and Aaditya Ramdas. 2026. “Improving Wald’s (Approximate) Sequential Probability Ratio Test by Avoiding Overshoot.” *IEEE Transactions on Information Theory* 72 (4): 2457–71. https://doi.org/10.1109/TIT.2026.3658855.

^ref-fischer2026improving

Hory, Cyril, and Alfred O. Hero. 2004. *Sequential Probability Ratio Test for the Detection of a Single Electron Spin in the OSCAR Setup*. arXiv preprint quant-ph/0402181.

^ref-hory2004sequential

Schulman, John, Philipp Moritz, Sergey Levine, Michael I. Jordan, and Pieter Abbeel. 2016. “High-Dimensional Continuous Control Using Generalized Advantage Estimation.” *International Conference on Learning Representations (ICLR)*.

^ref-schulman2016high

Ross, Stéphane, Geoffrey Gordon, and J. Andrew Bagnell. 2011. “A Reduction of Imitation Learning and Structured Prediction to No-Regret Online Learning.” *Proceedings of the Fourteenth International Conference on Artificial Intelligence and Statistics (AISTATS)* 15: 627–35.

^ref-ross2011reduction

## Source

[Repository Source](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/books/vol3/backmatter/appendix_math.qmd) · [Original License](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/LICENSE.md)

[Rendered Reading Snapshot](https://mlsysbook.ai/vol3/backmatter/appendix_math.html#sec-vol3-appendix-math). Rendering provenance is recorded in the import manifest.
