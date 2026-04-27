from typing import Any

from ai_aerostruct.skills.base import BaseSkill, SkillResult


class RuleCheckerSkill(BaseSkill):
    name = "rule_checker"
    description = "根据需求检查气动、强度和挠度是否满足。"

    def run(self, data: dict[str, Any]) -> SkillResult:
        try:
            checks = []

            checks.append({
                "name": "lift_requirement",
                "passed": data["lift_N"] >= data["target_lift_N"],
                "actual": data["lift_N"],
                "required": data["target_lift_N"],
                "unit": "N",
            })

            checks.append({
                "name": "safety_factor",
                "passed": data["safety_factor"] >= data["safety_factor_min"],
                "actual": data["safety_factor"],
                "required": data["safety_factor_min"],
                "unit": "-",
            })

            checks.append({
                "name": "tip_deflection",
                "passed": data["tip_deflection_m"] <= data["max_deflection_m"],
                "actual": data["tip_deflection_m"],
                "required": data["max_deflection_m"],
                "unit": "m",
            })

            passed = all(item["passed"] for item in checks)

            return SkillResult(
                success=True,
                data={
                    "passed": passed,
                    "checks": checks,
                },
            )
        except Exception as exc:
            return SkillResult(success=False, errors=[str(exc)])
