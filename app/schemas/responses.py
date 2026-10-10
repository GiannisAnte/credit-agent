
from typing import Literal

from pydantic import BaseModel, ConfigDict, Field


class AgentResponse(BaseModel):
    model_config = ConfigDict(extra="forbid")

    session_id: str
    status: Literal["completed", "clarification_required", "blocked", "error"]
    message: str = Field(min_length=1)
    pending_question: str | None = None
