from pydantic import BaseModel, Field, ConfigDict
from .common import ArtifactHeader, ArtifactRef
from .enums import WorkflowStage
from .items import AcceptanceCriterionItem, VerificationStepItem, FileScopeRule


class CodexTask(BaseModel):
    model_config = ConfigDict(extra="forbid")

    header: ArtifactHeader

    based_on: list[ArtifactRef] = Field(default_factory=list)

    background: str
    current_context: str
    current_phase: WorkflowStage

    objective: str
    non_goals: list[str] = Field(default_factory=list)

    allowed_files: list[FileScopeRule] = Field(default_factory=list)
    forbidden_files: list[FileScopeRule] = Field(default_factory=list)

    acceptance_criteria: list[AcceptanceCriterionItem] = Field(default_factory=list)
    verification_steps: list[VerificationStepItem] = Field(default_factory=list)

    reviewer_role: str