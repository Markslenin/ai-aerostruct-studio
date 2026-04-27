from typing import Any

from ai_aerostruct.skills.base import BaseSkill, SkillResult


class SimpleStructureSolverSkill(BaseSkill):
    name = "simple_structure_solver"
    description = "简化悬臂梁结构校核：翼根弯矩、弯曲应力、安全系数。"

    def run(self, data: dict[str, Any]) -> SkillResult:
        try:
            span = data["span_m"]
            lift = data["lift_N"]
            elastic_modulus = data["elastic_modulus_pa"]
            yield_strength = data["yield_strength_pa"]
            spar_height = data["spar_height_m"]
            spar_width = data["spar_width_m"]

            # 简化：半翼看作悬臂梁，载荷等效作用于半展长中点
            half_span = span / 2
            root_moment = lift * half_span / 2

            # 简化矩形梁惯性矩
            inertia = spar_width * spar_height**3 / 12
            y_max = spar_height / 2
            max_stress = root_moment * y_max / inertia
            safety_factor = yield_strength / max_stress if max_stress > 0 else float("inf")

            # 简化集中等效载荷挠度估算
            tip_deflection = lift * half_span**3 / (3 * elastic_modulus * inertia)

            return SkillResult(
                success=True,
                data={
                    "root_bending_moment_Nm": root_moment,
                    "section_inertia_m4": inertia,
                    "max_stress_pa": max_stress,
                    "tip_deflection_m": tip_deflection,
                    "safety_factor": safety_factor,
                },
                warnings=["当前为简化梁模型，不替代三维有限元验证。"],
            )
        except Exception as exc:
            return SkillResult(success=False, errors=[str(exc)])
