import math
from typing import Any

from ai_aerostruct.skills.base import BaseSkill, SkillResult


class SimpleAeroSolverSkill(BaseSkill):
    name = "simple_aero_solver"
    description = "简化低速翼面气动估算：面积、展弦比、CL、CD、升力、阻力。"

    def run(self, data: dict[str, Any]) -> SkillResult:
        try:
            span = data["span_m"]
            root_chord = data["root_chord_m"]
            tip_chord = data["tip_chord_m"]
            velocity = data["velocity_mps"]
            rho = data.get("air_density_kg_m3", 1.225)
            alpha_deg = data.get("alpha_deg", 5.0)

            area = 0.5 * (root_chord + tip_chord) * span
            aspect_ratio = span**2 / area
            alpha_rad = math.radians(alpha_deg)

            # 简化有限翼升力线斜率
            cl_alpha = 2 * math.pi * aspect_ratio / (aspect_ratio + 2)
            cl = cl_alpha * alpha_rad

            oswald_e = 0.8
            cd0 = 0.02
            k = 1.0 / (math.pi * oswald_e * aspect_ratio)
            cd = cd0 + k * cl**2

            q = 0.5 * rho * velocity**2
            lift = q * area * cl
            drag = q * area * cd

            return SkillResult(
                success=True,
                data={
                    "wing_area_m2": area,
                    "aspect_ratio": aspect_ratio,
                    "CL": cl,
                    "CD": cd,
                    "lift_N": lift,
                    "drag_N": drag,
                    "dynamic_pressure_pa": q,
                },
                warnings=["当前为简化气动估算，不适用于失速、强分离或跨音速问题。"],
            )
        except Exception as exc:
            return SkillResult(success=False, errors=[str(exc)])
