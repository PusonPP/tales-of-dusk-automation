from pydantic import BaseModel, Field, ConfigDict
from .common import ArtifactHeader, ArtifactRef
from .enums import ReviewDecision


class AcceptanceReport(BaseModel):
    model_config = ConfigDict(extra="forbid")

    header: ArtifactHeader

    based_on: list[ArtifactRef] = Field(default_factory=list)

    scope_checked: list[str] = Field(default_factory=list)
    evidence_reviewed: list[str] = Field(default_factory=list)
    blocking_failures: list[str] = Field(default_factory=list)

    decision: ReviewDecision
    release_recommendation: str