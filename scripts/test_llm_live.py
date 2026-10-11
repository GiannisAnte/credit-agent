from langchain_core.messages import HumanMessage, SystemMessage

from app.services.llm import get_chat_model


def main() -> None:
    model = get_chat_model()

    messages = [
        SystemMessage(
            content=(
                "Ты помощник по извлечению параметров кредитного запроса. "
                "Отвечай кратко и по-русски."
            )
        ),
        HumanMessage(
            content=(
                "Клиент пишет: «Нужен кредит на развитие бизнеса "
                "на 2 миллиона рублей». "
                "Определи цель кредита и запрошенную сумму."
            )
        ),
    ]

    response = model.invoke(messages)

    print("\n=== Ответ LLM ===")
    print(response.content)
    print("\n=== Метаданные ===")
    print(f"Модель: {response.response_metadata.get('model_name', 'не указана')}")
    print(f"Токены: {response.usage_metadata}")


if __name__ == "__main__":
    main()
