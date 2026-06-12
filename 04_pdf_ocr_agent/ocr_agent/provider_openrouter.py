from __future__ import annotations

import json
import os
from pathlib import Path

import requests
from dotenv import load_dotenv


OPENROUTER_URL = "https://openrouter.ai/api/v1/chat/completions"


def extract(path: str | Path, document_type: str) -> dict:
    load_dotenv()
    api_key = os.getenv("OPENROUTER_API_KEY")
    model = os.getenv("OPENROUTER_MODEL", "mistralai/mistral-small-3.1-24b-instruct:free")
    if not api_key:
        raise RuntimeError("OPENROUTER_API_KEY absent. Configurez .env ou utilisez sample/huggingface.")

    text = Path(path).read_text(encoding="utf-8")
    prompt = (
        "Extrais les champs du document fictif suivant en JSON strict. "
        f"Type attendu: {document_type}. Ne renvoie aucun texte hors JSON.\n\n{text}"
    )
    try:
        response = requests.post(
            OPENROUTER_URL,
            headers={
                "Authorization": f"Bearer {api_key}",
                "Content-Type": "application/json",
            },
            json={
                "model": model,
                "messages": [{"role": "user", "content": prompt}],
                "temperature": 0,
            },
            timeout=60,
        )
    except requests.RequestException as exc:
        raise RuntimeError(f"Erreur reseau OpenRouter: {exc}") from exc
    if response.status_code >= 400:
        raise RuntimeError(f"Erreur OpenRouter {response.status_code}: {response.text[:500]}")
    content = response.json()["choices"][0]["message"]["content"]
    try:
        return json.loads(content)
    except json.JSONDecodeError as exc:
        raise RuntimeError("OpenRouter n'a pas retourne un JSON strict exploitable.") from exc
