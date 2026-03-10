from pydantic import BaseModel, Field, ConfigDict
from .common import ArtifactHeader, ArtifactRef, RiskItem


class Proposal(BaseModel):
    model_config = ConfigDict(extra="forbid")

    header: ArtifactHeader

    based_on: list[ArtifactRef] = Field(default_factory=list)

    proposal_summary: str
    assumptions: list[str] = Field(default_factory=list)
    alternatives_considered: list[str] = Field(default_factory=list)
    recommendation: str

    scope_impact: list[str] = Field(default_factory=list)
    technical_impact: list[str] = Field(default_factory=list)

    known_risks: list[RiskItem] = Field(default_factory=list)