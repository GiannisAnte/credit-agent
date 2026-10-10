from fastapi import APIRouter

from app.graph.builder import build_graph
from app.graph.state import AgentState
from app.schemas.requests import AgentRequest
from app.schemas.responses import AgentResponse

router = APIRouter()

#Граф собирается один раз при загрузке приложения.
graph = build_graph()


@router.get("/health")
def health_check() -> dict[str, str]:
    return {"status": "ok"}


@router.post("/agent", response_model=AgentResponse)
def run_agent(request: AgentRequest) -> AgentResponse:
    current_message = next(
        (
            message.content
            for message in reversed(request.messages)
            if message.role == "user"
        ),
        request.messages[-1].content,
    )

    initial_state: AgentState = {
        "session_id": request.session_id,
        "client_id": request.client_id,
        "messages": [
            message.model_dump() for message in request.messages
        ],
        "current_message": current_message,
    }

    result = graph.invoke(initial_state)

    return AgentResponse(
        session_id=request.session_id,
        status=result["response_status"],
        message=result["response_message"],
        pending_question=result.get("pending_question"),
    )
