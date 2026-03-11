import re
from pathlib import Path

from automation.langgraph.schemas.common import ArtifactRef
from automation.langgraph.schemas.enums import ArtifactType, WorkflowStage
from automation.langgraph.schemas.workflow_state import WorkflowState

REPO_ROOT = Path(__file__).resolve().parents[3]

BRIEF_PATH = "docs/examples/BRF-0001_bootstrap-protocols_v1.0.0.md"
PROPOSAL_PATH = "docs/examples/PRP-0001_protocol-schema_v1.0.0.md"
REVIEW_PATH = "docs/examples/RVW-0001_protocol-schema_v1.0.0.md"
SPEC_PATH = "docs/examples/SPEC-0001_protocol-schema_v1.0.0.md"


def _artifact_ref(
    artifact_id: str,
    artifact_type: ArtifactType,
    version: str,
    path: str,
) -> ArtifactRef:
    return ArtifactRef(
        artifact_id=artifact_id,
        artifact_type=artifact_type,
        version=version,
        path=path,
    )


def _append_artifact(
    state: WorkflowState,
    key: str,
    ref: ArtifactRef,
) -> dict:
    active = dict(state.active_artifact_ids)
    active[key] = ref.artifact_id

    history = list(state.artifact_history)
    history.append(ref)

    return {
        "active_artifact_ids": active,
        "artifact_history": history,
    }


def _read_text(rel_path: str) -> str:
    return (REPO_ROOT / rel_path).read_text(encoding="utf-8")


def _extract_review_decision() -> str:
    text = _read_text(REVIEW_PATH).lower()

    patterns = [
        r"\*\*decision:\*\*\s*(approve|revise|reject)",
        r"decision:\s*(approve|revise|reject)",
    ]

    for pattern in patterns:
        match = re.search(pattern, text)
        if match:
            return match.group(1)

    return "unknown"


def validate_repo_baseline(state: WorkflowState) -> dict:
    required = [
        "docs/protocols/automation_protocol.md",
        "docs/protocols/workflow_stage_machine.md",
        BRIEF_PATH,
        PROPOSAL_PATH,
        REVIEW_PATH,
        SPEC_PATH,
        "automation/langgraph/schemas/workflow_state.py",
        "automation/scripts/validate_protocols.py",
        "game/tales-of-dusk/project.godot",
    ]

    missing = [p for p in required if not (REPO_ROOT / p).exists()]
    blockers = list(state.blockers)

    if missing:
        blockers.append(f"Missing required files: {', '.join(missing)}")

    return {"blockers": blockers}


def load_design_brief(state: WorkflowState) -> dict:
    ref = _artifact_ref(
        "BRF-0001",
        ArtifactType.DESIGN_BRIEF,
        "1.0.0",
        BRIEF_PATH,
    )

    update = _append_artifact(state, "design_brief", ref)
    update["current_stage"] = WorkflowStage.PROPOSAL
    return update


def register_proposal(state: WorkflowState) -> dict:
    ref = _artifact_ref(
        "PRP-0001",
        ArtifactType.PROPOSAL,
        "1.0.0",
        PROPOSAL_PATH,
    )

    update = _append_artifact(state, "proposal", ref)
    update["current_stage"] = WorkflowStage.REVIEW
    return update


def register_review(state: WorkflowState) -> dict:
    ref = _artifact_ref(
        "RVW-0001",
        ArtifactType.REVIEW,
        "1.0.0",
        REVIEW_PATH,
    )

    update = _append_artifact(state, "review", ref)
    return update


def route_after_baseline(state: WorkflowState) -> str:
    return "halt_on_blocker" if state.blockers else "load_design_brief"


def route_after_review(state: WorkflowState) -> str:
    decision = _extract_review_decision()
    return "register_approved_spec" if decision == "approve" else "rollback_stop"


def halt_on_blocker(state: WorkflowState) -> dict:
    return {
        "current_stage": WorkflowStage.BRIEF_INTAKE,
    }


def rollback_stop(state: WorkflowState) -> dict:
    blockers = list(state.blockers)
    blockers.append("Review outcome did not approve progression to approved_spec.")
    return {
        "blockers": blockers,
        "current_stage": WorkflowStage.REVIEW,
    }


def register_approved_spec(state: WorkflowState) -> dict:
    ref = _artifact_ref(
        "SPEC-0001",
        ArtifactType.APPROVED_SPEC,
        "1.0.0",
        SPEC_PATH,
    )

    update = _append_artifact(state, "approved_spec", ref)
    update["current_stage"] = WorkflowStage.APPROVED_SPEC
    return update


def promote_to_codex_tasking(state: WorkflowState) -> dict:
    return {
        "current_stage": WorkflowStage.CODEX_TASKING,
    }