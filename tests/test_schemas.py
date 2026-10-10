import pytest
from pydantic import ValidationError

from app.schemas.requests import AgentRequest
from app.schemas.responses import AgentResponse


def test_valid_agent_request() -> None:
    request = AgentRequest(
        session_id="session-001",
        client_id="client-001",
        messages=[{"role": "user", "content": "Нужен кредит на развитие бизнеса"}],
    )

    assert request.session_id == "session-001"
    assert request.messages[0].role == "user"


def test_request_rejects_unknown_fields() -> None:
    with pytest.raises(ValidationError):
        AgentRequest(
            session_id="session-001",
            client_id="client-001",
            messages=[{"role": "user", "content": "Привет"}],
            unexpected_field="value",
        )


def test_response_with_clarification() -> None:
    response = AgentResponse(
        session_id="session-001",
        status="clarification_required",
        message="Для какой цели нужен кредит?",
        pending_question="Для какой цели нужен кредит?",
    )

    assert response.status == "clarification_required"


def test_response_rejects_invalid_status() -> None:
    with pytest.raises(ValidationError):
        AgentResponse(
            session_id="session-001",
            status="unknown",
            message="Ответ",
        )
