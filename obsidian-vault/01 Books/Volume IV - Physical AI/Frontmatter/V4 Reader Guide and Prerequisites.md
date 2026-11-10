---
title: V4 Reader Guide and Prerequisites
type: Frontmatter
volume: 4
chapter: 0
publication_status: In Development
source_repository: https://github.com/klappe-pm/cs249r_book
source_commit: de87c0103806d7bfb1c677dbb77a2b92fa00c298
source_path: books/vol4/frontmatter/prerequisites.qmd
source_anchor: reader-guide-and-prerequisites
source_mode: Source-Correlated Published HTML
tags:
- Type/Frontmatter
- Book/Volume_4
rendered_source_url: https://mlsysbook.ai/vol4/frontmatter/prerequisites.html
---

# V4 Reader Guide and Prerequisites

[[Home|Home]] · [[01 Books/Volume IV - Physical AI/Volume 4 Overview|Volume Overview]]

^reader-guide-and-prerequisites

*Physical AI: Machine Learning Systems That Sense and Act* is an independent textbook for advanced undergraduate students, graduate researchers, and practicing engineers who want to build machines that sense and act. Readers may arrive from machine learning, software systems, electrical engineering, or robotics. The common goal is to connect learned behavior to physical execution and explain the conditions under which that connection can be trusted.

## The Technical Starting Point

^sec-prereq-baseline

A physical AI systems engineer must reason across disciplines, but need not enter with specialist training in all of them. The starting point is programming experience, basic machine learning intuition, and introductory mechanics, supported by undergraduate mathematics. Prior study of another volume in this series is not required.

The following competencies support the worked examples. Each area supplies a practical skill that the chapters build on rather than a prerequisite in advanced theory:

- **Programming**: Read and modify a short program, follow its data flow, and interpret experimental output. The executable calculations use Python; familiarity with C or C++ helps with implementation examples but is not the entry requirement.
- **Machine learning intuition**: Distinguish training from inference, understand a learned model as a mapping fitted from data, and recognize why performance on held-out examples may differ from deployment. Experience building a large model or using a particular framework is not required.
- **Mathematics**: Work with algebra, vectors, matrices, derivatives, and elementary probability. These tools support coordinate transformations, rates of change, and uncertainty estimates. More specialized notation is introduced with the mechanism that needs it.
- **Physical reasoning**: Relate force to acceleration, speed to distance traveled, and electrical power to energy use. Introductory Newtonian mechanics supplies the starting intuition for stopping, contact, and actuator limits.
- **Experimental practice**: Interpret a measurement with its units and conditions, distinguish an assumption from an observation, and compare a calculation with a test. The book develops this practice into evidence for operating a machine.

Specialized control theory, robot kinematics, real-time scheduling, and accelerator architecture are subjects of study here, rather than a second set of admission requirements. Some derivations require a slower pass or background reading. The local appendices provide machine learning background (**[[05 Reference/Volume IV - Physical AI/V4 Machine Learning Background#^sec-appendix-ml|Machine Learning Background]]**), control and dynamics (**[[05 Reference/Volume IV - Physical AI/V4 Control and Dynamics#^sec-appendix-control|Control and Dynamics]]**), and systems and hardware (**[[05 Reference/Volume IV - Physical AI/V4 Systems and Hardware#^sec-appendix-systems|Systems and Hardware]]**). When a failure spans perception, planning, and actuation, **[[05 Reference/Volume IV - Physical AI/V4 The Sense–Plan–Act Paradigm#^sec-appendix-spa-troubleshooting|Physical AI Production Troubleshooting Matrix]]** maps the symptom to measurements that distinguish competing causes.

### Learning Across Disciplinary Boundaries

^sec-prereq-disciplinary-boundaries

Readers from different backgrounds enter this loop from different sides. An ML practitioner starts from the consequences of a proposed action and works toward the mechanics and timing that constrain it. An embedded systems engineer starts from a hardware deadline and learns how training data and policy behavior shape the workload that must meet it. A roboticist starts from a model of the plant and examines what changes when a learned proposer supplies goals and trajectories. Each reader brings one part of the foundation and meets the others where the system connects them.

On a first pass through a dense derivation, identify the physical quantity being bounded, the assumptions the bound needs, and the decision it changes. Then work through the example before returning to the derivation. A formal guarantee may require that deeper mathematical treatment; understanding the systems decision still begins with the concrete failure the mechanism is meant to prevent.

## Curricular Reading Tracks

^sec-prereq-tracks

The sequential path is the default for learning the whole discipline. Specialist tracks select an emphasis within that path. They do not make the common physical model or the evidence limits optional.

All tracks begin with **[[01 Books/Volume IV - Physical AI/00 Introduction/01 The Causal Boundary/V4-01 The Causal Boundary#^sec-boundary|The Causal Boundary]]** and the machine anatomy in **[[01 Books/Volume IV - Physical AI/01 Machine Anatomy/02 The Physical Body/V4-02 The Physical Body#^sec-body|The Physical Body]]**, **[[01 Books/Volume IV - Physical AI/01 Machine Anatomy/03 The Cognitive Brain/V4-03 The Cognitive Brain#^sec-brain|The Cognitive Brain]]**, and **[[01 Books/Volume IV - Physical AI/01 Machine Anatomy/04 The Nervous System/V4-04 The Nervous System#^sec-nervous|The Nervous System]]**. These establish physical budgets, learned proposals, and the independent path that decides whether a proposal may act. Later chapters repeatedly use those foundations. After that common start, readers can concentrate their deeper study along one of four role-specific tracks ([[01 Books/Volume IV - Physical AI/Frontmatter/V4 Reader Guide and Prerequisites#^tbl-prereq-tracks|table P.1]]).

| Track                                | Primary Audience                                    | Core Chapter Progression                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   | Primary Systems Competency                                                                    |
|:-------------------------------------|:----------------------------------------------------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:----------------------------------------------------------------------------------------------|
| **Core systems curriculum**          | Students and engineers learning the full discipline | Complete sequence from **[[01 Books/Volume IV - Physical AI/00 Introduction/01 The Causal Boundary/V4-01 The Causal Boundary#^sec-boundary\|The Causal Boundary]]** through **[[01 Books/Volume IV - Physical AI/04 Governing the Machine/18 Engineering Physical AI/V4-18 Engineering Physical AI#^sec-frontier\|Engineering Physical AI]]**                                                                                                                                                                                                                                                                                                                                                                                           | Integrate physical limits, learning, runtime design, and operating evidence                   |
| **ML systems and learned runtimes**  | ML engineers and researchers                        | Common start; **[[01 Books/Volume IV - Physical AI/02 Teaching the Machine/05 Physical Data/V4-05 Physical Data#^sec-data\|Physical Data]]** through **[[01 Books/Volume IV - Physical AI/02 Teaching the Machine/07 Closed-Loop Evaluation/V4-07 Closed-Loop Evaluation#^sec-evaluation\|Closed-Loop Evaluation]]**; **[[01 Books/Volume IV - Physical AI/03 Running the Machine/08 Sensor Perception/V4-08 Sensor Perception#^sec-perception\|Sensor Perception]]** through **[[01 Books/Volume IV - Physical AI/03 Running the Machine/13 Workload Placement/V4-13 Workload Placement#^sec-placement\|Workload Placement]]**; **[[01 Books/Volume IV - Physical AI/04 Governing the Machine/16 Deployment Release/V4-16 Deployment Release#^sec-release\|Deployment Release]]** and **[[01 Books/Volume IV - Physical AI/04 Governing the Machine/18 Engineering Physical AI/V4-18 Engineering Physical AI#^sec-frontier\|Engineering Physical AI]]** | Develop and evaluate learned behavior within physical and computational limits                |
| **Embedded systems and silicon**     | Embedded engineers and computer architects          | Common start; evaluation limits in **[[01 Books/Volume IV - Physical AI/02 Teaching the Machine/07 Closed-Loop Evaluation/V4-07 Closed-Loop Evaluation#^sec-evaluation\|Closed-Loop Evaluation]]**; **[[01 Books/Volume IV - Physical AI/03 Running the Machine/08 Sensor Perception/V4-08 Sensor Perception#^sec-perception\|Sensor Perception]]** through **[[01 Books/Volume IV - Physical AI/03 Running the Machine/13 Workload Placement/V4-13 Workload Placement#^sec-placement\|Workload Placement]]**; **[[01 Books/Volume IV - Physical AI/04 Governing the Machine/14 Supervisory Intervention/V4-14 Supervisory Intervention#^sec-intervention\|Supervisory Intervention]]** through **[[01 Books/Volume IV - Physical AI/04 Governing the Machine/18 Engineering Physical AI/V4-18 Engineering Physical AI#^sec-frontier\|Engineering Physical AI]]**                                        | Keep sensing, permission, and actuation timely under interference and faults                  |
| **Robotics, control, and assurance** | Roboticists and control engineers                   | Common start; **[[01 Books/Volume IV - Physical AI/02 Teaching the Machine/05 Physical Data/V4-05 Physical Data#^sec-data\|Physical Data]]** through **[[01 Books/Volume IV - Physical AI/02 Teaching the Machine/07 Closed-Loop Evaluation/V4-07 Closed-Loop Evaluation#^sec-evaluation\|Closed-Loop Evaluation]]**; **[[01 Books/Volume IV - Physical AI/03 Running the Machine/09 Spatial Memory/V4-09 Spatial Memory#^sec-memory\|Spatial Memory]]** through **[[01 Books/Volume IV - Physical AI/04 Governing the Machine/18 Engineering Physical AI/V4-18 Engineering Physical AI#^sec-frontier\|Engineering Physical AI]]**                                                                                                                                                                                                                 | Integrate learned behavior with state estimation, feasible motion, and conditional guarantees |

Table P.1: **Curricular reading tracks**: Four structured reading tracks through this book.

^tbl-prereq-tracks

When a track omits a chapter from detailed study, its opening, worked handoff, and summary provide the context needed downstream. For example, a planning exercise still needs dated observations and a current state estimate; a release decision still needs evidence about human authority and fault response. Instructors can select technical depth while retaining those dependencies. The full sequence contains more detail than every course will cover at equal depth.

## What the Book Introduces

^what-the-book-introduces

The curriculum builds toward an end-to-end engineering judgment about a machine performing a specified task. Its parts contribute different capabilities:

1.  In Part I, determine which physical budget binds, estimate what the learned proposer can supply, and derive the timing requirements that connect computation to actuation.
2.  In Part II, collect demonstrations with their operating conditions, choose a training regime, and evaluate behavior in the feedback loop where actions change subsequent observations. Use failures to collect new experience and test whether a changed candidate expands competence without losing established behavior.
3.  In Part III, turn measurements into dated state estimates, grounded goals, and feasible trajectories; then check proposals against physical limits and place the runtime on resources that can meet its deadlines.
4.  In Part IV, design human intervention, challenge the integrated system with faults, and justify useful service within the conditions the evidence covers, assessing task performance and physical containment separately.

The conclusion synthesizes those engineering capabilities and tests whether they transfer to an unfamiliar machine. The records accumulated along the way preserve the reasoning behind a design: what was measured, what was assumed, which decision followed, and what would invalidate it. Filling in a record is useful only when the underlying engineering argument is sound.

## How to Read the Numbers

^sec-reader-numbers

The evidence behind a number determines what it can support. Four categories distinguish observations and calculations from ratings and illustrative inputs; a fifth label identifies a design choice:

- **Measured**: A calibrated observation of a particular machine. It names its instrument, its operating conditions, its sample count, and, for a distribution, the percentile it reports. Only a measured number, or a number derived from measured ones, can support a safety margin.
- **Derived**: Computed from stated inputs through a physical or statistical model. It carries that model’s assumptions, input provenance, and propagated uncertainty. A result derived from illustrative inputs remains illustrative evidence.
- **Datasheet**: A manufacturer’s rating under the manufacturer’s conditions. It says what to expect and what to test, and it is not evidence about the unit on the bench.
- **Illustrative**: Selected to show arithmetic or scaling. It supports no margin, timeout, or release decision.

A budget or requirement, such as a lease duration or a clearance margin, belongs to none of the four. It is a design decision, labeled **chosen**, and it means something only when it is checked against the measured or derived number it must fit, as a chosen lease is checked against the derived ceiling on pre-brake delay.

A worked design in this book shows a decision procedure. When its inputs are illustrative, the decision it reaches is illustrative too. It shows how the machine’s speed, lease, or verdict would be set, and it would bind a real machine only after its physical and timing premises are qualified. Some examples stipulate a supporting evidence packet to teach how successful learning or restricted service could be justified. Such branches are hypothetical throughout; their assumed trial counts and outcomes are not measurements of the book’s machine.

When a number decides something, such as a speed limit, a timeout, or a release, the book keeps it as a **limit record** with six elements. The record pairs the nominal value (or distribution) and its measurement uncertainty with the operating conditions under which that value holds (payload, temperature, supply voltage, surface, concurrent workload, and firmware). Alongside the engineering margin between the operating target and the breakdown threshold, it names the runtime detector that catches an excursion while the machine runs and records the value’s provenance, meaning its label and the instrument or model that produced it. A limit holds only under its stated conditions. When wear, heat, a new payload, or a new build changes them, the limit must be established again before it is reused.

Before using a worked value to justify a decision, establish both its category and the conditions attached to it, because an unlabeled value does not become a measured limit merely by appearing in a calculation. Every result holds only under the assumptions stated with its example. A statistical bound from finitely many trials depends on its sampling assumptions and proves nothing beyond them. A measured percentile describes only the tested workload rather than a true worst case. In a release argument (**[[01 Books/Volume IV - Physical AI/04 Governing the Machine/16 Deployment Release/V4-16 Deployment Release#^sec-release|Deployment Release]]** and **[[01 Books/Volume IV - Physical AI/04 Governing the Machine/18 Engineering Physical AI/V4-18 Engineering Physical AI#^sec-frontier|Engineering Physical AI]]**), each premise therefore carries an explicit status: established by qualified measurements or derivations, assumed, decided by accountable judgment, unsupported, or outside the threat model.

## What We Deliberately Omit

^what-we-deliberately-omit

The book develops specialist mechanisms to the depth needed for systems decisions, introducing each topic from first principles inside the chapter whose decision depends on it and stopping there. In the anatomy and learning chapters, model quantization is introduced where it sets the intent model’s latency (**[[01 Books/Volume IV - Physical AI/01 Machine Anatomy/03 The Cognitive Brain/V4-03.05 The Cost of a Fresh Evaluation#^sec-brain-quantization|Quantizing the intent model]]**), while reinforcement learning fundamentals and the pretrain-then-post-train recipe appear when the arm learns the spring-latched door task (**[[01 Books/Volume IV - Physical AI/02 Teaching the Machine/06 Policy Training/V4-06.03 Policy Training Regimes#^sec-training-rl-primer|The latch task as a reward problem]]**, **[[01 Books/Volume IV - Physical AI/02 Teaching the Machine/06 Policy Training/V4-06.03 Policy Training Regimes#^sec-training-pretrain-post-train|Pretrained generalist policies and post-training]]**). In the runtime chapters, perception stops at the qualified measurement and hands state estimation to spatial memory (**[[01 Books/Volume IV - Physical AI/03 Running the Machine/09 Spatial Memory/V4-09 Spatial Memory#^sec-memory|Spatial Memory]]**). Spatial memory builds from the discrete and extended Kalman filters, multi-target tracking, and delayed updates (**[[01 Books/Volume IV - Physical AI/03 Running the Machine/09 Spatial Memory/V4-09.03 Estimating State from Dated Measurements#^sec-perception-state-estimation|Estimating State from Dated Measurements]]**) to localization and SLAM in the planning map (**[[01 Books/Volume IV - Physical AI/03 Running the Machine/09 Spatial Memory/V4-09.06 Coordinate Transform Expiry and Localization Drift#^sec-memory-localization-slam|Localization drift and map frames that jump]]**). Task and motion planning grounds abstract goals in feasible geometry (**[[01 Books/Volume IV - Physical AI/03 Running the Machine/10 Grounded Intent/V4-10.03 Task Operators and Geometric Samplers#^sec-intent-task-motion|Task Operators and Geometric Samplers]]**), while manipulator kinematics, time parameterization, and mobile-base planning build the trajectory record (**[[01 Books/Volume IV - Physical AI/03 Running the Machine/11 Trajectory Planning/V4-11.03 The Planning Handoff and the Trajectory Record#^sec-planning-handoff|The Planning Handoff and the Trajectory Record]]**, **[[01 Books/Volume IV - Physical AI/03 Running the Machine/11 Trajectory Planning/V4-11.05 Kinodynamic Feasibility#^sec-planning-time-parameterization|Time parameterization under torque and jerk bounds]]**, **[[01 Books/Volume IV - Physical AI/03 Running the Machine/11 Trajectory Planning/V4-11.07 Choosing a Trajectory Generator#^sec-planning-mobile-base|Mobile-base planning under nonholonomic constraints]]**) and worst-case execution time analysis tests hardware isolation (**[[01 Books/Volume IV - Physical AI/03 Running the Machine/13 Workload Placement/V4-13.08 Empirical Verification of Silicon Isolation#^sec-placement-testing-separation|Empirical Verification of Silicon Isolation]]**). Finally, the governance chapters introduce importance sampling where rare-failure rates must be estimated (**[[01 Books/Volume IV - Physical AI/04 Governing the Machine/15 Adversarial Verification/V4-15.11 Interpreting Campaign Statistics#^sec-verification-importance-sampling|Estimating a rare failure rate by importance sampling]]**) and functional safety standards where the release argument is assembled (**[[01 Books/Volume IV - Physical AI/04 Governing the Machine/16 Deployment Release/V4-16.04 Safety Cases and Claims#^sec-release-standards-map|The standards map for the running machine]]**).

What the book omits is the remainder of each of those fields. It does not provide an exhaustive catalog of manipulator geometries or grasp analysis, or a complete course in nonlinear or optimal control. It omits the convergence theory of reinforcement learning and the construction of large-scale SLAM back ends. It also leaves out the internals of static timing-analysis tools and a comprehensive theory of deep learning optimization, and it is not a substitute for the text of a safety standard. Specialized derivations appear where they explain a bound or trade-off, and the appendices provide supporting background.

Implementation examples expose timing, memory, communication, and actuation mechanisms. They are not tutorials for a particular robotics middleware package or simulation product. The intended result is the ability to reason about a new machine and recognize when its design needs additional specialist analysis or measurement.

Back to top

## Source

[Repository Source](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/books/vol4/frontmatter/prerequisites.qmd) · [Original License](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/LICENSE.md)

[Rendered Reading Snapshot](https://mlsysbook.ai/vol4/frontmatter/prerequisites.html#reader-guide-and-prerequisites). Rendering provenance is recorded in the import manifest.
