---
title: Accuracy and Efficiency
type: theme
tags:
- Type/Theme
- Theme/Accuracy_and_Efficiency
source_repository: https://github.com/klappe-pm/cs249r_book
source_commit: de87c0103806d7bfb1c677dbb77a2b92fa00c298
source_path: taxonomy/taxonomy.yml
editorial_scope: Curated Navigation Lens
---

# Accuracy and Efficiency

Connect model quality to representation, compression, and the measured resource cost of a useful result.

This curated navigation lens is an editorial association, not a claim of dependency or equivalence.

## Concepts

- [[02 Concepts/Foundations/Workloads & Requirements/Pareto Frontier|Pareto Frontier]] — The set of configurations for which no objective, such as accuracy, latency, or cost, can improve without worsening another.
- [[02 Concepts/Lifecycle/Model Evaluation & Testing/Generalization|Generalization]] — Performance on relevant examples or conditions beyond those used to fit the system.
- [[02 Concepts/Qualities/Performance, Efficiency & Benchmarking/Quantization|Quantization]] — Representing values using a reduced discrete set with a specified encoding and approximation rule.
- [[02 Concepts/Qualities/Performance, Efficiency & Benchmarking/Post Training Quantization|Post Training Quantization]] — Quantizing a trained model without retraining, choosing scales and rounding from statistics of the weights and, for many methods, a small calibration set of representative inputs.
- [[02 Concepts/Qualities/Performance, Efficiency & Benchmarking/Quantization Aware Training|Quantization Aware Training]] — Training or fine-tuning with simulated quantization in the forward pass so the model adapts to reduced precision, in contrast to post-training quantization.
- [[02 Concepts/Qualities/Performance, Efficiency & Benchmarking/Weight Only Quantization|Weight Only Quantization]] — Storing weights at low bit width while computing in higher-precision activations, cutting memory traffic for bandwidth-bound decoding, with error-compensating or activation-aware rounding.
- [[02 Concepts/Stack/Frameworks, Compilers & Runtimes/Numerical Precision|Numerical Precision]] — The representable values and arithmetic behavior of a numerical format.
- [[02 Concepts/Qualities/Performance, Efficiency & Benchmarking/Pruning|Pruning]] — Removing weights, neurons, channels, or other structures judged unimportant from a network, usually followed by fine-tuning to recover quality.
- [[02 Concepts/Qualities/Performance, Efficiency & Benchmarking/Structured Pruning|Structured Pruning]] — Pruning whole channels, filters, heads, or layers so that the remaining model stays dense and runs faster without sparse-execution support.
- [[02 Concepts/Qualities/Performance, Efficiency & Benchmarking/Knowledge Distillation|Knowledge Distillation]] — Training a student to match output distributions or internal signals from a teacher model or ensemble, potentially reducing serving cost when the student is cheaper while requiring validation of retained quality.
- [[02 Concepts/Qualities/Sustainability & Cost/Energy Efficiency|Energy Efficiency]] — Useful work completed per unit energy, such as inferences or tokens per joule, measured within a stated system boundary.
- [[02 Concepts/Qualities/Sustainability & Cost/Cost per Useful Outcome|Cost per Useful Outcome]] — Total relevant expenditure divided by outcomes meeting a specified acceptance criterion.

## Connected Book Passages

- [[01 Books/Volume I - Foundations/03 Optimization/10 Model Compression/V1-10.03 Structural Optimization Changing What the Model Computes#^sec-model-compression-pruning-d1cb|V1-10.03 Structural Optimization Changing What the Model Computes]]
- [[01 Books/Volume I - Foundations/03 Optimization/10 Model Compression/V1-10.04 Numerical Precision Changing How Values Are Stored#^sec-model-compression-performance-gains-0656|V1-10.04 Numerical Precision Changing How Values Are Stored]]
- [[01 Books/Volume III - Agentic Systems/06 Agents at Scale/19 Agent Economics/V3-19.03 Cost per Accepted Task#^sec-vol3-agent-economics-cohort-ratio|V3-19.03 Cost per Accepted Task]]

## Navigation

[[00 Navigation/Topic Index|Topic Index]]
