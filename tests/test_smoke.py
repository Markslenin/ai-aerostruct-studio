from ai_aerostruct.skills.aero_solver import SimpleAeroSolverSkill


def test_simple_aero_solver_smoke():
    skill = SimpleAeroSolverSkill()
    result = skill.run({
        "span_m": 1.2,
        "root_chord_m": 0.24,
        "tip_chord_m": 0.14,
        "velocity_mps": 30,
        "air_density_kg_m3": 1.225,
        "alpha_deg": 6,
    })
    assert result.success
    assert result.data["lift_N"] > 0
