from pydantic import BaseModel, Field, ConfigDict
from .common import ArtifactHeader, ArtifactRef
from .items import ScenarioResultItem, FindingItem


class QAReport(BaseModel):
    model_config = ConfigDict(extra="forbid")

    header: ArtifactHeader

    based_on: list[ArtifactRef] = Field(default_factory=list)

    build_under_test: str
    scenarios_tested: list[ScenarioResultItem] = Field(default_factory=list)

    passes: list[str] = Field(default_factory=list)
    failures: list[FindingItem] = Field(default_factory=list)
    regression_notes: list[str] = Field(default_factory=list)