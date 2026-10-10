from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_health_check() -> None:
    response = client.get("/health")

    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


def test_agent_endpoint() -> None:
    response = client.post(
        "/agent",
        json={
            "session_id": "session-001",
            "client_id": "client-001",
            "messages": [
                {"role": "user", "content": "Нужен кредит на развитие бизнеса"}
            ],
        },
    )

    assert response.status_code == 200
    body = response.json()
    assert body["session_id"] == "session-001"
    assert body["status"] == "completed"
    assert "Нужен кредит на развитие бизнеса" in body["message"]


def test_agent_rejects_invalid_request() -> None:
    response = client.post(
        "/agent",
        json={
            "session_id": "session-001",
            "messages": [{"role": "user", "content": "Привет"}],
        },
    )

    assert response.status_code == 422
