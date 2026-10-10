from typing import Literal, TypedDict


class AgentState(TypedDict, total=False):
    #Идентификаторы диалога и клиента
    session_id: str
    client_id: str

    #Вход текущего запроса
    messages: list[dict[str, str]]
    current_message: str

    #Результаты safety-проверок. None означает, что проверка ещё не выполнена.
    is_trolling: bool | None
    compliance_blocked: bool | None
    prompt_injection_detected: bool | None

    #Извлечённые параметры запроса
    business_goal: str | None
    requested_amount: int | None

    #Результаты классификации
    cluster: str | None
    final_goal: str | None

    #Результаты подбора продуктов
    client_products: list[dict[str, object]] | None
    available_products: list[dict[str, object]] | None

    #Состояние диалога
    pending_question: str | None

    #Результат обработки
    response_status: Literal[
        "completed",
        "clarification_required",
        "blocked",
        "error",
    ]
    response_message: str

    #Контекст, по которому были получены кешируемые результаты. Позже он поможет понять, какие узлы нужно выполнить повторно
    intent_input_snapshot: str | None
    amount_input_snapshot: str | None
    cluster_input_goal: str | None
    cluster_input_amount: int | None
