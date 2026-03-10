from pydantic import BaseModel, Field, ConfigDict
from .common import ArtifactHeader, ArtifactRef
from .items import CompatibilityImpactItem


class ChangeRequest(BaseModel):
    model_config = ConfigDict(extra="forbid")

    header: ArtifactHeader

    based_on: list[ArtifactRef] = Field(default_factory=list)

    requested_change: str
    reason: str
    affected_systems: list[str] = Field(default_factory=list)
    compatibility_impacts: list[CompatibilityImpactItem] = Field(default_factory=list)

    scope_change: str
    required_approval: list[str] = Field(default_factory=list)