# Skill Design

## Skill 基本要求

每个 Skill 必须包含：

- name
- description
- input schema
- output schema
- limitations
- run method

## 示例

```yaml
name: simple_aero_solver
description: 简化低速翼面气动估算
inputs:
  - span_m
  - root_chord_m
  - tip_chord_m
  - velocity_mps
  - air_density_kg_m3
  - alpha_deg
outputs:
  - wing_area_m2
  - aspect_ratio
  - CL
  - CD
  - lift_N
  - drag_N
limitations:
  - 不考虑失速
  - 不适用于高速可压缩流
  - 不替代 CFD
```

## 防幻觉策略

- LLM 不生成最终计算结果；
- Skill 返回结构化结果；
- RuleChecker 做最终通过/不通过判断；
- 报告必须引用 Skill 数据。
