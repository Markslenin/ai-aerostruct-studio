# Research Roadmap

本文件记录 AI AeroStruct Studio 从工程原型走向论文级研究系统的长期路线。

项目短期目标不是直接替代工程师，也不是直接训练一个大模型生成最终飞机结构，而是构建一个可验证、可扩展的智能初步设计闭环：

```text
自然语言需求
↓
DesignSpec 参数化描述
↓
参数化几何 / 3D 模型生成
↓
气动、结构、规则 Skill 校核
↓
数据集自动生成
↓
Surrogate / Recommender 推荐尺寸
↓
仿真闭环再校核
↓
报告与设计迭代
```

---

## 1. 总体研究问题

核心问题可以表述为：

> 如何让 AI 在三维工程设计空间中，通过物理计算和仿真闭环，生成可验证、可追溯、满足约束的初步设计方案？

更具体地说，本项目关注：

- 如何把自然语言需求转化为结构化 `DesignSpec`；
- 如何将翼面几何、气动、结构和校核统一到可复现的计算管线；
- 如何自动生成训练数据，而不是完全依赖人工标注；
- 如何让模型先推荐合理初值，再由确定性 Skill 或仿真器校核；
- 如何记录失败原因，并把失败样本转化为后续训练经验；
- 如何从单一翼面原型扩展到更通用的工程设计 Agent。

---

## 2. 阶段一：毕业设计 / 工程原型级

目标：形成一个可运行、可展示、可解释的低速翼面初步设计系统。

### 需要完成

- [ ] `DesignSpec` 完整校验；
- [ ] `core/pipeline.py` 统一计算流程；
- [ ] 气动 Skill：翼面积、展弦比、升力、阻力；
- [ ] 结构 Skill：翼根弯矩、应力、安全系数、挠度；
- [ ] 规则 Skill：升力、强度、挠度约束判断；
- [ ] Streamlit 前端；
- [ ] Markdown 报告生成；
- [ ] 最小单元测试；
- [ ] 示例输入和示例输出。

### 论文/毕设定位

```text
面向低速翼面初步设计的 LLM-Skill 协同辅助设计系统
```

该阶段重点是系统完整性和工程可解释性，不强调复杂算法创新。

---

## 3. 阶段二：应用论文级

目标：从“计算工具”升级为“尺寸推荐方法”。

### 核心路线

```text
参数随机采样
↓
气动/结构 Skill 自动计算
↓
规则模块自动打标签
↓
生成训练数据集
↓
训练 Surrogate / Recommender
↓
推荐候选尺寸
↓
再次校核并筛选
```

### 需要完成

- [ ] `dataset/generator.py`：自动生成大量 `DesignSpec`；
- [ ] `dataset/exporter.py`：导出 CSV / JSONL；
- [ ] `optimizer/surrogate.py`：训练尺寸推荐模型；
- [ ] `optimizer/search.py`：随机搜索、网格搜索、启发式搜索；
- [ ] 对比方法：Random Search、Grid Search、Rule-based Heuristic、Surrogate；
- [ ] 评价指标：成功率、阻力、质量近似、约束裕度、计算次数；
- [ ] 消融实验：无 surrogate、无自训练、无规则校核。

### 推荐论文题目

```text
基于仿真闭环自训练的低速梯形翼初步尺寸推荐方法
```

或者：

```text
Simulation-in-the-loop Self-training for Preliminary Aero-Structural Wing Design
```

---

## 4. 阶段三：强论文级 / 专业期刊级

目标：引入更真实的几何、气动和结构模型，提升方法可信度。

### 技术升级

- [ ] NACA 翼型生成；
- [ ] 梯形翼 3D mesh 生成；
- [ ] STL / OBJ 导出；
- [ ] 多视角渲染图生成；
- [ ] 点云采样；
- [ ] 升力线法；
- [ ] VLM 涡格法；
- [ ] 梁单元 / 简化 FEM；
- [ ] 气动载荷到结构载荷映射；
- [ ] 多目标优化：升力、阻力、质量、强度、挠度。

### 方法升级

- [ ] Multi-fidelity evaluation：经验公式 → VLM → FEM / CFD；
- [ ] Active learning：优先选择最有价值样本进行高保真仿真；
- [ ] Failure-aware self-training：记录失败原因和修改策略；
- [ ] OOD 测试：不同速度、升力需求、材料和构型下的泛化能力。

### 推荐论文题目

```text
A multi-fidelity self-training framework for aero-structural wing design optimization
```

---

## 5. 阶段四：Nature 系列探索级

该阶段不是当前短期目标，而是长期研究方向。

单纯提出一个 `LLM + Skill` 架构不足以支撑高水平主刊。主刊级目标需要把问题从“设计一个翼面”提升到：

> 一个能在真实 3D 工程设计空间中，通过物理仿真自我学习，并生成可验证设计的通用智能设计框架。

### 可能架构：PG-SEDA

暂定名称：

```text
PG-SEDA: Physics-Grounded Self-Evolving Design Agent
```

核心模块：

```text
Requirement Parser
↓
Parametric + 3D Geometry Generator
↓
Multimodal Geometry Encoder
↓
Multi-Fidelity Evaluator
↓
Failure-Aware Critic
↓
Active Learning Controller
↓
Surrogate Design Model
↓
Self-Evolving Design Memory
↓
Pareto Proposal Engine
↓
Validated CAD / Report
```

### 主刊级必要条件

- [ ] 不局限于一个翼面任务，至少覆盖多个工程设计任务；
- [ ] 构建公开 benchmark；
- [ ] 包含自然语言需求、参数化设计、CAD/mesh/point cloud、多视角图、仿真结果和设计轨迹；
- [ ] 与 GA、Bayesian Optimization、CMA-ES、NSGA-II、RL、diffusion model、LLM-only agent 等方法对比；
- [ ] 显著减少高保真 CFD/FEM 调用次数；
- [ ] 证明 OOD 泛化能力；
- [ ] 最好包含实验或高可信度仿真验证；
- [ ] 开源代码、数据集和评测脚本。

### 主刊级论文叙事

```text
Generative AI can propose engineering shapes, but it cannot guarantee physical validity.
We introduce a physics-grounded self-evolving design agent that couples multimodal geometry generation, multi-fidelity simulation, failure-aware self-training and active learning.
Across aerodynamic, structural and thermal design tasks, the agent discovers feasible Pareto-optimal designs with substantially fewer high-fidelity simulations than conventional optimization baselines.
```

---

## 6. 推荐模块规划

```text
src/ai_aerostruct/
├── core/
│   ├── pipeline.py
│   ├── result.py
│   └── report.py
├── schemas/
│   ├── design_spec.py
│   ├── result_spec.py
│   └── dataset_spec.py
├── skills/
│   ├── aero_solver.py
│   ├── structure_solver.py
│   ├── rule_checker.py
│   └── base.py
├── geometry/
│   ├── airfoil.py
│   ├── wing_mesh.py
│   └── render.py
├── dataset/
│   ├── sampler.py
│   ├── generator.py
│   └── exporter.py
├── optimizer/
│   ├── search.py
│   ├── surrogate.py
│   └── recommender.py
└── agent/
    ├── parser.py
    ├── planner.py
    └── memory.py
```

---

## 7. 近期执行顺序

优先级最高的 10 个任务：

1. 将 `examples/run_demo.py` 的流程抽到 `core/pipeline.py`；
2. 让 demo 使用 `DesignSpec.model_validate()`；
3. 修正结构 Skill 中整翼升力与半翼载荷的关系；
4. 给每个 Skill 增加输入/输出 Schema；
5. 增加 `SkillCallLog`，记录输入、输出、warning、error 和数据来源；
6. 写 `dataset/sampler.py`，随机生成翼面参数；
7. 写 `dataset/generator.py`，批量运行 pipeline 并保存数据；
8. 写基础测试：气动、结构、规则、pipeline；
9. 训练第一个 surrogate baseline；
10. 用 Random Search / Grid Search / Surrogate 做第一组对比实验。

---

## 8. 项目边界

短期内不宣称：

- 直接替代工程师；
- 端到端生成真实飞机结构；
- 大模型直接保证尺寸正确；
- 没有校核就输出最终设计；
- 简化公式等同于高保真 CFD/FEM。

本项目坚持：

```text
模型负责提出候选设计；
Skill / 仿真器负责物理校核；
规则模块负责约束判断；
报告模块负责解释和追溯。
```
