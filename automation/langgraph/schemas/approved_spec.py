from pydantic import BaseModel, Field, ConfigDict
from .common import ArtifactHeader, ArtifactRef, RiskItem
from .items import AcceptanceCriterionItem


class ApprovedSpec(BaseModel):
    model_config = ConfigDict(extra="forbid")

    header: ArtifactHeader

    based_on: list[ArtifactRef] = Field(default_factory=list)

    approved_objective: str
    constraints: list[str] = Field(default_factory=list)
    functional_scope: list[str] = Field(default_factory=list)
    technical_mapping: list[str] = Field(default_factory=list)
    non_goals: list[str] = Field(default_factory=list)

    acceptance_criteria: list[AcceptanceCriterionItem] = Field(default_factory=list)
    required_tests: list[str] = Field(default_factory=list)

    open_risks: list[RiskItem] = Field(default_factory=list)