
from typing import Literal, TypedDict


class AgentState(TypedDict, total=False):
    # Идентификаторы диалога и клиента
    session_id: str
    client_id: str

    # История и текущее сообщение
    messages: list[dict[str, str]]
    current_message: str

    # Результаты проверок безопасности для текущего сообщения
    is_trolling: bool | None
    is_compliance: bool | None
    prompt_injection: bool | None

    # Результаты извлечения бизнес-параметров
    business_goal: str | None
    requested_amount: int | None

    # Результаты определения продукта
    cluster: str | None
    final_goal: str | None
    client_products: list[dict[str, object]] | None
    available_products: list[dict[str, object]] | None

    # Состояние уточняющего диалога
    pending_question: str | None
    pending_field: Literal["business_goal", "requested_amount", "cluster"] | None

    # Служебные данные для определения актуальности результатов
    intent_input_snapshot: str | None
    amount_input_snapshot: str | None
    cluster_input_goal: str | None
    cluster_input_amount: int | None

    # Результат текущего выполнения графа
    response_status: Literal[
        "completed",
        "clarification_required",
        "blocked",
        "error",
    ]
    response_message: str
