
import os
import urllib.request
import json
from pathlib import Path

from dotenv import dotenv_values

env = dotenv_values(".env")
api_key = env.get("LLM_API_KEY") or os.getenv("LLM_API_KEY")
base_url = env.get("LLM_BASE_URL") or os.getenv("LLM_BASE_URL")
base_url = (base_url or "https://api.groq.com/openai/v1").rstrip("/")

if not api_key:
    raise RuntimeError("LLM_API_KEY не найден")

payload = json.dumps({
    "model": "llama-3.3-70b-versatile",
    "messages": [
        {"role": "user", "content": "Ответь одним словом: привет"}
    ],
}).encode("utf-8")

request = urllib.request.Request(
    f"{base_url}/chat/completions",
    data=payload,
    headers={
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json",
    },
    method="POST",
)

# На время проверки не используем системный прокси.
opener = urllib.request.build_opener(
    urllib.request.ProxyHandler({})
)

try:
    with opener.open(request, timeout=30) as response:
        print("HTTP:", response.status)
        print(response.read().decode("utf-8"))
except Exception as exc:
    print("Ошибка:", exc)
    if hasattr(exc, "read"):
        print("Ответ сервера:", exc.read().decode("utf-8", errors="replace"))
