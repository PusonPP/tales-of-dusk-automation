from pydantic import BaseModel, Field, ConfigDict
from .common import ArtifactHeader, ArtifactRef
from .items import FindingItem, ReviewOutcome


class Review(BaseModel):
    model_config = ConfigDict(extra="forbid")

    header: ArtifactHeader

    review_target: ArtifactRef
    findings: list[FindingItem] = Field(default_factory=list)
    blocking_issues: list[str] = Field(default_factory=list)
    non_blocking_issues: list[str] = Field(default_factory=list)

    outcome: ReviewOutcome
    required_revisions: list[str] = Field(default_factory=list)