---
title: V1 Data Foundations
type: Reference
volume: 1
chapter: 0
publication_status: Released
source_repository: https://github.com/klappe-pm/cs249r_book
source_commit: de87c0103806d7bfb1c677dbb77a2b92fa00c298
source_path: books/vol1/backmatter/appendix_data.qmd
source_anchor: sec-appdx-data-foundations
source_mode: Source-Correlated Published HTML
tags:
- Type/Reference
- Book/Volume_1
rendered_source_url: https://mlsysbook.ai/vol1/backmatter/appendix_data.html
---

# V1 Data Foundations

[[Home|Home]] · [[01 Books/Volume I - Foundations/Volume 1 Overview|Volume Overview]]

^sec-appdx-data-foundations

Data problems rarely present as data problems. They surface as a training run that will not speed up, an accelerator sitting idle, accuracy eroding while dashboards stay green, or an evaluation whose verdict does not survive a second test set. The chapters use the back-of-the-envelope calculations and statistical tools that trace such symptoms back to measurable quantities without deriving them. This appendix supplies the derivations: transfer times, decode and storage-layout costs, tail probabilities, the sample sizes that make a measured rate trustworthy, and drift divergences. The tools lean on basic probability and on the data term of the iron law.

## How to Use This Appendix

^how-to-use-this-appendix

This appendix is a reference organized by symptom. Each section states its tool compactly and points to the chapter that teaches the concept and applies it to a lighthouse workload, and [[05 Reference/Volume I - Foundations/V1 Data Foundations#^tbl-appdx-data-lookup|table 1]] maps each symptom to the section that carries the tool.

| **When the need is…**                                      | **Tool**                                       | **Section**                                                                                                                               |
|:-----------------------------------------------------------|:-----------------------------------------------|:------------------------------------------------------------------------------------------------------------------------------------------|
| **Moving a dataset between sites or regions**              | Transfer time ${D_{\text{vol}}}/{\text{BW}}$   | [[05 Reference/Volume I - Foundations/V1 Data Foundations#^sec-appdx-data-foundations-napkin-math-physics-data-gravity-9ae0\|section 1.1.1]] |
| **An accelerator starving behind CPU decode**              | Decode throughput by format                    | [[05 Reference/Volume I - Foundations/V1 Data Foundations#^sec-appdx-data-foundations-cost-serialization-b921\|section 1.1.2]]               |
| **Reading a few features from wide records**               | Row versus columnar layout                     | [[05 Reference/Volume I - Foundations/V1 Data Foundations#^sec-appdx-data-foundations-row-vs-columnar-formats-bca2\|section 1.1.3]]          |
| **A feature pipeline whose cost explodes**                 | Selection, projection, and join costs          | [[05 Reference/Volume I - Foundations/V1 Data Foundations#^sec-appdx-data-foundations-algebra-data-9792\|section 1.1.4]]                     |
| **An average that looks fine while users complain**        | Session-level tail probability                 | [[05 Reference/Volume I - Foundations/V1 Data Foundations#^sec-appdx-data-foundations-distributions-long-tail-901f\|section 1.2.1]]          |
| **Deciding whether a measured rate or difference is real** | Confidence interval, sample size, McNemar, A/B | [[05 Reference/Volume I - Foundations/V1 Data Foundations#^sec-appdx-data-foundations-sampling-estimation-5b1e\|section 1.2.2]]              |
| **Accuracy drifting silently in production**               | KL divergence, PSI, KS statistic               | [[05 Reference/Volume I - Foundations/V1 Data Foundations#^sec-appdx-data-foundations-measuring-drift-divergence-a6dd\|section 1.2.3]]       |
| **More data that no longer improves the model**            | Entropy and signal per byte                    | [[05 Reference/Volume I - Foundations/V1 Data Foundations#^sec-appdx-data-foundations-information-theory-systems-c033\|section 1.2.4]]       |

Table 1: **Symptom-to-Section Lookup**: Each row pairs a symptom a chapter may name with the tool in this appendix that turns it into a measurement.

^tbl-appdx-data-lookup

The first half of the appendix, Moving and Storing Data, serves the data pipelines in **[[01 Books/Volume I - Foundations/01 Foundations/04 Data Engineering/V1-04.06 Ingestion and Validation#^sec-data-engineering-data-pipeline-architecture-b527|Ingestion and Validation]]**. The second half, Probability and Statistics, provides the tests that decide whether a measured number can be trusted for the evaluations in **[[01 Books/Volume I - Foundations/03 Optimization/12 Benchmarking/V1-12.09 Benchmarking Best Practices#^sec-benchmarking-statistical-methodological-issues-7aa5|Statistical and methodological issues]]** and the operational monitoring in **[[01 Books/Volume I - Foundations/04 Deployment/14 ML Operations/V1-14.06 Production Monitoring#^sec-ml-operations-model-infrastructure-monitoring-3988|Statistical monitoring and drift detection]]**.

## Moving and Storing Data

^sec-appdx-data-foundations-data-engineering-foundations-0c20

Before a model can learn from a record, the record must leave storage, cross a network, and be decoded into tensors, and any one of those steps can idle an accelerator before a single gradient is computed. **[[01 Books/Volume I - Foundations/01 Foundations/04 Data Engineering/V1-04 Data Engineering#^sec-data-engineering|Data Engineering]]** develops these stages inside a working pipeline; the reference models and tables below provide the templates for checking each cost by hand.

### Data Gravity

^sec-appdx-data-foundations-napkin-math-physics-data-gravity-9ae0

Copying a petabyte of training data across a 1 Gbps wide-area link takes months, whereas shipping the job to the cluster that already holds the data takes minutes. Data gravity[[05 Reference/Volume I - Foundations/V1 Data Foundations#^fn1|¹]] names this constraint, which transfer-time arithmetic makes precise, and **[[01 Books/Volume I - Foundations/01 Foundations/04 Data Engineering/V1-04.10 Physics of Data#^sec-data-engineering-data-gravity-adcb|Data gravity]]** applies it to petabyte-scale training data. Network bandwidth is finite and does not grow with compute, so moving a large dataset can cost more time and energy than moving computation to where the data already lives.

The ideal line-rate transfer time is ${T}= {D_{\text{vol}}}/{\text{BW}}$ after converting data volume and bandwidth to compatible units (the calculations below convert decimal bytes and bits per second explicitly). For the large volumes here, latency is negligible. **[[05 Reference/Volume I - Foundations/V1 Machine Foundations#^sec-appdx-machine-foundations-bandwidth-vs-latency-5320|Bandwidth versus latency]]** gives the full equation with its latency term. [[05 Reference/Volume I - Foundations/V1 Data Foundations#^tbl-data-gravity|Table 2]] gives lower bounds; protocol overhead and endpoint limits increase them.

| **Data Volume** | **1 Gbps (Standard WAN)** | **10 Gbps (High-End WAN)** | **100 Gbps (Direct Connect)** | **Truck (Illustrative)** |
|:----------------|:-------------------------:|:--------------------------:|:-----------------------------:|:------------------------:|
| **1 TB**        |         2.2 hours         |        13.3 minutes        |          80 seconds           |           N/A            |
| **100 TB**      |          9 days           |         22.2 hours         |           2.2 hours           |           N/A            |
| **1 PB**        |         3 months          |           9 days           |          22.2 hours           |          2 days          |

Table 2: **The Cost of Inertia**: These transfer times explain why we often “ship compute to data” rather than “ship data to compute.” Network columns are lower bounds at sustained line rate. The truck entry is an illustrative elapsed-time model for 1 PB: 8 hours to load, 32 hours in transit, and 8 hours to unload, excluding scheduling and provisioning overhead.

^tbl-data-gravity

### Serialization Cost

^sec-appdx-data-foundations-cost-serialization-b921

Even after data arrives at the machine, it must be decoded before the accelerator can use it.[[05 Reference/Volume I - Foundations/V1 Data Foundations#^fn2|²]] The CPU cost of that decoding can differ by an order of magnitude across formats ([[05 Reference/Volume I - Foundations/V1 Data Foundations#^tbl-serialization-cost|table 3]]). Parsing text-based formats like JavaScript Object Notation (JSON) or CSV into floating-point numbers is CPU-bound and often leaves the accelerator idle.

| **Format**   | **Decoding Speed (MB/s)** | **Relative CPU Decode Cost** | **Suitability**        |
|:-------------|:-------------------------:|:----------------------------:|:-----------------------|
| **CSV/JSON** |         ~100 MB/s         |             High             | Inspection/interchange |
| **Protobuf** |         ~300 MB/s         |            Medium            | RPC/Messages           |
| **Parquet**  |        ~1,000 MB/s        |             Low              | Columnar storage       |

Table 3: **Serialization Overhead**: These illustrative values show why binary columnar formats can outperform row-based text, but they are not portable benchmarks. Arrow is an in-memory/IPC format; Parquet is a compressed storage format.

^tbl-serialization-cost

### Row and Columnar Formats

^sec-appdx-data-foundations-row-vs-columnar-formats-bca2

Decoding speed per byte is only half of the format cost, because the storage layout also decides how many bytes a query must read from disk in the first place. Row-oriented formats such as CSV and JSON store data record-by-record, so reading the `age` field still requires parsing every attribute in each row, a layout that suits append-only logs while penalizing feature filtering. In contrast, Parquet stores compressed column chunks on disk, and Arrow provides a contiguous columnar representation in memory and across inter-process communication (IPC). Parquet readers can use *projection pushdown* to fetch only the requested column chunks, while both formats feed *vectorized processing*. Where the row layout forces a wide scan across all fields (`ID`, `Age`, `Loc`), the columnar layout isolates the target `Age` chunk and avoids moving irrelevant attributes ([[05 Reference/Volume I - Foundations/V1 Data Foundations#^fig-row-vs-col|figure 1]]). **[[01 Books/Volume I - Foundations/01 Foundations/04 Data Engineering/V1-04.11 Storage and Delivery#^sec-data-engineering-formats-compression-partitioning-8b17|Formats, compression, and partitioning]]** develops format choice as a lever on the data term of the iron law.

![[90 Assets/Volume I/Shared Figures/Generated Figure 0e32cb813c.svg]]

Figure 1: **Storage Layouts**: Row-oriented formats group values by record, so the illustrated scan reads every field. Column-oriented formats group values by feature, so the illustrated scan reads only Age.

^fig-row-vs-col

**Systems Perspective 1.1: The accelerator starvation problem**

The choice of file format often determines whether a training pipeline is I/O bound or compute bound. Row-oriented formats force full-record scans, so storage layout compounds the decode cost whenever models consume a subset of tabular features, and the data-movement term of the iron law can silently become the critical path. **[[01 Books/Volume I - Foundations/01 Foundations/04 Data Engineering/V1-04.10 Physics of Data#^sec-data-engineering-feeding-problem|The feeding problem]]** develops that starvation condition and the stage that causes it.

### The Algebra of Data

^sec-appdx-data-foundations-algebra-data-9792

Layout fixes what a scan can skip, while the operations a feature pipeline applies decide how much it must read. Feature engineering turns raw records into the columns a model can learn from. A pipeline first narrows the population, then chooses the features, then attaches context from other tables. Those three moves correspond to three Structured Query Language (SQL) primitives, and their computational cost determines whether the feature job stays local, scans unnecessary bytes, or turns into a network shuffle.

1.  **Selection (${\sigma}$)**: Filtering rows (for example, `WHERE age > 30`).
    - **Cost**: For a table of ${N}$ rows, $\mathcal{O}(\log {N}+ {K})$ if a B-tree index lookup returns ${K}$ rows; $\mathcal{O}({N})$ for a full scan.
2.  **Projection ($\pi$)**: Selecting columns (for example, `SELECT age`).
    - **Cost**: Selected chunks plus decoding and metadata in columnar formats. This row-format example reads 1 KB for a 4-byte integer, wasting 99.6 percent of the read.
3.  **Join ($\bowtie$)**: Combining tables. Usually the most expensive operation.
    - **Shuffle Join**: Both tables are partitioned by key and exchanged over the network.
      - **Cost**: Reshuffling both 1 TB tables moves ~2 TB; partitioning and locality can reduce this.
    - **Broadcast Join**: One small table is sent to all workers.
      - **Cost**: ${s_{\text{table}}}({N_{\text{workers}}}-1)$ bytes; the ${s_{\text{table}}}$-byte table must fit on each of ${N_{\text{workers}}}$ workers.

**[[01 Books/Volume I - Foundations/01 Foundations/04 Data Engineering/V1-04.08 Data Processing#^sec-data-engineering-scaling-distributed-processing-cb9b|Distributed processing]]** shows when these costs push feature processing beyond one machine. Formats, serialization, and algebraic primitives determine how efficiently data moves. They say nothing about whether the numbers computed from that data can be trusted, or whether the data has changed character since training. Answering those questions requires probability and statistics.

## Probability and Statistics

^sec-appdx-data-foundations-probability-statistics-3934

Once records arrive at the model, summary averages can still mislead an engineer about whether a measured number can be trusted or whether the data has changed character since training: a low mean latency can hide frequent slow user sessions, a 0.5-point accuracy gain on a finite validation set can sit inside binomial noise, and a feature’s mean can stay constant while its tails drift enough to degrade predictions. Four statistical tools separate those real effects from noise: tail probabilities for multi-request sessions, confidence intervals and paired or online sample-size formulas for finite evaluations, divergence measures for distribution shift, and information-theoretic units for the signal a dataset carries.

### Distributions and the Long Tail

^sec-appdx-data-foundations-distributions-long-tail-901f

A service whose “p99” (99th percentile) latency is 500 ms leaves at most 1 percent of individual requests slower than 500 ms, yet at scale (1M users) even a 1 percent affected-user rate degrades the experience of 10,000 users, and multi-request sessions push the fraction of users who see at least one slow response much higher. Because latency distributions are long-tailed, user-visible services are governed by high-percentile behavior rather than by the mean response time ([[05 Reference/Volume I - Foundations/V1 Data Foundations#^ref-dean2013|Dean and Barroso 2013]]).

**Napkin Math 1.1: The median experience**

For ${N_{\text{session}}}=$ 100 independent requests, each with a 0.01 chance of being slow, the probability of at least one p99-tail event is $\Pr(\text{Slow}) = 1 - (0.99)^{100} \approx 1 - 0.366 = 63.4\%$.

**Systems insight**: With independent requests, a 100-request session is more likely than not to include an event beyond p99. Correlated slowdowns can change this probability ([[05 Reference/Volume I - Foundations/V1 Data Foundations#^ref-dean2013|Dean and Barroso 2013]]).

**[[01 Books/Volume I - Foundations/04 Deployment/13 Model Serving/V1-13.05 Queuing Theory#^sec-model-serving-tail-latency-5376|Tail latency]]** develops tail latency for a serving system, where queuing produces the tail and request fan-out amplifies it. Tail probabilities describe one measured distribution. Deciding whether a measured rate is itself trustworthy is a sampling question.

### Sampling and Estimation

^sec-appdx-data-foundations-sampling-estimation-5b1e

Every accuracy, error rate, and conversion rate in this book is measured on a finite sample, so every one of them carries sampling error. The question that decides a release is whether a measured number, or a measured difference, is larger than that error. Four tools answer it: an interval for one rate, the sample size that makes the interval narrow enough, a paired test for two models scored on the same examples, and the traffic an online A/B test needs. Each reduces to a short formula for the number of labeled examples or user sessions an engineer must collect.

The first tool is the **confidence interval for a rate**. A model that classifies a fraction ${\hat{p}}$ of ${N}$ independent examples correctly has, by the normal approximation to the binomial, an interval of

$$
{\hat{p}} \pm {z_{\alpha/2}} \sqrt{\frac{{\hat{p}}(1-{\hat{p}})}{{N}}} \tag{1}
$$

^eq-appdx-data-rate-interval

at the confidence level ${z_{\alpha/2}}$ encodes (1.96 for 95 percent). ResNet-50 at 76 percent top-1 on the 50,000-image ImageNet validation set is therefore known only to within about 0.4 percentage points. Two models scored on independent samples of that size have a difference interval about $\sqrt{2}$ times wider, because the variances of the two estimates add, roughly 0.5 percentage points. A smaller accuracy gap between them cannot be resolved that way. **[[01 Books/Volume I - Foundations/03 Optimization/12 Benchmarking/V1-12.09 Benchmarking Best Practices#^sec-benchmarking-statistical-methodological-issues-7aa5|Statistical and methodological issues]]** applies the interval to benchmark reports and shows why a single accuracy number without one is not a result.

When the evaluation set has not yet been collected, solving [[05 Reference/Volume I - Foundations/V1 Data Foundations#^eq-appdx-data-rate-interval|equation 1]] for ${N}$ gives the required **sample size for a rate**: the critical value squared, times ${\hat{p}}(1-{\hat{p}})$, divided by the square of the target half-width. Because the half-width falls only as the square root of the count, halving it quadruples the labeling cost. A keyword spotter expected to detect 98 percent of wake words needs 3,012 labeled one-second clips to pin that rate within 0.5 percentage points (about 50 minutes of audio). Reaching 0.25 percentage points takes 12,047 clips (3.3 hours). The count applies to every slice that must be certified separately. **[[01 Books/Volume I - Foundations/04 Deployment/15 Responsible Engineering/V1-15.04 Responsible Engineering Across the Lifecycle#^sec-responsible-engineering-predeployment-assessment-2324|Specify: Requirements before training]]** multiplies it across demographic subgroups, where a rare group must be oversampled to reach the count at all. **[[01 Books/Volume I - Foundations/03 Optimization/09 Data Selection/V1-09.03 Measuring Data Value#^sec-data-selection-computeoptimal-frontier-24ba|The compute-optimal frontier]]** needs it to confirm that a curated subset still reaches the target accuracy.

When a baseline and a compressed model are scored on the same validation set, **McNemar’s test** sharpens the comparison because the examples both models get right or both get wrong cancel out. Only the discordant counts matter: ${n_{\text{base}}}$ examples that only the baseline gets right and ${n_{\text{comp}}}$ that only the compressed model gets right. The test statistic is

$$
{\chi^2} = \frac{({n_{\text{base}}} - {n_{\text{comp}}})^2}{{n_{\text{base}}} + {n_{\text{comp}}}}, \tag{2}
$$

^eq-appdx-data-mcnemar

and the difference is significant at 95 percent when it exceeds 3.84 (the square of 1.96). Suppose FP32 and INT8 ResNet-50 disagree on the ImageNet validation set as follows, an illustrative split: 300 images only the FP32 model gets right and 250 only the INT8 model gets right. The net loss is 50 images, 0.1 percentage points of accuracy, well inside the unpaired interval above, yet [[05 Reference/Volume I - Foundations/V1 Data Foundations#^eq-appdx-data-mcnemar|equation 2]] gives ${\chi^2}=$ 4.55, which exceeds the threshold. Pairing resolves a drop that independent samples could not, which is why an evaluation harness must keep per-example outcomes rather than only the two accuracies. **[[01 Books/Volume I - Foundations/03 Optimization/12 Benchmarking/V1-12.09 Benchmarking Best Practices#^sec-benchmarking-statistical-methodological-issues-7aa5|Statistical and methodological issues]]** works through the case in which the same marginal scores leave the verdict open, and **[[01 Books/Volume I - Foundations/03 Optimization/10 Model Compression/V1-10 Model Compression#^sec-model-compression|Model Compression]]** produces the INT8 model whose accuracy loss the test checks.

When the comparison moves to live traffic, an online **A/B test** assigns users at random to a control arm and a treatment arm and compares a rate, such as conversion, between them. Let ${\delta_{\text{MDE}}}$ be the smallest absolute difference worth detecting, ${\sigma}^2$ the per-user variance (the baseline rate times one minus it for a yes-or-no outcome), and ${z_{\beta}}$ the critical value for the chosen power. The users needed per arm are

$$
{n} = \frac{2({z_{\alpha/2}} + {z_{\beta}})^2 {\sigma}^2}{{\delta_{\text{MDE}}}^2}. \tag{3}
$$

^eq-appdx-data-ab-sample-size

For a 2 percent relative lift on a 5 percent baseline at 95 percent confidence and 80 percent power, [[05 Reference/Volume I - Foundations/V1 Data Foundations#^eq-appdx-data-ab-sample-size|equation 3]] requires 745,644 users per arm in the release scenario of **[[01 Books/Volume I - Foundations/04 Deployment/14 ML Operations/V1-14.05 Releasing Models#^sec-ml-operations-ab-testing-model-validation-e480|A/B testing for model validation]]**. A service that can route 100,000 users per day to each arm needs about 7.5 days to finish one test. That duration, not compute, sets how often a recommendation model can be released on evidence.

Each of these tools assumes the examples come from one fixed population. When the population itself moves, the question changes from estimating a rate to detecting that the distribution has shifted.

### Measuring Drift

^sec-appdx-data-foundations-measuring-drift-divergence-a6dd

Comparing means is not enough to catch that shift, because a distribution’s tails or bin shares can move while its average stays fixed. Comparing the serving distribution (${P_t}$) with the training distribution (${P_0}$) therefore requires a distance measure across the full distribution shape: KL divergence and the population stability index for binned features, and the Kolmogorov-Smirnov (KS) statistic for continuous ones. **[[01 Books/Volume I - Foundations/01 Foundations/04 Data Engineering/V1-04.13 Operational Data Health#^sec-data-engineering-detecting-responding-data-drift-509a|Data drift detection and response]]** develops drift detection and its taxonomy around these three measures, and **[[01 Books/Volume I - Foundations/04 Deployment/14 ML Operations/V1-14.06 Production Monitoring#^sec-ml-operations-production-monitoring-5e1b|Production Monitoring]]** decides what an alert should trigger.

For discrete outcomes ${x}$, [[05 Reference/Volume I - Foundations/V1 Data Foundations#^eq-appdx-data-kl-divergence|equation 4]] expresses KL divergence[[05 Reference/Volume I - Foundations/V1 Data Foundations#^fn3|³]] as the expected extra coding cost of approximating ${P_t}$ with ${P_0}$ ([[05 Reference/Volume I - Foundations/V1 Data Foundations#^ref-kullback1951|Kullback and Leibler 1951]]; [[05 Reference/Volume I - Foundations/V1 Data Foundations#^ref-cover2006|Cover and Thomas 2006]]). The displayed form is finite only when ${P_0}({x}) > 0$ wherever ${P_t}({x}) > 0$. Production implementations therefore need explicit smoothing or zero handling.

$$
{\mathcal{D}_{\text{KL}}}({P_t} \lVert {P_0}) = \sum_{x}{P_t}({x}) \log \frac{{P_t}({x})}{{P_0}({x})} \tag{4}
$$

^eq-appdx-data-kl-divergence

**Napkin Math 1.2: Worked example: KL divergence for drift detection**

**Scenario**: A keyword-spotting model was trained on audio windows binned by signal-to-noise ratio: 60 percent high, 30 percent medium, and 10 percent low. After the device maker changes the microphone in a new product generation, the windows arriving from the fleet shift to 45 percent high, 40 percent medium, and 15 percent low.

**Math**:

Training distribution ${P_0}$: \[0.60, 0.30, 0.10\]. Serving distribution ${P_t}$: \[0.45, 0.40, 0.15\].

$$
\begin{gather*} \mathcal{D}_{\text{KL}}(P_t \lVert P_0) = 0.45 \log\frac{0.45}{0.60} + 0.40 \log\frac{0.40}{0.30} + 0.15 \log\frac{0.15}{0.10}\end{gather*}
$$

$$
\begin{gather*} = 0.45 \times (-0.2877) + 0.40 \times (0.2877) + 0.15 \times (0.4055) \\[-1pt] = -0.1295 + 0.1151 + 0.0608 = 0.0464\text{ nats}\end{gather*}
$$

$$
\begin{gather*} \mathcal{D}_{\text{KL}}(P_0 \lVert P_t) = 0.60 \log\frac{0.60}{0.45} + 0.30 \log\frac{0.30}{0.40} + 0.10 \log\frac{0.10}{0.15}\end{gather*}
$$

$$
\begin{gather*} = 0.60 \times 0.2877 + 0.30 \times (-0.2877) + 0.10 \times (-0.4055) \\[-1pt] = 0.1726 + (-0.0863) + (-0.0405) = 0.0458\text{ nats}\end{gather*}
$$

The two directions give different values, ${\mathcal{D}_{\text{KL}}}({P_0} \lVert {P_t}) \neq {\mathcal{D}_{\text{KL}}}({P_t} \lVert {P_0})$. The population stability index (PSI) symmetrizes this by summing the two directions. The calculation below uses natural logarithms:

$$
\begin{gather*} \text{PSI} = \sum (P_{0,i} - P_{t,i}) \log\frac{P_{0,i}}{P_{t,i}} = (0.15)(0.2877) + (-0.10)(-0.2877) + (-0.05)(-0.4055) \\[-1pt] = 0.04315 + 0.02877 + 0.02027 = 0.0922 \end{gather*}
$$

**Systems insight**: Since PSI = 0.0922 \< 0.1, this drift sits just below the conventional warning threshold and well short of the critical threshold of 0.25 used in **[[01 Books/Volume I - Foundations/04 Deployment/14 ML Operations/V1-14 ML Operations#^sec-ml-operations|ML Operations]]**. The right response is to keep the feature on the monitoring dashboard and look for corroborating drift signals rather than retraining from this statistic alone. The statistic is also cheap to collect on an always-on device, which can report three bin counters per interval instead of raw audio, so the check fits the power budget and raw recordings never need to leave the device.

Those PSI thresholds remain illustrative because their meaning depends on sample size, binning, smoothing, and zero handling, and because retraining requires model-quality evidence.

KL divergence and PSI compare binned or categorical distributions. For a continuous feature, such as the loudness of an audio window, the two-sample Kolmogorov-Smirnov statistic avoids binning altogether. It is the largest gap between the empirical cumulative distribution functions of a training sample and a serving sample,

$$
{\mathcal{D}_{\text{KS}}}= \max_{{x_{\text{feat}}}}|{F_{P_0}}({x_{\text{feat}}}) - {F_{P_t}}({x_{\text{feat}}})|.
$$

Its critical value shrinks with the square root of the sample sizes, so a large serving sample flags even a tiny shift as significant. Whether that shift matters is a separate question. **[[01 Books/Volume I - Foundations/01 Foundations/04 Data Engineering/V1-04.06 Ingestion and Validation#^sec-data-engineering-quality-validation-monitoring-498f|Quality through validation and monitoring]]** works the test through with its critical value. All three measures rest on information theory, which supplies their units.

### Information Theory for Systems

^sec-appdx-data-foundations-information-theory-systems-c033

A training run can consume more examples, run longer, and still stop improving if the added data carries too little useful signal. At that point the limit is the information the data pipeline delivers to the learner, not compute or bandwidth. **[[05 Reference/Volume I - Foundations/V1 The D·A·M Taxonomy#^sec-appdx-dam-taxonomy-information-roofline-destination-6426|The information roofline]]** treats that data quality limit as a diagnostic constraint, and information theory provides the units for reasoning about it.

- **Entropy (${H}$)**:[[05 Reference/Volume I - Foundations/V1 Data Foundations#^fn4|⁴]] The average uncertainty in a distribution, defined as ${H}({X}) = -\sum {p}({x}) \log {p}({x})$. The log base sets the unit: natural logs give nats, while $\log_2$ gives bits. A uniform distribution has maximum entropy only over a fixed finite support. This connects directly to KL divergence above: ${\mathcal{D}_{\text{KL}}}$ measures the excess coding cost of using the wrong distribution.
- **Information density**: Used here as a book-level heuristic for useful learning signal per unit of storage, not as a standard information-theory quantity.
- **Signal-to-noise ratio (SNR)**: The ratio of signal power to noise power. In ML, the book uses low SNR qualitatively for data in which task-relevant structure is weak relative to noise; adding compute cannot compensate for missing task-relevant signal.

Together with tail probabilities, finite-sample intervals, and drift divergences, these quantities complete the statistical half of the data foundations: the first half of the appendix prices how fast bytes move and decode, and the second prices how much evidence those bytes actually carry.

## Summary

^sec-appdx-data-foundations-summary-3c72

When a data symptom appears, find its row in [[05 Reference/Volume I - Foundations/V1 Data Foundations#^tbl-appdx-data-lookup|table 1]] and compute the number. Each section points back to the chapter that teaches the tool, where the lighthouse workloads show it deciding a design.

Back to top

## Source References

^source-references

McCrory, Dave. 2010. *Data Gravity – in the Clouds*.

^ref-mccrory2010datagravity

Dean, Jeffrey, and Luiz André Barroso. 2013. “The Tail at Scale.” *Communications of the ACM* 56 (2): 74–80. https://doi.org/10.1145/2408776.2408794.

^ref-dean2013

Kullback, Solomon, and Richard A. Leibler. 1951. “On Information and Sufficiency.” *The Annals of Mathematical Statistics* 22 (1): 79–86. https://doi.org/10.1214/aoms/1177729694.

^ref-kullback1951

Cover, Thomas M., and Joy A. Thomas. 2006. *Elements of Information Theory*. 2nd ed. Wiley. https://doi.org/10.1002/047174882X.

^ref-cover2006

Shannon, Claude E. 1948. “A Mathematical Theory of Communication.” *Bell System Technical Journal* 27 (3): 379–423. https://doi.org/10.1002/j.1538-7305.1948.tb01338.x.

^ref-shannon1948

## Footnotes

^footnotes

<sup>1</sup> **Data gravity**: Coined by Dave McCrory in 2010 to describe how large datasets attract services and applications toward them, much as massive bodies attract smaller ones in physics ([[05 Reference/Volume I - Foundations/V1 Data Foundations#^ref-mccrory2010datagravity|McCrory 2010]]).

^fn1

<sup>2</sup> **Serialization**: From Latin *serialis* (forming a series). The process of converting in-memory data structures into a byte stream for storage or transmission, and the reverse (*deserialization*). In ML pipelines, the choice of serialization format can dominate end-to-end training time; **[[01 Books/Volume I - Foundations/01 Foundations/04 Data Engineering/V1-04.11 Storage and Delivery#^sec-data-engineering-data-ingestion-8efc|The dataloader]]** covers pipeline design strategies that minimize this overhead.

^fn2

<sup>3</sup> **KL divergence**: Named after Solomon Kullback and Richard Leibler, who introduced it in 1951. Also called *relative entropy*, it quantifies the expected extra information needed to encode samples from one distribution using a code optimized for another; for drift monitoring in this book, the canonical direction is ${\mathcal{D}_{\text{KL}}}({P_t} \lVert {P_0})$. With natural logarithms, as in the example above, the unit is nats; with base-2 logarithms, the unit is bits.

^fn3

<sup>4</sup> **Entropy**: Shannon adopted the term in 1948 to quantify information content ([[05 Reference/Volume I - Foundations/V1 Data Foundations#^ref-shannon1948|Shannon 1948]]). In systems terms, Shannon entropy is a lower bound on average lossless code length. Practical prefix codes approach it, and block codes can approach it asymptotically. These bounds inform compression ratios and data-pipeline sizing.

^fn4

## Source

[Repository Source](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/books/vol1/backmatter/appendix_data.qmd) · [Original License](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/LICENSE.md)

[Rendered Reading Snapshot](https://mlsysbook.ai/vol1/backmatter/appendix_data.html#sec-appdx-data-foundations). Rendering provenance is recorded in the import manifest.
