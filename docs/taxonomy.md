# Open World Discovery: Focus, Related Fields, and Scope

[← Main list](../README.md)

<a id="positioning"></a>

## What does Open World Discovery aim to do?

We use **Open World Discovery (OWD)** as a broad organizing term for research on acquiring, constructing, and revising knowledge through exploration and learning in incompletely understood or changing worlds. It brings open-world learning, scientific and causal discovery, discovery intelligence, self-evolving agents, recursive self-improvement, and open-endedness into a shared conversation. This framing is an organizing choice for the list; the communities retain their own definitions and objectives.

Our organizing question is: **How can an agent investigate a partially understood world, recognize when its current account is insufficient, obtain evidence to revise it, and use what it learns in subsequent investigations?**

The [working definition](../README.md#what-is-owd) connects three research objectives:

- **Build discovery agents** that choose informative experiments, maintain hypotheses, and revise inadequate explanations or representations.
- **Develop discovery environments** that expose unknown mechanisms and allow meaningful investigation, with explicit action, feedback, and verification limits.
- **Learn and evaluate discovery capabilities** by measuring verified knowledge gained and whether experience improves discovery on new investigations under comparable resource budgets.

Evaluate what was discovered separately from whether the discovery procedure improved. A fixed procedure can produce useful knowledge; a self-modifying agent still needs evidence that its changes benefit investigation.

## What makes the world open?

Evidence may reveal that the current model or problem formulation is incomplete. For example, an agent might find that adjusting an equation's coefficients cannot explain new observations, propose an additional mechanism, and design an experiment to distinguish competing explanations. It then checks whether the revised model supports independent predictions or further investigation.

Openness is relative to what the agent is given and allowed to change:

| Dimension | What is unknown or revisable? |
| --- | --- |
| Parameters | Values within a specified model |
| Mechanisms | Causal structure, functions, or interactions |
| Representation | Variables, concepts, or the hypothesis language |
| Questions | Which investigation to pursue |
| World changes | Whether previously supported mechanisms still apply |
| Transfer | New structures, mechanism families, or domains |

Bounded tasks can isolate useful capabilities. Estimating coefficients in a supplied correct model does not by itself demonstrate the ability to recognize a missing variable or revise the model family. Distinguish novelty to an agent from novelty to the scientific community.

<a id="related-directions"></a>

## Related fields within a shared research agenda

The following perspectives contribute complementary questions and methods. Their emphases differ, and a single system can connect several of them. The descriptions summarize our interpretation of the cited work.

| Related direction | Questions and contributions to the shared agenda |
| --- | --- |
| [Open World Learning (OWL)](https://arxiv.org/abs/1809.06004) | How can a system recognize, characterize, and learn from unknowns? Foundations include [open-world recognition (2015)](https://openaccess.thecvf.com/content_cvpr_2015/html/Bendale_Towards_Open_World_2015_CVPR_paper.html), combining unknown detection with incremental category learning, and [self-initiated OWL (2021)](https://arxiv.org/abs/2110.11385), encompassing interaction, adaptation, and continual learning. |
| [Discovery Intelligence / Discovery Foundation Models](https://arxiv.org/abs/2609.15973) | How can discovery capabilities be built, learned, and evaluated? Connects problem formulation, representation construction, hypotheses, interventions, evidence-grounded revision, and continual improvement. |
| [Self-evolving agents](https://arxiv.org/abs/2507.21046) | How can experience improve an agent's models, memory, tools, and architecture? Supplies mechanisms for adapting discovery systems and retaining useful experience. |
| Recursive self-improvement ([illustrated by Hyperagents](https://arxiv.org/abs/2603.19461)) | How can improvements strengthen the capacity for further improvement? Connects changes to the system with changes to its improvement procedure. |
| [Open-endedness](https://arxiv.org/abs/2406.04268) | How can novelty and learnability continue over time? Connects the generation of new questions and challenges with continuing exploration and capability development. |

For example, a system can recognize a new object category, incorporate it into its knowledge, investigate why it behaves differently, test competing mechanisms, and retain an improved investigation strategy. This sequence connects open-world learning, scientific discovery, and agent adaptation. Different studies may investigate individual steps or the complete loop, using recognition accuracy, adaptation performance, validated knowledge, or transfer as appropriate evidence.

Scientific discovery and causal learning supply central methods for hypothesis formation, experimentation, identification, and validation. Relevant work from all these communities is welcome.

**Why organize around OWD?** It provides a common language for connecting how systems encounter unknowns, develop and verify knowledge, and improve through experience. The list connects these contributions through shared problems, methods, environments, and evaluation, while making each work's assumptions and evidence explicit.

<a id="categories"></a>

## Categories and core questions

Classify a work by its primary contribution. Secondary methods and capabilities belong in tags; a work can contribute to several questions while appearing once in the list.

The [paper review records](../data/paper-reviews.json) document consulted sections, evidence, limitations, and classification rationale. The [catalog](../data/resources.json) keeps verified paper, code, project, model, and dataset links together; an absent link does not imply that no release exists.

| Category | Core question | Scope |
| --- | --- | --- |
| **Discovery Foundations** | What constitutes a discovery? | Surveys, definitions, theoretical principles, and the epistemic basis of discovery. |
| **Discovery Representations** | What representations enable discovery? | Knowledge representations, concepts, causal structures, world models, and reusable program abstractions. |
| **Discovery Reasoning** | How should agents formulate and test hypotheses? | Hypothesis generation, experimental design, planning, search, and verification; candidate equations and programs can also be tested hypotheses. |
| **Discovery Training** | How can we train agents to discover? | Pretraining, post-training, policy learning, meta-learning, and training objectives for discovery capabilities. |
| **Continual Discovery** | How can agents learn from ongoing investigations? | Test-time adaptation, online updates, feedback-based reflection, and retention or transfer of experience. |
| **Discovery Systems** | How can we build reliable discovery systems? | Agent harnesses, tools, execution infrastructure, memory management, multi-agent coordination, and integrated discovery systems. |
| **Open-Ended Discovery** | How can agents expand the scope of discovery? | Question and environment generation, automatic curricula, autonomous exploration, agent design, and self-improvement. |
| **Discovery Evaluation** | How can we measure progress in discovery? | Datasets, interactive environments, benchmarks, verifiers, and evaluation protocols. |

For **Discovery Training**, distinguish pretraining or foundation-model training, post-training such as SFT and RL, and direct policy or meta-learning approaches. A method trained from scratch need not fit a foundation-model training stage. The category also includes enabling training methods whose discovery application remains to be tested.

For **Continual Discovery**, focus on how feedback changes the agent during or across investigations, including weights, state, memory, or skills. For **Open-Ended Discovery**, focus on generating new investigations or changing the agent's design and improvement process to expand its capabilities. For **Discovery Systems**, focus on the architecture or infrastructure that supports execution. A training algorithm, an adaptation mechanism, and a complete system may use similar components; the main contribution determines placement.

<a id="inclusion"></a>

## What belongs in the list?

- **Core:** Directly studies discovery methods, discovery learning, systems, or evaluation.
- **Enabling:** Supplies a concrete component for evidence acquisition, knowledge revision, or learning to discover.
- **Adjacent:** Provides an informative baseline or comparison with explicit limits.

State the contribution and its supporting evidence. Standalone OOD detection, generic reasoning, or general-purpose tools need a concrete discovery connection.

Each work has one primary category and specific capability tags. Combine papers, code, blogs, and datasets describing the same work into one entry. Distinct environment usage modes belong in the [benchmark guide](benchmarks.md).

## What to record

Identify the unknowns, available evidence and actions, resulting knowledge, and verification method. For learning claims, record what changes, what persists, and performance on new investigations. Separate physical measurements, recorded data, simulations, and computational verification.

Contribution steps and metadata requirements are in [CONTRIBUTING](../CONTRIBUTING.md).
