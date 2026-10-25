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
  <a href="#contents"><img src="https://img.shields.io/badge/works-418-2563eb?style=flat-square" alt="418 curated works"></a>
  <a href="docs/benchmarks.md"><img src="https://img.shields.io/badge/environment_profiles-83-0f766e?style=flat-square" alt="83 environment profiles"></a>
  <a href="CONTRIBUTING.md"><img src="https://img.shields.io/badge/contributions-welcome-7c3aed?style=flat-square" alt="Contributions welcome"></a>
</p>

<p align="center">
  <a href="https://owd-ai.github.io/awesome-open-world-discovery/">Research observatory ↗</a> · <a href="#what-is-owd">What is OWD?</a> · <a href="#why-owd">Why this focus?</a> · <a href="#updates">Latest papers</a> · <a href="#contents">Browse the list</a> · <a href="CONTRIBUTING.md">Contribute</a>
</p>

<p align="center"><sub>Literature checked through 2026-10-25 · Papers, author blogs, code, and benchmarks</sub></p>

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

The latest 10 source-checked papers from our daily monitor · Updated 2026-10-25.

Visit the website for summaries, figures, today's updates, and the full research library.

| Date | Paper |
| --- | --- |
| 2026-10-22 | [RIDAR: Safeguarding Research Integrity in Autonomous Research Agents via Automated Detection and Runtime Intervention](https://arxiv.org/abs/2610.31372) |
| 2026-10-22 | [Large Language Models Meet Bayesian Optimization: Towards Self-evolving Wireless Digital Twins](https://arxiv.org/abs/2610.31192) |
| 2026-10-22 | [Inherited, Not Invented: Tracing the Provenance of Wait in Reasoning Models](https://arxiv.org/abs/2610.30882) |
| 2026-10-22 | [HiSTEVE 1.0: Harnessing Human-Interface VLA Agents for Open-World Games](https://arxiv.org/abs/2610.31162) |
| 2026-10-22 | [Co-Recursive Semantic Self-Extension: A Mathematical Foundation for Open-Ended Intelligence](https://arxiv.org/abs/2610.31097) |
| 2026-10-22 | [CellTrack-Bench: Microscopic Cell Tracking Benchmark for Vision-Language Models](https://arxiv.org/abs/2610.31566) |
| 2026-10-22 | [ADAPT for Science: A Multi-Agent System for Self-Evolving Scientific Optimization](https://arxiv.org/abs/2610.30851) |
| 2026-10-21 | [WeVisOne-VL: Unified Visual Perception from Objects to Pixels](https://arxiv.org/abs/2610.31329) |
| 2026-10-21 | [VX-One: Typed, Calibrated Decision Heads for Real-Time Perimeter Triage - An empirical study of unknown-attack honesty, cascade gray zones, and calibration under drift](https://arxiv.org/abs/2610.30090) |
| 2026-10-21 | [Toward Recursive Self-Improvement in Physical AI](https://arxiv.org/abs/2610.29677) |

<a id="contents"></a>

## 🗂️ Contents

| Topic | Research question | Works |
| --- | --- | ---: |
| 📚 [Discovery Foundations](#foundations) | What constitutes a discovery? | 27 |
| 🧩 [Discovery Representations](#causality) | What representations enable discovery? | 47 |
| 🔬 [Discovery Reasoning](#sci_methods) | How should agents formulate and test hypotheses? | 32 |
| 🧠 [Discovery Training](#learning) | How can we train agents to discover? | 62 |
| 🔄 [Continual Discovery](#adaptation) | How can agents learn from ongoing investigations? | 58 |
| 🛠️ [Discovery Systems](#systems) | How can we build reliable discovery systems? | 74 |
| 🌱 [Open-Ended Discovery](#open_ended) | How can agents expand the scope of discovery? | 44 |
| 📊 [Discovery Evaluation](#benchmarks) | How can we measure progress in discovery? | 74 |

[🔗 Related lists](#related) · [🤝 Contributing](#contributing)

Each work appears once under its primary contribution; see the [classification guide](docs/taxonomy.md#categories) for category scopes. Entries are grouped by publication year, newest first. Each work keeps its paper, code, project, and dataset links together, followed by authors and paper-time affiliations. Full attribution is recorded in the [catalog data](data/resources.json).

<a id="foundations"></a>

## 📚 Discovery Foundations

*What constitutes a discovery?*

### 2026

- <a id="paper-7c2e98f772c31d33"></a>**A Conditional No-Hair Theorem for Transformers: How Language Models Forget Their Prompt** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.24133)* · [Paper](https://arxiv.org/abs/2610.24133) · [Code](https://github.com/ShuyangenFrance/no-hair-transformers)<br>
  Shuyang Xiang · Independent researcher
- <a id="self-evolving-survey"></a>**A Survey of Self-Evolving Agents: What, When, How, and Where to Evolve on the Path to Artificial Super Intelligence** · *[TMLR 2026](https://openreview.net/pdf?id=CTr3bovS5F)* · [Paper](https://arxiv.org/abs/2507.21046) · [List](https://github.com/CharlesQ9/Self-Evolving-Agents)<br>
  Huan-ang Gao et al. · Princeton University; Princeton AI Lab; Tsinghua University; +14 institutions
- <a id="causal-agents"></a>**Causal Discovery in the Era of Agents** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2606.23608)* · [Paper](https://arxiv.org/abs/2606.23608)<br>
  Yujia Zheng et al. · Carnegie Mellon University; Mohamed bin Zayed University of Artificial Intelligence
- <a id="paper-7fabe26ca5c43e1f"></a>**Co-Recursive Semantic Self-Extension: A Mathematical Foundation for Open-Ended Intelligence** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.31097)* · [Paper](https://arxiv.org/abs/2610.31097)<br>
  Simon Hegelich et al. · GaiaLogic Unipessoal Lda.; Nanyang Technological University, Singapore; University of Macau
- <a id="paper-be65e818efe095a3"></a>**Designing Human-AI Collaborative Science: The 9A Framework** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.22948)* · [Paper](https://arxiv.org/abs/2610.22948) · [Code](https://github.com/ZihanZheng2000/human-ai-collaborative-science-framework)<br>
  Zihan Zheng, Linyue Pan, Xin Lan · University of Illinois Urbana–Champaign; Tsinghua University; Michigan State University
- <a id="discovery-foundation-models"></a>**Discovery Foundation Models: Toward Open-Ended Discovery Intelligence** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2609.15973)* · [Paper](https://arxiv.org/abs/2609.15973) · [Research resources](https://github.com/Gen-Verse/DFM-Plans) · [Project](https://phai-labs.com/collaborate/)<br>
  Ling Yang, Zhenfei Yin, Yingcheng Wu · DFM Scientist Collaboration Program
- <a id="paper-17285314da74286e"></a>**From Existing Methods to New Research Ideas: Two Perspectives on Recursive Self-Improvement** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.14625)* · [Paper](https://arxiv.org/abs/2610.14625) · [Project](https://prism-shadow.github.io/awesome-rsi/) · [Code](https://github.com/Prism-Shadow/awesome-rsi)<br>
  Leijun Zhou et al. · PrismShadow; Peking University; Zhejiang University; +1 institutions
- <a id="paper-318b93aa36b4f84e"></a>**From Sliding Windows to Self-evolving Lifelong Memory: A Dual-perspective Survey of Memory Paradigms for Long-Horizon Robotics VLA Models** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.23319)* · [Paper](https://arxiv.org/abs/2610.23319)<br>
  Yong Wang et al. · Department of Computer Science and Technology, Hainan Bielefeld University of Applied Sciences, Hainan 571700, China
- <a id="paper-cc26871dfb8c52d0"></a>**Memory-Centric Continual Learning for AI Agents** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.29357)* · [Paper](https://arxiv.org/abs/2610.29357)<br>
  Dongfang Li et al. · Harbin Institute of Technology (Shenzhen), Shenzhen, China; Shenzhen Loop Area Institute, Shenzhen, China; Tsinghua University, Beijing, China; +3 institutions
- <a id="paper-12f2f100744d125c"></a>**MMLA-RSI: Recursive Self-Improvement through RTT and RTMA** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.20294)* · [Paper](https://arxiv.org/abs/2610.20294)<br>
  Junyi Zou, Avrova Donz · MMLA-org; Communication University of China (CUC)
- <a id="paper-51ce772b7b376b84"></a>**Modeling Authentic Research Trajectories: A Graph View of Research Ideation** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.27337)* · [Paper](https://arxiv.org/abs/2610.27337)<br>
  Ruochen Li, Zhiyu Chen · University of Texas at Dallas
- <a id="paper-1178f409c73ca56a"></a>**Multimodal Embodied Agents: A Unified Capability-centric Perspective from Computer-Use to Robot-Use** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.30108)* · [Paper](https://arxiv.org/abs/2610.30108) · [Project](https://showlab.github.io/Awesome-Multimodal-Embodied-Agent)<br>
  Yanzhe Chen et al. · Show Lab, National University of Singapore
- <a id="paper-ec9a86ab8654e080"></a>**On the Tip of the Tongue: First-Token Cueing as a Behavioral Probe of Recall Failures in LLMs** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.23400)* · [Paper](https://arxiv.org/abs/2610.23400)<br>
  Jaewon Sok et al. · Seoul National University
- <a id="paper-dfbccdacbb319eab"></a>**Reading, Writing, Sharing, and Interacting with the World through Video** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.31668)* · [Paper](https://arxiv.org/abs/2610.31668) · [Project](https://vid-gen.github.io/video-world-model-survey) · [Code](https://github.com/vid-gen/awesome-video-world-model)<br>
  Shengqiong Wu et al. · University of Oxford; NUS; NTU; +1 institutions
- <a id="paper-4bc2aa3dc5c6d11a"></a>**Self-Evolving Agent Harness** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.18813)* · [Paper](https://arxiv.org/abs/2610.18813) · [Code](https://github.com/zgcagi/Harness-RSI) · [Project](https://zgcagi.github.io/Harness-RSI/)<br>
  Chuyang Wei et al. · Zhongguancun Academy; Zhongguancun Institute of Artificial Intelligence; University of Science and Technology of China
- <a id="paper-1e60f285c8164f89"></a>**Toward Recursive Self-Improvement in Physical AI** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.29677)* · [Paper](https://arxiv.org/abs/2610.29677) · [Project](https://physical2rsi.github.io) · [Code](https://github.com/Physical2RSI/Awesome-Physical2RSI)<br>
  Meng Luo et al. · National University of Singapore; Huazhong University of Science and Technology; Shanghai Jiao Tong University; +2 institutions
- <a id="paper-207da96ea3ec4712"></a>**Who Improves the Robot? Toward Physical Recursive Self-Improvement** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.18842)* · [Paper](https://arxiv.org/abs/2610.18842) · [Project](https://github.com/SAIL-Research-Lab/Physical-RSI)<br>
  Hai Zhou et al. · Shanghai Jiao Tong University; Google; Microsoft; +13 institutions

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
- <a id="cider-fm"></a>**CIDER-FM: Foundation Models for Causal Inference from Diverse Experimental Regimes** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2609.39523)* · [Paper](https://arxiv.org/abs/2609.39523)<br>
  Yuche Gao et al. · University of Cambridge; Max Planck Institute for Intelligent Systems; Prior Labs; +3 institutions
- <a id="paper-e6134b72bb2987fb"></a>**Coupling Noisy Pairwise Knowledge to the DAG Posterior for Causal Discovery** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.04559)* · [Paper](https://arxiv.org/abs/2610.04559)<br>
  Guoliang Xu, James E. Corter · Columbia University
- <a id="paper-c749e943da3bd0cf"></a>**D-World: An Explicit World-Language-Action Model with Recursive Self-Improvement under Dual Control** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.17114)* · [Paper](https://arxiv.org/abs/2610.17114)<br>
  Xuan Wen, Baichao Wang · Geek+
- <a id="paper-d6361dc4d470facb"></a>**Generalizing Identifiability Results in Causal Discovery from Complete Data to Missing Data Settings** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.19211)* · [Paper](https://arxiv.org/abs/2610.19211)<br>
  Matteo Ceriscioli, Shohei Shimizu, Mallika Gupta, Karthika Mohan · Oregon State University, Causal Intelligence and Reasoning Lab, Corvallis, USA; RIKEN Advanced Intelligence Project, Causal Inference Team, Tokyo, Japan; The University of Osaka, Reasoning for Intelligence Department, Osaka, Japan; +1 institutions
- <a id="paper-cff6e82a848858e5"></a>**Identifying ODEs from Unstructured Data with Causal Representation Learning** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2609.37083)* · [Paper](https://arxiv.org/abs/2609.37083)<br>
  Alessandro Trenta, Riccardo Massidda, Davide Bacciu, Sara Magliacane · University of Pisa; Saarland Informatics Campus; Saarland University; +1 institutions
- <a id="paper-4934e32c8ead615a"></a>**LaLa-World: Scaling Latent World Models with Natural Language Actions** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.27851)* · [Paper](https://arxiv.org/abs/2610.27851) · [Project](https://june-page.github.io/lala-world/) · [Code](https://github.com/junha1125/LaLa-World)<br>
  Junha Song et al. · NAVER AI Lab; Georgia Institute of Technology; Brown University; +1 institutions
- <a id="paper-4f0706d28b33b8b2"></a>**Language Models as AI Research World Models** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.12235)* · [Paper](https://arxiv.org/abs/2610.12235)<br>
  Zijun Wang et al. · Amazon; UC Santa Cruz; Emory University; +2 institutions
- <a id="paper-c49994cd61004d2c"></a>**Local Fisher Information Enables Sparse Causal Discovery** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.04291)* · [Paper](https://arxiv.org/abs/2610.04291)<br>
  Byeongguk Kang, Donghyeon Lee, Euijong Song, Gunwoong Park · Seoul National University
- <a id="paper-994c8a84ad65793d"></a>**Looking Ahead: Modeling Future Evolution in Autoregressive Video Generation** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.29989)* · [Paper](https://arxiv.org/abs/2610.29989) · [Code](https://github.com/TencentARC/Looking-Ahead) · [Project](https://hellorpg.github.io/looking-ahead/) · [HF Model](https://huggingface.co/TencentARC/Looking-Ahead) · [Dataset](https://huggingface.co/datasets/TencentARC/Looking-Ahead)<br>
  Ruopeng Gao et al. · Nanjing University; ARC Lab, Tencent IEG; Zhejiang University
- <a id="paper-7d26a5c9a55b02eb"></a>**Memento 3: Model-Based Recursive Self-Improvement through Reflective Rulebooks** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.11794)* · [Paper](https://arxiv.org/abs/2610.11794)<br>
  Haoyu Zhao et al. · University College London; Huawei Noah’s Ark Lab, UK; University of Liverpool
- <a id="paper-87bd413320e9c2f6"></a>**Not All Features Are Created Equal: A Mechanistic Study of Vision-Language-Action Models** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2603.19233)* · [Paper](https://arxiv.org/abs/2603.19233) · [Code](https://github.com/CWRU-AISM/action-atlas) · [Project](https://cwru-aism.github.io/vla-interp-page/) · [Project](https://action-atlas.com/)<br>
  Bryce Grant, Xijia Zhao, Peng Wang · Case Western Reserve University
- <a id="paper-11a0170b8097038e"></a>**One Thing Leads to Another: The Essentials of Time Series Causal Discovery** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.13430)* · [Paper](https://arxiv.org/abs/2610.13430) · [Project](https://github.com/CHAI-UK/Awesome-Time-Series-Causal-Discovery)<br>
  Kurt Butler et al. · The University of Edinburgh; Causality in Healthcare AI Hub (CHAI); University College London
- <a id="paper-64dc66d0c1650b10"></a>**PhysLDM: Latent Diffusion for High-Fidelity Deformable Simulation** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.07609)* · [Paper](https://arxiv.org/abs/2610.07609) · [Project](https://yucrazing.github.io/physldm/)<br>
  Yu Zhang, Xudong Xu, Xingang Pan · S-Lab, Nanyang Technological University, Singapore; Shanghai Artificial Intelligence Laboratory, Shanghai, China
- <a id="paper-328d19a6d649c766"></a>**Rate-Based Causal Discovery for Heavy-Tailed Models** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.15051)* · [Paper](https://arxiv.org/abs/2610.15051)<br>
  Vishal Routh · University of Georgia
- <a id="paper-a77e0de913ae3ba2"></a>**Residual-Based Causal Discovery via Pretrained In-Context Quantile Regression** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.29530)* · [Paper](https://arxiv.org/abs/2610.29530) · [Code](https://github.com/causality-lab/loscar)<br>
  Daniel Klippert, Quang Nhat Huynh, Alexander Marx · TU Dortmund University; Research Center Trustworthy Data Science and Security, University Alliance Ruhr; University of M¨unster
- <a id="paper-9a7fdd3c6dd57014"></a>**Ropedia W0: Scaling Loco-Manipulation World Models across Embodiments with Human Experience** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.26855)* · [Paper](https://arxiv.org/abs/2610.26855) · [Project](https://ropedia.github.io/ropedia-w0/) · [Code](https://github.com/Ropedia/ropedia-w0) · [HF Model](https://huggingface.co/ropedia-ai/Ropedia-W0)<br>
  Tianqi Liu et al. · Nanyang Technological University; Ropedia; Duke University; +2 institutions
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
- <a id="paper-9689553423421d52"></a>**State World Models: Execute the Rules, Generate the Pixels** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.26811)* · [Paper](https://arxiv.org/abs/2610.26811) · [Code](https://github.com/Zhangyr2022/StateWorldModel) · [Project](https://ivg-yanranzhang.github.io/StateWorldModel/) · [Dataset](https://huggingface.co/datasets/Louis0411/StateWorldModel)<br>
  Chan Yan Ki et al. · Department of Automation, Tsinghua University, China; GigaAI
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

- <a id="paper-b34e9d0c4929185b"></a>**AI-Driven Reproducibility and Analytical Robustness in Scientific Discovery** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.23845)* · [Paper](https://arxiv.org/abs/2610.23845)<br>
  Shicheng Liu et al. · Stanford University; Databricks AI Research; University of Massachusetts Amherst
- <a id="paper-e998d3a5dbcbbbaa"></a>**ALDER: Discovering the Laws of a World by Acting in It** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2609.33728)* · [Paper](https://arxiv.org/abs/2609.33728)<br>
  Teng Cao, Yu Deng, Quentin Delfosse, Kristian Kersting · Technische Universität Darmstadt; Intrinsic; German Research Center for AI; +1 institutions
- <a id="paper-e8558e860f15ac05"></a>**DAGLoop: Aligning Method Design with Experimental Feedback in Automated AI Research** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.25089)* · [Paper](https://arxiv.org/abs/2610.25089) · [Code](https://github.com/deng34567/DAGLoop)<br>
  Dengyuxing Wang et al. · The Hong Kong University of Science and Technology; Hong Kong Baptist University; Hong Kong Generative AI Research & Development Center; +1 institutions
- <a id="paper-c8b4c6ec0a0c2f8e"></a>**Diffusion Language Models Change Speed Across Tasks and Languages** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.25835)* · [Paper](https://arxiv.org/abs/2610.25835)<br>
  Mohsen Fayyaz et al. · University of California, Los Angeles; CIS, LMU Munich; Munich Center for Machine Learning
- <a id="paper-50dc4089b84b69c1"></a>**Formally Verified Autoresearch for Analyzing the Expressivity of Multi-Head Attention** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.25341)* · [Paper](https://arxiv.org/abs/2610.25341) · [Code](https://github.com/VerifiedMechanisms/automlr)<br>
  Karthik Viswanathan, Plamen Dimitrov, Stefano Rocca, Sarayu Sirikonda · Verified Mechanisms; MATS Research; University of California, Berkeley
- <a id="paper-1f223adc2e100034"></a>**Insights from Autoresearch for Solar Panel Segmentation** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.10491)* · [Paper](https://arxiv.org/abs/2610.10491) · [Code](https://github.com/VU-AIML/automl4eo-autoresearch-segmentation)<br>
  Justinas Lekavičius, Kürşat Kömürcü, Valentas Gružauskas, Linas Petkevičius · Vilnius University, Institute of Computer Science, Artificial Intelligence Methods Lab; IRISA, Université Bretagne Sud; European Commission Joint Research Centre
- <a id="paper-892f3051f980319f"></a>**Knowledge Manifold Optimization for Scientific Discovery** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.25662)* · [Paper](https://arxiv.org/abs/2610.25662)<br>
  Shigeru Obayashi, Yoshiaki Kawagoe, Kazuhiko Komatsu, Tomonaga Okabe · Institute of Fluid Science, Tohoku University; Department of Aerospace Engineering, Tohoku University; Research Center for Green X-Tech, Tohoku University; +1 institutions
- <a id="paper-ce6ca28e99a1250e"></a>**LLM-IDEA: Identifiability-Driven Experimental Agent for Autonomous Discovery of Mechanistic World Models** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.11253)* · [Paper](https://arxiv.org/abs/2610.11253) · [Code](https://github.com/Suraskey/llm-idea)<br>
  Surya Shetty, Ulisses Braga-Neto · Texas A&M University; Polara Labs Inc.
- <a id="paper-0b0ccb120eb20f9a"></a>**Multi-Agent AI Design of a Nanowatt Biomedical Low-Pass Filter from Topology to Layout** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.28677)* · [Paper](https://arxiv.org/abs/2610.28677) · [Code](https://github.com/MacAnalog/spicexplorer-release)<br>
  Danial Noori Zadeh, Devanshu Prasad, Mohamed B. Elamien · Department of Electrical and Computer Engineering, McMaster University
- <a id="paper-c70675c50ebe2aee"></a>**MultiEcho: An Experimental Science of Learned Worlds** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2609.33347)* · [Paper](https://arxiv.org/abs/2609.33347)<br>
  Meng Zhu, Airui Zhang · SHIHAO XINRUI Group
- <a id="paper-c0e89760c2e30631"></a>**Open-ended Scientific Discovery with Possibilistic Reasoning** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.11289)* · [Paper](https://arxiv.org/abs/2610.11289)<br>
  Anita Yang et al. · Lattice Lab, Toyota Motor Corporation, Japan; Department of Computer Science, University of Tokyo, Japan; EPIC Lab, College of Computing & Data Science, Nanyang Technological University, Singapore; +2 institutions
- <a id="paper-20a3bacb4d339fde"></a>**PremiseCheck: Efficient Fact-Checking of Human and AI Peer Reviews** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.21046)* · [Paper](https://arxiv.org/abs/2610.21046) · [Code](https://github.com/OpenLAIR/PremiseCheck) · [Dataset](https://huggingface.co/datasets/songdj/ReviewFact) · [Project](https://openlair.github.io/premisecheck/)<br>
  Dingjie Song et al. · Lehigh University; University of British Columbia; Vector Institute
- <a id="paper-3f5ff0f0f2d712fe"></a>**Reward Engine: Reward-Centric Self-Evolution for Open-Ended Tool Agents** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.22915)* · [Paper](https://arxiv.org/abs/2610.22915)<br>
  Litong Feng et al. · Huawei openJiuwen Team; Department of Statistics and Data Science, The Chinese University of Hong Kong (CUHK)
- <a id="multiple-hypotheses"></a>**Searching for What Matters: Open-Ended Discovery of Multiple Hypotheses with Agentic Data Exploration** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.17874)* · [Paper](https://arxiv.org/abs/2610.17874)<br>
  Sanchit Kabra et al. · Virginia Tech; Amazon
- <a id="paper-afdbb707d7a14074"></a>**Small but Mighty: Test Suites as Improvement Signals for Self-Evolving Agents** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.15964)* · [Paper](https://arxiv.org/abs/2610.15964) · [Code](https://github.com/ccsnow127/TeSearch)<br>
  Yutong Cheng et al. · Virginia Tech; NEC Laboratories America
- <a id="paper-d5a1b1084ce1c261"></a>**TagBO: LLM-Driven Task-Aware Graph Bayesian Optimization for Scientific Discovery** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.14626)* · [Paper](https://arxiv.org/abs/2610.14626)<br>
  Xinzhe Yuan et al. · Shanghai Artificial Intelligence Laboratory; Harbin Institute of Technology; Fudan University; +4 institutions
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
- <a id="paper-381c08cf57748156"></a>**Amortizing Sequential Experimental Design in Reasoning LLMs** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.20832)* · [Paper](https://arxiv.org/abs/2610.20832)<br>
  Anita Kriz, Antonin Berthon, Nicolás Astorga, Mihaela van der Schaar · University of Cambridge
- <a id="paper-511a84f55bad4b22"></a>**Ask to Distill: Learning to Synthesize Data for On-Policy Distillation** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.27450)* · [Paper](https://arxiv.org/abs/2610.27450) · [Code](https://github.com/GasolSun36/Ask_to_Distill) · [Dataset](https://huggingface.co/datasets/gasolsun/Ask_to_Distill-eval)<br>
  Jiashuo Sun et al. · University of Illinois Urbana-Champaign; The Hong Kong University of Science and Technology; Texas A&M University
- <a id="paper-dff7af28b08d7a75"></a>**Axiomatic World Modeling for Physics Reasoning** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.24519)* · [Paper](https://arxiv.org/abs/2610.24519) · [Project](https://lei-nlp-lab.github.io/physics_reasoning_neurips_2026/) · [Code](https://github.com/lei-nlp-lab/physics_reasoning_neurips_2026)<br>
  Xinye Yang, Zhenyang Liu, Yuxuan Wang, Yuanyuan Lei · Northwestern University; University of Florida
- <a id="paper-5abf8c8643b1a01d"></a>**Breaking Diffusion: Parallel Reasoning with Draft Refinement** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.26542)* · [Paper](https://arxiv.org/abs/2610.26542)<br>
  Jaesang Yu et al. · KAIST; Microsoft Research Asia; SkillBench
- <a id="paper-99e6c99aaec144c3"></a>**Bridged Self-Distillation for On-Policy Learning** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.26397)* · [Paper](https://arxiv.org/abs/2610.26397) · [Code](https://github.com/TUMLegalTech/Bridged-Self-Distillation)<br>
  Runsheng Chen et al. · Technical University of Munich; LMU Munich; Munich Center for Machine Learning (MCML)
- <a id="paper-c3fd4139f7f2c827"></a>**Can Visual Generation Expand What Unified Multimodal Models Know?** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.21459)* · [Paper](https://arxiv.org/abs/2610.21459) · [Project](https://kevinlllee.github.io/Knowledge-Transfer-Probing/) · [Code](https://github.com/kevinlllee/Knowledge-Transfer-Probing)<br>
  Wenkai Li, Wenyi Hong, Zhuoyi Yang, Jie Tang · Tsinghua University; Z.AI
- <a id="h04"></a>**CHART: A Harness-Rotation Curriculum for Harness-Robust Search Agents** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2609.22247)* · [Paper](https://arxiv.org/abs/2609.22247)<br>
  Xinlu Zhang et al. · Amazon
- <a id="paper-127deb898376f43f"></a>**Co-Evolving Acting and Forecasting for Language Agents** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.20597)* · [Paper](https://arxiv.org/abs/2610.20597) · [Code](https://github.com/ulab-uiuc/CoPE)<br>
  Haofei Yu et al. · University of Illinois Urbana-Champaign; University of California San Diego; Meta AI
- <a id="compute-aligned"></a>**Compute Aligned Training: Optimizing for Test Time Inference** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2604.24957)* · [Paper](https://arxiv.org/abs/2604.24957) · [Code](https://github.com/adamoosya/compute-aligned-training)<br>
  Adam Ousherovitch, Ambuj Tewari · University of Michigan
- <a id="paper-09c58b5352e897c3"></a>**CoworkEnv: Synthesizing Training Environments for Long-Horizon Cowork Agents** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.24960)* · [Paper](https://arxiv.org/abs/2610.24960) · [Code](https://github.com/HKUST-KnowComp/CoworkEnv) · [Project](https://github.com/zhongweixie/CoworkEnv-Lessons) · [HF Model](https://huggingface.co/zhongweixie/PocketWorker-8B-ClawEval-SFT)<br>
  Zhongwei XIE et al. · The Hong Kong University of Science and Technology; The Chinese University of Hong Kong; Hong Kong Baptist University; +1 institutions
- <a id="paper-0b814b1f03c2835d"></a>**CURIO: Curiosity-Driven Test-Time Learning for Open-Ended Discovery** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.04851)* · [Paper](https://arxiv.org/abs/2610.04851) · [Project](https://ft2023.github.io/CURIO/) · [Code](https://github.com/ft2023/CURIO)<br>
  Tao Feng et al. · University of Illinois Urbana-Champaign; University of Maryland, College Park; Stanford University
- <a id="paper-008b443e8ade0e00"></a>**Deep Fusion Memory: A Chunk-Level Parametric Memory for Large Language Models** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.25100)* · [Paper](https://arxiv.org/abs/2610.25100)<br>
  Rubin Wei et al. · LUMIA Lab, School of Artificial Intelligence, Shanghai Jiao Tong University; Shanghai Artificial Intelligence Laboratory
- <a id="paper-fd98d0ad6f9d37a7"></a>**ECHO: Efficient Causal Self-Recursion Beyond Auxiliary Multi-Token Prediction** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.24766)* · [Paper](https://arxiv.org/abs/2610.24766) · [Code](https://github.com/ernie-research/ECHO)<br>
  Yuxuan Zhou et al. · ERNIE Team, Baidu; Independent Researcher
- <a id="paper-d0a1aad7216e9e1d"></a>**Evolving in Thought Space: Training a Small Model at Test Time Unlocks Better Discoveries** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.06269)* · [Paper](https://arxiv.org/abs/2610.06269) · [Code](https://github.com/Human-Agent-Society/reef/tree/main/recipes/tttd/examples/guidance_ttt) · [Project](https://www.reefinfra.ai/docs/user-guide/recipes/guidance-ttt/)<br>
  Chonghe Jiang et al. · Massachusetts Institute of Technology; Hong Kong Polytechnic University; ByteDance Inc.; +6 institutions
- <a id="r05"></a>**Explore More, Drift Less: Outcome-Only Reinforcement Learning Can Suffice for Long-Horizon Interactive Agents** · *[arXiv 2026 (preprint)](https://arxiv.org/html/2609.01245v1)* · [Paper](https://arxiv.org/html/2609.01245v1)<br>
  Liming Pu et al.
- <a id="paper-339e82eef6e4a8b6"></a>**From Valid to Useful: Post-Verification Acquisition for Recursive Self-Improving Recommendation** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.04302)* · [Paper](https://arxiv.org/abs/2610.04302)<br>
  Tonmoy Hasan et al. · Nubank
- <a id="paper-843cdbc0b49a3683"></a>**Harness Scaling for Generalizable Agentic Reinforcement Learning** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.29458)* · [Paper](https://arxiv.org/abs/2610.29458)<br>
  Fei Bai et al. · Gaoling School of Artificial Intelligence, Renmin University of China; IQuest Research; Beihang University
- <a id="paper-0182cce120aad869"></a>**HarnessRL: Co-Evolving Policies with a Just-in-Time Training Harness for Open-Ended RL** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.26426)* · [Paper](https://arxiv.org/abs/2610.26426) · [Code](https://github.com/Tongyi-ConvAI/Qwen-Character/tree/main/HarnessRL)<br>
  Xiaoqiang Wang et al. · Alibaba Token Hub, Alibaba Group; Université de Montréal; Mila - Quebec AI Institute
- <a id="paper-48d5ab7e8e8c0f56"></a>**HybridResearcher: Bridging the Structured-Unstructured Boundary for Deep Research Agents** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.24899)* · [Paper](https://arxiv.org/abs/2610.24899)<br>
  Soyoung Yoon et al. · Seoul National University; University of California, Los Angeles; University of North Carolina at Chapel Hill; +2 institutions
- <a id="paper-c474fbc2967f22ed"></a>**Inherited, Not Invented: Tracing the Provenance of Wait in Reasoning Models** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.30882)* · [Paper](https://arxiv.org/abs/2610.30882)<br>
  Zhizhuo Kou et al. · The Hong Kong University of Science and Technology; Peking University; Huawei Noah’s Ark Lab
- <a id="paper-ff790d2b9ae4b233"></a>**Language Models Learn to Improve Language Models** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.23344)* · [Paper](https://arxiv.org/abs/2610.23344)<br>
  Minhua Lin et al. · The Pennsylvania State University; UC Santa Cruz; Emory University; +2 institutions
- <a id="paper-a97c1f5a709e4de6"></a>**Lean4AgenticRL: Advancing Agentic RL with Verifiable Multi-level Process Rewards** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.22448)* · [Paper](https://arxiv.org/abs/2610.22448) · [Code](https://github.com/RickySkywalker/Lean4AgenticRL) · [HF Model](https://huggingface.co/amazon/LAR-27B)<br>
  Ruida Wang, Gerald Friedland, Tong Zhang, Chris Kong · Amazon Web Services; University of Illinois Urbana-Champaign
- <a id="paper-44d308ca6f63a0d7"></a>**LeanPRM: Lean-Grounded Process Supervision for Natural Language Proof Verification** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.17697)* · [Paper](https://arxiv.org/abs/2610.17697) · [Project](https://rlafuente.com/lean-prm) · [Code](https://github.com/pavelslab-nyu/LeanPRM) · [Dataset](https://huggingface.co/datasets/pavelslab-nyu/LeanPRM/tree/main/data) · [Dataset](https://huggingface.co/datasets/pavelslab-nyu/LeanPRM/tree/main/benchmark)<br>
  Rodney Lafuente-Mercado et al. · University of Texas at Austin; University of California, Los Angeles; New York University
- <a id="paper-bc757bb51b5cc488"></a>**Learning to Think and Explore in 3D World** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.21783)* · [Paper](https://arxiv.org/abs/2610.21783) · [Project](https://williamium3000.github.io/act3d/)<br>
  Yijiang Li, Bingyang Wang, Nuno Vasconcelos · University of California San Diego; Georgia Institute of Technology
- <a id="paper-07ae5adf14031356"></a>**MELD: Recursive Self-Improvement via Hierarchical Coordination for Multi-Agent Scientific Discovery** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.24454)* · [Paper](https://arxiv.org/abs/2610.24454)<br>
  Sizhe Tang, Zuyuan Zhang, Zeyu Fang, Tian Lan · George Washington University
- <a id="paper-03627392f7accc23"></a>**MLExpert: Towards a Generalist Agentic Model for Autonomous Machine Learning Engineering** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.22344)* · [Paper](https://arxiv.org/abs/2610.22344) · [Code](https://github.com/InternScience/MLExpert) · [HF Model](https://huggingface.co/InternScience/MLExpert)<br>
  Shangheng Du et al. · East China Normal University; Shanghai Artificial Intelligence Laboratory
- <a id="paper-2d09cb91206e5f2c"></a>**Muse Glimmer 30B: An On-Device Agentic Model** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.24628)* · [Paper](https://arxiv.org/abs/2610.24628) · [HF Model](https://huggingface.co/meta-models/Muse-Glimmer-30B)<br>
  Muse Glimmer team et al. · Meta Superintelligence Labs
- <a id="paper-75eeeb130b15e1f6"></a>**PAR: Progress-Aligned Recurrence for Length Generalization in State Tracking** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.27628)* · [Paper](https://arxiv.org/abs/2610.27628)<br>
  Pan Wang et al. · Ant International; National University of Singapore
- <a id="paper-06be42075e2fd31a"></a>**Progress-Aware Distillation for Mitigating Stagnation in Small Language Model Agents** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.19439)* · [Paper](https://arxiv.org/abs/2610.19439) · [Code](https://github.com/CaoYuanpu/ProD)<br>
  Yuanpu Cao et al. · The Pennsylvania State University; Microsoft CoreAI
- <a id="paper-6458fcd3e61718e0"></a>**RSIPO: Recursive Self-Improving Policy Optimization for Agentic Reinforcement Learning via Skill-Policy Co-Evolution** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.15772)* · [Paper](https://arxiv.org/abs/2610.15772) · [Code](https://github.com/zfkarl/RSIPO) · [HF Model](https://huggingface.co/Karl28/RSIPO-Qwen2.5-7B-Instruct-ALFWorld) · [HF Model](https://huggingface.co/Karl28/RSIPO-Qwen2.5-7B-Instruct-Search)<br>
  Fan Zhang et al. · CUHK; THU; NUS; +5 institutions
- <a id="paper-0687e07a2193b7e6"></a>**Rubric-CEPR: Self-Evolving Image Editing via Reward-Verified Self-Distillation** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.12469)* · [Paper](https://arxiv.org/abs/2610.12469) · [Code](https://github.com/riteshthawkar/Rubric-CEPR) · [Project](https://riteshthawkar.github.io/Rubric-CEPR/)<br>
  Ritesh Thawkar, Shubham Patle, Shravan Venkatraman, Rao Muhammad Anwer · Mohamed bin Zayed University of Artificial Intelligence; Aalto University
- <a id="paper-f5ebfafb83c6121b"></a>**Scaling in Games: Continued Pre-Training For Embodied Agents In Diverse Virtual Worlds** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.28698)* · [Paper](https://arxiv.org/abs/2610.28698) · [Project](https://gamescaling.github.io) · [Code](https://github.com/THUSI-Lab/GameScaling) · [HF Model](https://huggingface.co/THUSI-Lab/GameScaling-9B-S1)<br>
  Kuan Zhang et al. · miHoYo Honkai AI R&D Team; College AI, Tsinghua University; University of Chinese Academy of Sciences; +3 institutions
- <a id="d05"></a>**Scaling Scientific Discovery Environments for Turn-Level Agentic RL** · *[arXiv 2026 (preprint)](https://arxiv.org/html/2607.28990v1)* · [Paper](https://arxiv.org/html/2607.28990v1)<br>
  Yucheng Xu et al. · Shanghai AI Laboratory
- <a id="paper-dc899dc4881918fb"></a>**Self-Evolve With a Reference:Anchored Training of Tool-Integrated Agents** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.09856)* · [Paper](https://arxiv.org/abs/2610.09856)<br>
  Wenjie Liao, Liangjie Zhao, Zehong Cao · Waseda University; Adelaide University
- <a id="r06"></a>**SPROUT: Scaling Agentic Reinforcement Learning for Long-Horizon Software Engineering** · *[arXiv 2026 (preprint)](https://arxiv.org/html/2610.14405v1)* · [Paper](https://arxiv.org/html/2610.14405v1) · [Code](https://github.com/RISE-X-Lab/SPROUT) · [Project](https://rise-x-lab.github.io/SPROUT/)<br>
  Mengyang Liu et al. · Shanghai Jiao Tong University; Amazon; Nanjing University; +2 institutions
- <a id="paper-b40ae7e623658513"></a>**SteerSearch: Interactive Search Reasoning with Mid-Response Steering** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.24287)* · [Paper](https://arxiv.org/abs/2610.24287)<br>
  Udit Thakur et al. · Language Technology Lab, University of Amsterdam; eBay
- <a id="paper-a2259b2fffb789f0"></a>**SynCo: Data Synthesis Co-Training for Self-Evolving LLMs via Multi-Agent Reinforcement Learning** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.11345)* · [Paper](https://arxiv.org/abs/2610.11345) · [Code](https://github.com/weiyang930/SynCo) · [Dataset](https://huggingface.co/datasets/weiyang930/SynCo)<br>
  Wei Yang et al. · University of Southern California; The George Washington University; Georgia Institute of Technology
- <a id="paper-7af4030312fdc9aa"></a>**ToM2Vec: Continuous Theory-of-Mind Tokens for Multi-Agent Coordination** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.29934)* · [Paper](https://arxiv.org/abs/2610.29934) · [Code](https://github.com/nsivaku/tom2vec)<br>
  Nithin Sivakumaran et al. · UNC Chapel Hill; Cisco; The University of Texas at Austin
- <a id="paper-38e70b683c26da97"></a>**TraceForge: Distilling with Your Own Thinking** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.29680)* · [Paper](https://arxiv.org/abs/2610.29680)<br>
  Yan Wang · Independent Researcher
- <a id="paper-c8f3602bba98a90b"></a>**Trinity: Self-Evolving Vision-Language Models with a Self-Verifier** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.04469)* · [Paper](https://arxiv.org/abs/2610.04469)<br>
  Youngwan Lee, Yong-Ju Lee, Sung Ju Hwang · Electronics and Telecommunications Research Institute (ETRI); Korea Advanced Institute of Science and Technology (KAIST); DeepAuto.ai
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

- <a id="paper-6f63cd1d3b1feb5c"></a>**Are Self-Evolving Agents Continual Learners?** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.25858)* · [Paper](https://arxiv.org/abs/2610.25858)<br>
  Xiaoyin Chen et al. · Mila – Quebec AI Institute; Université de Montréal; Google DeepMind
- <a id="t13"></a>**ASCENT: Online Test-Time Training of Long-Horizon Agents via Self-Distillation of Verified Experience** · *[arXiv 2026 (preprint)](https://arxiv.org/html/2610.05303v1)* · [Paper](https://arxiv.org/html/2610.05303v1) · [Project](https://artificer-ai-lab.github.io/ASCENT/)<br>
  Haodong Lu, Dong Gong · UNSW Sydney
- <a id="paper-94ab554ffc39816c"></a>**Beyond Successor Accuracy: State Retention for Recursive Self-Improvement in Recommendation** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.07105)* · [Paper](https://arxiv.org/abs/2610.07105) · [Code](https://github.com/Jinfeng-Xu/RecRSI)<br>
  Jinfeng Xu et al. · The University of Hong Kong; The Hong Kong Polytechnic University; The Hong Kong University of Science and Technology; +1 institutions
- <a id="paper-63c5fd925e9f2dcd"></a>**ChartEvo: Self-Evolving Agent Harnesses for Long-Tail Chart Reasoning** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.28282)* · [Paper](https://arxiv.org/abs/2610.28282)<br>
  Qi Wang et al. · State Key Laboratory of Multimodal Artificial Intelligence Systems, CASIA; School of Artificial Intelligence, University of Chinese Academy of Sciences; New Laboratory of Pattern Recognition, CASIA; +1 institutions
- <a id="paper-7f537879bf2ffb4a"></a>**CoEvolve: Self-Evolving Code Policies from Skills to Strategies for Humanoid Robots** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.23288)* · [Paper](https://arxiv.org/abs/2610.23288)<br>
  Zicheng Liu et al. · Peking University; Renmin University of China; Beijing XYZ Embodied AI Co., Ltd.; +1 institutions
- <a id="paper-4bd61eafe4f2ad4e"></a>**Darwin-Claw: Environment-Adaptive Experience Consolidation for Recursively Self-Evolving Agents** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.23574)* · [Paper](https://arxiv.org/abs/2610.23574)<br>
  Mingze Yin et al. · Zhejiang University; Tencent; Zhongguancun Academy
- <a id="paper-8e422795873eb25c"></a>**EmbodiedEvo: Self-Evolving Coding Agent For Physical Intelligence** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.18867)* · [Paper](https://arxiv.org/abs/2610.18867) · [Project](https://lab.einsia.ai/embodiedevo/) · [Code](https://github.com/Einsia/EmbodiedEvo)<br>
  Wenyi Li et al. · Navers Lab; Einsia.AI; Tsinghua University
- <a id="paper-dc5079437446d0d5"></a>**EvoBelief: Falsifiable World Models for Self-Improving LLM Agents** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.12789)* · [Paper](https://arxiv.org/abs/2610.12789)<br>
  Janet Wang et al. · Tulane University; Amazon
- <a id="paper-65f2aa74e4cbffb5"></a>**ForkPilot: Self-Evolving Policy for Retrospective Search in Long-Horizon Agents** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.04889)* · [Paper](https://arxiv.org/abs/2610.04889)<br>
  Xinyue Zeng et al. · Virginia Tech; Microsoft
- <a id="paper-173432e0518b18b9"></a>**From Pareto to Preference: Personalized Test-Time Scaling via Amortized Agentic Policy Discovery** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.09684)* · [Paper](https://arxiv.org/abs/2610.09684) · [Code](https://github.com/WangXinglin/PersonTTS)<br>
  Xinglin Wang et al. · Beijing Institute of Technology; Xiaohongshu Inc
- <a id="harness-ttt"></a>**HarnessTTT: Learn to Optimize Harness at Test-Time for Scientific Discovery** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.17370)* · [Paper](https://arxiv.org/abs/2610.17370) · [Code](https://github.com/SaFo-Lab/Self_Adapt_Harness) · [Project](https://gray311.github.io/harnessrl/) · [HF Dataset](https://huggingface.co/datasets/gray311/HarnessRL)<br>
  Yingzi Ma et al. · University of Wisconsin-Madison; NVIDIA; Johns Hopkins University; +2 institutions
- <a id="paper-396ef1a44f871e38"></a>**InstAgent: A Recursively Self-Improving Agent Operating System for Heterogeneous Robot Collaboration** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.23098)* · [Paper](https://arxiv.org/abs/2610.23098)<br>
  Haoyang Luo et al. · ShanghaiTech University, Shanghai, China; InstAdapt, Shanghai, China
- <a id="paper-47d9c27401b76abb"></a>**InterMimicGen: Scaling Humanoid Loco-Manipulation through Self-Evolving Motion Imitation** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.06850)* · [Paper](https://arxiv.org/abs/2610.06850) · [Project](https://sirui-xu.github.io/InterMimicGen/)<br>
  Yucheng Zhang et al. · University of Illinois Urbana-Champaign; NVIDIA
- <a id="paper-f67c24c899266324"></a>**Learning to Compose: Recursive Self-Improvement of Shared Executable Stacks for Zero-Shot Long-Horizon Robot Manipulation** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.24464)* · [Paper](https://arxiv.org/abs/2610.24464) · [Code](https://github.com/cocacola-lab/Recursia) · [Project](https://cocacola-lab.github.io/Recursia-website/)<br>
  Yangzhi Chen et al. · Beijing Jiaotong University; New York University; University of Southern California; +2 institutions
- <a id="t11"></a>**Learning to Discover at Test Time** · *[ICML 2026](https://proceedings.mlr.press/v306/yuksekgonul26a.html)* · [Paper](https://arxiv.org/html/2601.16175v1) · [Code](https://github.com/test-time-training/discover) · [Project](https://test-time-training.github.io/discover)<br>
  Mert Yuksekgonul et al. · Stanford University; NVIDIA; Astera Institute; +2 institutions
- <a id="paper-bf157ba63fabe951"></a>**Memory as Belief: Bayesian Evolution of Memory for Self-Evolving LLM Agents** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.25119)* · [Paper](https://arxiv.org/abs/2610.25119)<br>
  Yiming Xu et al. · School of Computer Science and Technology, Xi’an Jiaotong University; Shaanxi Provincial Key Laboratory of Big Data Knowledge Engineering, Xi’an Jiaotong University; University of Virginia, Charlottesville, Virginia, USA; +1 institutions
- <a id="paper-4f24e668bd567dab"></a>**More Memory, Worse Agents: Error Reproduction and Anti-Persistence in LLM Agents** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.27406)* · [Paper](https://arxiv.org/abs/2610.27406)<br>
  Ruhan Wang, Kishan Panaganti, Dongruo Zhou · Indiana University; Tencent HY
- <a id="t12"></a>**No Time Like the Present: Agentic Test-Time Training for LLM Agents** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2607.03441)* · [Paper](https://arxiv.org/abs/2607.03441)<br>
  Yanbo Wang et al. · Kuaishou Technology
- <a id="paper-6273fff431181535"></a>**Online Open-World Wafer Defect Discovery using Hyperdimensional Computing** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.28949)* · [Paper](https://arxiv.org/abs/2610.28949)<br>
  Quanling Zhao et al. · University of California San Diego; IBM Research; Anderon
- <a id="paper-52731a9209ac98ed"></a>**PreCoMem: Predictive Cognitive Memory for Self-Evolving Long-Term Dialogue Agents** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.29467)* · [Paper](https://arxiv.org/abs/2610.29467) · [Code](https://github.com/ZhongWishing/PreCoMem)<br>
  Jian Zhong et al. · Nankai University; vivo AI Lab; Tsinghua University; +2 institutions
- <a id="paper-cb72119b3b1f3079"></a>**Recursive Self-Improvement of Visuomotor Policies through Local Recovery Supervision** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.05151)* · [Paper](https://arxiv.org/abs/2610.05151)<br>
  Yuzhi Zhang, Xinyu Liu, Yu Zhang · Beihang University
- <a id="paper-55ab01be48315197"></a>**Reflect After Failure: Brain-Inspired Self-Evolving Agents for Embodied Spatial Intelligence** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.20312)* · [Paper](https://arxiv.org/abs/2610.20312)<br>
  Xin Li et al. · City University of Hong Kong; East China Normal University; University of Electronic Science and Technology of China; +2 institutions
- <a id="paper-c15fc300d6309d58"></a>**Remembering Has a Price: Learning Memory Worth under Resource Constraints** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.26453)* · [Paper](https://arxiv.org/abs/2610.26453) · [Code](https://github.com/AIGNLAI/TokenWorth)<br>
  Guannan Lai, Zi-Yang Bai, Jun-Peng Jiang, Han-Jia Ye · School of Artificial Intelligence, Nanjing University; National Key Laboratory for Novel Software Technology, Nanjing University
- <a id="paper-256ec415fdba134a"></a>**RewardWeaver: Long-Horizon Interactive Learning for Language Agents via Self-Evolving Reward Adaptation** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.10120)* · [Paper](https://arxiv.org/abs/2610.10120)<br>
  Hengbo Xiao et al. · Yoolee.ai; University of Science and Technology of China; Peking University; +1 institutions
- <a id="paper-41968877a20ed1a5"></a>**RoboBridge: A Self-Evolving Embodied Agent Framework for Sim-to-Real Transfer** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.02717)* · [Paper](https://arxiv.org/abs/2610.02717)<br>
  Chenxi Li et al. · Shanghai Artificial Intelligence Laboratory; Zhejiang University; Beihang University; +3 institutions
- <a id="paper-2e4a524137176712"></a>**SEER: Self-Evolving Event Reasoning and Retrieval for Time Series Forecasting** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.04109)* · [Paper](https://arxiv.org/abs/2610.04109) · [Project](https://github.com/BennyTMT/SEER)<br>
  Mingtian Tan et al. · Google Cloud AI Research; University of Virginia
- <a id="paper-2d5446a91ef47109"></a>**Self-Evolving Agents through Privileged Retrospective Distillation** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.27495)* · [Paper](https://arxiv.org/abs/2610.27495)<br>
  Yuhang Zhou et al. · Meta AI
- <a id="paper-a68e54ff3367de89"></a>**Self-Evolving Static Analysis via LLM Pseudo-Labeling** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.30184)* · [Paper](https://arxiv.org/abs/2610.30184)<br>
  Rui Melo et al. · Carnegie Mellon University; FEUP
- <a id="paper-d1c8322a1b1949b1"></a>**Selm: Self-Evolving Library Management for Multi-Skill Agent Optimization** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.24630)* · [Paper](https://arxiv.org/abs/2610.24630)<br>
  Mengxi Hu et al. · School of Information, Renmin University of China, Beijing, China; Key Laboratory of Data Engineering and Knowledge Engineering, Beijing, China; Engineering Research Center of Database and Business Intelligence, Beijing, China; +2 institutions
- <a id="paper-cf7f5519592d5d60"></a>**Skill-V: Verifiable Self-Evolving Skill Library for Interactive Agents** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.11781)* · [Paper](https://arxiv.org/abs/2610.11781)<br>
  Jie Ma et al. · Xiamen University; Kuaishou Technology; Nankai University
- <a id="skilltta"></a>**Skills on the Fly: Test-Time Adaptive Skill Synthesis for LLM Agents** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2605.16986)* · [Paper](https://arxiv.org/abs/2605.16986) · [Code](https://github.com/Hydr0pon1c/Skills-on-the-fly)<br>
  Jingxing Wang et al. · Shanghai Jiao Tong University; OPPO Research Institute
- <a id="paper-79697a458d1ee6cc"></a>**SpatialBrain: Spatial Intelligence Growing from Experience** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.29317)* · [Paper](https://arxiv.org/abs/2610.29317)<br>
  Yifan Zhou et al. · Shanghai Jiao Tong University; Zhejiang University
- <a id="paper-308a2c9d337c0bc8"></a>**SpecForge: Recursive Self-Improvement for Coding Agents via Behavioral Specifications** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.15708)* · [Paper](https://arxiv.org/abs/2610.15708) · [Code](https://github.com/ccsnow127/SpecForge)<br>
  Yutong Cheng, Haifeng Chen, Peng Gao, Wei Cheng · Virginia Tech; NEC Laboratories America
- <a id="ttt-ntp"></a>**Test-Time Training with Next-Token Prediction** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2606.21803)* · [Paper](https://arxiv.org/abs/2606.21803) · [Code](https://github.com/yancyou/TTT-NTP)<br>
  Xuan Ouyang, Zefan Cai, Junjie Hu · University of Wisconsin-Madison
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
- <a id="paper-c5f5637b6166e690"></a>**AReaL-RSI: Adaptive Scaling and Coordination of Recursive Self-Improvement** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.18083)* · [Paper](https://arxiv.org/abs/2610.18083) · [Code](https://github.com/areal-project/AReaL-RSI)<br>
  Wenhao Zhou et al. · Ant Group; Zhejiang University; HKUST
- <a id="a01"></a>**autoresearch** <sup>project</sup> · [Code](https://github.com/karpathy/autoresearch)<br>
  Andrej Karpathy
- <a id="paper-1e69ca6b1461149c"></a>**BrickWright: Agentic Creation of Physically Feasible Brick Builds** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.31651)* · [Paper](https://arxiv.org/abs/2610.31651) · [Project](https://avalovelace1.github.io/brickwright/) · [Code](https://github.com/AvaLovelace1/brickwright)<br>
  Ava Pun et al. · Carnegie Mellon University; Independent Researcher; Stanford University
- <a id="paper-66f56984b6446ca0"></a>**Building AI Research Teams for Autonomous Discovery of Linear Attention Architectures** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.28887)* · [Paper](https://arxiv.org/abs/2610.28887)<br>
  Yujian Liu et al. · UC Santa Barbara; Pennsylvania State University; LinkedIn
- <a id="paper-433abe28aa06ff75"></a>**Cache Engineering for Agents** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.28577)* · [Paper](https://arxiv.org/abs/2610.28577) · [Code](https://github.com/thu-nics/AKV)<br>
  Tianyu Fu et al. · Tsinghua University; The Chinese University of Hong Kong
- <a id="station"></a>**Can AI Agents Make Open-Ended Scientific Discovery? Evidence from Station** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.08927)* · [Paper](https://arxiv.org/abs/2610.08927) · [Code](https://github.com/dualverse-ai/station-open-reseach) · [Data](https://github.com/dualverse-ai/station-open-reseach_data) · [Project](https://dualverse-ai.github.io/station-open-reseach_data)<br>
  Wenyu Du, Stephen Chung · DualverseAI; The University of Hong Kong; University of Cambridge
- <a id="causalsteward"></a>**CausalSteward: An Agentic Divide-Conquer-Combine Copilot for Causal Discovery** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2607.01936)* · [Paper](https://arxiv.org/abs/2607.01936)<br>
  Nicholas Tagliapietra et al. · TU Darmstadt; Bosch Center for Artificial Intelligence; hessian.AI; +2 institutions
- <a id="paper-83d8f02ebb01f589"></a>**Compile Once, Run Cheap: Frozen, Portable Skills for Embodied Agents, and What Recursive Self-Improvement Adds** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.25114)* · [Paper](https://arxiv.org/abs/2610.25114) · [Code](https://github.com/Orillusion/embodied-skill-rsi)<br>
  Jingwen Bai et al. · Beijing Ou Rui Ling Shi Technology Co., Ltd.; ChangingTek Robotics Technology (Suzhou) Co., Ltd.; Shanghai Yunfan Intelligent Control Robot Technology Co., Ltd.
- <a id="paper-1bad7b8c664a2eb2"></a>**DeepRewind: Predicting and Repairing Premature Commitments in Deep Research Agents** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2609.36344)* · [Paper](https://arxiv.org/abs/2609.36344) · [Code](https://github.com/AmirAbaskohi/DeepRewind)<br>
  Amirhossein Abaskohi et al. · University of British Columbia
- <a id="paper-92174196b7146b88"></a>**Design Anything, Design at Scale** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.24771)* · [Paper](https://arxiv.org/abs/2610.24771) · [Code](https://github.com/Gemus-AI/DesignAnything) · [Dataset](https://huggingface.co/datasets/Gemus-AI/DesignAnything-Bench)<br>
  Xuchao Ren et al. · Tsinghua University; Beijing Institute of Fashion Technology; Massachusetts Institute of Technology; +1 institutions
- <a id="paper-f991937645caaaa5"></a>**DiffResearch: Accelerating Deep Research with Diffusion Language Models** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.28909)* · [Paper](https://arxiv.org/abs/2610.28909) · [Code](https://github.com/alanrbtx/DiffResearch)<br>
  Alan-Barsag Gazzaev, Alexey Gavrilov, Mikhail Mozikov, Sergey Muravyov · ITMO University; AXXX
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
- <a id="paper-d03c4239f891aa34"></a>**Federation over Harness** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.24007)* · [Paper](https://arxiv.org/abs/2610.24007) · [Code](https://github.com/dixiyao/FoH)<br>
  Dixi Yao, Tahseen Rabbani, Tian Li · University of Chicago
- <a id="paper-e14cabb1256a4b15"></a>**Fork-and-Flush: Escaping Idea Basins in Autoresearch Agents** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.07447)* · [Paper](https://arxiv.org/abs/2610.07447)<br>
  Ziyang Cai et al. · Microsoft Research
- <a id="paper-0d8be09c556e897e"></a>**From VLM Planners to Robotic Agents: Self-Evolving Harnesses for History-Dependent Manipulation** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.29560)* · [Paper](https://arxiv.org/abs/2610.29560)<br>
  Tingwen Du et al. · University of Science and Technology of China; Shanghai Artificial Intelligence Laboratory; Shanghai Jiao Tong University; +2 institutions
- <a id="h03"></a>**Harness-1: Reinforcement Learning for Search Agents with State-Externalizing Harnesses** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2606.02373)* · [Paper](https://arxiv.org/abs/2606.02373) · [Code](https://github.com/pat-jj/harness-1) · [HF Model](https://huggingface.co/pat-jj/harness-1) · [HF Dataset](https://huggingface.co/datasets/pat-jj/harness-1-train-data)<br>
  Pengcheng Jiang et al. · University of Illinois Urbana-Champaign; UC Berkeley; Chroma
- <a id="paper-9e49e6d93707d1f6"></a>**Harness^2: Recursive Agent Harnessing for an Open World** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.14224)* · [Paper](https://arxiv.org/abs/2610.14224) · [Code](https://github.com/google-research/harness2) · [Project](https://harness2.github.io/)<br>
  Ruiyao Xu et al. · Northwestern University; Google Cloud AI Research
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
- <a id="paper-1d9cf5babf2989a2"></a>**Librarian Agents: Training LLMs to Curate Long-Context Workspaces that Anticipate Future Queries** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.22273)* · [Paper](https://arxiv.org/abs/2610.22273) · [Project](https://librarian-agents.github.io/) · [Code](https://github.com/teresaz05/librarian-agents)<br>
  Anikait Singh et al. · Stanford University; Carnegie Mellon University
- <a id="paper-79115fb39819fd02"></a>**MaD-RSI: Model-as-Data for Recursive Self-Improvement of Agent Harnesses** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.28201)* · [Paper](https://arxiv.org/abs/2610.28201)<br>
  Yu Cui et al. · Beijing Institute of Technology; Tsinghua University; Chengdu Institute of Computer Applications, Chinese Academy of Sciences; +4 institutions
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
- <a id="paper2agent"></a>**Reimagining research papers as interactive and reliable AI agents** · *[Nature 2026](https://www.nature.com/articles/s41586-026-11044-y)* · [Paper](https://www.nature.com/articles/s41586-026-11044-y) · [Preprint](https://arxiv.org/abs/2509.06917) · [Code](https://github.com/jmiao24/Paper2Agent)<br>
  Jiacheng Miao et al. · Stanford University
- <a id="paper-c97a20989ff958e4"></a>**RIDAR: Safeguarding Research Integrity in Autonomous Research Agents via Automated Detection and Runtime Intervention** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.31372)* · [Paper](https://arxiv.org/abs/2610.31372) · [Code](https://github.com/THU-KEG/RIDAR)<br>
  Jiening Siow et al. · Department of Computer Science and Technology, Tsinghua University; School of Information, Renmin University of China; Zhipu AI
- <a id="robin"></a>**Robin: A multi-agent system for automating scientific discovery** · *[Nature 2026](https://www.nature.com/articles/s41586-026-10652-y)* · [Paper](https://arxiv.org/abs/2505.13400)<br>
  Ali Essam Ghareeb et al. · FutureHouse; University of Oxford
- <a id="paper-c397688c68ae69b3"></a>**RoleFlow: Self-Evolving Multi-Role Agentic Collaboration via Structural Adaptation** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.30429)* · [Paper](https://arxiv.org/abs/2610.30429)<br>
  Yi Ge et al. · University of Maryland, College Park; University of Pittsburgh; The University of Texas at Dallas
- <a id="paper-da0b864f0a61a686"></a>**RouteWeaver: Weaving Mode Selection and Execution into Unified LLM Routing** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.19705)* · [Paper](https://arxiv.org/abs/2610.19705) · [Code](https://github.com/LaughKing/RouteWeaver) · [Project](https://laughking.github.io/RouteWeaver/)<br>
  Xiaohan Wang et al. · Nanyang Technological University; Huazhong University of Science and Technology; University of Illinois Urbana-Champaign
- <a id="paper-5946c006a4e58dd8"></a>**RSIGym: A Flexible Environment for Recursive Self-Improvement** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.10310)* · [Paper](https://arxiv.org/abs/2610.10310) · [Code](https://github.com/evolvent-ai/RSIGym) · [Project](https://rsi-index.ai/)<br>
  Fanqing Meng et al. · Evolvent AI; National University of Singapore
- <a id="paper-09c8b51fd5a44907"></a>**S-Agent 2.0: Spatial Reasoning with a General Coding Agent** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.28354)* · [Paper](https://arxiv.org/abs/2610.28354) · [Project](https://ropedia.github.io/S-Agent-2.0) · [Code](https://github.com/Ropedia/S-Agent-2.0)<br>
  Rui Gong et al. · Nanyang Technological University; University of Hong Kong; Ropedia
- <a id="paper-029806d18c63cad7"></a>**Same Simulation, Different Evidence: Where Retrieved Tool Output Costs LLM Agents Accuracy** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.26836)* · [Paper](https://arxiv.org/abs/2610.26836) · [Code](https://github.com/grenadeComing/same-simulation-different-evidence) · [Dataset](https://huggingface.co/datasets/grenadeComing/same-simulation-different-evidence)<br>
  Ke Zhang et al. · University of California, Riverside; University of California, Irvine
- <a id="paper-38f74d617740ea23"></a>**SEIS: Self-Evolving Inference Systems** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.04646)* · [Paper](https://arxiv.org/abs/2610.04646) · [Project](https://nehzux.github.io/SEIS/) · [Code](https://github.com/smth-fun/self-evolving-inference-system)<br>
  Zhen Xu et al. · University of Chicago
- <a id="paper-644afb0b5cb55eed"></a>**SEPM: Self-Evolving Procedural Memory Grounded in Task Graphs for Multi-Agent Collaboration** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.14515)* · [Paper](https://arxiv.org/abs/2610.14515) · [Code](https://github.com/cookieApril/SEPM)<br>
  Yi Liu et al. · Beijing University of Posts and Telecommunications; China Telecom
- <a id="paper-e3c5bce0180303e4"></a>**Skip the Compressor: Coding Agents Fix More Issues When They Pick Whole Files** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.21073)* · [Paper](https://arxiv.org/abs/2610.21073)<br>
  Xiaocong Yang et al. · University of Illinois Urbana-Champaign
- <a id="paper-7cbe516dd8f1d6f6"></a>**SplatLab: Autonomous Scientific Discovery for 3DGS Research** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.30468)* · [Paper](https://arxiv.org/abs/2610.30468) · [Code](https://github.com/seemandhar/SplatLab) · [Project](https://seemandharjain.com/splatlab/)<br>
  Seemandhar Jain, Manmohan Chandraker · University of California San Diego
- <a id="paper-ef8dd675a4428711"></a>**StopLoss: Teaching Agents to Predict Failure and Stop Early** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.25525)* · [Paper](https://arxiv.org/abs/2610.25525) · [Code](https://github.com/TIGER-AI-Lab/StopLoss) · [Dataset](https://huggingface.co/datasets/TIGER-Lab/StopLoss-Training-Data) · [HF Model](https://huggingface.co/TIGER-Lab/StopLoss-Qwen2.5-7B-Instruct) · [HF Model](https://huggingface.co/TIGER-Lab/StopLoss-Qwen3-8B) · [HF Model](https://huggingface.co/TIGER-Lab/StopLoss-Qwen2.5-Coder-7B-Instruct)<br>
  Jiarong Liang et al. · University of Waterloo
- <a id="paper-65df409d4e89a361"></a>**STRATA: Self-Maintaining Structured Experience Graphs for Self-Evolving Language Agents** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.19386)* · [Paper](https://arxiv.org/abs/2610.19386)<br>
  Guanhua Zhu et al. · New Jersey Institute of Technology; The Chinese University of Hong Kong, Shenzhen
- <a id="paper-94d2abf0fb9eec2d"></a>**TCMScience: An Autonomous Scientist for Traditional Chinese Medicine** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.24601)* · [Paper](https://arxiv.org/abs/2610.24601) · [Code](https://github.com/IMPF-AI-Institute/TCMScience)<br>
  Yanlan Kang et al. · Institute of Medical Philosophy & Future AI (IMPF-AI); Shanghai Medical College, Fudan University; Guangdong Provincial Key Laboratory of New Drug Screening and Guangdong–Hong Kong–Macao Joint Laboratory for New Drug Screening, School of Pharmaceutical Sciences, Southern Medical University; +4 institutions
- <a id="ai-scientist"></a>**The AI Scientist: Towards Fully Automated Open-Ended Scientific Discovery** · *[Nature 2026](https://www.nature.com/articles/s41586-026-10265-5)* · [Paper](https://arxiv.org/abs/2408.06292) · [Code](https://github.com/SakanaAI/AI-Scientist)<br>
  Chris Lu et al. · Sakana AI; University of Oxford; University of British Columbia; +2 institutions
- <a id="paper-3e1d6c58b4640b70"></a>**The Last Remote Sensing Model Built by Humans? Casting Any Earth Observation Task as Recursive Self-Improvement** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.18845)* · [Paper](https://arxiv.org/abs/2610.18845) · [Code](https://github.com/Yokoya-Lab-UTokyo/RSI4EO)<br>
  Sijie Zhao et al. · The University of Tokyo; RIKEN; Stanford University
- <a id="paper-0f5aefdeeb0a0bf5"></a>**VideoEvoHarness: Self Evolving Agent Harness from Unlabeled Videos for Video Understanding** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.15389)* · [Paper](https://arxiv.org/abs/2610.15389) · [Code](https://github.com/Wei-Xin-Xu/VideoEvoHarness)<br>
  Weixin Xu et al. · Institute of Automation, Chinese Academy of Sciences; School of Advanced Interdisciplinary Sciences, University of Chinese Academy of Sciences; School of Computer Science and Communication Engineering, Jiangsu University of Science and Technology; +3 institutions
- <a id="paper-81e562d86820e0f8"></a>**What It Is, Not What It Says: Securing Agentic Browsing Interactions with Web Semantics** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.22697)* · [Paper](https://arxiv.org/abs/2610.22697) · [Code](https://github.com/llm-platform-security/intact) · [Dataset](https://huggingface.co/datasets/umariqbal/web-agent-attack-benchmark)<br>
  Umar Iqbal · Washington University in St. Louis

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
- <a id="paper-025c299892959576"></a>**CoEvo-RSI: When Harnesses Evolve, Which Models Should Follow?** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.25078)* · [Paper](https://arxiv.org/abs/2610.25078) · [Code](https://github.com/SuJQ0722/CoEvo-RSI) · [HF Model](https://huggingface.co/nullptr04/CoEvo-RSI-homebench)<br>
  Jiaqi Su et al. · National University of Singapore; Agency for Science, Technology and Research (A*STAR); SenseTime Group Inc.
- <a id="a03"></a>**Darwin Gödel Machine: Open-Ended Evolution of Self-Improving Agents** · *[ICLR 2026](https://proceedings.iclr.cc/paper_files/paper/2026/hash/aa5f5e6eb6f613ec412f1d948dfa21a5-Abstract-Conference.html)* · [Paper](https://arxiv.org/html/2505.22954v1) · [Code](https://github.com/jennyzzt/dgm) · [Blog](https://sakana.ai/dgm/)<br>
  Jenny Zhang et al. · University of British Columbia; Vector Institute; Sakana AI; +1 institutions
- <a id="paper-b53f2f037fbc3af0"></a>**Data-Centric Recursive Self-Improvement for Navigation via Policy-Synchronized Language-Action Dual Bootstrapping** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.15782)* · [Paper](https://arxiv.org/abs/2610.15782) · [Code](https://github.com/OpenGVLab/RSI-Nav)<br>
  Songze Li et al. · Fudan University; Shanghai AI Laboratory; Harbin Institute of Technology; +6 institutions
- <a id="discoveryrsi"></a>**DiscoveryRSI: Recursively Learning to Discover Valuable Hypotheses** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.23839)* · [Paper](https://arxiv.org/abs/2610.23839) · [Code](https://github.com/Gen-Verse/DiscoveryRSI) · [HF Model](https://huggingface.co/Gen-Verse/DiscoveryRSI-27B) · [HF Dataset](https://huggingface.co/datasets/Gen-Verse/DiscoveryRSI-Hypothesis-Task-Examples) · [HF Collection](https://huggingface.co/collections/Gen-Verse/discoveryrsi) · [Demo](https://foundry-arena.rsi-arena.workers.dev/arena)<br>
  Jianyuan Zhong et al. · PhAI Labs; The Chinese University of Hong Kong; University of Michigan; +13 institutions
- <a id="paper-e10b8d841147a1b9"></a>**Drafting Agents, Not Just Tokens: Speculative Recursive Self-Improvement for Agentic Systems** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.16491)* · [Paper](https://arxiv.org/abs/2610.16491) · [Code](https://github.com/SpecRSI-GPR/SpecRSI)<br>
  Xin Xu et al. · Tencent AMS; Xiaohongshu; University of Chinese Academy of Sciences; +3 institutions
- <a id="paper-4f543aaf09b8e37b"></a>**ECG-RSI: Recursive Self-Improvement through Targeted Electrocardiogram Waveform Evolution** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.17718)* · [Paper](https://arxiv.org/abs/2610.17718) · [Project](https://pork-pay.github.io/ECG-RSI/) · [Project](https://github.com/pork-pay/ECG-RSI)<br>
  Xiaoliang Wang et al. · Zhejiang University; Ant Group; Shanghai Artificial Intelligence Laboratory; +1 institutions
- <a id="paper-ef48cb890dde5a10"></a>**EvoAlloc: A Self-Evolving Resource Allocation Agent for Efficient Program Evolution** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.12086)* · [Paper](https://arxiv.org/abs/2610.12086)<br>
  Yanning Dai et al. · Center of Excellence for Generative AI, King Abdullah University of Science and Technology (KAUST), Thuwal, Saudi Arabia; Sakana AI, Tokyo, Japan
- <a id="paper-d6749ecc14796b6e"></a>**Evolving Agent Interfaces** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.28601)* · [Paper](https://arxiv.org/abs/2610.28601) · [Code](https://github.com/simular-ai/Agent-S)<br>
  Saaket Agashe et al. · University of California, Santa Barbara; Cornell University; Carnegie Mellon University; +1 institutions
- <a id="paper-cc8cdd0ee81ef8b9"></a>**Evolving with Open Worlds: Towards Recursive Self-Improvement for Future Forecasting** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.29784)* · [Paper](https://arxiv.org/abs/2610.29784) · [Project](https://github.com/RUCAIBox/DeepEvolve)<br>
  Zhipeng Chen et al. · Gaoling School of Artificial Intelligence, Renmin University of China; IQuest Research; Nanyang Technological University
- <a id="paper-2d3763112aef5022"></a>**ExpEvolve: Structuring and Reusing Experience for Open-Ended Discovery** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.29303)* · [Paper](https://arxiv.org/abs/2610.29303)<br>
  Yongqiang Chen et al. · MBZUAI; Carnegie Mellon University; TMLR Group, Hong Kong Baptist University; +2 institutions
- <a id="paper-d57ea0fb0cf5ef2f"></a>**GuideEvolve: Self-Evolving Agent Framework with Expert Guidance and 3Ts Mechanisms** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.30017)* · [Paper](https://arxiv.org/abs/2610.30017)<br>
  Meihong Jia, Yasemin Timar, Jonathan Taws · Amazon; Amazon Web Services
- <a id="paper-2870028c1b518506"></a>**HarnessPro: Recursive Harness Self-Improvement with Pareto Optimization for Performance-Cost Trade-offs** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.26770)* · [Paper](https://arxiv.org/abs/2610.26770) · [Code](https://github.com/pzs19/HarnessPro)<br>
  Zhuoshi Pan et al. · Tsinghua University; Z.AI Co., Ltd.; Shanghai Jiao Tong University; +2 institutions
- <a id="h05"></a>**HELIX: Model-Harness Co-evolution for Recursive Self-Improvement** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2608.13951)* · [Paper](https://arxiv.org/abs/2608.13951) · [Code](https://github.com/HKUDS/HELIX)<br>
  Tianyu Fan, Chao Huang · The University of Hong Kong
- <a id="hyperagents"></a>**Hyperagents** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2603.19461)* · [Paper](https://arxiv.org/abs/2603.19461) · [Code](https://github.com/facebookresearch/Hyperagents)<br>
  Jenny Zhang et al. · University of British Columbia; Vector Institute; University of Edinburgh; +4 institutions
- <a id="paper-a721352a4172d790"></a>**Kernel Autoresearch for Open-Ended Model Discovery** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.10394)* · [Paper](https://arxiv.org/abs/2610.10394) · [Code](https://github.com/richardcsuwandi/kernaut) · [Project](https://richardcsuwandi.github.io/kernaut/)<br>
  Richard Cornelius Suwandi, Feng Yin, Kevin Murphy · CUHK-Shenzhen; University of British Columbia
- <a id="paper-02f41708e47efed6"></a>**Large Language Models Meet Bayesian Optimization: Towards Self-evolving Wireless Digital Twins** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.31192)* · [Paper](https://arxiv.org/abs/2610.31192)<br>
  Yingzhuo Sun et al. · KTH Royal Institute of Technology; Data Machine Elite; ˙Izmir Institute of Technology
- <a id="paper-034319a912d1c23e"></a>**MedZERO: Self-Evolving Agents for Open-Ended Medical Reasoning Through Controlled Knowledge Accumulation** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.08327)* · [Paper](https://arxiv.org/abs/2610.08327) · [Code](https://github.com/IcecreamArtist/MedZERO)<br>
  Xilin Dang et al. · The Chinese University of Hong Kong; Zhongshan Hospital; Fudan University; +3 institutions
- <a id="paper-bc10433cad9d513d"></a>**MetaShare: Failure-Aware Collective Self-Improvement for Open-Ended Agents** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.21887)* · [Paper](https://arxiv.org/abs/2610.21887)<br>
  Vishal Bhutani, Prasang Gupta, Sumanth Chundru, Kevin Paul · PricewaterhouseCoopers (PwC)
- <a id="paper-8986b52e03245503"></a>**QD-Rec: Open-Ended Evolution of Recommendations via Quality-Diversity** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.23470)* · [Paper](https://arxiv.org/abs/2610.23470) · [Code](https://github.com/SakanaAI/QD-Rec) · [Project](https://pub.sakana.ai/qd-rec/)<br>
  Takashi Ishida, Taro Makino, Issa Sugiura · Sakana AI
- <a id="paper-e0e322c3332399a4"></a>**R$^2$Orch: Recursive Self-Improvement for Agent Orchestration via Self-Play within a Skill-Internalization Loop** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.22740)* · [Paper](https://arxiv.org/abs/2610.22740) · [Code](https://github.com/beita6969/R2Orch)<br>
  Mingda Zhang et al. · The Chinese University of Hong Kong, Shenzhen; Fudan University; University of Illinois Urbana-Champaign; +2 institutions
- <a id="r-zero"></a>**R-Zero: Self-Evolving Reasoning LLM from Zero Data** · *[ICLR 2026](https://openreview.net/pdf?id=96apU6YzSO)* · [Paper](https://arxiv.org/abs/2508.05004) · [Code](https://github.com/Chengsong-Huang/R-Zero) · [Project](https://chengsong-huang.github.io/R-Zero.github.io/)<br>
  Chengsong Huang et al. · Tencent AI Seattle Lab; Washington University in St. Louis; University of Maryland, College Park; +1 institutions
- <a id="paper-2017be142f7eddde"></a>**Recursive Self-Improvement on a Budget: Scoring Code Edits Before They Run** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.29121)* · [Paper](https://arxiv.org/abs/2610.29121)<br>
  Erfan Darzi, Sree Bhargavi Balija, Sheng He · Harvard University; Massachusetts Institute of Technology; UC San Diego
- <a id="paper-7f79a91ca4549965"></a>**Recursive Self-Improvement through Multi-Agent Self-Supervision** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.12176)* · [Paper](https://arxiv.org/abs/2610.12176) · [Code](https://github.com/SakanaAI/mass) · [Project](https://pub.sakana.ai/mass/)<br>
  Hyunin Lee et al. · UC Berkeley; Sakana AI
- <a id="paper-93034516b473593c"></a>**RSIFlow: Adaptive Self-Improvement Workflows with an Evolving Meta-Agent** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.21791)* · [Paper](https://arxiv.org/abs/2610.21791) · [Code](https://github.com/1HUAN1/RSI-Flow)<br>
  Huan Zhang et al. · Beijing Advanced Innovation Center for Future Blockchain and Privacy Computing; Beihang University; Tsinghua University; +1 institutions
- <a id="paper-26bdab7224d77ff2"></a>**SCOPE: Compiling Natural-Language Policies into Neurosymbolic Predicate Programs** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.31062)* · [Paper](https://arxiv.org/abs/2610.31062) · [Dataset](https://huggingface.co/datasets/Plurai/SCOPE)<br>
  Arnon Mazza, Elad Levi · Plurai
- <a id="paper-54910a6ae6785da1"></a>**Second-Order Problem Solving for Recursive Self-Improvement in Formal Verification** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.05701)* · [Paper](https://arxiv.org/abs/2610.05701)<br>
  Yuxuan Jiang, Aditya Vempaty, Ashish Jagmohan · University of Maryland, Baltimore County; Emergence AI
- <a id="paper-589ac49b04a690ec"></a>**Selection Is Not Learning: Choosing Model Futures** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.22029)* · [Paper](https://arxiv.org/abs/2610.22029)<br>
  Haoyi Yang, Kshitij Mishra, Nils Lukas, Salem Lahlou · Mohamed bin Zayed University of Artificial Intelligence
- <a id="self-hpo"></a>**Self-Evolving Coding Agents via Harness-Policy Optimization** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.22791)* · [Paper](https://arxiv.org/abs/2610.22791) · [Code](https://github.com/MSR-Orchard/Self-HPO) · [HF Model (Self-HPO)](https://huggingface.co/self-hpo/Self-HPO-Qwen3.5-35B-A3B) · [HF Model (HPO)](https://huggingface.co/self-hpo/HPO-Qwen3.5-35B-A3B)<br>
  Zhepei Wei et al. · Microsoft Research; University of Virginia; Carnegie Mellon University
- <a id="paper-2f2697994fe0d1fe"></a>**Self-Evolving Visual Agent via Margin Reward** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.15084)* · [Paper](https://arxiv.org/abs/2610.15084) · [Code](https://github.com/YWenxi/marvo)<br>
  Wenxi Yang et al. · UCAS; Microsoft Research Asia; Beihang University
- <a id="swarmrsi"></a>**SwarmRSI: Recursive Self-Improvement through Evolving Scientific Agent Swarm** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.20431)* · [Paper](https://arxiv.org/abs/2610.20431)<br>
  Qianru Meng et al. · Huawei Technologies Co., Ltd.; Leiden University; University of Groningen
- <a id="paper-bb5599a8f4dfd40c"></a>**Towards Robust Prehensile Manipulation in Open-Ended Environments** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.06376)* · [Paper](https://arxiv.org/abs/2610.06376)<br>
  Mathilde Kappel et al. · Sorbonne Universit´e; CNRS; Institut des Syst`emes Intelligents et de Robotique (ISIR)
- <a id="paper-ee825def7bc9147c"></a>**VERSE: Verified Self-Evolving Optimizer for Agent Harnesses** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.02616)* · [Paper](https://arxiv.org/abs/2610.02616) · [Code](https://github.com/wzekai/VERSE)<br>
  Zekai Wang et al. · MIT; Amazon
- <a id="paper-1e6847de2c470a1b"></a>**VideoHarness-SRSI: Structured Recursive Self-Improvement for Video Understanding Harness** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.19424)* · [Paper](https://arxiv.org/abs/2610.19424) · [Project](https://zihaolinqz.github.io/VHarness-SRSI/)<br>
  Zihao Lin et al. · University of California, Davis; Duke University; University of Illinois at Urbana-Champaign; +3 institutions
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
- <a id="exploration-narrowing"></a>**AI Research Agents Narrow Scientific Exploration** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2605.27905)* · [Paper](https://arxiv.org/abs/2605.27905)<br>
  Yixuan Tang, Yi Yang · The Hong Kong University of Science and Technology
- <a id="paper-118197ae3e94acd7"></a>**AnyGoal: On World Model Generalization Beyond Expert Rollouts** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.26844)* · [Paper](https://arxiv.org/abs/2610.26844) · [Project](https://hazel-heejeong-nam.github.io/anygoal/) · [Code](https://github.com/galilai-group/AnyGoal)<br>
  Heejeong Nam et al. · Brown University; Cold Spring Harbor Laboratory; Mila, Universit´e de Montr´eal; +1 institutions
- <a id="paper-31ad9246f9a10e34"></a>**Are We Measuring Scientific Intelligence? Rethinking the Evaluation of AI Scientists** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.04915)* · [Paper](https://arxiv.org/abs/2610.04915)<br>
  Kate Zhang, Yuante Li · Carnegie Mellon University
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
- <a id="paper-13a316d3fa2ce54f"></a>**Benchmarking and Enhancing Agentic Causal Discovery** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.22846)* · [Paper](https://arxiv.org/abs/2610.22846)<br>
  Pingchuan Ma, Rui Ding, Shuai Wang · Zhejiang University of Technology; Microsoft; The Hong Kong University of Science and Technology
- <a id="paper-31224f0f7655c123"></a>**Benchmarking and Error Analysis of Deep Search and Deep Research LLM Agents** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.29346)* · [Paper](https://arxiv.org/abs/2610.29346)<br>
  Zixuan Yu, Zhenheng Tang, Xiaowen Chu, Bo Han · School of Computer science and engi-
neering, Sun Yat-sen University; CSE, The Hong Kong University of Science and Technology; DSA Thrust, The Hong Kong Uni-
versity of Science and Technology (GuangZhou); +1 institutions
- <a id="paper-3abe80f754180570"></a>**Beyond Better Ideas: How Human-AI Collaboration Shapes Scientific Ideas and Human Perceptions** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.30568)* · [Paper](https://arxiv.org/abs/2610.30568)<br>
  Qian Chen et al. · The Pennsylvania State University; Harvard University; Arizona State University; +1 institutions
- <a id="paper-66cadadf2737fc2b"></a>**Beyond Watching and Searching: Benchmarking Agents for Video-centered Deep Research Reports** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.31158)* · [Paper](https://arxiv.org/abs/2610.31158) · [Code](https://github.com/Multimedia-Semantic-Analytics-Lab/OmniDR-Bench) · [Dataset](https://huggingface.co/datasets/marinero4972/OmniDR-Bench)<br>
  Jiahao Meng et al. · Peking University; Alibaba Token Hub, Alibaba Group; Independent Researcher; +1 institutions
- <a id="paper-ecf2a0572888b64b"></a>**BlenderWorld: Benchmarking Visual Agents for 3D Creation from Real-World References** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.23986)* · [Paper](https://arxiv.org/abs/2610.23986) · [Project](https://blenderworld.github.io/) · [Code](https://github.com/QwenLM/BlenderWorld) · [Dataset](https://huggingface.co/datasets/Qwen/BlenderWorld)<br>
  Xinyu Fang et al. · Zhejiang University; Alibaba Token Hub, Alibaba Group; The Chinese University of Hong Kong; +2 institutions
- <a id="c11"></a>**CausaLab: A Scalable Environment for Interactive Causal Discovery Toward AI Scientists** · *[arXiv 2026 (preprint)](https://arxiv.org/html/2605.26029v2)* · [Paper](https://arxiv.org/html/2605.26029v2)<br>
  Junlin Yang et al. · Tsinghua University; University of Illinois Urbana-Champaign; Carnegie Mellon University; +2 institutions
- <a id="paper-e461db7393754058"></a>**CellTrack-Bench: Microscopic Cell Tracking Benchmark for Vision-Language Models** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.31566)* · [Paper](https://arxiv.org/abs/2610.31566) · [Code](https://github.com/royerlab/celltrack-bench)<br>
  Ilan Theodoro, Jordão Bragantini, Loïc A. Royer · Biohub
- <a id="paper-6e3e2ae7454ba2f5"></a>**Competence-Based Evaluation of Logical Reasoning in Large Language Models** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.22894)* · [Paper](https://arxiv.org/abs/2610.22894) · [Dataset](https://huggingface.co/datasets/jizej/Competence-Based-Evaluation)<br>
  Jize Jiang, Chengxiang Zhai · University of Illinois Urbana-Champaign
- <a id="paper-8b5e7afcd33dcbed"></a>**Data World: Scaling Data Environments from Scratch** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.21656)* · [Paper](https://arxiv.org/abs/2610.21656) · [Code](https://github.com/Zhanli-Li/Data-World) · [Project](https://zhanli-li.github.io/Data-World/) · [Dataset](https://huggingface.co/datasets/Zhanli-Li/DataWorld-Bench) · [Dataset](https://huggingface.co/collections/Zhanli-Li/dataworld) · [HF Model](https://huggingface.co/Zhanli-Li/DataWorld-35B-A3B)<br>
  Zhanli Li et al. · School of Artificial Intelligence; National Key Laboratory for Novel Software Technology, Nanjing University; Longcat Interaction Team, Meituan; +7 institutions
- <a id="paper-ec30270490ea6cac"></a>**DataSense-Bench: The First Step Toward an AI Scientist** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.12190)* · [Paper](https://arxiv.org/abs/2610.12190) · [Code](https://github.com/DataSense-Bench/DataSense-Bench) · [Project](https://datasense-bench.github.io/)<br>
  Yudi Zhang et al. · Eindhoven University of Technology; University of Surrey; ELLIS Institute T¨ubingen; +2 institutions
- <a id="paper-50d8cd71040f538b"></a>**DecisionPivot: A Diagnostic Benchmark for Decision Models in LLM Systems** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.28522)* · [Paper](https://arxiv.org/abs/2610.28522) · [Code](https://github.com/StartLuxLabs/DecisionPivot) · [Dataset](https://huggingface.co/datasets/startlux-models/DecisionPivot)<br>
  Xialie Zhuang et al. · StartLux
- <a id="paper-d26e59a1cb2b6340"></a>**Deep Search in Real-World Web Environments** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.30181)* · [Paper](https://arxiv.org/abs/2610.30181) · [Code](https://github.com/Yu-xm/OpenDS) · [Dataset](https://huggingface.co/datasets/Yu2020/OpenDS-World)<br>
  Xiaomin Yu et al. · HKUST(GZ); FDU; UW; +11 institutions
- <a id="discern"></a>**DISCERN: Can AI Agents Work Like Scientists and Guide Discovery?** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2609.33357)* · [Paper](https://arxiv.org/abs/2609.33357) · [HF Dataset](https://huggingface.co/datasets/discern-bench-anon/discern-benchmark)<br>
  Nan Huang et al. · University of California San Diego
- <a id="paper-e15c7d3de5e7f265"></a>**DrugTargetWorld: A Synthetic Biobank for Training and Benchmarking AI Scientists** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.09558)* · [Paper](https://arxiv.org/abs/2610.09558) · [Code](https://github.com/sammargolis/DrugTargetWorld) · [Project](https://drugtargetworld.vercel.app/) · [Dataset](https://huggingface.co/datasets/sammargolis/drugtargetworld-assets)<br>
  Samuel Margolis et al. · Stanford University; Brown University
- <a id="paper-105b4672ff4fd27c"></a>**EdgeKernelBench: Unified LLM-Driven Kernel Generation for Edge Backends** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.24648)* · [Paper](https://arxiv.org/abs/2610.24648) · [Project](https://pillor9.github.io/EdgeKernelBench/) · [Code](https://github.com/pillor9/EdgeKernelBench)<br>
  Yuhua Zheng et al. · Westlake University; Zhejiang University
- <a id="paper-97aa05f1d051eb67"></a>**EmbodiedCLBench: Evaluating Continual Learning for Self-Evolving Embodied Agents** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.13021)* · [Paper](https://arxiv.org/abs/2610.13021) · [Project](https://pku-value-lab.github.io/EmbodiedCLBench-homepage) · [Code](https://github.com/PKU-VaLuE-Lab/EmbodiedCLBench) · [Dataset](https://huggingface.co/datasets/PKU-VaLuE-Lab/EmbodiedCLBench)<br>
  Jie Huang et al. · School of Intelligence Science and Technology, Peking University; State Key Laboratory of General Artificial Intelligence, BIGAI, Beijing, China; University of Hong Kong
- <a id="paper-1663c6679dab72c8"></a>**EvalResearchBench: Can AI Agents Build Their Own Feedback for Recursive Self-Improvement?** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.04184)* · [Paper](https://arxiv.org/abs/2610.04184) · [Project](https://mercury7353.github.io/self-evaluation-bench/) · [Code](https://github.com/Mercury7353/self-evaluation-bench)<br>
  Yaolun Zhang et al. · Oregon State University; University of California, San Diego; Pennsylvania State University; +1 institutions
- <a id="paper-ff655bd3f5066c0f"></a>**EvaOmni: An Evidence-Grounded Benchmark for Audio-Visual Reasoning** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.28444)* · [Paper](https://arxiv.org/abs/2610.28444) · [Code](https://github.com/VisionXLab/EvaOmni) · [Dataset](https://huggingface.co/datasets/VisionXLab/EvaOmni-Dataset)<br>
  Xiaoxing Hu et al. · Shanghai Jiao Tong University; Shanghai Innnovation Institute; Inner Mongolia University of Technology; +7 institutions
- <a id="paper-dd2dc379979e7af0"></a>**From Scientific Observations to Mechanisms: Benchmarking Hypothesis Generation by AI Scientists** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.05197)* · [Paper](https://arxiv.org/abs/2610.05197)<br>
  Xiaxun Xie et al. · Computer Network Information Center, Chinese Academy of Sciences; National University of Singapore; Sichuan University
- <a id="paper-72af933c20feb3a7"></a>**FrontierCS 2: A Benchmark for Computer Science R&D** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.29932)* · [Paper](https://arxiv.org/abs/2610.29932) · [Code](https://github.com/FrontierCS/FrontierCS-2) · [Project](https://frontier-cs.org/)<br>
  Qiuyang Mang et al. · UC Berkeley; Princeton University; University of Waterloo; +16 institutions
- <a id="paper-7b88221edcfc1946"></a>**GameBoyWorlds: A Testbed for Self-Improvement in Embodied Video Games** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2609.32093)* · [Paper](https://arxiv.org/abs/2609.32093) · [Code](https://github.com/DhananjayAshok/GameBoyWorlds-Benchmark) · [Code](https://github.com/DhananjayAshok/GameBoyWorlds)<br>
  Dhananjay Ashok et al. · Information Sciences Institute, University of Southern California; Columbia University; University of Chicago; +2 institutions
- <a id="paper-c8f0a1e7ad6a901d"></a>**GlobeBench: Evaluating Text-Based World Model Capabilities for Scalable Environment Simulations** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.22708)* · [Paper](https://arxiv.org/abs/2610.22708) · [Code](https://github.com/patronus-ai/globebench) · [Dataset](https://huggingface.co/datasets/PatronusAI/globebench)<br>
  Nicholas Saban, Charvi Bannur, Mariya Vasileva, Darshan Deshpande · Patronus AI
- <a id="paper-d3835393933ca7ee"></a>**HSPR: Recovering Software-Agent Benchmark Scores via Hierarchical Posterior Inference** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.24611)* · [Paper](https://arxiv.org/abs/2610.24611) · [Project](https://wanyichen06.github.io/HSPR/) · [Code](https://github.com/wanyichen06/HSPR)<br>
  Wanyi Chen et al. · Soochow University; Singapore Management University
- <a id="into-the-unknown"></a>**Into the Unknown: Benchmarking AI agents on open scientific research problems** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.19159)* · [Paper](https://arxiv.org/abs/2610.19159) · [Code](https://github.com/prometheus-eval/into-the-unknown) · [Project](https://prometheus-eval.github.io/into-the-unknown/viewer/) · [HF Dataset](https://huggingface.co/datasets/prometheus-eval/into-the-unknown)<br>
  Seungone Kim et al. · Carnegie Mellon University; University of Minnesota; Stanford University; +13 institutions
- <a id="paper-d413c98db0f6141e"></a>**MMEnterprise-Bench: Evaluating Enterprise Agents over Evolving Multimodal Records** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.27911)* · [Paper](https://arxiv.org/abs/2610.27911) · [Project](https://mlvlab.github.io/MMEnterprise-Bench/) · [Code](https://github.com/mlvlab/MMEnterprise-Bench)<br>
  Seohyun Lee et al. · KAIST; Korea University
- <a id="paper-aa059e79208dfb82"></a>**MMPostTrainBench: Benchmarking Autonomous Research for Multimodal Post-Training** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.05398)* · [Paper](https://arxiv.org/abs/2610.05398) · [Code](https://github.com/sod1010/MMPostTrainBench)<br>
  Yuxin Liu et al. · University of Science and Technology of China; Alibaba Token Hub, Alibaba Group; University of the Chinese Academy of Sciences; +2 institutions
- <a id="d03"></a>**NewtonBench: Benchmarking Generalizable Scientific Law Discovery in LLM Agents** · *[ICLR 2026](https://proceedings.iclr.cc/paper_files/paper/2026/hash/a0e1c2c40fc245b5fe7251ea33fbb045-Abstract-Conference.html)* · [Paper](https://arxiv.org/abs/2510.07172) · [Code](https://github.com/HKUST-KnowComp/NewtonBench)<br>
  Tianshi Zheng et al. · HKUST; NVIDIA
- <a id="paper-12a4904af7aa0825"></a>**On Open-Ended Information Seeking for Information Elicitation Agents** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.07509)* · [Paper](https://arxiv.org/abs/2610.07509) · [Code](https://github.com/infosenselab/open-elicitation) · [Dataset](https://huggingface.co/datasets/infosense/open-elicitation-trajectories)<br>
  Victor De Lima, Grace Hui Yang · Georgetown University
- <a id="paper-03406ae2f3bae7d2"></a>**On the Fragility of Tasks under Composition: Implicit Budgeting in Language Models** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.27190)* · [Paper](https://arxiv.org/abs/2610.27190) · [Project](https://chenpanli.github.io/fragility) · [Code](https://github.com/chenpanli/fragility)<br>
  Chenpan Li et al. · TU Munich; MIT CSAIL
- <a id="paper-bc9b70a35a8d90a3"></a>**OpenSocialJax: Evaluating Social Adaptation in Sequential Social Dilemmas with Open-Ended Environmental Dynamics** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.13710)* · [Paper](https://arxiv.org/abs/2610.13710) · [Code](https://github.com/cooperativex/OpenSocialJax)<br>
  Zihao Guo, Meng Fang, Joel Z. Leibo, Yali Du · King’s College London; University of Liverpool; The Alan Turing Institute; +1 institutions
- <a id="paper-5d861400b2f29a95"></a>**OR-License: Evaluating LLM Agents as Real-World Operations Research Practitioners** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.24087)* · [Paper](https://arxiv.org/abs/2610.24087) · [Code](https://github.com/NineAbyss/OR-License) · [Dataset](https://huggingface.co/datasets/OR-License/OR-License)<br>
  Peisong Wang et al. · HKUST-GZ; HKU; Qingzhi Optimization (Jinan) Information Technology Co., Ltd.; +6 institutions
- <a id="paper-0d36244bb44988af"></a>**Pre-Registered Genesis Accounting for Recursive Self-Improvement: First Audited Operator-Genesis Events in a Physics-Discovery Runtime** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.14843)* · [Paper](https://arxiv.org/abs/2610.14843)<br>
  Wenbin Mao, Pei Zou · HoomanBio AI Lab, Huaman Biotechnology (Beijing) Co., Ltd.
- <a id="paper-dcda595d5edb15af"></a>**PVBench: Quantifying Physical Plausibility in Video Generation with Object-Level Physical Measurements** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.26711)* · [Paper](https://arxiv.org/abs/2610.26711) · [Code](https://github.com/KSZG-11/PVBench) · [Project](https://kszg-11.github.io/PVBench-Website/)<br>
  Kaiwei Chen et al. · APRIL Lab, Zhejiang University; Huazhong University of Science and Technology; Tencent Youtu Lab
- <a id="paper-045c2b8bd847ae46"></a>**Quant-Arena: Benchmarking LLM Agents for Quantitative Trading Research** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.30113)* · [Paper](https://arxiv.org/abs/2610.30113) · [Project](https://lab.einsia.ai/quant-arena/)<br>
  Houde Qian et al. · Navers Lab; Einsia.AI
- <a id="paper-d4e79e43099df1b8"></a>**ResearchFlow-Eval: Tracing the Execution Gap in End-to-End Multi-Claim Autoresearch** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.18088)* · [Paper](https://arxiv.org/abs/2610.18088) · [Code](https://github.com/Jp-17/ResearchFlow-Eval)<br>
  Peng Jiang, Dongyang Li, Quanying Liu, Xiaoxuan Jia · Center for Life Sciences and Artificial Intelligence, School of Life Sciences, Tsinghua University, Beijing, China; IDG/McGovern Institute for Brain Research, Tsinghua University, Beijing, China; Tsinghua-Peking Center for Life Sciences, Tsinghua University, Beijing, China; +2 institutions
- <a id="paper-ee84b521258fee34"></a>**Retrieval Augmented Generation Compositionality** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.29722)* · [Paper](https://arxiv.org/abs/2610.29722) · [Code](https://github.com/dolev31/lasagna) · [Project](https://dolev31.github.io/lasagna/)<br>
  Ido Levy, Segev Shlomov, Leshem Choshen · IBM; Weizmann Institute of Science
- <a id="paper-b92b08173531b188"></a>**RSI-Forge: From Research Papers to Environments for Recursive Self-Improvement** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.09426)* · [Paper](https://arxiv.org/abs/2610.09426)<br>
  Renxiong Wang et al. · Scale AI; University of California, Santa Cruz; University of North Carolina at Chapel Hill
- <a id="paper-f73eeee30c4bf920"></a>**Sci$Π$vot: Benchmarking Principal-Investigator Judgment at Pivotal Moments of Scientific AutoResearch Agents** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.21082)* · [Paper](https://arxiv.org/abs/2610.21082) · [Code](https://github.com/AutoResearch-Factory/SciPIvot) · [Project](https://autoresearch-factory.github.io/SciPIvot/) · [Dataset](https://huggingface.co/datasets/sun1245/SciPIvot)<br>
  Youran Sun et al. · University of Maryland, College Park; The Chinese University of Hong Kong; Gradient Network; +3 institutions
- <a id="science-gym"></a>**Science-Gym: a simple testbed for AI-driven scientific discovery** · *[Machine Learning 2026](https://link.springer.com/article/10.1007/s10994-025-06914-x)* · [Paper](https://link.springer.com/article/10.1007/s10994-025-06914-x) · [Code](https://github.com/pibborn/science-gym)<br>
  Mattia Cerrato et al. · Johannes Gutenberg University Mainz; TU Darmstadt and hessian.AI; Max Planck Institute for Polymer Research; +2 institutions
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
- <a id="paper-1b71ddb115ba5e37"></a>**The Scientific Research Taste Benchmark (SciTaste-Bench): A Multi-Disciplinary Benchmark for Assessing Large Language Models' Judgment of Research Taste in Scientific Papers** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.28653)* · [Paper](https://arxiv.org/abs/2610.28653)<br>
  Xinyi Gao et al. · University of Chinese Academy of Sciences; Alibaba Group; Tsinghua University
- <a id="paper-644098a7aa74502f"></a>**VerifierBench: Benchmarking the Generation of Executable Verifiers for LLM Agents** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.28679)* · [Paper](https://arxiv.org/abs/2610.28679) · [Project](https://verifierbench.github.io/) · [Dataset](https://huggingface.co/datasets/Catherine1213/VerifierBench) · [Code](https://github.com/DwanZhang-AI/verifier-suite)<br>
  Jianing Yin et al. · University of Pennsylvania; University of Illinois at Urbana-Champaign; University of California, Berkeley; +2 institutions
- <a id="paper-282f8f39baa392ae"></a>**VibeTraining-Bench: Data-Trainer-Harness Co-Design for Iterative System Improvement** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.26342)* · [Paper](https://arxiv.org/abs/2610.26342)<br>
  Ruotian Peng et al. · Zhejiang University; Westlake University; Alibaba Token Hub, Alibaba Group; +2 institutions
- <a id="paper-1313ca747d97581e"></a>**VX-One: Typed, Calibrated Decision Heads for Real-Time Perimeter Triage - An empirical study of unknown-attack honesty, cascade gray zones, and calibration under drift** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.30090)* · [Paper](https://arxiv.org/abs/2610.30090)<br>
  Juan S. Santillana · Independent research
- <a id="paper-4f6e0f0aac76178e"></a>**Where is Physical RSI capability from? An Observational Scaling Law of LLM-as-policy** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.26848)* · [Paper](https://arxiv.org/abs/2610.26848) · [Project](https://physrsi-eval.github.io/)<br>
  Zekai Li et al. · Galbot Team

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
