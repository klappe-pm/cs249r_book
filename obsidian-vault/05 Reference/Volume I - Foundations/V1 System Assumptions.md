---
title: V1 System Assumptions
type: Reference
volume: 1
chapter: 0
publication_status: Released
source_repository: https://github.com/klappe-pm/cs249r_book
source_commit: de87c0103806d7bfb1c677dbb77a2b92fa00c298
source_path: books/vol1/backmatter/appendix_assumptions.qmd
source_anchor: sec-appdx-system-assumptions
source_mode: Source-Correlated Published HTML
tags:
- Type/Reference
- Book/Volume_1
rendered_source_url: https://mlsysbook.ai/vol1/backmatter/appendix_assumptions.html
---

# V1 System Assumptions

[[Home|Home]] · [[01 Books/Volume I - Foundations/Volume 1 Overview|Volume Overview]]

^sec-appdx-system-assumptions

A napkin calculation is only as trustworthy as the inputs behind it, and those inputs are easy to lose track of: an accelerator’s peak rate, a model’s parameter count, an electricity price, an energy cost per operation. This appendix gathers those canonical values and the unit conventions they depend on into a single reference sheet, so that a reader can check an estimate or substitute a newer figure. The chapters can then argue from numbers without restating where each one came from.

## How to Use This Appendix

^how-to-use-this-appendix

Every value here is dated: it belongs to a particular product, model, or price, and it changes when the next generation ships. Ratios and orders of magnitude, such as the energy gap between a DRAM access and an arithmetic operation, hold much longer, and **[[05 Reference/Volume I - Foundations/V1 Machine Foundations#^sec-appdx-machine-foundations-numbers-know-b531|Numbers to Know]]** collects them. The NVIDIA H100 is the book’s reference machine, so training and serving examples plug in the values of [[05 Reference/Volume I - Foundations/V1 System Assumptions#^sec-appdx-assumptions-h100-reference-machine-2b6f|section 1.2.2]] unless a chapter names another device. [[05 Reference/Volume I - Foundations/V1 System Assumptions#^tbl-appdx-assumptions-lookup|Table 1]] maps each need to the section that holds the values. [[05 Reference/Volume I - Foundations/V1 System Assumptions#^sec-appdx-assumption-provenance|Section 1.10]] records where each value comes from, so a reader can substitute a current or local value and rerun the estimate without changing its method.

| **Need**                                                                   | **Section**                                                                                                                            |
|:---------------------------------------------------------------------------|:---------------------------------------------------------------------------------------------------------------------------------------|
| **Convert a unit alias or check a decimal prefix**                         | [[05 Reference/Volume I - Foundations/V1 System Assumptions#^sec-appdx-assumptions-unit-conventions-3e8b\|section 1.1]]              |
| **Compare accelerator generations on one page**                            | [[05 Reference/Volume I - Foundations/V1 System Assumptions#^sec-appdx-assumptions-accelerator-matrix-c4d0\|section 1.2.1]]          |
| **Plug in the reference machine’s peak rates, bandwidth, or ridge point**  | [[05 Reference/Volume I - Foundations/V1 System Assumptions#^sec-appdx-assumptions-h100-reference-machine-2b6f\|section 1.2.2]]      |
| **Look up an older or alternative accelerator**                            | [[05 Reference/Volume I - Foundations/V1 System Assumptions#^sec-appdx-assumptions-accelerator-specifications-7a21\|section 1.2]]    |
| **Size a mobile, edge, or microcontroller deployment**                     | [[05 Reference/Volume I - Foundations/V1 System Assumptions#^sec-appdx-assumptions-cpu-mobile-edge-d2f9\|section 1.2.9]]             |
| **Check which numeric formats a GPU generation supports**                  | [[05 Reference/Volume I - Foundations/V1 System Assumptions#^sec-appdx-assumptions-precision-support-6e3a\|section 1.2.10]]          |
| **Interpret an advertised peak-throughput claim**                          | [[05 Reference/Volume I - Foundations/V1 System Assumptions#^sec-appdx-assumptions-advertised-peak-a7c5\|section 1.2.11]]            |
| **Turn a list price into a price per unit of peak throughput**             | [[05 Reference/Volume I - Foundations/V1 System Assumptions#^sec-appdx-assumptions-accelerator-cost-worksheet-3f02\|section 1.2.12]] |
| **Find a lighthouse’s home regime and the resource that limits it**        | [[05 Reference/Volume I - Foundations/V1 System Assumptions#^sec-appdx-assumptions-lighthouse-workloads-5c19\|section 1.3.1]]        |
| **Look up a model’s parameters, operations, or training scale**            | [[05 Reference/Volume I - Foundations/V1 System Assumptions#^sec-appdx-assumptions-reference-models-e2d4\|section 1.3.2]]            |
| **Size training-state memory per parameter**                               | [[05 Reference/Volume I - Foundations/V1 System Assumptions#^sec-appdx-assumptions-training-memory-conventions-91b3\|section 1.4]]   |
| **Estimate the energy of an operation or a memory access**                 | [[05 Reference/Volume I - Foundations/V1 System Assumptions#^sec-appdx-assumptions-energy-constants-4a6d\|section 1.5]]              |
| **Compare access latency and bandwidth across memory, links, and storage** | [[05 Reference/Volume I - Foundations/V1 System Assumptions#^sec-appdx-assumptions-latency-bandwidth-tier-c1a2\|section 1.6.1]]      |
| **Estimate a transfer time over PCIe, NVLink, InfiniBand, or Ethernet**    | [[05 Reference/Volume I - Foundations/V1 System Assumptions#^sec-appdx-assumptions-interconnect-specifications-0f6b\|section 1.6.2]] |
| **Price electricity or data egress**                                       | [[05 Reference/Volume I - Foundations/V1 System Assumptions#^sec-appdx-assumptions-economic-constants-8c4e\|section 1.7]]            |
| **Anchor a production request volume or sensor data rate**                 | [[05 Reference/Volume I - Foundations/V1 System Assumptions#^sec-appdx-assumptions-scale-references-d73a\|section 1.8]]              |
| **Follow a complete estimate built from these values**                     | [[05 Reference/Volume I - Foundations/V1 System Assumptions#^sec-appdx-assumptions-worked-estimates-2e95\|section 1.9]]              |
| **Trace a value to its source**                                            | [[05 Reference/Volume I - Foundations/V1 System Assumptions#^sec-appdx-assumption-provenance\|section 1.10]]                         |

Table 1: **Where to Look**: Each need maps to the section of this appendix that holds the values.

^tbl-appdx-assumptions-lookup

## Unit Conventions

^sec-appdx-assumptions-unit-conventions-3e8b

Mixing binary ($2^{30}$-byte) capacities with decimal ($10^9$-byte) bandwidths shifts a memory or transfer estimate by 7 percent before any rounding, and confusing total FLOPs with FLOP/s turns a time equation into a unit error. Every quantitative example in this book avoids those mismatches by using shared unit conventions: decimal data prefixes, distinct FLOPs and FLOP/s quantities, and the aliases in [[05 Reference/Volume I - Foundations/V1 System Assumptions#^tbl-assumptions-units|table 2]]. Each row gives the multiplier ${k}$ in `1 alias` $=$ ${k}$ `base`. Data prefixes use decimal SI ($\text{KB} = 10^3$ bytes, not 1024). Binary IEC prefixes do not appear in the book’s prose. Throughput quantities (FLOP/s, GB/s) combine these aliases with time; adding incompatible dimensions (bytes to FLOP/s) is a category error in napkin math, not a unit conversion.

Hardware capacity labels are the one deliberate exception. The reference tables retain vendor nameplate numbers and labels; the byte budgets used in calculations follow the book’s device assumptions. For example, the book models an 80 GB accelerator with $80 \times 2^{30}$ bytes and assigns $512 \times 2^{10}$ bytes to a microcontroller with 512 KB of SRAM. These are modeled capacity assumptions, not universal guarantees inferred from the labels. Every other data quantity, including model footprints, activation sizes, and transfer volumes, uses the decimal prefixes above. Where a worked example subtracts a computed footprint from a device capacity, the capacity is converted to decimal units alongside the footprint, so that the arithmetic printed on the page is the arithmetic a reader can reproduce.

| **Alias**    | **Multiplier** | **Base unit** |
|:-------------|:--------------:|:-------------:|
| **`byte`**   |       1        |     byte      |
| **`KB`**     |      1000      |     byte      |
| **`MB`**     |     1e+06      |     byte      |
| **`GB`**     |     1e+09      |     byte      |
| **`TB`**     |     1e+12      |     byte      |
| **`PB`**     |     1e+15      |     byte      |
| **`flop`**   |       1        |     flop      |
| **`GFLOPs`** |     1e+09      |     flop      |
| **`TFLOPs`** |     1e+12      |     flop      |
| **`ZFLOPs`** |     1e+21      |     flop      |
| **`param`**  |       1        |     param     |
| **`Mparam`** |     1e+06      |     param     |
| **`Gbps`**   |     1e+09      |     bit/s     |
| **`NS`**     |   $10^{-9}$    |    second     |
| **`US`**     |   $10^{-6}$    |    second     |
| **`MS`**     |   $10^{-3}$    |    second     |
| **`second`** |       1        |    second     |
| **`hour`**   |      3600      |    second     |
| **`day`**    |     86400      |    second     |
| **`joule`**  |       1        |     joule     |
| **`watt`**   |       1        |     watt      |
| **`meter`**  |       1        |     meter     |

Table 2: **Unit Conventions**: Decimal SI aliases and scale factors (book convention for napkin math). Throughput forms such as FLOP/s and GB/s divide work or data by time using the same conventions.

^tbl-assumptions-units

## Accelerator Specifications

^sec-appdx-assumptions-accelerator-specifications-7a21

Sizing a training cluster or a serving fleet requires a single set of per-chip ceilings so that estimates across chapters compare the workload rather than shifting hardware baselines. These **accelerator assumptions** supply the peak throughput, memory bandwidth, memory capacity, and thermal design power (TDP) for each generation the chapters cite. Values are vendor datasheet peaks, which serve as ceilings for napkin math rather than as sustained utilization. They are drawn from NVIDIA product documentation and IEEE Micro architecture articles ([[05 Reference/Volume I - Foundations/V1 System Assumptions#^ref-nvidia2017gpu|NVIDIA Corporation 2017]], [[05 Reference/Volume I - Foundations/V1 System Assumptions#^ref-nvidia2020v100datasheet|2020b]], [[05 Reference/Volume I - Foundations/V1 System Assumptions#^ref-NVIDIA2020|2020a]], [[05 Reference/Volume I - Foundations/V1 System Assumptions#^ref-nvidia2021a10080gb|2021]], [[05 Reference/Volume I - Foundations/V1 System Assumptions#^ref-nvidia2018t4|2018]], [[05 Reference/Volume I - Foundations/V1 System Assumptions#^ref-nvidia2024blackwell|2024]]; [[05 Reference/Volume I - Foundations/V1 System Assumptions#^ref-choquette2021|Choquette et al. 2021]]; [[05 Reference/Volume I - Foundations/V1 System Assumptions#^ref-choquette2023|Choquette 2023]]), AMD MI300X documentation ([[05 Reference/Volume I - Foundations/V1 System Assumptions#^ref-amd2023mi300x|AMD 2023]]), Google Tensor Processing Unit (TPU) publications ([[05 Reference/Volume I - Foundations/V1 System Assumptions#^ref-jouppi2020|Jouppi et al. 2020]]; [[05 Reference/Volume I - Foundations/V1 System Assumptions#^ref-jouppi2023|Jouppi et al. 2023]]), and Google Cloud’s current TPU v6e specification page ([[05 Reference/Volume I - Foundations/V1 System Assumptions#^ref-googleCloudTpuV6eDocs|Google Cloud 2026]]). Capacity rows keep the vendor’s labeled capacity. The master matrix compares the generations on one page, and the sections after it give the per-chip values and three dated comparisons on precision support, advertised peaks, and price per unit of peak throughput. **[[01 Books/Volume I - Foundations/03 Optimization/11 Hardware Acceleration/V1-11.07 Performance Bounds#^sec-hardware-acceleration-roofline-model-42ff|Performance Bounds]]** develops the roofline analysis that turns these values into a regime for a given workload.

### Master Accelerator Matrix

^sec-appdx-assumptions-accelerator-matrix-c4d0

Side by side, the accelerators the book cites span more than an order of magnitude in peak rate, memory capacity, and power, yet most place their FP16 ridge point within a band of a few hundred FLOP per byte ([[05 Reference/Volume I - Foundations/V1 System Assumptions#^tbl-appdx-assumptions-accelerator-matrix|table 3]]). The ridge point divides peak FP16 throughput by memory bandwidth (**[[05 Reference/Volume I - Foundations/V1 Machine Foundations#^sec-appdx-machine-foundations-roofline-model-2529|The Roofline model]]** develops the model). A workload whose arithmetic intensity falls below a chip’s ridge is bandwidth bound on that chip and gains nothing from a faster datapath. Two chips sit far outside that band, at opposite ends. The first TPU paired an INT8-only datapath with DDR3 memory, which places its ridge point far above the band, and the wafer-scale engine keeps its weights in on-wafer SRAM, which places its ridge point far below it.

| **Accelerator**         | **Year** | **FP16/BF16 Peak** | **FP8 or INT8 Peak** | **Memory** | **Bandwidth** | **TDP**  | **Ridge Point (${I_{\text{ridge}}}$)** |
|:------------------------|:--------:|:------------------:|:--------------------:|:----------:|:-------------:|:--------:|:--------------------------------------:|
| **NVIDIA V100**         |   2017   |    125 TFLOP/s     |          —           |   32 GB    |   900 GB/s    |  300 W   |            138.9 FLOP/byte             |
| **NVIDIA T4**           |   2018   |     65 TFLOP/s     |   130 TOPS (INT8)    |   16 GB    |   320 GB/s    |   70 W   |            203.1 FLOP/byte             |
| **NVIDIA A100**         |   2020   |    312 TFLOP/s     |   624 TOPS (INT8)    |   80 GB    |  2,039 GB/s   |  400 W   |            153.0 FLOP/byte             |
| **NVIDIA H100**         |   2022   |    989 TFLOP/s     | 1,979 TFLOP/s (FP8)  |   80 GB    |  3,350 GB/s   |  700 W   |            295.2 FLOP/byte             |
| **NVIDIA H200**         |   2023   |    989 TFLOP/s     | 1,979 TFLOP/s (FP8)  |   141 GB   |  4,800 GB/s   |  700 W   |            206.0 FLOP/byte             |
| **NVIDIA B200**         |   2024   |   2,250 TFLOP/s    | 4,500 TFLOP/s (FP8)  |   180 GB   |  8,000 GB/s   | 1,000 W  |            281.2 FLOP/byte             |
| **AMD Instinct MI300X** |   2023   |   1,307 TFLOP/s    | 2,614 TFLOP/s (FP8)  |   192 GB   |  5,300 GB/s   |  750 W   |            246.6 FLOP/byte             |
| **Intel Gaudi 2**       |   2022   |    432 TFLOP/s     |  865 TFLOP/s (FP8)   |   96 GB    |  2,450 GB/s   |  600 W   |            176.3 FLOP/byte             |
| **Intel Gaudi 3**       |   2024   |   1,835 TFLOP/s    | 1,835 TFLOP/s (FP8)  |   128 GB   |  3,700 GB/s   |  900 W   |            495.9 FLOP/byte             |
| **Google TPU v1**       |   2017   |         —          |    92 TOPS (INT8)    |    8 GB    |    34 GB/s    |   75 W   |        2,705.9 FLOP/byte (INT8)        |
| **Google TPU v2**       |   2017   |     46 TFLOP/s     |          —           |   16 GB    |   700 GB/s    |  280 W   |             65.7 FLOP/byte             |
| **Google TPU v3**       |   2018   |    123 TFLOP/s     |          —           |   32 GB    |   900 GB/s    |  450 W   |            136.7 FLOP/byte             |
| **Google TPU v4**       |   2021   |    275 TFLOP/s     |          —           |   32 GB    |  1,200 GB/s   |  200 W   |            229.2 FLOP/byte             |
| **Google TPU v5p**      |   2023   |    459 TFLOP/s     |   918 TOPS (INT8)    |   95 GB    |  2,760 GB/s   |  300 W   |            166.3 FLOP/byte             |
| **Google TPU v6e**      |   2024   |    918 TFLOP/s     |          —           |   32 GB    |  1,638 GB/s   |  300 W   |            560.4 FLOP/byte             |
| **Cerebras WSE-3**      |   2024   |  125,000 TFLOP/s   |          —           | 44 GB SRAM |    21 PB/s    | 23,000 W |             6.0 FLOP/byte              |

Table 3: **Master Accelerator Specification Matrix**: Dense peak throughput, memory capacity and bandwidth, TDP, and FP16 ridge point (${I_{\text{ridge}}}$ = peak FP16 throughput divided by memory bandwidth) for each accelerator the book cites, read from the hardware registry. The FP8 or INT8 column gives each chip’s dense low-precision peak where the registry lists one; TPU v1’s ridge point uses its INT8 peak because it has no floating-point path. Memory is the vendor nameplate capacity.

^tbl-appdx-assumptions-accelerator-matrix

### NVIDIA H100 (Reference Machine)

^sec-appdx-assumptions-h100-reference-machine-2b6f

The NVIDIA H100 is the default accelerator for the book’s training and serving calculations, supplying a single baseline for peak FLOP/s, high-bandwidth memory (HBM) bandwidth, and capacity across chapters. It pairs Hopper-generation FP8 Tensor Cores and the Transformer Engine with HBM3 memory ([[05 Reference/Volume I - Foundations/V1 System Assumptions#^ref-choquette2023|Choquette 2023]]) ([[05 Reference/Volume I - Foundations/V1 System Assumptions#^tbl-assumptions-h100|table 4]]).

| **Assumption**                                    | **Value**        |
|:--------------------------------------------------|:-----------------|
| **Release year**                                  | 2022             |
| **Peak FP16/BF16 tensor throughput (dense)**      | 989 TFLOP/s      |
| **Peak FP16/BF16 tensor throughput (2:4 sparse)** | 1,979 TFLOP/s    |
| **Peak FP8 tensor throughput (dense)**            | 1,979 TFLOP/s    |
| **Peak INT8 tensor throughput (dense)**           | 1,979 TOPS       |
| **Peak TF32 tensor throughput (dense)**           | 494.5 TFLOP/s    |
| **Peak FP32 throughput (CUDA cores)**             | 67 TFLOP/s       |
| **HBM3 capacity (nameplate)**                     | 80 GB            |
| **HBM3 bandwidth**                                | 3.35 TB/s        |
| **L2 cache**                                      | 50 MB            |
| **Streaming multiprocessors**                     | 132              |
| **NVLink 4.0 bandwidth (bidirectional total)**    | 900 GB/s         |
| **PCIe Gen5 x16 host link (per direction)**       | 64 GB/s          |
| **TDP**                                           | 700 W            |
| **Ridge point, FP16/BF16**                        | 295.2 FLOP/byte  |
| **Ridge point, FP8/INT8**                         | 590.7 FLOP/byte  |
| **List price (approximate)**                      | ~\$25,000–30,000 |

Table 4: **NVIDIA H100 (Hopper), the Reference Machine**: Peak specifications from the Hopper architecture overview and datasheet ([[05 Reference/Volume I - Foundations/V1 System Assumptions#^ref-choquette2023|Choquette 2023]]), as recorded in the hardware registry. Ridge points divide each dense peak by HBM3 bandwidth. The list price is the representative range used in cost-performance examples, not a quote.

^tbl-assumptions-h100

The two ridge points turn these values into a classification. A kernel whose arithmetic intensity exceeds the FP16/BF16 ridge of 295.2 FLOP/byte is compute bound on the H100; one below it is bandwidth bound and runs no faster on a faster datapath. FP8 and INT8 double the peak rate while bandwidth stays fixed, so the ridge rises to 590.7 FLOP/byte and a layer that was compute bound at FP16 can fall below it after quantization. **[[05 Reference/Volume I - Foundations/V1 Machine Foundations#^sec-appdx-machine-foundations-concrete-example-a100-analysis-5b30|A concrete example: The H100 analysis]]** works the roofline example on these values, and **[[01 Books/Volume I - Foundations/03 Optimization/11 Hardware Acceleration/V1-11.07 Performance Bounds#^sec-hardware-acceleration-roofline-model-42ff|Performance Bounds]]** develops the regimes.

### NVIDIA V100

^sec-appdx-assumptions-v100-1f5e

The Volta-generation V100 ([[05 Reference/Volume I - Foundations/V1 System Assumptions#^tbl-assumptions-v100|table 5]]) introduced Tensor Cores and is the accelerator of the GPT-3 training run that the book’s cost and energy examples reconstruct. Its HBM2 bandwidth and power envelope serve as the early-generation baseline against which Ampere, Hopper, and Blackwell gains are measured.

| **Assumption**                         | **Value** | **Unit** |
|:---------------------------------------|:---------:|:--------:|
| **Peak FP16 tensor throughput (V100)** |    125    | TFLOP/s  |
| **Peak FP32 throughput (V100)**        |   15.7    | TFLOP/s  |
| **HBM bandwidth (V100)**               |    900    |   GB/s   |
| **HBM capacity (V100)**                |    32     |    GB    |
| **TDP (V100)**                         |    300    |    W     |

Table 5: **NVIDIA V100 (Volta)**: Peak specs from NVIDIA’s architecture whitepaper and product datasheet ([[05 Reference/Volume I - Foundations/V1 System Assumptions#^ref-nvidia2017gpu|NVIDIA Corporation 2017]], [[05 Reference/Volume I - Foundations/V1 System Assumptions#^ref-nvidia2020v100datasheet|2020b]]). The V100 anchors baseline-generation comparisons.

^tbl-assumptions-v100

### NVIDIA T4

^sec-appdx-assumptions-t4-8b2c

Low-power inference comparisons use the Turing-generation T4 as their baseline ([[05 Reference/Volume I - Foundations/V1 System Assumptions#^tbl-assumptions-t4|table 6]]). Because the card fits within a low-power PCIe slot envelope without auxiliary power connectors, it anchors cost-per-query and edge-server comparisons across the serving chapters.

| **Assumption**                       | **Value** | **Unit** |
|:-------------------------------------|:---------:|:--------:|
| **Peak FP16 tensor throughput (T4)** |    65     | TFLOP/s  |
| **Peak INT8 throughput (T4)**        |    130    |   TOPS   |
| **Memory bandwidth (T4)**            |    320    |   GB/s   |
| **TDP (T4)**                         |    70     |    W     |

Table 6: **NVIDIA T4 (Turing)**: Peak specs from NVIDIA Tesla T4 product documentation ([[05 Reference/Volume I - Foundations/V1 System Assumptions#^ref-nvidia2018t4|NVIDIA Corporation 2018]]). Its low TDP makes this inference accelerator a useful cost-per-inference anchor.

^tbl-assumptions-t4

### NVIDIA A100

^sec-appdx-assumptions-a100-5d97

The Ampere-generation A100 ([[05 Reference/Volume I - Foundations/V1 System Assumptions#^tbl-assumptions-a100|table 7]]) preceded the reference machine, and dated comparisons across generations use its values. It introduced TF32 and BF16 Tensor Cores alongside the HBM2e capacity tier that the H100 retained.

| **Assumption**                         | **Value** | **Unit** |
|:---------------------------------------|:---------:|:--------:|
| **Peak FP16 tensor throughput (A100)** |    312    | TFLOP/s  |
| **Peak FP32 throughput (A100)**        |   19.5    | TFLOP/s  |
| **Peak INT8 throughput (A100)**        |    624    |   TOPS   |
| **Peak TF32 throughput (A100)**        |    156    | TFLOP/s  |
| **HBM bandwidth (A100)**               |   2039    |   GB/s   |
| **HBM capacity (A100)**                |    80     |    GB    |
| **TDP (A100)**                         |    400    |    W     |

Table 7: **NVIDIA A100 (Ampere)**: Peak specs from NVIDIA’s architecture whitepaper, 80 GB datasheet, and architecture article ([[05 Reference/Volume I - Foundations/V1 System Assumptions#^ref-NVIDIA2020|NVIDIA Corporation 2020a]], [[05 Reference/Volume I - Foundations/V1 System Assumptions#^ref-nvidia2021a10080gb|2021]]; [[05 Reference/Volume I - Foundations/V1 System Assumptions#^ref-choquette2021|Choquette et al. 2021]]). Ampere introduced TF32 Tensor Cores and the HBM capacity point that the H100 kept, with HBM3 in place of HBM2e.

^tbl-assumptions-a100

### NVIDIA B200

^sec-appdx-assumptions-b200-9e14

Forward-looking capacity-planning examples rely on Blackwell-generation specs ([[05 Reference/Volume I - Foundations/V1 System Assumptions#^tbl-assumptions-b200|table 8]]). Its HBM3e bandwidth and native FP4 and FP8 Tensor Core rates show how memory capacity, bandwidth, and power continue to scale past Hopper.

| **Assumption**                         | **Value** | **Unit** |
|:---------------------------------------|:---------:|:--------:|
| **Peak FP16 tensor throughput (B200)** |   2250    | TFLOP/s  |
| **Peak FP8 tensor throughput (B200)**  |   4500    | TFLOP/s  |
| **Peak FP4 throughput (B200)**         |   9000    | TFLOP/s  |
| **HBM bandwidth (B200)**               |     8     |   TB/s   |
| **HBM capacity (B200)**                |    180    |    GB    |
| **TDP (B200)**                         |   1000    |    W     |

Table 8: **NVIDIA B200 (Blackwell)**: Peak specs from NVIDIA Blackwell product documentation ([[05 Reference/Volume I - Foundations/V1 System Assumptions#^ref-nvidia2024blackwell|NVIDIA Corporation 2024]]). Forward-looking capacity-planning examples use its HBM3e bandwidth and FP8 throughput.

^tbl-assumptions-b200

### AMD Instinct MI300X

^sec-appdx-assumptions-mi300x-46ac

The MI300X capacity, bandwidth, throughput, and power specifications give a cross-vendor comparison with the H100 used elsewhere ([[05 Reference/Volume I - Foundations/V1 System Assumptions#^tbl-assumptions-mi300x|table 9]]). Its larger HBM3 capacity and memory bandwidth illustrate how an accelerator tuned for memory-bound serving shifts the single-device capacity ceiling.

| **Assumption**                           | **Value** | **Unit** |
|:-----------------------------------------|:---------:|:--------:|
| **Peak FP16 tensor throughput (MI300X)** |   1307    | TFLOP/s  |
| **HBM bandwidth (MI300X)**               |    5.3    |   TB/s   |
| **HBM capacity (MI300X)**                |    192    |    GB    |
| **TDP (MI300X)**                         |    750    |    W     |

Table 9: **AMD Instinct MI300X**: Peak specs from AMD Instinct MI300X product documentation ([[05 Reference/Volume I - Foundations/V1 System Assumptions#^ref-amd2023mi300x|AMD 2023]]). Its HBM capacity and bandwidth make it a cross-vendor baseline for bandwidth-bound and capacity-bound workloads.

^tbl-assumptions-mi300x

### Google TPU V4, V5p, and V6e

^sec-appdx-assumptions-tpu-0c83

When comparing training economics across accelerator families, TPUs, Google’s custom application-specific integrated circuit (ASIC) accelerators, offer the main alternative to GPUs ([[05 Reference/Volume I - Foundations/V1 System Assumptions#^tbl-assumptions-tpuv4|table 10]]). Each chip couples its systolic arrays to HBM and to neighboring chips over the Inter-Chip Interconnect (ICI), the TPU counterpart of NVLink.

| **Assumption**                   | **TPU v4**  | **TPU v5p** | **TPU v6e** |
|:---------------------------------|:------------|:------------|:------------|
| **Peak BF16 throughput**         | 275 TFLOP/s | 459 TFLOP/s | 918 TFLOP/s |
| **Peak INT8 throughput**         | —           | 918 TOPS    | —           |
| **HBM capacity**                 | 32 GB       | 95 GB       | 32 GB       |
| **HBM bandwidth**                | 1,200 GB/s  | 2,760 GB/s  | 1,638 GB/s  |
| **On-chip vector memory (VMEM)** | —           | 128 MB      | —           |
| **ICI bandwidth**                | 300 GB/s    | 1,200 GB/s  | 800 GB/s    |
| **TDP**                          | 200 W       | 300 W       | 300 W       |

Table 10: **Google TPU v4, v5p, and v6e (Trillium)**: TPU v4 values come from Google TPU publications ([[05 Reference/Volume I - Foundations/V1 System Assumptions#^ref-jouppi2023|Jouppi et al. 2023]]), TPU v6e values from Google Cloud’s Trillium specification page ([[05 Reference/Volume I - Foundations/V1 System Assumptions#^ref-googleCloudTpuV6eDocs|Google Cloud 2026]]), and TPU v5p values from Google Cloud’s v5p specification as recorded in the hardware registry. ICI bandwidth for v5p and v6e is the bidirectional total per chip.

^tbl-assumptions-tpuv4

### CPU and Mobile/Edge Processors

^sec-appdx-assumptions-cpu-mobile-edge-d2f9

Edge and mobile ML examples rely on a different performance baseline ([[05 Reference/Volume I - Foundations/V1 System Assumptions#^tbl-assumptions-cpu-mobile|table 11]]), well below data center throughput. The microcontroller rows describe the ESP32-S3, the board on which the book’s keyword-spotting examples run.

| **Assumption**                               | **Value** | **Unit** |
|:---------------------------------------------|:---------:|:--------:|
| **Peak FP32 throughput (reference CPU)**     |     1     | TFLOP/s  |
| **DRAM bandwidth (reference server)**        |    50     |   GB/s   |
| **Reference NPU throughput (iPhone 15 Pro)** |    35     |   TOPS   |
| **Memory bandwidth (iPhone 15 Pro)**         |   51.2    |   GB/s   |
| **TDP (mobile device, reference)**           |     5     |    W     |
| **Power (edge object detector, reference)**  |     2     |    W     |
| **Battery capacity (phone, reference)**      |    15     |    Wh    |
| **On-chip SRAM (microcontroller, ESP32-S3)** |    520    |   KiB    |
| **TDP (microcontroller, ESP32-S3)**          |    0.4    |    W     |

Table 11: **CPU, Mobile NPU, Edge, and Microcontroller Specs**: Illustrative reference points for edge, mobile, and microcontroller examples (not vendor peaks for a single SKU, except the ESP32-S3 rows). The contrast with data-center accelerators shows why deployment target shapes every design decision.

^tbl-assumptions-cpu-mobile

### Precision Support by Generation

^sec-appdx-assumptions-precision-support-6e3a

Tensor Core format support widened with each NVIDIA generation from Volta through Ampere ([[05 Reference/Volume I - Foundations/V1 System Assumptions#^tbl-nvidia-numerics|table 12]]). Volta supported little below FP16. Ampere introduced TF32, which combines the exponent range of FP32 with the mantissa width of FP16 ([[05 Reference/Volume I - Foundations/V1 System Assumptions#^ref-nvidia-tf32-2b878de3|NVIDIA 2020]]), alongside broader support for BF16, INT8, and INT4 ([[05 Reference/Volume I - Foundations/V1 System Assumptions#^ref-nvidia2017gpu|NVIDIA Corporation 2017]], [[05 Reference/Volume I - Foundations/V1 System Assumptions#^ref-nvidia2018t4|2018]], [[05 Reference/Volume I - Foundations/V1 System Assumptions#^ref-NVIDIA2020|2020a]]). Later generations narrow the formats further, with FP8 on Hopper and FP4 on Blackwell ([[05 Reference/Volume I - Foundations/V1 System Assumptions#^tbl-assumptions-h100|table 4]]; [[05 Reference/Volume I - Foundations/V1 System Assumptions#^tbl-assumptions-b200|table 8]]). **[[01 Books/Volume I - Foundations/03 Optimization/11 Hardware Acceleration/V1-11.05 Compute Units#^sec-hardware-acceleration-precision-tradeoffs-8fa8|Precision trade-offs]]** explains why each narrower format raises peak throughput on the same silicon.

| **Architecture** | **Year** | **Tensor Core Formats**            | **CUDA Core Formats**        |
|:-----------------|:--------:|:-----------------------------------|:-----------------------------|
| **Volta**        |   2017   | FP16                               | FP64, FP32, FP16             |
| **Turing**       |   2018   | FP16, INT8, INT4, INT1             | FP64, FP32, FP16, INT8       |
| **Ampere**       |   2020   | FP64, TF32, BF16, FP16, INT8, INT4 | FP64, FP32, FP16, BF16, INT8 |

Table 12: **Precision Support Evolution**: From Volta through Ampere, Tensor Core support expanded from FP16 to TF32, BF16, and integer formats, broadening the precision choices available to training and inference; the CUDA-core column shows the separate scalar/vector formats each generation supports.

^tbl-nvidia-numerics

### Advertised Peak Throughput Across Generations

^sec-appdx-assumptions-advertised-peak-a7c5

Advertised single-chip GPU throughput rose by more than three orders of magnitude across the generations plotted in [[05 Reference/Volume I - Foundations/V1 System Assumptions#^fig-ai-performance|figure 1]], which combine architectural scaling with lower numerical precisions and structured sparsity ([[05 Reference/Volume I - Foundations/V1 System Assumptions#^ref-nvidia2017gpu|NVIDIA Corporation 2017]], [[05 Reference/Volume I - Foundations/V1 System Assumptions#^ref-NVIDIA2020|2020a]], [[05 Reference/Volume I - Foundations/V1 System Assumptions#^ref-nvidia2024blackwell|2024]]; [[05 Reference/Volume I - Foundations/V1 System Assumptions#^ref-choquette2023|Choquette 2023]]). Because the points mix precision formats, combine FLOP/s with INT8 operations per second, and assume structured sparsity for the A100, H100, and B200, they do not measure one consistent quantity. Instead, the curve compares each generation’s most prominent advertised path rather than same-precision application performance. [[05 Reference/Volume I - Foundations/V1 System Assumptions#^tbl-appdx-assumptions-accelerator-matrix|Table 3]] gives the same chips’ dense, precision-specific peaks, bandwidths, and power limits.

![[90 Assets/Volume I/Shared Figures/Generated Figure b813ac03b5.svg]]

Figure 1: **Advertised GPU Peak Capability Across Generations**: Single-chip values are plotted on a logarithmic axis. The precision label at each point matters because the curve does not measure same-precision scaling. The series follows Dally ([[05 Reference/Volume I - Foundations/V1 System Assumptions#^ref-dally2023|2023]]; [[05 Reference/Volume I - Foundations/V1 System Assumptions#^ref-nvidia2017gpu|NVIDIA Corporation 2017]], [[05 Reference/Volume I - Foundations/V1 System Assumptions#^ref-NVIDIA2020|2020a]], [[05 Reference/Volume I - Foundations/V1 System Assumptions#^ref-nvidia2024blackwell|2024]]; [[05 Reference/Volume I - Foundations/V1 System Assumptions#^ref-choquette2023|Choquette 2023]]).

^fig-ai-performance

### Accelerator Cost Worksheet

^sec-appdx-assumptions-accelerator-cost-worksheet-3f02

Dividing an accelerator’s acquisition price by its advertised peak throughput gives a quick price-per-TFLOP/s baseline, but comparing that ratio across generations misleads when the peaks use different precision modes or when memory bandwidth limits execution before compute does ([[05 Reference/Volume I - Foundations/V1 System Assumptions#^tbl-accelerator-economics|table 13]]). List prices also vary across vendor, region, contract terms, and procurement volume, and the throughput rows in the worksheet use distinct numerical precision modes. The resulting price-per-peak-operation ratio is therefore meaningful within a single row, where it shows how a price assumption enters the arithmetic, rather than as a cross-device ranking. **[[01 Books/Volume I - Foundations/03 Optimization/11 Hardware Acceleration/V1-11.12 Choosing an Accelerator#^sec-hardware-acceleration-costperformance-analysis-e925|Cost-performance analysis]]** states the durable rule the worksheet supports, which divides cost by the throughput a workload delivers on its limiting resource rather than by the advertised peak.

| **Accelerator** |  **List Price**  | **Representative Peak (precision shown)** | **Memory Bandwidth** | **Price per Peak TFLOP/s** |
|:----------------|:----------------:|:-----------------------------------------:|:--------------------:|:--------------------------:|
| **NVIDIA V100** |    ~\$10,000     |            125 TFLOP/s (FP16)             |       900 GB/s       |       \$80/(TFLOP/s)       |
| **NVIDIA A100** |    ~\$15,000     |            312 TFLOP/s (FP16)             |      2,039 GB/s      |      \$48.1/(TFLOP/s)      |
| **NVIDIA H100** | ~\$25,000–30,000 |           494.5 TFLOP/s (TF32)            |      3,350 GB/s      |     ~\$50.6/(TFLOP/s)      |

Table 13: **Illustrative Accelerator Cost Worksheet**: Each row divides an approximate acquisition-price assumption by the representative peak mode shown. Because precision, sparsity assumptions, and price sources differ, the ratios are not comparable as workload performance. Total cost also includes utilization, memory capacity, power, cooling, interconnect, software, and infrastructure.

^tbl-accelerator-economics

## Model Specifications

^sec-appdx-assumptions-model-specifications-b8e7

Hardware ceilings only become bottlenecks when paired with a workload’s parameter count, operation budget, and working-set footprint: the same H100 that is compute-bound on a 256-image ResNet-50 training step becomes bandwidth-bound on single-sequence language-model decode and capacity-bound on a 100 GB recommendation table. Pairing the book’s recurring models with the hardware baselines of [[05 Reference/Volume I - Foundations/V1 System Assumptions#^sec-appdx-assumptions-accelerator-specifications-7a21|section 1.2]] fixes both the operational regime of each lighthouse workload and the parameter counts, inference FLOPs, and training-scale anchors that the chapters plug into their estimates.

### Lighthouse Workloads

^sec-appdx-assumptions-lighthouse-workloads-5c19

Five lighthouse workloads recur through the book, each introduced in the regime it typifies (**[[01 Books/Volume I - Foundations/00 Introduction/01 Introduction/V1-01.08 Iron Law of ML Systems#^sec-introduction-lighthouse-models-9b1c|Lighthouse models put the iron law into practice]]**; **[[01 Books/Volume I - Foundations/01 Foundations/02 System Paradigms/V1-02.04 Analyzing Workloads#^sec-ml-systems-workload-archetypes-fd10|Workload archetypes]]**). A regime belongs to a workload on a machine rather than to a model name. Each row of [[05 Reference/Volume I - Foundations/V1 System Assumptions#^tbl-appdx-assumptions-lighthouses|table 14]] is therefore keyed by model, phase, and batch, with the second GPT-2 XL row recording a crossing out of the model’s home regime. Across those rows, four regimes appear. Compute-bound and bandwidth-bound workloads are separated by the roofline’s ridge point. Capacity-bound and power-bound workloads are constrained before either time term applies, because the working set must fit in memory and the energy budget must cover the run. For the compute- and bandwidth-bound rows, the last column compares the time a step spends on arithmetic at peak FP16 throughput with the time it spends reading the weights once at peak HBM bandwidth on one H100. Whichever time is larger names the regime. A fifth regime, overhead-bound, arises when the iron law’s fixed latency term dominates, and it belongs to a deployment choice such as batch-one serving rather than to a lighthouse (**[[05 Reference/Volume I - Foundations/V1 The D·A·M Taxonomy#^sec-appdx-dam-taxonomy-case-2-latency-cliff-algorithm-8ee2|Case 2: The latency cliff (cross-axis)]]**).

| **Lighthouse**   | **Phase**                   | **Batch**                    | **Machine** | **Regime**                       | **Limiting Resource**                      | **What Sets the Regime**                                                                           |
|:-----------------|:----------------------------|:-----------------------------|:------------|:---------------------------------|:-------------------------------------------|:---------------------------------------------------------------------------------------------------|
| **ResNet-50**    | Training                    | 256 images                   | H100        | Compute-bound                    | Tensor throughput                          | 6.4 ms of arithmetic against 15.3 μs of weight reads per step                                      |
| **MobileNetV2**  | Inference                   | 1 image                      | Phone NPU   | Compute-bound (efficient regime) | Arithmetic within a phone’s power envelope | 17.1 μs of arithmetic at the NPU’s 35 TOPS peak, inside a 5 W device envelope                      |
| **GPT-2 XL**     | Decode                      | 1 sequence                   | H100        | Bandwidth-bound                  | HBM bandwidth                              | 3.0 μs of arithmetic against 0.90 ms of weight reads per token                                     |
| **GPT-2 XL**     | Training                    | 32 sequences of 1,024 tokens | H100        | Compute-bound (crossing)         | Tensor throughput                          | 298.2 ms of arithmetic against 0.90 ms of weight reads per step                                    |
| **Llama 3 8B**   | Decode, 8,192-token context | 1 sequence                   | H100        | Bandwidth-bound                  | HBM bandwidth and KV-cache capacity        | 5.1 ms reading 16.1 GB of weights and 1.07 GB of KV cache, against 16.2 μs of arithmetic per token |
| **DLRM**         | Inference                   | Any                          | H100        | Capacity-bound                   | Memory capacity                            | 100 GB of embedding tables against 80 GB of HBM                                                    |
| **KWS (DS-CNN)** | Inference                   | 1 audio window               | ESP32-S3    | Power-bound                      | Energy per inference                       | 200 KB INT8 model in 520 KB of SRAM, on a board drawing 50 mW to 1.2 W                             |

Table 14: **Lighthouse Workloads by Model, Phase, and Batch**: Each row’s regime on its machine, with the registry quantities that set it. Times are idealized lower bounds at peak FP16 throughput and peak HBM bandwidth of one H100 (the phone NPU’s INT8 peak for MobileNetV2); activation traffic is excluded, so the comparison establishes a regime only where the two times differ by orders of magnitude. Training costs about three forward passes, and decode costs two FLOPs per parameter per token.

^tbl-appdx-assumptions-lighthouses

The same model changes regime when phase or batch changes. GPT-2 XL streams every weight to produce one decode token, but a training step amortizes one weight read over tens of thousands of tokens and becomes arithmetic-dominated. Llama 3 8B’s KV cache adds bytes to every decode step as the context grows. **[[01 Books/Volume I - Foundations/03 Optimization/11 Hardware Acceleration/V1-11.07 Performance Bounds#^sec-hardware-acceleration-roofline-model-42ff|Performance Bounds]]** places these workloads on the H100 roofline, **[[01 Books/Volume I - Foundations/02 Development/06 Network Architectures/V1-06.08 Transformers Parallel Sequence Processing#^sec-network-architectures-inference-memory-bandwidth-wall-98d1|Autoregressive decoding]]** sizes the KV cache that makes decode bandwidth bound, and **[[01 Books/Volume I - Foundations/04 Deployment/13 Model Serving/V1-13.10 LLM Serving#^sec-model-serving-memory-kv-cache-d1ea|Memory and KV cache]]** budgets that cache against serving capacity.

### Reference Model Specifications

^sec-appdx-assumptions-reference-models-e2d4

Parameter counts, per-inference FLOP budgets, and published training-scale anchors form the **reference model assumptions** behind training-cost, memory-footprint, and inference-workload examples ([[05 Reference/Volume I - Foundations/V1 System Assumptions#^tbl-assumptions-models|table 15]]). Published model sizes follow primary papers, model reports, and official documentation ([[05 Reference/Volume I - Foundations/V1 System Assumptions#^ref-devlin2019|Devlin et al. 2019]]; [[05 Reference/Volume I - Foundations/V1 System Assumptions#^ref-radford2019language|Radford et al. 2019]]; [[05 Reference/Volume I - Foundations/V1 System Assumptions#^ref-brown2020language|Brown et al. 2020]]; [[05 Reference/Volume I - Foundations/V1 System Assumptions#^ref-dubey2024llama|Dubey et al. 2024]]; [[05 Reference/Volume I - Foundations/V1 System Assumptions#^ref-he2016|He et al. 2016]]; [[05 Reference/Volume I - Foundations/V1 System Assumptions#^ref-sandler2018|Sandler et al. 2018]]; [[05 Reference/Volume I - Foundations/V1 System Assumptions#^ref-ultralytics2023yolov8Docs|Ultralytics 2023]]; [[05 Reference/Volume I - Foundations/V1 System Assumptions#^ref-naumov2019deep|Naumov et al. 2019]]; [[05 Reference/Volume I - Foundations/V1 System Assumptions#^ref-banbury2021mlperf|Banbury et al. 2021]]). The inference FLOP budgets, by contrast, are book-derived from sequence length 128 for BERT-Base, $224{\times}224$ images for ResNet-50 and MobileNetV2, and $640{\times}640$ images for YOLOv8-Nano, counting two FLOPs per multiply-add in the vision models. For large-scale training anchors, GPT-3 training FLOPs follow ([[05 Reference/Volume I - Foundations/V1 System Assumptions#^ref-brown2020language|Brown et al. 2020]]), while its duration and accelerator count come from the published carbon reconstruction ([[05 Reference/Volume I - Foundations/V1 System Assumptions#^ref-patterson2021carbon|Patterson et al. 2021]]). Because the GPT-4 technical report does not disclose architecture size, the GPT-4 parameter count and training GPU-days use public third-party mixture of experts (MoE) estimates ([[05 Reference/Volume I - Foundations/V1 System Assumptions#^ref-semianalysisGPT4|Patel and Wong 2023]]). Finally, the DLRM row represents the book’s reference configuration, whose FP32 embedding values exceed one accelerator’s memory, rather than a single production recommender.

| **Assumption**                              |  **Value**  |     **Unit**     |
|:--------------------------------------------|:-----------:|:----------------:|
| **Inference FLOPs (BERT-Base)**             |   2.2e+10   |       flop       |
| **Parameters (BERT-Base)**                  |   1.1e+08   |      param       |
| **Parameters (Llama 3 8B)**                 |  8.03e+09   |      param       |
| **Hidden dimension (GPT-2 XL)**             |    1600     |        \-        |
| **Layers (GPT-2 XL)**                       |     48      |        \-        |
| **Parameters (GPT-2 XL)**                   |   1.5e+09   |      param       |
| **Parameters (GPT-3)**                      |  1.75e+11   |      param       |
| **Reference training duration (GPT-3)**     |    14.8     |        d         |
| **Reference training accelerators (GPT-3)** |   10,000    |    V100 GPUs     |
| **Reference training FLOPs (GPT-3)**        |  3.14e+23   |       flop       |
| **Parameters (GPT-4, public MoE estimate)** |  1.76e+12   |      param       |
| **Reference training GPU-days (GPT-4)**     |   2.5e+06   |     GPU-days     |
| **Inference FLOPs (ResNet-50)**             |   8.2e+09   |       flop       |
| **Parameters (ResNet-50)**                  | 2.5557e+07  |      param       |
| **Inference FLOPs (MobileNetV2)**           |    6e+08    |       flop       |
| **Parameters (MobileNetV2)**                | 3.50487e+06 |      param       |
| **Inference FLOPs (YOLOv8-Nano)**           |   8.7e+09   |       flop       |
| **Embedding table size (DLRM, reference)**  |     100     |        GB        |
| **Embedding values (DLRM, reference)**      |   2.5e+10   | embedding values |
| **Parameters (KWS DS-CNN)**                 |   200000    |      param       |
| **Inference FLOPs (KWS DS-CNN)**            |    2e+07    |       flop       |

Table 15: **Reference Model Specifications**: Parameter counts and FLOP budgets for worked examples, with sources as given in the text above. GPT-4 rows cite ([[05 Reference/Volume I - Foundations/V1 System Assumptions#^ref-openai2023gpt4|OpenAI et al. 2023]]) for the official model family and ([[05 Reference/Volume I - Foundations/V1 System Assumptions#^ref-semianalysisGPT4|Patel and Wong 2023]]) for the public MoE parameter and GPU-day estimates used in this edition.

^tbl-assumptions-models

## Training Memory Conventions

^sec-appdx-assumptions-training-memory-conventions-91b3

Multiplying a model’s parameter count by 2 bytes sizes its BF16 weights for inference, but a full training run must also hold gradients, an FP32 master copy of the weights, and optimizer state in accelerator memory before a single activation is allocated. Training-memory napkin math across the book therefore uses the mixed-precision Adaptive Moment Estimation (Adam) storage model: BF16 weights, BF16 gradients, and FP32 master weights plus Adam first- and second-moment buffers (16 bytes per parameter in total). This is a book convention, not a measured hardware constant. The BF16 data path uses standard BF16 mixed-precision training ([[05 Reference/Volume I - Foundations/V1 System Assumptions#^ref-kalamkar2019|Kalamkar et al. 2019]]), the FP32 master copy of the weights follows earlier FP16 work ([[05 Reference/Volume I - Foundations/V1 System Assumptions#^ref-micikevicius2017mixed|Micikevicius et al. 2018]]; [[05 Reference/Volume I - Foundations/V1 System Assumptions#^ref-nvidia-tensors-fp16-2017-23d257af|NVIDIA 2017]]), and Adam’s first- and second-moment buffers follow ([[05 Reference/Volume I - Foundations/V1 System Assumptions#^ref-kingma2014adam|Kingma and Ba 2015]]). Multiplying the bytes per parameter by the parameter count gives the nonactivation training-state footprint, and [[05 Reference/Volume I - Foundations/V1 System Assumptions#^tbl-assumptions-training-memory|table 16]] lists the per-component byte widths. **[[05 Reference/Volume I - Foundations/V1 Algorithm Foundations#^sec-appdx-algorithm-foundations-true-cost-training-memory-e54e|Training memory]]** derives each component and the activation memory that adds to it, and **[[01 Books/Volume I - Foundations/02 Development/08 Model Training/V1-08.04 Computation and Memory Costs of Training#^sec-model-training-optimization-algorithms-c6a9|Optimizers and their memory]]** applies the convention to the book’s training runs.

| **Assumption**                                 | **Value** | **Unit** |
|:-----------------------------------------------|:---------:|:--------:|
| **Weight/gradient width (BF16)**               |     2     |  bytes   |
| **Master weight width (FP32)**                 |     4     |  bytes   |
| **Master + Adam states per parameter (FP32)**  |    12     |  bytes   |
| **Bytes per parameter (mixed-precision Adam)** |    16     |  bytes   |

Table 16: **Training Memory Conventions**: Per-parameter storage for mixed-precision Adam, 16 bytes before activations. Book convention for napkin math; see ([[05 Reference/Volume I - Foundations/V1 System Assumptions#^ref-nvidia-tensors-fp16-2017-23d257af|NVIDIA 2017]]) for mixed-precision training context.

^tbl-assumptions-training-memory

## Energy Constants

^sec-appdx-assumptions-energy-constants-4a6d

Peak throughput and byte widths bound how fast a chip can run and how much state it holds, whereas **energy assumptions** determine whether that execution is thermally and economically viable at the level of individual operations and memory accesses. Horowitz’s 45 nm arithmetic and 32-bit DRAM estimates ([[05 Reference/Volume I - Foundations/V1 System Assumptions#^ref-horowitz2014|Horowitz 2014]]), together with illustrative book anchors for register and SRAM access, MobileNetV2 inference, and 5G transfer, underpin the book’s efficiency comparisons but are not process-independent. Access energy rises from registers through DRAM, and the arithmetic energy of an add and a multiply falls with operand width ([[05 Reference/Volume I - Foundations/V1 System Assumptions#^tbl-assumptions-energy|table 17]]). The access hierarchy quantifies why data reuse dominates kernel design, and **[[05 Reference/Volume I - Foundations/V1 Machine Foundations#^sec-appdx-machine-foundations-memory-hierarchy-2278|The memory hierarchy]]** explains the physics behind it as ratios that hold across process nodes.

| **Assumption**                               | **Value** |  **Unit**   |
|:---------------------------------------------|:---------:|:-----------:|
| **Register access energy**                   |    0.1    |     pJ      |
| **L1 SRAM access energy**                    |    0.5    |     pJ      |
| **L2 SRAM access energy**                    |     2     |     pJ      |
| **DRAM access energy (32-bit)**              |    640    |     pJ      |
| **DRAM access energy (per byte)**            |    160    |   pJ/byte   |
| **FP32 add energy (45 nm)**                  |    0.9    |   pJ/add    |
| **FP16 add energy (45 nm)**                  |    0.4    |   pJ/add    |
| **INT32 add energy (45 nm)**                 |    0.1    |   pJ/add    |
| **INT8 add energy (45 nm)**                  |   0.03    |   pJ/add    |
| **FP32 multiply energy (45 nm)**             |    3.7    | pJ/multiply |
| **FP16 multiply energy (45 nm)**             |    1.1    | pJ/multiply |
| **INT8 multiply energy (45 nm)**             |    0.2    | pJ/multiply |
| **MobileNetV2 inference energy (reference)** |    0.1    |     mJ      |
| **5G transfer energy per MB**                |    100    |    mJ/MB    |

Table 17: **Energy per Operation and Access**: Arithmetic and 32-bit DRAM estimates use Horowitz’s 45 nm model ([[05 Reference/Volume I - Foundations/V1 System Assumptions#^ref-horowitz2014|Horowitz 2014]]), and the per-byte DRAM row is derived from that estimate. Register, SRAM, MobileNetV2, and 5G rows are illustrative book anchors. The roughly 6,400× gap between a 0.1 pJ register access and a 640 pJ DRAM access explains why data reuse dominates ML kernel optimization.

^tbl-assumptions-energy

The arithmetic rows carry two orderings that hold at every process node. A multiply costs several times an add at the same precision, because multiplier area grows roughly with the square of the operand bit width ${b}$ while an adder grows linearly in it, and both fall as the operand narrows ([[05 Reference/Volume I - Foundations/V1 System Assumptions#^ref-horowitz2014|Horowitz 2014]]; [[05 Reference/Volume I - Foundations/V1 System Assumptions#^ref-dally2021|Dally et al. 2021]]). Newer nodes lower every absolute value in the table, so the 45 nm figures are upper anchors for current silicon, and the orderings, not the absolute values, are what precision and reuse arguments depend on.

## Interconnect and Network Bandwidth

^sec-appdx-assumptions-interconnect-network-bandwidth-7d58

Energy costs operate at the chip level, but real ML systems also move data across interconnects, between accelerators, across racks, and over wide-area networks. These **bandwidth assumptions** apply when chapters reason about gradient synchronization, pipeline bubbles, checkpoint I/O, or cross–data center latency, covering both the tier-by-tier hierarchy within a single H100 node and the link families that connect accelerators, hosts, and racks.

### Latency and Bandwidth by Tier

^sec-appdx-assumptions-latency-bandwidth-tier-c1a2

Access latency rises by five orders of magnitude from a register to an NVMe read, while bandwidth falls from terabytes per second at HBM to single gigabytes per second at local storage ([[05 Reference/Volume I - Foundations/V1 System Assumptions#^tbl-appdx-assumptions-tier-latency|table 18]]). **[[05 Reference/Volume I - Foundations/V1 Machine Foundations#^sec-appdx-machine-foundations-latencies-every-programmer-know-e89f|The latency hierarchy]]** expresses the same tiers as decades and as multiples of a register access, which change more slowly than the values here.

| **Tier**               | **Technology**    | **Latency** | **Bandwidth** |
|:-----------------------|:------------------|:-----------:|:-------------:|
| **Registers**          | Flip-flops        |   0.3 ns    |       —       |
| **L1 cache**           | SRAM              |    1 ns     |       —       |
| **L2 cache**           | SRAM              |    4 ns     |       —       |
| **Accelerator memory** | HBM3 (H100)       |   273 ns    |  3,350 GB/s   |
| **Accelerator link**   | NVLink 4.0 (H100) |   500 ns    |   900 GB/s    |
| **Host link**          | PCIe Gen5 x16     |  1,000 ns   |    64 GB/s    |
| **Host memory**        | DDR4/DDR5         |   100 ns    |    50 GB/s    |
| **Network**            | InfiniBand NDR    |    5 μs     |    50 GB/s    |
| **Local storage**      | NVMe SSD (Gen4)   |   100 μs    |    7 GB/s     |

Table 18: **Latency and Bandwidth by Tier (H100 Node)**: Representative access latency and bandwidth from registers to local storage. Register, L1, and L2 latencies are generic on-chip anchors; the HBM row uses a microbenchmarked Hopper global-memory latency, and the host-memory row a CPU main-memory reference latency. NVLink bandwidth is the bidirectional total; other bandwidths are per direction.

^tbl-appdx-assumptions-tier-latency

### Interconnect Specifications

^sec-appdx-assumptions-interconnect-specifications-0f6b

On the reference node, NVLink runs more than an order of magnitude faster than the PCIe host link, and the host link runs faster than the node’s InfiniBand NDR port ([[05 Reference/Volume I - Foundations/V1 System Assumptions#^tbl-assumptions-interconnect|table 19]]). The boundary a transfer crosses therefore sets its cost before its size does. Every rate is quoted in GB/s for comparison, with the direction convention each vendor uses; a bidirectional total halves for a one-way transfer. NVLink and PCIe rates follow accelerator product documentation ([[05 Reference/Volume I - Foundations/V1 System Assumptions#^ref-nvidia2017gpu|NVIDIA Corporation 2017]], [[05 Reference/Volume I - Foundations/V1 System Assumptions#^ref-NVIDIA2020|2020a]]; [[05 Reference/Volume I - Foundations/V1 System Assumptions#^ref-choquette2023|Choquette 2023]]). The InfiniBand architecture specification anchors the protocol family ([[05 Reference/Volume I - Foundations/V1 System Assumptions#^ref-infiniband2000spec|InfiniBand Trade Association 2000]]), while current high-speed product families and Ethernet roadmaps anchor modern link-rate examples ([[05 Reference/Volume I - Foundations/V1 System Assumptions#^ref-nvidia2026quantumX800|NVIDIA 2026]]; [[05 Reference/Volume I - Foundations/V1 System Assumptions#^ref-ethernetAlliance2025roadmap|Ethernet Alliance 2025]]). **[[01 Books/Volume I - Foundations/03 Optimization/11 Hardware Acceleration/V1-11.06 Memory Systems#^sec-hardware-acceleration-hostaccelerator-communication-bb7a|Host-accelerator communication]]** develops the transfer-time model these rates feed. The speed of light in fiber, which bounds every cross–data center round trip, is a physical constant kept with the other durable values in **[[05 Reference/Volume I - Foundations/V1 Machine Foundations#^sec-appdx-machine-foundations-numbers-know-b531|Numbers to Know]]**.

| **Link**                      | **Device or Generation** | **Bandwidth** | **Convention**      | **Latency** |
|:------------------------------|:-------------------------|:-------------:|:--------------------|:-----------:|
| **PCIe Gen3 x16**             | Host link (V100)         |  15.75 GB/s   | Per direction       |      —      |
| **PCIe Gen4 x16**             | Host link (A100)         |    32 GB/s    | Per direction       |      —      |
| **PCIe Gen5 x16**             | Host link (H100, B200)   |    64 GB/s    | Per direction       |  1,000 ns   |
| **CXL memory over PCIe Gen5** | Memory expansion         |    64 GB/s    | Per direction       |      —      |
| **NVLink 2.0**                | V100                     |   300 GB/s    | Bidirectional total |   500 ns    |
| **NVLink 3.0**                | A100                     |   600 GB/s    | Bidirectional total |   500 ns    |
| **NVLink 4.0**                | H100                     |   900 GB/s    | Bidirectional total |   500 ns    |
| **NVLink 5.0**                | B200                     |  1,800 GB/s   | Bidirectional total |   500 ns    |
| **ICI**                       | TPU v4                   |   300 GB/s    | Per direction       |      —      |
| **ICI**                       | TPU v5p                  |  1,200 GB/s   | Bidirectional total |      —      |
| **ICI**                       | TPU v6e                  |   800 GB/s    | Bidirectional total |      —      |
| **InfiniBand EDR**            | Network port             |   12.5 GB/s   | Per direction       |      —      |
| **InfiniBand HDR**            | Network port             |    25 GB/s    | Per direction       |    7 μs     |
| **InfiniBand NDR**            | Network port             |    50 GB/s    | Per direction       |    5 μs     |
| **InfiniBand XDR**            | Network port             |   100 GB/s    | Per direction       |    5 μs     |
| **RoCE (100 GbE)**            | Network port             |   12.5 GB/s   | Per direction       |    10 μs    |
| **RoCE (400 GbE)**            | Network port             |    50 GB/s    | Per direction       |    10 μs    |
| **10 GbE**                    | Network port             |   1.25 GB/s   | Per direction       |    50 μs    |
| **100 GbE**                   | Network port             |   12.5 GB/s   | Per direction       |    50 μs    |
| **400 GbE**                   | Network port             |    50 GB/s    | Per direction       |    50 μs    |
| **800 GbE**                   | Network port             |   100 GB/s    | Per direction       |    50 μs    |
| **NVMe SSD (Gen3)**           | Local storage            |   3.5 GB/s    | Sequential read     |      —      |
| **NVMe SSD (Gen4)**           | Local storage            |    7 GB/s     | Sequential read     |      —      |
| **NVMe SSD (Gen5)**           | Local storage            |    14 GB/s    | Sequential read     |      —      |

Table 19: **Interconnect Specifications**: Link-family bandwidths from accelerator product documentation, the InfiniBand architecture specification, and current product and roadmap documentation ([[05 Reference/Volume I - Foundations/V1 System Assumptions#^ref-nvidia2017gpu|NVIDIA Corporation 2017]], [[05 Reference/Volume I - Foundations/V1 System Assumptions#^ref-NVIDIA2020|2020a]]; [[05 Reference/Volume I - Foundations/V1 System Assumptions#^ref-choquette2023|Choquette 2023]]; [[05 Reference/Volume I - Foundations/V1 System Assumptions#^ref-infiniband2000spec|InfiniBand Trade Association 2000]]; [[05 Reference/Volume I - Foundations/V1 System Assumptions#^ref-nvidia2026quantumX800|NVIDIA 2026]]; [[05 Reference/Volume I - Foundations/V1 System Assumptions#^ref-ethernetAlliance2025roadmap|Ethernet Alliance 2025]]), as recorded in the hardware and systems registries. Network ports are converted from line rate at eight bits per byte. Latencies are representative end-to-end values where the registry records one: a generic NVLink and PCIe hop and a fabric-level network latency.

^tbl-assumptions-interconnect

## Economic Constants

^sec-appdx-assumptions-economic-constants-8c4e

Converting a training run’s megawatt-hours or a dataset’s cross-region transfer volume into dollars requires baseline utility and network rates. These **pricing assumptions** underpin total cost of ownership (TCO) and energy-cost napkin math in [[05 Reference/Volume I - Foundations/V1 System Assumptions#^tbl-assumptions-economic|table 20]]. They are illustrative hyperscaler-order rates for ratio analysis (similar in spirit to carbon accounting examples in ([[05 Reference/Volume I - Foundations/V1 System Assumptions#^ref-patterson2021carbon|Patterson et al. 2021]])), not quotes for a specific region or contract. Local values should replace these anchors when absolute price dominates. Accelerator list prices are kept with each chip, in [[05 Reference/Volume I - Foundations/V1 System Assumptions#^tbl-assumptions-h100|table 4]] and [[05 Reference/Volume I - Foundations/V1 System Assumptions#^tbl-accelerator-economics|table 13]].

| **Assumption**                | **Value** |  **Unit**  |
|:------------------------------|:---------:|:----------:|
| **Cloud electricity price**   |   0.12    | dollar/kWh |
| **Cloud egress price per GB** |   0.09    | dollar/GB  |

Table 20: **Economic Assumptions**: Illustrative cloud electricity and egress rates for TCO napkin math (2024–2025 order of magnitude). On-premise cost structures differ.

^tbl-assumptions-economic

## Scale References

^sec-appdx-assumptions-scale-references-d73a

Per-chip peaks, link bandwidths, and utility prices size a single request or training step, but fleet and storage estimates also depend on the arrival rates and raw sensor volumes that drive total system load: a web service answering billions of queries per day or an autonomous vehicle recording gigabytes of camera and lidar data per hour faces a very different ingestion and serving regime than a small batch pipeline. The **scale assumptions** in [[05 Reference/Volume I - Foundations/V1 System Assumptions#^tbl-assumptions-scale|table 21]] fix illustrative order-of-magnitude baselines for email and search volume, autonomous-vehicle sensor streams, and standard 1080p and 4K video formats. They serve as magnitude anchors rather than audited statistics for a specific year.

| **Assumption**                    | **Value** | **Unit** |
|:----------------------------------|:---------:|:--------:|
| **Gmail emails per day**          | 1.21e+11  |    \-    |
| **Google searches per day**       | 1.37e+10  |    \-    |
| **Waymo sensor data rate (low)**  |     1     |   TB/h   |
| **Waymo sensor data rate (high)** |    19     |   TB/h   |
| **1080p frame width**             |   1920    |    \-    |
| **1080p frame height**            |   1080    |    \-    |
| **4K frame width**                |   3840    |    \-    |
| **4K frame height**               |   2160    |    \-    |
| **Bytes per RGB pixel**           |     3     |  bytes   |
| **Video frame rate (standard)**   |    30     |    Hz    |

Table 21: **Production Scale and Data Rate References**: Illustrative workload and sensor-rate anchors, plus standard 1080p and UHD 4K video parameters.

^tbl-assumptions-scale

## Worked Estimates

^sec-appdx-assumptions-worked-estimates-2e95

A table of peak rates, byte widths, and utility prices does not by itself tell an engineer whether a kernel is bandwidth bound, whether a fine-tuning job fits on one GPU, or what a training run’s electricity bill covers. Three worked templates combine the reference tables of this appendix to answer those performance, capacity, and cost questions in sequence, and each names the section that develops its method so a reader can rerun the calculation with substituted values.

On a single accelerator, the first question is whether arithmetic throughput or memory bandwidth limits execution. Applying the roofline method of **[[05 Reference/Volume I - Foundations/V1 Machine Foundations#^sec-appdx-machine-foundations-roofline-model-2529|The Roofline model]]** to the H100 constants in [[05 Reference/Volume I - Foundations/V1 System Assumptions#^tbl-assumptions-h100|table 4]] separates compute-bound matrix multiplies from bandwidth-bound token generation.

**Napkin Math 1.1: Classify a roofline regime**

**Problem**: For the stated H100 and workload intensities, which operations are compute bound and which are bandwidth bound?

**Variables**: For an H100 at FP16/BF16 peak, use 989 TFLOP/s peak compute and 3.35 TB/s memory bandwidth.

**Math**: Divide peak FLOP/s by memory bandwidth to get the roofline ridge point: 989 TFLOP/s/3.35 TB/s $\approx$ 295.2 FLOP/byte. A large general matrix multiply (GEMM) with ${N}=$ 4096 has intensity ${N}/3 \approx$ 1,365.3 FLOP/byte.

**Result**: Operations above 295.2 FLOP/byte are compute bound; operations below it are bandwidth bound. The GEMM example is compute bound, while a single-token autoregressive decode at FP16, with intensity of about 1 FLOP/byte, is deeply bandwidth bound.

**Systems insight**: The same accelerator can be compute rich and memory constrained. Arithmetic intensity determines which resource the workload actually consumes.

Before a workload can reach either roofline ceiling, its working state must fit in device memory. Combining the Llama 3 8B parameter count ([[05 Reference/Volume I - Foundations/V1 System Assumptions#^tbl-assumptions-models|table 15]]) with the mixed-precision Adam layout ([[05 Reference/Volume I - Foundations/V1 System Assumptions#^tbl-assumptions-training-memory|table 16]]) tests whether full fine-tuning fits on a single H100; **[[05 Reference/Volume I - Foundations/V1 Algorithm Foundations#^sec-appdx-algorithm-foundations-true-cost-training-memory-e54e|Training memory]]** derives the state components, and **[[01 Books/Volume I - Foundations/02 Development/08 Model Training/V1-08.04 Computation and Memory Costs of Training#^sec-model-training-finetuning-memory-one-accelerator-7c2e|Fine-tuning memory on one accelerator]]** shows how parameter-efficient fine-tuning brings the same model onto one accelerator.

**Napkin Math 1.2: Estimate training-state memory**

**Problem**: How much model-state memory is required to fully fine-tune Llama 3 8B with mixed-precision Adam?

**Variables**: Mixed-precision Adam stores BF16 weights, gradients, FP32 master weights, momentum, and variance. The model-state budget is 16 bytes per parameter.

**Math**: For 8.03B parameters, model state is 8.03B $\times$ 16 bytes = 128.5 GB.

**Result**: An H100 has 80 GB of HBM, so the model state alone exceeds a single accelerator before accounting for activations.

**Systems insight**: Optimizer state, not weights alone, sets the floor for training memory. Capacity planning that starts from parameter bytes underestimates the real requirement.

When a training job scales beyond one accelerator to a multi-week cluster run, thermal design power and duration turn hardware utilization into megawatt-hours and utility cost. Multiplying the V100 power envelope ([[05 Reference/Volume I - Foundations/V1 System Assumptions#^tbl-assumptions-v100|table 5]]), the reconstructed GPT-3 cluster duration ([[05 Reference/Volume I - Foundations/V1 System Assumptions#^tbl-assumptions-models|table 15]]), and the cloud electricity rate ([[05 Reference/Volume I - Foundations/V1 System Assumptions#^tbl-assumptions-economic|table 20]]) estimates the accelerator-only electricity bill; **[[05 Reference/Volume I - Foundations/V1 Machine Foundations#^sec-appdx-machine-foundations-dimensional-analysis-76b3|Dimensional analysis]]** verifies that the units of such a product reduce to energy, and **[[01 Books/Volume I - Foundations/04 Deployment/15 Responsible Engineering/V1-15.05 Environmental and Cost Awareness#^sec-responsible-engineering-tco-calculation-methodology-7cb0|Accounting for cost and carbon]]** extends the accounting to total cost and carbon at deployment scale.

**Napkin Math 1.3: Estimate accelerator electricity cost**

**Problem**: What is the accelerator-only electricity cost of the GPT-3 training run?

**Variables**: Use 10,000 V100s, 300 W per accelerator, ~14.8 days wall-clock, and \$0.12/kWh electricity ([[05 Reference/Volume I - Foundations/V1 System Assumptions#^ref-patterson2021carbon|Patterson et al. 2021]]).

**Math**: The run requires roughly $3.14 \times 10^{23}$ FLOPs. The accelerator-only electricity-cost estimate is ~14.8 days wall-clock $\times$ 10,000 V100s $\times$ 24 h/day $\times$ 0.3 kW $\times$ \$0.12/kWh = ~\$127,872.

**Result**: The accelerator-only electricity cost is roughly \$128,000. This TDP-only estimate excludes host CPUs, networking, storage, cooling, and facility overhead. The 1,066 MWh of accelerator energy behind it covers about 83 percent of the 1,287 MWh reported for the run, which also counts host power and data center overhead. The GPU count and duration are a published reconstruction from measured per-GPU throughput, so only their product is firm ([[05 Reference/Volume I - Foundations/V1 System Assumptions#^ref-patterson2021carbon|Patterson et al. 2021]]).

**Systems insight**: Energy follows directly from power and time, while the dollar figure depends on the electricity rate assumed.

## Assumption Provenance

^sec-appdx-assumption-provenance

Those three calculations mix an H100 vendor datasheet ceiling, a book convention for Adam training state, a published reconstruction of the GPT-3 training run, and an illustrative utility rate, and treating all four as interchangeable measurements would misstate what an estimate proves. Each quantitative input in this appendix therefore carries a provenance record that places it in an explicit evidence class alongside its primary references ([[05 Reference/Volume I - Foundations/V1 System Assumptions#^tbl-assumption-provenance-catalog|table 22]]). Vendor specifications and standards define published limits, peer-reviewed measurements provide empirical anchors, and explicitly marked editorial scenarios supply illustrative values where no durable universal constant exists. Every value is read from the book’s hardware, model, systems, and infrastructure registries, which record the same provenance per entry. Checking the evidence class before trusting a number keeps vendor ceilings distinct from empirical anchors and scenario placeholders.

| **Appendix section**            | **Source type**                                                                                                                     | **Primary references**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
|:--------------------------------|:------------------------------------------------------------------------------------------------------------------------------------|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Accelerator specifications**  | Vendor datasheet peaks and list-price ranges; editorial CPU/mobile anchors; release-year format support; advertised marketing peaks | ([[05 Reference/Volume I - Foundations/V1 System Assumptions#^ref-nvidia2017gpu\|NVIDIA Corporation 2017]], [[05 Reference/Volume I - Foundations/V1 System Assumptions#^ref-nvidia2018t4\|2018]], [[05 Reference/Volume I - Foundations/V1 System Assumptions#^ref-NVIDIA2020\|2020a]], [[05 Reference/Volume I - Foundations/V1 System Assumptions#^ref-nvidia2024blackwell\|2024]]; [[05 Reference/Volume I - Foundations/V1 System Assumptions#^ref-nvidia-tf32-2b878de3\|NVIDIA 2020]]; [[05 Reference/Volume I - Foundations/V1 System Assumptions#^ref-choquette2021\|Choquette et al. 2021]]; [[05 Reference/Volume I - Foundations/V1 System Assumptions#^ref-choquette2023\|Choquette 2023]]; [[05 Reference/Volume I - Foundations/V1 System Assumptions#^ref-amd2023mi300x\|AMD 2023]]; [[05 Reference/Volume I - Foundations/V1 System Assumptions#^ref-jouppi2023\|Jouppi et al. 2023]]; [[05 Reference/Volume I - Foundations/V1 System Assumptions#^ref-googleCloudTpuV6eDocs\|Google Cloud 2026]]); editorial for CPU/mobile rows                                                                                                                                                                                                                                                             |
| **Model specifications**        | Published papers, model reports, benchmark references, and official docs; GPT-3 run reconstruction; GPT-4 size from public analysis | ([[05 Reference/Volume I - Foundations/V1 System Assumptions#^ref-devlin2019\|Devlin et al. 2019]]; [[05 Reference/Volume I - Foundations/V1 System Assumptions#^ref-radford2019language\|Radford et al. 2019]]; [[05 Reference/Volume I - Foundations/V1 System Assumptions#^ref-brown2020language\|Brown et al. 2020]]; [[05 Reference/Volume I - Foundations/V1 System Assumptions#^ref-patterson2021carbon\|Patterson et al. 2021]]; [[05 Reference/Volume I - Foundations/V1 System Assumptions#^ref-dubey2024llama\|Dubey et al. 2024]]; [[05 Reference/Volume I - Foundations/V1 System Assumptions#^ref-he2016\|He et al. 2016]]; [[05 Reference/Volume I - Foundations/V1 System Assumptions#^ref-sandler2018\|Sandler et al. 2018]]; [[05 Reference/Volume I - Foundations/V1 System Assumptions#^ref-ultralytics2023yolov8Docs\|Ultralytics 2023]]; [[05 Reference/Volume I - Foundations/V1 System Assumptions#^ref-naumov2019deep\|Naumov et al. 2019]]; [[05 Reference/Volume I - Foundations/V1 System Assumptions#^ref-banbury2021mlperf\|Banbury et al. 2021]]; [[05 Reference/Volume I - Foundations/V1 System Assumptions#^ref-openai2023gpt4\|OpenAI et al. 2023]]; [[05 Reference/Volume I - Foundations/V1 System Assumptions#^ref-semianalysisGPT4\|Patel and Wong 2023]]) |
| **Training memory conventions** | Book convention (mixed-precision Adam layout)                                                                                       | ([[05 Reference/Volume I - Foundations/V1 System Assumptions#^ref-kingma2014adam\|Kingma and Ba 2015]]; [[05 Reference/Volume I - Foundations/V1 System Assumptions#^ref-kalamkar2019\|Kalamkar et al. 2019]]; [[05 Reference/Volume I - Foundations/V1 System Assumptions#^ref-micikevicius2017mixed\|Micikevicius et al. 2018]]; [[05 Reference/Volume I - Foundations/V1 System Assumptions#^ref-nvidia-tensors-fp16-2017-23d257af\|NVIDIA 2017]])                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| **Energy constants**            | Published 45 nm arithmetic/DRAM estimates; add-versus-multiply scaling                                                              | ([[05 Reference/Volume I - Foundations/V1 System Assumptions#^ref-horowitz2014\|Horowitz 2014]]; [[05 Reference/Volume I - Foundations/V1 System Assumptions#^ref-dally2021\|Dally et al. 2021]]) for arithmetic/DRAM; editorial for register/SRAM, MobileNetV2, and 5G rows                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| **Interconnect bandwidth**      | Vendor specs; InfiniBand standard; product and roadmap documentation; representative latency tiers                                  | ([[05 Reference/Volume I - Foundations/V1 System Assumptions#^ref-nvidia2017gpu\|NVIDIA Corporation 2017]], [[05 Reference/Volume I - Foundations/V1 System Assumptions#^ref-NVIDIA2020\|2020a]]; [[05 Reference/Volume I - Foundations/V1 System Assumptions#^ref-choquette2023\|Choquette 2023]]; [[05 Reference/Volume I - Foundations/V1 System Assumptions#^ref-infiniband2000spec\|InfiniBand Trade Association 2000]]; [[05 Reference/Volume I - Foundations/V1 System Assumptions#^ref-nvidia2026quantumX800\|NVIDIA 2026]]; [[05 Reference/Volume I - Foundations/V1 System Assumptions#^ref-ethernetAlliance2025roadmap\|Ethernet Alliance 2025]])                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| **Economic assumptions**        | Illustrative cloud/utility rates                                                                                                    | ([[05 Reference/Volume I - Foundations/V1 System Assumptions#^ref-patterson2021carbon\|Patterson et al. 2021]]) (methodology context)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| **Scale references**            | Illustrative workload rates; standard video conventions                                                                             | Editorial for workload rates; standard format definitions for video                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| **Unit conventions**            | Decimal SI; book notation                                                                                                           | Editorial                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| **Worked estimates**            | Derived from the rows above                                                                                                         | As for the inputs they use                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |

Table 22: **Assumption Provenance Catalog**: Quick map from appendix section to source class and bibliography.

^tbl-assumption-provenance-catalog

## Summary

^sec-appdx-assumptions-summary-6b1f

Back-of-envelope estimates stay comparable across chapters only when they share a single set of unit conventions and dated hardware, model, energy, interconnect, and economic inputs. Because those values come from vendor datasheet peaks, published empirical measurements, interface standards, and editorial scenarios, they carry different evidentiary weight and age at different rates.

Use these tables as starting inputs, not universal constants. For each estimate, record the table row, unit convention, and provenance. Replace time-sensitive peaks, prices, and rates with local values. Distinguish a physical ceiling from a measured operating point and a scenario assumption. Report which assumptions dominate the result. That record keeps napkin math reproducible and makes clear which input controls the conclusion.

Back to top

## Source References

^source-references

Jouppi, Norman P., Doe Hyun Yoon, George Kurian, Sheng Li, Nishant Patil, James Laudon, Cliff Young, and David Patterson. 2020. “A Domain-Specific Supercomputer for Training Deep Neural Networks.” *Communications of the ACM* 63 (7): 67–78. https://doi.org/10.1145/3360307.

^ref-jouppi2020

NVIDIA Corporation. 2020b. *NVIDIA V100 Tensor Core GPU Datasheet*. NVIDIA product documentation.

^ref-nvidia2020v100datasheet

NVIDIA Corporation. 2021. *NVIDIA A100 Tensor Core GPU Datasheet*. NVIDIA product documentation.

^ref-nvidia2021a10080gb

Dally, Bill. 2023. “Hardware for Deep Learning.” *2023 IEEE Hot Chips 35 Symposium (HCS)*, 1–58. https://doi.org/10.1109/hcs59251.2023.10254716.

^ref-dally2023

NVIDIA Corporation. 2017. *NVIDIA Tesla V100 GPU Architecture*. NVIDIA Whitepaper.

^ref-nvidia2017gpu

NVIDIA Corporation. 2018. *NVIDIA Tesla T4 Tensor Core GPU*. NVIDIA product documentation.

^ref-nvidia2018t4

NVIDIA Corporation. 2020a. *NVIDIA A100 Tensor Core GPU Architecture*. NVIDIA Whitepaper, V1.0.

^ref-NVIDIA2020

NVIDIA Corporation. 2024. *NVIDIA Blackwell Architecture*. NVIDIA product documentation.

^ref-nvidia2024blackwell

NVIDIA. 2020. *TensorFloat-32 in the A100 GPU Accelerates AI Training, HPC up to 20x*.

^ref-nvidia-tf32-2b878de3

Choquette, Jack, Wishwesh Gandhi, Olivier Giroux, Nick Stam, and Ronny Krashinsky. 2021. “NVIDIA A100 Tensor Core GPU: Performance and Innovation.” *IEEE Micro* 41 (2): 29–35. https://doi.org/10.1109/mm.2021.3061394.

^ref-choquette2021

Choquette, Jack. 2023. “NVIDIA Hopper H100 GPU: Scaling Performance.” *IEEE Micro* 43 (3): 9–17. https://doi.org/10.1109/mm.2023.3256796.

^ref-choquette2023

AMD. 2023. *AMD Instinct MI300X Accelerators*. AMD product documentation.

^ref-amd2023mi300x

Jouppi, Norm, George Kurian, Sheng Li, Peter Ma, Rahul Nagarajan, Lifeng Nai, Nishant Patil, et al. 2023. “TPU v4: An Optically Reconfigurable Supercomputer for Machine Learning with Hardware Support for Embeddings.” *Proceedings of the 50th Annual International Symposium on Computer Architecture*, 1–14. https://doi.org/10.1145/3579371.3589350.

^ref-jouppi2023

Google Cloud. 2026. *TPU v6e*.

^ref-googleCloudTpuV6eDocs

Devlin, Jacob, Ming-Wei Chang, Kenton Lee, and Kristina Toutanova. 2019. “BERT: Pre-Training of Deep Bidirectional Transformers for Language Understanding.” *Proceedings of the 2019 Conference of the North American Chapter of the Association for Computational Linguistics: Human Language Technologies*, 4171–86. https://doi.org/10.18653/v1/n19-1423.

^ref-devlin2019

Radford, Alec, Jeffrey Wu, Rewon Child, David Luan, Dario Amodei, and Ilya Sutskever. 2019. *Language Models Are Unsupervised Multitask Learners*. OpenAI.

^ref-radford2019language

Brown, Tom B., Benjamin Mann, Nick Ryder, Melanie Subbiah, Jared Kaplan, Prafulla Dhariwal, Arvind Neelakantan, et al. 2020. “Language Models Are Few-Shot Learners.” *Advances in Neural Information Processing Systems* 33: 1877–901. https://doi.org/10.48550/arxiv.2005.14165.

^ref-brown2020language

Patterson, David, Joseph Gonzalez, Quoc Le, Chen Liang, Lluis-Miquel Munguia, Daniel Rothchild, David So, Maud Texier, and Jeff Dean. 2021. “Carbon Emissions and Large Neural Network Training.” *arXiv Preprint arXiv:2104.10350*.

^ref-patterson2021carbon

Dubey, Abhimanyu, Abhinav Jauhri, Abhinav Pandey, Abhishek Kadian, et al. 2024. *The Llama 3 Herd of Models*. arXiv preprint arXiv:2407.21783.

^ref-dubey2024llama

He, Kaiming, Xiangyu Zhang, Shaoqing Ren, and Jian Sun. 2016. “Deep Residual Learning for Image Recognition.” *2016 IEEE Conference on Computer Vision and Pattern Recognition (CVPR)*, 770–78. https://doi.org/10.1109/cvpr.2016.90.

^ref-he2016

Sandler, Mark, Andrew Howard, Menglong Zhu, Andrey Zhmoginov, and Liang-Chieh Chen. 2018. “MobileNetV2: Inverted Residuals and Linear Bottlenecks.” *2018 IEEE/CVF Conference on Computer Vision and Pattern Recognition*, 4510–20. https://doi.org/10.1109/cvpr.2018.00474.

^ref-sandler2018

Ultralytics. 2023. *YOLOv8*.

^ref-ultralytics2023yolov8Docs

Naumov, Maxim, Dheevatsa Mudigere, Hao-Jun Michael Shi, Jianyu Huang, Narayanan Sundaraman, Jongsoo Park, Xiaodong Wang, et al. 2019. “Deep Learning Recommendation Model for Personalization and Recommendation Systems.” *arXiv Preprint arXiv:1906.00091*.

^ref-naumov2019deep

Banbury, Colby, Vijay Janapa Reddi, Peter Torelli, Jeremy Holleman, Nat Jeffries, Csaba Kirber, et al. 2021. “MLPerf Tiny Benchmark.” *Proceedings of the Neural Information Processing Systems Track on Datasets and Benchmarks (NeurIPS)*.

^ref-banbury2021mlperf

OpenAI, Josh Achiam, Steven Adler, Sandhini Agarwal, Lama Ahmad, Ilge Akkaya, Florencia Leoni Aleman, et al. 2023. “GPT-4 Technical Report.” *arXiv Preprint arXiv:2303.08774*, ahead of print. https://doi.org/10.48550/arXiv.2303.08774.

^ref-openai2023gpt4

Patel, Dylan, and Gerald Wong. 2023. *GPT-4 Architecture, Infrastructure, Training Dataset, Costs, Vision, MoE*. SemiAnalysis Blog.

^ref-semianalysisGPT4

Kingma, Diederik P., and Jimmy Ba. 2015. “Adam: A Method for Stochastic Optimization.” *3rd International Conference on Learning Representations (ICLR)*.

^ref-kingma2014adam

Kalamkar, Dhiraj, Dheevatsa Mudigere, Naveen Mellempudi, Dipankar Das, Kunal Banerjee, Sasikanth Avancha, Dharma Teja Vooturi, et al. 2019. *A Study of BFLOAT16 for Deep Learning Training*.

^ref-kalamkar2019

Micikevicius, Paulius, Sharan Narang, Jonah Alben, Gregory Diamos, Erich Elsen, David Garcia, Boris Ginsburg, et al. 2018. “Mixed Precision Training.” *International Conference on Learning Representations (ICLR)*.

^ref-micikevicius2017mixed

NVIDIA. 2017. *Training with Mixed Precision*.

^ref-nvidia-tensors-fp16-2017-23d257af

Horowitz, Mark. 2014. “1.1 Computing’s Energy Problem (and What We Can Do about It).” *2014 IEEE International Solid-State Circuits Conference Digest of Technical Papers (ISSCC)*, 10–14. https://doi.org/10.1109/isscc.2014.6757323.

^ref-horowitz2014

Dally, William J., Stephen W. Keckler, and David B. Kirk. 2021. “Evolution of the Graphics Processing Unit (GPU).” *IEEE Micro* 41 (6): 42–51. https://doi.org/10.1109/mm.2021.3113475.

^ref-dally2021

InfiniBand Trade Association. 2000. *InfiniBand Architecture Specification Volume 1*. InfiniBand Trade Association.

^ref-infiniband2000spec

NVIDIA. 2026. *NVIDIA Quantum-X800 InfiniBand Platform*. NVIDIA product documentation.

^ref-nvidia2026quantumX800

Ethernet Alliance. 2025. *2025 Ethernet Roadmap*. Ethernet Alliance roadmap.

^ref-ethernetAlliance2025roadmap

## Source

[Repository Source](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/books/vol1/backmatter/appendix_assumptions.qmd) · [Original License](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/LICENSE.md)

[Rendered Reading Snapshot](https://mlsysbook.ai/vol1/backmatter/appendix_assumptions.html#sec-appdx-system-assumptions). Rendering provenance is recorded in the import manifest.
