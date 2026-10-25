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
  <a href="#contents"><img src="https://img.shields.io/badge/works-243-2563eb?style=flat-square" alt="243 curated works"></a>
  <a href="docs/benchmarks.md"><img src="https://img.shields.io/badge/environment_profiles-49-0f766e?style=flat-square" alt="49 environment profiles"></a>
  <a href="CONTRIBUTING.md"><img src="https://img.shields.io/badge/contributions-welcome-7c3aed?style=flat-square" alt="Contributions welcome"></a>
</p>

<p align="center">
  <a href="https://owd-ai.github.io/awesome-open-world-discovery/">Research observatory ↗</a> · <a href="#what-is-owd">What is OWD?</a> · <a href="#why-owd">Why this focus?</a> · <a href="#updates">Latest papers</a> · <a href="#contents">Browse the list</a> · <a href="CONTRIBUTING.md">Contribute</a>
</p>

<p align="center"><sub>Literature checked through 2026-10-24 · Papers, author blogs, code, and benchmarks</sub></p>

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

The latest 10 source-checked papers from our daily monitor · Updated 2026-10-24.

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
| 📚 [Discovery Foundations](#foundations) | What constitutes a discovery? | 19 |
| 🧩 [Discovery Representations](#causality) | What representations enable discovery? | 30 |
| 🔬 [Discovery Reasoning](#sci_methods) | How should agents formulate and test hypotheses? | 24 |
| 🧠 [Discovery Training](#learning) | How can we train agents to discover? | 33 |
| 🔄 [Continual Discovery](#adaptation) | How can agents learn from ongoing investigations? | 34 |
| 🛠️ [Discovery Systems](#systems) | How can we build reliable discovery systems? | 40 |
| 🌱 [Open-Ended Discovery](#open_ended) | How can agents expand the scope of discovery? | 23 |
| 📊 [Discovery Evaluation](#benchmarks) | How can we measure progress in discovery? | 40 |

[🔗 Related lists](#related) · [🤝 Contributing](#contributing)

Each work appears once under its primary contribution; see the [classification guide](docs/taxonomy.md#categories) for category scopes. Entries are grouped by publication year, newest first. Each work keeps its paper, code, project, and dataset links together, followed by authors and paper-time affiliations. Full attribution is recorded in the [catalog data](data/resources.json).

<a id="foundations"></a>

## 📚 Discovery Foundations

*What constitutes a discovery?*

### 2026

- <a id="self-evolving-survey"></a>**A Survey of Self-Evolving Agents: What, When, How, and Where to Evolve on the Path to Artificial Super Intelligence** · *[TMLR 2026](https://openreview.net/pdf?id=CTr3bovS5F)* · [Paper](https://arxiv.org/abs/2507.21046) · [List](https://github.com/CharlesQ9/Self-Evolving-Agents)<br>
  Huan-ang Gao et al. · Princeton University; Princeton AI Lab; Tsinghua University; +14 institutions
- <a id="causal-agents"></a>**Causal Discovery in the Era of Agents** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2606.23608)* · [Paper](https://arxiv.org/abs/2606.23608)<br>
  Yujia Zheng et al. · Carnegie Mellon University; Mohamed bin Zayed University of Artificial Intelligence
- <a id="paper-7fabe26ca5c43e1f"></a>**Co-Recursive Semantic Self-Extension: A Mathematical Foundation for Open-Ended Intelligence** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.31097)* · [Paper](https://arxiv.org/abs/2610.31097)<br>
  Simon Hegelich et al. · GaiaLogic Unipessoal Lda.; Nanyang Technological University, Singapore; University of Macau
- <a id="discovery-foundation-models"></a>**Discovery Foundation Models: Toward Open-Ended Discovery Intelligence** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2609.15973)* · [Paper](https://arxiv.org/abs/2609.15973) · [Research resources](https://github.com/Gen-Verse/DFM-Plans) · [Project](https://phai-labs.com/collaborate/)<br>
  Ling Yang, Zhenfei Yin, Yingcheng Wu · DFM Scientist Collaboration Program
- <a id="paper-cc26871dfb8c52d0"></a>**Memory-Centric Continual Learning for AI Agents** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.29357)* · [Paper](https://arxiv.org/abs/2610.29357)<br>
  Dongfang Li et al. · Harbin Institute of Technology (Shenzhen), Shenzhen, China; Shenzhen Loop Area Institute, Shenzhen, China; Tsinghua University, Beijing, China; +3 institutions
- <a id="paper-51ce772b7b376b84"></a>**Modeling Authentic Research Trajectories: A Graph View of Research Ideation** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.27337)* · [Paper](https://arxiv.org/abs/2610.27337)<br>
  Ruochen Li, Zhiyu Chen · University of Texas at Dallas
- <a id="paper-1178f409c73ca56a"></a>**Multimodal Embodied Agents: A Unified Capability-centric Perspective from Computer-Use to Robot-Use** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.30108)* · [Paper](https://arxiv.org/abs/2610.30108) · [Project](https://showlab.github.io/Awesome-Multimodal-Embodied-Agent)<br>
  Yanzhe Chen et al. · Show Lab, National University of Singapore
- <a id="paper-dfbccdacbb319eab"></a>**Reading, Writing, Sharing, and Interacting with the World through Video** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.31668)* · [Paper](https://arxiv.org/abs/2610.31668) · [Project](https://vid-gen.github.io/video-world-model-survey) · [Code](https://github.com/vid-gen/awesome-video-world-model)<br>
  Shengqiong Wu et al. · University of Oxford; NUS; NTU; +1 institutions
- <a id="paper-1e60f285c8164f89"></a>**Toward Recursive Self-Improvement in Physical AI** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.29677)* · [Paper](https://arxiv.org/abs/2610.29677) · [Project](https://physical2rsi.github.io) · [Code](https://github.com/Physical2RSI/Awesome-Physical2RSI)<br>
  Meng Luo et al. · National University of Singapore; Huazhong University of Science and Technology; Shanghai Jiao Tong University; +2 institutions

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
- <a id="paper-5bbfa21913204559"></a>**Agentic World Action Models** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.30136)* · [Paper](https://arxiv.org/abs/2610.30136) · [Project](https://agentic-wam.github.io/)<br>
  Zhuoyang Liu et al. · UC Berkeley; NVIDIA; University of Pennsylvania
- <a id="paper-d5842cf69174cd5a"></a>**ALPS: Visual State Encoders for World Models** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.30120)* · [Paper](https://arxiv.org/abs/2610.30120) · [Code](https://github.com/UCSC-VLAA/ALPS) · [Project](https://ucsc-vlaa.github.io/ALPS) · [HF Model](https://huggingface.co/UCSC-VLAA/ALPS)<br>
  Yanqing Liu et al. · University of California, Santa Cruz; Google; University of California, Santa Barbara
- <a id="paper-5a683d7a781fb5bd"></a>**Causal Discovery for Linear Models with Latent Confounding via Multi-domain Identifiable Representation Learning** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.28134)* · [Paper](https://arxiv.org/abs/2610.28134)<br>
  Danru Xu, Aapo Hyv¨arinen, Sara Magliacane · University of Amsterdam; University of Helsinki; Saarland University
- <a id="cider-fm"></a>**CIDER-FM: Foundation Models for Causal Inference from Diverse Experimental Regimes** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2609.39523)* · [Paper](https://arxiv.org/abs/2609.39523)<br>
  Yuche Gao et al. · University of Cambridge; Max Planck Institute for Intelligent Systems; Prior Labs; +3 institutions
- <a id="paper-cff6e82a848858e5"></a>**Identifying ODEs from Unstructured Data with Causal Representation Learning** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2609.37083)* · [Paper](https://arxiv.org/abs/2609.37083)<br>
  Alessandro Trenta, Riccardo Massidda, Davide Bacciu, Sara Magliacane · University of Pisa; Saarland Informatics Campus; Saarland University; +1 institutions
- <a id="paper-4f0706d28b33b8b2"></a>**Language Models as AI Research World Models** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.12235)* · [Paper](https://arxiv.org/abs/2610.12235)<br>
  Zijun Wang et al. · Amazon; UC Santa Cruz; Emory University; +2 institutions
- <a id="paper-994c8a84ad65793d"></a>**Looking Ahead: Modeling Future Evolution in Autoregressive Video Generation** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.29989)* · [Paper](https://arxiv.org/abs/2610.29989) · [Code](https://github.com/TencentARC/Looking-Ahead) · [Project](https://hellorpg.github.io/looking-ahead/) · [HF Model](https://huggingface.co/TencentARC/Looking-Ahead) · [Dataset](https://huggingface.co/datasets/TencentARC/Looking-Ahead)<br>
  Ruopeng Gao et al. · Nanjing University; ARC Lab, Tencent IEG; Zhejiang University
- <a id="paper-87bd413320e9c2f6"></a>**Not All Features Are Created Equal: A Mechanistic Study of Vision-Language-Action Models** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2603.19233)* · [Paper](https://arxiv.org/abs/2603.19233) · [Code](https://github.com/CWRU-AISM/action-atlas) · [Project](https://cwru-aism.github.io/vla-interp-page/) · [Project](https://action-atlas.com/)<br>
  Bryce Grant, Xijia Zhao, Peng Wang · Case Western Reserve University
- <a id="paper-a77e0de913ae3ba2"></a>**Residual-Based Causal Discovery via Pretrained In-Context Quantile Regression** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.29530)* · [Paper](https://arxiv.org/abs/2610.29530) · [Code](https://github.com/causality-lab/loscar)<br>
  Daniel Klippert, Quang Nhat Huynh, Alexander Marx · TU Dortmund University; Research Center Trustworthy Data Science and Security, University Alliance Ruhr; University of M¨unster
- <a id="paper-3d80f1abd6ff2ffd"></a>**ScaleNav: Scalable Internet Video Pretraining for Language-Conditioned Local Navigation** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.25690)* · [Paper](https://arxiv.org/abs/2610.25690) · [Project](https://zju3dv.github.io/ScaleNav/) · [Code](https://github.com/MachEmbodied/ScaleNav)<br>
  Yihui Yang et al. · Zhejiang University; Li Auto Inc.; Shenzhen University
- <a id="paper-9f6561b2a28884a6"></a>**SCDM: Scalable Causal Discovery in Nonlinear Temporal Systems with Meta-Learning** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.29992)* · [Paper](https://arxiv.org/abs/2610.29992) · [Project](https://shaogangren.github.io/SCDM/) · [Code](https://github.com/ShaogangRen/SCDM)<br>
  Jingbo Wang, Kegeng Tang, Zihao Wang, Shaogang Ren · University of Tennessee at Chattanooga
- <a id="paper-ff5ed4b91b994247"></a>**Skeleton-Grounded Latent Action Model for Robot World Models** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.31474)* · [Paper](https://arxiv.org/abs/2610.31474) · [Project](https://aopolin-lv.github.io/SkeLAM/)<br>
  Qi Lv et al. · HIT (Shenzhen); Show Lab, NUS; Ping An Tech
- <a id="paper-9689553423421d52"></a>**State World Models: Execute the Rules, Generate the Pixels** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.26811)* · [Paper](https://arxiv.org/abs/2610.26811) · [Code](https://github.com/Zhangyr2022/StateWorldModel) · [Project](https://ivg-yanranzhang.github.io/StateWorldModel/) · [Dataset](https://huggingface.co/datasets/Louis0411/StateWorldModel)<br>
  Chan Yan Ki et al. · Department of Automation, Tsinghua University, China; GigaAI
- <a id="paper-cf2e288d5f7302fd"></a>**VCLMU: Mechanism-Centric Virtual Cell World Modeling for Perturbation Response** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.04475)* · [Paper](https://arxiv.org/abs/2610.04475)<br>
  Yuwei Miao et al. · Johnson & Johnson Innovative Medicine; University of Texas at Arlington
- <a id="paper-6057a7437a99f1c3"></a>**Vision-Language-Delta-Action: Learning Compact Deltas as Actionable Transition Interfaces for Robotic Manipulation** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.25874)* · [Paper](https://arxiv.org/abs/2610.25874) · [Code](https://github.com/baidu-baige/LoongForge/tree/master/cookbook/loongforge-vlda) · [Project](https://baidu-baige.github.io/LoongForge/projects/vlda.html) · [Code](https://github.com/baidu-baige/LoongForge)<br>
  Lingsen Zhang et al. · Harbin Institute of Technology, Shenzhen; Baidu, Inc.; Shenzhen Loop Area Institute
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

- <a id="paper-e998d3a5dbcbbbaa"></a>**ALDER: Discovering the Laws of a World by Acting in It** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2609.33728)* · [Paper](https://arxiv.org/abs/2609.33728)<br>
  Teng Cao, Yu Deng, Quentin Delfosse, Kristian Kersting · Technische Universität Darmstadt; Intrinsic; German Research Center for AI; +1 institutions
- <a id="paper-e8558e860f15ac05"></a>**DAGLoop: Aligning Method Design with Experimental Feedback in Automated AI Research** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.25089)* · [Paper](https://arxiv.org/abs/2610.25089) · [Code](https://github.com/deng34567/DAGLoop)<br>
  Dengyuxing Wang et al. · The Hong Kong University of Science and Technology; Hong Kong Baptist University; Hong Kong Generative AI Research & Development Center; +1 institutions
- <a id="paper-50dc4089b84b69c1"></a>**Formally Verified Autoresearch for Analyzing the Expressivity of Multi-Head Attention** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.25341)* · [Paper](https://arxiv.org/abs/2610.25341) · [Code](https://github.com/VerifiedMechanisms/automlr)<br>
  Karthik Viswanathan, Plamen Dimitrov, Stefano Rocca, Sarayu Sirikonda · Verified Mechanisms; MATS Research; University of California, Berkeley
- <a id="paper-892f3051f980319f"></a>**Knowledge Manifold Optimization for Scientific Discovery** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.25662)* · [Paper](https://arxiv.org/abs/2610.25662)<br>
  Shigeru Obayashi, Yoshiaki Kawagoe, Kazuhiko Komatsu, Tomonaga Okabe · Institute of Fluid Science, Tohoku University; Department of Aerospace Engineering, Tohoku University; Research Center for Green X-Tech, Tohoku University; +1 institutions
- <a id="paper-ce6ca28e99a1250e"></a>**LLM-IDEA: Identifiability-Driven Experimental Agent for Autonomous Discovery of Mechanistic World Models** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.11253)* · [Paper](https://arxiv.org/abs/2610.11253) · [Code](https://github.com/Suraskey/llm-idea)<br>
  Surya Shetty, Ulisses Braga-Neto · Texas A&M University; Polara Labs Inc.
- <a id="paper-0b0ccb120eb20f9a"></a>**Multi-Agent AI Design of a Nanowatt Biomedical Low-Pass Filter from Topology to Layout** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.28677)* · [Paper](https://arxiv.org/abs/2610.28677) · [Code](https://github.com/MacAnalog/spicexplorer-release)<br>
  Danial Noori Zadeh, Devanshu Prasad, Mohamed B. Elamien · Department of Electrical and Computer Engineering, McMaster University
- <a id="paper-c70675c50ebe2aee"></a>**MultiEcho: An Experimental Science of Learned Worlds** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2609.33347)* · [Paper](https://arxiv.org/abs/2609.33347)<br>
  Meng Zhu, Airui Zhang · SHIHAO XINRUI Group
- <a id="multiple-hypotheses"></a>**Searching for What Matters: Open-Ended Discovery of Multiple Hypotheses with Agentic Data Exploration** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.17874)* · [Paper](https://arxiv.org/abs/2610.17874)<br>
  Sanchit Kabra et al. · Virginia Tech; Amazon
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

- <a id="r09"></a>**AgentGym-RL: Training LLM Agents for Long-Horizon Decision Making through Multi-Turn Reinforcement Learning** · *[ICLR 2026](https://proceedings.iclr.cc/paper_files/paper/2026/hash/1571ce1ff735be4551db50887043726e-Abstract-Conference.html)* · [Paper](https://arxiv.org/abs/2509.08755) · [Code](https://github.com/woooodyy/AgentGym-RL) · [Project](https://AgentGym-RL.github.io) · [HF Dataset](https://huggingface.co/datasets/AgentGym/AgentGym-RL-Data-ID)<br>
  Zhiheng Xi et al. · Fudan University; ByteDance Seed; Shanghai Innovation Institute
- <a id="paper-c916585f0ec11b72"></a>**AgenticRoboRL: Bringing Coding-Agent Post-Training to Agentic Robotics** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.28589)* · [Paper](https://arxiv.org/abs/2610.28589) · [Code](https://github.com/xinxinliu-ai/AgenticRoboRL) · [Project](https://l-codingspace.github.io/AgenticRoboRL/) · [HF Model](https://huggingface.co/ciciciciliu/AgenticRoboRL-Qwen3.5-9B/tree/main/rl-v006)<br>
  Xinxin Liu et al. · University of Central Florida; University of Southern California; Michigan State University
- <a id="paper-511a84f55bad4b22"></a>**Ask to Distill: Learning to Synthesize Data for On-Policy Distillation** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.27450)* · [Paper](https://arxiv.org/abs/2610.27450) · [Code](https://github.com/GasolSun36/Ask_to_Distill) · [Dataset](https://huggingface.co/datasets/gasolsun/Ask_to_Distill-eval)<br>
  Jiashuo Sun et al. · University of Illinois Urbana-Champaign; The Hong Kong University of Science and Technology; Texas A&M University
- <a id="h04"></a>**CHART: A Harness-Rotation Curriculum for Harness-Robust Search Agents** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2609.22247)* · [Paper](https://arxiv.org/abs/2609.22247)<br>
  Xinlu Zhang et al. · Amazon
- <a id="compute-aligned"></a>**Compute Aligned Training: Optimizing for Test Time Inference** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2604.24957)* · [Paper](https://arxiv.org/abs/2604.24957) · [Code](https://github.com/adamoosya/compute-aligned-training)<br>
  Adam Ousherovitch, Ambuj Tewari · University of Michigan
- <a id="paper-09c58b5352e897c3"></a>**CoworkEnv: Synthesizing Training Environments for Long-Horizon Cowork Agents** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.24960)* · [Paper](https://arxiv.org/abs/2610.24960) · [Code](https://github.com/HKUST-KnowComp/CoworkEnv) · [Project](https://github.com/zhongweixie/CoworkEnv-Lessons) · [HF Model](https://huggingface.co/zhongweixie/PocketWorker-8B-ClawEval-SFT)<br>
  Zhongwei XIE et al. · The Hong Kong University of Science and Technology; The Chinese University of Hong Kong; Hong Kong Baptist University; +1 institutions
- <a id="paper-0b814b1f03c2835d"></a>**CURIO: Curiosity-Driven Test-Time Learning for Open-Ended Discovery** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.04851)* · [Paper](https://arxiv.org/abs/2610.04851) · [Project](https://ft2023.github.io/CURIO/) · [Code](https://github.com/ft2023/CURIO)<br>
  Tao Feng et al. · University of Illinois Urbana-Champaign; University of Maryland, College Park; Stanford University
- <a id="r05"></a>**Explore More, Drift Less: Outcome-Only Reinforcement Learning Can Suffice for Long-Horizon Interactive Agents** · *[arXiv 2026 (preprint)](https://arxiv.org/html/2609.01245v1)* · [Paper](https://arxiv.org/html/2609.01245v1)<br>
  Liming Pu et al.
- <a id="paper-843cdbc0b49a3683"></a>**Harness Scaling for Generalizable Agentic Reinforcement Learning** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.29458)* · [Paper](https://arxiv.org/abs/2610.29458)<br>
  Fei Bai et al. · Gaoling School of Artificial Intelligence, Renmin University of China; IQuest Research; Beihang University
- <a id="paper-c474fbc2967f22ed"></a>**Inherited, Not Invented: Tracing the Provenance of Wait in Reasoning Models** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.30882)* · [Paper](https://arxiv.org/abs/2610.30882)<br>
  Zhizhuo Kou et al. · The Hong Kong University of Science and Technology; Peking University; Huawei Noah’s Ark Lab
- <a id="paper-75eeeb130b15e1f6"></a>**PAR: Progress-Aligned Recurrence for Length Generalization in State Tracking** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.27628)* · [Paper](https://arxiv.org/abs/2610.27628)<br>
  Pan Wang et al. · Ant International; National University of Singapore
- <a id="paper-f5ebfafb83c6121b"></a>**Scaling in Games: Continued Pre-Training For Embodied Agents In Diverse Virtual Worlds** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.28698)* · [Paper](https://arxiv.org/abs/2610.28698) · [Project](https://gamescaling.github.io) · [Code](https://github.com/THUSI-Lab/GameScaling) · [HF Model](https://huggingface.co/THUSI-Lab/GameScaling-9B-S1)<br>
  Kuan Zhang et al. · miHoYo Honkai AI R&D Team; College AI, Tsinghua University; University of Chinese Academy of Sciences; +3 institutions
- <a id="d05"></a>**Scaling Scientific Discovery Environments for Turn-Level Agentic RL** · *[arXiv 2026 (preprint)](https://arxiv.org/html/2607.28990v1)* · [Paper](https://arxiv.org/html/2607.28990v1)<br>
  Yucheng Xu et al. · Shanghai AI Laboratory
- <a id="r06"></a>**SPROUT: Scaling Agentic Reinforcement Learning for Long-Horizon Software Engineering** · *[arXiv 2026 (preprint)](https://arxiv.org/html/2610.14405v1)* · [Paper](https://arxiv.org/html/2610.14405v1) · [Code](https://github.com/RISE-X-Lab/SPROUT) · [Project](https://rise-x-lab.github.io/SPROUT/)<br>
  Mengyang Liu et al. · Shanghai Jiao Tong University; Amazon; Nanjing University; +2 institutions
- <a id="paper-38e70b683c26da97"></a>**TraceForge: Distilling with Your Own Thinking** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.29680)* · [Paper](https://arxiv.org/abs/2610.29680)<br>
  Yan Wang · Independent Researcher
- <a id="paper-ce88f69c0203ec29"></a>**WeVisOne-VL: Unified Visual Perception from Objects to Pixels** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.31329)* · [Paper](https://arxiv.org/abs/2610.31329) · [Project](https://tencent.github.io/WeVisOne-VL) · [Code](https://github.com/Tencent/WeVisOne-VL)<br>
  Tianming Liang et al. · WeChat Vision, Tencent Inc.

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
- <a id="paper-63c5fd925e9f2dcd"></a>**ChartEvo: Self-Evolving Agent Harnesses for Long-Tail Chart Reasoning** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.28282)* · [Paper](https://arxiv.org/abs/2610.28282)<br>
  Qi Wang et al. · State Key Laboratory of Multimodal Artificial Intelligence Systems, CASIA; School of Artificial Intelligence, University of Chinese Academy of Sciences; New Laboratory of Pattern Recognition, CASIA; +1 institutions
- <a id="paper-dc5079437446d0d5"></a>**EvoBelief: Falsifiable World Models for Self-Improving LLM Agents** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.12789)* · [Paper](https://arxiv.org/abs/2610.12789)<br>
  Janet Wang et al. · Tulane University; Amazon
- <a id="harness-ttt"></a>**HarnessTTT: Learn to Optimize Harness at Test-Time for Scientific Discovery** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.17370)* · [Paper](https://arxiv.org/abs/2610.17370) · [Code](https://github.com/SaFo-Lab/Self_Adapt_Harness) · [Project](https://gray311.github.io/harnessrl/) · [HF Dataset](https://huggingface.co/datasets/gray311/HarnessRL)<br>
  Yingzi Ma et al. · University of Wisconsin-Madison; NVIDIA; Johns Hopkins University; +2 institutions
- <a id="t11"></a>**Learning to Discover at Test Time** · *[ICML 2026](https://proceedings.mlr.press/v306/yuksekgonul26a.html)* · [Paper](https://arxiv.org/html/2601.16175v1) · [Code](https://github.com/test-time-training/discover) · [Project](https://test-time-training.github.io/discover)<br>
  Mert Yuksekgonul et al. · Stanford University; NVIDIA; Astera Institute; +2 institutions
- <a id="paper-bf157ba63fabe951"></a>**Memory as Belief: Bayesian Evolution of Memory for Self-Evolving LLM Agents** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.25119)* · [Paper](https://arxiv.org/abs/2610.25119)<br>
  Yiming Xu et al. · School of Computer Science and Technology, Xi’an Jiaotong University; Shaanxi Provincial Key Laboratory of Big Data Knowledge Engineering, Xi’an Jiaotong University; University of Virginia, Charlottesville, Virginia, USA; +1 institutions
- <a id="t12"></a>**No Time Like the Present: Agentic Test-Time Training for LLM Agents** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2607.03441)* · [Paper](https://arxiv.org/abs/2607.03441)<br>
  Yanbo Wang et al. · Kuaishou Technology
- <a id="paper-6273fff431181535"></a>**Online Open-World Wafer Defect Discovery using Hyperdimensional Computing** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.28949)* · [Paper](https://arxiv.org/abs/2610.28949)<br>
  Quanling Zhao et al. · University of California San Diego; IBM Research; Anderon
- <a id="paper-52731a9209ac98ed"></a>**PreCoMem: Predictive Cognitive Memory for Self-Evolving Long-Term Dialogue Agents** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.29467)* · [Paper](https://arxiv.org/abs/2610.29467) · [Code](https://github.com/ZhongWishing/PreCoMem)<br>
  Jian Zhong et al. · Nankai University; vivo AI Lab; Tsinghua University; +2 institutions
- <a id="paper-c15fc300d6309d58"></a>**Remembering Has a Price: Learning Memory Worth under Resource Constraints** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.26453)* · [Paper](https://arxiv.org/abs/2610.26453) · [Code](https://github.com/AIGNLAI/TokenWorth)<br>
  Guannan Lai, Zi-Yang Bai, Jun-Peng Jiang, Han-Jia Ye · School of Artificial Intelligence, Nanjing University; National Key Laboratory for Novel Software Technology, Nanjing University
- <a id="paper-2d5446a91ef47109"></a>**Self-Evolving Agents through Privileged Retrospective Distillation** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.27495)* · [Paper](https://arxiv.org/abs/2610.27495)<br>
  Yuhang Zhou et al. · Meta AI
- <a id="skilltta"></a>**Skills on the Fly: Test-Time Adaptive Skill Synthesis for LLM Agents** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2605.16986)* · [Paper](https://arxiv.org/abs/2605.16986) · [Code](https://github.com/Hydr0pon1c/Skills-on-the-fly)<br>
  Jingxing Wang et al. · Shanghai Jiao Tong University; OPPO Research Institute
- <a id="paper-79697a458d1ee6cc"></a>**SpatialBrain: Spatial Intelligence Growing from Experience** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.29317)* · [Paper](https://arxiv.org/abs/2610.29317)<br>
  Yifan Zhou et al. · Shanghai Jiao Tong University; Zhejiang University
- <a id="ttt-ntp"></a>**Test-Time Training with Next-Token Prediction** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2606.21803)* · [Paper](https://arxiv.org/abs/2606.21803) · [Code](https://github.com/yancyou/TTT-NTP)<br>
  Xuan Ouyang, Zefan Cai, Junjie Hu · University of Wisconsin-Madison
- <a id="ttcs"></a>**TTCS: Test-Time Curriculum Synthesis for Self-Evolving** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2601.22628)* · [Paper](https://arxiv.org/abs/2601.22628) · [Code](https://github.com/XMUDeepLIT/TTCS)<br>
  Chengyi Yang et al. · Xiamen University; Washington University in St. Louis; Renmin University of China

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

- <a id="d09"></a>**Accelerating scientific discovery with Co-Scientist** · *[Nature 2026](https://www.nature.com/articles/s41586-026-10644-y)* · [Paper](https://arxiv.org/abs/2502.18864)<br>
  Juraj Gottweis et al. · Google Cloud AI Research; Google DeepMind; Google Research; +4 institutions
- <a id="h02"></a>**Agent Lightning v1.0: Towards Harnessed Agentic RL** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2608.17528)* · [Paper](https://arxiv.org/abs/2608.17528) · [Code](https://github.com/microsoft/agent-lightning)<br>
  Zhiyuan He et al. · Microsoft; Fudan University; Zhejiang University; +1 institutions
- <a id="a01"></a>**autoresearch** <sup>project</sup> · [Code](https://github.com/karpathy/autoresearch)<br>
  Andrej Karpathy
- <a id="paper-66f56984b6446ca0"></a>**Building AI Research Teams for Autonomous Discovery of Linear Attention Architectures** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.28887)* · [Paper](https://arxiv.org/abs/2610.28887)<br>
  Yujian Liu et al. · UC Santa Barbara; Pennsylvania State University; LinkedIn
- <a id="paper-433abe28aa06ff75"></a>**Cache Engineering for Agents** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.28577)* · [Paper](https://arxiv.org/abs/2610.28577) · [Code](https://github.com/thu-nics/AKV)<br>
  Tianyu Fu et al. · Tsinghua University; The Chinese University of Hong Kong
- <a id="station"></a>**Can AI Agents Make Open-Ended Scientific Discovery? Evidence from Station** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.08927)* · [Paper](https://arxiv.org/abs/2610.08927) · [Code](https://github.com/dualverse-ai/station-open-reseach) · [Data](https://github.com/dualverse-ai/station-open-reseach_data) · [Project](https://dualverse-ai.github.io/station-open-reseach_data)<br>
  Wenyu Du, Stephen Chung · DualverseAI; The University of Hong Kong; University of Cambridge
- <a id="causalsteward"></a>**CausalSteward: An Agentic Divide-Conquer-Combine Copilot for Causal Discovery** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2607.01936)* · [Paper](https://arxiv.org/abs/2607.01936)<br>
  Nicholas Tagliapietra et al. · TU Darmstadt; Bosch Center for Artificial Intelligence; hessian.AI; +2 institutions
- <a id="paper-1bad7b8c664a2eb2"></a>**DeepRewind: Predicting and Repairing Premature Commitments in Deep Research Agents** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2609.36344)* · [Paper](https://arxiv.org/abs/2609.36344) · [Code](https://github.com/AmirAbaskohi/DeepRewind)<br>
  Amirhossein Abaskohi et al. · University of British Columbia
- <a id="eurekagent"></a>**EurekAgent: Agent Environment Engineering is All You Need For Autonomous Scientific Discovery** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2606.13662)* · [Paper](https://arxiv.org/abs/2606.13662) · [Code](https://github.com/THU-Team-Eureka/EurekAgent)<br>
  Amy Xin et al. · Tsinghua University; Renmin University of China
- <a id="paper-0d8be09c556e897e"></a>**From VLM Planners to Robotic Agents: Self-Evolving Harnesses for History-Dependent Manipulation** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.29560)* · [Paper](https://arxiv.org/abs/2610.29560)<br>
  Tingwen Du et al. · University of Science and Technology of China; Shanghai Artificial Intelligence Laboratory; Shanghai Jiao Tong University; +2 institutions
- <a id="h03"></a>**Harness-1: Reinforcement Learning for Search Agents with State-Externalizing Harnesses** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2606.02373)* · [Paper](https://arxiv.org/abs/2606.02373) · [Code](https://github.com/pat-jj/harness-1) · [HF Model](https://huggingface.co/pat-jj/harness-1) · [HF Dataset](https://huggingface.co/datasets/pat-jj/harness-1-train-data)<br>
  Pengcheng Jiang et al. · University of Illinois Urbana-Champaign; UC Berkeley; Chroma
- <a id="paper-bd5dfa376cbe2ce7"></a>**HiSTEVE 1.0: Harnessing Human-Interface VLA Agents for Open-World Games** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.31162)* · [Paper](https://arxiv.org/abs/2610.31162)<br>
  Zecong Tang et al. · The University of Hong Kong; Zhejiang University; Fudan University; +2 institutions
- <a id="paper-50201f413f6c1220"></a>**Is Complex Agentic Memory Always Needed? Naive RAG Is Stronger Than We Thought** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.30755)* · [Paper](https://arxiv.org/abs/2610.30755) · [Code](https://github.com/Litmeb/RAW-RAG)<br>
  Zhengye Bao et al. · Luo Lab Undergraduate Division (LUD), Xi’an Jiaotong University; Shanghai Jiao Tong University; Zhejiang University; +1 institutions
- <a id="paper-ff469b4c8e0c8634"></a>**JANUS: Enhancing Long-Horizon Autonomous Research with Co-Evolving World Models** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.13194)* · [Paper](https://arxiv.org/abs/2610.13194) · [Project](https://github.com/bilemond/JANUS)<br>
  Mengdi Liu et al. · State Key Laboratory of AI Safety, Institute of Computing Technology, CAS, China; University of Chinese Academy of Sciences (CAS), China
- <a id="paper-79115fb39819fd02"></a>**MaD-RSI: Model-as-Data for Recursive Self-Improvement of Agent Harnesses** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.28201)* · [Paper](https://arxiv.org/abs/2610.28201)<br>
  Yu Cui et al. · Beijing Institute of Technology; Tsinghua University; Chengdu Institute of Computer Applications, Chinese Academy of Sciences; +4 institutions
- <a id="paper-0ed8e563cfef8c1c"></a>**MIRA: A Multimodal Illustrated Deep Research Agent for Controllable Reports** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.25926)* · [Paper](https://arxiv.org/abs/2610.25926) · [Project](https://mira-mmdeepresearch.github.io/)<br>
  Hongrui Wu et al. · Stanford University; The Hong Kong University of Science and Technology; JD.com; +3 institutions
- <a id="paper-fb16b20d25ce57e6"></a>**NeuroAct: Advancing EEG Analysis and Decoding via Dual-Loop Autonomous Research** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.25211)* · [Paper](https://arxiv.org/abs/2610.25211)<br>
  Wei Xiong et al. · Tongji University; Ant Group; Shanghai Jiao Tong University; +1 institutions
- <a id="paper-42c33aa80d5fcaf8"></a>**OMAR: Open-World Multi-Attribute Reasoning for Scene-Conditioned Shelf Organization** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.29761)* · [Paper](https://arxiv.org/abs/2610.29761)<br>
  Benedikt Kreis et al. · University of Bonn; Lamarr Institute for ML and AI; Technical University of Darmstadt
- <a id="paper-ae989ddb519ce3e3"></a>**OpenSaC: A Python Library for Search as Code in Deep Research Agents** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.25779)* · [Paper](https://arxiv.org/abs/2610.25779) · [Code](https://github.com/liuqi6777/OpenSaC)<br>
  Qi Liu et al. · Renmin University of China; National University of Singapore
- <a id="paper-18f922743caba570"></a>**OpenVLHarness: Real World Visual Agentic Tool-Use with Multimodal Memory** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.26860)* · [Paper](https://arxiv.org/abs/2610.26860) · [Project](https://openvlharness.github.io/) · [Code](https://github.com/uclanlp/OpenVLHarness) · [Dataset](https://huggingface.co/datasets/uclanlp/OpenVLHarness-Evaluation-Datasets) · [Project](https://openvlharness.github.io)<br>
  Yu Zhou et al. · University of California, Los Angeles; Apple
- <a id="paper2agent"></a>**Reimagining research papers as interactive and reliable AI agents** · *[Nature 2026](https://www.nature.com/articles/s41586-026-11044-y)* · [Paper](https://www.nature.com/articles/s41586-026-11044-y) · [Preprint](https://arxiv.org/abs/2509.06917) · [Code](https://github.com/jmiao24/Paper2Agent)<br>
  Jiacheng Miao et al. · Stanford University
- <a id="paper-c97a20989ff958e4"></a>**RIDAR: Safeguarding Research Integrity in Autonomous Research Agents via Automated Detection and Runtime Intervention** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.31372)* · [Paper](https://arxiv.org/abs/2610.31372) · [Code](https://github.com/THU-KEG/RIDAR)<br>
  Jiening Siow et al. · Department of Computer Science and Technology, Tsinghua University; School of Information, Renmin University of China; Zhipu AI
- <a id="robin"></a>**Robin: A multi-agent system for automating scientific discovery** · *[Nature 2026](https://www.nature.com/articles/s41586-026-10652-y)* · [Paper](https://arxiv.org/abs/2505.13400)<br>
  Ali Essam Ghareeb et al. · FutureHouse; University of Oxford
- <a id="paper-c397688c68ae69b3"></a>**RoleFlow: Self-Evolving Multi-Role Agentic Collaboration via Structural Adaptation** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.30429)* · [Paper](https://arxiv.org/abs/2610.30429)<br>
  Yi Ge et al. · University of Maryland, College Park; University of Pittsburgh; The University of Texas at Dallas
- <a id="paper-09c8b51fd5a44907"></a>**S-Agent 2.0: Spatial Reasoning with a General Coding Agent** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.28354)* · [Paper](https://arxiv.org/abs/2610.28354) · [Project](https://ropedia.github.io/S-Agent-2.0) · [Code](https://github.com/Ropedia/S-Agent-2.0)<br>
  Rui Gong et al. · Nanyang Technological University; University of Hong Kong; Ropedia
- <a id="ai-scientist"></a>**The AI Scientist: Towards Fully Automated Open-Ended Scientific Discovery** · *[Nature 2026](https://www.nature.com/articles/s41586-026-10265-5)* · [Paper](https://arxiv.org/abs/2408.06292) · [Code](https://github.com/SakanaAI/AI-Scientist)<br>
  Chris Lu et al. · Sakana AI; University of Oxford; University of British Columbia; +2 institutions

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
- <a id="a03"></a>**Darwin Gödel Machine: Open-Ended Evolution of Self-Improving Agents** · *[ICLR 2026](https://proceedings.iclr.cc/paper_files/paper/2026/hash/aa5f5e6eb6f613ec412f1d948dfa21a5-Abstract-Conference.html)* · [Paper](https://arxiv.org/html/2505.22954v1) · [Code](https://github.com/jennyzzt/dgm) · [Blog](https://sakana.ai/dgm/)<br>
  Jenny Zhang et al. · University of British Columbia; Vector Institute; Sakana AI; +1 institutions
- <a id="discoveryrsi"></a>**DiscoveryRSI: Recursively Learning to Discover Valuable Hypotheses** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.23839)* · [Paper](https://arxiv.org/abs/2610.23839) · [Code](https://github.com/Gen-Verse/DiscoveryRSI) · [HF Model](https://huggingface.co/Gen-Verse/DiscoveryRSI-27B) · [HF Dataset](https://huggingface.co/datasets/Gen-Verse/DiscoveryRSI-Hypothesis-Task-Examples) · [HF Collection](https://huggingface.co/collections/Gen-Verse/discoveryrsi) · [Demo](https://foundry-arena.rsi-arena.workers.dev/arena)<br>
  Jianyuan Zhong et al. · PhAI Labs; The Chinese University of Hong Kong; University of Michigan; +13 institutions
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
- <a id="paper-02f41708e47efed6"></a>**Large Language Models Meet Bayesian Optimization: Towards Self-evolving Wireless Digital Twins** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.31192)* · [Paper](https://arxiv.org/abs/2610.31192)<br>
  Yingzhuo Sun et al. · KTH Royal Institute of Technology; Data Machine Elite; ˙Izmir Institute of Technology
- <a id="r-zero"></a>**R-Zero: Self-Evolving Reasoning LLM from Zero Data** · *[ICLR 2026](https://openreview.net/pdf?id=96apU6YzSO)* · [Paper](https://arxiv.org/abs/2508.05004) · [Code](https://github.com/Chengsong-Huang/R-Zero) · [Project](https://chengsong-huang.github.io/R-Zero.github.io/)<br>
  Chengsong Huang et al. · Tencent AI Seattle Lab; Washington University in St. Louis; University of Maryland, College Park; +1 institutions
- <a id="paper-2017be142f7eddde"></a>**Recursive Self-Improvement on a Budget: Scoring Code Edits Before They Run** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.29121)* · [Paper](https://arxiv.org/abs/2610.29121)<br>
  Erfan Darzi, Sree Bhargavi Balija, Sheng He · Harvard University; Massachusetts Institute of Technology; UC San Diego
- <a id="paper-26bdab7224d77ff2"></a>**SCOPE: Compiling Natural-Language Policies into Neurosymbolic Predicate Programs** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.31062)* · [Paper](https://arxiv.org/abs/2610.31062) · [Dataset](https://huggingface.co/datasets/Plurai/SCOPE)<br>
  Arnon Mazza, Elad Levi · Plurai
- <a id="self-hpo"></a>**Self-Evolving Coding Agents via Harness-Policy Optimization** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.22791)* · [Paper](https://arxiv.org/abs/2610.22791) · [Code](https://github.com/MSR-Orchard/Self-HPO) · [HF Model (Self-HPO)](https://huggingface.co/self-hpo/Self-HPO-Qwen3.5-35B-A3B) · [HF Model (HPO)](https://huggingface.co/self-hpo/HPO-Qwen3.5-35B-A3B)<br>
  Zhepei Wei et al. · Microsoft Research; University of Virginia; Carnegie Mellon University
- <a id="swarmrsi"></a>**SwarmRSI: Recursive Self-Improvement through Evolving Scientific Agent Swarm** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.20431)* · [Paper](https://arxiv.org/abs/2610.20431)<br>
  Qianru Meng et al. · Huawei Technologies Co., Ltd.; Leiden University; University of Groningen

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
- <a id="paper-81e8d8901cbd7168"></a>**Auditing the Product, Not the Recursion: The Evaluation Evidence Behind Recursive Self-Improvement Claims** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.27610)* · [Paper](https://arxiv.org/abs/2610.27610)<br>
  Zihan Chen, Di Zhu, Lei Nico Zheng · Stevens Institute of Technology; University of Massachusetts Boston
- <a id="paper-d8639c0b4eb9ace3"></a>**Automating ML for Science: Can Frontier Agents Climb Scientific Hills in the Wild?** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.28763)* · [Paper](https://arxiv.org/abs/2610.28763) · [Code](https://github.com/maszhongming/agent4sci) · [Dataset](https://huggingface.co/datasets/MingZhong/agent4sci)<br>
  Ming Zhong, Stacy Li, Nicholas Carlini, Matthew Jagielski · Anthropic Fellows Program; Anthropic
- <a id="as-bench"></a>**Autonomous Science Bench: Evaluating AI Agents for Autonomous Scientific Discovery** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.18449)* · [Paper](https://arxiv.org/abs/2610.18449) · [Code](https://github.com/Yibo-Wen/as-bench) · [Project](https://yibow.me/autonomous-science-bench)<br>
  Yibo Wen, Han Liu · Northwestern University
- <a id="paper-31224f0f7655c123"></a>**Benchmarking and Error Analysis of Deep Search and Deep Research LLM Agents** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.29346)* · [Paper](https://arxiv.org/abs/2610.29346)<br>
  Zixuan Yu, Zhenheng Tang, Xiaowen Chu, Bo Han · School of Computer science and engi-
neering, Sun Yat-sen University; CSE, The Hong Kong University of Science and Technology; DSA Thrust, The Hong Kong Uni-
versity of Science and Technology (GuangZhou); +1 institutions
- <a id="c11"></a>**CausaLab: A Scalable Environment for Interactive Causal Discovery Toward AI Scientists** · *[arXiv 2026 (preprint)](https://arxiv.org/html/2605.26029v2)* · [Paper](https://arxiv.org/html/2605.26029v2)<br>
  Junlin Yang et al. · Tsinghua University; University of Illinois Urbana-Champaign; Carnegie Mellon University; +2 institutions
- <a id="paper-e461db7393754058"></a>**CellTrack-Bench: Microscopic Cell Tracking Benchmark for Vision-Language Models** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.31566)* · [Paper](https://arxiv.org/abs/2610.31566) · [Code](https://github.com/royerlab/celltrack-bench)<br>
  Ilan Theodoro, Jordão Bragantini, Loïc A. Royer · Biohub
- <a id="paper-50d8cd71040f538b"></a>**DecisionPivot: A Diagnostic Benchmark for Decision Models in LLM Systems** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.28522)* · [Paper](https://arxiv.org/abs/2610.28522) · [Code](https://github.com/StartLuxLabs/DecisionPivot) · [Dataset](https://huggingface.co/datasets/startlux-models/DecisionPivot)<br>
  Xialie Zhuang et al. · StartLux
- <a id="discern"></a>**DISCERN: Can AI Agents Work Like Scientists and Guide Discovery?** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2609.33357)* · [Paper](https://arxiv.org/abs/2609.33357) · [HF Dataset](https://huggingface.co/datasets/discern-bench-anon/discern-benchmark)<br>
  Nan Huang et al. · University of California San Diego
- <a id="paper-ff655bd3f5066c0f"></a>**EvaOmni: An Evidence-Grounded Benchmark for Audio-Visual Reasoning** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.28444)* · [Paper](https://arxiv.org/abs/2610.28444) · [Code](https://github.com/VisionXLab/EvaOmni) · [Dataset](https://huggingface.co/datasets/VisionXLab/EvaOmni-Dataset)<br>
  Xiaoxing Hu et al. · Shanghai Jiao Tong University; Shanghai Innnovation Institute; Inner Mongolia University of Technology; +7 institutions
- <a id="paper-7b88221edcfc1946"></a>**GameBoyWorlds: A Testbed for Self-Improvement in Embodied Video Games** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2609.32093)* · [Paper](https://arxiv.org/abs/2609.32093) · [Code](https://github.com/DhananjayAshok/GameBoyWorlds-Benchmark) · [Code](https://github.com/DhananjayAshok/GameBoyWorlds)<br>
  Dhananjay Ashok et al. · Information Sciences Institute, University of Southern California; Columbia University; University of Chicago; +2 institutions
- <a id="into-the-unknown"></a>**Into the Unknown: Benchmarking AI agents on open scientific research problems** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.19159)* · [Paper](https://arxiv.org/abs/2610.19159) · [Code](https://github.com/prometheus-eval/into-the-unknown) · [Project](https://prometheus-eval.github.io/into-the-unknown/viewer/) · [HF Dataset](https://huggingface.co/datasets/prometheus-eval/into-the-unknown)<br>
  Seungone Kim et al. · Carnegie Mellon University; University of Minnesota; Stanford University; +13 institutions
- <a id="paper-d413c98db0f6141e"></a>**MMEnterprise-Bench: Evaluating Enterprise Agents over Evolving Multimodal Records** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.27911)* · [Paper](https://arxiv.org/abs/2610.27911) · [Project](https://mlvlab.github.io/MMEnterprise-Bench/) · [Code](https://github.com/mlvlab/MMEnterprise-Bench)<br>
  Seohyun Lee et al. · KAIST; Korea University
- <a id="d03"></a>**NewtonBench: Benchmarking Generalizable Scientific Law Discovery in LLM Agents** · *[ICLR 2026](https://proceedings.iclr.cc/paper_files/paper/2026/hash/a0e1c2c40fc245b5fe7251ea33fbb045-Abstract-Conference.html)* · [Paper](https://arxiv.org/abs/2510.07172) · [Code](https://github.com/HKUST-KnowComp/NewtonBench)<br>
  Tianshi Zheng et al. · HKUST; NVIDIA
- <a id="paper-ee84b521258fee34"></a>**Retrieval Augmented Generation Compositionality** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.29722)* · [Paper](https://arxiv.org/abs/2610.29722) · [Code](https://github.com/dolev31/lasagna) · [Project](https://dolev31.github.io/lasagna/)<br>
  Ido Levy, Segev Shlomov, Leshem Choshen · IBM; Weizmann Institute of Science
- <a id="science-gym"></a>**Science-Gym: a simple testbed for AI-driven scientific discovery** · *[Machine Learning 2026](https://link.springer.com/article/10.1007/s10994-025-06914-x)* · [Paper](https://link.springer.com/article/10.1007/s10994-025-06914-x) · [Code](https://github.com/pibborn/science-gym)<br>
  Mattia Cerrato et al. · Johannes Gutenberg University Mainz; TU Darmstadt and hessian.AI; Max Planck Institute for Polymer Research; +2 institutions
- <a id="paper-e5da3aa895bba2db"></a>**Self-Consistency of Entity Sets and Citations in a Deep Research System under Repeated Prompting** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.26421)* · [Paper](https://arxiv.org/abs/2610.26421)<br>
  Lauri Pykälä, Kimmo K. Kaski · Aalto University School of Science
- <a id="paper-5bd5dfea78d8efef"></a>**ST-Bench: A Spatial-Temporal Benchmark for Multi-Agent System Generation on Scientific Research Tasks** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.07763)* · [Paper](https://arxiv.org/abs/2610.07763)<br>
  Qi Cheng et al. · Rutgers University; University of Pittsburgh; University of Minnesota; +3 institutions
- <a id="paper-1b71ddb115ba5e37"></a>**The Scientific Research Taste Benchmark (SciTaste-Bench): A Multi-Disciplinary Benchmark for Assessing Large Language Models' Judgment of Research Taste in Scientific Papers** · *[arXiv 2026 (preprint)](https://arxiv.org/abs/2610.28653)* · [Paper](https://arxiv.org/abs/2610.28653)<br>
  Xinyi Gao et al. · University of Chinese Academy of Sciences; Alibaba Group; Tsinghua University
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
