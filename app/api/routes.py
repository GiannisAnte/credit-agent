from fastapi import APIRouter

from app.schemas.requests import AgentRequest
from app.schemas.responses import AgentResponse

router = APIRouter()


@router.get("/health")
def health_check() -> dict[str, str]:
    return {"status": "ok"}


@router.post("/agent", response_model=AgentResponse)
def run_agent(request: AgentRequest) -> AgentResponse:
    #Временная заглушка. Позже тут запуск графа
    last_message = request.messages[-1]

    return AgentResponse(
        session_id=request.session_id,
        status="completed",
        message=f"Запрос принят: {last_message.content}",
    )
