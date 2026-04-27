```text
🚧================================================🚧
||                                                ||
||                施 工  ing                      ||
||                                                ||
||      AI AeroStruct Studio is under build       ||
||                                                ||
🚧================================================🚧
```

# AI AeroStruct Studio 🚧

一个面向低速飞行器翼面初步设计的轻量化智能辅助设计平台。

项目采用 **LLM + Skills** 架构：  
LLM 负责理解需求、检索资料、组织流程和生成报告；  
几何、气动、结构和校核计算由确定性的 Skill 模块完成。

---

## 项目目标

构建一套从需求到初步验证的设计闭环：

```text
用户需求
↓
DesignSpec 参数化描述
↓
几何生成
↓
气动估算
↓
结构校核
↓
规则判断
↓
报告输出
```

第一阶段聚焦：

- 梯形翼 / 弹翼 / 小型无人机翼面；
- NACA 翼型生成；
- 简化气动估算；
- 悬臂梁结构校核；
- 设计规则检查；
- Markdown 报告生成。

---

## 为什么用 Skill 架构？

工程设计里，LLM 不应该直接给最终数值结论。

本项目的设计原则是：

```text
LLM 负责理解和解释
Skill 负责计算和校核
规则模块负责最终判断
```

关键数据需要有明确来源：

| 来源 | 含义 |
|---|---|
| `user_input` | 用户输入 |
| `retrieved` | 手册、材料库、翼型库检索 |
| `computed` | Skill 模块计算结果 |

这样可以降低幻觉风险，也方便后续复查。

---

## 当前进度

🚧 施工 ing

已完成：

- [x] 项目目标定义
- [x] 总体架构设计
- [x] `DesignSpec` 数据结构草案
- [x] Skill 注册器骨架
- [x] 简化气动 Skill
- [x] 简化结构 Skill
- [x] 规则校核 Skill
- [x] 示例输入文件
- [x] Demo 运行入口

待完成：

- [ ] Streamlit 前端
- [ ] LLM 需求解析
- [ ] RAG 知识库
- [ ] 翼面 3D 可视化
- [ ] 升力线法 / VLM
- [ ] 更完整的结构模型
- [ ] 自动报告生成

---

## 项目结构

```text
ai-aerostruct-studio/
├── README.md
├── PROJECT.md
├── ROADMAP.md
├── pyproject.toml
├── src/
│   └── ai_aerostruct/
│       ├── agent/
│       ├── core/
│       ├── schemas/
│       └── skills/
├── docs/
├── examples/
└── tests/
```

---

## 快速开始

```bash
python -m venv .venv
source .venv/bin/activate

pip install -e .
python examples/run_demo.py
```

当前 demo 会运行一个简化流程：

```text
读取示例 DesignSpec
↓
计算气动参数
↓
计算结构参数
↓
执行规则校核
↓
打印结果
```

---

## 技术路线

| 模块 | 当前方案 | 后续计划 |
|---|---|---|
| LLM | 预留接口 | 本地 14B 模型 |
| 参数描述 | Pydantic Schema | 更完整的 DesignSpec |
| 几何 | NACA 翼型函数 | 翼面网格与导出 |
| 气动 | 经验公式 | 升力线法 / VLM |
| 结构 | 悬臂梁模型 | 梁单元 / 壳简化 |
| 校核 | Python 规则 | 更完整的规则引擎 |
| 前端 | 暂无 | Streamlit |
| 知识库 | 暂无 | RAG |

---

## 项目边界

本项目暂时不是：

- 通用 CAD 软件；
- 高精度 CFD 软件；
- 完整有限元软件；
- 自动替代工程师的设计系统。

它更像是一个初步设计阶段的工程助手：

> 快速生成方案，快速估算性能，快速发现明显问题。

---

## License

暂定 MIT。

如果后续引入第三方开源内核，需要重新检查许可证兼容性。
