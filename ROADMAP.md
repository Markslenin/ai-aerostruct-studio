# Roadmap

本路线图分为两部分：

- 工程实现路线：保证项目从最小 demo 逐步变成可展示系统；
- 研究路线：见 [`docs/RESEARCH_ROADMAP.md`](docs/RESEARCH_ROADMAP.md)，用于规划从毕业设计、应用论文到长期高水平研究探索的演进路径。

---

## v0.1：项目骨架

- [x] README
- [x] 项目说明
- [x] 目录结构
- [x] Skill 架构草案
- [x] DesignSpec 草案

## v0.2：最小计算闭环

- [x] 手动输入 DesignSpec
- [x] 生成翼面积、展弦比
- [ ] 生成平均弦长
- [x] 经验公式计算升力/阻力
- [x] 悬臂梁结构校核
- [x] 规则判断是否满足需求
- [ ] 将 demo 流程抽象为 `core/pipeline.py`
- [ ] 使用 `DesignSpec.model_validate()` 校验输入
- [ ] 修正整翼升力与半翼结构载荷关系

## v0.3：LLM 接入

- [ ] 自然语言解析为 DesignSpec
- [ ] JSON Schema 校验
- [ ] 错误自动修复
- [ ] 结果解释生成
- [ ] Skill 调用日志与数据来源追踪

## v0.4：几何展示

- [ ] NACA 翼型生成
- [ ] 梯形翼网格生成
- [ ] 3D 可视化
- [ ] STL/OBJ 导出
- [ ] 多视角渲染图导出
- [ ] 点云采样

## v0.5：知识库

- [ ] 材料库
- [ ] 翼型库
- [ ] 设计手册 RAG
- [ ] 参数来源追踪

## v0.6：算法增强

- [ ] 升力线法
- [ ] VLM 涡格法
- [ ] 展向载荷分布
- [ ] 气动载荷转结构载荷
- [ ] 梁单元 / 简化 FEM

## v0.7：数据集与自训练闭环

- [ ] `dataset/sampler.py`：随机生成设计参数
- [ ] `dataset/generator.py`：批量运行 pipeline
- [ ] `dataset/exporter.py`：导出 CSV / JSONL
- [ ] 自动记录 passed / failed / failure_reason
- [ ] 构建第一版低速翼面设计数据集

## v0.8：Surrogate 尺寸推荐

- [ ] 训练 Random Forest / XGBoost / MLP baseline
- [ ] 输入需求，输出推荐翼展、弦长、梁尺寸
- [ ] 与 Random Search 对比
- [ ] 与 Grid Search 对比
- [ ] 与 Rule-based Heuristic 对比
- [ ] 统计成功率、阻力、质量近似、约束裕度、计算次数

## v1.0：可展示 Demo

- [ ] Streamlit 界面
- [ ] 自然语言输入
- [ ] 一键生成设计结果
- [ ] 曲线图、3D 图、校核表
- [ ] Markdown/PDF 报告
- [ ] 示例项目与复现实验脚本

## Long-term：物理约束自进化设计 Agent

长期探索方向见 [`docs/RESEARCH_ROADMAP.md`](docs/RESEARCH_ROADMAP.md)。

目标不是让大模型直接替代工程师，而是构建：

```text
模型提出候选设计
↓
Skill / 仿真器进行物理校核
↓
规则模块判断是否满足约束
↓
失败原因反馈给设计策略
↓
通过验证的数据进入训练集
↓
模型逐步提升推荐能力
```

长期架构暂定为：

```text
PG-SEDA: Physics-Grounded Self-Evolving Design Agent
```
