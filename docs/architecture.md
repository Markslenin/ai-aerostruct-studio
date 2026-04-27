# Architecture

## 设计原则

1. LLM 不直接输出最终工程结论；
2. 所有关键数值来自用户输入、检索结果或 Skill 计算；
3. Skill 输入输出必须经过 Schema 校验；
4. 规则校核结果优先于 LLM 解释；
5. 所有结果记录来源，便于复查。

## 分层

```text
User Interface
↓
LLM Agent
↓
Skill Registry
↓
Skill Modules
↓
Validation Layer
↓
Result Store
↓
Report Layer
```

## 数据流

```text
Natural Language
→ DesignSpec
→ GeometryResult
→ AeroResult
→ StructureResult
→ CheckResult
→ Report
```

## 后续扩展

- 多模态输入；
- RAG 知识库；
- VLM/VLM-like 云图解释；
- C/C++ 高性能气动内核；
- VLM 涡格法；
- 有限元后端。
