---
title: V2 Inference Foundations
type: Reference
volume: 2
chapter: 0
publication_status: Preview
source_repository: https://github.com/klappe-pm/cs249r_book
source_commit: de87c0103806d7bfb1c677dbb77a2b92fa00c298
source_path: books/vol2/backmatter/appendix_inference.qmd
source_anchor: sec-appdx-appendix-inference
source_mode: Source-Correlated Published HTML
tags:
- Type/Reference
- Book/Volume_2
rendered_source_url: https://mlsysbook.ai/vol2/backmatter/appendix_inference.html
---

# V2 Inference Foundations

[[Home|Home]] · [[01 Books/Volume II - Scaling/Volume 2 Overview|Volume Overview]]

^sec-appdx-appendix-inference

Serving a model at scale is governed by the mathematics of waiting lines and the physics of the key-value cache. This appendix develops the analytical serving models that the book’s inference and operations chapters draw on, establishing how queuing dynamics and attention-cache memory arithmetic combine into a single serving constraint under strict latency service-level objectives (SLOs). In C$^3$ terms, inference turns compute capacity, communication with memory and clients, and coordination across queues into one serving constraint.

## How to Use This Appendix

^how-to-use-this-appendix

This appendix is a quantitative reference for serving systems. Use the queuing surrogate to screen batch sizes and estimate mean delay under its stated assumptions, then validate tail latency with measurements or simulation. Use the key-value cache arithmetic to size memory or to determine when the cache, rather than compute, caps throughput.

- **When a serving tier misses its latency target under load**: Use the queuing model in [[05 Reference/Volume II - Scaling/V2 Inference Foundations#^sec-appdx-inference-scale-queuing-theory-batched-inference-bbf0|section 1.1.1]] to separate waiting, batch-formation, and service time.
- **When choosing a batch size**: Use the worked example in [[05 Reference/Volume II - Scaling/V2 Inference Foundations#^sec-appdx-inference-scale-worked-example-gpt3-serving-100-qps-edcf|section 1.1.1.4]] and the decision framework in [[05 Reference/Volume II - Scaling/V2 Inference Foundations#^sec-appdx-inference-scale-decision-framework-batch-size-selection-given-sla-8e4e|section 1.1.1.5]].
- **When memory, not compute, caps concurrency**: Use the KV-cache sizing in [[05 Reference/Volume II - Scaling/V2 Inference Foundations#^sec-appdx-inference-scale-kv-cache-fundamentals-2ccd|section 1.1.2]].

## Serving Performance Analysis

^sec-appdx-appendix-inference-serving

When a GPT-3 serving replica receives a burst of 100 queries per second, an aggressive batch size can saturate high-bandwidth memory with key-value states while a conservative batch size causes the arrival queue to grow without bound. Serving performance analysis therefore has two coupled layers. The queue determines how requests wait, batch, and shed under stochastic arrivals; the key-value cache determines how much live state the accelerator can hold while meeting the latency budget. Because a batch cannot execute until it both clears the arrival queue and fits in device memory, sizing a serving replica requires solving the queuing delay curve first and then bounding candidate batch sizes against key-value cache capacity.

### Queuing Theory for Batched Inference

^sec-appdx-inference-scale-queuing-theory-batched-inference-bbf0

Processing requests one at a time leaves GPU tensor cores starved for work, yet waiting to accumulate a batch of 64 requests adds tens of milliseconds of collection delay before the first kernel even launches. Batching trades waiting time for throughput, and production systems require quantitative analysis to choose batch sizes under stochastic arrival patterns. Queuing theory provides the mathematical framework to derive these operating points and to explain why certain batch sizes outperform others under specific load conditions.

#### Queuing Notation and the M/G/1 Batch Surrogate

^sec-appdx-inference-scale-mgck-queue-model-gpu-serving-c4c4

The **M/G/c/K notation** names four characteristics that a production GPU-serving model may need to represent. Together, these four fields specify the arrival process, the service-time distribution, the server count, and the queue capacity:

- **M (Markov arrivals)**: Requests arrive according to a Poisson process with rate ${\lambda_{\text{arr}}}$. This models the memoryless property of user requests, where arrival of one request does not predict the timing of the next.
- **G (General service distribution)**: Service times follow a general distribution, not restricted to exponential. GPU inference times depend on batch size and show deterministic components (compute) mixed with stochastic variation (memory contention, kernel scheduling).
- **c (Number of servers)**: The system has ${c}$ parallel GPU workers, each capable of serving requests independently.
- **K (System capacity)**: At most ${K}$ requests may be present, including those in service. Requests arriving to a full system are rejected (load shedding).

The notation comes from the same systems-performance lineage that sized telephone networks before it was applied to GPU clusters. Its parameters map directly onto the arrival, execution, and admission controls of an inference server.

**Systems Perspective 1.1: Queuing theory and performance**

Queuing theory, developed by Agner Krarup Erlang in 1909 for telephone network analysis, remains foundational to systems performance engineering ([[05 Reference/Volume II - Scaling/V2 Inference Foundations#^ref-erlang1909telephone|Erlang 1909]]). The same mathematical framework that sized telephone exchanges now informs GPU cluster capacity. Standard systems texts develop the component queuing models and approximations on which this notation builds ([[05 Reference/Volume II - Scaling/V2 Inference Foundations#^ref-jain1991art|Jain 1991]]; [[05 Reference/Volume II - Scaling/V2 Inference Foundations#^ref-kleinrock1975queueing|Kleinrock 1975]]).

For a batched inference system with batch size ${B}$, service time becomes a function of batch size. Let ${T_{\text{svc}}}({B})$ denote the time to process a batch of ${B}$ requests. From the physics of batching (**[[01 Books/Volume II - Scaling/03 The Fleet in Production/10 Serving at Scale/V2-10.07 Batching Strategies at Scale#^sec-inference-scale-batching-strategies-scale-6733|Batching Strategies at Scale]]**), [[05 Reference/Volume II - Scaling/V2 Inference Foundations#^eq-service-time-batch|equation 1]] models this as:

$$
{T_{\text{svc}}}({B}) = {T_{\text{fixed}}}+ {t_{\text{req}}}\cdot {B} \tag{1}
$$

^eq-service-time-batch

where ${T_{\text{fixed}}}$ represents fixed service overhead (kernel launch, weight loading from high-bandwidth memory (HBM)) and ${t_{\text{req}}}$ represents marginal per-request computation time. This linear model captures the first-order behavior observed in production systems, though actual service times may show slight sublinearity due to memory bandwidth saturation at large batch sizes.

The **effective service rate** for batched processing divides the batch size by the batch execution time. That ratio determines the maximum sustained request throughput at a given batch size:

$$
{\mu_{\text{eff}}}({B}) = \frac{{B}}{{T_{\text{svc}}}({B})} = \frac{{B}}{{T_{\text{fixed}}}+ {t_{\text{req}}}\cdot {B}}
$$

The effective rate increases with batch size, approaching the asymptotic limit $1/{t_{\text{req}}}$ as ${B}\to \infty$. Once fixed launch and weight-loading overheads are amortized, marginal per-request work sets the throughput ceiling.

#### Response Time Analysis

^sec-appdx-inference-scale-response-time-analysis-ffc3

Amortizing fixed launch and weight-loading overhead raises server throughput, but a client experiences end-to-end latency rather than kernel throughput alone. Before a request ever executes on the accelerator, it must wait for prior batches to clear and pause in the staging buffer while peer requests arrive to complete its own batch, splitting total response time ${t}$ into three sequential components:

$$
\mathbb{E}[{t}] = \mathbb{E}[{W_{q}}] + \mathbb{E}[{L_{\text{lat,form}}}] + \mathbb{E}[{T_{\text{svc}}}]
$$

where:

- $\mathbb{E}[{W_{q}}]$ is the expected waiting time in queue before joining a batch
- $\mathbb{E}[{L_{\text{lat,form}}}]$ is the expected per-request batch-accumulation delay before dispatch
- $\mathbb{E}[{T_{\text{svc}}}]$ is the expected inference time once the batch executes

For dynamic batching with maximum wait time ${T_{\text{window}}}$ and maximum batch size ${B_{\text{max}}}$, the first request triggers the batching window. Let ${Q_{\text{arr}}}\sim \operatorname{Poisson}({\lambda_{\text{arr}}}{}{T_{\text{window}}})$ count subsequent arrivals during that window and let ${k}={B_{\text{max}}}-1$. For ${B_{\text{max}}}>1$, the realized batch size is ${B}=\min({B_{\text{max}}},1+{Q_{\text{arr}}})$, including the trigger request, so:

$$
\mathbb{E}[{B}] = \sum_{n=0}^{{k}-1}({n}+1)\Pr({Q_{\text{arr}}}={n}) + {B_{\text{max}}}\Pr({Q_{\text{arr}}}\geq {k})
$$

Let ${\tau}_k$ be the Erlang-distributed time of the ${k}$th subsequent arrival. A full batch closes when ${\tau}_k \leq {T_{\text{window}}}$, while a timeout batch closes at ${T_{\text{window}}}$ with ${Q_{\text{arr}}}={n}<{k}$. The mean per-request accumulation delay within each realized batch is:

$$
\mathbb{E}[{L_{\text{lat,form}}} \mid \text{full}] = \frac{1}{2}\mathbb{E}[{\tau}_k \mid {\tau}_k \leq {T_{\text{window}}}]
$$

$$
\mathbb{E}[{L_{\text{lat,form}}} \mid {Q_{\text{arr}}}={n},\ \text{timeout}] = \frac{{T_{\text{window}}}}{2}\left(1+\frac{1}{{n}+1}\right), \qquad 0 \leq {n}< {k}
$$

Weighting each batch outcome by its realized request count gives the mean delay of a randomly selected request. This weighted average accounts for the fact that larger batches contain a proportionally larger share of the arriving queries:

$$
\mathbb{E}[{L_{\text{lat,form}}}] = \frac{{B_{\text{max}}}\Pr({Q_{\text{arr}}}\geq {k})\mathbb{E}[{\tau}_k/2 \mid {\tau}_k\leq {T_{\text{window}}}] + \sum_{n=0}^{{k}-1}({n}+1)\Pr({Q_{\text{arr}}}={n})\mathbb{E}[{L_{\text{lat,form}}} \mid {Q_{\text{arr}}}={n},\ \text{timeout}]}{\mathbb{E}[{B}]}
$$

When batches reliably fill before timeout, this expression approaches $\mathbb{E}[{\tau}_k]/2=({B_{\text{max}}}-1)/(2{\lambda_{\text{arr}}})$. For ${B_{\text{max}}}=1$, the batch contains only its trigger request and accumulation delay is zero.

#### Optimal Batch Size Derivation

^sec-appdx-inference-scale-optimal-batch-size-derivation-3a3c

Increasing the batch size ${B}$ pulls the three latency components in opposite directions: a larger batch raises the effective service rate and drains the arrival queue faster, yet it forces every request to wait longer during batch formation and adds ${t_{\text{req}}}$ per additional request during execution. The optimal batch size ${B}$ minimizes expected response time across those competing terms subject to throughput stability:

$$
{B}= \operatorname{arg\,min}_{{B}} \mathbb{E}[{t}({B})] \quad \text{subject to} \quad {\mu_{\text{eff}}}({B}) > {\lambda_{\text{arr}}}
$$

The constraint ensures system stability so that the effective service rate strictly exceeds the arrival rate. Without that margin, the arrival queue grows without bound under stochastic traffic bursts.

For a high-traffic regime in which batches of size ${B}$ reliably fill before timeout, substituting the response time components gives a closed-form objective. Each term in the sum responds differently as ${B}$ increases:

$$
\mathbb{E}[{t}({B})] = \mathbb{E}[{W_{q}}({B})] + \frac{{B}-1}{2{\lambda_{\text{arr}}}} + {T_{\text{svc}}}({B})
$$

For a tractable waiting-time estimate, use an M/G/1 surrogate that treats batches as Poisson “super-requests.” If the request arrival rate is ${\lambda_{\text{arr}}}$ and the average batch size is ${B}$, this surrogate uses batch arrival rate ${\lambda_{\text{batch}}}={\lambda_{\text{arr}}}/{B}$. This is not the exact process produced by grouping Poisson request arrivals, because fixed-size grouping yields Erlang inter-batch times; finite ${K}$ or ${c}>1$ requires a bulk-service model or simulation. Within the explicit surrogate, the Pollaczek-Khinchine formula gives:

$$
\mathbb{E}[{W_{q}}] = \frac{{\lambda_{\text{batch}}}\cdot \mathbb{E}[{T_{\text{svc}}}^2]}{2(1 - {\rho_{\text{serv}}})}
$$

where ${\rho_{\text{serv}}} = {\lambda_{\text{batch}}}\cdot \mathbb{E}[{T_{\text{svc}}}] = {\lambda_{\text{arr}}} \cdot \mathbb{E}[{T_{\text{svc}}}]/{B}$ is the server utilization. The second moment $\mathbb{E}[{T_{\text{svc}}}^2]$ captures service time variability.

For the linear service time model with deterministic service in this surrogate, the second moment simplifies to ${T_{\text{svc}}}({B})^2$. Substituting that deterministic service time into the Pollaczek-Khinchine relation gives the explicit waiting-time curve:

$$
\mathbb{E}[{W_{q}}({B})] = \frac{{\lambda_{\text{arr}}} \cdot {T_{\text{svc}}}({B})^2}{2{B}(1 - {\lambda_{\text{arr}}} \cdot {T_{\text{svc}}}({B})/{B})}
$$

For production sizing, teams often first enforce a utilization headroom target rather than solving the full latency minimization problem. With ${T_{\text{svc}}}({B})={T_{\text{fixed}}}+{t_{\text{req}}} {B}$, the constraint ${\rho_{\text{serv}}}={\lambda_{\text{arr}}} {T_{\text{svc}}}({B})/{B}\leq {\rho_{\text{target}}}$ yields the target-utilization batch bound ([[05 Reference/Volume II - Scaling/V2 Inference Foundations#^eq-optimal-batch-approx|equation 2]]):

$$
{B_{\text{util}}}({\rho_{\text{target}}}) = \frac{{\lambda_{\text{arr}}} {T_{\text{fixed}}}}{{\rho_{\text{target}}}- {\lambda_{\text{arr}}} {t_{\text{req}}}} \tag{2}
$$

^eq-optimal-batch-approx

where ${\rho_{\text{target}}}$ is the target utilization (typically 0.7–0.8 for production systems to maintain latency headroom) and ${\rho_{\text{target}}}> {\lambda_{\text{arr}}} {t_{\text{req}}}$.

**Systems Perspective 1.2: Target-utilization batch sizing**

The target-utilization batch bound ([[05 Reference/Volume II - Scaling/V2 Inference Foundations#^eq-optimal-batch-approx|equation 2]]) shows that the minimum utilization-feasible batch size grows with fixed overhead and arrival rate, through three dependencies:

1.  **Higher traffic** $({\lambda_{\text{arr}}})$: Required batch size increases.
2.  **Higher fixed overhead** $({T_{\text{fixed}}})$: Required batch size increases to amortize overhead.
3.  **Higher target utilization** $({\rho_{\text{target}}})$: Required batch size decreases, but with less latency headroom.

This utilization-constrained sizing explains why large language models (LLMs) (high ${T_{\text{fixed}}}$ from weight loading) benefit from larger batches than vision models (low ${T_{\text{fixed}}}$), even at the same arrival rate.

#### GPT-3 Serving at 100 QPS

^sec-appdx-inference-scale-worked-example-gpt3-serving-100-qps-edcf

Consider a hypothetical prefill-stage sizing exercise for a GPT-3 class model (175B parameters). The following assumed service-time coefficients illustrate the queuing calculation; they are not a measured GPT-3 benchmark:

- Arrival rate: ${\lambda_{\text{arr}}} =$ 100 requests/second
- Hardware: 8$\times$ A100 GPUs (one DGX A100 node) with tensor parallelism
- Fixed prefill-stage service overhead: ${T_{\text{fixed}}}=$ 50 ms
- Marginal prefill-stage service time: ${t_{\text{req}}}=$ 0.5 ms per request
- Target utilization: ${\rho_{\text{target}}}=$ 0.75

For the prefill phase (processing the input prompt), service time follows the linear batch model of [[05 Reference/Volume II - Scaling/V2 Inference Foundations#^eq-service-time-batch|equation 1]]. Substituting the fixed 50 ms overhead and 0.5 ms marginal cost gives the per-batch execution time:

$$
{T_{\text{svc}}}({B}) = 50 + 0.5 \cdot {B} \text{ ms}
$$

Applying [[05 Reference/Volume II - Scaling/V2 Inference Foundations#^eq-optimal-batch-approx|equation 2]] yields the minimum batch size that meets the 75 percent target utilization while leaving 25 percent headroom. The numerator captures the fixed overhead rate and the denominator captures the available utilization margin:

$$
{B_{\text{util}}} \approx \frac{100 \times 0.05}{0.75 - 100 \times 0.0005} = \frac{5}{0.70} \approx 7.14
$$

Rounding up gives ${B}=$ 8 as the smallest batch size that meets the target utilization headroom. Evaluating the surrogate response-time expression under the full-batch assumption then shows how larger batches reduce utilization and queuing delay but add batch-accumulation delay ([[05 Reference/Volume II - Scaling/V2 Inference Foundations#^tbl-batch-size-comparison|table 1]]).

| **Size ${B}$** | **${T_{\text{svc}}}({B})$ (ms)** | **req/s** | **${\rho_{\text{serv}}}$** | **$\mathbb{E}[{W_{q}}]$ (ms)** | **$({B}-1)/(2{\lambda_{\text{arr}}})$ (ms)** | **$\mathbb{E}[{t}]$ (ms)** |
|:---------------|:--------------------------------:|:---------:|:--------------------------:|:------------------------------:|:--------------------------------------------:|:--------------------------:|
| **1**          |               50.5               |   19.8    |      505% (unstable)       |            $\infty$            |                      0                       |          $\infty$          |
| **4**          |                52                |   76.9    |      130% (unstable)       |            $\infty$            |                      15                      |          $\infty$          |
| **8**          |                54                |   148.1   |           67.5%            |              56.1              |                      35                      |           145.1            |
| **16**         |                58                |   275.9   |           36.3%            |              16.5              |                      75                      |           149.5            |
| **32**         |                66                |   484.8   |           20.6%            |              8.6               |                     155                      |           229.6            |

Table 1: **Batch Size Impact on GPT-3 Serving Performance**: Batch sizes of 5 or fewer cannot sustain 100 QPS (utilization exceeds 100 percent); ${B}=$ 6 is the smallest stable batch and ${B}=$ 8 the smallest that meets the 75 percent utilization target. Among the tabulated sizes, ${B}=$ 8 has the lowest mean latency, and evaluating every integer batch size places the minimum of this model near ${B}=$ 10. ${B}=$ 16 has similar mean latency with lower utilization, while ${B}=32$ leaves more headroom but pays a large accumulation-delay penalty.

^tbl-batch-size-comparison

Four operational regimes emerge across these batch sizes:

1.  **Unstable regime (batch sizes 1 to 5)**: Utilization exceeds 100 percent, so the system cannot keep up with arrivals and queues grow without bound. The stability boundary of [[05 Reference/Volume II - Scaling/V2 Inference Foundations#^eq-stability-threshold|equation 3]], ${B_{\text{min}}}\approx$ 5.3, falls inside this range.
2.  **Utilization-target threshold (batch size 8)**: At 67.5 percent utilization, the system meets the 75 percent target, but queuing delay still contributes substantially to latency (56.1 ms). The steep occupancy trajectory charted in [[05 Reference/Volume II - Scaling/V2 Inference Foundations#^fig-queuing-hockey-stick|figure 1]] isolates why. Batch sizes between the stability boundary and this threshold push utilization past the ${\rho_{\text{serv}}} \approx 0.80$ hockey-stick knee into the caution band, where queuing delay surges nonlinearly as the curve approaches saturation.
3.  **Latency knee (batch sizes 8 to 16)**: Mean latency is lowest in this range, with the model’s minimum near ${B}=$ 10. Batch size 16 trades a few milliseconds of additional total latency for lower utilization and queue wait time (16.5 ms vs. 56.1 ms), while ${B}=$ 32 leaves still more utilization headroom but pays too much batch-accumulation delay.
4.  **Diminishing returns (batch sizes beyond 32)**: Further batch size increases reduce utilization in this surrogate but increase accumulation delay. The separate KV-cache example below supplies a decode-memory bound; it is not part of this prefill-time calculation.

![[90 Assets/Volume II/Shared Figures/Cell 5 Output 1 e37aeca11c.png]]

Figure 1: **The Queuing Hockey Stick**: For an M/M/1 queue, ${\rho_{\text{serv}}}/(1-{\rho_{\text{serv}}})$ is the expected number of requests in the system, including the request in service. Its hyperbolic rise near saturation explains why production systems retain utilization headroom; the shaded operating bands are illustrative rather than universal thresholds.

^fig-queuing-hockey-stick

Applying Little’s Law provides an internal consistency check for these results. Because ${Q_{\text{req}}} = {\lambda_{\text{arr}}} \cdot {T_{\text{lat}}}$ holds regardless of the arrival or service distribution, multiplying the arrival rate by the decomposed latency must recover the sum of requests in service and waiting in the queue.

**Napkin Math 1.1: Applying Little's Law to verify**

**Verification**: By Little’s Law ([[05 Reference/Volume II - Scaling/V2 Inference Foundations#^ref-little1961|Little 1961]]), ${Q_{\text{req}}} = {\lambda_{\text{arr}}} \cdot {T_{\text{lat}}}$:

At ${B}=$ 16 with ${\lambda_{\text{arr}}} =$ 100 req/s and $\mathbb{E}[{t}] =$ 149.5 ms:

${Q_{\text{req}}} =$ 100 $\times$ 0.1495 s = 14.95 requests in system

With batch size 16 and utilization 36.3 percent:

- Expected requests in service: 16 $\times$ 0.363 = 5.8
- Expected requests in queue: 14.95 - 5.8 = 9.15

This matches the response-time decomposition: roughly 6 requests are in service and roughly 9 are waiting or accumulating into batches on average.

#### Batch Size Selection Framework Given an SLO

^sec-appdx-inference-scale-decision-framework-batch-size-selection-given-sla-8e4e

The 100 QPS analysis screened candidate batches by mean response time $\mathbb{E}[{t}]$, but production serving contracts enforce tail latency percentiles (for example, p99 latency \< 200 ms) rather than averages. Selecting a production batch size under a tail-latency SLO follows a five-step procedure:

##### Step 1 Characterize Service Time

^step-1-characterize-service-time

Measure ${T_{\text{fixed}}}$ and ${t_{\text{req}}}$ empirically by profiling inference at batch sizes 1, 8, and 32. Fit the linear model ${T_{\text{svc}}}({B}) = {T_{\text{fixed}}}+ {t_{\text{req}}} {B}$.

##### Step 2 Compute Stability Threshold

^step-2-compute-stability-threshold

Find the minimum batch size ${B_{\text{min}}}$ such that ${\mu_{\text{eff}}}({B_{\text{min}}}) > {\lambda_{\text{arr}}}$. Substituting the linear service-time model into ${B} / {T_{\text{svc}}}({B}) = {\lambda_{\text{arr}}}$ yields the stability boundary:

$$
{B_{\text{min}}}= \frac{{T_{\text{fixed}}}{\lambda_{\text{arr}}}}{1 - {t_{\text{req}}}{\lambda_{\text{arr}}}} \tag{3}
$$

^eq-stability-threshold

Choose an integer batch size strictly above this boundary, assuming ${\lambda_{\text{arr}}}{}{t_{\text{req}}}<1$. Equality leaves no stability margin; if the denominator is nonpositive, batching alone cannot sustain the arrival rate.

##### Step 3 Compute Latency at Candidate Batch Sizes

^step-3-compute-latency-at-candidate-batch-sizes

Under the same Poisson-super-request surrogate and full-batch assumption, evaluate the expected response time across the candidate grid ${B}\in \{{B_{\text{min}}}, 2{B_{\text{min}}}, ..., {B_{\text{max}}}\}$. Summing the queuing, batch-accumulation, and execution terms gives the total expected latency:

$$
\mathbb{E}[{t}({B})] = \frac{{\lambda_{\text{arr}}} \cdot {T_{\text{svc}}}({B})^2}{2{B}(1 - {\lambda_{\text{arr}}} {T_{\text{svc}}}({B})/{B})} + \frac{{B}-1}{2{\lambda_{\text{arr}}}} + {T_{\text{svc}}}({B})
$$

##### Step 4 Account for Tail Latency

^step-4-account-for-tail-latency

If measured response times are approximately Gaussian, their p99 can be estimated from the mean and standard deviation. Adding 2.33 standard deviations captures the 99th percentile of a normal distribution:

$$
{T_{\text{lat},\text{p99}}} \approx \mathbb{E}[{t}] + 2.33 \cdot {\sigma_t}
$$

where ${\sigma_t}$ is the standard deviation of response time. This Gaussian rule is not a general heavy-traffic approximation because queuing response times are commonly skewed. For exponential response times, p99 is $-\ln(0.01)\mathbb{E}[{t}] \approx 4.6 \cdot \mathbb{E}[{t}]$; use measured percentiles for production sizing.

##### Step 5 Select Optimal Batch Size

^step-5-select-optimal-batch-size

When the objective is maximum throughput under the increasing service-rate model, choose the largest stable, memory-feasible integer batch size whose p99 latency meets the SLO. Writing that constraint as an optimization problem over the candidate grid gives:

$$
{B}= \max\{{B}: {T_{\text{lat},\text{p99}}}({B}) \leq \text{SLO}\}
$$

Operating rules for batch size selection ([[05 Reference/Volume II - Scaling/V2 Inference Foundations#^tbl-batch-decision-framework|table 2]]) balance stability, latency SLOs, and cost efficiency. These rules generate candidate configurations, and load tests must then verify their latency, capacity, and cost under the actual request distribution:

| **Condition**                              | **Recommended action**                         |       **Rationale**       |
|:-------------------------------------------|:-----------------------------------------------|:-------------------------:|
| ${B}< {B_{\text{min}}}$                    | Increase batch size or add replicas            |    System is unstable     |
| ${T_{\text{lat},\text{p99}}} > \text{SLO}$ | Re-evaluate stable batch sizes or add replicas |  Latency exceeds target   |
| ${\rho_{\text{serv}}} < 0.5$               | Consider reducing replicas to save cost        | System is overprovisioned |
| ${\rho_{\text{serv}}} > 0.85$              | Add replicas for headroom                      |  Approaching instability  |

Table 2: **Batch Size Decision Framework**: Systematic approach to selecting batch size based on stability, latency SLO, and utilization targets.

^tbl-batch-decision-framework

#### Trade-Off Curves for Visualizing the Operating Region

^sec-appdx-inference-scale-tradeoff-curves-visualizing-operating-region-9f95

Batch execution sets two pressures against each other. As batch size ${B}$ grows from 1 to 128, throughput climbs with diminishing returns as fixed overheads are amortized. Batch service time expands steadily, so a latency budget caps how much of the throughput gain a server can take ([[05 Reference/Volume II - Scaling/V2 Inference Foundations#^fig-batch-tradeoff-curves|figure 2]]).

![[90 Assets/Volume II/Shared Figures/Cell 7 Output 1 42a03c2254.png]]

Figure 2: **Batch Size Trade-Off Curves**: Dimensionless schematic with batch service time t(B) = 1 + 0.15(B − 1) and throughput B/t(B), each normalized to its batch-1 value. Larger batches amortize fixed work but take longer to complete. These hypothetical curves are not a benchmark, exclude queuing and batch-formation delay, and establish neither a memory-capacity boundary nor an optimal batch size.

^fig-batch-tradeoff-curves

Four properties of these curves guide the choice of batch size across candidate operating points. Together they explain why throughput and latency cannot be optimized independently:

1.  **Pareto Frontier**: An operating point is Pareto efficient when no other candidate provides at least as much throughput and no more latency, with a strict improvement in at least one objective. The frontier is the set of these nondominated points.
2.  **Knee of the Curve**: A knee marks diminishing throughput gains relative to increasing service time; it does not by itself select the best operating point.
3.  **SLO-Constrained Optimum**: The best feasible batch size depends on the optimization objective and measured end-to-end latency, including queuing and batch formation. An SLO boundary can constrain that choice without guaranteeing an intersection or a unique optimum.
4.  **Diminishing Returns**: In the schematic, fixed work becomes a smaller fraction of each batch, so successive batch-size increases yield smaller throughput gains.

The queuing-theoretic framework provides the mathematical foundation for the batching strategies introduced in **[[01 Books/Volume II - Scaling/03 The Fleet in Production/10 Serving at Scale/V2-10.07 Batching Strategies at Scale#^sec-inference-scale-batching-strategies-scale-6733|Batching Strategies at Scale]]**. Where intuition might suggest “larger batches are better for throughput,” stability constraints, latency targets, and diminishing returns create a well-defined optimal operating region that varies by model type and deployment requirements. For autoregressive transformers, any candidate batch inside that queuing-feasible region must also fit its live attention state into accelerator memory.

### KV Cache Fundamentals

^sec-appdx-inference-scale-kv-cache-fundamentals-2ccd

During a single 2,048-token GPT-3 generation request, the key and value vectors accumulated across all 96 layers consume roughly 9.4 GB of high-bandwidth memory. A batch of 32 concurrent requests therefore exhausts the remaining memory of an eight-GPU A100 node before compute ever saturates. **[[01 Books/Volume II - Scaling/03 The Fleet in Production/10 Serving at Scale/V2-10.08 Memory and Decode-Time Management#^sec-inference-scale-kv-cache-management-04ed|Memory and Decode-Time Management]]** defines the KV cache and the paged allocation that manages it, and **[[05 Reference/Volume II - Scaling/V2 Single-Machine Foundations#^sec-appdx-dam-taxonomy-transformer-arithmetic|Transformer Arithmetic]]** gives its per-token size. Sizing a serving node around those per-token states requires accounting for three coupled effects: how caching trades quadratic recomputation for linear memory growth, how the resulting footprint scales with sequence length and batch size, and why naive contiguous reservation fragments HBM ([[05 Reference/Volume II - Scaling/V2 Inference Foundations#^ref-kwon2023|Kwon et al. 2023]]).

For a standard attention implementation at fixed model width, autoregressive generation without caching requires $\mathcal{O}({S}^2)$ computation per token because each transformer layer recomputes the full prefix, including attention among its tokens. The KV cache stores previously computed key and value vectors, allowing each new token to attend to the prefix in $\mathcal{O}({S})$ computation. For serving at scale, this compute saving creates a memory-management challenge, because KV cache memory can exceed model weights for long contexts. The cache size grows linearly with both sequence length and batch size as calculated by [[05 Reference/Volume II - Scaling/V2 Inference Foundations#^eq-kv-cache-size|equation 4]]:

$$
{M_{\text{KV}}} = 2 \times {N_L} \times {d}\times {S}\times {B}\times {s_{\text{elem}}} \tag{4}
$$

^eq-kv-cache-size

For standard multihead attention, where the aggregate KV width equals the hidden width, ${N_L}$ is the number of layers, ${d}$ is the hidden dimension, ${S}$ is sequence length, ${B}$ is batch size, ${s_{\text{elem}}}$ is storage size per element in bytes. The factor of 2 accounts for both keys and values. Grouped-query or multiquery attention instead uses the aggregate KV-head width in place of ${d}$.

Evaluating [[05 Reference/Volume II - Scaling/V2 Inference Foundations#^eq-kv-cache-size|equation 4]] for a concrete multi-GPU node shows how quickly the KV cache bounds concurrency. For the 175B GPT-3 model (${N_L} =$ 96, ${d}=$ 12,288, FP16 ${s_{\text{elem}}} =$ 2 bytes) at its training context length ${S}=$ 2,048, each request requires:

$$
M_{\text{KV/req}} = 2 \times 96 \times 12288 \times 2048 \times 2 \text{ B} \approx 9.66 \text{ GB/request}
$$

Across 8$\times$ A100 80-GB GPUs (687.2 GB total HBM), storing model weights in FP16 consumes 350 GB, leaving 337.2 GB for activation and KV cache memory. Dividing that residual capacity by the per-request cache gives a capacity-only upper bound of 34 concurrent requests. This bound assumes balanced sharding and reserves no memory for activations, workspaces, runtime state, or allocator losses; an implementable batch must be smaller (device nameplate capacities are converted to decimal GB before subtracting the decimal model footprint). Together with [[05 Reference/Volume II - Scaling/V2 Inference Foundations#^tbl-batch-size-comparison|table 1]], this capacity ceiling closes the two-layer serving model: queuing dynamics set the minimum batch size needed for stability and latency headroom, while HBM capacity caps the maximum concurrent batch at long context lengths.

## Summary

^summary

Serving performance is bounded by queues and by memory. As utilization ${\rho_{\text{serv}}}$ approaches 1, queue depth and latency grow without bound, so production systems retain headroom suited to their workload and SLO. Larger batches raise throughput but add batch-accumulation delay, which produces a latency knee rather than monotonic improvement; the best batch size depends on whether the objective is minimum mean latency, maximum SLO-compliant throughput, or cost. Little’s Law, ${Q_{\text{req}}} = {\lambda_{\text{arr}}} {T_{\text{lat}}}$, gives a one-line consistency check on any serving measurement. The KV cache grows with sequence length, batch size, and KV-head width and can exceed the model weights (principle [[01 Books/Volume II - Scaling/03 The Fleet in Production/V2 Fleet-In-Production Principles#^pri-autoregressive-bottleneck|18]]); paging reduces fragmentation and reservation losses without removing the underlying footprint.

Back to top

## Source References

^source-references

Kleinrock, L. 1975. *Queueing Systems, Volume 1: Theory*. Wiley-Interscience.

^ref-kleinrock1975queueing

Jain, R. 1991. *The Art of Computer Systems Performance Analysis: Techniques for Experimental Design, Measurement, Simulation, and Modeling*. John Wiley & Sons.

^ref-jain1991art

Erlang, Agner Krarup. 1909. “The Theory of Probabilities and Telephone Conversations.” *Nyt Tidsskrift for Matematik B* 20: 33–39.

^ref-erlang1909telephone

Little, John D. C. 1961. “A Proof for the Queuing Formula: $L = \lambda W$.” *Operations Research* 9 (3): 383–87. https://doi.org/10.1287/opre.9.3.383.

^ref-little1961

Kwon, Woosuk, Zhuohan Li, Siyuan Zhuang, Ying Sheng, Lianmin Zheng, Cody Hao Yu, Joseph Gonzalez, Hao Zhang, and Ion Stoica. 2023. “Efficient Memory Management for Large Language Model Serving with PagedAttention.” *Proceedings of the 29th Symposium on Operating Systems Principles*, 611–26. https://doi.org/10.1145/3600006.3613165.

^ref-kwon2023

## Source

[Repository Source](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/books/vol2/backmatter/appendix_inference.qmd) · [Original License](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/LICENSE.md)

[Rendered Reading Snapshot](https://mlsysbook.ai/vol2/backmatter/appendix_inference.html#sec-appdx-appendix-inference). Rendering provenance is recorded in the import manifest.
