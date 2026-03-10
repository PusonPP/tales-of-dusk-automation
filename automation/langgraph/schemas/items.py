from pydantic import BaseModel, Field, ConfigDict
from .enums import Severity, ReviewDecision


class AcceptanceCriterionItem(BaseModel):
    model_config = ConfigDict(extra="forbid")

    criterion_id: str
    description: str
    is_blocking: bool = True


class VerificationStepItem(BaseModel):
    model_config = ConfigDict(extra="forbid")

    step_id: str
    description: str
    expected_result: str


class FileScopeRule(BaseModel):
    model_config = ConfigDict(extra="forbid")

    path: str
    reason: str


class FindingItem(BaseModel):
    model_config = ConfigDict(extra="forbid")

    finding_id: str
    title: str
    severity: Severity
    description: str
    is_blocking: bool = False


class ReviewOutcome(BaseModel):
    model_config = ConfigDict(extra="forbid")

    decision: ReviewDecision
    summary: str


class ScenarioResultItem(BaseModel):
    model_config = ConfigDict(extra="forbid")

    scenario_id: str
    name: str
    passed: bool
    notes: str = ""


class CompatibilityImpactItem(BaseModel):
    model_config = ConfigDict(extra="forbid")

    area: str
    impact: str
    risk_level: Severity
    mitigation: str