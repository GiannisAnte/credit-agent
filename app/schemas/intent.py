from typing import Literal

from pydantic import BaseModel, ConfigDict, Field


class ExtractedIntent(BaseModel):
    model_config = ConfigDict(extra="forbid")

    business_goal: str | None = Field(
        default=None,
        description="Цель кредита, извлечённая из сообщения пользователя",
    )
    requested_amount: int | None = Field(
        default=None,
        ge=1,
        description="Запрашиваемая сумма кредита в рублях",
    )
    clarification_field: Literal[
        "business_goal",
        "requested_amount",
        "none",
    ] = "none"
