from pydantic import BaseModel, Field, ConfigDict
from .common import ArtifactHeader, RiskItem


class DesignBrief(BaseModel):
    model_config = ConfigDict(extra="forbid")

    header: ArtifactHeader

    objective: str
    high_level_inputs: list[str] = Field(default_factory=list)
    non_negotiables: list[str] = Field(default_factory=list)
    out_of_scope: list[str] = Field(default_factory=list)
    success_conditions: list[str] = Field(default_factory=list)
    open_questions: list[str] = Field(default_factory=list)

    known_risks: list[RiskItem] = Field(default_factory=list)