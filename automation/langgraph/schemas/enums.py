from enum import StrEnum


class WorkflowStage(StrEnum):
    BRIEF_INTAKE = "brief_intake"
    PROPOSAL = "proposal"
    REVIEW = "review"
    APPROVED_SPEC = "approved_spec"
    CODEX_TASKING = "codex_tasking"
    IMPLEMENTATION = "implementation"
    QA = "qa"
    ACCEPTANCE = "acceptance"
    RELEASE_READY = "release_ready"


class ArtifactType(StrEnum):
    DESIGN_BRIEF = "design_brief"
    PROPOSAL = "proposal"
    REVIEW = "review"
    APPROVED_SPEC = "approved_spec"
    CODEX_TASK = "codex_task"
    QA_REPORT = "qa_report"
    ACCEPTANCE_REPORT = "acceptance_report"
    CHANGE_REQUEST = "change_request"


class ArtifactStatus(StrEnum):
    DRAFT = "draft"
    IN_REVIEW = "in_review"
    APPROVED = "approved"
    REJECTED = "rejected"
    SUPERSEDED = "superseded"
    IMPLEMENTED = "implemented"
    ARCHIVED = "archived"


class ReviewDecision(StrEnum):
    APPROVE = "approve"
    REVISE = "revise"
    REJECT = "reject"


class Severity(StrEnum):
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"
    CRITICAL = "critical"