from automation.langgraph.schemas.common import ArtifactHeader
from automation.langgraph.schemas.enums import ArtifactType, ArtifactStatus


def test_header_model():
    header = ArtifactHeader(
        artifact_id="BRF-0001",
        artifact_type=ArtifactType.DESIGN_BRIEF,
        version="1.0.0",
        status=ArtifactStatus.DRAFT,
        workflow_thread_id="bootstrap-phase3",
        author_role="BriefInterpreter",
        created_at="2026-03-09T00:00:00Z",
        updated_at="2026-03-09T00:00:00Z",
    )
    assert header.artifact_id == "BRF-0001"