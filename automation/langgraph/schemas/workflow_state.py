from pydantic import BaseModel, Field, ConfigDict
from .common import ArtifactRef, RiskItem
from .enums import WorkflowStage


class RepoContext(BaseModel):
    model_config = ConfigDict(extra="forbid")

    repo_name: str = "tales-of-dusk-automation"
    default_branch: str = "main"
    integration_branch: str = "integration"
    working_branch: str | None = None


class RuntimeInvariant(BaseModel):
    model_config = ConfigDict(extra="forbid")

    main_scene_path: str = "res://scenes/boot/boot.tscn"
    title_scene_path: str = "res://scenes/title/title.tscn"
    chapter_map_scene_path: str = "res://scenes/chapter_map/chapter_map.tscn"
    room_test_scene_path: str = "res://scenes/rooms/room_test.tscn"

    required_autoloads: list[str] = Field(
        default_factory=lambda: ["EventBus", "GameSession", "SaveSystem", "SceneRouter"]
    )

    room_phase_order: list[str] = Field(
        default_factory=lambda: ["Preview", "Deploy", "Combat", "Result"]
    )


class WorkflowState(BaseModel):
    model_config = ConfigDict(extra="forbid")

    thread_id: str
    project_id: str = "tales-of-dusk-automation"
    schema_version: str = "0.1.0"

    current_stage: WorkflowStage = WorkflowStage.BRIEF_INTAKE

    active_artifact_ids: dict[str, str] = Field(default_factory=dict)
    artifact_history: list[ArtifactRef] = Field(default_factory=list)

    open_risks: list[RiskItem] = Field(default_factory=list)
    blockers: list[str] = Field(default_factory=list)

    requires_human_approval: bool = False
    pending_interrupt: dict | None = None

    repo: RepoContext = Field(default_factory=RepoContext)
    runtime_invariants: RuntimeInvariant = Field(default_factory=RuntimeInvariant)