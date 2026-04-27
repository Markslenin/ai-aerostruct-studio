from pydantic import BaseModel, Field


class GeometrySpec(BaseModel):
    wing_type: str = "trapezoidal"
    span_m: float = Field(gt=0)
    root_chord_m: float = Field(gt=0)
    tip_chord_m: float = Field(gt=0)
    thickness_m: float = Field(gt=0)
    sweep_deg: float = 0.0
    dihedral_deg: float = 0.0
    airfoil: str = "NACA2412"


class AeroSpec(BaseModel):
    velocity_mps: float = Field(gt=0)
    air_density_kg_m3: float = Field(default=1.225, gt=0)
    alpha_deg: float = 5.0
    target_lift_N: float = Field(gt=0)


class MaterialSpec(BaseModel):
    name: str = "7075-T6 Aluminum"
    elastic_modulus_pa: float = Field(default=71.7e9, gt=0)
    yield_strength_pa: float = Field(default=505e6, gt=0)
    density_kg_m3: float = Field(default=2810, gt=0)


class StructureSpec(BaseModel):
    safety_factor_min: float = Field(default=1.5, gt=0)
    max_deflection_m: float = Field(default=0.002, gt=0)
    spar_height_m: float = Field(default=0.02, gt=0)
    spar_width_m: float = Field(default=0.003, gt=0)


class DesignSpec(BaseModel):
    project_name: str = "demo_wing"
    geometry: GeometrySpec
    aero: AeroSpec
    material: MaterialSpec = MaterialSpec()
    structure: StructureSpec = StructureSpec()
