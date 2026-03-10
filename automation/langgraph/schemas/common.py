from pydantic import BaseModel, Field, ConfigDict
from .enums import ArtifactType, ArtifactStatus, Severity


class ArtifactHeader(BaseModel):
    model_config = ConfigDict(extra="forbid")

    artifact_id: str
    artifact_type: ArtifactType
    version: str
    status: ArtifactStatus
    project_id: str = "tales-of-dusk-automation"
    workflow_thread_id: str
    author_role: str
    created_at: str
    updated_at: str
    supersedes: str | None = None
    related_artifacts: list[str] = Field(default_factory=list)


class RiskItem(BaseModel):
    model_config = ConfigDict(extra="forbid")

    risk_id: str
    title: str
    severity: Severity
    owner_role: str
    mitigation: str
    is_open: bool = True


class ArtifactRef(BaseModel):
    model_config = ConfigDict(extra="forbid")

    artifact_id: str
    artifact_type: ArtifactType
    version: str
    path: str