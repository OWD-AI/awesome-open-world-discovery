<p align="center">
  <img src="assets/owd-mark.svg?v=27a293ca0c" width="72" height="72" alt="Open World Discovery: exploring beyond a known boundary">
</p>

<h1 align="center">Awesome Open World Discovery</h1>

<p align="center">
  <strong>Acquire evidence. Discover mechanisms. Learn to discover.</strong><br>
  A curated research guide to discovery agents, learning methods, and evaluation.
</p>

<p align="center">
  <a href="https://awesome.re"><img src="https://awesome.re/badge.svg" alt="Awesome"></a>
  <a href="#contents"><img src="https://img.shields.io/badge/works-712-2563eb?style=flat-square" alt="712 curated works"></a>
  <a href="docs/benchmarks.md"><img src="https://img.shields.io/badge/environment_profiles-136-0f766e?style=flat-square" alt="136 environment profiles"></a>
  <a href="CONTRIBUTING.md"><img src="https://img.shields.io/badge/contributions-welcome-7c3aed?style=flat-square" alt="Contributions welcome"></a>
</p>

<p align="center">
  <a href="https://owd-ai.github.io/awesome-open-world-discovery/">Research observatory ↗</a> · <a href="#what-is-owd">What is OWD?</a> · <a href="#why-owd">Why this focus?</a> · <a href="#updates">Latest papers</a> · <a href="#contents">Browse the list</a> · <a href="CONTRIBUTING.md">Contribute</a>
</p>

<p align="center"><sub>Literature checked through 2026-10-28 · Papers, author blogs, code, and benchmarks</sub></p>

<a id="what-is-owd"></a>

## 🧭 What is Open World Discovery?

> **Our working definition:** Open World Discovery connects research on how agents acquire, construct, and revise knowledge through exploration and learning in incompletely understood or changing worlds. This broad agenda brings together discovering unknowns, developing verifiable and reusable knowledge, and improving the ability to discover.

The central loop connects **hypotheses, informative actions, evidence, and revision**. Its outputs should be checked against independent observations, interventions, or executable/formal verifiers. Learning to discover asks how experience improves this loop across investigations.

![A discovery agent sends experiments to a partially known world, revises its hypotheses using returned evidence, and can expand its knowledge boundary. A separate learning loop improves discovery across investigations.](assets/open-world-discovery.png)

[View the diagram at full size](assets/open-world-discovery.png)

**What makes the world open?** The current model or problem formulation may be incomplete: evidence can call for a different mechanism, a new variable, or a revised question. Openness is relative to what the agent is given and allowed to change. Bounded discovery tasks help study individual components; see the [scope guide](docs/taxonomy.md#positioning).

<a id="why-owd"></a>

### Why Open World Discovery?

<a id="related-directions"></a>

Discovery involves deciding what to investigate, gathering evidence, testing explanations, and carrying knowledge into future investigations. Representations, reasoning, training, and agent systems each contribute to this process.

**We use Open World Discovery as a shared research agenda connecting these contributions.** It brings together work on learning from unknowns, generating and validating discoveries, and improving discovery capabilities over time. By organizing methods, systems, and evaluation around common questions, this list aims to help researchers understand how individual advances can support the discovery process as a whole. See [the research scope and connections to related fields](docs/taxonomy.md#positioning).

**Download the catalog:** [BibTeX](references.bib) · [JSON](data/resources.json)

<a id="updates"></a>

## 📰 Latest Papers

**[Explore the research observatory →](https://owd-ai.github.io/awesome-open-world-discovery/#updates)**

The latest 10 source-checked papers from our daily monitor · Updated 2026-10-28.

Visit the website for summaries, figures, today's updates, and the full research library.

| Date | Paper |
| --- | --- |
| 2026-10-27 | [Vision-Language-Action or World-Action? Just Action Models](https://arxiv.org/abs/2610.37219) |
| 2026-10-27 | [ThinkWorld: World Imagination Reinforces Chain-of-Dynamics Reasoning](https://arxiv.org/abs/2610.37666) |
| 2026-10-27 | [RubricAtlas: Mining Type-Level Rubrics from Expert Reports to Evaluate Deep Research Agents](https://arxiv.org/abs/2610.36878) |
| 2026-10-27 | [MLE-World: Predicting Machine Learning Experiment Outcomes with a Learned World Model](https://arxiv.org/abs/2610.37175) |
| 2026-10-27 | [Can LLMs Uncover Hidden Physical Laws through Free Exploration?](https://arxiv.org/abs/2610.37649) |
| 2026-10-27 | [AutoRSE: Evaluating LLM Agents as Recommendation Engineers for Self-Evolving Recommender Systems](https://arxiv.org/abs/2610.37228) |
| 2026-10-26 | [Work Agents: Systems, Capabilities, and Optimization](https://arxiv.org/abs/2610.35845) |
| 2026-10-26 | [Trustworthy Recursive Self-Improvement in the Era of Large Models: Foundation, Risks, Evaluation and Open Challenges](https://arxiv.org/abs/2610.35193) |
| 2026-10-26 | [SO-101 Bench: Accessible Spatial Manipulation](https://arxiv.org/abs/2610.36420) |
| 2026-10-26 | [RoboDoctor: Training-Free Recursive Self-Improvement for Robot Policies](https://arxiv.org/abs/2610.35604) |

<a id="contents"></a>

## 🗂️ Contents

| Topic | Research question | Works |
| --- | --- | ---: |
| 📚 [Discovery Foundations](#foundations) | What constitutes a discovery? | 40 |
| 🧩 [Discovery Representations](#causality) | What representations enable discovery? | 78 |
| 🔬 [Discovery Reasoning](#sci_methods) | How should agents formulate and test hypotheses? | 59 |
| 🧠 [Discovery Training](#learning) | How can we train agents to discover? | 115 |
| 🔄 [Continual Discovery](#adaptation) | How can agents learn from ongoing investigations? | 100 |
| 🛠️ [Discovery Systems](#systems) | How can we build reliable discovery systems? | 120 |
| 🌱 [Open-Ended Discovery](#open_ended) | How can agents expand the scope of discovery? | 73 |
| 📊 [Discovery Evaluation](#benchmarks) | How can we measure progress in discovery? | 127 |

[🔗 Related lists](#related) · [🤝 Contributing](#contributing)

Each work appears once under its primary contribution; see the [classification guide](docs/taxonomy.md#categories) for category scopes. Entries are grouped by publication year, newest first. Each work keeps its paper, code, project, and dataset links together, followed by authors and paper-time affiliations. Full attribution is recorded in the [catalog data](data/resources.json).

<a id="foundations"></a>

## 📚 Discovery Foundations

*What constitutes a discovery?*

### 2026

- <a id="paper-7c2e98f772c31d33"></a>**A Conditional No-Hair Theorem for Transformers: How Language Models Forget Their Prompt** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.24133)* · [Paper](https://arxiv.org/abs/2610.24133) · [Code](https://github.com/ShuyangenFrance/no-hair-transformers)<br>
  Shuyang Xiang · Independent researcher
- <a id="paper-57052b4cd1377f60"></a>**A Kinetic Theory of the Gated Self-Evolving LLM Agent** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.03243)* · [Paper](https://arxiv.org/abs/2610.03243)<br>
  Haipeng Wang · Neusoft Corporation
- <a id="self-evolving-survey"></a>**A Survey of Self-Evolving Agents: What, When, How, and Where to Evolve on the Path to Artificial Super Intelligence** · *[TMLR 2026](https://openreview.net/pdf?id=CTr3bovS5F)* · [Paper](https://arxiv.org/abs/2507.21046) · [List](https://github.com/CharlesQ9/Self-Evolving-Agents)<br>
  Huan-ang Gao et al. · Princeton University; Princeton AI Lab; Tsinghua University; +14 institutions
- <a id="paper-2ef94c45e113c85e"></a>**Agentic Economies for Autonomous Scientific Discovery** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2609.31562)* · [Paper](https://arxiv.org/abs/2609.31562)<br>
  Nenad Tomašev et al. · Google DeepMind
- <a id="paper-663c45b308182702"></a>**Audit the Scaffold, Not the Checkpoint: A Stationarity Dichotomy for Recursive Self-Improvement in Agentic Coding** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2609.34924)* · [Paper](https://arxiv.org/abs/2609.34924)<br>
  Sebastian Bobadilla-Suarez, Bob Suh, Ryan Fortin · OnCorps
- <a id="paper-f7d99db0c10b4603"></a>**Beyond Federated Learning: Decentralized Agentic Systems for Self-Evolving Clinical Intelligence** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.35453)* · [Paper](https://arxiv.org/abs/2610.35453)<br>
  Haoyuan Li, Mathias Funk, Aaqib Saeed · Eindhoven University of Technology
- <a id="paper-e7d4b4cbecd5681d"></a>**Building Trustworthy Household Robots through Open-World Safety** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.14034)* · [Paper](https://arxiv.org/abs/2610.14034)<br>
  Yu-Lin Tsai et al. · University of California, Berkeley
- <a id="causal-agents"></a>**Causal Discovery in the Era of Agents** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2606.23608)* · [Paper](https://arxiv.org/abs/2606.23608)<br>
  Yujia Zheng et al. · Carnegie Mellon University; Mohamed bin Zayed University of Artificial Intelligence
- <a id="paper-7fabe26ca5c43e1f"></a>**Co-Recursive Semantic Self-Extension: A Mathematical Foundation for Open-Ended Intelligence** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.31097)* · [Paper](https://arxiv.org/abs/2610.31097)<br>
  Simon Hegelich et al. · GaiaLogic Unipessoal Lda.; Nanyang Technological University, Singapore; University of Macau
- <a id="paper-be65e818efe095a3"></a>**Designing Human-AI Collaborative Science: The 9A Framework** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.22948)* · [Paper](https://arxiv.org/abs/2610.22948) · [Code](https://github.com/ZihanZheng2000/human-ai-collaborative-science-framework)<br>
  Zihan Zheng, Linyue Pan, Xin Lan · University of Illinois Urbana–Champaign; Tsinghua University; Michigan State University
- <a id="discovery-foundation-models"></a>**Discovery Foundation Models: Toward Open-Ended Discovery Intelligence** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2609.15973)* · [Paper](https://arxiv.org/abs/2609.15973) · [Research resources](https://github.com/Gen-Verse/DFM-Plans) · [Project](https://phai-labs.com/collaborate/)<br>
  Ling Yang, Zhenfei Yin, Yingcheng Wu · DFM Scientist Collaboration Program
- <a id="paper-0114a6f3ab1bd81d"></a>**Evolutionary Computation for Trustworthy AI: From Attacks and Defenses to Self-Evolving Era** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.02996)* · [Paper](https://arxiv.org/abs/2610.02996)<br>
  Junhao Dong et al. · Nanyang Technological University; Center for Frontier AI Research, Institute of High Performance Computing, A*STAR; Google; +2 institutions
- <a id="paper-71d5d311cc1af97a"></a>**Evolutionary Safety of Recursive Self-Improving AI: Taxonomy, Risk Discovery, and Evaluation** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2609.31186)* · [Paper](https://arxiv.org/abs/2609.31186) · [Project](https://chaunceykung.github.io/evolutionary-safety-rsi/) · [Project](https://github.com/ChaunceyKung/awesome-evolutionary-safety)<br>
  CHANG GONG et al. · Institute of Computing Technology, Chinese Academy of Sciences; The Hong Kong Polytechnic University; Peking University
- <a id="paper-17285314da74286e"></a>**From Existing Methods to New Research Ideas: Two Perspectives on Recursive Self-Improvement** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.14625)* · [Paper](https://arxiv.org/abs/2610.14625) · [Project](https://prism-shadow.github.io/awesome-rsi/) · [Code](https://github.com/Prism-Shadow/awesome-rsi)<br>
  Leijun Zhou et al. · PrismShadow; Peking University; Zhejiang University; +1 institutions
- <a id="paper-318b93aa36b4f84e"></a>**From Sliding Windows to Self-evolving Lifelong Memory: A Dual-perspective Survey of Memory Paradigms for Long-Horizon Robotics VLA Models** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.23319)* · [Paper](https://arxiv.org/abs/2610.23319)<br>
  Yong Wang et al. · Department of Computer Science and Technology, Hainan Bielefeld University of Applied Sciences, Hainan 571700, China
- <a id="paper-b77ee31d35a18dcc"></a>**How Is Automated Research Evaluated? A Survey of Benchmarks and Evaluation Practices** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.11877)* · [Paper](https://arxiv.org/abs/2610.11877)<br>
  Liulei Zhang et al. · NLP2CT Lab, Department of Artificial Intelligence University of Macau, Macau, China
- <a id="paper-cc26871dfb8c52d0"></a>**Memory-Centric Continual Learning for AI Agents** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.29357)* · [Paper](https://arxiv.org/abs/2610.29357)<br>
  Dongfang Li et al. · Harbin Institute of Technology (Shenzhen), Shenzhen, China; Shenzhen Loop Area Institute, Shenzhen, China; Tsinghua University, Beijing, China; +3 institutions
- <a id="paper-966a7ee9e76d9427"></a>**Mixed-Prior Decision Risk for Open-Set Recognition** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2609.35043)* · [Paper](https://arxiv.org/abs/2609.35043)<br>
  L. A. Erlygin, P. D. Proskura, A. A. Zaytsev · Skolkovo Institute of Science and Technology (Skoltech); Risk Management, Sber; The Institute for Information Transmission Problems (IITP RAS)
- <a id="paper-12f2f100744d125c"></a>**MMLA-RSI: Recursive Self-Improvement through RTT and RTMA** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.20294)* · [Paper](https://arxiv.org/abs/2610.20294)<br>
  Junyi Zou, Avrova Donz · MMLA-org; Communication University of China (CUC)
- <a id="paper-51ce772b7b376b84"></a>**Modeling Authentic Research Trajectories: A Graph View of Research Ideation** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.27337)* · [Paper](https://arxiv.org/abs/2610.27337)<br>
  Ruochen Li, Zhiyu Chen · University of Texas at Dallas
- <a id="paper-1178f409c73ca56a"></a>**Multimodal Embodied Agents: A Unified Capability-centric Perspective from Computer-Use to Robot-Use** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.30108)* · [Paper](https://arxiv.org/abs/2610.30108) · [Project](https://showlab.github.io/Awesome-Multimodal-Embodied-Agent)<br>
  Yanzhe Chen et al. · Show Lab, National University of Singapore
- <a id="paper-1c4fe91ded721a1e"></a>**Mycelium: A Meta-Study of Hallucination Detection Across Provenance, Typology, and Granularities** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.33608)* · [Paper](https://arxiv.org/abs/2610.33608) · [Code](https://github.com/lmeribal/mycelium)<br>
  Julia Belikova, Elisei Rykov · Skoltech; Sber AI Lab
- <a id="paper-ec9a86ab8654e080"></a>**On the Tip of the Tongue: First-Token Cueing as a Behavioral Probe of Recall Failures in LLMs** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.23400)* · [Paper](https://arxiv.org/abs/2610.23400)<br>
  Jaewon Sok et al. · Seoul National University
- <a id="paper-94d5d577ef0fe3a4"></a>**Open-world AI: a Tale of Three Requirements** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.20782)* · [Paper](https://arxiv.org/abs/2610.20782) · [Code](https://github.com/facebookresearch/MemoryMosaics)<br>
  Jianyu Zhang, Léon Bottou · FAIR, Meta; Flatiron Institute
- <a id="paper-dfbccdacbb319eab"></a>**Reading, Writing, Sharing, and Interacting with the World through Video** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.31668)* · [Paper](https://arxiv.org/abs/2610.31668) · [Project](https://vid-gen.github.io/video-world-model-survey) · [Code](https://github.com/vid-gen/awesome-video-world-model)<br>
  Shengqiong Wu et al. · University of Oxford; NUS; NTU; +1 institutions
- <a id="paper-4bc2aa3dc5c6d11a"></a>**Self-Evolving Agent Harness** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.18813)* · [Paper](https://arxiv.org/abs/2610.18813) · [Code](https://github.com/zgcagi/Harness-RSI) · [Project](https://zgcagi.github.io/Harness-RSI/)<br>
  Chuyang Wei et al. · Zhongguancun Academy; Zhongguancun Institute of Artificial Intelligence; University of Science and Technology of China
- <a id="paper-1e60f285c8164f89"></a>**Toward Recursive Self-Improvement in Physical AI** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.29677)* · [Paper](https://arxiv.org/abs/2610.29677) · [Project](https://physical2rsi.github.io) · [Code](https://github.com/Physical2RSI/Awesome-Physical2RSI)<br>
  Meng Luo et al. · National University of Singapore; Huazhong University of Science and Technology; Shanghai Jiao Tong University; +2 institutions
- <a id="paper-27096c6218492feb"></a>**Trustworthy Recursive Self-Improvement in the Era of Large Models: Foundation, Risks, Evaluation and Open Challenges** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.35193)* · [Paper](https://arxiv.org/abs/2610.35193) · [Project](https://github.com/pujiayue/Trustworthy-RSI) · [Project](https://pujiayue.github.io/Trustworthy-RSI/)<br>
  Jiayue Pu et al. · Gaoling School of Artificial Intelligence, Renmin University of China; University of Chinese Academy of Sciences
- <a id="paper-207da96ea3ec4712"></a>**Who Improves the Robot? Toward Physical Recursive Self-Improvement** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.18842)* · [Paper](https://arxiv.org/abs/2610.18842) · [Project](https://github.com/SAIL-Research-Lab/Physical-RSI)<br>
  Hai Zhou et al. · Shanghai Jiao Tong University; Google; Microsoft; +13 institutions
- <a id="paper-47e008c461c64eb6"></a>**Work Agents: Systems, Capabilities, and Optimization** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.35845)* · [Paper](https://arxiv.org/abs/2610.35845) · [Project](https://github.com/EnjunDu/awesome-working-agent)<br>
  Zishan Xu et al. · Shanghai Jiao Tong University; The University of Hong Kong; The Hong Kong University of Science and Technology (Guangzhou); +5 institutions

### 2025

- <a id="survey-agentic-ai"></a>**Agentic AI for Scientific Discovery: A Survey of Progress, Challenges, and Future Directions** · *[ICLR AgenticAI Workshop 2025](https://openreview.net/forum?id=TyCYakX9BD)* · [Paper](https://arxiv.org/abs/2503.08979)<br>
  Mourad Gridach et al. · IQVIA
- <a id="scientific-agents-vision"></a>**Autonomous Agents for Scientific Discovery: Orchestrating Scientists, Language, Code, and Physics** · *[arXiv 2025 (preprint)](https://arxiv.org/abs/2510.09901)* · [Paper](https://arxiv.org/abs/2510.09901)<br>
  Lianhao Zhou et al. · Texas A&M University; Harvard Medical School; Massachusetts Institute of Technology; +2 institutions
- <a id="survey-agentic-science"></a>**From AI for Science to Agentic Science: A Survey on Autonomous Scientific Discovery** · *[arXiv 2025 (preprint)](https://arxiv.org/abs/2508.14111)* · [Paper](https://arxiv.org/abs/2508.14111) · [Project](https://agenticscience.github.io/) · [List](https://github.com/AgenticScience/Awesome-Agent-Scientists)<br>
  Jiaqi Wei et al. · Shanghai AI Laboratory; Zhejiang University; Fudan University; +7 institutions
- <a id="survey-autonomy"></a>**From Automation to Autonomy: A Survey on Large Language Models in Scientific Discovery** · *[EMNLP 2025](https://aclanthology.org/2025.emnlp-main.895/)* · [Paper](https://arxiv.org/abs/2505.13259) · [List](https://github.com/HKUST-KnowComp/Awesome-LLM-Scientific-Discovery)<br>
  Tianshi Zheng et al. · HKUST
- <a id="survey-scientific-intelligence"></a>**Towards Scientific Intelligence: A Survey of LLM-based Scientific Agents** · *[arXiv 2025 (preprint)](https://arxiv.org/abs/2503.24047)* · [Paper](https://arxiv.org/abs/2503.24047)<br>
  Shuo Ren et al. · Institute of Automation, Chinese Academy of Sciences; University of Chinese Academy of Sciences; Wuhan AI Research

### 2024

- <a id="open-ended-asi"></a>**Open-Endedness is Essential for Artificial Superhuman Intelligence** · *[ICML 2024](https://proceedings.mlr.press/v235/hughes24a.html)* · [Paper](https://arxiv.org/abs/2406.04268)<br>
  Edward Hughes et al. · Google DeepMind

### 2020

- <a id="owl-review"></a>**A Review of Open-World Learning and Steps Toward Open-World Learning Without Labels** · *[arXiv 2020 (preprint)](https://arxiv.org/abs/2011.12906)* · [Paper](https://arxiv.org/abs/2011.12906)<br>
  Mohsen Jafarzadeh et al. · University of Colorado Colorado Springs

### 2009

- <a id="c01"></a>**Causal Inference in Statistics An Overview** · *[Statistics Surveys 2009](https://projecteuclid.org/journals/statistics-surveys/volume-3/issue-none/Causal-inference-in-statistics-An-overview/10.1214/09-SS057.full)* · [Paper](https://escholarship.org/uc/item/36w8n7pg) · [Author PDF](https://ftp.cs.ucla.edu/pub/stat_ser/r350.pdf)<br>
  Judea Pearl · UCLA
- <a id="f04"></a>**Driven by Compression Progress: A Simple Principle Explains Essential Aspects of Subjective Beauty, Novelty, Surprise, Interestingness, Attention, Curiosity, Creativity, Art, Science, Music, Jokes** · *[ABiALS 2008, LNCS 5499 2009](https://link.springer.com/chapter/10.1007/978-3-642-02565-5_4)* · [Paper](https://arxiv.org/abs/0812.4360)<br>
  Jürgen Schmidhuber · TU Munich; IDSIA

### 2005

- <a id="f05"></a>**A tutorial introduction to the minimum description length principle** · *[Advances in Minimum Description Length (MIT Press) 2005 (chapter)](https://homepages.cwi.nl/~pdg/publicationpage.html)* · [Paper](https://arxiv.org/abs/math/0406077)<br>
  Peter Grünwald · Centrum Wiskunde & Informatica (CWI)

[↑ Contents](#contents)

<a id="causality"></a>

## 🧩 Discovery Representations

*What representations enable discovery?*

### 2026

- <a id="paper-0818c2841249d620"></a>**ActionRoPE: action as coordinates for spatially consistent control in planar-camera game world models** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.25861)* · [Paper](https://arxiv.org/abs/2610.25861) · [Code](https://github.com/TeaWhiteBro/ActionRoPE) · [Project](https://teawhite.cn/ActionRoPE/) · [HF Model](https://huggingface.co/teawhite/ActionRoPE)<br>
  Zhiyang Deng, Yuzhe Wu, Zijun Lin, Yeying Jin · Tencent; National University of Singapore; Nanyang Technological University
- <a id="paper-948fc75c37f774f8"></a>**AffordanceWAM: Affordance-Aware Joint World-Action Modeling for Robot Manipulation** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2609.22332)* · [Paper](https://arxiv.org/abs/2609.22332) · [Project](https://skywalker-yqz.github.io/AffordanceWAM/) · [Code](https://github.com/Skywalker-yqz/AffordanceWAM)<br>
  Jiadi You et al. · The University of Hong Kong; Peking University; HKUST (GZ); +3 institutions
- <a id="paper-5bbfa21913204559"></a>**Agentic World Action Models** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.30136)* · [Paper](https://arxiv.org/abs/2610.30136) · [Project](https://agentic-wam.github.io/)<br>
  Zhuoyang Liu et al. · UC Berkeley; NVIDIA; University of Pennsylvania
- <a id="paper-d5842cf69174cd5a"></a>**ALPS: Visual State Encoders for World Models** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.30120)* · [Paper](https://arxiv.org/abs/2610.30120) · [Code](https://github.com/UCSC-VLAA/ALPS) · [Project](https://ucsc-vlaa.github.io/ALPS) · [HF Model](https://huggingface.co/UCSC-VLAA/ALPS)<br>
  Yanqing Liu et al. · University of California, Santa Cruz; Google; University of California, Santa Barbara
- <a id="paper-6a169d3244b9be5d"></a>**Causal Discovery beyond Conditional Independence: Identifiability, Algorithms, and Statistical Inference for Directed Acyclic and Cyclic Graphs** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.23543)* · [Paper](https://arxiv.org/abs/2610.23543)<br>
  Yang Ni · Department of Statistics and Data Science, The University of Texas at Austin
- <a id="paper-5a683d7a781fb5bd"></a>**Causal Discovery for Linear Models with Latent Confounding via Multi-domain Identifiable Representation Learning** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.28134)* · [Paper](https://arxiv.org/abs/2610.28134)<br>
  Danru Xu, Aapo Hyv¨arinen, Sara Magliacane · University of Amsterdam; University of Helsinki; Saarland University
- <a id="paper-a54a51900eb1699c"></a>**Causal Discovery Under Hard Selection Bias: A New Robust Score-Matching Approach** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.18075)* · [Paper](https://arxiv.org/abs/2610.18075)<br>
  Yiwen Qiu, Francesco Montagna, Shimeng Huang, Francesco Locatello · IST Austria
- <a id="paper-7745a2c4bef6fedf"></a>**CausalAlign: Causal Alignment of Video Generation Models for Consistent Ego-Motion** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.29915)* · [Paper](https://arxiv.org/abs/2610.29915) · [Code](https://github.com/PKU-VaLuE-Lab/CausalAlign) · [Project](https://pku-value-lab.github.io/CausalAlign-homepage/)<br>
  Kai Zhu et al. · Peking University; Beijing Institute for General Artificial Intelligence; NVIDIA; +2 institutions
- <a id="cider-fm"></a>**CIDER-FM: Foundation Models for Causal Inference from Diverse Experimental Regimes** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2609.39523)* · [Paper](https://arxiv.org/abs/2609.39523)<br>
  Yuche Gao et al. · University of Cambridge; Max Planck Institute for Intelligent Systems; Prior Labs; +3 institutions
- <a id="paper-22327f3887bd989e"></a>**Code Plans, Diffusion Renders: Open-Ended Generative World Modeling** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2609.26458)* · [Paper](https://arxiv.org/abs/2609.26458) · [Project](https://becauseimbatman0.github.io/CoDeR)<br>
  Zixun Fang et al. · USTC; TongYi Lab
- <a id="paper-e6134b72bb2987fb"></a>**Coupling Noisy Pairwise Knowledge to the DAG Posterior for Causal Discovery** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.04559)* · [Paper](https://arxiv.org/abs/2610.04559)<br>
  Guoliang Xu, James E. Corter · Columbia University
- <a id="paper-c749e943da3bd0cf"></a>**D-World: An Explicit World-Language-Action Model with Recursive Self-Improvement under Dual Control** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.17114)* · [Paper](https://arxiv.org/abs/2610.17114)<br>
  Xuan Wen, Baichao Wang · Geek+
- <a id="paper-6b6e5337c5fddd67"></a>**Decoupled Causal Discovery** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2609.23535)* · [Paper](https://arxiv.org/abs/2609.23535)<br>
  Zhengkang Guan, Fei Wu, Kun Kuang · Zhejiang University
- <a id="paper-9f94bbfaed11244a"></a>**Demistifying Data and Simulator Assumptions in Supervised Causal Discovery** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2609.37446)* · [Paper](https://arxiv.org/abs/2609.37446)<br>
  Pingchuan Ma, Rui Ding, Bojun Huang, Shuai Wang · Zhejiang University of Technology; Microsoft Research Asia; Sony Research; +1 institutions
- <a id="paper-cfc2e6a5c2589e80"></a>**Discrete Score Matching Enables Causal Discovery from Count Data** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2609.39326)* · [Paper](https://arxiv.org/abs/2609.39326)<br>
  Euijong Song, Hyewon Park, Gunwoong Park · Seoul National University
- <a id="paper-65b6e8c3b7795317"></a>**Forecast-Necessary Causal Discovery for Nonlinear Political Panel Data: Feedback, Functional Form, and the Dynamics of Democratization** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2609.34115)* · [Paper](https://arxiv.org/abs/2609.34115)<br>
  Michael Coppedge, Dmitry Zaytsev, Valentina Kuskova · Department of Political Science, University of Notre Dame; Kellogg Institute, University of Notre Dame; Lucy Family Institute for Data & Society, University of Notre Dame
- <a id="paper-b24b420dd674a955"></a>**Functional Causal Discovery via Conditional Covariance Ordering** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2609.27256)* · [Paper](https://arxiv.org/abs/2609.27256)<br>
  Keyu Li, Ruoxu Tan · School of Mathematical Sciences and School of Economics and Management, Tongji University
- <a id="paper-d6361dc4d470facb"></a>**Generalizing Identifiability Results in Causal Discovery from Complete Data to Missing Data Settings** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.19211)* · [Paper](https://arxiv.org/abs/2610.19211)<br>
  Matteo Ceriscioli, Shohei Shimizu, Mallika Gupta, Karthika Mohan · Oregon State University, Causal Intelligence and Reasoning Lab, Corvallis, USA; RIKEN Advanced Intelligence Project, Causal Inference Team, Tokyo, Japan; The University of Osaka, Reasoning for Intelligence Department, Osaka, Japan; +1 institutions
- <a id="paper-03aea9589c54c66f"></a>**Gluing Local Contexts into Global Meaning: A Sheaf-Theoretic Decomposition of Transformer Representations** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.17117)* · [Paper](https://arxiv.org/abs/2610.17117) · [Project](https://cwru-aism.github.io/gluing-lc-page/) · [Code](https://github.com/CWRU-AISM/gluing-lc)<br>
  Bryce Grant, Peng Wang · Case Western Reserve University
- <a id="paper-b9a6b3cf4345027c"></a>**Holi-World: Building Holistic World Intelligence from Human-Ego Experience** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.26549)* · [Paper](https://arxiv.org/abs/2610.26549) · [Project](https://github.com/Ropedia/holi-world) · [HF Model](https://huggingface.co/ropedia-ai/holiworld-vl) · [Dataset](https://huggingface.co/datasets/ropedia-ai/holiworld-data)<br>
  Hao Li et al. · Ropedia; NTU; HKUST; +1 institutions
- <a id="paper-137628e5f45d0875"></a>**How Far Can Coding Agents Go in Visual Generation?** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.19025)* · [Paper](https://arxiv.org/abs/2610.19025)<br>
  Hengguang Zhou et al. · University of California, Los Angeles; Tsinghua University
- <a id="paper-12ca4a45f1a3899a"></a>**Hy-Nomas: Towards Free-form Interactive World Generation** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.36729)* · [Paper](https://arxiv.org/abs/2610.36729) · [Project](https://hy-nomas.hy.tencent.com/) · [Code](https://github.com/Tencent-Hunyuan/Hy-Nomas) · [HF Model](https://huggingface.co/tencent/Hy-Nomas) · [Dataset](https://huggingface.co/datasets/tencent/Hy-Nomas-Bench)<br>
  Tencent Hy Visual Generation Team · Tencent Hy
- <a id="paper-cff6e82a848858e5"></a>**Identifying ODEs from Unstructured Data with Causal Representation Learning** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2609.37083)* · [Paper](https://arxiv.org/abs/2609.37083)<br>
  Alessandro Trenta, Riccardo Massidda, Davide Bacciu, Sara Magliacane · University of Pisa; Saarland Informatics Campus; Saarland University; +1 institutions
- <a id="paper-d4efb0c6a2ce0b19"></a>**ITSY: Causal Discovery From Irregular Time-Series Data** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2609.23516)* · [Paper](https://arxiv.org/abs/2609.23516)<br>
  Wenbo Xu et al. · Renmin University of China; Zhejiang University
- <a id="paper-4934e32c8ead615a"></a>**LaLa-World: Scaling Latent World Models with Natural Language Actions** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.27851)* · [Paper](https://arxiv.org/abs/2610.27851) · [Project](https://june-page.github.io/lala-world/) · [Code](https://github.com/junha1125/LaLa-World)<br>
  Junha Song et al. · NAVER AI Lab; Georgia Institute of Technology; Brown University; +1 institutions
- <a id="paper-4f0706d28b33b8b2"></a>**Language Models as AI Research World Models** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.12235)* · [Paper](https://arxiv.org/abs/2610.12235)<br>
  Zijun Wang et al. · Amazon; UC Santa Cruz; Emory University; +2 institutions
- <a id="paper-b2edd9dbadf5564e"></a>**Learning the 4D World through Point Trajectory Forecasting** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.28594)* · [Paper](https://arxiv.org/abs/2610.28594) · [Project](https://rootyjeon.github.io/video-point-model/) · [Code](https://github.com/rootyJeon/VPM) · [Dataset](https://huggingface.co/datasets/rooty2020/VPM-Data) · [Dataset](https://huggingface.co/datasets/rooty2020/VP-WorldBench) · [HF Model](https://huggingface.co/rooty2020/VPM-DROID)<br>
  Byungwoo Jeon et al. · KAIST; ETH Z¨urich; Seoul National University; +3 institutions
- <a id="paper-c49994cd61004d2c"></a>**Local Fisher Information Enables Sparse Causal Discovery** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.04291)* · [Paper](https://arxiv.org/abs/2610.04291)<br>
  Byeongguk Kang, Donghyeon Lee, Euijong Song, Gunwoong Park · Seoul National University
- <a id="paper-994c8a84ad65793d"></a>**Looking Ahead: Modeling Future Evolution in Autoregressive Video Generation** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.29989)* · [Paper](https://arxiv.org/abs/2610.29989) · [Code](https://github.com/TencentARC/Looking-Ahead) · [Project](https://hellorpg.github.io/looking-ahead/) · [HF Model](https://huggingface.co/TencentARC/Looking-Ahead) · [Dataset](https://huggingface.co/datasets/TencentARC/Looking-Ahead)<br>
  Ruopeng Gao et al. · Nanjing University; ARC Lab, Tencent IEG; Zhejiang University
- <a id="paper-7cea29ac9f6e3f51"></a>**Mapping and Advancing the Scalability-Accuracy Frontier of Nonlinear Causal Discovery** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.03258)* · [Paper](https://arxiv.org/abs/2610.03258)<br>
  Hendrik Suhr, Sascha Xu, Jilles Vreeken · CISPA Helmholtz Center for Information Security
- <a id="paper-f9fb7f276f2a7a00"></a>**MARCEDES: Score-based causal discovery under non-Gaussianity with continuous optimization** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2609.30643)* · [Paper](https://arxiv.org/abs/2609.30643)<br>
  Anamitra Chaudhuri, Anirban Bhattacharya, Yang Ni · Florida State University; Texas A&M University; The University of Texas at Austin
- <a id="paper-7d26a5c9a55b02eb"></a>**Memento 3: Model-Based Recursive Self-Improvement through Reflective Rulebooks** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.11794)* · [Paper](https://arxiv.org/abs/2610.11794)<br>
  Haoyu Zhao et al. · University College London; Huawei Noah’s Ark Lab, UK; University of Liverpool
- <a id="paper-fc860eb46913be72"></a>**MLE-World: Predicting Machine Learning Experiment Outcomes with a Learned World Model** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.37175)* · [Paper](https://arxiv.org/abs/2610.37175) · [Project](https://mle-world.github.io/)<br>
  Brian Ko et al. · University of Washington; University of Illinois at Urbana-Champaign; University of Oxford; +2 institutions
- <a id="paper-87bd413320e9c2f6"></a>**Not All Features Are Created Equal: A Mechanistic Study of Vision-Language-Action Models** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2603.19233)* · [Paper](https://arxiv.org/abs/2603.19233) · [Code](https://github.com/CWRU-AISM/action-atlas) · [Project](https://cwru-aism.github.io/vla-interp-page/) · [Project](https://action-atlas.com/)<br>
  Bryce Grant, Xijia Zhao, Peng Wang · Case Western Reserve University
- <a id="paper-bed2b1a28486dea6"></a>**On the Token Collapse Phenomenon in Textual Graph Soft Prompting** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.31572)* · [Paper](https://arxiv.org/abs/2610.31572) · [Code](https://github.com/difra100/Token_Collapse_KGQA)<br>
  Andrea Giuseppe Di Francesco et al. · Sapienza University of Rome, Rome, Italy; ISTI-CNR, Pisa, Italy; University of Cambridge, Cambridge, UK; +1 institutions
- <a id="paper-11a0170b8097038e"></a>**One Thing Leads to Another: The Essentials of Time Series Causal Discovery** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.13430)* · [Paper](https://arxiv.org/abs/2610.13430) · [Project](https://github.com/CHAI-UK/Awesome-Time-Series-Causal-Discovery)<br>
  Kurt Butler et al. · The University of Edinburgh; Causality in Healthcare AI Hub (CHAI); University College London
- <a id="paper-33f13c12a6d20792"></a>**Oneira: From Open-Ended Generation to Open-World Interaction in Video World Models** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.01614)* · [Paper](https://arxiv.org/abs/2610.01614) · [Project](https://madaoer.github.io/projects/oneira/) · [Code](https://github.com/Madaoer/Oneira) · [HF Model](https://huggingface.co/Madaoer-Otaku/Oneira_example_weights) · [Dataset](https://huggingface.co/datasets/Madaoer-Otaku/Oneira_example_data)<br>
  Xindi Yang et al. · Monash University; University of Bristol; Dalian University of Technology; +2 institutions
- <a id="paper-28263e185eb4c918"></a>**Optimal Correction Sets for Provable Redress of Contestable Causal Discovery** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.33138)* · [Paper](https://arxiv.org/abs/2610.33138) · [Code](https://github.com/briziorusso/ArgCausalDisco)<br>
  Fabrizio Russo et al. · Imperial College London, London, United Kingdom; University of Calabria, Rende, Italy
- <a id="paper-b30aedba981183d1"></a>**OverSeer: Multi-Agent World Models Beyond What Agents See** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.28554)* · [Paper](https://arxiv.org/abs/2610.28554) · [Project](https://runjiali-rl.github.io/OverSeer/)<br>
  Runjia Li et al. · Meta AI; University of Oxford
- <a id="paper-c30ad45a06557efa"></a>**Physis-Lang: Self-Evolving Language as a Physical Representation for Video World Model** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2609.40358)* · [Paper](https://arxiv.org/abs/2609.40358) · [Project](https://elemmire1.github.io/physis-lang/)<br>
  Liming Lu et al. · NVIDIA; MIT; University of Oxford
- <a id="paper-64dc66d0c1650b10"></a>**PhysLDM: Latent Diffusion for High-Fidelity Deformable Simulation** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.07609)* · [Paper](https://arxiv.org/abs/2610.07609) · [Project](https://yucrazing.github.io/physldm/)<br>
  Yu Zhang, Xudong Xu, Xingang Pan · S-Lab, Nanyang Technological University, Singapore; Shanghai Artificial Intelligence Laboratory, Shanghai, China
- <a id="paper-07f581e485bcadb4"></a>**Predictive Closure: A Set-Level Characterization of JEPA's Feature Selection** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.27364)* · [Paper](https://arxiv.org/abs/2610.27364) · [Code](https://github.com/Mosh0110/predictive-closure)<br>
  Mosh Levy, Aly Lidayan, Yoav Goldberg · Bar-Ilan University; University of California, Berkeley; Allen Institute for AI
- <a id="paper-ba5b84051bbc46cb"></a>**Proxy-Adjusted Causal Discovery from Targeted Interventions** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2609.23897)* · [Paper](https://arxiv.org/abs/2609.23897)<br>
  Li Chen, Wei Pan, Xiaotong Shen · University of Minnesota
- <a id="paper-328d19a6d649c766"></a>**Rate-Based Causal Discovery for Heavy-Tailed Models** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.15051)* · [Paper](https://arxiv.org/abs/2610.15051)<br>
  Vishal Routh · University of Georgia
- <a id="paper-07ba9b81fc275bba"></a>**Relational Learning as World Modeling** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.16763)* · [Paper](https://arxiv.org/abs/2610.16763) · [Code](https://github.com/oooranz/TabWM) · [HF Model](https://huggingface.co/oooranz/TabWM)<br>
  Zheyu Zhang, Gjergji Kasneci · Technical University of Munich; Munich Center for Machine Learning (MCML)
- <a id="paper-a77e0de913ae3ba2"></a>**Residual-Based Causal Discovery via Pretrained In-Context Quantile Regression** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.29530)* · [Paper](https://arxiv.org/abs/2610.29530) · [Code](https://github.com/causality-lab/loscar)<br>
  Daniel Klippert, Quang Nhat Huynh, Alexander Marx · TU Dortmund University; Research Center Trustworthy Data Science and Security, University Alliance Ruhr; University of M¨unster
- <a id="paper-8202760640131977"></a>**Right Screen, Wrong Transition: World Models as Verifiers for GUI Agents** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.11942)* · [Paper](https://arxiv.org/abs/2610.11942) · [Code](https://github.com/jiamingzhang94/lgwm) · [Dataset](https://huggingface.co/datasets/jiamingzz/lgwm-data) · [HF Model](https://huggingface.co/jiamingzz/lgwm)<br>
  Jiaming Zhang et al. · Nanyang Technological University; Institute of Science Tokyo; Sony AI
- <a id="paper-9a7fdd3c6dd57014"></a>**Ropedia W0: Scaling Loco-Manipulation World Models across Embodiments with Human Experience** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.26855)* · [Paper](https://arxiv.org/abs/2610.26855) · [Project](https://ropedia.github.io/ropedia-w0/) · [Code](https://github.com/Ropedia/ropedia-w0) · [HF Model](https://huggingface.co/ropedia-ai/Ropedia-W0)<br>
  Tianqi Liu et al. · Nanyang Technological University; Ropedia; Duke University; +2 institutions
- <a id="paper-e0ce81ff789e9233"></a>**RynnUnify: Towards Unified Embodied Brain** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.32965)* · [Paper](https://arxiv.org/abs/2610.32965) · [Code](https://github.com/alibaba-damo-academy/RynnUnify) · [Project](https://alibaba-damo-academy.github.io/RynnUnify.github.io) · [HF Model](https://huggingface.co/Alibaba-DAMO-Academy/RynnUnify-Base) · [HF Model](https://huggingface.co/Alibaba-DAMO-Academy/RynnUnify-Agentic-Reasoner) · [HF Model](https://huggingface.co/Alibaba-DAMO-Academy/RynnUnify-WAM-RoboCasa)<br>
  Minghao Zhu et al. · DAMO Academy, Alibaba Group; Hupan Lab
- <a id="paper-a293907f11982b44"></a>**Sample Dependence-Aware Blind Source Separation for Linear Causal Discovery** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.06656)* · [Paper](https://arxiv.org/abs/2610.06656)<br>
  Cihan Eralp Kumbasar, Emin Erdem Kumbasar, T¨ulay Adali · University of Maryland Baltimore County
- <a id="paper-3d80f1abd6ff2ffd"></a>**ScaleNav: Scalable Internet Video Pretraining for Language-Conditioned Local Navigation** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.25690)* · [Paper](https://arxiv.org/abs/2610.25690) · [Project](https://zju3dv.github.io/ScaleNav/) · [Code](https://github.com/MachEmbodied/ScaleNav)<br>
  Yihui Yang et al. · Zhejiang University; Li Auto Inc.; Shenzhen University
- <a id="paper-9f6561b2a28884a6"></a>**SCDM: Scalable Causal Discovery in Nonlinear Temporal Systems with Meta-Learning** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.29992)* · [Paper](https://arxiv.org/abs/2610.29992) · [Project](https://shaogangren.github.io/SCDM/) · [Code](https://github.com/ShaogangRen/SCDM)<br>
  Jingbo Wang, Kegeng Tang, Zihao Wang, Shaogang Ren · University of Tennessee at Chattanooga
- <a id="paper-e2d8ec7bb639f952"></a>**Self-Distilling Future Video Representations for World Action Models** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.30320)* · [Paper](https://arxiv.org/abs/2610.30320) · [Project](https://huiwon-jang.github.io/FRED/) · [Code](https://github.com/suhyeok-jang/FRED)<br>
  Huiwon Jang et al. · KAIST; RLWRLD
- <a id="paper-ff5ed4b91b994247"></a>**Skeleton-Grounded Latent Action Model for Robot World Models** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.31474)* · [Paper](https://arxiv.org/abs/2610.31474) · [Project](https://aopolin-lv.github.io/SkeLAM/)<br>
  Qi Lv et al. · HIT (Shenzhen); Show Lab, NUS; Ping An Tech
- <a id="paper-fccc1ba3d58415fb"></a>**Slot-JEPA: Object-Structured Prediction Interfaces for Latent World Models** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.28074)* · [Paper](https://arxiv.org/abs/2610.28074) · [Code](https://github.com/KID-7391/Slot-JEPA)<br>
  Peisong Wen et al. · School of Computer Science and Technology, University of Chinese Academy of Sciences; State Key Laboratory of AI Safety, Institute of Computing Technology, Chinese Academy of Sciences; Beijing Academy of Artificial Intelligence; +2 institutions
- <a id="paper-9689553423421d52"></a>**State World Models: Execute the Rules, Generate the Pixels** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.26811)* · [Paper](https://arxiv.org/abs/2610.26811) · [Code](https://github.com/Zhangyr2022/StateWorldModel) · [Project](https://ivg-yanranzhang.github.io/StateWorldModel/) · [Dataset](https://huggingface.co/datasets/Louis0411/StateWorldModel)<br>
  Chan Yan Ki et al. · Department of Automation, Tsinghua University, China; GigaAI
- <a id="paper-bcf3506533d1345c"></a>**Statistical Inference for Causal Discovery under Selection and Latent Variables via Single-Target Interventions** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2609.28856)* · [Paper](https://arxiv.org/abs/2609.28856)<br>
  Xiaotian Hou, Kwangmoon Park, Hongzhe Li · University of Pennsylvania
- <a id="paper-c36a7ebcd0bd12a0"></a>**Steering Black-Box Large Language Model Agents with Pitfall Anticipation World Model** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.29139)* · [Paper](https://arxiv.org/abs/2610.29139)<br>
  Jiongxiao Wang et al. · University of Wisconsin–Madison; AWS AI
- <a id="paper-c7e757199e9fcb15"></a>**The Statistical Cost of Causal Discovery with Feedback** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2609.34050)* · [Paper](https://arxiv.org/abs/2609.34050)<br>
  Sunmin Oh, Seungsu Han, Gunwoong Park · Seoul National University; Princeton University
- <a id="paper-9f0b1afaa9684d4a"></a>**Using Heteroscedasticity for Causal Discovery under Hidden Confounding** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.21219)* · [Paper](https://arxiv.org/abs/2610.21219)<br>
  Jing Zou, Wei Li, Wei Lin · Peking University; Renmin University of China
- <a id="paper-cf2e288d5f7302fd"></a>**VCLMU: Mechanism-Centric Virtual Cell World Modeling for Perturbation Response** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.04475)* · [Paper](https://arxiv.org/abs/2610.04475)<br>
  Yuwei Miao et al. · Johnson & Johnson Innovative Medicine; University of Texas at Arlington
- <a id="paper-6057a7437a99f1c3"></a>**Vision-Language-Delta-Action: Learning Compact Deltas as Actionable Transition Interfaces for Robotic Manipulation** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.25874)* · [Paper](https://arxiv.org/abs/2610.25874) · [Code](https://github.com/baidu-baige/LoongForge/tree/master/cookbook/loongforge-vlda) · [Project](https://baidu-baige.github.io/LoongForge/projects/vlda.html) · [Code](https://github.com/baidu-baige/LoongForge)<br>
  Lingsen Zhang et al. · Harbin Institute of Technology, Shenzhen; Baidu, Inc.; Shenzhen Loop Area Institute
- <a id="paper-25be5f1bd7762386"></a>**What Makes a Good Symbol for Hybrid Discrete-Continuous Planning?** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.23010)* · [Paper](https://arxiv.org/abs/2610.23010) · [Project](https://pyywill.github.io/good-symbols/)<br>
  Yiyuan Pan, Changliu Liu, Jiayuan Mao · Carnegie Mellon University; University of Pennsylvania
- <a id="paper-51b526cf48936017"></a>**World Model Interpretability: From Decoding Representations to Understanding Latent Worlds** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.25296)* · [Paper](https://arxiv.org/abs/2610.25296) · [Project](https://github.com/Jize-W/Awesome-World-Model-Interpretability)<br>
  Jize Wang et al. · School of Automation and Intelligent Sensing, Shang- hai Jiao Tong University; College of Computing and Data Science, Nanyang Technological University
- <a id="paper-4fab9a768e49ef16"></a>**World Models with Configurable Perception** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.27914)* · [Paper](https://arxiv.org/abs/2610.27914) · [Project](https://configwm.github.io) · [Code](https://github.com/yijunshens/ConfigWM) · [Dataset](https://huggingface.co/datasets/YijunShen/ConfigWM)<br>
  Yĳun Shen et al. · East China Normal University; HKUST
- <a id="paper-b7765a43c46af2b6"></a>**WorldStream: Streaming Interactive 3D Worlds with Hierarchical Planning and Persistent State** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.28827)* · [Paper](https://arxiv.org/abs/2610.28827) · [Project](https://krennic999.github.io/WorldStream/) · [Project](https://krennic999.github.io/WorldStream/blog/)<br>
  Xiaoxiao Ma et al. · University of Science and Technology of China; Joy Future Academy, JD

### 2023

- <a id="f06"></a>**DreamCoder: Growing generalizable, interpretable knowledge with wake-sleep Bayesian program learning** · *[Philosophical Transactions of the Royal Society A 2023](https://doi.org/10.1098/rsta.2022.0050)* · [Paper](https://arxiv.org/abs/2006.08381) · [Code](https://github.com/ellisk42/ec)<br>
  Kevin Ellis et al. · MIT; NeuroSpin; Center for Brains, Minds and Machines
- <a id="csiva"></a>**Learning to Induce Causal Structure** · *[ICLR 2023](https://openreview.net/forum?id=hp_RwhKDJ5)* · [Paper](https://arxiv.org/abs/2204.04875)<br>
  Nan Rosemary Ke et al. · DeepMind; Mila; Polytechnique Montréal; +2 institutions

### 2022

- <a id="avici"></a>**Amortized Inference for Causal Structure Learning** · *[NeurIPS 2022](https://proceedings.neurips.cc/paper_files/paper/2022/hash/54f7125dee9b8b3dc798bb9a082b09e2-Abstract-Conference.html)* · [Paper](https://arxiv.org/abs/2205.12934) · [Code](https://github.com/larslorch/avici)<br>
  Lars Lorch et al. · ETH Zurich; Max Planck Institute for Intelligent Systems
- <a id="dag-gflownet"></a>**Bayesian Structure Learning with Generative Flow Networks** · *[UAI 2022](https://proceedings.mlr.press/v180/deleu22a.html)* · [Paper](https://arxiv.org/abs/2202.13903) · [Code](https://github.com/tristandeleu/jax-dag-gflownet)<br>
  Tristan Deleu et al. · Mila, Université de Montréal; Technical University of Munich; KTH Royal Institute of Technology; +1 institutions
- <a id="citris"></a>**CITRIS: Causal Identifiability from Temporal Intervened Sequences** · *[ICML 2022](https://proceedings.mlr.press/v162/lippe22a.html)* · [Paper](https://arxiv.org/abs/2202.03169) · [Code](https://github.com/phlippe/CITRIS)<br>
  Phillip Lippe et al. · University of Amsterdam; MIT-IBM Watson AI Lab; Qualcomm AI Research
- <a id="weakly-supervised-crl"></a>**Weakly supervised causal representation learning** · *[NeurIPS 2022](https://proceedings.neurips.cc/paper_files/paper/2022/hash/fa567e2b2c870f8f09a87b6e73370869-Abstract-Conference.html)* · [Paper](https://arxiv.org/abs/2203.16437) · [Code](https://github.com/Qualcomm-AI-research/weakly-supervised-causal-representation-learning)<br>
  Johann Brehmer, Pim de Haan, Phillip Lippe, Taco Cohen · Qualcomm AI Research; University of Amsterdam

### 2021

- <a id="dibs"></a>**DiBS: Differentiable Bayesian Structure Learning** · *[NeurIPS 2021](https://proceedings.neurips.cc/paper_files/paper/2021/hash/ca6ab34959489659f8c3776aaf1f8efd-Abstract.html)* · [Paper](https://arxiv.org/abs/2105.11839) · [Code](https://github.com/larslorch/dibs)<br>
  Lars Lorch, Jonas Rothfuss, Bernhard Schölkopf, Andreas Krause · ETH Zurich; Max Planck Institute for Intelligent Systems
- <a id="c09"></a>**Towards Causal Representation Learning** · *[Proceedings of the IEEE 2021](https://ieeexplore.ieee.org/document/9363924/)* · [Paper](https://arxiv.org/abs/2102.11107)<br>
  Bernhard Schölkopf et al. · Max Planck Institute for Intelligent Systems; ETH Zurich; Mila / Université de Montréal; +2 institutions

### 2020

- <a id="c14"></a>**Joint Causal Inference from Multiple Contexts** · *[JMLR 2020](https://jmlr.org/papers/v21/17-123.html)* · [Paper](https://jmlr.org/papers/v21/17-123.html) · [Code](https://github.com/caus-am/jci)<br>
  Joris M. Mooij, Sara Magliacane, Tom Claassen · University of Amsterdam; MIT-IBM Watson AI Lab / IBM Research; Radboud University

### 2018

- <a id="c06"></a>**DAGs with NO TEARS: Continuous Optimization for Structure Learning** · *[NeurIPS 2018](https://proceedings.neurips.cc/paper_files/paper/2018/hash/e347c51419ffb23ca3fd5050202f9c3d-Abstract.html)* · [Paper](https://arxiv.org/abs/1803.01422) · [Code](https://github.com/xunzheng/notears)<br>
  Xun Zheng, Bryon Aragam, Pradeep Ravikumar, Eric P. Xing · Carnegie Mellon University

### 2016

- <a id="c08"></a>**Causal inference using invariant prediction: identification and confidence intervals** · *[JRSS Series B 2016](https://academic.oup.com/jrsssb/article/78/5/947/7040653)* · [Paper](https://arxiv.org/abs/1501.01332) · [Code (R)](https://cran.r-project.org/package=InvariantCausalPrediction)<br>
  Jonas Peters, Peter Bühlmann, Nicolai Meinshausen · Max Planck Institute for Intelligent Systems; ETH Zurich

### 2014

- <a id="c07"></a>**Causal Discovery with Continuous Additive Noise Models** · *[JMLR 2014](https://jmlr.org/papers/v15/peters14a.html)* · [Paper](https://jmlr.org/papers/v15/peters14a.html)<br>
  Jonas Peters, Joris M. Mooij, Dominik Janzing, Bernhard Schölkopf · ETH Zurich; University of Amsterdam; Radboud University; +1 institutions

[↑ Contents](#contents)

<a id="sci_methods"></a>

## 🔬 Discovery Reasoning

*How should agents formulate and test hypotheses?*

### 2026

- <a id="paper-dc6f0c55ed5292e7"></a>**Agentic High-Dimensional Bayesian Optimization with Hypothesis- and Evidence-Guided Search** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2609.34281)* · [Paper](https://arxiv.org/abs/2609.34281)<br>
  Zhixuan Gao et al. · State Key Laboratory of Novel Software Technology, Nanjing University; School of Artificial Intelligence, Nanjing University
- <a id="paper-b34e9d0c4929185b"></a>**AI-Driven Reproducibility and Analytical Robustness in Scientific Discovery** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.23845)* · [Paper](https://arxiv.org/abs/2610.23845)<br>
  Shicheng Liu et al. · Stanford University; Databricks AI Research; University of Massachusetts Amherst
- <a id="paper-e998d3a5dbcbbbaa"></a>**ALDER: Discovering the Laws of a World by Acting in It** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2609.33728)* · [Paper](https://arxiv.org/abs/2609.33728)<br>
  Teng Cao, Yu Deng, Quentin Delfosse, Kristian Kersting · Technische Universität Darmstadt; Intrinsic; German Research Center for AI; +1 institutions
- <a id="paper-d66c8d011ed14fbb"></a>**Beyond Natural Language: An Agent-Native Language for Autonomous Science** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2609.25421)* · [Paper](https://arxiv.org/abs/2609.25421) · [Code](https://github.com/ARA-Labs/Lara)<br>
  Yifeng He, Jiachen Liu · ARA Lab
- <a id="paper-6ff4226eb72ddd9f"></a>**Brilliance: toward autonomous computational research in particle accelerator physics** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.15615)* · [Paper](https://arxiv.org/abs/2610.15615) · [Code](https://github.com/Jinyu95/Brilliance)<br>
  Jinyu Wan et al. · Institute of High Energy Physics, Chinese Academy of Sciences; University of Chinese Academy of Sciences; China Spallation Neutron Source
- <a id="paper-684cb6641ea22913"></a>**ConflictGuide: AutoResearch Improves When Competing Behaviors Are Made Visible** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2609.39933)* · [Paper](https://arxiv.org/abs/2609.39933)<br>
  Binqian Xu, Qiran Zou, Xiangbo Shu, Dianbo Liu · National University of Singapore; Nanjing University of Science and Technology
- <a id="paper-ce1931d0c82b17af"></a>**Constrained Decoding: Harmful or Beneficial? Revisiting Its Impact on LLM Performance** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.35328)* · [Paper](https://arxiv.org/abs/2610.35328)<br>
  Ngoc Trinh Hung Nguyen, Alonso Silva, Armen Aghasaryan, Mehwish Alam · T´el´ecom Paris, Institut Polytechnique de Paris; Nokia Bell Labs
- <a id="paper-d0f8ebef91a045e3"></a>**Contextualization of Third-Party Cloud Security Findings** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.08895)* · [Paper](https://arxiv.org/abs/2610.08895)<br>
  Leon Goldberg, Gal Engelberg · Sola Security
- <a id="paper-e8558e860f15ac05"></a>**DAGLoop: Aligning Method Design with Experimental Feedback in Automated AI Research** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.25089)* · [Paper](https://arxiv.org/abs/2610.25089) · [Code](https://github.com/deng34567/DAGLoop)<br>
  Dengyuxing Wang et al. · The Hong Kong University of Science and Technology; Hong Kong Baptist University; Hong Kong Generative AI Research & Development Center; +1 institutions
- <a id="paper-c8b4c6ec0a0c2f8e"></a>**Diffusion Language Models Change Speed Across Tasks and Languages** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.25835)* · [Paper](https://arxiv.org/abs/2610.25835)<br>
  Mohsen Fayyaz et al. · University of California, Los Angeles; CIS, LMU Munich; Munich Center for Machine Learning
- <a id="paper-3545268c96046966"></a>**Distill, Debate, Discover: Grounding Multi-Agent Research Ideation in Graph-Distilled Insights** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.33366)* · [Paper](https://arxiv.org/abs/2610.33366) · [Code](https://github.com/MichelleMa8/InsightAgents)<br>
  Qianran Ma et al. · University of Pennsylvania
- <a id="paper-65e1b24b684787e4"></a>**EPOCH: Reliable Discovery through Evidence-Governed Search** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.06986)* · [Paper](https://arxiv.org/abs/2610.06986)<br>
  Binjie Guo, Aisheng Mo, Ruitong Li, Xinle Deng · Zhejiang University; The University of Hong Kong
- <a id="paper-d940c8c31187f5bf"></a>**Evidence-First Agentic Verification** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.17724)* · [Paper](https://arxiv.org/abs/2610.17724) · [Code](https://github.com/rsanayei/Sauron)<br>
  Reza Sanayei et al. · Scale AI; University of Arizona
- <a id="paper-4be86010ca166aa2"></a>**Experimental Experience Modeling for Autonomous Research** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2609.39392)* · [Paper](https://arxiv.org/abs/2609.39392)<br>
  Wenda Wei et al. · State Key Laboratory of AI Safety; Institute of Computing Technology, Chinese Academy of Sciences; University of Chinese Academy of Sciences; +1 institutions
- <a id="paper-b491323f08b86575"></a>**Failure Recovery via Belief Updates and World Modeling for Long-Horizon Agents** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.18082)* · [Paper](https://arxiv.org/abs/2610.18082)<br>
  Xiyang Wu et al. · University of Maryland; Google; MBZUAI
- <a id="paper-50dc4089b84b69c1"></a>**Formally Verified Autoresearch for Analyzing the Expressivity of Multi-Head Attention** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.25341)* · [Paper](https://arxiv.org/abs/2610.25341) · [Code](https://github.com/VerifiedMechanisms/automlr)<br>
  Karthik Viswanathan, Plamen Dimitrov, Stefano Rocca, Sarayu Sirikonda · Verified Mechanisms; MATS Research; University of California, Berkeley
- <a id="paper-74d382cf780e1dfd"></a>**How AI Agents Discover Scientific Equations: From Hydrotope Rediscovery to New Water-Wave Amplitudes** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.00435)* · [Paper](https://arxiv.org/abs/2610.00435) · [Code](https://github.com/ZihanZhou26/hydrotope_benchmark)<br>
  Zihan Zhou, Digvijay Wadekar, Matias Zaldarriaga · Princeton University; University of Texas at Austin; Institute for Advanced Study
- <a id="paper-1f223adc2e100034"></a>**Insights from Autoresearch for Solar Panel Segmentation** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.10491)* · [Paper](https://arxiv.org/abs/2610.10491) · [Code](https://github.com/VU-AIML/automl4eo-autoresearch-segmentation)<br>
  Justinas Lekavičius, Kürşat Kömürcü, Valentas Gružauskas, Linas Petkevičius · Vilnius University, Institute of Computer Science, Artificial Intelligence Methods Lab; IRISA, Université Bretagne Sud; European Commission Joint Research Centre
- <a id="paper-892f3051f980319f"></a>**Knowledge Manifold Optimization for Scientific Discovery** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.25662)* · [Paper](https://arxiv.org/abs/2610.25662)<br>
  Shigeru Obayashi, Yoshiaki Kawagoe, Kazuhiko Komatsu, Tomonaga Okabe · Institute of Fluid Science, Tohoku University; Department of Aerospace Engineering, Tohoku University; Research Center for Green X-Tech, Tohoku University; +1 institutions
- <a id="paper-bf706b858234e243"></a>**LLM sequential decision making under uncertainty in biochemical domains** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2609.33061)* · [Paper](https://arxiv.org/abs/2609.33061)<br>
  Mattias Akke et al. · Lund University; Stanford; MIT
- <a id="paper-ce6ca28e99a1250e"></a>**LLM-IDEA: Identifiability-Driven Experimental Agent for Autonomous Discovery of Mechanistic World Models** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.11253)* · [Paper](https://arxiv.org/abs/2610.11253) · [Code](https://github.com/Suraskey/llm-idea)<br>
  Surya Shetty, Ulisses Braga-Neto · Texas A&M University; Polara Labs Inc.
- <a id="paper-dd39f6104750943c"></a>**LLM2Cert: LLM Synthesis of Certificates with SMT/Lean Verification** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.30524)* · [Paper](https://arxiv.org/abs/2610.30524) · [Code](https://github.com/FormalCert-AI/llm2cert) · [Project](https://formalcert-ai.github.io/llm2cert/) · [Dataset](https://github.com/FormalCert-AI/llm2cert/tree/main/data)<br>
  Zhipeng Cao et al. · Institute of Software, Chinese Academy of Sciences (CAS); School of Advanced Interdisciplinary Sciences, University of Chinese Academy of Sciences; Language Technologies Institute, School of Computer Science, Carnegie Mellon University; +5 institutions
- <a id="paper-a69e794da1fcd20e"></a>**Measuring Mechanistic Uncertainty in Large Language Models via Causal Robustness** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.22636)* · [Paper](https://arxiv.org/abs/2610.22636)<br>
  Aneesh Komanduri, Majid Afshar, Timothy A. Miller, Yanjun Gao · University of Colorado Anschutz Medical Campus; University of Wisconsin-Madison; Harvard Medical School; +1 institutions
- <a id="paper-28313e64017c36f0"></a>**MERID: Multimodal Exploration via Recursive Self-Improvement Agents for Major Depression Analysis** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2609.36235)* · [Paper](https://arxiv.org/abs/2609.36235) · [Code](https://github.com/DiscoAILab/MERID)<br>
  Lei Liu et al. · Yale University; Zhejiang University; Northwestern University; +3 institutions
- <a id="paper-81a2e2184fd534d5"></a>**MolLean: A Process-Verifiable Language for Chemical Reasoning** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.20459)* · [Paper](https://arxiv.org/abs/2610.20459) · [Project](https://github.com/phenixace/Open-MolLean)<br>
  Jiatong Li, Yatao Bian · National University of Singapore
- <a id="paper-0b0ccb120eb20f9a"></a>**Multi-Agent AI Design of a Nanowatt Biomedical Low-Pass Filter from Topology to Layout** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.28677)* · [Paper](https://arxiv.org/abs/2610.28677) · [Code](https://github.com/MacAnalog/spicexplorer-release)<br>
  Danial Noori Zadeh, Devanshu Prasad, Mohamed B. Elamien · Department of Electrical and Computer Engineering, McMaster University
- <a id="paper-c70675c50ebe2aee"></a>**MultiEcho: An Experimental Science of Learned Worlds** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2609.33347)* · [Paper](https://arxiv.org/abs/2609.33347)<br>
  Meng Zhu, Airui Zhang · SHIHAO XINRUI Group
- <a id="paper-456c7c8f7dcbfa06"></a>**Null Controls Are Necessary but Not Sufficient: Evaluating Acceptance Guards for Scientific Discovery and Interpretability** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.22445)* · [Paper](https://arxiv.org/abs/2610.22445) · [Project](https://real-project-aether.github.io/project-aether/)<br>
  Tianyu Wu · Project Aether
- <a id="paper-c0e89760c2e30631"></a>**Open-ended Scientific Discovery with Possibilistic Reasoning** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.11289)* · [Paper](https://arxiv.org/abs/2610.11289)<br>
  Anita Yang et al. · Lattice Lab, Toyota Motor Corporation, Japan; Department of Computer Science, University of Tokyo, Japan; EPIC Lab, College of Computing & Data Science, Nanyang Technological University, Singapore; +2 institutions
- <a id="paper-1be99c75669dc696"></a>**PACE: Research Proving Agent for Adaptive Conjecture Exploration** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.33690)* · [Paper](https://arxiv.org/abs/2610.33690)<br>
  Shu Miao et al. · Peking University; Nankai University; Fudan University
- <a id="paper-e943a5c4fbfc9794"></a>**Pre-registered tests of solid-state-physics-inspired LLM compression: a cluster-level negative result at small-language-model scale** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2609.34292)* · [Paper](https://arxiv.org/abs/2609.34292)<br>
  Jun-qiang Lu · Department of Physics, University of Puerto Rico
- <a id="paper-20a3bacb4d339fde"></a>**PremiseCheck: Efficient Fact-Checking of Human and AI Peer Reviews** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.21046)* · [Paper](https://arxiv.org/abs/2610.21046) · [Code](https://github.com/OpenLAIR/PremiseCheck) · [Dataset](https://huggingface.co/datasets/songdj/ReviewFact) · [Project](https://openlair.github.io/premisecheck/)<br>
  Dingjie Song et al. · Lehigh University; University of British Columbia; Vector Institute
- <a id="paper-d8ca89c0a96c3e80"></a>**Principia: Test-Time Hypotheses to Principle Construction for Scientific Discovery** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.32195)* · [Paper](https://arxiv.org/abs/2610.32195) · [Code](https://github.com/DongkiKim95/Principia)<br>
  Dongki Kim et al. · KAIST; DeepAuto.ai
- <a id="paper-3f5ff0f0f2d712fe"></a>**Reward Engine: Reward-Centric Self-Evolution for Open-Ended Tool Agents** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.22915)* · [Paper](https://arxiv.org/abs/2610.22915)<br>
  Litong Feng et al. · Huawei openJiuwen Team; Department of Statistics and Data Science, The Chinese University of Hong Kong (CUHK)
- <a id="paper-0b7f8ce49e86db5b"></a>**Robust Explanatory Analysis for Structured Optimization Networks (REASON) in Learning** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.19378)* · [Paper](https://arxiv.org/abs/2610.19378)<br>
  Vahid Jebraeeli, Hamid Krim, Keisuke Fujii · North Carolina State University; Nagoya University
- <a id="paper-0deb0ab403be3bb5"></a>**Scientific Discovery under Validation Congestion via Multi-Fidelity Pairwise Rankings** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.01827)* · [Paper](https://arxiv.org/abs/2610.01827)<br>
  Kevin Tirta Wijaya et al. · University of Bonn; Fraunhofer SCAI; Massachusetts Institute of Technology
- <a id="multiple-hypotheses"></a>**Searching for What Matters: Open-Ended Discovery of Multiple Hypotheses with Agentic Data Exploration** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.17874)* · [Paper](https://arxiv.org/abs/2610.17874)<br>
  Sanchit Kabra et al. · Virginia Tech; Amazon
- <a id="paper-c89da1a6cfaf5632"></a>**Self-Evolving Multi-Agent Symbolic Discovery for Financial Fundamental Analysis** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2609.32746)* · [Paper](https://arxiv.org/abs/2609.32746)<br>
  Kelvin J.L. Koa et al. · National University of Singapore; Asian Institute of Digital Finance; KTH Royal Institute of Technology; +1 institutions
- <a id="paper-afdbb707d7a14074"></a>**Small but Mighty: Test Suites as Improvement Signals for Self-Evolving Agents** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.15964)* · [Paper](https://arxiv.org/abs/2610.15964) · [Code](https://github.com/ccsnow127/TeSearch)<br>
  Yutong Cheng et al. · Virginia Tech; NEC Laboratories America
- <a id="paper-d5a1b1084ce1c261"></a>**TagBO: LLM-Driven Task-Aware Graph Bayesian Optimization for Scientific Discovery** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.14626)* · [Paper](https://arxiv.org/abs/2610.14626)<br>
  Xinzhe Yuan et al. · Shanghai Artificial Intelligence Laboratory; Harbin Institute of Technology; Fudan University; +4 institutions
- <a id="paper-f1ed6530207c60ff"></a>**Thinking-in-Bets at Test Time Reduces Sycophantic Revisions in LLM Agents** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.34654)* · [Paper](https://arxiv.org/abs/2610.34654) · [Project](https://thinking-in-bets.github.io/)<br>
  Nghi D. Q. Bui · Google
- <a id="paper-966010cf5b5a964c"></a>**Triage-PiEvo: Evidence Admission for Principle-Evolving Scientific Agents** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.14683)* · [Paper](https://arxiv.org/abs/2610.14683)<br>
  Peize Li et al. · Westlake University; Kuaishou Technology; Dalian University of Technology; +2 institutions
- <a id="paper-0476a40991c9db1e"></a>**What Output-Only Review Cannot Verify: Study Contracts for Research Agents** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.11754)* · [Paper](https://arxiv.org/abs/2610.11754)<br>
  Eitan Waks, Ben Glocker · Department of Computing, Imperial College London
- <a id="paper-1a7c58d5e92ffdaa"></a>**When Does Feedback Help? Auditing Learned Voltage-Clamp Experimental Design** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.27632)* · [Paper](https://arxiv.org/abs/2610.27632)<br>
  Rayan Nyaupane, Abhiram Bhupatiraju · The University of Texas at Austin

### 2025

- <a id="llm-sr"></a>**LLM-SR: Scientific Equation Discovery via Programming with Large Language Models** · *[ICLR 2025](https://proceedings.iclr.cc/paper_files/paper/2025/hash/28df8e730c054c5331855fd4d5403ba9-Abstract-Conference.html)* · [Paper](https://arxiv.org/abs/2404.18400) · [Code](https://github.com/deep-symbolic-mathematics/LLM-SR)<br>
  Parshin Shojaee et al. · Virginia Tech; Carnegie Mellon University; Allen Institute for AI

### 2024

- <a id="llm-causal-frontier"></a>**Causal Reasoning and Large Language Models: Opening a New Frontier for Causality** · *[TMLR 2024](https://openreview.net/forum?id=RkaqxxAOfN)* · [Paper](https://arxiv.org/abs/2305.00050) · [Code](https://github.com/py-why/pywhy-llm)<br>
  Emre Kıcıman, Robert Ness, Amit Sharma, Chenhao Tan · Microsoft Research; University of Chicago
- <a id="funsearch"></a>**Mathematical discoveries from program search with large language models** · *[Nature 2024](https://www.nature.com/articles/s41586-023-06924-6)* · [Paper](https://www.nature.com/articles/s41586-023-06924-6) · [Code](https://github.com/google-deepmind/funsearch)<br>
  Bernardino Romera-Paredes et al. · Google DeepMind; University of Wisconsin-Madison; University of Lyon

### 2023

- <a id="c05"></a>**Active Causal Structure Learning with Advice** · *[ICML 2023](https://proceedings.mlr.press/v202/choo23a.html)* · [Paper](https://proceedings.mlr.press/v202/choo23a.html) · [Code](https://github.com/cxjdavin/active-causal-structure-learning-with-advice)<br>
  Davin Choo, Themistoklis Gouleakis, Arnab Bhattacharyya · National University of Singapore
- <a id="alphadev"></a>**Faster sorting algorithms discovered using deep reinforcement learning** · *[Nature 2023](https://www.nature.com/articles/s41586-023-06004-9)* · [Paper](https://www.nature.com/articles/s41586-023-06004-9) · [Code](https://github.com/google-deepmind/alphadev)<br>
  Daniel J. Mankowitz et al. · DeepMind; Google
- <a id="pysr"></a>**Interpretable Machine Learning for Science with PySR and SymbolicRegression.jl** · *[arXiv 2023 (preprint)](https://arxiv.org/abs/2305.01582)* · [Paper](https://arxiv.org/abs/2305.01582) · [Code](https://github.com/MilesCranmer/PySR) · [Code (Julia)](https://github.com/MilesCranmer/SymbolicRegression.jl)<br>
  Miles Cranmer · Princeton University; Flatiron Institute
- <a id="react"></a>**ReAct: Synergizing Reasoning and Acting in Language Models** · *[ICLR 2023](https://arxiv.org/abs/2210.03629)* · [Paper](https://arxiv.org/abs/2210.03629) · [Project](https://react-lm.github.io/) · [Code](https://github.com/ysymyth/ReAct)<br>
  Shunyu Yao et al. · Princeton University; Google Research
- <a id="gnome"></a>**Scaling deep learning for materials discovery** · *[Nature 2023](https://www.nature.com/articles/s41586-023-06735-9)* · [Paper](https://www.nature.com/articles/s41586-023-06735-9) · [Code & Data](https://github.com/google-deepmind/materials_discovery)<br>
  Amil Merchant et al. · Google DeepMind; Google Research

### 2022

- <a id="udsr"></a>**A Unified Framework for Deep Symbolic Regression** · *[NeurIPS 2022](https://proceedings.neurips.cc/paper_files/paper/2022/hash/dbca58f35bddc6e4003b2dd80e42f838-Abstract-Conference.html)* · [Paper](https://proceedings.neurips.cc/paper_files/paper/2022/hash/dbca58f35bddc6e4003b2dd80e42f838-Abstract-Conference.html) · [Code](https://github.com/brendenpetersen/deep-symbolic-regression)<br>
  Mikel Landajuela et al. · Lawrence Livermore National Laboratory
- <a id="alphatensor"></a>**Discovering faster matrix multiplication algorithms with reinforcement learning** · *[Nature 2022](https://www.nature.com/articles/s41586-022-05172-4)* · [Paper](https://www.nature.com/articles/s41586-022-05172-4) · [Code](https://github.com/google-deepmind/alphatensor)<br>
  Alhussein Fawzi et al. · DeepMind
- <a id="b05"></a>**How to Stay Curious while Avoiding Noisy TVs using Aleatoric Uncertainty Estimation** · *[ICML 2022](https://proceedings.mlr.press/v162/mavor-parker22a.html)* · [Paper](https://proceedings.mlr.press/v162/mavor-parker22a.html) · [Code](https://github.com/self-supervisor/Escaping-Stochastic-Traps-With-Aleatoric-Mapping-Agents)<br>
  Augustine Mavor-Parker, Kimberly Young, Caswell Barry, Lewis Griffin · University College London; Boston University
- <a id="c04"></a>**Interventions, Where and How? Experimental Design for Causal Models at Scale** · *[NeurIPS 2022](https://proceedings.neurips.cc/paper_files/paper/2022/hash/98a5c0470e57d518ade4e56c6ee0b363-Abstract-Conference.html)* · [Paper](https://arxiv.org/abs/2203.02016) · [Code](https://github.com/yannadani/cbed)<br>
  Panagiotis Tigas et al. · University of Oxford; KTH Royal Institute of Technology; Max Planck Institute for Intelligent Systems; +1 institutions

### 2021

- <a id="deep-symbolic-regression"></a>**Deep symbolic regression: Recovering mathematical expressions from data via risk-seeking policy gradients** · *[ICLR 2021](https://openreview.net/forum?id=m5Qsh0kBQG)* · [Paper](https://arxiv.org/abs/1912.04871) · [Code](https://github.com/brendenpetersen/deep-symbolic-regression)<br>
  Brenden K. Petersen et al. · Lawrence Livermore National Laboratory
- <a id="neural-gp"></a>**Symbolic Regression via Deep Reinforcement Learning Enhanced Genetic Programming Seeding** · *[NeurIPS 2021](https://proceedings.neurips.cc/paper/2021/hash/d073bb8d0c47f317dd39de9c9f004e9d-Abstract.html)* · [Paper](https://proceedings.neurips.cc/paper/2021/hash/d073bb8d0c47f317dd39de9c9f004e9d-Abstract.html) · [Code](https://github.com/brendenpetersen/deep-symbolic-regression)<br>
  T. Nathan Mundhenk et al. · Lawrence Livermore National Laboratory

### 2016

- <a id="f03"></a>**VIME: Variational Information Maximizing Exploration** · *[NeurIPS 2016](https://proceedings.neurips.cc/paper_files/paper/2016/hash/abd815286ba1007abfbb8415b83ae2cf-Abstract.html)* · [Paper](https://arxiv.org/abs/1605.09674) · [Code](https://github.com/openai/vime)<br>
  Rein Houthooft et al. · UC Berkeley; Ghent University / imec; OpenAI

[↑ Contents](#contents)

<a id="learning"></a>

## 🧠 Discovery Training

*How can we train agents to discover?*

### 2026

- <a id="paper-a4026bea93447d03"></a>**Agent World Model in the Wild: Computer-Use Agent Environment Synthesis** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.26828)* · [Paper](https://arxiv.org/abs/2610.26828) · [Project](https://msr-orchard.github.io/WildAWM/) · [Code](https://github.com/MSR-Orchard/WildAWM) · [Dataset](https://huggingface.co/datasets/ChilleD/WildAWM) · [HF Model](https://huggingface.co/ChilleD/WildAWM-35B-A3B) · [HF Model](https://huggingface.co/ChilleD/WildAWM-4B)<br>
  Zhaoyang Wang et al. · UNC-Chapel Hill; Microsoft Research; Georgia Tech; +2 institutions
- <a id="r09"></a>**AgentGym-RL: Training LLM Agents for Long-Horizon Decision Making through Multi-Turn Reinforcement Learning** · *[ICLR 2026](https://proceedings.iclr.cc/paper_files/paper/2026/hash/1571ce1ff735be4551db50887043726e-Abstract-Conference.html)* · [Paper](https://arxiv.org/abs/2509.08755) · [Code](https://github.com/woooodyy/AgentGym-RL) · [Project](https://AgentGym-RL.github.io) · [HF Dataset](https://huggingface.co/datasets/AgentGym/AgentGym-RL-Data-ID)<br>
  Zhiheng Xi et al. · Fudan University; ByteDance Seed; Shanghai Innovation Institute
- <a id="paper-c916585f0ec11b72"></a>**AgenticRoboRL: Bringing Coding-Agent Post-Training to Agentic Robotics** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.28589)* · [Paper](https://arxiv.org/abs/2610.28589) · [Code](https://github.com/xinxinliu-ai/AgenticRoboRL) · [Project](https://l-codingspace.github.io/AgenticRoboRL/) · [HF Model](https://huggingface.co/ciciciciliu/AgenticRoboRL-Qwen3.5-9B/tree/main/rl-v006)<br>
  Xinxin Liu et al. · University of Central Florida; University of Southern California; Michigan State University
- <a id="paper-552b5951a6b715ab"></a>**AlphaDiverse: Post-Training Local Quantitative Research Agents for Diverse Exploration in Alpha Factor Mining** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2609.29014)* · [Paper](https://arxiv.org/abs/2609.29014)<br>
  Qingzhuo Wang, Zikun Wei, Zhihua Wei, Wen Shen · Tongji University; Shanghai Non-convex Intelligent Technology
- <a id="paper-381c08cf57748156"></a>**Amortizing Sequential Experimental Design in Reasoning LLMs** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.20832)* · [Paper](https://arxiv.org/abs/2610.20832)<br>
  Anita Kriz, Antonin Berthon, Nicolás Astorga, Mihaela van der Schaar · University of Cambridge
- <a id="paper-511a84f55bad4b22"></a>**Ask to Distill: Learning to Synthesize Data for On-Policy Distillation** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.27450)* · [Paper](https://arxiv.org/abs/2610.27450) · [Code](https://github.com/GasolSun36/Ask_to_Distill) · [Dataset](https://huggingface.co/datasets/gasolsun/Ask_to_Distill-eval)<br>
  Jiashuo Sun et al. · University of Illinois Urbana-Champaign; The Hong Kong University of Science and Technology; Texas A&M University
- <a id="paper-dff7af28b08d7a75"></a>**Axiomatic World Modeling for Physics Reasoning** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.24519)* · [Paper](https://arxiv.org/abs/2610.24519) · [Project](https://lei-nlp-lab.github.io/physics_reasoning_neurips_2026/) · [Code](https://github.com/lei-nlp-lab/physics_reasoning_neurips_2026)<br>
  Xinye Yang, Zhenyang Liu, Yuxuan Wang, Yuanyuan Lei · Northwestern University; University of Florida
- <a id="paper-50a3bf2dcda6ba17"></a>**Beyond Generator-Specific Shortcuts: Open-World AI-Generated Video Detection via Adversarial Training** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.23906)* · [Paper](https://arxiv.org/abs/2610.23906)<br>
  Qi Zhou et al. · Faculty of Electronic and Information Engineering, Xi’an Jiaotong University
- <a id="paper-5abf8c8643b1a01d"></a>**Breaking Diffusion: Parallel Reasoning with Draft Refinement** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.26542)* · [Paper](https://arxiv.org/abs/2610.26542)<br>
  Jaesang Yu et al. · KAIST; Microsoft Research Asia; SkillBench
- <a id="paper-99e6c99aaec144c3"></a>**Bridged Self-Distillation for On-Policy Learning** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.26397)* · [Paper](https://arxiv.org/abs/2610.26397) · [Code](https://github.com/TUMLegalTech/Bridged-Self-Distillation)<br>
  Runsheng Chen et al. · Technical University of Munich; LMU Munich; Munich Center for Machine Learning (MCML)
- <a id="paper-c3fd4139f7f2c827"></a>**Can Visual Generation Expand What Unified Multimodal Models Know?** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.21459)* · [Paper](https://arxiv.org/abs/2610.21459) · [Project](https://kevinlllee.github.io/Knowledge-Transfer-Probing/) · [Code](https://github.com/kevinlllee/Knowledge-Transfer-Probing)<br>
  Wenkai Li, Wenyi Hong, Zhuoyi Yang, Jie Tang · Tsinghua University; Z.AI
- <a id="h04"></a>**CHART: A Harness-Rotation Curriculum for Harness-Robust Search Agents** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2609.22247)* · [Paper](https://arxiv.org/abs/2609.22247)<br>
  Xinlu Zhang et al. · Amazon
- <a id="paper-081d2afb18f35c00"></a>**Co-adaptive Rule Routing and Constraining for Structured Knowledge Retrieval** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.14465)* · [Paper](https://arxiv.org/abs/2610.14465) · [Code](https://github.com/charlieqi02/Co-Adaptive-Rule-Routing-and-Constraining-Retrieval-)<br>
  Zhisheng Qi et al. · University of Georgia; Michigan State University; Georgia Institute of Technology; +4 institutions
- <a id="paper-127deb898376f43f"></a>**Co-Evolving Acting and Forecasting for Language Agents** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.20597)* · [Paper](https://arxiv.org/abs/2610.20597) · [Code](https://github.com/ulab-uiuc/CoPE)<br>
  Haofei Yu et al. · University of Illinois Urbana-Champaign; University of California San Diego; Meta AI
- <a id="paper-548da90a5e9c3395"></a>**COEVO: Co-Evolving Context and Parameters for Recursive Self-Improvement** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2609.33398)* · [Paper](https://arxiv.org/abs/2609.33398)<br>
  Siwei Chen et al. · Peking University; Emotional Machine
- <a id="compute-aligned"></a>**Compute Aligned Training: Optimizing for Test Time Inference** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2604.24957)* · [Paper](https://arxiv.org/abs/2604.24957) · [Code](https://github.com/adamoosya/compute-aligned-training)<br>
  Adam Ousherovitch, Ambuj Tewari · University of Michigan
- <a id="paper-09c58b5352e897c3"></a>**CoworkEnv: Synthesizing Training Environments for Long-Horizon Cowork Agents** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.24960)* · [Paper](https://arxiv.org/abs/2610.24960) · [Code](https://github.com/HKUST-KnowComp/CoworkEnv) · [Project](https://github.com/zhongweixie/CoworkEnv-Lessons) · [HF Model](https://huggingface.co/zhongweixie/PocketWorker-8B-ClawEval-SFT)<br>
  Zhongwei XIE et al. · The Hong Kong University of Science and Technology; The Chinese University of Hong Kong; Hong Kong Baptist University; +1 institutions
- <a id="paper-0b814b1f03c2835d"></a>**CURIO: Curiosity-Driven Test-Time Learning for Open-Ended Discovery** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.04851)* · [Paper](https://arxiv.org/abs/2610.04851) · [Project](https://ft2023.github.io/CURIO/) · [Code](https://github.com/ft2023/CURIO)<br>
  Tao Feng et al. · University of Illinois Urbana-Champaign; University of Maryland, College Park; Stanford University
- <a id="paper-008b443e8ade0e00"></a>**Deep Fusion Memory: A Chunk-Level Parametric Memory for Large Language Models** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.25100)* · [Paper](https://arxiv.org/abs/2610.25100)<br>
  Rubin Wei et al. · LUMIA Lab, School of Artificial Intelligence, Shanghai Jiao Tong University; Shanghai Artificial Intelligence Laboratory
- <a id="paper-5fc86e0f1760f581"></a>**DeLoop: Repeated Actions as Self-Supervision for Long-Horizon Agents** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.19376)* · [Paper](https://arxiv.org/abs/2610.19376) · [Project](https://github.com/cskyl/deloop)<br>
  Tianle Chen et al. · Google; Boston University; University of Washington; +2 institutions
- <a id="paper-fbc297b42e444ceb"></a>**Did the Model Use That? Counterfactual Training Boosts Self-Attribution in Language Models** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.35295)* · [Paper](https://arxiv.org/abs/2610.35295) · [Code](https://github.com/stanford-oval/CREDIT)<br>
  Zikai Zhou et al. · Stanford University; Duke University; Emory University; +1 institutions
- <a id="paper-0e9154958b34b909"></a>**Direct Self-Evolving Optimization: Evolving LLMs without Challenger Training** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2609.34279)* · [Paper](https://arxiv.org/abs/2609.34279)<br>
  Yuyang Deng, Yu Wang, Jiayun Wang · Accenture, Center for Advanced AI; Georgia Institute of Technology
- <a id="paper-3ec8fb151cd77aab"></a>**DiscoDemo: Discovering Efficient and Diverse Robot Demonstrations for Imitation Learning** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.32093)* · [Paper](https://arxiv.org/abs/2610.32093) · [Project](https://davian-robotics.github.io/DiscoDemo/) · [Code](https://github.com/DAVIAN-Robotics/DiscoDemo) · [Dataset](https://huggingface.co/datasets/DAVIAN-Robotics/DiscoDemo-Stage2_GenData-PnP_Banana) · [HF Model](https://huggingface.co/DAVIAN-Robotics/DiscoDemo-Stage3_SFT-PnP_Banana)<br>
  Minho Park et al. · KAIST; Holiday Robotics
- <a id="paper-98c6269e3dfb0ba6"></a>**Does Learning Protein Folding Generalize to Broader Reasoning?** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2609.38879)* · [Paper](https://arxiv.org/abs/2609.38879) · [Code](https://github.com/GENTEL-lab/Fold2Reason) · [Dataset](https://huggingface.co/datasets/GENTEL-Lab/FoldingCorpus) · [Dataset](https://huggingface.co/datasets/GENTEL-Lab/FTB-Core-v1) · [HF Model](https://huggingface.co/GENTEL-Lab/Fold2Reason-Qwen3.5-9B)<br>
  Yong Liu et al. · Shanghai Jiao Tong University; Fudan University; Shanghai Innovation Institute; +1 institutions
- <a id="paper-438dade489ddfb5b"></a>**Dr. Free: You Don't Need Difficulty Rewards for Self-Evolving Search Agents** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2609.33565)* · [Paper](https://arxiv.org/abs/2609.33565)<br>
  Zhipeng Qian et al. · VCIP, School of Computer Science, Nankai University; Kuaishou Technology; Xiamen University
- <a id="paper-8e34a7493e3c3928"></a>**Dr.Credit: Rubric-Grounded Process Credit Assignment for Deep Research Agents** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2609.34296)* · [Paper](https://arxiv.org/abs/2609.34296)<br>
  Yingjian Zhu et al. · School of Artificial Intelligence, University of Chinese Academy of Sciences; State Key Laboratory of Multimodal Artificial Intelligence Systems (MAIS), Institute of Automation, Chinese Academy of Sciences; Alibaba Token Hub, Alibaba Group; +1 institutions
- <a id="paper-424fdb621545a108"></a>**DynaFlow: Learning Free-Form Multi-Agent Orchestration** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.34467)* · [Paper](https://arxiv.org/abs/2610.34467) · [Code](https://github.com/amiya-special/Dynaflow) · [Project](https://amiya-special.github.io/DynaFlow-website)<br>
  Ruhao Liu, Qi Li, Shizun Wang, Xinchao Wang · National University of Singapore
- <a id="paper-f403a911c87fbaff"></a>**Eat Your Precision: Precision Objective Mitigates Reward Hacking in Rubric-based RL** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.33512)* · [Paper](https://arxiv.org/abs/2610.33512) · [Code](https://github.com/JHKim631/FORK)<br>
  Hyun Ryu et al. · KAIST AI; Carnegie Mellon University Language Technologies Institute
- <a id="paper-fd98d0ad6f9d37a7"></a>**ECHO: Efficient Causal Self-Recursion Beyond Auxiliary Multi-Token Prediction** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.24766)* · [Paper](https://arxiv.org/abs/2610.24766) · [Code](https://github.com/ernie-research/ECHO)<br>
  Yuxuan Zhou et al. · ERNIE Team, Baidu; Independent Researcher
- <a id="paper-d3da834b254c9317"></a>**EnvLunch: The Environment as a Free Lunch for Learning to Interact** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.33817)* · [Paper](https://arxiv.org/abs/2610.33817) · [Code](https://github.com/thinkwee/EnvLunch)<br>
  Wei Liu, Min Gao, Yali Du, Yulan He · King’s College London; Chongqing University; The Alan Turing Institute
- <a id="paper-6c921d13d0b14a4e"></a>**Evolve on Graph: Self-Evolving Knowledge Graph Reasoning without Question Annotations** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.35598)* · [Paper](https://arxiv.org/abs/2610.35598) · [Project](https://szy5.github.io/EoG/) · [Code](https://github.com/Szy5/EoG) · [HF Model](https://huggingface.co/Bobzong/EoG)<br>
  Zongyuan Sun et al. · Beijing University of Posts and Telecommunications; University of Helsinki; University of Amsterdam; +1 institutions
- <a id="paper-d0a1aad7216e9e1d"></a>**Evolving in Thought Space: Training a Small Model at Test Time Unlocks Better Discoveries** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.06269)* · [Paper](https://arxiv.org/abs/2610.06269) · [Code](https://github.com/Human-Agent-Society/reef/tree/main/recipes/tttd/examples/guidance_ttt) · [Project](https://www.reefinfra.ai/docs/user-guide/recipes/guidance-ttt/)<br>
  Chonghe Jiang et al. · Massachusetts Institute of Technology; Hong Kong Polytechnic University; ByteDance Inc.; +6 institutions
- <a id="r05"></a>**Explore More, Drift Less: Outcome-Only Reinforcement Learning Can Suffice for Long-Horizon Interactive Agents** · *[arXiv 2026 (preprint)](https://arxiv.org/html/2609.01245v1)* · [Paper](https://arxiv.org/html/2609.01245v1)<br>
  Liming Pu et al.
- <a id="paper-687abc7b122b3288"></a>**False Frontiers: Diagnosing and Mitigating Co-Cheating in Self-Evolving Search Agents** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2609.39102)* · [Paper](https://arxiv.org/abs/2609.39102)<br>
  Meijia Chen et al. · Rutgers University; Independent Researcher; University of California, San Diego; +3 institutions
- <a id="paper-795331a5c91b086f"></a>**FC-SWE: Failure-Conditioned RL for Long-Horizon Software Engineering Agents** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.07898)* · [Paper](https://arxiv.org/abs/2610.07898)<br>
  Jia Liufu et al. · NVIDIA; Tsinghua University
- <a id="paper-339e82eef6e4a8b6"></a>**From Valid to Useful: Post-Verification Acquisition for Recursive Self-Improving Recommendation** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.04302)* · [Paper](https://arxiv.org/abs/2610.04302)<br>
  Tonmoy Hasan et al. · Nubank
- <a id="paper-98824c70837642db"></a>**Function-Space Temporal Self-Distillation for Policy Optimization** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.19687)* · [Paper](https://arxiv.org/abs/2610.19687)<br>
  Aryan Das, Arnab Bhattacharya, Vinay Kumar Verma · Indian Institute of Technology Kanpur, India
- <a id="paper-0b82946374e2d1ff"></a>**GRADS: Graph-Regulated Agentic Data Synthesis with Controllable Difficulty** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.21167)* · [Paper](https://arxiv.org/abs/2610.21167)<br>
  Gaocheng Yang et al. · Johns Hopkins University; Nanjing University; Amazon
- <a id="paper-c4a481fb0af0b157"></a>**Group-Marginalized Self-Rewarding RL Drives Zero-Label Self-Evolving** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2609.36750)* · [Paper](https://arxiv.org/abs/2609.36750)<br>
  Yiming Wang et al. · Shanghai Jiao Tong University; Tencent
- <a id="paper-843cdbc0b49a3683"></a>**Harness Scaling for Generalizable Agentic Reinforcement Learning** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.29458)* · [Paper](https://arxiv.org/abs/2610.29458)<br>
  Fei Bai et al. · Gaoling School of Artificial Intelligence, Renmin University of China; IQuest Research; Beihang University
- <a id="paper-0182cce120aad869"></a>**HarnessRL: Co-Evolving Policies with a Just-in-Time Training Harness for Open-Ended RL** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.26426)* · [Paper](https://arxiv.org/abs/2610.26426) · [Code](https://github.com/Tongyi-ConvAI/Qwen-Character/tree/main/HarnessRL)<br>
  Xiaoqiang Wang et al. · Alibaba Token Hub, Alibaba Group; Université de Montréal; Mila - Quebec AI Institute
- <a id="paper-990a9823b1d96f35"></a>**Hindsight Structured Advice Distillation: Steering Executor Agents with Advisors Trained on Their Failures and Task Characteristics** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.13000)* · [Paper](https://arxiv.org/abs/2610.13000) · [Project](https://samaya.ai/blog/hindsight-structured-advice-distillation)<br>
  O. Ozan Koyluoglu · Samaya AI
- <a id="paper-48d5ab7e8e8c0f56"></a>**HybridResearcher: Bridging the Structured-Unstructured Boundary for Deep Research Agents** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.24899)* · [Paper](https://arxiv.org/abs/2610.24899)<br>
  Soyoung Yoon et al. · Seoul National University; University of California, Los Angeles; University of North Carolina at Chapel Hill; +2 institutions
- <a id="paper-b62cde245db5c0cf"></a>**IdeaScientist: Orchestrating Agents for Grounded Scientific Ideation** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.04074)* · [Paper](https://arxiv.org/abs/2610.04074) · [Code](https://github.com/jiarui-liu/IdeaScientist) · [Dataset](https://huggingface.co/datasets/Jerry999/SvalbardIdeaVault)<br>
  Jiarui Liu et al. · Carnegie Mellon University; Meta Reality Labs; FAIR at Meta; +5 institutions
- <a id="paper-c474fbc2967f22ed"></a>**Inherited, Not Invented: Tracing the Provenance of Wait in Reasoning Models** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.30882)* · [Paper](https://arxiv.org/abs/2610.30882)<br>
  Zhizhuo Kou et al. · The Hong Kong University of Science and Technology; Peking University; Huawei Noah’s Ark Lab
- <a id="paper-ac8626d0b39c368e"></a>**Interlock: From Local Correctness to Task Completion in Long-Horizon Agents** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.19686)* · [Paper](https://arxiv.org/abs/2610.19686)<br>
  Linji Hao et al. · Peking University; The Hong Kong University of Science and Technology (Guangzhou); Tsinghua University; +1 institutions
- <a id="paper-8d7f564fd9f13e27"></a>**Judging the Justification: Decision Certificate Supervision for Generative Reward Models** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.27528)* · [Paper](https://arxiv.org/abs/2610.27528) · [Code](https://github.com/UConn-DSIS/DeCert) · [HF Model](https://huggingface.co/gqbond/DeCert-Llama-3.1-8B)<br>
  Guiquan Sun, Bing Bai, Martin Renqiang Min, Dongjin Song · School of Computing, University of Connecticut; NEC Labs America
- <a id="paper-b1b56960665af09f"></a>**Ladders of Thought: A Self-Evolving Curriculum of Progressively Simplified Reasoning Traces** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2609.25643)* · [Paper](https://arxiv.org/abs/2609.25643)<br>
  Minghui Liu et al. · University of Maryland, College Park; Capital One
- <a id="paper-ff790d2b9ae4b233"></a>**Language Models Learn to Improve Language Models** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.23344)* · [Paper](https://arxiv.org/abs/2610.23344)<br>
  Minhua Lin et al. · The Pennsylvania State University; UC Santa Cruz; Emory University; +2 institutions
- <a id="gollum"></a>**Large language models as uncertainty-calibrated optimizers for experimental discovery** · *[Nature Machine Intelligence 2026](https://www.nature.com/articles/s42256-026-01283-z)* · [Paper](https://www.nature.com/articles/s42256-026-01283-z) · [Preprint](https://arxiv.org/abs/2504.06265) · [Code](https://github.com/schwallergroup/gollum)<br>
  Bojana Ranković, Ryan-Rhys Griffiths, Philippe Schwaller · École Polytechnique Fédérale de Lausanne (EPFL); NCCR Catalysis, EPFL; QuantumGreen
- <a id="paper-a97c1f5a709e4de6"></a>**Lean4AgenticRL: Advancing Agentic RL with Verifiable Multi-level Process Rewards** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.22448)* · [Paper](https://arxiv.org/abs/2610.22448) · [Code](https://github.com/RickySkywalker/Lean4AgenticRL) · [HF Model](https://huggingface.co/amazon/LAR-27B)<br>
  Ruida Wang, Gerald Friedland, Tong Zhang, Chris Kong · Amazon Web Services; University of Illinois Urbana-Champaign
- <a id="paper-44d308ca6f63a0d7"></a>**LeanPRM: Lean-Grounded Process Supervision for Natural Language Proof Verification** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.17697)* · [Paper](https://arxiv.org/abs/2610.17697) · [Project](https://rlafuente.com/lean-prm) · [Code](https://github.com/pavelslab-nyu/LeanPRM) · [Dataset](https://huggingface.co/datasets/pavelslab-nyu/LeanPRM/tree/main/data) · [Dataset](https://huggingface.co/datasets/pavelslab-nyu/LeanPRM/tree/main/benchmark)<br>
  Rodney Lafuente-Mercado et al. · University of Texas at Austin; University of California, Los Angeles; New York University
- <a id="paper-56ebfe7910628572"></a>**Learning and Reasoning with Geometry: How Generation Helps Spatial Understanding** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.36022)* · [Paper](https://arxiv.org/abs/2610.36022) · [Code](https://github.com/hku-sail/GeoUG)<br>
  Rui Yang et al. · The University of Hong Kong; Shanghai Jiao Tong University; ByteDance Seed
- <a id="paper-bc757bb51b5cc488"></a>**Learning to Think and Explore in 3D World** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.21783)* · [Paper](https://arxiv.org/abs/2610.21783) · [Project](https://williamium3000.github.io/act3d/)<br>
  Yijiang Li, Bingyang Wang, Nuno Vasconcelos · University of California San Diego; Georgia Institute of Technology
- <a id="paper-0cf18f180d63c3e4"></a>**Learning What to Investigate Next: Meta-Reasoning for Long-Horizon Research Agents** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.02525)* · [Paper](https://arxiv.org/abs/2610.02525)<br>
  Ankur Samanta et al. · Meta AI; Columbia University; Tel Aviv University
- <a id="paper-fcce4784f34771ef"></a>**Long-MDR: Long-Context Reinforcement Learning for Multimodal Deep-Research Agents** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.05195)* · [Paper](https://arxiv.org/abs/2610.05195)<br>
  Tang On Tai, Huanyao Zhang, Jiepeng Zhou, Wentao Zhang · The Hong Kong University of Science and Technology (HKUST); Peking University; The Hong Kong University of Science and Technology (Guangzhou)
- <a id="paper-07ae5adf14031356"></a>**MELD: Recursive Self-Improvement via Hierarchical Coordination for Multi-Agent Scientific Discovery** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.24454)* · [Paper](https://arxiv.org/abs/2610.24454)<br>
  Sizhe Tang, Zuyuan Zhang, Zeyu Fang, Tian Lan · George Washington University
- <a id="paper-03627392f7accc23"></a>**MLExpert: Towards a Generalist Agentic Model for Autonomous Machine Learning Engineering** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.22344)* · [Paper](https://arxiv.org/abs/2610.22344) · [Code](https://github.com/InternScience/MLExpert) · [HF Model](https://huggingface.co/InternScience/MLExpert)<br>
  Shangheng Du et al. · East China Normal University; Shanghai Artificial Intelligence Laboratory
- <a id="paper-080ac6ed1ce6901d"></a>**MMVistaReason: Toward Open-Data and Post-Training Recipes for Multimodal Reasoning** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.01352)* · [Paper](https://arxiv.org/abs/2610.01352) · [Code](https://github.com/JackieForest/MMVistaReason) · [Dataset](https://huggingface.co/datasets/JackieLin0123/MMVistaReason-SFT-528K) · [Dataset](https://huggingface.co/datasets/JackieLin0123/MMVistaReason-RL-63K)<br>
  Juekai Lin et al. · Zhejiang University; Ant Group, AFu Team; Shanghai Jiao Tong University; +1 institutions
- <a id="paper-e2843f98db0b548f"></a>**More: Mode-Optimized Reasoning with Self-Adaptive Effort for Self-Evolving Agents** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.33684)* · [Paper](https://arxiv.org/abs/2610.33684)<br>
  Dianxing Shi, Dingjie Fu, Tianyu Lei, Wangjie Qiu · Beihang University; Huazhong University of Technology
- <a id="paper-572a65a52169b4df"></a>**MultiAgent-OPD: End-to-End Training of Hierarchical Multi-Agent Systems with On-Policy Distillation** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.23234)* · [Paper](https://arxiv.org/abs/2610.23234)<br>
  Yuhan Sun et al. · Alibaba Group; Zhejiang University
- <a id="paper-2d09cb91206e5f2c"></a>**Muse Glimmer 30B: An On-Device Agentic Model** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.24628)* · [Paper](https://arxiv.org/abs/2610.24628) · [HF Model](https://huggingface.co/meta-models/Muse-Glimmer-30B)<br>
  Muse Glimmer team et al. · Meta Superintelligence Labs
- <a id="paper-f2d49208f39c3a48"></a>**My FAULT: Self-Diagnosis as Credit Assignment in Self-Evolving Agentic Reinforcement Learning** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.01161)* · [Paper](https://arxiv.org/abs/2610.01161)<br>
  Yihua Zhu et al. · Alibaba Group; Kyoto University; NII LLMC; +6 institutions
- <a id="paper-15ebd2f0c38c3b18"></a>**OneSearch-VL: Unified Multimodal Deep Research Agent for Image and Video** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.12419)* · [Paper](https://arxiv.org/abs/2610.12419) · [Code](https://github.com/appletea233/OneSearch-VL) · [HF Model](https://huggingface.co/OneSearch-VL/OneSearch-VL-8B) · [Dataset](https://huggingface.co/datasets/OneSearch-VL/OneSearch-VL-SFT-110K) · [Dataset](https://huggingface.co/datasets/OneSearch-VL/OneSearch-VL-RL-10K) · [Dataset](https://huggingface.co/datasets/OneSearch-VL/OneSearch-MI-Bench) · [Dataset](https://huggingface.co/datasets/OneSearch-VL/OneSearch-Video-Bench)<br>
  Hongyu Li et al. · BUAA; CUHK; NTU; +2 institutions
- <a id="paper-75eeeb130b15e1f6"></a>**PAR: Progress-Aligned Recurrence for Length Generalization in State Tracking** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.27628)* · [Paper](https://arxiv.org/abs/2610.27628)<br>
  Pan Wang et al. · Ant International; National University of Singapore
- <a id="paper-b489367d0862d8cb"></a>**ParaAgent: Reinforcing Parallel Acting in Open-World Tool Environments** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2609.33618)* · [Paper](https://arxiv.org/abs/2609.33618) · [Code](https://github.com/yueshengbin/paraagent) · [Dataset](https://huggingface.co/datasets/ShengbinYue/paraagent-sft) · [Dataset](https://huggingface.co/datasets/ShengbinYue/paraagent-rl) · [Dataset](https://huggingface.co/datasets/ShengbinYue/ToolEnv-sft) · [HF Model](https://huggingface.co/ShengbinYue/ToolEnv-14B)<br>
  Shengbin Yue et al. · Fudan University; Shanghai Innovation Institute; University of Edinburgh; +3 institutions
- <a id="paper-42c099672148be7f"></a>**POSEIDON: Scaling Training Environments for Scientific Agents from Code Repositories** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.32448)* · [Paper](https://arxiv.org/abs/2610.32448)<br>
  Qifan Zhang et al. · The Hong Kong University of Science and Technology (Guangzhou); Hunyuan Team, Tencent
- <a id="paper-1cf7caf1e3962092"></a>**Predicting Privileged Information Effectiveness for On-Policy Self-Distillation** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.22512)* · [Paper](https://arxiv.org/abs/2610.22512) · [Code](https://github.com/zkjzou/PI-OPSD)<br>
  Kaijian Zou et al. · University of Michigan – Ann Arbor; Mila; Scale AI
- <a id="paper-43d941c286c670db"></a>**ProAS: A Progress-Aware Advantage Shaping Framework for Multi-Turn Agentic Reinforcement Learning** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.18683)* · [Paper](https://arxiv.org/abs/2610.18683) · [Code](https://github.com/LINs-lab/ProAS)<br>
  Bowen Ding et al. · Zhejiang University; School of Engineering, Westlake University; Institute of Advanced Technology, Westlake Institute for Advanced Study; +1 institutions
- <a id="paper-06be42075e2fd31a"></a>**Progress-Aware Distillation for Mitigating Stagnation in Small Language Model Agents** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.19439)* · [Paper](https://arxiv.org/abs/2610.19439) · [Code](https://github.com/CaoYuanpu/ProD)<br>
  Yuanpu Cao et al. · The Pennsylvania State University; Microsoft CoreAI
- <a id="paper-9d6f1aaa601bd596"></a>**Recursive Self-Improvement in Unified Multimodal Models** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.03002)* · [Paper](https://arxiv.org/abs/2610.03002)<br>
  Huijuan Wang et al. · University of Southern California; University of California San Diego; Carnegie Mellon University
- <a id="paper-20899a0b6ded457f"></a>**Recursive Self-Improvement via On-Policy Distillation for Reasoning** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2609.30652)* · [Paper](https://arxiv.org/abs/2609.30652)<br>
  Shangjian Yin et al. · Meta AI; University of California, Riverside
- <a id="paper-77674d7f948270f6"></a>**Rollback: Experience Backtracking in World Models for Policy Improvement** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.36068)* · [Paper](https://arxiv.org/abs/2610.36068) · [Project](https://rollback-wm.github.io/)<br>
  Jiayi Luo et al. · AgiBot; BUAA; NUS
- <a id="paper-6458fcd3e61718e0"></a>**RSIPO: Recursive Self-Improving Policy Optimization for Agentic Reinforcement Learning via Skill-Policy Co-Evolution** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.15772)* · [Paper](https://arxiv.org/abs/2610.15772) · [Code](https://github.com/zfkarl/RSIPO) · [HF Model](https://huggingface.co/Karl28/RSIPO-Qwen2.5-7B-Instruct-ALFWorld) · [HF Model](https://huggingface.co/Karl28/RSIPO-Qwen2.5-7B-Instruct-Search)<br>
  Fan Zhang et al. · CUHK; THU; NUS; +5 institutions
- <a id="paper-0687e07a2193b7e6"></a>**Rubric-CEPR: Self-Evolving Image Editing via Reward-Verified Self-Distillation** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.12469)* · [Paper](https://arxiv.org/abs/2610.12469) · [Code](https://github.com/riteshthawkar/Rubric-CEPR) · [Project](https://riteshthawkar.github.io/Rubric-CEPR/)<br>
  Ritesh Thawkar, Shubham Patle, Shravan Venkatraman, Rao Muhammad Anwer · Mohamed bin Zayed University of Artificial Intelligence; Aalto University
- <a id="paper-3b7f2fe0b2750f8f"></a>**S3AC: Stabilized, Selective, and Scalable Actor-Critic for LLM Reasoning** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.35518)* · [Paper](https://arxiv.org/abs/2610.35518)<br>
  Shuo Shen et al. · Shanghai AI Laboratory; Independent Researcher
- <a id="paper-f5ebfafb83c6121b"></a>**Scaling in Games: Continued Pre-Training For Embodied Agents In Diverse Virtual Worlds** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.28698)* · [Paper](https://arxiv.org/abs/2610.28698) · [Project](https://gamescaling.github.io) · [Code](https://github.com/THUSI-Lab/GameScaling) · [HF Model](https://huggingface.co/THUSI-Lab/GameScaling-9B-S1)<br>
  Kuan Zhang et al. · miHoYo Honkai AI R&D Team; College AI, Tsinghua University; University of Chinese Academy of Sciences; +3 institutions
- <a id="d05"></a>**Scaling Scientific Discovery Environments for Turn-Level Agentic RL** · *[arXiv 2026 (preprint)](https://arxiv.org/html/2607.28990v1)* · [Paper](https://arxiv.org/html/2607.28990v1)<br>
  Yucheng Xu et al. · Shanghai AI Laboratory
- <a id="paper-1ff51f6d4550cdeb"></a>**Self-Credit: Credit Assignment for Long-Horizon Agentic RL via Intra-group Rescaling** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.28388)* · [Paper](https://arxiv.org/abs/2610.28388)<br>
  Fangcong Yin et al. · Meta; New York University; Duke University
- <a id="paper-e55ba0ce535c45d0"></a>**Self-Evaluating Recursive Agents** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.04902)* · [Paper](https://arxiv.org/abs/2610.04902) · [Code](https://github.com/OliverLeeXZ/SERA) · [Dataset](https://github.com/OliverLeeXZ/SERA/blob/main/Dataset/README.md) · [HF Model](https://huggingface.co/Litux12138/SERA)<br>
  Tianyi Lyu et al. · Tongji University; Independent; Shanghai Artificial Intelligence Laboratory; +3 institutions
- <a id="paper-dc899dc4881918fb"></a>**Self-Evolve With a Reference:Anchored Training of Tool-Integrated Agents** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.09856)* · [Paper](https://arxiv.org/abs/2610.09856)<br>
  Wenjie Liao, Liangjie Zhao, Zehong Cao · Waseda University; Adelaide University
- <a id="paper-0a41cf93b0ee9088"></a>**Self-Evolving Algorithm-Design Agents: Escaping In-Context Evolutionary Stagnation via Population-Curated Policy Optimization** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2609.38757)* · [Paper](https://arxiv.org/abs/2609.38757)<br>
  Chen Lu et al. · State Key Laboratory of Novel Software Technology, Nanjing University, China; School of Artificial Intelligence, Nanjing University, China; Huawei Noah’s Ark Lab, China
- <a id="paper-4524ae6f78d2baaf"></a>**SeOPD: Self-Evolving LLMs via Online Policy Distillation from Self-Generated Chain-of-Thought** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2609.33181)* · [Paper](https://arxiv.org/abs/2609.33181)<br>
  Xiaoshu Chen, Sihang Zhou, Ke Liang, Xinwang Liu · National University of Defense Technology
- <a id="paper-b0a747f7d53aca09"></a>**SmoothOperator: Enhancing Representations for Fine-grained Open-set Recognition via Modulated Label Smoothing** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.00851)* · [Paper](https://arxiv.org/abs/2610.00851)<br>
  Thiru Thillai Nadarasar Bahavan, Yu Xia, Sachith Seneviratne, Saman Halgamuge · The University of Melbourne
- <a id="r06"></a>**SPROUT: Scaling Agentic Reinforcement Learning for Long-Horizon Software Engineering** · *[arXiv 2026 (preprint)](https://arxiv.org/html/2610.14405v1)* · [Paper](https://arxiv.org/html/2610.14405v1) · [Code](https://github.com/RISE-X-Lab/SPROUT) · [Project](https://rise-x-lab.github.io/SPROUT/)<br>
  Mengyang Liu et al. · Shanghai Jiao Tong University; Amazon; Nanjing University; +2 institutions
- <a id="paper-b40ae7e623658513"></a>**SteerSearch: Interactive Search Reasoning with Mid-Response Steering** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.24287)* · [Paper](https://arxiv.org/abs/2610.24287)<br>
  Udit Thakur et al. · Language Technology Lab, University of Amsterdam; eBay
- <a id="paper-a2259b2fffb789f0"></a>**SynCo: Data Synthesis Co-Training for Self-Evolving LLMs via Multi-Agent Reinforcement Learning** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.11345)* · [Paper](https://arxiv.org/abs/2610.11345) · [Code](https://github.com/weiyang930/SynCo) · [Dataset](https://huggingface.co/datasets/weiyang930/SynCo)<br>
  Wei Yang et al. · University of Southern California; The George Washington University; Georgia Institute of Technology
- <a id="paper-f11c120345a76678"></a>**ThinkWorld: World Imagination Reinforces Chain-of-Dynamics Reasoning** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.37666)* · [Paper](https://arxiv.org/abs/2610.37666) · [Project](https://thinkworld-project.github.io/)<br>
  Chaehyun Kim et al. · NVIDIA; KAIST
- <a id="paper-7af4030312fdc9aa"></a>**ToM2Vec: Continuous Theory-of-Mind Tokens for Multi-Agent Coordination** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.29934)* · [Paper](https://arxiv.org/abs/2610.29934) · [Code](https://github.com/nsivaku/tom2vec)<br>
  Nithin Sivakumaran et al. · UNC Chapel Hill; Cisco; The University of Texas at Austin
- <a id="paper-38e70b683c26da97"></a>**TraceForge: Distilling with Your Own Thinking** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.29680)* · [Paper](https://arxiv.org/abs/2610.29680)<br>
  Yan Wang · Independent Researcher
- <a id="paper-9e2f9fe91ea38fa6"></a>**Training Reasoning Models to Generate Diverse Scientific Ideas** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.22324)* · [Paper](https://arxiv.org/abs/2610.22324) · [Code](https://github.com/ManyaWadhwa/diverge_ideation)<br>
  Manya Wadhwa et al. · New York University; Stony Brook University; Salesforce AI Research
- <a id="paper-16ab0f9e2218180c"></a>**Training the Whole Agent, Not Just the Model** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.28069)* · [Paper](https://arxiv.org/abs/2610.28069) · [Code](https://github.com/lingxiaotang/HarnessAdapt-RL) · [HF Model](https://huggingface.co/anon-review-7f3a/HarnessAdapt-RL)<br>
  Lingxiao Tang, Wei Tao, Yiwen Guo, Lingfeng Bao · Zhejiang University; LIGHTSPEED; Independent Researcher
- <a id="paper-e5af65d8ed72be8d"></a>**Trajectory2Gym: Decision-Grounded Compositional Interaction Synthesis for Tool-Use Agents** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.33568)* · [Paper](https://arxiv.org/abs/2610.33568) · [Project](https://yihaohu0118.github.io/Trajectory2Gym-page/) · [Code](https://github.com/yihaohu0118/Trajectory2Gym) · [Dataset](https://huggingface.co/datasets/mis2/Trajectory2gym)<br>
  Yihao Hu et al. · Westlake University; Ant International
- <a id="paper-c8f3602bba98a90b"></a>**Trinity: Self-Evolving Vision-Language Models with a Self-Verifier** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.04469)* · [Paper](https://arxiv.org/abs/2610.04469)<br>
  Youngwan Lee, Yong-Ju Lee, Sung Ju Hwang · Electronics and Telecommunications Research Institute (ETRI); Korea Advanced Institute of Science and Technology (KAIST); DeepAuto.ai
- <a id="paper-f25291638fa3e4c7"></a>**VideoResearchAgent: Grounded Task Synthesis and Sim-to-Real RL for Open-Web Video Research** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.04911)* · [Paper](https://arxiv.org/abs/2610.04911) · [Code](https://github.com/Ralph-Zhou/VideoResearchAgent) · [Dataset](https://huggingface.co/datasets/VideoResearchAgent/VideoResearchAgent-Data) · [HF Model](https://huggingface.co/VideoResearchAgent/VideoResearchAgent-4B-SFT) · [HF Model](https://huggingface.co/VideoResearchAgent/VideoResearchAgent-4B-RL)<br>
  Yuhang Zhou et al. · Institute of Trustworthy Embodied AI, Fudan University; Shanghai Key Laboratory of Multimodal Embodied AI; Singapore Management University
- <a id="paper-c597ebcff760d449"></a>**Vision-Language-Action or World-Action? Just Action Models** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.37219)* · [Paper](https://arxiv.org/abs/2610.37219) · [Project](https://y0uroy.github.io/JAM)<br>
  Yonghao Yu, Lang Huang, Runyi Li, Toshihiko Yamasaki · The University of Tokyo; National Institute of Informatics
- <a id="paper-ce88f69c0203ec29"></a>**WeVisOne-VL: Unified Visual Perception from Objects to Pixels** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.31329)* · [Paper](https://arxiv.org/abs/2610.31329) · [Project](https://tencent.github.io/WeVisOne-VL) · [Code](https://github.com/Tencent/WeVisOne-VL)<br>
  Tianming Liang et al. · WeChat Vision, Tencent Inc.
- <a id="paper-29b6bdf1923373d0"></a>**Where Research Ideation Begins: Forward-Citation Supervision for Actionable Limitation Generation** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.23038)* · [Paper](https://arxiv.org/abs/2610.23038)<br>
  Liyang Zhao, Yong Cao, Haibin Ling · Westlake University; University of Tübingen

### 2025

- <a id="agentevolver"></a>**AgentEvolver: Towards Efficient Self-Evolving Agent System** · *[arXiv 2025 (preprint)](https://arxiv.org/abs/2511.10395)* · [Paper](https://arxiv.org/abs/2511.10395) · [Code](https://github.com/modelscope/AgentEvolver) · [Project](https://modelscope.github.io/AgentEvolver/)<br>
  Yunpeng Zhai et al. · Tongyi Lab, Alibaba Group
- <a id="f09"></a>**DeepSeek-R1: Incentivizing Reasoning Capability in LLMs via Reinforcement Learning** · *[Nature 2025](https://www.nature.com/articles/s41586-025-09422-z)* · [Paper](https://arxiv.org/abs/2501.12948) · [Code](https://github.com/deepseek-ai/DeepSeek-R1) · [HF Model](https://huggingface.co/deepseek-ai/DeepSeek-R1)<br>
  DeepSeek-AI
- <a id="r01"></a>**RAGEN: Understanding Self-Evolution in LLM Agents via Multi-Turn Reinforcement Learning** · *[arXiv 2025 (preprint)](https://arxiv.org/abs/2504.20073)* · [Paper](https://arxiv.org/abs/2504.20073) · [Code](https://github.com/RAGEN-AI/RAGEN) · [Project](https://ragen-ai.github.io/)<br>
  Zihan Wang et al. · Northwestern University; University of Washington; Stanford University; +4 institutions
- <a id="search-r1"></a>**Search-R1: Training LLMs to Reason and Leverage Search Engines with Reinforcement Learning** · *[COLM 2025](https://arxiv.org/abs/2503.09516)* · [Paper](https://arxiv.org/abs/2503.09516) · [Code](https://github.com/PeterGriffinJin/Search-R1) · [HF Collection](https://huggingface.co/collections/PeterJinGo/search-r1-67d1a021202731cb065740f5) · [HF Model (7B)](https://huggingface.co/PeterJinGo/SearchR1-nq_hotpotqa_train-qwen2.5-7b-em-ppo) · [HF Dataset](https://huggingface.co/datasets/PeterJinGo/nq_hotpotqa_train)<br>
  Bowen Jin et al. · University of Illinois Urbana-Champaign; University of Massachusetts Amherst; Google Cloud AI Research
- <a id="r10"></a>**WebRL: Training LLM Web Agents via Self-Evolving Online Curriculum Reinforcement Learning** · *[ICLR 2025](https://proceedings.iclr.cc/paper_files/paper/2025/hash/c66e1fcc9691aae706250638f36f681b-Abstract-Conference.html)* · [Paper](https://arxiv.org/abs/2411.02337) · [Code](https://github.com/THUDM/WebRL) · [HF Model (GLM-9B)](https://huggingface.co/THUDM/webrl-glm-4-9b) · [HF Model (Llama-8B)](https://huggingface.co/THUDM/webrl-llama-3.1-8b) · [HF Model (Llama-70B)](https://huggingface.co/THUDM/webrl-llama-3.1-70b) · [HF Reward Model](https://huggingface.co/THUDM/webrl-orm-llama-3.1-8b)<br>
  Zehan Qi et al. · Tsinghua University; Zhipu AI

### 2024

- <a id="agenttuning"></a>**AgentTuning: Enabling Generalized Agent Abilities for LLMs** · *[Findings of ACL 2024](https://aclanthology.org/2024.findings-acl.181/)* · [Paper](https://arxiv.org/abs/2310.12823) · [Code](https://github.com/THUDM/AgentTuning) · [Project](https://thudm.github.io/AgentTuning/) · [HF Model (70B)](https://huggingface.co/THUDM/agentlm-70b) · [HF Dataset](https://huggingface.co/datasets/THUDM/AgentInstruct)<br>
  Aohan Zeng et al. · Tsinghua University; Zhipu.AI
- <a id="restem"></a>**Beyond Human Data: Scaling Self-Training for Problem-Solving with Language Models** · *[TMLR 2024](https://arxiv.org/abs/2312.06585)* · [Paper](https://arxiv.org/abs/2312.06585)<br>
  Avi Singh et al. · Google DeepMind; Mila
- <a id="eureka"></a>**Eureka: Human-Level Reward Design via Coding Large Language Models** · *[ICLR 2024](https://proceedings.iclr.cc/paper_files/paper/2024/hash/70c26937fbf3d4600b69a129031b66ec-Abstract-Conference.html)* · [Paper](https://arxiv.org/abs/2310.12931) · [Project](https://eureka-research.github.io) · [Code](https://github.com/eureka-research/Eureka)<br>
  Yecheng Jason Ma et al. · NVIDIA; University of Pennsylvania; California Institute of Technology; +1 institutions
- <a id="r07"></a>**Re-ReST: Reflection-Reinforced Self-Training for Language Agents** · *[EMNLP 2024](https://aclanthology.org/2024.emnlp-main.861/)* · [Paper](https://arxiv.org/abs/2406.01495) · [Code](https://github.com/PlusLabNLP/Re-ReST)<br>
  Zi-Yi Dou et al. · UCLA

### 2023

- <a id="meta-causal"></a>**A Meta-Reinforcement Learning Algorithm for Causal Discovery** · *[CLeaR 2023](https://proceedings.mlr.press/v213/sauter23a.html)* · [Paper](https://arxiv.org/abs/2207.08457) · [Code](https://github.com/sa-and/MCD)<br>
  Andreas Sauter, Erman Acar, Vincent François-Lavet · Vrije Universiteit Amsterdam; University of Amsterdam
- <a id="rest-react"></a>**ReST meets ReAct: Self-Improvement for Multi-Step Reasoning LLM Agent** · *[arXiv 2023 (preprint)](https://arxiv.org/abs/2312.10003)* · [Paper](https://arxiv.org/abs/2312.10003)<br>
  Renat Aksitov et al. · Google Research; Google DeepMind; Google

### 2022

- <a id="star"></a>**STaR: Bootstrapping Reasoning With Reasoning** · *[NeurIPS 2022](https://proceedings.neurips.cc/paper_files/paper/2022/hash/639a9a172c044fbb64175b5fad42e9a5-Abstract-Conference.html)* · [Paper](https://arxiv.org/abs/2203.14465)<br>
  Eric Zelikman, Yuhuai Wu, Jesse Mu, Noah D. Goodman · Stanford University; Google Research

### 2021

- <a id="f01"></a>**Deep Adaptive Design Amortizing Sequential Bayesian Experimental Design** · *[ICML 2021](https://proceedings.mlr.press/v139/foster21a.html)* · [Paper](https://proceedings.mlr.press/v139/foster21a.html) · [Code](https://github.com/ae-foster/dad)<br>
  Adam Foster, Desi R Ivanova, Ilyas Malik, Tom Rainforth · University of Oxford

### 2020

- <a id="f02"></a>**VariBAD: A Very Good Method for Bayes-Adaptive Deep RL via Meta-Learning** · *[ICLR 2020](https://arxiv.org/abs/1910.08348)* · [Paper](https://arxiv.org/abs/1910.08348) · [Code](https://github.com/lmzintgraf/varibad)<br>
  Luisa Zintgraf et al. · University of Oxford; Latent Logic; Microsoft Research

### 2019

- <a id="c02"></a>**Causal Reasoning from Meta-reinforcement Learning** · *[arXiv 2019 (preprint)](https://arxiv.org/abs/1901.08162)* · [Paper](https://arxiv.org/abs/1901.08162)<br>
  Ishita Dasgupta et al. · DeepMind; UCL; Harvard University

### 2017

- <a id="r08"></a>**Hindsight Experience Replay** · *[NeurIPS 2017](https://proceedings.neurips.cc/paper_files/paper/2017/hash/453fadbd8a1a3af50a9df4df899537b5-Abstract.html)* · [Paper](https://arxiv.org/abs/1707.01495)<br>
  Marcin Andrychowicz et al. · OpenAI

### 1999

- <a id="f08"></a>**Policy Invariance under Reward Transformations Theory and Application to Reward Shaping** · *[ICML 1999](https://people.eecs.berkeley.edu/~russell/papers/icml99-shaping.pdf)* · [Paper](https://ai.stanford.edu/~ang/papers/shaping-icml99.pdf) · [Author PDF](https://people.eecs.berkeley.edu/~russell/papers/icml99-shaping.pdf)<br>
  Andrew Y. Ng, Daishi Harada, Stuart Russell · UC Berkeley

[↑ Contents](#contents)

<a id="adaptation"></a>

## 🔄 Continual Discovery

*How can agents learn from ongoing investigations?*

### 2026

- <a id="paper-0ffd35130fc956d4"></a>**AnyAct: Universal Action for Self-Evolving Agents** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2609.37025)* · [Paper](https://arxiv.org/abs/2609.37025) · [Code](https://github.com/HKUDS/AnyTool)<br>
  Lingrui Xu et al. · The University of Hong Kong
- <a id="paper-6f63cd1d3b1feb5c"></a>**Are Self-Evolving Agents Continual Learners?** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.25858)* · [Paper](https://arxiv.org/abs/2610.25858)<br>
  Xiaoyin Chen et al. · Mila – Quebec AI Institute; Université de Montréal; Google DeepMind
- <a id="t13"></a>**ASCENT: Online Test-Time Training of Long-Horizon Agents via Self-Distillation of Verified Experience** · *[arXiv 2026 (preprint)](https://arxiv.org/html/2610.05303v1)* · [Paper](https://arxiv.org/html/2610.05303v1) · [Project](https://artificer-ai-lab.github.io/ASCENT/)<br>
  Haodong Lu, Dong Gong · UNSW Sydney
- <a id="paper-94ab554ffc39816c"></a>**Beyond Successor Accuracy: State Retention for Recursive Self-Improvement in Recommendation** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.07105)* · [Paper](https://arxiv.org/abs/2610.07105) · [Code](https://github.com/Jinfeng-Xu/RecRSI)<br>
  Jinfeng Xu et al. · The University of Hong Kong; The Hong Kong Polytechnic University; The Hong Kong University of Science and Technology; +1 institutions
- <a id="paper-88ed6b4d7523fe2d"></a>**Can Test-Time Memory Evolution Outperform Test-Time Training for Scientific Discovery?** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.32046)* · [Paper](https://arxiv.org/abs/2610.32046) · [Code](https://github.com/yepengliu/TTME)<br>
  Yepeng Liu et al. · UC Santa Barbara; UC Berkeley
- <a id="paper-63c5fd925e9f2dcd"></a>**ChartEvo: Self-Evolving Agent Harnesses for Long-Tail Chart Reasoning** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.28282)* · [Paper](https://arxiv.org/abs/2610.28282)<br>
  Qi Wang et al. · State Key Laboratory of Multimodal Artificial Intelligence Systems, CASIA; School of Artificial Intelligence, University of Chinese Academy of Sciences; New Laboratory of Pattern Recognition, CASIA; +1 institutions
- <a id="paper-7f537879bf2ffb4a"></a>**CoEvolve: Self-Evolving Code Policies from Skills to Strategies for Humanoid Robots** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.23288)* · [Paper](https://arxiv.org/abs/2610.23288)<br>
  Zicheng Liu et al. · Peking University; Renmin University of China; Beijing XYZ Embodied AI Co., Ltd.; +1 institutions
- <a id="paper-68c4d078d5e76020"></a>**CoSMO: Conformal Semantic Mapping for Open-World Safe Robot Navigation** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.18321)* · [Paper](https://arxiv.org/abs/2610.18321) · [Project](https://yangming911.github.io/cosmo-page/)<br>
  Shuqi Wang et al. · Shanghai Jiao Tong University; Shanghai Innovation Institute; Fudan University
- <a id="paper-5ff961211382d518"></a>**Counterfactual Self-Evolving Agents for Evidence-Grounded Reasoning** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2609.32870)* · [Paper](https://arxiv.org/abs/2609.32870)<br>
  Xing Han et al. · Johns Hopkins University; MIT; University of Texas at Austin; +1 institutions
- <a id="paper-4bd61eafe4f2ad4e"></a>**Darwin-Claw: Environment-Adaptive Experience Consolidation for Recursively Self-Evolving Agents** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.23574)* · [Paper](https://arxiv.org/abs/2610.23574)<br>
  Mingze Yin et al. · Zhejiang University; Tencent; Zhongguancun Academy
- <a id="paper-8c25de7e3b883e2e"></a>**Do Self-Evolving Skills Generalize to Held-Out Tasks?** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2609.39148)* · [Paper](https://arxiv.org/abs/2609.39148)<br>
  Xihao Piao, Zifeng Wang, Zheng Chen · Osaka University
- <a id="paper-274759ea4fce57e7"></a>**EASE: Behavior-Adaptive Skill Curation for Self-Evolving Agents** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2609.36746)* · [Paper](https://arxiv.org/abs/2609.36746)<br>
  Zhen Xiong, Qiaoyu Tan · New York University; New York University Shanghai
- <a id="paper-8e422795873eb25c"></a>**EmbodiedEvo: Self-Evolving Coding Agent For Physical Intelligence** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.18867)* · [Paper](https://arxiv.org/abs/2610.18867) · [Project](https://lab.einsia.ai/embodiedevo/) · [Code](https://github.com/Einsia/EmbodiedEvo)<br>
  Wenyi Li et al. · Navers Lab; Einsia.AI; Tsinghua University
- <a id="paper-d27b79ad52026607"></a>**EmbodiRSI: Recursive Self-Improvement for Data-Efficient Robot Adaptation** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2609.38905)* · [Paper](https://arxiv.org/abs/2609.38905)<br>
  Haoran Lang et al. · ShanghaiTech University; InstAdapt
- <a id="paper-d20bb21bfca9c7c3"></a>**Energy Ring: Stabilizing Feature Energy for Reliable Test-Time Discovery** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.14525)* · [Paper](https://arxiv.org/abs/2610.14525) · [Code](https://github.com/LeTianL-TT/ER-for-TTD)<br>
  Tianle Liu et al. · School of Electronics and Information Engineering, Suzhou University of Science and Technology; Computer Vision Center, Universitat Autònoma de Barcelona; College of Computer Science, Northwest University; +4 institutions
- <a id="paper-f128cef6245387b0"></a>**EvoAD: Self-Evolving Autonomous Driving via Latent World-Model Guided Post-hoc Reflection** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.23886)* · [Paper](https://arxiv.org/abs/2610.23886)<br>
  Junjie Yang et al. · The Hong Kong University of Science and Technology; The Hong Kong University of Science and Technology (Guangzhou); The Chinese University of Hong Kong, Shenzhen; +2 institutions
- <a id="paper-dc5079437446d0d5"></a>**EvoBelief: Falsifiable World Models for Self-Improving LLM Agents** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.12789)* · [Paper](https://arxiv.org/abs/2610.12789)<br>
  Janet Wang et al. · Tulane University; Amazon
- <a id="paper-9cb4fd90a578a1f8"></a>**Evolving to Match Capabilities: Improving Harness Self-Evolution via Skill Adaptation** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.33024)* · [Paper](https://arxiv.org/abs/2610.33024) · [Project](https://zhihaoyang30.github.io/skill-adaptation/)<br>
  Zhihao Yang et al. · University of Chinese Academy of Sciences; Independent Researcher; University of California, Santa Cruz; +4 institutions
- <a id="paper-4faf84fcc2c0dce6"></a>**EvolvingBrain: An Adaptive Skill System for Multi-modal Agents Self-Evolution in Open Worlds** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.20786)* · [Paper](https://arxiv.org/abs/2610.20786) · [Code](https://github.com/Runxuan-Liu/EvolvingBrain)<br>
  Runxuan Liu et al. · Harbin Institute of Technology; iFLYTEK; Meituan; +1 institutions
- <a id="paper-795b51132cf40a82"></a>**EvoSim: Learning to Model, Modeling to Learn** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.11344)* · [Paper](https://arxiv.org/abs/2610.11344)<br>
  Yun-Wei Song et al. · Beijing Key Laboratory of Complex Solid-State Batteries, Department of Chemical Engineering, Tsinghua University, Beijing, China; State Key Laboratory of Chemical Engineering and Low-Carbon Technology, Tsinghua University, Beijing, China; Beijing Tsingyu Technology Co., Ltd., Beijing, China; +5 institutions
- <a id="paper-65f2aa74e4cbffb5"></a>**ForkPilot: Self-Evolving Policy for Retrospective Search in Long-Horizon Agents** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.04889)* · [Paper](https://arxiv.org/abs/2610.04889)<br>
  Xinyue Zeng et al. · Virginia Tech; Microsoft
- <a id="paper-5095dee825366c6b"></a>**From Identification to Discovery: Holistic RF Fingerprinting via Learning-Aided Quantization** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.05979)* · [Paper](https://arxiv.org/abs/2610.05979) · [Code](https://github.com/omer-hazan/RFFI-with-GCD-via-VQVAE)<br>
  Omer Hazan, Gil Paryanti, Nir Shlezinger · ECE School, Ben-Gurion University of the Negev; Elbit Systems
- <a id="paper-173432e0518b18b9"></a>**From Pareto to Preference: Personalized Test-Time Scaling via Amortized Agentic Policy Discovery** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.09684)* · [Paper](https://arxiv.org/abs/2610.09684) · [Code](https://github.com/WangXinglin/PersonTTS)<br>
  Xinglin Wang et al. · Beijing Institute of Technology; Xiaohongshu Inc
- <a id="paper-eb67a46d1dffb8ee"></a>**From Semantic Decisions to Feasible Trajectories: Self-Evolving LLM-Guided Optimal Control for Narrow-Space Parking** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2609.24631)* · [Paper](https://arxiv.org/abs/2609.24631)<br>
  Zhengbao Yao, Yuanfu Luo, Kehan Xue · xLean Robotics Co., Ltd.
- <a id="paper-a5ff9a218203c4e6"></a>**GenMem: Generative Symbolic Memory for Self-Evolving Harness** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2609.34633)* · [Paper](https://arxiv.org/abs/2609.34633)<br>
  Xinke Jiang et al. · National Engineering Research Center of Software Engineering, Peking University; School of Computer Science, Peking University; Key Laboratory of High Confidence Software Technologies, Ministry of Education; +2 institutions
- <a id="harness-ttt"></a>**HarnessTTT: Learn to Optimize Harness at Test-Time for Scientific Discovery** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.17370)* · [Paper](https://arxiv.org/abs/2610.17370) · [Code](https://github.com/SaFo-Lab/Self_Adapt_Harness) · [Project](https://gray311.github.io/harnessrl/) · [HF Dataset](https://huggingface.co/datasets/gray311/HarnessRL)<br>
  Yingzi Ma et al. · University of Wisconsin-Madison; NVIDIA; Johns Hopkins University; +2 institutions
- <a id="paper-e86c5d55b8099877"></a>**ImageRSI: Verification-Driven Recursive Self-Improvement for Agentic Image Generation** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.32120)* · [Paper](https://arxiv.org/abs/2610.32120)<br>
  Shuo Han et al. · University of Science and Technology of China; Qwen Business Unit of Alibaba, Alibaba Token Hub; Xidian University
- <a id="paper-396ef1a44f871e38"></a>**InstAgent: A Recursively Self-Improving Agent Operating System for Heterogeneous Robot Collaboration** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.23098)* · [Paper](https://arxiv.org/abs/2610.23098)<br>
  Haoyang Luo et al. · ShanghaiTech University, Shanghai, China; InstAdapt, Shanghai, China
- <a id="paper-47d9c27401b76abb"></a>**InterMimicGen: Scaling Humanoid Loco-Manipulation through Self-Evolving Motion Imitation** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.06850)* · [Paper](https://arxiv.org/abs/2610.06850) · [Project](https://sirui-xu.github.io/InterMimicGen/)<br>
  Yucheng Zhang et al. · University of Illinois Urbana-Champaign; NVIDIA
- <a id="paper-7420a54429f1ece0"></a>**Learning from Fleet Experience: A Collective Learning Paradigm for Robots** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.25736)* · [Paper](https://arxiv.org/abs/2610.25736) · [Project](https://cel-robot-learning.github.io/)<br>
  Chao Yu et al. · Tsinghua University; AgiBot; Infinigence AI
- <a id="paper-f67c24c899266324"></a>**Learning to Compose: Recursive Self-Improvement of Shared Executable Stacks for Zero-Shot Long-Horizon Robot Manipulation** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.24464)* · [Paper](https://arxiv.org/abs/2610.24464) · [Code](https://github.com/cocacola-lab/Recursia) · [Project](https://cocacola-lab.github.io/Recursia-website/)<br>
  Yangzhi Chen et al. · Beijing Jiaotong University; New York University; University of Southern California; +2 institutions
- <a id="t11"></a>**Learning to Discover at Test Time** · *[ICML 2026](https://proceedings.mlr.press/v306/yuksekgonul26a.html)* · [Paper](https://arxiv.org/html/2601.16175v1) · [Code](https://github.com/test-time-training/discover) · [Project](https://test-time-training.github.io/discover)<br>
  Mert Yuksekgonul et al. · Stanford University; NVIDIA; Astera Institute; +2 institutions
- <a id="paper-73e7e7f6ce4315bc"></a>**MedForge-RSI: Medical Deepfake Detection via Recursive Self-Improvement** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2609.36549)* · [Paper](https://arxiv.org/abs/2609.36549)<br>
  Zhihui Chen, Mengling Feng · National University of Singapore
- <a id="paper-bf157ba63fabe951"></a>**Memory as Belief: Bayesian Evolution of Memory for Self-Evolving LLM Agents** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.25119)* · [Paper](https://arxiv.org/abs/2610.25119)<br>
  Yiming Xu et al. · School of Computer Science and Technology, Xi’an Jiaotong University; Shaanxi Provincial Key Laboratory of Big Data Knowledge Engineering, Xi’an Jiaotong University; University of Virginia, Charlottesville, Virginia, USA; +1 institutions
- <a id="paper-f46e042d0f23b6f7"></a>**MemT-1.0: Towards Memory-Native Evolution** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.26825)* · [Paper](https://arxiv.org/abs/2610.26825) · [Code](https://github.com/MemTensor/MemT-1.0) · [HF Model](https://huggingface.co/MemTensor/MemT-1.0-Nano)<br>
  MemTensor Team et al. · NVIDIA
- <a id="paper-4f24e668bd567dab"></a>**More Memory, Worse Agents: Error Reproduction and Anti-Persistence in LLM Agents** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.27406)* · [Paper](https://arxiv.org/abs/2610.27406)<br>
  Ruhan Wang, Kishan Panaganti, Dongruo Zhou · Indiana University; Tencent HY
- <a id="paper-bb11c7dcbd6603d3"></a>**MOVE: Multimodal Open-world Verification and Expansion for Graph Learning** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.00268)* · [Paper](https://arxiv.org/abs/2610.00268)<br>
  Zekai Chen et al. · Beijing Institute of Technology; Shandong University
- <a id="paper-2688a4b095ad2a70"></a>**Nested Sparsity for Scalable Pretraining and Continual Learning** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.31818)* · [Paper](https://arxiv.org/abs/2610.31818) · [Code](https://github.com/Ma-Lab-Berkeley/Nestor)<br>
  Tianzhe Chu, Druv Pai, Yi Ma · University of Hong Kong; UC Berkeley
- <a id="paper-9091cb8dd45473e8"></a>**NLPG: Natural-Language Policy Gradients for Self-Evolving Language Agents** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2609.33379)* · [Paper](https://arxiv.org/abs/2609.33379)<br>
  Xu Liu et al. · School of Electronic Information, Wuhan University; School of Remote Sensing and Information Engineering, Wuhan University; State Key Laboratory of Information Engineering in Surveying, Mapping and Remote Sensing, Wuhan University
- <a id="t12"></a>**No Time Like the Present: Agentic Test-Time Training for LLM Agents** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2607.03441)* · [Paper](https://arxiv.org/abs/2607.03441)<br>
  Yanbo Wang et al. · Kuaishou Technology
- <a id="paper-6273fff431181535"></a>**Online Open-World Wafer Defect Discovery using Hyperdimensional Computing** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.28949)* · [Paper](https://arxiv.org/abs/2610.28949)<br>
  Quanling Zhao et al. · University of California San Diego; IBM Research; Anderon
- <a id="paper-52731a9209ac98ed"></a>**PreCoMem: Predictive Cognitive Memory for Self-Evolving Long-Term Dialogue Agents** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.29467)* · [Paper](https://arxiv.org/abs/2610.29467) · [Code](https://github.com/ZhongWishing/PreCoMem)<br>
  Jian Zhong et al. · Nankai University; vivo AI Lab; Tsinghua University; +2 institutions
- <a id="paper-b2d39182f36164f6"></a>**PrivMeSA: Privacy-Aware Self-Evolving Multi-Agent System for Medicine via Local-Remote LLM Collaboration** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2609.38458)* · [Paper](https://arxiv.org/abs/2609.38458)<br>
  Dannong Wang et al. · University of Central Florida; Universit´e de Montr´eal
- <a id="paper-9752f967ba715846"></a>**PsyEvo: A Personalized Counseling Agent That Self-Evolves at Test Time** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.02885)* · [Paper](https://arxiv.org/abs/2610.02885) · [Code](https://github.com/Lingxi-mental-health/PsyEvo)<br>
  Yuting Yan et al. · Lyncia Lab; Tianqiao and Chrissy Chen Institute
- <a id="paper-cb72119b3b1f3079"></a>**Recursive Self-Improvement of Visuomotor Policies through Local Recovery Supervision** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.05151)* · [Paper](https://arxiv.org/abs/2610.05151)<br>
  Yuzhi Zhang, Xinyu Liu, Yu Zhang · Beihang University
- <a id="paper-55ab01be48315197"></a>**Reflect After Failure: Brain-Inspired Self-Evolving Agents for Embodied Spatial Intelligence** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.20312)* · [Paper](https://arxiv.org/abs/2610.20312)<br>
  Xin Li et al. · City University of Hong Kong; East China Normal University; University of Electronic Science and Technology of China; +2 institutions
- <a id="paper-5f578362e97630cb"></a>**ReGE: Stronger Agents through Experience Synthesis** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.33861)* · [Paper](https://arxiv.org/abs/2610.33861) · [Code](https://github.com/TIGER-AI-Lab/ReGE)<br>
  Jiarong Liang et al. · University of Waterloo; University of North Carolina at Chapel Hill; University of British Columbia
- <a id="paper-bf8ebac80a705321"></a>**Relational Semantic Grounding for Test-Time Discovery** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.14721)* · [Paper](https://arxiv.org/abs/2610.14721) · [Code](https://github.com/LeTianL-TT/SEGA-for-TTD)<br>
  Tianle Liu et al. · School of Electronics and Information Engineering, Suzhou University of Science and Technology; School of Intelligence Science and Technology, Nanjing University; School of Computer Science Engineering, North Minzu University; +1 institutions
- <a id="paper-c15fc300d6309d58"></a>**Remembering Has a Price: Learning Memory Worth under Resource Constraints** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.26453)* · [Paper](https://arxiv.org/abs/2610.26453) · [Code](https://github.com/AIGNLAI/TokenWorth)<br>
  Guannan Lai, Zi-Yang Bai, Jun-Peng Jiang, Han-Jia Ye · School of Artificial Intelligence, Nanjing University; National Key Laboratory for Novel Software Technology, Nanjing University
- <a id="paper-c9f8f3ab02d4c27b"></a>**RetroNav: Scene-Grounded Retrospection and Retry for Self-Evolving Lifelong Navigation** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.35172)* · [Paper](https://arxiv.org/abs/2610.35172)<br>
  Diantao Tu et al. · Institute of Automation, Chinese Academy of Sciences; School of Artificial Intelligence, University of Chinese Academy of Sciences; School of Advanced Interdisciplinary Sciences, University of Chinese Academy of Sciences
- <a id="paper-256ec415fdba134a"></a>**RewardWeaver: Long-Horizon Interactive Learning for Language Agents via Self-Evolving Reward Adaptation** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.10120)* · [Paper](https://arxiv.org/abs/2610.10120)<br>
  Hengbo Xiao et al. · Yoolee.ai; University of Science and Technology of China; Peking University; +1 institutions
- <a id="paper-41968877a20ed1a5"></a>**RoboBridge: A Self-Evolving Embodied Agent Framework for Sim-to-Real Transfer** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.02717)* · [Paper](https://arxiv.org/abs/2610.02717)<br>
  Chenxi Li et al. · Shanghai Artificial Intelligence Laboratory; Zhejiang University; Beihang University; +3 institutions
- <a id="paper-3ec53d4cbe1b3187"></a>**RoboDoctor: Training-Free Recursive Self-Improvement for Robot Policies** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.35604)* · [Paper](https://arxiv.org/abs/2610.35604) · [Code](https://github.com/THUSI-Lab/RoboDoctor) · [Project](https://robodoctor-rsi.github.io/)<br>
  Heyang Yu et al. · Tsinghua University; New York University; Northwestern University
- <a id="paper-11fd9b1a5a2a256f"></a>**SAGE: A Statistical Acceptance Gate for Self-Evolving Agents** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2609.36043)* · [Paper](https://arxiv.org/abs/2609.36043)<br>
  Yihao Wang et al. · Peking University; University of Oklahoma; Imperial College London; +5 institutions
- <a id="paper-44d313ca8f7a6ce2"></a>**SE-ADD: Self-Evolving Audio Deepfake Detection with Mistake-Driven Supervision** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2609.39679)* · [Paper](https://arxiv.org/abs/2609.39679) · [Code](https://github.com/SE-ADD/SE-ADD)<br>
  Rong Wan et al. · University of Surrey; Guangxi University; Shenzhen University of Advanced Technology; +1 institutions
- <a id="paper-2e4a524137176712"></a>**SEER: Self-Evolving Event Reasoning and Retrieval for Time Series Forecasting** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.04109)* · [Paper](https://arxiv.org/abs/2610.04109) · [Project](https://github.com/BennyTMT/SEER)<br>
  Mingtian Tan et al. · Google Cloud AI Research; University of Virginia
- <a id="paper-8341014696695a89"></a>**SEES: A Self-Evolving Embodied System via Failure-Guided VLA Policy Adaptation** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2609.32698)* · [Paper](https://arxiv.org/abs/2609.32698)<br>
  Ziwen Li et al. · Mohamed bin Zayed University of Artificial Intelligence; University of Sydney; University of Oxford; +3 institutions
- <a id="paper-2d5446a91ef47109"></a>**Self-Evolving Agents through Privileged Retrospective Distillation** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.27495)* · [Paper](https://arxiv.org/abs/2610.27495)<br>
  Yuhang Zhou et al. · Meta AI
- <a id="paper-9cdbed943ac0c08a"></a>**Self-Evolving Agents via Likelihood-Guided Tool-Space Optimization** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2609.34151)* · [Paper](https://arxiv.org/abs/2609.34151)<br>
  Xuanqi Zhang et al. · University of British Columbia; Vector Institute; Columbia University
- <a id="paper-e3d49176e9c7ae9b"></a>**Self-Evolving Defense: Continual Security Policy Learning for LLM Agents** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2609.36603)* · [Paper](https://arxiv.org/abs/2609.36603) · [Code](https://github.com/Infini-AI-Lab/SED) · [Project](https://infini-ai-lab.github.io/SED)<br>
  Minh Nhat Le et al. · Carnegie Mellon University; University of Massachusetts Amherst
- <a id="paper-97de4224b6371eea"></a>**Self-Evolving Multimedia Verification through Memory Consolidation of Contestation Experiences** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2609.27175)* · [Paper](https://arxiv.org/abs/2609.27175) · [Code](https://github.com/Analytics-Everywhere-Lab/SEMV)<br>
  Truong Thanh Hung Nguyen et al. · University of New Brunswick; FPT Software; University of Science and Technology of Hanoi
- <a id="paper-a68e54ff3367de89"></a>**Self-Evolving Static Analysis via LLM Pseudo-Labeling** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.30184)* · [Paper](https://arxiv.org/abs/2610.30184)<br>
  Rui Melo et al. · Carnegie Mellon University; FEUP
- <a id="paper-3dd4a597d7094e74"></a>**Self-Evolving Time-Series Forecasting Agents with Episodic Memory and Online Policy Learning** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2609.32689)* · [Paper](https://arxiv.org/abs/2609.32689)<br>
  Junyi Wang, Yilin Wang, Wen Wu, Chao Zhang · Shanghai Jiao Tong University; Shanghai Artificial Intelligence Laboratory; Tsinghua University
- <a id="paper-d1c8322a1b1949b1"></a>**Selm: Self-Evolving Library Management for Multi-Skill Agent Optimization** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.24630)* · [Paper](https://arxiv.org/abs/2610.24630)<br>
  Mengxi Hu et al. · School of Information, Renmin University of China, Beijing, China; Key Laboratory of Data Engineering and Knowledge Engineering, Beijing, China; Engineering Research Center of Database and Business Intelligence, Beijing, China; +2 institutions
- <a id="paper-0268ace042e4dcb9"></a>**Semantic Concept Steering Breaks the Explanation Drift Loop in Continual Learning** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.33877)* · [Paper](https://arxiv.org/abs/2610.33877) · [Code](https://github.com/yonisGit/concept_consistent_continual_learning)<br>
  Yehonatan Elisha, Oren Barkan, Noam Koenigstein · Tel Aviv University; The Open University
- <a id="paper-cf7f5519592d5d60"></a>**Skill-V: Verifiable Self-Evolving Skill Library for Interactive Agents** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.11781)* · [Paper](https://arxiv.org/abs/2610.11781)<br>
  Jie Ma et al. · Xiamen University; Kuaishou Technology; Nankai University
- <a id="skilltta"></a>**Skills on the Fly: Test-Time Adaptive Skill Synthesis for LLM Agents** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2605.16986)* · [Paper](https://arxiv.org/abs/2605.16986) · [Code](https://github.com/Hydr0pon1c/Skills-on-the-fly)<br>
  Jingxing Wang et al. · Shanghai Jiao Tong University; OPPO Research Institute
- <a id="paper-bb9e61607f3890b9"></a>**Socratic Skill Learning: Interleaving Teaching and Practice for Transferable Agent Skills** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.17860)* · [Paper](https://arxiv.org/abs/2610.17860) · [Code](https://github.com/NJU-LINK/Socratic-Skill-Learning)<br>
  Letian Zhu et al. · Nanjing University; Alibaba Group
- <a id="paper-79697a458d1ee6cc"></a>**SpatialBrain: Spatial Intelligence Growing from Experience** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.29317)* · [Paper](https://arxiv.org/abs/2610.29317)<br>
  Yifan Zhou et al. · Shanghai Jiao Tong University; Zhejiang University
- <a id="paper-240aac2e29165d36"></a>**SpatialSkill: Self-Evolving Skills for Cross-View Spatial Reasoning** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2609.34124)* · [Paper](https://arxiv.org/abs/2609.34124) · [Code](https://github.com/vindahi/SpatialSkill)<br>
  Ruifan Zuo et al. · Shandong University; Shanghai AI Laboratory; Zhiyang Innovation Co., Ltd.
- <a id="paper-308a2c9d337c0bc8"></a>**SpecForge: Recursive Self-Improvement for Coding Agents via Behavioral Specifications** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.15708)* · [Paper](https://arxiv.org/abs/2610.15708) · [Code](https://github.com/ccsnow127/SpecForge)<br>
  Yutong Cheng, Haifeng Chen, Peng Gao, Wei Cheng · Virginia Tech; NEC Laboratories America
- <a id="paper-38e39e582b5f3a35"></a>**StraTune: Adaptive Selection of Revision Operators for Self-Evolving LLM Skills** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2609.32886)* · [Paper](https://arxiv.org/abs/2609.32886) · [Code](https://github.com/seai-lab/StraTune)<br>
  Zeping Liu et al. · The University of Texas at Austin; Amazon
- <a id="paper-4cfad5ee09b0c528"></a>**Test-Time Generalized Category Discovery** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2609.33937)* · [Paper](https://arxiv.org/abs/2609.33937)<br>
  Shambhavi Mishra et al. · ÉTS Montréal, Canada
- <a id="ttt-ntp"></a>**Test-Time Training with Next-Token Prediction** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2606.21803)* · [Paper](https://arxiv.org/abs/2606.21803) · [Code](https://github.com/yancyou/TTT-NTP)<br>
  Xuan Ouyang, Zefan Cai, Junjie Hu · University of Wisconsin-Madison
- <a id="paper-531cda116cd33f76"></a>**The Right Lesson at the Right Step: Deriving Control Updates for Self-Evolving Agents** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2609.34988)* · [Paper](https://arxiv.org/abs/2609.34988)<br>
  Yunhe Su et al. · Independent Researcher; Sun Yat-sen University; eunomia-bpf community; +4 institutions
- <a id="paper-759ea716e2ac02e1"></a>**TILDE: Teacher-in-the-Loop Distillation from Embodied Foundation Models** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.25376)* · [Paper](https://arxiv.org/abs/2610.25376) · [Project](https://github.com/hku-sail/TILDE)<br>
  Yuxiang Lu et al. · The University of Hong Kong
- <a id="paper-bc96cee780e278b5"></a>**TokenEconomizer: Experience-Driven Black-Box Cost Control for Coding Agents** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.22732)* · [Paper](https://arxiv.org/abs/2610.22732) · [Project](https://tokeneconomizer.github.io) · [Code](https://github.com/microsoft/TokenEconomizer)<br>
  Aaron J. Li et al. · UC Berkeley; Microsoft Research; Microsoft Security
- <a id="ttcs"></a>**TTCS: Test-Time Curriculum Synthesis for Self-Evolving** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2601.22628)* · [Paper](https://arxiv.org/abs/2601.22628) · [Code](https://github.com/XMUDeepLIT/TTCS)<br>
  Chengyi Yang et al. · Xiamen University; Washington University in St. Louis; Renmin University of China
- <a id="paper-2c4c026c9ccf9ba0"></a>**Unsupervised Tool Evolution for Coding Agents in Data-Lake Analytics** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.27327)* · [Paper](https://arxiv.org/abs/2610.27327)<br>
  Yuqing Yang et al. · University of Southern California; Google; New York University
- <a id="paper-d753212771182899"></a>**Verifier-Harness Co-Evolution for Training-Free Self-Improvement on Open-Ended Tasks** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.17609)* · [Paper](https://arxiv.org/abs/2610.17609) · [Code](https://github.com/tianyi0216/Unified-Co-Evolution)<br>
  Tianyi Xu et al. · Oregon State University; Pennsylvania State University; Johnson & Johnson; +1 institutions
- <a id="paper-068fadc12006e7da"></a>**When Tomorrow Becomes Today: Self-Evolving Policies for Agentic Time-Series Forecasting** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2609.24862)* · [Paper](https://arxiv.org/abs/2609.24862)<br>
  Yifan Hu et al. · Ant International; Tsinghua University; The Chinese University of Hong Kong
- <a id="paper-dde5e0a4009da777"></a>**Which Agent's Skill Should Change? Group-Relative Credit Assignment for Evolving Multi-Agent Teams** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.27227)* · [Paper](https://arxiv.org/abs/2610.27227) · [Code](https://github.com/yananma1029/GRSE-Skills)<br>
  Yanan Ma et al. · Mayo Clinic; University of Manchester; Alibaba Token Hub, Alibaba Group; +1 institutions

### 2025

- <a id="t05"></a>**Learning to (Learn at Test Time): RNNs with Expressive Hidden States** · *[ICML 2025](https://proceedings.mlr.press/v267/sun25h.html)* · [Paper](https://arxiv.org/abs/2407.04620) · [Code (PyTorch)](https://github.com/test-time-training/ttt-lm-pytorch) · [Code (JAX)](https://github.com/test-time-training/ttt-lm-jax)<br>
  Yu Sun et al. · Stanford University; UC San Diego; UC Berkeley; +1 institutions
- <a id="t09"></a>**Self-Adapting Language Models** · *[NeurIPS 2025](https://proceedings.neurips.cc/paper_files/paper/2025/hash/6b41e04c41726e2a60e456d0a2b961ab-Abstract-Conference.html)* · [Paper](https://arxiv.org/html/2506.10943v1) · [Code](https://github.com/Continual-Intelligence/SEAL) · [Blog](https://jyopari.github.io/posts/seal)<br>
  Adam Zweiger et al. · MIT
- <a id="t04"></a>**The Surprising Effectiveness of Test-Time Training for Few-Shot Learning** · *[ICML 2025](https://proceedings.mlr.press/v267/akyurek25a.html)* · [Paper](https://arxiv.org/abs/2411.07279) · [Code (BBH)](https://github.com/adamzweiger/Fewshot-TTT) · [Code (ARC)](https://github.com/ekinakyurek/marc) · [HF Model](https://huggingface.co/ekinakyurek/marc-8B-finetuned-llama3) · [HF Adapters](https://huggingface.co/ekinakyurek/marc-lora-adapters-8B-finetuned-llama3)<br>
  Ekin Akyürek et al. · MIT
- <a id="t06"></a>**Titans: Learning to Memorize at Test Time** · *[NeurIPS 2025](https://proceedings.neurips.cc/paper_files/paper/2025/hash/a4ca07aa108036f80cbb5b82285fd4b1-Abstract-Conference.html)* · [Paper](https://arxiv.org/abs/2501.00663) · [Blog](https://research.google/blog/titans-miras-helping-ai-have-long-term-memory/)<br>
  Ali Behrouz, Peilin Zhong, Vahab Mirrokni · Google Research
- <a id="t10"></a>**TTRL: Test-Time Reinforcement Learning** · *[NeurIPS 2025](https://proceedings.neurips.cc/paper_files/paper/2025/hash/be690ea16f005c174f6c4102a5970e67-Abstract-Conference.html)* · [Paper](https://arxiv.org/abs/2504.16084) · [Code](https://github.com/PRIME-RL/TTRL)<br>
  Yuxin Zuo et al. · Tsinghua University; Shanghai AI Laboratory

### 2024

- <a id="t03"></a>**Test-Time Training on Nearest Neighbors for Large Language Models** · *[ICLR 2024](https://proceedings.iclr.cc/paper_files/paper/2024/hash/f02f1185b97518ab5bd7ebde466992d3-Abstract-Conference.html)* · [Paper](https://arxiv.org/abs/2305.18466) · [Code](https://github.com/socialfoundations/tttlm) · [HF Model (retriever)](https://huggingface.co/socialfoundations/roberta-large-pile-lr2e-5-bs16-8gpu-1700000)<br>
  Moritz Hardt, Yu Sun · Max Planck Institute for Intelligent Systems; University of Tübingen / Tübingen AI Center; Stanford University

### 2023

- <a id="ada"></a>**Human-Timescale Adaptation in an Open-Ended Task Space** · *[ICML 2023](https://proceedings.mlr.press/v202/bauer23a.html)* · [Paper](https://arxiv.org/abs/2301.07608)<br>
   Adaptive Agent Team et al. · DeepMind
- <a id="reflexion"></a>**Reflexion: Language Agents with Verbal Reinforcement Learning** · *[NeurIPS 2023](https://proceedings.neurips.cc/paper_files/paper/2023/hash/1b44b878bb782e6954cd888628510e90-Abstract-Conference.html)* · [Paper](https://arxiv.org/abs/2303.11366) · [Code](https://github.com/noahshinn/reflexion)<br>
  Noah Shinn et al. · Northeastern University; Massachusetts Institute of Technology; Princeton University

### 2022

- <a id="cotta"></a>**Continual Test-Time Domain Adaptation** · *[CVPR 2022](https://openaccess.thecvf.com/content/CVPR2022/html/Wang_Continual_Test-Time_Domain_Adaptation_CVPR_2022_paper.html)* · [Paper](https://arxiv.org/abs/2203.13591) · [Code](https://github.com/qinenergy/CoTTA)<br>
  Qin Wang, Olga Fink, Luc Van Gool, Dengxin Dai · ETH Zurich; Max Planck Institute for Informatics; EPFL; +1 institutions
- <a id="eata"></a>**Efficient Test-Time Model Adaptation without Forgetting** · *[ICML 2022](https://proceedings.mlr.press/v162/niu22a.html)* · [Paper](https://arxiv.org/abs/2204.02610) · [Code](https://github.com/mr-eggplant/EATA)<br>
  Shuaicheng Niu et al. · South China University of Technology; Tencent AI Lab; National University of Singapore
- <a id="self-initiated-owl"></a>**Self-Initiated Open World Learning for Autonomous AI Agents** · *[AAAI Spring Symposium Series 2022](https://arxiv.org/abs/2110.11385)* · [Paper](https://arxiv.org/abs/2110.11385)<br>
  Bing Liu, Eric Robertson, Scott Grigsby, Sahisnu Mazumder · University of Illinois at Chicago; PAR Government Systems Corporation
- <a id="ttt-mae"></a>**Test-Time Training with Masked Autoencoders** · *[NeurIPS 2022](https://proceedings.neurips.cc/paper_files/paper/2022/hash/bcdec1c2d60f94a93b6e36f937aa0530-Abstract-Conference.html)* · [Paper](https://arxiv.org/abs/2209.07522) · [Project](https://yossigandelsman.github.io/ttt_mae/index.html) · [Code](https://github.com/yossigandelsman/test_time_training_mae)<br>
  Yossi Gandelsman, Yu Sun, Xinlei Chen, Alexei A. Efros · University of California, Berkeley; Meta AI

### 2021

- <a id="tent"></a>**Tent: Fully Test-time Adaptation by Entropy Minimization** · *[ICLR 2021](https://arxiv.org/abs/2006.10726)* · [Paper](https://arxiv.org/abs/2006.10726) · [Code](https://github.com/DequanWang/tent)<br>
  Dequan Wang et al. · University of California, Berkeley; Adobe Research
- <a id="ttt-plus"></a>**TTT++: When Does Self-Supervised Test-Time Training Fail or Thrive?** · *[NeurIPS 2021](https://proceedings.neurips.cc/paper_files/paper/2021/hash/b618c3210e934362ac261db280128c22-Abstract.html)* · [Paper](https://proceedings.neurips.cc/paper_files/paper/2021/file/b618c3210e934362ac261db280128c22-Paper.pdf) · [Code](https://github.com/vita-epfl/ttt-plus-plus)<br>
  Yuejiang Liu et al. · EPFL

### 2020

- <a id="t02"></a>**Test Time Training with Self Supervision for Generalization under Distribution Shifts** · *[ICML 2020](https://proceedings.mlr.press/v119/sun20b.html)* · [Paper](https://proceedings.mlr.press/v119/sun20b.html) · [Code](https://github.com/yueatsprograms/ttt_cifar_release) · [Project](https://test-time-training.github.io/)<br>
  Yu Sun et al. · UC Berkeley; UC San Diego

### 2019

- <a id="t01"></a>**Dynamic Evaluation of Transformer Language Models** · *[arXiv 2019 (preprint)](https://arxiv.org/abs/1904.08378)* · [Paper](https://arxiv.org/abs/1904.08378) · [Code](https://github.com/benkrause/dynamiceval-transformer)<br>
  Ben Krause, Emmanuel Kahembwe, Iain Murray, Steve Renals · University of Edinburgh
- <a id="owl-product"></a>**Open-world Learning and Application to Product Classification** · *[WWW 2019](https://doi.org/10.1145/3308558.3313644)* · [Paper](https://arxiv.org/abs/1809.06004) · [Code](https://github.com/howardhsu/Meta-Open-World-Learning) · [Blog](https://howardhsu.github.io/article/owl/)<br>
  Hu Xu, Bing Liu, Lei Shu, P. Yu · University of Illinois at Chicago; Tsinghua University

### 2015

- <a id="open-world-recognition"></a>**Towards Open World Recognition** · *[CVPR 2015](https://openaccess.thecvf.com/content_cvpr_2015/html/Bendale_Towards_Open_World_2015_CVPR_paper.html)* · [Paper](https://openaccess.thecvf.com/content_cvpr_2015/html/Bendale_Towards_Open_World_2015_CVPR_paper.html) · [Author PDF](https://openaccess.thecvf.com/content_cvpr_2015/papers/Bendale_Towards_Open_World_2015_CVPR_paper.pdf)<br>
  Abhijit Bendale, Terrance Boult · University of Colorado at Colorado Springs

[↑ Contents](#contents)

<a id="systems"></a>

## 🛠️ Discovery Systems

*How can we build reliable discovery systems?*

### 2026

- <a id="paper-6e87228c64a8ec80"></a>**A Society of Researchers: Designing Institutions for Populations of Autonomous Research Agents** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.10468)* · [Paper](https://arxiv.org/abs/2610.10468)<br>
  Ali Asaria, Deep Gandhi, Tony Salomone · Transformer Lab
- <a id="d09"></a>**Accelerating scientific discovery with Co-Scientist** · *[Nature 2026](https://www.nature.com/articles/s41586-026-10644-y)* · [Paper](https://arxiv.org/abs/2502.18864)<br>
  Juraj Gottweis et al. · Google Cloud AI Research; Google DeepMind; Google Research; +4 institutions
- <a id="h02"></a>**Agent Lightning v1.0: Towards Harnessed Agentic RL** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2608.17528)* · [Paper](https://arxiv.org/abs/2608.17528) · [Code](https://github.com/microsoft/agent-lightning)<br>
  Zhiyuan He et al. · Microsoft; Fudan University; Zhejiang University; +1 institutions
- <a id="paper-07001ea82b328e28"></a>**AIM: Agentic Idea Management for Automated Research** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2609.38445)* · [Paper](https://arxiv.org/abs/2609.38445) · [Project](https://imhgchoi.github.io/agentic-idea-manager/)<br>
  Hyeong Kyu Choi et al. · Google Cloud AI Research; University of Wisconsin-Madison
- <a id="paper-7a8405c90f1854a1"></a>**ALF: An Active Learning Framework for Scientific Discovery** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2609.31197)* · [Paper](https://arxiv.org/abs/2609.31197) · [Code](https://github.com/instadeepai/alf) · [Project](https://instadeepai.github.io/alf/)<br>
  Shikha Surana et al. · InstaDeep; University College London; University of Oxford
- <a id="paper-c5f5637b6166e690"></a>**AReaL-RSI: Adaptive Scaling and Coordination of Recursive Self-Improvement** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.18083)* · [Paper](https://arxiv.org/abs/2610.18083) · [Code](https://github.com/areal-project/AReaL-RSI)<br>
  Wenhao Zhou et al. · Ant Group; Zhejiang University; HKUST
- <a id="paper-02c2d4bf0d53a944"></a>**ASENA: Self-evolving Agents for Embodied Navigation** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2609.39207)* · [Paper](https://arxiv.org/abs/2609.39207) · [Project](https://research.nvidia.com/labs/gear/asena/)<br>
  An-Chieh Cheng et al. · NVIDIA; University of California, San Diego; The University of Texas at Austin
- <a id="paper-1746b40a9100d582"></a>**AutoMark: Enabling Autoresearch to Discover Better LLM Watermarks** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2609.37310)* · [Paper](https://arxiv.org/abs/2609.37310) · [Code](https://github.com/eth-sri/automark) · [Project](https://www.sri.inf.ethz.ch/blog/automark)<br>
  Thibaud Gloaguen, Robin Staab, Martin Vechev · ETH Zurich
- <a id="a01"></a>**autoresearch** <sup>project</sup> · [Code](https://github.com/karpathy/autoresearch)<br>
  Andrej Karpathy
- <a id="paper-a5811dd93a29c236"></a>**AutoResearch at Production Scale: Failure Modes and a Multi-Agent Framework** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2609.30541)* · [Paper](https://arxiv.org/abs/2609.30541)<br>
  Aparajith Chandran et al. · Amazon
- <a id="paper-015983a5216461e4"></a>**Autoresearch in Mixed-Integer Linear and Nonlinear Programming** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2609.39360)* · [Paper](https://arxiv.org/abs/2609.39360)<br>
  Yuwei Gu et al. · Chengdu University of Information Technology; Eindhoven University of Technology; Nanyang University of Technology; +2 institutions
- <a id="paper-0fc21b6838fcff99"></a>**Beyond Maliciousness: Static and Runtime Attack-Surface Profiling of Agent Skills** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.19264)* · [Paper](https://arxiv.org/abs/2610.19264)<br>
  Ratnesh Pandey et al. · Metano Labs; Purdue University; VulNow
- <a id="paper-270d7139fe7e7927"></a>**Beyond Skill Evolution: Self-Evolving Context Management Policies for Long-Horizon Agent Harnesses** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2609.34649)* · [Paper](https://arxiv.org/abs/2609.34649)<br>
  Weiyuan Li et al. · School of Data Science, Fudan University; Shanghai Key Laboratory of Data Science; College of Computer Science and Artificial Intelligence, Fudan University
- <a id="paper-1e69ca6b1461149c"></a>**BrickWright: Agentic Creation of Physically Feasible Brick Builds** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.31651)* · [Paper](https://arxiv.org/abs/2610.31651) · [Project](https://avalovelace1.github.io/brickwright/) · [Code](https://github.com/AvaLovelace1/brickwright)<br>
  Ava Pun et al. · Carnegie Mellon University; Independent Researcher; Stanford University
- <a id="paper-66f56984b6446ca0"></a>**Building AI Research Teams for Autonomous Discovery of Linear Attention Architectures** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.28887)* · [Paper](https://arxiv.org/abs/2610.28887)<br>
  Yujian Liu et al. · UC Santa Barbara; Pennsylvania State University; LinkedIn
- <a id="paper-433abe28aa06ff75"></a>**Cache Engineering for Agents** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.28577)* · [Paper](https://arxiv.org/abs/2610.28577) · [Code](https://github.com/thu-nics/AKV)<br>
  Tianyu Fu et al. · Tsinghua University; The Chinese University of Hong Kong
- <a id="paper-0365f0df8dab5c31"></a>**Can Agent Harnesses and Inference Engines Hear Each Other? The HEAR Protocol for Agentic LLM Serving** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.06597)* · [Paper](https://arxiv.org/abs/2610.06597)<br>
  Jiaqi Zhao et al. · Harbin Institute of Technology (Shenzhen)
- <a id="station"></a>**Can AI Agents Make Open-Ended Scientific Discovery? Evidence from Station** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.08927)* · [Paper](https://arxiv.org/abs/2610.08927) · [Code](https://github.com/dualverse-ai/station-open-reseach) · [Data](https://github.com/dualverse-ai/station-open-reseach_data) · [Project](https://dualverse-ai.github.io/station-open-reseach_data)<br>
  Wenyu Du, Stephen Chung · DualverseAI; The University of Hong Kong; University of Cambridge
- <a id="paper-ab69aff2f86002f6"></a>**Can AI Scientists Coordinate at Runtime?** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.00980)* · [Paper](https://arxiv.org/abs/2610.00980) · [Code](https://github.com/systemind-team/Runtime-AI-Scientist) · [Project](https://systemind-team.github.io/Runtime-AI-Scientist/)<br>
  Zijian Liu et al. · University of Oxford; King Abdullah University of Science and Technology; University of Sydney; +1 institutions
- <a id="causalsteward"></a>**CausalSteward: An Agentic Divide-Conquer-Combine Copilot for Causal Discovery** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2607.01936)* · [Paper](https://arxiv.org/abs/2607.01936)<br>
  Nicholas Tagliapietra et al. · TU Darmstadt; Bosch Center for Artificial Intelligence; hessian.AI; +2 institutions
- <a id="paper-67f22dd62e086df9"></a>**Collaborative Principle Evolution via Evidence Transfer for Scientific Discovery** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2609.35315)* · [Paper](https://arxiv.org/abs/2609.35315)<br>
  Yingming Pu, Hongyu Chen, Tao Lin · Zhejiang University; Westlake University
- <a id="paper-83d8f02ebb01f589"></a>**Compile Once, Run Cheap: Frozen, Portable Skills for Embodied Agents, and What Recursive Self-Improvement Adds** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.25114)* · [Paper](https://arxiv.org/abs/2610.25114) · [Code](https://github.com/Orillusion/embodied-skill-rsi)<br>
  Jingwen Bai et al. · Beijing Ou Rui Ling Shi Technology Co., Ltd.; ChangingTek Robotics Technology (Suzhou) Co., Ltd.; Shanghai Yunfan Intelligent Control Robot Technology Co., Ltd.
- <a id="paper-d90f6364ce9b753e"></a>**Continual Graph Memory for Mathematical Research Agents** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.02945)* · [Paper](https://arxiv.org/abs/2610.02945) · [Code](https://github.com/uclanlp/continual-graph-memory)<br>
  Junyi Zhang et al. · University of California, Los Angeles
- <a id="paper-e6112360ce8388d8"></a>**Coral Discovery: The Division of Cognitive Labor in Autonomous Research** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.33281)* · [Paper](https://arxiv.org/abs/2610.33281)<br>
  Xinxing Ren et al. · Coral AI Labs; Università di Trento; Harvard University; +3 institutions
- <a id="paper-0c850351466e0ab2"></a>**DAGent: Evaluate-then-Grow Planning for Deep Research Agents** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2609.39154)* · [Paper](https://arxiv.org/abs/2609.39154) · [Code](https://github.com/hanwenliu6825/DAGent)<br>
  Hanwen Liu, Yuanfu Sun, Qiaoyu Tan · New York University; New York University Shanghai
- <a id="paper-1bad7b8c664a2eb2"></a>**DeepRewind: Predicting and Repairing Premature Commitments in Deep Research Agents** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2609.36344)* · [Paper](https://arxiv.org/abs/2609.36344) · [Code](https://github.com/AmirAbaskohi/DeepRewind)<br>
  Amirhossein Abaskohi et al. · University of British Columbia
- <a id="paper-a0694d5560c4572c"></a>**Demonstration of a Structured Agentic Workflow for Applied Quantum Computing Research** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.05304)* · [Paper](https://arxiv.org/abs/2610.05304) · [Project](https://haiqu.ai/agenticos)<br>
  Dikshant Dulal, Maxence Grandadam, Maciej Koch-Janusz, Mykola Maksymenko · Haiqu, Inc.
- <a id="paper-92174196b7146b88"></a>**Design Anything, Design at Scale** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.24771)* · [Paper](https://arxiv.org/abs/2610.24771) · [Code](https://github.com/Gemus-AI/DesignAnything) · [Dataset](https://huggingface.co/datasets/Gemus-AI/DesignAnything-Bench)<br>
  Xuchao Ren et al. · Tsinghua University; Beijing Institute of Fashion Technology; Massachusetts Institute of Technology; +1 institutions
- <a id="paper-7d2325553eb22ef0"></a>**Designing Collaborative AI-Driven Workflows for Scientific Software Engineering** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.09995)* · [Paper](https://arxiv.org/abs/2610.09995) · [Code](https://github.com/Lab-Notebooks/CodeScribe)<br>
  Akash Dhruv, Max Knobbe, Pedro Machado, Anshu Dubey · Argonne National Laboratory; Fermi National Accelerator Laboratory; RIKEN Center for Computational Science
- <a id="paper-33b8ee2d6304a602"></a>**DexAgent: An Agentic Human2Sim2Robot Framework for Dexterous Manipulation with Self-Evolving Tool Library** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2609.35318)* · [Paper](https://arxiv.org/abs/2609.35318) · [Project](https://dexagent1.github.io/) · [Code](https://github.com/dexagent1/DexAgent)<br>
  Youhui Wang et al. · Stanford University; Columbia University
- <a id="paper-f991937645caaaa5"></a>**DiffResearch: Accelerating Deep Research with Diffusion Language Models** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.28909)* · [Paper](https://arxiv.org/abs/2610.28909) · [Code](https://github.com/alanrbtx/DiffResearch)<br>
  Alan-Barsag Gazzaev, Alexey Gavrilov, Mikhail Mozikov, Sergey Muravyov · ITMO University; AXXX
- <a id="paper-69f6cbf39ab201a1"></a>**DynaHarness: A Dynamic Physical Harness for Self-Evolving Robot Agents** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2609.40306)* · [Paper](https://arxiv.org/abs/2609.40306) · [Project](https://denghaoyuan123.github.io/Dynaharness_page/)<br>
  Haoyuan Deng et al. · Nanyang Technological University; Nanjing University
- <a id="paper-5d0025a257e8df1b"></a>**Embodied Turing Machines: Stateful Code for Robot Recursive Self-Improvement** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.12369)* · [Paper](https://arxiv.org/abs/2610.12369) · [Project](https://etmcode-bit.github.io/)<br>
  Kairui Hu et al. · Nanyang Technological University; Ropedia
- <a id="paper-fd271a5f07c0fe55"></a>**EmbodiedSmith: Scaling Embodied Data through Recursive Self-Improvement Flywheel in Simulation** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.07969)* · [Paper](https://arxiv.org/abs/2610.07969)<br>
  Yikai Qin et al. · The Hong Kong University of Science and Technology (Guangzhou); Xiaomi Robotics; Southeastern University; +7 institutions
- <a id="paper-cf7a39add6564008"></a>**Epi: Towards a Persistent, Self-Improving Agent for Autonomous Research** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.24944)* · [Paper](https://arxiv.org/abs/2610.24944) · [Code](https://github.com/BakeLab/Epi-results) · [Project](https://www.bakelab.ai/research/articles/epi/)<br>
  Yue Huang et al. · Bake AI; University of Notre Dame; University of Washington; +10 institutions
- <a id="eurekagent"></a>**EurekAgent: Agent Environment Engineering is All You Need For Autonomous Scientific Discovery** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2606.13662)* · [Paper](https://arxiv.org/abs/2606.13662) · [Code](https://github.com/THU-Team-Eureka/EurekAgent)<br>
  Amy Xin et al. · Tsinghua University; Renmin University of China
- <a id="paper-a05a302fbb0b80d4"></a>**EvoCast: Reliable Autonomous Research Agents for Iterative Forecasting Architecture Evolution** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.04517)* · [Paper](https://arxiv.org/abs/2610.04517) · [Code](https://github.com/18e0-x/EvoCast)<br>
  Kaipeng Xu et al. · Jiangnan University; Southeast University
- <a id="paper-293e9f771c126e3f"></a>**EvolvAttack: Backdooring self Evolving VLM Agents** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.15244)* · [Paper](https://arxiv.org/abs/2610.15244)<br>
  Chuan Zou et al. · University of Pennsylvania; Brown University; Nanyang Technological University; +2 institutions
- <a id="paper-f8f021c90e8a1d58"></a>**Evolve Together, Fall into Place: How Social Scaffolding Shapes Self-Evolving Multi-Agent Systems** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.19799)* · [Paper](https://arxiv.org/abs/2610.19799)<br>
  Seojin Hwang, Youngmin Choi, Hwanhee Lee · Chung-Ang University
- <a id="paper-25c116ef8f23e7f4"></a>**EvoSteer: Online Self-Evolving Graph Orchestration via Reference-Anchored Credit Assignment** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2609.38661)* · [Paper](https://arxiv.org/abs/2609.38661) · [Code](https://github.com/beita6969/evosteer) · [HF Model](https://huggingface.co/beita6969/EvoSteer-9b)<br>
  Mingda Zhang et al. · The Chinese University of Hong Kong, Shenzhen; Dalian University of Technology; Fudan University; +3 institutions
- <a id="paper-d03c4239f891aa34"></a>**Federation over Harness** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.24007)* · [Paper](https://arxiv.org/abs/2610.24007) · [Code](https://github.com/dixiyao/FoH)<br>
  Dixi Yao, Tahseen Rabbani, Tian Li · University of Chicago
- <a id="paper-94dad5340d5493a7"></a>**FlowState: Execution State as Memory for Long-Horizon LLM Agents** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2609.34565)* · [Paper](https://arxiv.org/abs/2609.34565)<br>
  Minghao Li et al. · Ant International; Ant Group
- <a id="paper-e14cabb1256a4b15"></a>**Fork-and-Flush: Escaping Idea Basins in Autoresearch Agents** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.07447)* · [Paper](https://arxiv.org/abs/2610.07447)<br>
  Ziyang Cai et al. · Microsoft Research
- <a id="paper-0d8be09c556e897e"></a>**From VLM Planners to Robotic Agents: Self-Evolving Harnesses for History-Dependent Manipulation** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.29560)* · [Paper](https://arxiv.org/abs/2610.29560)<br>
  Tingwen Du et al. · University of Science and Technology of China; Shanghai Artificial Intelligence Laboratory; Shanghai Jiao Tong University; +2 institutions
- <a id="paper-aa714b09dd384ec0"></a>**GitSwarm: Decentralized Compounding Inference** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.04862)* · [Paper](https://arxiv.org/abs/2610.04862) · [Project](https://veds12.github.io/git-swarm/)<br>
  Vedant Shah et al. · Meta Superintelligence Labs; Mila - Québec AI Institute; Université de Montréal; +3 institutions
- <a id="paper-7be1f38a8edb49a3"></a>**Harness Self-Evolution for Long-Horizon Terminal Agents** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.27435)* · [Paper](https://arxiv.org/abs/2610.27435)<br>
  Ruhan Wang et al. · Tencent HY LLM Frontier; Indiana University; University of Maryland, College Park; +2 institutions
- <a id="h03"></a>**Harness-1: Reinforcement Learning for Search Agents with State-Externalizing Harnesses** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2606.02373)* · [Paper](https://arxiv.org/abs/2606.02373) · [Code](https://github.com/pat-jj/harness-1) · [HF Model](https://huggingface.co/pat-jj/harness-1) · [HF Dataset](https://huggingface.co/datasets/pat-jj/harness-1-train-data)<br>
  Pengcheng Jiang et al. · University of Illinois Urbana-Champaign; UC Berkeley; Chroma
- <a id="paper-9e49e6d93707d1f6"></a>**Harness^2: Recursive Agent Harnessing for an Open World** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.14224)* · [Paper](https://arxiv.org/abs/2610.14224) · [Code](https://github.com/google-research/harness2) · [Project](https://harness2.github.io/)<br>
  Ruiyao Xu et al. · Northwestern University; Google Cloud AI Research
- <a id="paper-302d003c6e0122f1"></a>**HarnessMM: Recursive Self-Improvement for Harness Token Efficiency** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.32813)* · [Paper](https://arxiv.org/abs/2610.32813)<br>
  Yuhua Jiang, Chang Xu, Feifei Gao, Li Zhao · Tsinghua University; Microsoft Research Asia (MSRA)
- <a id="paper-ed9e613c992f87fc"></a>**Hidden Messages Between Diffusion Language Model Agents: Causal Evidence for Latent Communication** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.28905)* · [Paper](https://arxiv.org/abs/2610.28905) · [Code](https://github.com/alanrbtx/hidden-messages-diffusion-agents)<br>
  Alan-Barsag Gazzaev, Alexey Gavrilov, Sergey Muravyov, Ilya Makarov · ITMO University; HSE University
- <a id="paper-bd5dfa376cbe2ce7"></a>**HiSTEVE 1.0: Harnessing Human-Interface VLA Agents for Open-World Games** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.31162)* · [Paper](https://arxiv.org/abs/2610.31162)<br>
  Zecong Tang et al. · The University of Hong Kong; Zhejiang University; Fudan University; +2 institutions
- <a id="paper-52de31b79b695201"></a>**IF-MAP: Influence-Function-Inspired Agent Prioritization in Multi-Agent Systems** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.24383)* · [Paper](https://arxiv.org/abs/2610.24383) · [Code](https://github.com/s1412/IF-MAP)<br>
  Jie Mao et al. · The Chinese University of Hong Kong, Shenzhen; Harbin Institute of Technology; School of Engineering and Applied Sciences, Harvard University
- <a id="paper-50201f413f6c1220"></a>**Is Complex Agentic Memory Always Needed? Naive RAG Is Stronger Than We Thought** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.30755)* · [Paper](https://arxiv.org/abs/2610.30755) · [Code](https://github.com/Litmeb/RAW-RAG)<br>
  Zhengye Bao et al. · Luo Lab Undergraduate Division (LUD), Xi’an Jiaotong University; Shanghai Jiao Tong University; Zhejiang University; +1 institutions
- <a id="paper-ff469b4c8e0c8634"></a>**JANUS: Enhancing Long-Horizon Autonomous Research with Co-Evolving World Models** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.13194)* · [Paper](https://arxiv.org/abs/2610.13194) · [Project](https://github.com/bilemond/JANUS)<br>
  Mengdi Liu et al. · State Key Laboratory of AI Safety, Institute of Computing Technology, CAS, China; University of Chinese Academy of Sciences (CAS), China
- <a id="paper-724ade21f496c142"></a>**JevGPT: Thinking Fast and Slow in Autonomous Research** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.18272)* · [Paper](https://arxiv.org/abs/2610.18272) · [Project](https://sunyasheng.github.io/projects/JevGPT.html) · [Code](https://github.com/sunyasheng/JevGPT) · [Dataset](https://huggingface.co/datasets/yashengsun/JevGPT-runs)<br>
  Yasheng Sun et al. · King Abdullah University of Science and Technology (KAUST)
- <a id="paper-6f2e8465da82c5f3"></a>**Large Knowledge Model: A Knowledge Foundation for Agentic Science at Scale** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2609.27297)* · [Paper](https://arxiv.org/abs/2609.27297) · [Project](https://lkm.bohrium.com/web/en) · [Code](https://github.com/dptech-corp/bohrium-skills)<br>
  Yuan Huang et al. · DP Technology; Institute of Theoretical Physics, Chinese Academy of Sciences; International Center for Quantum Materials, School of Physics, Peking University; +4 institutions
- <a id="paper-fc3b7e421ef0a1e9"></a>**LegoSR: A Unified Framework for Self-improving Agent-Guided Scientific Discovery** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.33465)* · [Paper](https://arxiv.org/abs/2610.33465) · [Code](https://github.com/Scientific-Artificial-Intelligence-Lab/kd)<br>
  Hao Mao et al. · The Hong Kong Polytechnic University, Hong Kong SAR, China; Amazon Web Services, Seattle, USA; University of Washington, Seattle, USA; +3 institutions
- <a id="paper-1d9cf5babf2989a2"></a>**Librarian Agents: Training LLMs to Curate Long-Context Workspaces that Anticipate Future Queries** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.22273)* · [Paper](https://arxiv.org/abs/2610.22273) · [Project](https://librarian-agents.github.io/) · [Code](https://github.com/teresaz05/librarian-agents)<br>
  Anikait Singh et al. · Stanford University; Carnegie Mellon University
- <a id="paper-79115fb39819fd02"></a>**MaD-RSI: Model-as-Data for Recursive Self-Improvement of Agent Harnesses** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.28201)* · [Paper](https://arxiv.org/abs/2610.28201)<br>
  Yu Cui et al. · Beijing Institute of Technology; Tsinghua University; Chengdu Institute of Computer Applications, Chinese Academy of Sciences; +4 institutions
- <a id="paper-ddad85e61e90e037"></a>**MemPilot: Orchestrating On-Demand Multimodal Memory Curation for LLM Agents** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.06830)* · [Paper](https://arxiv.org/abs/2610.06830) · [Project](https://viktoraxelsen.github.io/MemPilot/) · [Code](https://github.com/ViktorAxelsen/MemPilot)<br>
  Haozhen Zhang et al. · Nanyang Technological University; Tsinghua University; University of Illinois Urbana-Champaign
- <a id="paper-0ed8e563cfef8c1c"></a>**MIRA: A Multimodal Illustrated Deep Research Agent for Controllable Reports** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.25926)* · [Paper](https://arxiv.org/abs/2610.25926) · [Project](https://mira-mmdeepresearch.github.io/)<br>
  Hongrui Wu et al. · Stanford University; The Hong Kong University of Science and Technology; JD.com; +3 institutions
- <a id="paper-fb16b20d25ce57e6"></a>**NeuroAct: Advancing EEG Analysis and Decoding via Dual-Loop Autonomous Research** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.25211)* · [Paper](https://arxiv.org/abs/2610.25211)<br>
  Wei Xiong et al. · Tongji University; Ant Group; Shanghai Jiao Tong University; +1 institutions
- <a id="paper-b401e2f2acb005b6"></a>**OfficeTown: Generative Organizations for Evolving Agent Intelligence** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.23194)* · [Paper](https://arxiv.org/abs/2610.23194) · [Project](https://officeintelligence.github.io/)<br>
  Hongchen Wei et al. · Wuhan University; University of California, San Diego; South China University of Technology; +3 institutions
- <a id="paper-42c33aa80d5fcaf8"></a>**OMAR: Open-World Multi-Attribute Reasoning for Scene-Conditioned Shelf Organization** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.29761)* · [Paper](https://arxiv.org/abs/2610.29761)<br>
  Benedikt Kreis et al. · University of Bonn; Lamarr Institute for ML and AI; Technical University of Darmstadt
- <a id="paper-ae989ddb519ce3e3"></a>**OpenSaC: A Python Library for Search as Code in Deep Research Agents** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.25779)* · [Paper](https://arxiv.org/abs/2610.25779) · [Code](https://github.com/liuqi6777/OpenSaC)<br>
  Qi Liu et al. · Renmin University of China; National University of Singapore
- <a id="paper-18f922743caba570"></a>**OpenVLHarness: Real World Visual Agentic Tool-Use with Multimodal Memory** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.26860)* · [Paper](https://arxiv.org/abs/2610.26860) · [Project](https://openvlharness.github.io/) · [Code](https://github.com/uclanlp/OpenVLHarness) · [Dataset](https://huggingface.co/datasets/uclanlp/OpenVLHarness-Evaluation-Datasets) · [Project](https://openvlharness.github.io)<br>
  Yu Zhou et al. · University of California, Los Angeles; Apple
- <a id="paper-e7b1d34663a13626"></a>**Origin Attribution for Unsafe Behavior in Self-Evolving Multi-Agent Coding Systems** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.17488)* · [Paper](https://arxiv.org/abs/2610.17488) · [Code](https://anonymous.4open.science/r/origin-in-self-evovling-multi-agent-8818/README.md)<br>
  Hanyi Yu, Jiaming Cui · University of Southern California; Virginia Tech
- <a id="paper-d762df67a1c93fa4"></a>**PaperFormalizer: Author-in-the-Loop Autoformalization of Research Papers in Lean** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.31810)* · [Paper](https://arxiv.org/abs/2610.31810) · [Code](https://github.com/Jiyuan-Tan/PaperFormalizer) · [Project](https://paperformalizer.org)<br>
  Jiyuan Tan, Vasilis Syrgkanis, Jose Blanchet · Stanford University
- <a id="paper-1ad6e160560ae715"></a>**RankEvolve: A Reliable Multi-Agent Auto-Research Harness for Evolving Ranking Models** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2609.39551)* · [Paper](https://arxiv.org/abs/2609.39551)<br>
  Zheng Chen, Linfeng Liu, Hong Li, Hong Yan · Meta
- <a id="paper-d4244eed905302a2"></a>**RegenHarness: A Robot Agent Harness with Evidence-Gated Recursive Self-Improvement** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2609.27612)* · [Paper](https://arxiv.org/abs/2609.27612)<br>
  Kailin Wang et al. · AI Lab, Country Garden Services Group; School of Mechanical Science and Engineering, Huazhong University of Science and Technology; Omni AI
- <a id="paper2agent"></a>**Reimagining research papers as interactive and reliable AI agents** · *[Nature 2026](https://www.nature.com/articles/s41586-026-11044-y)* · [Paper](https://www.nature.com/articles/s41586-026-11044-y) · [Preprint](https://arxiv.org/abs/2509.06917) · [Code](https://github.com/jmiao24/Paper2Agent)<br>
  Jiacheng Miao et al. · Stanford University
- <a id="paper-612d122323ff66e0"></a>**Rethinking Verification in Agent Harnesses** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.34577)* · [Paper](https://arxiv.org/abs/2610.34577)<br>
  Zhengxin Zhang et al. · Cornell University; Alibaba Group
- <a id="paper-c97a20989ff958e4"></a>**RIDAR: Safeguarding Research Integrity in Autonomous Research Agents via Automated Detection and Runtime Intervention** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.31372)* · [Paper](https://arxiv.org/abs/2610.31372) · [Code](https://github.com/THU-KEG/RIDAR)<br>
  Jiening Siow et al. · Department of Computer Science and Technology, Tsinghua University; School of Information, Renmin University of China; Zhipu AI
- <a id="paper-e839b2c23d29e7f5"></a>**RIVO: Lightweight Adaptive Rerouting for Deep Research Agents** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.15910)* · [Paper](https://arxiv.org/abs/2610.15910)<br>
  Mingchen Li, Jiatan Huang, Hong Yu · University of Massachusetts, Amherst; University of Connecticut
- <a id="robin"></a>**Robin: A multi-agent system for automating scientific discovery** · *[Nature 2026](https://www.nature.com/articles/s41586-026-10652-y)* · [Paper](https://arxiv.org/abs/2505.13400)<br>
  Ali Essam Ghareeb et al. · FutureHouse; University of Oxford
- <a id="paper-26d90efac0c84106"></a>**RoboHarness: A Simple Harness Outperforms VLA and World Action Models** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.14018)* · [Paper](https://arxiv.org/abs/2610.14018) · [Code](https://github.com/BinceQu/RoboHarness) · [Project](https://bincequ.github.io/RoboHarness)<br>
  Bince Qu, Wei Chen, Bo Zhang · Zhejiang University
- <a id="paper-c397688c68ae69b3"></a>**RoleFlow: Self-Evolving Multi-Role Agentic Collaboration via Structural Adaptation** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.30429)* · [Paper](https://arxiv.org/abs/2610.30429)<br>
  Yi Ge et al. · University of Maryland, College Park; University of Pittsburgh; The University of Texas at Dallas
- <a id="paper-da0b864f0a61a686"></a>**RouteWeaver: Weaving Mode Selection and Execution into Unified LLM Routing** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.19705)* · [Paper](https://arxiv.org/abs/2610.19705) · [Code](https://github.com/LaughKing/RouteWeaver) · [Project](https://laughking.github.io/RouteWeaver/)<br>
  Xiaohan Wang et al. · Nanyang Technological University; Huazhong University of Science and Technology; University of Illinois Urbana-Champaign
- <a id="paper-5946c006a4e58dd8"></a>**RSIGym: A Flexible Environment for Recursive Self-Improvement** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.10310)* · [Paper](https://arxiv.org/abs/2610.10310) · [Code](https://github.com/evolvent-ai/RSIGym) · [Project](https://rsi-index.ai/)<br>
  Fanqing Meng et al. · Evolvent AI; National University of Singapore
- <a id="paper-f17d395d9610cd5a"></a>**RSIHub: A Composable Framework for Agent-Evolution Methods** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.32253)* · [Paper](https://arxiv.org/abs/2610.32253) · [Code](https://github.com/simple-agent-lab/RSIHub) · [Project](https://simpleagentlab.com/rsihub/)<br>
  Zimu Wang et al. · University of California, Berkeley; University of Science and Technology of China; Douyin Group; +4 institutions
- <a id="paper-09c8b51fd5a44907"></a>**S-Agent 2.0: Spatial Reasoning with a General Coding Agent** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.28354)* · [Paper](https://arxiv.org/abs/2610.28354) · [Project](https://ropedia.github.io/S-Agent-2.0) · [Code](https://github.com/Ropedia/S-Agent-2.0)<br>
  Rui Gong et al. · Nanyang Technological University; University of Hong Kong; Ropedia
- <a id="paper-029806d18c63cad7"></a>**Same Simulation, Different Evidence: Where Retrieved Tool Output Costs LLM Agents Accuracy** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.26836)* · [Paper](https://arxiv.org/abs/2610.26836) · [Code](https://github.com/grenadeComing/same-simulation-different-evidence) · [Dataset](https://huggingface.co/datasets/grenadeComing/same-simulation-different-evidence)<br>
  Ke Zhang et al. · University of California, Riverside; University of California, Irvine
- <a id="paper-b16db32e289347ac"></a>**Scaling Discovery Requires Forgetting** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.20563)* · [Paper](https://arxiv.org/abs/2610.20563)<br>
  Shangyin Tan et al. · UC Berkeley; Stanford; Bespoke Labs
- <a id="paper-38f74d617740ea23"></a>**SEIS: Self-Evolving Inference Systems** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.04646)* · [Paper](https://arxiv.org/abs/2610.04646) · [Project](https://nehzux.github.io/SEIS/) · [Code](https://github.com/smth-fun/self-evolving-inference-system)<br>
  Zhen Xu et al. · University of Chicago
- <a id="paper-644afb0b5cb55eed"></a>**SEPM: Self-Evolving Procedural Memory Grounded in Task Graphs for Multi-Agent Collaboration** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.14515)* · [Paper](https://arxiv.org/abs/2610.14515) · [Code](https://github.com/cookieApril/SEPM)<br>
  Yi Liu et al. · Beijing University of Posts and Telecommunications; China Telecom
- <a id="paper-e3c5bce0180303e4"></a>**Skip the Compressor: Coding Agents Fix More Issues When They Pick Whole Files** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.21073)* · [Paper](https://arxiv.org/abs/2610.21073)<br>
  Xiaocong Yang et al. · University of Illinois Urbana-Champaign
- <a id="paper-17d0bb9aaa5e2f73"></a>**Sol-H3: Recursive Self-Improvement for MiniMax-H3 Inference Acceleration on Sol-Engine across Cloud and Edge** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2609.35110)* · [Paper](https://arxiv.org/abs/2609.35110) · [Code](https://github.com/NVlabs/Sana/tree/sol-engine/models/minimax_h3) · [Project](https://nvlabs.github.io/Sana/Sol-Engine/Sol-H3/)<br>
  Yitong Li et al. · NVIDIA Research
- <a id="paper-7cbe516dd8f1d6f6"></a>**SplatLab: Autonomous Scientific Discovery for 3DGS Research** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.30468)* · [Paper](https://arxiv.org/abs/2610.30468) · [Code](https://github.com/seemandhar/SplatLab) · [Project](https://seemandharjain.com/splatlab/)<br>
  Seemandhar Jain, Manmohan Chandraker · University of California San Diego
- <a id="paper-3f04751adc624bfa"></a>**Stateless Language Agents: Scaling Long-Horizon Automated Research** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.07625)* · [Paper](https://arxiv.org/abs/2610.07625) · [Project](https://github.com/Alex-q-z/stateless-language-agents)<br>
  Qizheng Zhang et al. · Stanford University; Carnegie Mellon University; University of Washington; +2 institutions
- <a id="paper-ef8dd675a4428711"></a>**StopLoss: Teaching Agents to Predict Failure and Stop Early** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.25525)* · [Paper](https://arxiv.org/abs/2610.25525) · [Code](https://github.com/TIGER-AI-Lab/StopLoss) · [Dataset](https://huggingface.co/datasets/TIGER-Lab/StopLoss-Training-Data) · [HF Model](https://huggingface.co/TIGER-Lab/StopLoss-Qwen2.5-7B-Instruct) · [HF Model](https://huggingface.co/TIGER-Lab/StopLoss-Qwen3-8B) · [HF Model](https://huggingface.co/TIGER-Lab/StopLoss-Qwen2.5-Coder-7B-Instruct)<br>
  Jiarong Liang et al. · University of Waterloo
- <a id="paper-65df409d4e89a361"></a>**STRATA: Self-Maintaining Structured Experience Graphs for Self-Evolving Language Agents** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.19386)* · [Paper](https://arxiv.org/abs/2610.19386)<br>
  Guanhua Zhu et al. · New Jersey Institute of Technology; The Chinese University of Hong Kong, Shenzhen
- <a id="paper-7879d80f8ba77ad5"></a>**StreamVibe: Proactive Video Agents for Evolving User Intent** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.34662)* · [Paper](https://arxiv.org/abs/2610.34662) · [Project](https://stream-vibe.github.io/)<br>
  Chengzhi Liu et al. · Google; University of California, Santa Barbara; University of California, Santa Cruz; +4 institutions
- <a id="paper-9a1928b04ab3c14c"></a>**TabFM-Auto: Self-Evolving Pipelines for Tabular Foundation Models** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2609.37989)* · [Paper](https://arxiv.org/abs/2609.37989)<br>
  Deqing Fu et al. · Google Research; Google DeepMind; University of Southern California; +2 institutions
- <a id="paper-94d2abf0fb9eec2d"></a>**TCMScience: An Autonomous Scientist for Traditional Chinese Medicine** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.24601)* · [Paper](https://arxiv.org/abs/2610.24601) · [Code](https://github.com/IMPF-AI-Institute/TCMScience)<br>
  Yanlan Kang et al. · Institute of Medical Philosophy & Future AI (IMPF-AI); Shanghai Medical College, Fudan University; Guangdong Provincial Key Laboratory of New Drug Screening and Guangdong–Hong Kong–Macao Joint Laboratory for New Drug Screening, School of Pharmaceutical Sciences, Southern Medical University; +4 institutions
- <a id="paper-4cca51b1d2fa9e6f"></a>**The Agentic Scientist: Orchestrating Coding Agents for Automated Scientific (Co-)Discovery** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.18933)* · [Paper](https://arxiv.org/abs/2610.18933) · [Code](https://github.com/SakanaAI/AI-Scientist-v3) · [Code](https://github.com/SakanaAI/AutoIllustrate) · [Project](https://pub.sakana.ai/agentic-scientist/) · [Model](https://github.com/RobertTLange/evosax/releases/tag/v.0.3.2)<br>
  Robert Tjarko Lange et al. · Sakana AI
- <a id="ai-scientist"></a>**The AI Scientist: Towards Fully Automated Open-Ended Scientific Discovery** · *[Nature 2026](https://www.nature.com/articles/s41586-026-10265-5)* · [Paper](https://arxiv.org/abs/2408.06292) · [Code](https://github.com/SakanaAI/AI-Scientist)<br>
  Chris Lu et al. · Sakana AI; University of Oxford; University of British Columbia; +2 institutions
- <a id="paper-3e1d6c58b4640b70"></a>**The Last Remote Sensing Model Built by Humans? Casting Any Earth Observation Task as Recursive Self-Improvement** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.18845)* · [Paper](https://arxiv.org/abs/2610.18845) · [Code](https://github.com/Yokoya-Lab-UTokyo/RSI4EO)<br>
  Sijie Zhao et al. · The University of Tokyo; RIKEN; Stanford University
- <a id="paper-8bd50ae4a7caaa00"></a>**Topological Coherence for Self-evolving Multi-agent Systems** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2609.37953)* · [Paper](https://arxiv.org/abs/2609.37953)<br>
  Sen Zhao et al. · Chongqing University of Posts and Telecommunications; Towngas
- <a id="paper-1858a2655b0e1621"></a>**Trust Mechanisms for Offline Generative AI at the Edge: A Connectivity-Regime Framework and an Empirical Study on a Raspberry Pi 5** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.33732)* · [Paper](https://arxiv.org/abs/2610.33732)<br>
  Georgios Feretzakis, Alexandros Papaspyridis · securagen.ai
- <a id="paper-8324cd60ab31faa0"></a>**VibeGame: Prompt-to-Game Development with AI-Native Engine and Self-Evolving Adversarial Agent Team** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.33106)* · [Paper](https://arxiv.org/abs/2610.33106) · [Code](https://github.com/tettethu/VibeGame) · [Project](https://vibegame.tettet.org/)<br>
  Wenbo Hu et al. · PRLab, Nanjing University; S-Lab, Nanyang Technological University; Liblib.ai
- <a id="paper-0f5aefdeeb0a0bf5"></a>**VideoEvoHarness: Self Evolving Agent Harness from Unlabeled Videos for Video Understanding** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.15389)* · [Paper](https://arxiv.org/abs/2610.15389) · [Code](https://github.com/Wei-Xin-Xu/VideoEvoHarness)<br>
  Weixin Xu et al. · Institute of Automation, Chinese Academy of Sciences; School of Advanced Interdisciplinary Sciences, University of Chinese Academy of Sciences; School of Computer Science and Communication Engineering, Jiangsu University of Science and Technology; +3 institutions
- <a id="paper-e34289be07a8d724"></a>**VPEvolve: A Self-Evolving Virtual Process Engineer for Computational Lithography** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2609.32473)* · [Paper](https://arxiv.org/abs/2609.32473) · [Project](https://true-litianyi.github.io/VPEVOLVE/) · [Code](https://github.com/True-Litianyi/VPEVOLVE_code)<br>
  Tianyi Li et al. · ShanghaiTech University; ZeroShot Co., Ltd.; Shanghai Optoelectronics Science and Technology Innovation Center
- <a id="paper-416fa880cfacea9c"></a>**WeaveData: A Multimodal Data Analysis System with Self-Critiquing and Self-Evolving LLM Plans** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2609.34764)* · [Paper](https://arxiv.org/abs/2609.34764)<br>
  Min Jia et al. · Northwest A&F University; East China Normal University; Renmin University of China; +1 institutions
- <a id="paper-8f34f3543ab3e50d"></a>**What Git Does Not Record: Provenance Legibility in Two AI-Assisted Research Repositories** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.28655)* · [Paper](https://arxiv.org/abs/2610.28655) · [Code](https://github.com/ktwu01/git-provenance-auditor)<br>
  Koutian Wu, Zesen Huang, Hejia Geng · The University of Texas at Austin; University of California, Los Angeles; University of Oxford
- <a id="paper-81e562d86820e0f8"></a>**What It Is, Not What It Says: Securing Agentic Browsing Interactions with Web Semantics** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.22697)* · [Paper](https://arxiv.org/abs/2610.22697) · [Code](https://github.com/llm-platform-security/intact) · [Dataset](https://huggingface.co/datasets/umariqbal/web-agent-attack-benchmark)<br>
  Umar Iqbal · Washington University in St. Louis
- <a id="paper-ef09ae7b3870a9b3"></a>**YouRA: A Persistent-State Architecture for Evidence-Traceable Autonomous Research Agents** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.01097)* · [Paper](https://arxiv.org/abs/2610.01097) · [Code](https://github.com/PrayPrey/Your-Research-Agent)<br>
  Yoonkyu Woo, Woojin Lee, Jin-xia Huang · Electronics and Telecommunications Research Institute; Department of Artificial Intelligence, University of Science and Technology

### 2025

- <a id="agent-laboratory"></a>**Agent Laboratory: Using LLM Agents as Research Assistants** · *[Findings of EMNLP 2025](https://aclanthology.org/2025.findings-emnlp.320/)* · [Paper](https://arxiv.org/abs/2501.04227) · [Project](https://AgentLaboratory.github.io/) · [Code](https://github.com/SamuelSchmidgall/AgentLaboratory)<br>
  Samuel Schmidgall et al. · AMD; Johns Hopkins University; ETH Zurich
- <a id="r02"></a>**Agent Lightning: Train ANY AI Agents with Reinforcement Learning** · *[arXiv 2025 (preprint)](https://arxiv.org/abs/2508.03680)* · [Paper](https://arxiv.org/abs/2508.03680) · [Code](https://github.com/microsoft/agent-lightning)<br>
  Xufang Luo et al. · Microsoft Research
- <a id="agentrxiv"></a>**AgentRxiv: Towards Collaborative Autonomous Research** · *[arXiv 2025 (preprint)](https://arxiv.org/abs/2503.18102)* · [Paper](https://arxiv.org/abs/2503.18102) · [Project](https://AgentRxiv.github.io/) · [Code](https://github.com/SamuelSchmidgall/AgentLaboratory)<br>
  Samuel Schmidgall, Michael Moor · Johns Hopkins University; ETH Zurich
- <a id="ai-researcher"></a>**AI-Researcher: Autonomous Scientific Innovation** · *[NeurIPS 2025](https://proceedings.neurips.cc/paper_files/paper/2025/hash/0d904d300a105809a2114d727851e759-Abstract-Conference.html)* · [Paper](https://arxiv.org/abs/2505.18705) · [Code](https://github.com/HKUDS/AI-Researcher)<br>
  Jiabin Tang, Lianghao Xia, Zhonghang Li, Chao Huang · The University of Hong Kong
- <a id="a02"></a>**AlphaEvolve: A coding agent for scientific and algorithmic discovery** · *[arXiv 2025 (preprint)](https://arxiv.org/abs/2506.13131)* · [Paper](https://arxiv.org/abs/2506.13131) · [Blog](https://deepmind.google/blog/alphaevolve-a-gemini-powered-coding-agent-for-designing-advanced-algorithms/) · [Results](https://github.com/google-deepmind/alphaevolve_results)<br>
  Alexander Novikov et al. · Google DeepMind
- <a id="biodiscoveryagent"></a>**BioDiscoveryAgent: An AI Agent for Designing Genetic Perturbation Experiments** · *[ICLR 2025](https://proceedings.iclr.cc/paper_files/paper/2025/hash/4252dc94531833029000f85dc5fac792-Abstract-Conference.html)* · [Paper](https://arxiv.org/abs/2405.17631) · [Code](https://github.com/snap-stanford/BioDiscoveryAgent)<br>
  Yusuf Roohani et al. · Stanford University; Arc Institute; Gladstone-UCSF Institute of Genomic Immunology; +1 institutions
- <a id="curie"></a>**Curie: Toward Rigorous and Automated Scientific Experimentation with AI Agents** · *[arXiv 2025 (preprint)](https://arxiv.org/abs/2502.16069)* · [Paper](https://arxiv.org/abs/2502.16069) · [Code](https://github.com/Just-Curieous/Curie)<br>
  Patrick Tser Jern Kon et al. · University of Michigan; Cisco Systems
- <a id="h06"></a>**Effective Harnesses for Long Running Agents** <sup>blog</sup> · [Code](https://github.com/anthropics/claude-quickstarts/tree/main/autonomous-coding) · [Blog](https://www.anthropic.com/engineering/effective-harnesses-for-long-running-agents)<br>
  Justin Young · Anthropic
- <a id="kosmos"></a>**Kosmos: An AI Scientist for Autonomous Discovery** · *[arXiv 2025 (preprint)](https://arxiv.org/abs/2511.02824)* · [Paper](https://arxiv.org/abs/2511.02824) · [Results](https://github.com/EdisonScientific/kosmos-figures)<br>
  Ludovico Mitchener et al. · Edison Scientific; University of Oxford
- <a id="d08"></a>**The AI Scientist-v2: Workshop-Level Automated Scientific Discovery via Agentic Tree Search** · *[arXiv 2025 (preprint)](https://arxiv.org/abs/2504.08066)* · [Paper](https://arxiv.org/abs/2504.08066) · [Code](https://github.com/SakanaAI/AI-Scientist-v2)<br>
  Yutaro Yamada et al. · Sakana AI; University of British Columbia; Vector Institute; +2 institutions
- <a id="virtual-lab"></a>**The Virtual Lab of AI agents designs new SARS-CoV-2 nanobodies** · *[Nature 2025](https://www.nature.com/articles/s41586-025-09442-9)* · [Paper](https://www.nature.com/articles/s41586-025-09442-9) · [Code](https://github.com/zou-group/virtual_lab)<br>
  Kyle Swanson et al. · Stanford University; Chan Zuckerberg Biohub

### 2024

- <a id="chemcrow"></a>**Augmenting large language models with chemistry tools** · *[Nature Machine Intelligence 2024](https://www.nature.com/articles/s42256-024-00832-8)* · [Paper](https://arxiv.org/abs/2304.05376) · [Code](https://github.com/ur-whitelab/chemcrow-public) · [Runs](https://github.com/ur-whitelab/chemcrow-runs)<br>
  Andres M Bran et al. · EPFL; University of Rochester; IBM Research Europe

### 2023

- <a id="a-lab"></a>**An autonomous laboratory for the accelerated synthesis of inorganic materials** · *[Nature 2023](https://www.nature.com/articles/s41586-023-06734-w)* · [Paper](https://www.nature.com/articles/s41586-023-06734-w) · [Code (ARROWS)](https://github.com/njszym/ARROWS) · [Code (XRD)](https://github.com/njszym/XRD-AutoAnalyzer)<br>
  Nathan J. Szymanski et al. · University of California, Berkeley; Lawrence Berkeley National Laboratory; Google DeepMind
- <a id="coscientist"></a>**Autonomous chemical research with large language models** · *[Nature 2023](https://www.nature.com/articles/s41586-023-06792-0)* · [Paper](https://www.nature.com/articles/s41586-023-06792-0) · [Code](https://github.com/gomesgroup/coscientist)<br>
  Daniil A. Boiko, Robert MacKnight, Ben Kline, Gabe Gomes · Carnegie Mellon University; Emerald Cloud Lab

[↑ Contents](#contents)

<a id="open_ended"></a>

## 🌱 Open-Ended Discovery

*How can agents expand the scope of discovery?*

### 2026

- <a id="paper-655737c5db5ee3dd"></a>**ADAPT for Science: A Multi-Agent System for Self-Evolving Scientific Optimization** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.30851)* · [Paper](https://arxiv.org/abs/2610.30851)<br>
  Zhaoran Feng et al. · National Laboratory of Solid State Microstructures, School of Physics and, Collaborative Innovation Center of Advanced Microstructures,, Nanjing University; Shanghai Innovation Institute; College of Computer Science and Artificial Intelligence,, Fudan University; +2 institutions
- <a id="paper-f351b48e981eb372"></a>**AdaRSI: On-Demand Recursive Self-Improvement for Embodied Agents** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.20474)* · [Paper](https://arxiv.org/abs/2610.20474)<br>
  Peidong Wang et al. · Northeastern University; AgiBot; University of Chinese Academy of Sciences
- <a id="paper-ee533641ab5c7b8f"></a>**AutoEnvScaling: Automating the Data Flywheel with Terminal Agents** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.14163)* · [Paper](https://arxiv.org/abs/2610.14163) · [Project](https://auto-env-scaling.github.io/) · [Code](https://github.com/MSR-Orchard/AutoEnvScaling)<br>
  Simon Yu et al. · Northeastern University; Microsoft; Stanford University; +2 institutions
- <a id="paper-0e0b59c299f9b99b"></a>**Build, Don't Play: Self-Improving LLM Research Agents Develop a Hearthstone Battlegrounds AI That Rivals Top Players** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.33845)* · [Paper](https://arxiv.org/abs/2610.33845) · [Code](https://github.com/MCG-NJU/AutoTavern)<br>
  Changlian Ma, Limin Wang · Nanjing University; Shanghai AI Laboratory
- <a id="paper-025c299892959576"></a>**CoEvo-RSI: When Harnesses Evolve, Which Models Should Follow?** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.25078)* · [Paper](https://arxiv.org/abs/2610.25078) · [Code](https://github.com/SuJQ0722/CoEvo-RSI) · [HF Model](https://huggingface.co/nullptr04/CoEvo-RSI-homebench)<br>
  Jiaqi Su et al. · National University of Singapore; Agency for Science, Technology and Research (A*STAR); SenseTime Group Inc.
- <a id="paper-3063513fb1da8114"></a>**CollabFlow: Recursive Self-Improvement of Agent Collaboration** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2609.38662)* · [Paper](https://arxiv.org/abs/2609.38662)<br>
  Xiao Huang et al. · Shanghai Jiao Tong University; The Chinese University of Hong Kong, Shenzhen; Fudan University; +1 institutions
- <a id="paper-4e39463f1abc150d"></a>**Component-Aware Feedback for Self-Evolving Programs** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2609.38639)* · [Paper](https://arxiv.org/abs/2609.38639)<br>
  Ethan Lin, Jinming Nian, Yi Fang · Santa Clara University
- <a id="a03"></a>**Darwin Gödel Machine: Open-Ended Evolution of Self-Improving Agents** · *[ICLR 2026](https://proceedings.iclr.cc/paper_files/paper/2026/hash/aa5f5e6eb6f613ec412f1d948dfa21a5-Abstract-Conference.html)* · [Paper](https://arxiv.org/html/2505.22954v1) · [Code](https://github.com/jennyzzt/dgm) · [Blog](https://sakana.ai/dgm/)<br>
  Jenny Zhang et al. · University of British Columbia; Vector Institute; Sakana AI; +1 institutions
- <a id="paper-b53f2f037fbc3af0"></a>**Data-Centric Recursive Self-Improvement for Navigation via Policy-Synchronized Language-Action Dual Bootstrapping** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.15782)* · [Paper](https://arxiv.org/abs/2610.15782) · [Code](https://github.com/OpenGVLab/RSI-Nav)<br>
  Songze Li et al. · Fudan University; Shanghai AI Laboratory; Harbin Institute of Technology; +6 institutions
- <a id="discoveryrsi"></a>**DiscoveryRSI: Recursively Learning to Discover Valuable Hypotheses** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.23839)* · [Paper](https://arxiv.org/abs/2610.23839) · [Code](https://github.com/Gen-Verse/DiscoveryRSI) · [HF Model](https://huggingface.co/Gen-Verse/DiscoveryRSI-27B) · [HF Dataset](https://huggingface.co/datasets/Gen-Verse/DiscoveryRSI-Hypothesis-Task-Examples) · [HF Collection](https://huggingface.co/collections/Gen-Verse/discoveryrsi) · [Demo](https://foundry-arena.rsi-arena.workers.dev/arena)<br>
  Jianyuan Zhong et al. · PhAI Labs; The Chinese University of Hong Kong; University of Michigan; +13 institutions
- <a id="paper-7f1896e8c90c3d01"></a>**DoAtlas-2: A Foundation for Self-Evolving Causal Biomedical Discovery** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2609.35107)* · [Paper](https://arxiv.org/abs/2609.35107) · [Project](https://imranrazzak.github.io/model-doatlas-2.html)<br>
  Yulong Li et al. · DoAtlas Team · MedOmni; MBZUAI
- <a id="paper-e10b8d841147a1b9"></a>**Drafting Agents, Not Just Tokens: Speculative Recursive Self-Improvement for Agentic Systems** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.16491)* · [Paper](https://arxiv.org/abs/2610.16491) · [Code](https://github.com/SpecRSI-GPR/SpecRSI)<br>
  Xin Xu et al. · Tencent AMS; Xiaohongshu; University of Chinese Academy of Sciences; +3 institutions
- <a id="paper-566558a1ce42da4c"></a>**EAU: Environment-Agent-User Co-evolution for Training User-Centric Agents** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.16523)* · [Paper](https://arxiv.org/abs/2610.16523) · [Code](https://github.com/StringNLPLAB/meta-agent)<br>
  Min Cai et al. · University of Alberta; National University of Singapore; Kuaishou Technology; +2 institutions
- <a id="paper-4f543aaf09b8e37b"></a>**ECG-RSI: Recursive Self-Improvement through Targeted Electrocardiogram Waveform Evolution** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.17718)* · [Paper](https://arxiv.org/abs/2610.17718) · [Project](https://pork-pay.github.io/ECG-RSI/) · [Project](https://github.com/pork-pay/ECG-RSI)<br>
  Xiaoliang Wang et al. · Zhejiang University; Ant Group; Shanghai Artificial Intelligence Laboratory; +1 institutions
- <a id="paper-ef48cb890dde5a10"></a>**EvoAlloc: A Self-Evolving Resource Allocation Agent for Efficient Program Evolution** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.12086)* · [Paper](https://arxiv.org/abs/2610.12086)<br>
  Yanning Dai et al. · Center of Excellence for Generative AI, King Abdullah University of Science and Technology (KAUST), Thuwal, Saudi Arabia; Sakana AI, Tokyo, Japan
- <a id="paper-636608d9746bd1e3"></a>**EvoAudio: Recursive Self-Improvement for Audio Understanding** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2609.27389)* · [Paper](https://arxiv.org/abs/2609.27389) · [Project](https://jensenyx.github.io/EvoAudio.github.io/)<br>
  Yuxiang Wang et al. · The Chinese University of Hong Kong, Shenzhen; Tsinghua University; Tencent Hunyuan; +1 institutions
- <a id="paper-d6749ecc14796b6e"></a>**Evolving Agent Interfaces** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.28601)* · [Paper](https://arxiv.org/abs/2610.28601) · [Code](https://github.com/simular-ai/Agent-S)<br>
  Saaket Agashe et al. · University of California, Santa Barbara; Cornell University; Carnegie Mellon University; +1 institutions
- <a id="paper-cc8cdd0ee81ef8b9"></a>**Evolving with Open Worlds: Towards Recursive Self-Improvement for Future Forecasting** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.29784)* · [Paper](https://arxiv.org/abs/2610.29784) · [Project](https://github.com/RUCAIBox/DeepEvolve)<br>
  Zhipeng Chen et al. · Gaoling School of Artificial Intelligence, Renmin University of China; IQuest Research; Nanyang Technological University
- <a id="paper-2d3763112aef5022"></a>**ExpEvolve: Structuring and Reusing Experience for Open-Ended Discovery** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.29303)* · [Paper](https://arxiv.org/abs/2610.29303)<br>
  Yongqiang Chen et al. · MBZUAI; Carnegie Mellon University; TMLR Group, Hong Kong Baptist University; +2 institutions
- <a id="paper-d57ea0fb0cf5ef2f"></a>**GuideEvolve: Self-Evolving Agent Framework with Expert Guidance and 3Ts Mechanisms** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.30017)* · [Paper](https://arxiv.org/abs/2610.30017)<br>
  Meihong Jia, Yasemin Timar, Jonathan Taws · Amazon; Amazon Web Services
- <a id="paper-7c54f1424d2cec7d"></a>**Gödel Forest: Balancing Search Depth and Breadth for Data-Centric Recursive Self-Improvement** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2609.36675)* · [Paper](https://arxiv.org/abs/2609.36675) · [Code](https://github.com/evolvent-ai/Godel-Forest) · [Project](https://rsibench.co/)<br>
  Ziqi Zhao et al. · Evolvent AI; The Hong Kong Polytechnic University; National University of Singapore; +1 institutions
- <a id="paper-2870028c1b518506"></a>**HarnessPro: Recursive Harness Self-Improvement with Pareto Optimization for Performance-Cost Trade-offs** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.26770)* · [Paper](https://arxiv.org/abs/2610.26770) · [Code](https://github.com/pzs19/HarnessPro)<br>
  Zhuoshi Pan et al. · Tsinghua University; Z.AI Co., Ltd.; Shanghai Jiao Tong University; +2 institutions
- <a id="h05"></a>**HELIX: Model-Harness Co-evolution for Recursive Self-Improvement** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2608.13951)* · [Paper](https://arxiv.org/abs/2608.13951) · [Code](https://github.com/HKUDS/HELIX)<br>
  Tianyu Fan, Chao Huang · The University of Hong Kong
- <a id="paper-ca73ad6631f866e6"></a>**HERA: Harness-Environment Co-Evolution for Reliable Agentic Abstention** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.06563)* · [Paper](https://arxiv.org/abs/2610.06563) · [Project](https://hera-bench.github.io/) · [Code](https://github.com/lhannnn/HERA-Bench)<br>
  Han Luo et al. · University of Washington; University of Leeds; Carnegie Mellon University; +2 institutions
- <a id="paper-a297723d20b70cb4"></a>**Heterogeneous Agentic Coevolution** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.16078)* · [Paper](https://arxiv.org/abs/2610.16078) · [Project](https://wenqian-ye.github.io/hace/)<br>
  Wenqian Ye et al. · Meta AI; University of Virginia
- <a id="hyperagents"></a>**Hyperagents** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2603.19461)* · [Paper](https://arxiv.org/abs/2603.19461) · [Code](https://github.com/facebookresearch/Hyperagents)<br>
  Jenny Zhang et al. · University of British Columbia; Vector Institute; University of Edinburgh; +4 institutions
- <a id="paper-be6027ef734ec5cb"></a>**Intrinsic Goals for Autonomous Agents: Hierarchical Exploration Captures Future Volitional Action in Drosophila** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.34638)* · [Paper](https://arxiv.org/abs/2610.34638) · [Project](https://neuroagents-lab.github.io/autonomous_drosophila/)<br>
  Declan Kutscher et al. · University of Maryland, College Park; Carnegie Mellon University
- <a id="paper-a721352a4172d790"></a>**Kernel Autoresearch for Open-Ended Model Discovery** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.10394)* · [Paper](https://arxiv.org/abs/2610.10394) · [Code](https://github.com/richardcsuwandi/kernaut) · [Project](https://richardcsuwandi.github.io/kernaut/)<br>
  Richard Cornelius Suwandi, Feng Yin, Kevin Murphy · CUHK-Shenzhen; University of British Columbia
- <a id="paper-02f41708e47efed6"></a>**Large Language Models Meet Bayesian Optimization: Towards Self-evolving Wireless Digital Twins** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.31192)* · [Paper](https://arxiv.org/abs/2610.31192)<br>
  Yingzhuo Sun et al. · KTH Royal Institute of Technology; Data Machine Elite; ˙Izmir Institute of Technology
- <a id="paper-e9f27e351be4ca7e"></a>**MedRSI: Recursive Self-Improvement for Medical Agents via Clinically Aligned Self-Evolution** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2609.24838)* · [Paper](https://arxiv.org/abs/2609.24838) · [Code](https://github.com/ImprintLab/MedRSI)<br>
  Junde Wu et al. · University of Oxford; Stanford University
- <a id="paper-034319a912d1c23e"></a>**MedZERO: Self-Evolving Agents for Open-Ended Medical Reasoning Through Controlled Knowledge Accumulation** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.08327)* · [Paper](https://arxiv.org/abs/2610.08327) · [Code](https://github.com/IcecreamArtist/MedZERO)<br>
  Xilin Dang et al. · The Chinese University of Hong Kong; Zhongshan Hospital; Fudan University; +3 institutions
- <a id="paper-bc10433cad9d513d"></a>**MetaShare: Failure-Aware Collective Self-Improvement for Open-Ended Agents** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.21887)* · [Paper](https://arxiv.org/abs/2610.21887)<br>
  Vishal Bhutani, Prasang Gupta, Sumanth Chundru, Kevin Paul · PricewaterhouseCoopers (PwC)
- <a id="paper-196c956b69f1a6ef"></a>**On-Policy Self-Training: Data-Free Self-Improvement in Large Language Models** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.32770)* · [Paper](https://arxiv.org/abs/2610.32770)<br>
  Leon Sick et al. · Google; Ulm University
- <a id="paper-685e075936202295"></a>**Organon : From Evolutionary Search to Recursive Self-Improving Agents for Scientific Discovery** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.33046)* · [Paper](https://arxiv.org/abs/2610.33046) · [Code](https://github.com/cheikh025/Organon)<br>
  Cheikh Ahmed et al. · Huawei Technologies Canada; Huawei Technologies
- <a id="paper-d94a846ad662e4ea"></a>**Predict Before You Modify: Learning Improvement Dynamics for Self-Evolving Agents** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.13991)* · [Paper](https://arxiv.org/abs/2610.13991)<br>
  Zixuan Xie, Chang Xu, Yuhua Jiang, Li Zhao · University of Virginia; Microsoft Research; Tsinghua University
- <a id="paper-8986b52e03245503"></a>**QD-Rec: Open-Ended Evolution of Recommendations via Quality-Diversity** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.23470)* · [Paper](https://arxiv.org/abs/2610.23470) · [Code](https://github.com/SakanaAI/QD-Rec) · [Project](https://pub.sakana.ai/qd-rec/)<br>
  Takashi Ishida, Taro Makino, Issa Sugiura · Sakana AI
- <a id="paper-645d1404d83ffc87"></a>**R$^2$ Flow: Recursive Self-Improvement via Recursive Skill Evolution** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2609.33867)* · [Paper](https://arxiv.org/abs/2609.33867) · [Code](https://github.com/beita6969/r2flow) · [Dataset](https://huggingface.co/datasets/beita6969/R2Flow-Dataset)<br>
  Mingda Zhang et al. · The Chinese University of Hong Kong, Shenzhen; Fudan University; University of Illinois at Urbana-Champaign; +2 institutions
- <a id="paper-e0e322c3332399a4"></a>**R$^2$Orch: Recursive Self-Improvement for Agent Orchestration via Self-Play within a Skill-Internalization Loop** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.22740)* · [Paper](https://arxiv.org/abs/2610.22740) · [Code](https://github.com/beita6969/R2Orch)<br>
  Mingda Zhang et al. · The Chinese University of Hong Kong, Shenzhen; Fudan University; University of Illinois Urbana-Champaign; +2 institutions
- <a id="r-zero"></a>**R-Zero: Self-Evolving Reasoning LLM from Zero Data** · *[ICLR 2026](https://openreview.net/pdf?id=96apU6YzSO)* · [Paper](https://arxiv.org/abs/2508.05004) · [Code](https://github.com/Chengsong-Huang/R-Zero) · [Project](https://chengsong-huang.github.io/R-Zero.github.io/)<br>
  Chengsong Huang et al. · Tencent AI Seattle Lab; Washington University in St. Louis; University of Maryland, College Park; +1 institutions
- <a id="paper-f330de6f12df20ba"></a>**Recursive self-improvement of AI research agents** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2609.26457)* · [Paper](https://arxiv.org/abs/2609.26457) · [Project](https://www.weco.ai/blog/first-evidence-of-recursive-self-improvement)<br>
  Dhruv Srikanth et al. · Weco AI
- <a id="paper-2017be142f7eddde"></a>**Recursive Self-Improvement on a Budget: Scoring Code Edits Before They Run** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.29121)* · [Paper](https://arxiv.org/abs/2610.29121)<br>
  Erfan Darzi, Sree Bhargavi Balija, Sheng He · Harvard University; Massachusetts Institute of Technology; UC San Diego
- <a id="paper-7f79a91ca4549965"></a>**Recursive Self-Improvement through Multi-Agent Self-Supervision** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.12176)* · [Paper](https://arxiv.org/abs/2610.12176) · [Code](https://github.com/SakanaAI/mass) · [Project](https://pub.sakana.ai/mass/)<br>
  Hyunin Lee et al. · UC Berkeley; Sakana AI
- <a id="paper-dfc771d2f376c834"></a>**ReSI: Recursive Safety Improvement toward Resistant and Resilient AI** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.12233)* · [Paper](https://arxiv.org/abs/2610.12233) · [Code](https://github.com/AI45Lab/ReSI) · [HF Model](https://huggingface.co/AI45Research/ReSI-Qwen3.6-27B) · [HF Model](https://huggingface.co/AI45Research/ReSI-Ministral-3-14B-Reasoning) · [HF Model](https://huggingface.co/AI45Research/ReSI-DeepSeek-V4-Flash) · [HF Model](https://huggingface.co/AI45Research/ReSI-Safin-1-35B-A3B)<br>
  Jingnan Zheng et al. · Shanghai AI Laboratory; National University of Singapore; Shanghai Jiao Tong University; +2 institutions
- <a id="paper-3b70b4be961ade0f"></a>**ReVision3D: Attribution-Guided Recursive Self-Improvement for 3D Medical Perception** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2609.32984)* · [Paper](https://arxiv.org/abs/2609.32984) · [Project](https://leeh43.github.io/ReVision3D/)<br>
  Ho Hin Lee et al. · Vanderbilt University; University of California, Santa Cruz; University of California, San Francisco; +2 institutions
- <a id="paper-a78bf587c937584f"></a>**RRSI: Regularized Recursive Self-Improvement of Agent Harnesses** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2609.24972)* · [Paper](https://arxiv.org/abs/2609.24972) · [Code](https://github.com/google-research/rrsi) · [Project](https://regularized-rsi.com/)<br>
  Peng Xia et al. · Google Cloud AI Research; UNC-Chapel Hill; Stanford University; +1 institutions
- <a id="paper-0a8f2fad6cda449e"></a>**RSI-Opt: Recursive Self-Improvement Optimizer Agents For Model Training** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.32026)* · [Paper](https://arxiv.org/abs/2610.32026)<br>
  Binghang Lu, Yige Sun, Guang Lin · Purdue University; Independent Researcher
- <a id="paper-93034516b473593c"></a>**RSIFlow: Adaptive Self-Improvement Workflows with an Evolving Meta-Agent** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.21791)* · [Paper](https://arxiv.org/abs/2610.21791) · [Code](https://github.com/1HUAN1/RSI-Flow)<br>
  Huan Zhang et al. · Beijing Advanced Innovation Center for Future Blockchain and Privacy Computing; Beihang University; Tsinghua University; +1 institutions
- <a id="paper-3c4b48d4f4217451"></a>**RSIGame: Autonomous Agentic Game Development with Recursive Self-improvement** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2609.39045)* · [Paper](https://arxiv.org/abs/2609.39045) · [Code](https://github.com/WenyiWU0111/RSIGame) · [Project](https://huggingface.co/spaces/RSIGame/rsigame-page) · [Dataset](https://huggingface.co/datasets/RSIGame/RSIGame-TableArtifacts)<br>
  Wenyi Wu et al. · University of California San Diego; ByteDance Inc.; Carnegie Mellon University
- <a id="paper-649cc9ecec2ec3d8"></a>**RSIV-Harness: A Recursive Self-Improvement Harness Framework for Open-Domain Conversational Text-to-Visualization** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.35316)* · [Paper](https://arxiv.org/abs/2610.35316)<br>
  Jiawei Lu et al. · The Hong Kong Polytechnic University; The Hong Kong University of Science and Technology
- <a id="paper-26bdab7224d77ff2"></a>**SCOPE: Compiling Natural-Language Policies into Neurosymbolic Predicate Programs** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.31062)* · [Paper](https://arxiv.org/abs/2610.31062) · [Dataset](https://huggingface.co/datasets/Plurai/SCOPE)<br>
  Arnon Mazza, Elad Levi · Plurai
- <a id="paper-54910a6ae6785da1"></a>**Second-Order Problem Solving for Recursive Self-Improvement in Formal Verification** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.05701)* · [Paper](https://arxiv.org/abs/2610.05701)<br>
  Yuxuan Jiang, Aditya Vempaty, Ashish Jagmohan · University of Maryland, Baltimore County; Emergence AI
- <a id="paper-589ac49b04a690ec"></a>**Selection Is Not Learning: Choosing Model Futures** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.22029)* · [Paper](https://arxiv.org/abs/2610.22029)<br>
  Haoyi Yang, Kshitij Mishra, Nils Lukas, Salem Lahlou · Mohamed bin Zayed University of Artificial Intelligence
- <a id="self-hpo"></a>**Self-Evolving Coding Agents via Harness-Policy Optimization** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.22791)* · [Paper](https://arxiv.org/abs/2610.22791) · [Code](https://github.com/MSR-Orchard/Self-HPO) · [HF Model (Self-HPO)](https://huggingface.co/self-hpo/Self-HPO-Qwen3.5-35B-A3B) · [HF Model (HPO)](https://huggingface.co/self-hpo/HPO-Qwen3.5-35B-A3B)<br>
  Zhepei Wei et al. · Microsoft Research; University of Virginia; Carnegie Mellon University
- <a id="paper-2511dda3bf837c9e"></a>**Self-Evolving Coding Rules for AI Coding Agents** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.00650)* · [Paper](https://arxiv.org/abs/2610.00650)<br>
  Zhengyuan Jiang et al. · Duke University
- <a id="paper-c453f738aea7d5a3"></a>**Self-Evolving Harness on Multiple Tasks with the Agent as Its Own Optimizer** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2609.38372)* · [Paper](https://arxiv.org/abs/2609.38372)<br>
  Qiankai Xu · Nanjing University
- <a id="paper-2f2697994fe0d1fe"></a>**Self-Evolving Visual Agent via Margin Reward** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.15084)* · [Paper](https://arxiv.org/abs/2610.15084) · [Code](https://github.com/YWenxi/marvo)<br>
  Wenxi Yang et al. · UCAS; Microsoft Research Asia; Beihang University
- <a id="paper-792ae4cee70ec7f2"></a>**SimEX: Simulation-Integrated Robotics AutoResearch** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2609.38982)* · [Paper](https://arxiv.org/abs/2609.38982) · [Project](https://robo-simex.github.io/)<br>
  Jiaheng Hu et al. · Amazon FAR (Frontier AI & Robotics); The University of Texas at Austin; Carnegie Mellon University
- <a id="paper-9cd4a9cd56f8d9b1"></a>**Skill^{infty}: Recursive Self-Improvement for Agent Skill Optimization** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.35434)* · [Paper](https://arxiv.org/abs/2610.35434) · [Code](https://github.com/taowangcheng/Skill-Infinity)<br>
  Wangcheng Tao, Zhanglu Yan, Han Wu, Weng-Fai Wong · National University of Singapore; City University of Hong Kong
- <a id="swarmrsi"></a>**SwarmRSI: Recursive Self-Improvement through Evolving Scientific Agent Swarm** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.20431)* · [Paper](https://arxiv.org/abs/2610.20431)<br>
  Qianru Meng et al. · Huawei Technologies Co., Ltd.; Leiden University; University of Groningen
- <a id="paper-bb5599a8f4dfd40c"></a>**Towards Robust Prehensile Manipulation in Open-Ended Environments** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.06376)* · [Paper](https://arxiv.org/abs/2610.06376)<br>
  Mathilde Kappel et al. · Sorbonne Universit´e; CNRS; Institut des Syst`emes Intelligents et de Robotique (ISIR)
- <a id="paper-ee825def7bc9147c"></a>**VERSE: Verified Self-Evolving Optimizer for Agent Harnesses** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.02616)* · [Paper](https://arxiv.org/abs/2610.02616) · [Code](https://github.com/wzekai/VERSE)<br>
  Zekai Wang et al. · MIT; Amazon
- <a id="paper-029deec292a7ccda"></a>**Video-RSI: Recursive Self-Improvement of Video Understanding Agents via Harness Evolution** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2609.37950)* · [Paper](https://arxiv.org/abs/2609.37950) · [Code](https://github.com/bingjunluo/Video-RSI) · [Project](https://bingjunluo.github.io/Video-RSI/)<br>
  Bingjun Luo, Jialin Guo, Siqi Li · Tsinghua University; Harbin Engineering University
- <a id="paper-1e6847de2c470a1b"></a>**VideoHarness-SRSI: Structured Recursive Self-Improvement for Video Understanding Harness** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.19424)* · [Paper](https://arxiv.org/abs/2610.19424) · [Project](https://zihaolinqz.github.io/VHarness-SRSI/)<br>
  Zihao Lin et al. · University of California, Davis; Duke University; University of Illinois at Urbana-Champaign; +3 institutions
- <a id="paper-8afedb8bc87bfd13"></a>**What Stops Recursive Self-Improvement in Robotics? Lessons from 123 Rounds of Agentic Skill Discovery** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2609.31760)* · [Paper](https://arxiv.org/abs/2609.31760)<br>
  Wang Jiaming · National University of Singapore
- <a id="paper-76e8130f572b6405"></a>**When Is Enough Enough in Self-Evolving LLM Systems?** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.04756)* · [Paper](https://arxiv.org/abs/2610.04756)<br>
  Enoch Yin, Bin Liu, Zhengling Qi · The George Washington University; Fudan University

### 2025

- <a id="sica"></a>**A Self-Improving Coding Agent** · *[arXiv 2025 (preprint)](https://arxiv.org/abs/2504.15228)* · [Paper](https://arxiv.org/abs/2504.15228) · [Code](https://github.com/MaximeRobeyns/self_improving_coding_agent)<br>
  Maxime Robeyns, Martin Szummer, Laurence Aitchison · University of Bristol; iGent AI
- <a id="f10"></a>**Absolute Zero: Reinforced Self-play Reasoning with Zero Data** · *[NeurIPS 2025](https://proceedings.neurips.cc/paper_files/paper/2025/hash/9837dc00ff67d176373268ed48042d49-Abstract-Conference.html)* · [Paper](https://arxiv.org/abs/2505.03335) · [Code](https://github.com/LeapLabTHU/Absolute-Zero-Reasoner) · [Project](https://andrewzh112.github.io/absolute-zero-reasoner/) · [HF Model](https://huggingface.co/andrewzh/Absolute_Zero_Reasoner-Coder-7b) · [HF Collection](https://huggingface.co/collections/andrewzh/absolute-zero-reasoner-68139b2bca82afb00bc69e5b)<br>
  Andrew Zhao et al. · Tsinghua University; Beijing Institute for General Artificial Intelligence; Penn State University
- <a id="h01"></a>**Automated Design of Agentic Systems** · *[ICLR 2025](https://proceedings.iclr.cc/paper_files/paper/2025/hash/36b7acf6f6010652b3f2a433774a66fe-Abstract-Conference.html)* · [Paper](https://arxiv.org/abs/2408.08435) · [Code](https://github.com/ShengranHu/ADAS)<br>
  Shengran Hu, Cong Lu, Jeff Clune · University of British Columbia; Vector Institute; CIFAR
- <a id="asal"></a>**Automating the Search for Artificial Life with Foundation Models** · *[Artificial Life 2025](https://direct.mit.edu/artl/article/31/3/368/132866/Automating-the-Search-for-Artificial-Life-With)* · [Paper](https://arxiv.org/abs/2412.17799) · [Code](https://github.com/SakanaAI/asal) · [Project](https://asal.sakana.ai/)<br>
  Akarsh Kumar et al. · Massachusetts Institute of Technology; Sakana AI; OpenAI; +1 institutions
- <a id="omni-epic"></a>**OMNI-EPIC: Open-endedness via Models of human Notions of Interestingness with Environments Programmed in Code** · *[ICLR 2025](https://openreview.net/forum?id=Y1XkzMJpPd)* · [Paper](https://arxiv.org/abs/2405.15568) · [Code](https://github.com/maxencefaldor/omni-epic) · [Project](https://www.jennyzhangzt.com/omni-epic)<br>
  Maxence Faldor, Jenny Zhang, Antoine Cully, Jeff Clune · Imperial College London; University of British Columbia; Vector Institute; +1 institutions

### 2024

- <a id="omni"></a>**OMNI: Open-endedness via Models of human Notions of Interestingness** · *[ICLR 2024](https://www.jennyzhangzt.com/omni/)* · [Paper](https://arxiv.org/abs/2306.01711) · [Project](https://www.jennyzhangzt.com/omni/) · [Code](https://github.com/jennyzzt/omni)<br>
  Jenny Zhang, Joel Lehman, Kenneth Stanley, Jeff Clune · University of British Columbia; Vector Institute; Stochastic Labs; +2 institutions

### 2023

- <a id="voyager"></a>**Voyager: An Open-Ended Embodied Agent with Large Language Models** · *[arXiv 2023 (preprint)](https://arxiv.org/abs/2305.16291)* · [Paper](https://arxiv.org/abs/2305.16291) · [Project](https://voyager.minedojo.org) · [Code](https://github.com/MineDojo/Voyager)<br>
  Guanzhi Wang et al. · NVIDIA; California Institute of Technology; The University of Texas at Austin; +2 institutions

### 2020

- <a id="f07"></a>**Enhanced POET: Open-Ended Reinforcement Learning through Unbounded Invention of Learning Challenges and their Solutions** · *[ICML 2020](https://proceedings.mlr.press/v119/wang20l.html)* · [Paper](https://arxiv.org/abs/2003.08536) · [Code](https://github.com/uber-research/poet)<br>
  Rui Wang et al. · Uber AI Labs; OpenAI

[↑ Contents](#contents)

<a id="benchmarks"></a>

## 📊 Discovery Evaluation

*How can we measure progress in discovery?*

For environment types, physical experiment access, and training interfaces, see the [benchmark guide](docs/benchmarks.md).

### 2026

- <a id="acdb"></a>**Active Causal Discovery Benchmark: Evaluating LLM Agents Under Budgeted Interventions** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2609.31675)* · [Paper](https://arxiv.org/abs/2609.31675)<br>
  Sagar Deb, Devam Shah, Ashwanth Krishnan · QpiAI
- <a id="paper-ee2ff832ad1772a4"></a>**AdaExploreBench: Benchmarking LLM Agents for Proactive Exploration and Test-time Adaptation in Evolving Environments** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.25950)* · [Paper](https://arxiv.org/abs/2610.25950) · [Code](https://github.com/HKUST-KnowComp/AdaExploreBench) · [Dataset](https://huggingface.co/datasets/Roryaccout/AdaExploreBench) · [Project](https://hkust-knowcomp.github.io/AdaExploreBench/)<br>
  Rui Wang et al. · HKUST; HKUST(GZ); HKUST-UGAIL; +3 institutions
- <a id="paper-9fbe7130605b3a7c"></a>**AgentProofBench: Benchmarking Reusable Verifiers for Web Agents** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.34634)* · [Paper](https://arxiv.org/abs/2610.34634) · [Project](https://ethanning.github.io/AgentProofBench/) · [Code](https://github.com/EthanNing/AgentProofBench)<br>
  Jingjie Ning, Xueqi Li, Yi Lu, Yibo Kong · Carnegie Mellon University
- <a id="paper-a13bbb297eb54c7e"></a>**AgentTime: Can Agents Estimate and Control Their Own Runtime?** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.09944)* · [Paper](https://arxiv.org/abs/2610.09944) · [Code](https://github.com/michaelofengenden/agenttimebench) · [Project](https://agenttimebench.com) · [Dataset](https://huggingface.co/datasets/mofengenden/agenttime-transcripts)<br>
  Michael Ofengenden, Maksym Andriushchenko · MATS; ELLIS Institute Tübingen; Max Planck Institute for Intelligent Systems; +1 institutions
- <a id="exploration-narrowing"></a>**AI Research Agents Narrow Scientific Exploration** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2605.27905)* · [Paper](https://arxiv.org/abs/2605.27905)<br>
  Yixuan Tang, Yi Yang · The Hong Kong University of Science and Technology
- <a id="paper-1e05076c941c1de8"></a>**AlphaIdeaBench: Benchmarking Automated Research Idea Generation under Feasibility Constraints with Peer Review Alignment** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.33644)* · [Paper](https://arxiv.org/abs/2610.33644)<br>
  Shunchao Zhou et al. · Singapore Management University; The Hong Kong Polytechnic University; Hangzhou Dianzi University; +3 institutions
- <a id="paper-118197ae3e94acd7"></a>**AnyGoal: On World Model Generalization Beyond Expert Rollouts** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.26844)* · [Paper](https://arxiv.org/abs/2610.26844) · [Project](https://hazel-heejeong-nam.github.io/anygoal/) · [Code](https://github.com/galilai-group/AnyGoal)<br>
  Heejeong Nam et al. · Brown University; Cold Spring Harbor Laboratory; Mila, Universit´e de Montr´eal; +1 institutions
- <a id="paper-31ad9246f9a10e34"></a>**Are We Measuring Scientific Intelligence? Rethinking the Evaluation of AI Scientists** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.04915)* · [Paper](https://arxiv.org/abs/2610.04915)<br>
  Kate Zhang, Yuante Li · Carnegie Mellon University
- <a id="paper-016b2d7e0ace0f55"></a>**Assessing the CAD Capabilities of General-Purpose AI Models: A Case Study of GPT-6 Astra** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.24451)* · [Paper](https://arxiv.org/abs/2610.24451) · [Project](https://qiang-zou.github.io/projects/icad-eval-report/)<br>
  Qiang Zou et al. · State Key Laboratory of CAD&CG, Zhejiang University, China; Design and Manufacturing Automation Lab
- <a id="paper-9b70877a4edd3d9e"></a>**Astro2Method: Benchmarking LLMs on Machine Learning Method Selection in Astronomy** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.30282)* · [Paper](https://arxiv.org/abs/2610.30282) · [Dataset](https://huggingface.co/datasets/Xingzhongfan/Astro2Method)<br>
  Xingzhong Fan, Hangfeng He, Fatemeh Nargesian · University of Rochester
- <a id="paper-81e8d8901cbd7168"></a>**Auditing the Product, Not the Recursion: The Evaluation Evidence Behind Recursive Self-Improvement Claims** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.27610)* · [Paper](https://arxiv.org/abs/2610.27610)<br>
  Zihan Chen, Di Zhu, Lei Nico Zheng · Stevens Institute of Technology; University of Massachusetts Boston
- <a id="paper-4e611eaf34efb11a"></a>**Auto-MD-bench: Evaluating Autoresearch Agents for Real-World Medical Tasks** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.25069)* · [Paper](https://arxiv.org/abs/2610.25069) · [Code](https://github.com/Edwin0080/Auto-MD-bench) · [Dataset](https://huggingface.co/datasets/Edwin0080/Auto-MD-bench)<br>
  Shenqi Zhou et al. · National University of Singapore; Zhejiang University; Amazon
- <a id="paper-d8639c0b4eb9ace3"></a>**Automating ML for Science: Can Frontier Agents Climb Scientific Hills in the Wild?** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.28763)* · [Paper](https://arxiv.org/abs/2610.28763) · [Code](https://github.com/maszhongming/agent4sci) · [Dataset](https://huggingface.co/datasets/MingZhong/agent4sci)<br>
  Ming Zhong, Stacy Li, Nicholas Carlini, Matthew Jagielski · Anthropic Fellows Program; Anthropic
- <a id="as-bench"></a>**Autonomous Science Bench: Evaluating AI Agents for Autonomous Scientific Discovery** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.18449)* · [Paper](https://arxiv.org/abs/2610.18449) · [Code](https://github.com/Yibo-Wen/as-bench) · [Project](https://yibow.me/autonomous-science-bench)<br>
  Yibo Wen, Han Liu · Northwestern University
- <a id="paper-8564d528b4a46811"></a>**AutoPDEBench: Benchmarking LLM Auto-Research for Neural PDE Solver Design** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2609.32245)* · [Paper](https://arxiv.org/abs/2609.32245) · [Code](https://github.com/RuoyanLi2002/AutoPDEBench-Benchmarking-LLM-Auto-Research-for-Neural-PDE-Solver-Design)<br>
  Ruoyan Li, Wei Wang, Yizhou Sun · University of California, Los Angeles
- <a id="paper-30b045ab4b6612bf"></a>**AutoRSE: Evaluating LLM Agents as Recommendation Engineers for Self-Evolving Recommender Systems** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.37228)* · [Paper](https://arxiv.org/abs/2610.37228) · [Project](https://github.com/Ray-Tiann/AutoRSE)<br>
  Rui Tian et al. · University of Science and Technology of China; National University of Singapore
- <a id="paper-13a316d3fa2ce54f"></a>**Benchmarking and Enhancing Agentic Causal Discovery** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.22846)* · [Paper](https://arxiv.org/abs/2610.22846)<br>
  Pingchuan Ma, Rui Ding, Shuai Wang · Zhejiang University of Technology; Microsoft; The Hong Kong University of Science and Technology
- <a id="paper-31224f0f7655c123"></a>**Benchmarking and Error Analysis of Deep Search and Deep Research LLM Agents** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.29346)* · [Paper](https://arxiv.org/abs/2610.29346)<br>
  Zixuan Yu, Zhenheng Tang, Xiaowen Chu, Bo Han · School of Computer science and engi-
neering, Sun Yat-sen University; CSE, The Hong Kong University of Science and Technology; DSA Thrust, The Hong Kong Uni-
versity of Science and Technology (GuangZhou); +1 institutions
- <a id="paper-3abe80f754180570"></a>**Beyond Better Ideas: How Human-AI Collaboration Shapes Scientific Ideas and Human Perceptions** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.30568)* · [Paper](https://arxiv.org/abs/2610.30568)<br>
  Qian Chen et al. · The Pennsylvania State University; Harvard University; Arizona State University; +1 institutions
- <a id="paper-ec27d50c3bb0542a"></a>**Beyond Compilation: Evaluating Faithful Natural-Language-to-Lean Statement Formalization** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2606.31002)* · [Paper](https://arxiv.org/abs/2606.31002) · [Code](https://github.com/grenadeComing/beyond-compilation)<br>
  Ke Zhang et al. · University of California, Riverside; University of Arizona; University of California, San Diego
- <a id="paper-5356077cb77fa887"></a>**Beyond Endpoint Performance: Process-Level Evaluation of Self-Evolving Agents** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2609.24663)* · [Paper](https://arxiv.org/abs/2609.24663) · [Code](https://github.com/HQ-Lin/EvoPathBench)<br>
  Hongqiang Lin et al. · Zhejiang University; Alibaba Group
- <a id="paper-66cadadf2737fc2b"></a>**Beyond Watching and Searching: Benchmarking Agents for Video-centered Deep Research Reports** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.31158)* · [Paper](https://arxiv.org/abs/2610.31158) · [Code](https://github.com/Multimedia-Semantic-Analytics-Lab/OmniDR-Bench) · [Dataset](https://huggingface.co/datasets/marinero4972/OmniDR-Bench)<br>
  Jiahao Meng et al. · Peking University; Alibaba Token Hub, Alibaba Group; Independent Researcher; +1 institutions
- <a id="paper-ecf2a0572888b64b"></a>**BlenderWorld: Benchmarking Visual Agents for 3D Creation from Real-World References** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.23986)* · [Paper](https://arxiv.org/abs/2610.23986) · [Project](https://blenderworld.github.io/) · [Code](https://github.com/QwenLM/BlenderWorld) · [Dataset](https://huggingface.co/datasets/Qwen/BlenderWorld)<br>
  Xinyu Fang et al. · Zhejiang University; Alibaba Token Hub, Alibaba Group; The Chinese University of Hong Kong; +2 institutions
- <a id="paper-68fff9f7177eccc7"></a>**Can AI Scientists Change Their Minds? Prior-Evidence Conflict in Synthetic Universes** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2609.36726)* · [Paper](https://arxiv.org/abs/2609.36726)<br>
  Kargi Chauhan · University of California, Santa Cruz
- <a id="paper-9b8a04c573ff3eb4"></a>**Can LLMs Uncover Hidden Physical Laws through Free Exploration?** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.37649)* · [Paper](https://arxiv.org/abs/2610.37649) · [Project](https://zhenyangcs.github.io/LongChang-website/) · [Code](https://github.com/EnVision-Research/LongChang)<br>
  Zhen Yang, Wen Wang, Xander Xu, Ying-Cong Chen · HKUST(GZ); Alibaba Group; ZJU; +1 institutions
- <a id="c11"></a>**CausaLab: A Scalable Environment for Interactive Causal Discovery Toward AI Scientists** · *[arXiv 2026 (preprint)](https://arxiv.org/html/2605.26029v2)* · [Paper](https://arxiv.org/html/2605.26029v2)<br>
  Junlin Yang et al. · Tsinghua University; University of Illinois Urbana-Champaign; Carnegie Mellon University; +2 institutions
- <a id="paper-e461db7393754058"></a>**CellTrack-Bench: Microscopic Cell Tracking Benchmark for Vision-Language Models** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.31566)* · [Paper](https://arxiv.org/abs/2610.31566) · [Code](https://github.com/royerlab/celltrack-bench)<br>
  Ilan Theodoro, Jordão Bragantini, Loïc A. Royer · Biohub
- <a id="paper-6e3e2ae7454ba2f5"></a>**Competence-Based Evaluation of Logical Reasoning in Large Language Models** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.22894)* · [Paper](https://arxiv.org/abs/2610.22894) · [Dataset](https://huggingface.co/datasets/jizej/Competence-Based-Evaluation)<br>
  Jize Jiang, Chengxiang Zhai · University of Illinois Urbana-Champaign
- <a id="paper-721958fe0d5a8c2d"></a>**CompMat-Bench: Benchmarking AI Agents for Computational Materials Science** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.00636)* · [Paper](https://arxiv.org/abs/2610.00636) · [Code](https://github.com/cz2014/CompMat-Bench)<br>
  Chenmu Zhang et al. · Rice University
- <a id="paper-c643418cbbaee3ee"></a>**CyberArena: Benchmarking AI Agents in Live Symmetric Attack-and-Defense Combat** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.19005)* · [Paper](https://arxiv.org/abs/2610.19005) · [Project](https://cyber-arena.ai) · [Code](https://github.com/cyber-arena-ai/cyber-arena) · [Code](https://github.com/cyber-arena-ai/octagon)<br>
  Bangya Liu et al. · 2077AI Open Source Foundation; UC Santa Cruz; UC Berkeley; +8 institutions
- <a id="paper-8b5e7afcd33dcbed"></a>**Data World: Scaling Data Environments from Scratch** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.21656)* · [Paper](https://arxiv.org/abs/2610.21656) · [Code](https://github.com/Zhanli-Li/Data-World) · [Project](https://zhanli-li.github.io/Data-World/) · [Dataset](https://huggingface.co/datasets/Zhanli-Li/DataWorld-Bench) · [Dataset](https://huggingface.co/collections/Zhanli-Li/dataworld) · [HF Model](https://huggingface.co/Zhanli-Li/DataWorld-35B-A3B)<br>
  Zhanli Li et al. · School of Artificial Intelligence; National Key Laboratory for Novel Software Technology, Nanjing University; Longcat Interaction Team, Meituan; +7 institutions
- <a id="paper-ec30270490ea6cac"></a>**DataSense-Bench: The First Step Toward an AI Scientist** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.12190)* · [Paper](https://arxiv.org/abs/2610.12190) · [Code](https://github.com/DataSense-Bench/DataSense-Bench) · [Project](https://datasense-bench.github.io/)<br>
  Yudi Zhang et al. · Eindhoven University of Technology; University of Surrey; ELLIS Institute T¨ubingen; +2 institutions
- <a id="paper-64e370b96218d353"></a>**Dating the Model: Hidden Dates in System Prompts Affect LLM Evaluation** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2609.36931)* · [Paper](https://arxiv.org/abs/2609.36931)<br>
  Mario Sanz-Guerrero, Minh Duc Bui, Manuel Mager, Katharina von der Wense · Johannes Gutenberg University Mainz; Universidad Iberoamericana; University of Colorado Boulder
- <a id="paper-50d8cd71040f538b"></a>**DecisionPivot: A Diagnostic Benchmark for Decision Models in LLM Systems** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.28522)* · [Paper](https://arxiv.org/abs/2610.28522) · [Code](https://github.com/StartLuxLabs/DecisionPivot) · [Dataset](https://huggingface.co/datasets/startlux-models/DecisionPivot)<br>
  Xialie Zhuang et al. · StartLux
- <a id="paper-d26e59a1cb2b6340"></a>**Deep Search in Real-World Web Environments** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.30181)* · [Paper](https://arxiv.org/abs/2610.30181) · [Code](https://github.com/Yu-xm/OpenDS) · [Dataset](https://huggingface.co/datasets/Yu2020/OpenDS-World)<br>
  Xiaomin Yu et al. · HKUST(GZ); FDU; UW; +11 institutions
- <a id="discern"></a>**DISCERN: Can AI Agents Work Like Scientists and Guide Discovery?** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2609.33357)* · [Paper](https://arxiv.org/abs/2609.33357) · [HF Dataset](https://huggingface.co/datasets/discern-bench-anon/discern-benchmark)<br>
  Nan Huang et al. · University of California San Diego
- <a id="paper-9b37a0eba72ea3b0"></a>**Do AI Scientists Know What's New?** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.36511)* · [Paper](https://arxiv.org/abs/2610.36511) · [Code](https://github.com/emmatliu/claimnov)<br>
  Miri Liu, Xiayu Zhao, Encheng Xie, ChengXiang Zhai · University of Illinois, Urbana-Champaign
- <a id="paper-ab11c98f74e97bb4"></a>**Does LeWorldModel Preserve Local Action Geometry?** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.31716)* · [Paper](https://arxiv.org/abs/2610.31716)<br>
  Vasil Vasilev, Siddharth Nayak · Technological School Electronic Systems (TUES); Massachusetts Institute of Technology
- <a id="paper-e15c7d3de5e7f265"></a>**DrugTargetWorld: A Synthetic Biobank for Training and Benchmarking AI Scientists** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.09558)* · [Paper](https://arxiv.org/abs/2610.09558) · [Code](https://github.com/sammargolis/DrugTargetWorld) · [Project](https://drugtargetworld.vercel.app/) · [Dataset](https://huggingface.co/datasets/sammargolis/drugtargetworld-assets)<br>
  Samuel Margolis et al. · Stanford University; Brown University
- <a id="paper-817d0cefc6986b31"></a>**Dual Exam: Controlled Evaluation of Multimodal Agents and World Models** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.31066)* · [Paper](https://arxiv.org/abs/2610.31066)<br>
  Zhefan Rao et al. · The Hong Kong University of Science and Technology; National University of Singapore; The Hong Kong Polytechnic University; +24 institutions
- <a id="paper-105b4672ff4fd27c"></a>**EdgeKernelBench: Unified LLM-Driven Kernel Generation for Edge Backends** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.24648)* · [Paper](https://arxiv.org/abs/2610.24648) · [Project](https://pillor9.github.io/EdgeKernelBench/) · [Code](https://github.com/pillor9/EdgeKernelBench)<br>
  Yuhua Zheng et al. · Westlake University; Zhejiang University
- <a id="paper-97aa05f1d051eb67"></a>**EmbodiedCLBench: Evaluating Continual Learning for Self-Evolving Embodied Agents** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.13021)* · [Paper](https://arxiv.org/abs/2610.13021) · [Project](https://pku-value-lab.github.io/EmbodiedCLBench-homepage) · [Code](https://github.com/PKU-VaLuE-Lab/EmbodiedCLBench) · [Dataset](https://huggingface.co/datasets/PKU-VaLuE-Lab/EmbodiedCLBench)<br>
  Jie Huang et al. · School of Intelligence Science and Technology, Peking University; State Key Laboratory of General Artificial Intelligence, BIGAI, Beijing, China; University of Hong Kong
- <a id="paper-6162f96ecddc8088"></a>**EmbodiedLab: Benchmarking Embodied Agents That Act to Know** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.35385)* · [Paper](https://arxiv.org/abs/2610.35385) · [Code](https://github.com/HexaFuture/EmbodiedLab) · [Project](https://hexafuture.ai/benchmarks/embodiedlab/)<br>
  Hongcheng Gao et al. · HexaFuture Inc.; Tsinghua University; National University of Singapore; +1 institutions
- <a id="paper-1663c6679dab72c8"></a>**EvalResearchBench: Can AI Agents Build Their Own Feedback for Recursive Self-Improvement?** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.04184)* · [Paper](https://arxiv.org/abs/2610.04184) · [Project](https://mercury7353.github.io/self-evaluation-bench/) · [Code](https://github.com/Mercury7353/self-evaluation-bench)<br>
  Yaolun Zhang et al. · Oregon State University; University of California, San Diego; Pennsylvania State University; +1 institutions
- <a id="paper-2693639d7f34414f"></a>**Evaluating Agentic Capabilities Before Post-Training: An End-to-End Approach** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.19425)* · [Paper](https://arxiv.org/abs/2610.19425)<br>
  Jiarui Qin et al. · Tencent Youtu Lab; Shanghai Jiao Tong University
- <a id="paper-ff655bd3f5066c0f"></a>**EvaOmni: An Evidence-Grounded Benchmark for Audio-Visual Reasoning** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.28444)* · [Paper](https://arxiv.org/abs/2610.28444) · [Code](https://github.com/VisionXLab/EvaOmni) · [Dataset](https://huggingface.co/datasets/VisionXLab/EvaOmni-Dataset)<br>
  Xiaoxing Hu et al. · Shanghai Jiao Tong University; Shanghai Innnovation Institute; Inner Mongolia University of Technology; +7 institutions
- <a id="paper-8daca2e781dd8746"></a>**FinAutoRubric: Expert-Guided Automatic Rubric Generation for Evaluating Financial Research Agents** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2609.35744)* · [Paper](https://arxiv.org/abs/2609.35744)<br>
  Hoyoung Lee et al. · LinqAlpha; UNIST; MassMutual Life Insurance; +9 institutions
- <a id="paper-480b56b9da41924d"></a>**From Retrieval to Customer Context: Evaluating Frontier-Model Systems for Voice-of-Customer Analysis** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.09375)* · [Paper](https://arxiv.org/abs/2610.09375)<br>
  Raviraja G, Viraj Bagal, Prabhath Chellingi · Enterpret
- <a id="paper-dd2dc379979e7af0"></a>**From Scientific Observations to Mechanisms: Benchmarking Hypothesis Generation by AI Scientists** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.05197)* · [Paper](https://arxiv.org/abs/2610.05197)<br>
  Xiaxun Xie et al. · Computer Network Information Center, Chinese Academy of Sciences; National University of Singapore; Sichuan University
- <a id="paper-72af933c20feb3a7"></a>**FrontierCS 2: A Benchmark for Computer Science R&D** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.29932)* · [Paper](https://arxiv.org/abs/2610.29932) · [Code](https://github.com/FrontierCS/FrontierCS-2) · [Project](https://frontier-cs.org/)<br>
  Qiuyang Mang et al. · UC Berkeley; Princeton University; University of Waterloo; +16 institutions
- <a id="paper-7b88221edcfc1946"></a>**GameBoyWorlds: A Testbed for Self-Improvement in Embodied Video Games** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2609.32093)* · [Paper](https://arxiv.org/abs/2609.32093) · [Code](https://github.com/DhananjayAshok/GameBoyWorlds-Benchmark) · [Code](https://github.com/DhananjayAshok/GameBoyWorlds)<br>
  Dhananjay Ashok et al. · Information Sciences Institute, University of Southern California; Columbia University; University of Chicago; +2 institutions
- <a id="paper-c8f0a1e7ad6a901d"></a>**GlobeBench: Evaluating Text-Based World Model Capabilities for Scalable Environment Simulations** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.22708)* · [Paper](https://arxiv.org/abs/2610.22708) · [Code](https://github.com/patronus-ai/globebench) · [Dataset](https://huggingface.co/datasets/PatronusAI/globebench)<br>
  Nicholas Saban, Charvi Bannur, Mariya Vasileva, Darshan Deshpande · Patronus AI
- <a id="paper-f34ad45741b405ff"></a>**Harness-Delta Attribution: Dissecting Gains From Harness Evolution** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.22466)* · [Paper](https://arxiv.org/abs/2610.22466) · [Code](https://github.com/Wenwen-D/HarnessDeltaAttribution) · [Project](https://wenwen-d.github.io/blog/harness-delta-attribution/)<br>
  Wenxuan Ding et al. · Amazon; New York University
- <a id="paper-7a9367ad16e43eeb"></a>**How Do Coding-Agent Harnesses Self-Evolve? An Empirical Study of Retrospective Adaptation** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.34938)* · [Paper](https://arxiv.org/abs/2610.34938) · [Dataset](https://zenodo.org/records/23653700)<br>
  Christoph Treude, Sebastian Baltes · Singapore Management University; Heidelberg University
- <a id="paper-d3835393933ca7ee"></a>**HSPR: Recovering Software-Agent Benchmark Scores via Hierarchical Posterior Inference** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.24611)* · [Paper](https://arxiv.org/abs/2610.24611) · [Project](https://wanyichen06.github.io/HSPR/) · [Code](https://github.com/wanyichen06/HSPR)<br>
  Wanyi Chen et al. · Soochow University; Singapore Management University
- <a id="paper-8e919583fc15a7ec"></a>**Humans in Space: Can MLLMs Construct Human-Centric Spatial Understanding via Active Exocentric Exploration?** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.34149)* · [Paper](https://arxiv.org/abs/2610.34149) · [Code](https://github.com/gtc-gh/SATE-Bench)<br>
  Tianchen Guo et al. · The University of Queensland; Australian Institute for Machine Learning, Adelaide University; University of Technology Sydney; +1 institutions
- <a id="paper-69d6a9490f99edc5"></a>**InteractiveWorld: A Verifiable Human-Centric Environment for Building Better Interactive MLLM Assistants** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.33966)* · [Paper](https://arxiv.org/abs/2610.33966) · [Code](https://github.com/facebookresearch/InteractiveWorld) · [Project](https://meta-interactiveworld.github.io/) · [Dataset](https://github.com/facebookresearch/InteractiveWorld/tree/main/benchmark/tasks)<br>
  Qinsi Wang et al. · Meta; Duke University
- <a id="into-the-unknown"></a>**Into the Unknown: Benchmarking AI agents on open scientific research problems** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.19159)* · [Paper](https://arxiv.org/abs/2610.19159) · [Code](https://github.com/prometheus-eval/into-the-unknown) · [Project](https://prometheus-eval.github.io/into-the-unknown/viewer/) · [HF Dataset](https://huggingface.co/datasets/prometheus-eval/into-the-unknown)<br>
  Seungone Kim et al. · Carnegie Mellon University; University of Minnesota; Stanford University; +13 institutions
- <a id="paper-44155a8b99014187"></a>**iPrefBench: A User-Centric Benchmark for Personalized Mobile Use Agents** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.34735)* · [Paper](https://arxiv.org/abs/2610.34735)<br>
  Yuting Ning et al. · The Ohio State University; Apple
- <a id="paper-01623fe5218eb9ef"></a>**JockeyBench: Evaluating LLM Agents on Horse-Racing Decision-Making** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.19589)* · [Paper](https://arxiv.org/abs/2610.19589) · [Code](https://github.com/HKUST-KnowComp/JockeyBench)<br>
  Zhongwei Xie et al. · The Hong Kong University of Science and Technology; Tsy Capital Limited; Independent researcher; +1 institutions
- <a id="paper-c4824adae163f399"></a>**Kolab: Benchmarking Human-Agent Collaboration in Long-Horizon Workflows** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.21109)* · [Paper](https://arxiv.org/abs/2610.21109) · [Project](https://minnesotanlp.github.io/kolab/)<br>
  Shirley Anugrah Hayati et al. · University of Minnesota
- <a id="paper-2f1aa49aeba545c1"></a>**Legal Research Bench: Measuring End-to-End Reliability in Long-Horizon Legal Research Agents** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.00609)* · [Paper](https://arxiv.org/abs/2610.00609) · [Code](https://github.com/vals-ai/legal-research-bench)<br>
  Katrina Drozdov, Oliver Chen, Langston Nashold, Rayan Krishnan · Vals AI
- <a id="paper-979463277edcf993"></a>**LifeSearch: Benchmarking Deep Research Agents for Real-World Life and Productivity** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.18092)* · [Paper](https://arxiv.org/abs/2610.18092)<br>
  Yibo Wang et al. · LLM Department, Tencent
- <a id="paper-53e3f761f6a0e8c3"></a>**LiveMACE: Process-Aware Evaluation of LLM Agent Capabilities in Evolving Markets** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.09872)* · [Paper](https://arxiv.org/abs/2610.09872) · [Code](https://github.com/RaymondVoldemortFu/LiveMACE)<br>
  Jun Zhao et al. · National University of Singapore; Fudan University; The University of Sydney
- <a id="paper-d413c98db0f6141e"></a>**MMEnterprise-Bench: Evaluating Enterprise Agents over Evolving Multimodal Records** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.27911)* · [Paper](https://arxiv.org/abs/2610.27911) · [Project](https://mlvlab.github.io/MMEnterprise-Bench/) · [Code](https://github.com/mlvlab/MMEnterprise-Bench)<br>
  Seohyun Lee et al. · KAIST; Korea University
- <a id="paper-aa059e79208dfb82"></a>**MMPostTrainBench: Benchmarking Autonomous Research for Multimodal Post-Training** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.05398)* · [Paper](https://arxiv.org/abs/2610.05398) · [Code](https://github.com/sod1010/MMPostTrainBench)<br>
  Yuxin Liu et al. · University of Science and Technology of China; Alibaba Token Hub, Alibaba Group; University of the Chinese Academy of Sciences; +2 institutions
- <a id="d03"></a>**NewtonBench: Benchmarking Generalizable Scientific Law Discovery in LLM Agents** · *[ICLR 2026](https://proceedings.iclr.cc/paper_files/paper/2026/hash/a0e1c2c40fc245b5fe7251ea33fbb045-Abstract-Conference.html)* · [Paper](https://arxiv.org/abs/2510.07172) · [Code](https://github.com/HKUST-KnowComp/NewtonBench)<br>
  Tianshi Zheng et al. · HKUST; NVIDIA
- <a id="paper-7387918ad74d1502"></a>**Novel or Not? PatEx-Gym: Agentic Prior-Art Search for Novelty Assessment in Patent Examination** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.33503)* · [Paper](https://arxiv.org/abs/2610.33503) · [Code](https://github.com/AIforIP/PatEx-Gym) · [Dataset](https://github.com/AIforIP/PatEx-Gym/tree/main/bench)<br>
  Qiyao Wang et al. · Shenzhen Institute of Advanced Technology, Chinese Academy of Sciences; University of Chinese Academy of Sciences; Dalian University of Technology; +1 institutions
- <a id="paper-12a4904af7aa0825"></a>**On Open-Ended Information Seeking for Information Elicitation Agents** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.07509)* · [Paper](https://arxiv.org/abs/2610.07509) · [Code](https://github.com/infosenselab/open-elicitation) · [Dataset](https://huggingface.co/datasets/infosense/open-elicitation-trajectories)<br>
  Victor De Lima, Grace Hui Yang · Georgetown University
- <a id="paper-03406ae2f3bae7d2"></a>**On the Fragility of Tasks under Composition: Implicit Budgeting in Language Models** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.27190)* · [Paper](https://arxiv.org/abs/2610.27190) · [Project](https://chenpanli.github.io/fragility) · [Code](https://github.com/chenpanli/fragility)<br>
  Chenpan Li et al. · TU Munich; MIT CSAIL
- <a id="paper-5a53c3bdb60bfc08"></a>**OpenProblemBench: Benchmarking AI on Open Problems in the Foundational Theoretical Sciences** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.11118)* · [Paper](https://arxiv.org/abs/2610.11118)<br>
  Zhiyi Li et al. · Department of Modern Physics, University of Science and Technology of China, Hefei, Anhui 230026, China; CAS Key Laboratory of Theoretical Physics, Institute of Theoretical Physics, Chinese Academy of Sciences, Beijing 100190, China; Hefei National Laboratory, University of Science and Technology of China, Hefei 230088, China; +3 institutions
- <a id="paper-bc9b70a35a8d90a3"></a>**OpenSocialJax: Evaluating Social Adaptation in Sequential Social Dilemmas with Open-Ended Environmental Dynamics** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.13710)* · [Paper](https://arxiv.org/abs/2610.13710) · [Code](https://github.com/cooperativex/OpenSocialJax)<br>
  Zihao Guo, Meng Fang, Joel Z. Leibo, Yali Du · King’s College London; University of Liverpool; The Alan Turing Institute; +1 institutions
- <a id="paper-5d861400b2f29a95"></a>**OR-License: Evaluating LLM Agents as Real-World Operations Research Practitioners** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.24087)* · [Paper](https://arxiv.org/abs/2610.24087) · [Code](https://github.com/NineAbyss/OR-License) · [Dataset](https://huggingface.co/datasets/OR-License/OR-License)<br>
  Peisong Wang et al. · HKUST-GZ; HKU; Qingzhi Optimization (Jinan) Information Technology Co., Ltd.; +6 institutions
- <a id="paper-f99b7ad173e24ad2"></a>**PaperScorer: How Predictable Is Paper Acceptance?** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.31791)* · [Paper](https://arxiv.org/abs/2610.31791) · [Project](https://sachinkonan.github.io/PaperScorer.html) · [Code](https://github.com/zlab-princeton/PaperScorer)<br>
  Sachin Konan, Jonathan Liu, Zhuang Liu · Princeton University
- <a id="paper-0d36244bb44988af"></a>**Pre-Registered Genesis Accounting for Recursive Self-Improvement: First Audited Operator-Genesis Events in a Physics-Discovery Runtime** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.14843)* · [Paper](https://arxiv.org/abs/2610.14843)<br>
  Wenbin Mao, Pei Zou · HoomanBio AI Lab, Huaman Biotechnology (Beijing) Co., Ltd.
- <a id="paper-476e87c36ff94c5c"></a>**Predictive Credit: Measuring What Scientific Explanations Add to Experimental Forecasts** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.00314)* · [Paper](https://arxiv.org/abs/2610.00314)<br>
  Jingjie Ning, Xueqi Li, Yibo Kong, Dongting Li · Carnegie Mellon University; Tsinghua University
- <a id="paper-dcda595d5edb15af"></a>**PVBench: Quantifying Physical Plausibility in Video Generation with Object-Level Physical Measurements** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.26711)* · [Paper](https://arxiv.org/abs/2610.26711) · [Code](https://github.com/KSZG-11/PVBench) · [Project](https://kszg-11.github.io/PVBench-Website/)<br>
  Kaiwei Chen et al. · APRIL Lab, Zhejiang University; Huazhong University of Science and Technology; Tencent Youtu Lab
- <a id="paper-045c2b8bd847ae46"></a>**Quant-Arena: Benchmarking LLM Agents for Quantitative Trading Research** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.30113)* · [Paper](https://arxiv.org/abs/2610.30113) · [Project](https://lab.einsia.ai/quant-arena/)<br>
  Houde Qian et al. · Navers Lab; Einsia.AI
- <a id="paper-6737b9769e0ac469"></a>**Quantifying Claim Smoothing by LLM Research Agents** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.35793)* · [Paper](https://arxiv.org/abs/2610.35793) · [Code](https://github.com/tiasa2/SmoothScore)<br>
  Tiasa Singha Roy, Manya Wadhwa, Greg Durrett · New York University
- <a id="paper-d4e79e43099df1b8"></a>**ResearchFlow-Eval: Tracing the Execution Gap in End-to-End Multi-Claim Autoresearch** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.18088)* · [Paper](https://arxiv.org/abs/2610.18088) · [Code](https://github.com/Jp-17/ResearchFlow-Eval)<br>
  Peng Jiang, Dongyang Li, Quanying Liu, Xiaoxuan Jia · Center for Life Sciences and Artificial Intelligence, School of Life Sciences, Tsinghua University, Beijing, China; IDG/McGovern Institute for Brain Research, Tsinghua University, Beijing, China; Tsinghua-Peking Center for Life Sciences, Tsinghua University, Beijing, China; +2 institutions
- <a id="paper-ee84b521258fee34"></a>**Retrieval Augmented Generation Compositionality** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.29722)* · [Paper](https://arxiv.org/abs/2610.29722) · [Code](https://github.com/dolev31/lasagna) · [Project](https://dolev31.github.io/lasagna/)<br>
  Ido Levy, Segev Shlomov, Leshem Choshen · IBM; Weizmann Institute of Science
- <a id="paper-3e1c96441442a7d4"></a>**Reward Hacking Challenges Oversight of Autonomous Research Agents** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2609.28614)* · [Paper](https://arxiv.org/abs/2609.28614)<br>
  Yue Huang et al. · Bake AI; University of Notre Dame; LMU Munich; +7 institutions
- <a id="paper-35b9a7f119c042ee"></a>**RoboJudge: Multimodal Language Models as Judges for Embodied Video Generation** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.27782)* · [Paper](https://arxiv.org/abs/2610.27782) · [Project](https://spherelab.ai/RoboJudge/) · [Code](https://github.com/Sphere-AI-Lab/RoboJudge)<br>
  Siyuan Ma et al. · The Chinese University of Hong Kong; Westlake University; Northeastern University; +3 institutions
- <a id="paper-7f92942419dc62bc"></a>**RSI Arena: Towards Recursive Self-Improvement with Human Feedback** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.33624)* · [Paper](https://arxiv.org/abs/2610.33624) · [Project](https://rsiarena.org/) · [HF Model](https://huggingface.co/RSIArena/RSIAgent-Aspen-Stage1) · [HF Model](https://huggingface.co/RSIArena/RSIAgent-Aspen-Stage2)<br>
  Yue Huang et al. · Bake AI; University of Notre Dame; University of California, Los Angeles; +8 institutions
- <a id="paper-b92b08173531b188"></a>**RSI-Forge: From Research Papers to Environments for Recursive Self-Improvement** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.09426)* · [Paper](https://arxiv.org/abs/2610.09426)<br>
  Renxiong Wang et al. · Scale AI; University of California, Santa Cruz; University of North Carolina at Chapel Hill
- <a id="paper-e37e7605cf26a455"></a>**RubricAtlas: Mining Type-Level Rubrics from Expert Reports to Evaluate Deep Research Agents** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.36878)* · [Paper](https://arxiv.org/abs/2610.36878)<br>
  Delin Wang et al. · StepFun; FinStep; Renmin University of China; +2 institutions
- <a id="paper-f73eeee30c4bf920"></a>**Sci$Π$vot: Benchmarking Principal-Investigator Judgment at Pivotal Moments of Scientific AutoResearch Agents** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.21082)* · [Paper](https://arxiv.org/abs/2610.21082) · [Code](https://github.com/AutoResearch-Factory/SciPIvot) · [Project](https://autoresearch-factory.github.io/SciPIvot/) · [Dataset](https://huggingface.co/datasets/sun1245/SciPIvot)<br>
  Youran Sun et al. · University of Maryland, College Park; The Chinese University of Hong Kong; Gradient Network; +3 institutions
- <a id="paper-ff06580726cc267c"></a>**SCI-AGENT-EXAM: Benchmarking Agents on Scientific Research Tasks** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.32441)* · [Paper](https://arxiv.org/abs/2610.32441)<br>
  Tianyun Zhong et al. · University of Chinese Academy of Sciences; Institute of Software, Chinese Academy of Sciences; AI Data, Alibaba Group; +4 institutions
- <a id="paper-cb2c3c5e8ea5e05f"></a>**SciCurateBench: Curating Experimental Data from Heterogeneous Scientific Literature with Verbal-Action Agents** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.14393)* · [Paper](https://arxiv.org/abs/2610.14393)<br>
  Minuk Ma, Kaiyun Guo, Jiarui Ding · University of British Columbia
- <a id="paper-3092c4571c115f82"></a>**Science Utopia? Closed-Loop LLM Simulation of Academic Research Ecosystems** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.01257)* · [Paper](https://arxiv.org/abs/2610.01257) · [Code](https://github.com/Ahren09/ScienceUtopia) · [Project](https://Ahren09.github.io/ScienceUtopia)<br>
  Yiqiao Jin et al. · Georgia Institute of Technology; University of California, Los Angeles; University of Chicago; +1 institutions
- <a id="science-gym"></a>**Science-Gym: a simple testbed for AI-driven scientific discovery** · *[Machine Learning 2026](https://link.springer.com/article/10.1007/s10994-025-06914-x)* · [Paper](https://link.springer.com/article/10.1007/s10994-025-06914-x) · [Code](https://github.com/pibborn/science-gym)<br>
  Mattia Cerrato et al. · Johannes Gutenberg University Mainz; TU Darmstadt and hessian.AI; Max Planck Institute for Polymer Research; +2 institutions
- <a id="paper-d90a8e0869dee55c"></a>**SciExam for ENSO: Can AI Agents Build Climate Models?** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.10513)* · [Paper](https://arxiv.org/abs/2610.10513) · [Code](https://github.com/ylzhang2447/SciExam-ENSO-code) · [Dataset](https://github.com/ylzhang2447/SciExam-ENSO-code/tree/main/dataset)<br>
  Yinling Zhang et al. · The Ohio State University; Yale University; University of California, San Diego; +2 institutions
- <a id="paper-5687d10cf290fed0"></a>**SEABench: Benchmarking Endogenous Misalignment In Self-Evolving Agents** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2609.35596)* · [Paper](https://arxiv.org/abs/2609.35596) · [Code](https://github.com/SEABench-Endogenous-Misalignment/SEABench)<br>
  Saswat Das et al. · University of Virginia; ELLIS Institute Tübingen; Max Planck Institute for Intelligent Systems; +1 institutions
- <a id="paper-d8f686761184cfb8"></a>**SEAR: Self-Evolving Agentic Robotics** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.18792)* · [Paper](https://arxiv.org/abs/2610.18792) · [Code](https://github.com/Self-Evolving-Agentic-Robotics/SEAR) · [Project](https://sear.bot/)<br>
  Xinyi Wang et al. · Luma AI
- <a id="paper-74664ec24514d549"></a>**Search Shapes Conclusions: Auditing Evidence Selection Bias in Deep Research Agents** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2609.39026)* · [Paper](https://arxiv.org/abs/2609.39026)<br>
  Shuyao Xiao et al. · Beijing Normal University; Ke Holdings
- <a id="paper-e5da3aa895bba2db"></a>**Self-Consistency of Entity Sets and Citations in a Deep Research System under Repeated Prompting** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.26421)* · [Paper](https://arxiv.org/abs/2610.26421)<br>
  Lauri Pykälä, Kimmo K. Kaski · Aalto University School of Science
- <a id="paper-6f75779fcd87792a"></a>**Self-Evolving Agents Can Repair Failures but Struggle to Generalize from Them** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.22984)* · [Paper](https://arxiv.org/abs/2610.22984)<br>
  Weixiang Zhao et al. · Harbin Institute of Technology, Harbin, China; Harbin Institute of Technology, Shenzhen, China; The Chinese University of Hong Kong
- <a id="paper-42953ba160717449"></a>**SpatialScout: Can VLM Agents Actively Explore and Map 3D Scenes?** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.26659)* · [Paper](https://arxiv.org/abs/2610.26659) · [Code](https://github.com/JesseZZZZZ/SpatialScout)<br>
  Zhaoxi Zhang et al. · Peking University; Tianjin University
- <a id="paper-5bd5dfea78d8efef"></a>**ST-Bench: A Spatial-Temporal Benchmark for Multi-Agent System Generation on Scientific Research Tasks** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.07763)* · [Paper](https://arxiv.org/abs/2610.07763)<br>
  Qi Cheng et al. · Rutgers University; University of Pittsburgh; University of Minnesota; +3 institutions
- <a id="paper-aa18c0346e5ad3a3"></a>**TARSphere: A Robot-Oriented Full-Stack Framework for Long-Horizon Embodied Agents in Evolving Physical and Social Environments** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.30043)* · [Paper](https://arxiv.org/abs/2610.30043) · [Code](https://github.com/xuyicheng-zju/TARSphere) · [Project](https://xuyicheng-zju.github.io/TARSphere/)<br>
  Yicheng Xu et al. · Zhejiang University; Fudan University
- <a id="paper-4c7b45ef0c27315b"></a>**The Marathon of Scientific Reasoning: Robustness of Scientific Agents to Perturbations in Multi-Turn Interactions** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2609.34537)* · [Paper](https://arxiv.org/abs/2609.34537)<br>
  Xiaoting Lyu et al. · Xi’an Jiaotong University; Inria; Agency for Science, Technology and Research (A*STAR); +1 institutions
- <a id="paper-1b71ddb115ba5e37"></a>**The Scientific Research Taste Benchmark (SciTaste-Bench): A Multi-Disciplinary Benchmark for Assessing Large Language Models' Judgment of Research Taste in Scientific Papers** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.28653)* · [Paper](https://arxiv.org/abs/2610.28653)<br>
  Xinyi Gao et al. · University of Chinese Academy of Sciences; Alibaba Group; Tsinghua University
- <a id="paper-f56bdaf671cb8be4"></a>**The Tasteful Agent: Measuring and Improving Taste in Long-Horizon Tasks** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2609.25804)* · [Paper](https://arxiv.org/abs/2609.25804) · [Code](https://github.com/wbopan/tastebench) · [Dataset](https://huggingface.co/datasets/wenbopan/taste-bench)<br>
  Wenbo Pan et al. · City University of Hong Kong; Independent Researcher; Microsoft
- <a id="paper-712abb20a14f30f7"></a>**Trial by Trace: Benchmarking AI Agent Harnesses for Reliability and Failure Attribution** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.32285)* · [Paper](https://arxiv.org/abs/2610.32285) · [Code](https://github.com/TraceLite-AI/TraceTrial-Bench)<br>
  TraceLite AI et al. · Institute of Automation, CAS; Zhongguancun Academy; Institute of Information Engineering, CAS; +2 institutions
- <a id="paper-fd33ef0d1dd90a8b"></a>**UserArena: Benchmarking Interactive User Simulation for Long-Horizon Shopping Agents** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.30932)* · [Paper](https://arxiv.org/abs/2610.30932) · [Code](https://github.com/RecGPT-Team/UserArena) · [Project](https://recgpt-team.github.io/UserArena-Page) · [Dataset](https://github.com/RecGPT-Team/UserArena/blob/main/data/sessions.jsonl)<br>
  Jujia Zhao et al. · Leiden University; Renmin University of China; Alibaba Group; +1 institutions
- <a id="paper-644098a7aa74502f"></a>**VerifierBench: Benchmarking the Generation of Executable Verifiers for LLM Agents** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.28679)* · [Paper](https://arxiv.org/abs/2610.28679) · [Project](https://verifierbench.github.io/) · [Dataset](https://huggingface.co/datasets/Catherine1213/VerifierBench) · [Code](https://github.com/DwanZhang-AI/verifier-suite)<br>
  Jianing Yin et al. · University of Pennsylvania; University of Illinois at Urbana-Champaign; University of California, Berkeley; +2 institutions
- <a id="paper-282f8f39baa392ae"></a>**VibeTraining-Bench: Data-Trainer-Harness Co-Design for Iterative System Improvement** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.26342)* · [Paper](https://arxiv.org/abs/2610.26342)<br>
  Ruotian Peng et al. · Zhejiang University; Westlake University; Alibaba Token Hub, Alibaba Group; +2 institutions
- <a id="paper-1313ca747d97581e"></a>**VX-One: Typed, Calibrated Decision Heads for Real-Time Perimeter Triage - An empirical study of unknown-attack honesty, cascade gray zones, and calibration under drift** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.30090)* · [Paper](https://arxiv.org/abs/2610.30090)<br>
  Juan S. Santillana · Independent research
- <a id="paper-f30aa5f207baccbb"></a>**WhatWorkedBench: Benchmarking Experimental Understanding in AI Agents** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2609.27490)* · [Paper](https://arxiv.org/abs/2609.27490) · [Project](https://ethanning.github.io/WhatWorkedBench/) · [Code](https://github.com/EthanNing/WhatWorkedBench)<br>
  Jingjie Ning, Xueqi Li, Yibo Kong, Dongting Li · Carnegie Mellon University; Tsinghua University
- <a id="paper-4f6e0f0aac76178e"></a>**Where is Physical RSI capability from? An Observational Scaling Law of LLM-as-policy** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.26848)* · [Paper](https://arxiv.org/abs/2610.26848) · [Project](https://physrsi-eval.github.io/)<br>
  Zekai Li et al. · Galbot Team
- <a id="paper-3c56ba0d896a7404"></a>**WORTH Benchmark: Evidence Discovery under Not-Fully-Cooperative Information -- A Two-Episode Pilot** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.27597)* · [Paper](https://arxiv.org/abs/2610.27597)<br>
  Bo Zou, Chao Xu · Bread Studio
- <a id="paper-ade9af525e3953af"></a>**Δτ-Bench: Pushing Agents Toward a Moving Capability** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.34238)* · [Paper](https://arxiv.org/abs/2610.34238) · [Code](https://github.com/zjunlp/delta-tau-bench) · [Dataset](https://huggingface.co/datasets/zjunlp/delta-tau-bench)<br>
  Shuofei Qiao et al. · Zhejiang University; University College London

### 2025

- <a id="d02"></a>**BoxingGym: Benchmarking Progress in Automated Experimental Design and Model Discovery** · *[NeurIPS SEA Workshop 2025](https://openreview.net/forum?id=TgobzsU03X)* · [Paper](https://arxiv.org/abs/2501.01540) · [Code](https://github.com/kanishkg/boxing-gym)<br>
  Kanishk Gandhi et al. · Stanford University
- <a id="c10"></a>**CausalARC: Abstract Reasoning with Causal World Models** · *[NeurIPS LAW Workshop 2025](https://arxiv.org/abs/2509.03636)* · [Paper](https://arxiv.org/abs/2509.03636) · [Code](https://github.com/jmaasch/causal_arc) · [Project](https://jmaasch.github.io/carc/) · [HF Dataset](https://huggingface.co/datasets/jmaasch/causal_arc)<br>
  Jacqueline Maasch, John Kalantari, Kia Khezeli · Cornell Tech; YRIKKA
- <a id="d04"></a>**DiscoveryBench: Towards Data-Driven Discovery with Large Language Models** · *[ICLR 2025](https://proceedings.iclr.cc/paper_files/paper/2025/hash/0d70af566e69f1dfb687791ecf955e28-Abstract-Conference.html)* · [Paper](https://arxiv.org/abs/2407.01725) · [Code](https://github.com/EnvCommons/DiscoveryBench) · [HF Dataset](https://huggingface.co/datasets/allenai/discoverybench)<br>
  Bodhisattwa Prasad Majumder et al. · Allen Institute for AI; OpenLocus; University of Massachusetts Amherst
- <a id="llm-srbench"></a>**LLM-SRBench: A New Benchmark for Scientific Equation Discovery with Large Language Models** · *[ICML 2025](https://proceedings.mlr.press/v267/shojaee25a.html)* · [Paper](https://arxiv.org/abs/2504.10415) · [Code](https://github.com/deep-symbolic-mathematics/llm-srbench) · [HF Dataset](https://huggingface.co/datasets/nnheui/llm-srbench)<br>
  Parshin Shojaee et al. · Virginia Tech; VinUniversity; Carnegie Mellon University; +1 institutions
- <a id="mle-bench"></a>**MLE-bench: Evaluating Machine Learning Agents on Machine Learning Engineering** · *[ICLR 2025](https://proceedings.iclr.cc/paper_files/paper/2025/hash/7e3767db483c942b883eb4f8cfb74e31-Abstract-Conference.html)* · [Paper](https://arxiv.org/abs/2410.07095) · [Code](https://github.com/openai/mle-bench/)<br>
  Jun Shern Chan et al. · OpenAI
- <a id="mlgym"></a>**MLGym: A New Framework and Benchmark for Advancing AI Research Agents** · *[COLM 2025](https://openreview.net/pdf/75f6e6aa5276a0b93fd3859ec7b41c92ee79cea8.pdf)* · [Paper](https://arxiv.org/abs/2502.14499) · [Code](https://github.com/facebookresearch/MLGym)<br>
  Deepak Nathani et al. · Meta; University of California, Santa Barbara; University College London; +2 institutions
- <a id="mlrc-bench"></a>**MLRC-Bench: Can Language Agents Solve Machine Learning Research Challenges?** · *[NeurIPS Datasets and Benchmarks 2025](https://proceedings.neurips.cc/paper_files/paper/2025/hash/82c96f3c90741ef2c9b248e65d9b5db0-Abstract-Datasets_and_Benchmarks_Track.html)* · [Paper](https://arxiv.org/abs/2504.09702) · [Code](https://github.com/yunx-z/MLRC-Bench)<br>
  Yunxiang Zhang et al. · University of Michigan; LG AI Research; University of Illinois Chicago
- <a id="paperbench"></a>**PaperBench: Evaluating AI's Ability to Replicate AI Research** · *[ICML 2025](https://proceedings.mlr.press/v267/starace25a.html)* · [Paper](https://arxiv.org/abs/2504.01848) · [Code](https://github.com/openai/preparedness/tree/main/project/paperbench)<br>
  Giulio Starace et al. · OpenAI
- <a id="re-bench"></a>**RE-Bench: Evaluating frontier AI R&D capabilities of language model agents against human experts** · *[ICML 2025](https://proceedings.mlr.press/v267/wijk25a.html)* · [Paper](https://arxiv.org/abs/2411.15114) · [Code](https://github.com/METR/ai-rd-tasks)<br>
  Hjalmar Wijk et al. · METR
- <a id="scienceagentbench"></a>**ScienceAgentBench: Toward Rigorous Assessment of Language Agents for Data-Driven Scientific Discovery** · *[ICLR 2025](https://proceedings.iclr.cc/paper_files/paper/2025/hash/f12b4df26344f3be803c06b555252efe-Abstract-Conference.html)* · [Paper](https://arxiv.org/abs/2410.05080) · [Code](https://github.com/OSU-NLP-Group/ScienceAgentBench) · [Project](https://osu-nlp-group.github.io/ScienceAgentBench/) · [HF Dataset](https://huggingface.co/datasets/osunlp/ScienceAgentBench)<br>
  Ziru Chen et al. · The Ohio State University; University of Wisconsin–Madison
- <a id="c12"></a>**The Causal Chambers: Real Physical Systems as a Testbed for AI Methodology** · *[Nature Machine Intelligence 2025](https://www.nature.com/articles/s42256-024-00964-x)* · [Paper](https://arxiv.org/abs/2404.11341) · [Code](https://github.com/juangamella/causal-chamber-package) · [Data](https://github.com/juangamella/causal-chamber) · [Remote lab](https://www.causalchamber.ai/index.html) · [Experiments](https://github.com/juangamella/causal-chamber-paper)<br>
  Juan L. Gamella, Jonas Peters, Peter Bühlmann · ETH Zurich
- <a id="kosmos-audit"></a>**When AI Does Science: Evaluating the Autonomous AI Scientist KOSMOS in Radiation Biology** · *[arXiv 2025 (preprint)](https://arxiv.org/abs/2511.13825)* · [Paper](https://arxiv.org/abs/2511.13825)<br>
  Humza Nusrat, Omar Nusrat · Henry Ford Health; Michigan State University; Toronto Metropolitan University

### 2024

- <a id="d01"></a>**DiscoveryWorld A Virtual Environment for Developing and Evaluating Automated Scientific Discovery Agents** · *[NeurIPS Datasets and Benchmarks 2024](https://proceedings.neurips.cc/paper_files/paper/2024/hash/13836f251823945316ae067350a5c366-Abstract-Datasets_and_Benchmarks_Track.html)* · [Paper](https://proceedings.neurips.cc/paper_files/paper/2024/hash/13836f251823945316ae067350a5c366-Abstract-Datasets_and_Benchmarks_Track.html) · [Code](https://github.com/allenai/discoveryworld)<br>
  Peter Jansen et al. · Allen Institute for AI; Microsoft Research; University of Arizona

### 2022

- <a id="genedisco"></a>**GeneDisco: A Benchmark for Experimental Design in Drug Discovery** · *[ICLR 2022](https://openreview.net/pdf/46263f4b010fc363d4351c09cb675b69418c8680.pdf)* · [Paper](https://arxiv.org/abs/2110.11875) · [Code](https://github.com/genedisco/genedisco)<br>
  Arash Mehrjou et al. · GlaxoSmithKline; MIT; University of Oxford; +2 institutions
- <a id="scienceworld"></a>**ScienceWorld: Is your Agent Smarter than a 5th Grader?** · *[EMNLP 2022](https://aclanthology.org/2022.emnlp-main.775/)* · [Paper](https://arxiv.org/abs/2203.07540) · [Code](https://github.com/allenai/ScienceWorld)<br>
  Ruoyao Wang, Peter Jansen, Marc-Alexandre Côté, Prithviraj Ammanabrolu · University of Arizona; Microsoft Research; Allen Institute for AI

[↑ Contents](#contents)

<a id="related"></a>

## 🔗 Related Lists

- [Awesome LLM Scientific Discovery](https://github.com/HKUST-KnowComp/Awesome-LLM-Scientific-Discovery) — Scientific-method and autonomy taxonomy.
- [Awesome Open-Ended AI](https://github.com/jennyzzt/awesome-open-ended) — Open-ended learning, environment generation and evolution.
- [Awesome Self-Improving Agents](https://github.com/selfimproving-agent/Awesome-Self-Improving-Agents) — Foundation-model versus scaffolding improvement.
- [Awesome AI Scientist](https://github.com/ResearAI/Awesome-AI-Scientist) — Research lifecycle and scientific agent systems.
- [Awesome AI Scientists](https://github.com/tsinghua-fib-lab/Awesome-AI-Scientists) — Functional roles, collaboration and research domains.
- [Awesome Test-Time LLMs](https://github.com/Dereck0602/Awesome_Test_Time_LLMs) — Earlier test-time computing literature; supplement recent papers.
- [Awesome LLM Causal Reasoning](https://github.com/chendl02/Awesome-LLM-Causal-Reasoning) — Language models and causal reasoning.
- [Awesome Causal Discovery](https://github.com/Ewillingfly/AwesomeCausalDiscovery) — Broader causal-discovery methods.

<a id="contributing"></a>

## 🤝 Contributing

Suggestions and corrections are welcome. Prefer primary papers and author explanations; merge related artifacts into one entry. See the [contribution guide](CONTRIBUTING.md).
