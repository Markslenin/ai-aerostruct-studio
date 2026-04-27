import json
from pathlib import Path

from ai_aerostruct.skills.aero_solver import SimpleAeroSolverSkill
from ai_aerostruct.skills.registry import SkillRegistry
from ai_aerostruct.skills.rule_checker import RuleCheckerSkill
from ai_aerostruct.skills.structure_solver import SimpleStructureSolverSkill


def main() -> None:
    spec = json.loads(Path("examples/sample_design_spec.json").read_text(encoding="utf-8"))

    registry = SkillRegistry()
    registry.register(SimpleAeroSolverSkill())
    registry.register(SimpleStructureSolverSkill())
    registry.register(RuleCheckerSkill())

    geom = spec["geometry"]
    aero = spec["aero"]
    mat = spec["material"]
    struct = spec["structure"]

    aero_input = {**geom, **aero}
    aero_result = registry.get("simple_aero_solver").run(aero_input)
    print("AERO:", aero_result.model_dump())

    structure_input = {
        **geom,
        **mat,
        **struct,
        "lift_N": aero_result.data["lift_N"],
    }
    structure_result = registry.get("simple_structure_solver").run(structure_input)
    print("STRUCTURE:", structure_result.model_dump())

    check_input = {
        **aero,
        **struct,
        **aero_result.data,
        **structure_result.data,
    }
    check_result = registry.get("rule_checker").run(check_input)
    print("CHECK:", check_result.model_dump())


if __name__ == "__main__":
    main()
