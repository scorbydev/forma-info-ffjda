from __future__ import annotations

import json
import os
from pathlib import Path

import requests
from dotenv import load_dotenv


def extract(path: str | Path, document_type: str) -> dict:
    load_dotenv()
    token = os.getenv("HF_API_TOKEN")
    model_id = os.getenv("HF_MODEL_ID")
    if not token:
        raise RuntimeError("HF_API_TOKEN absent. Configurez .env ou utilisez le provider sample.")
    if not model_id:
        raise RuntimeError("HF_MODEL_ID absent. Configurez .env avec un modele Hugging Face compatible.")

    text = Path(path).read_text(encoding="utf-8")
    prompt = (
        "Extrais les champs du document fictif en JSON strict. "
        f"Type attendu: {document_type}.\n\n{text}"
    )
    try:
        response = requests.post(
            f"https://api-inference.huggingface.co/models/{model_id}",
            headers={"Authorization": f"Bearer {token}"},
            json={"inputs": prompt, "parameters": {"return_full_text": False}},
            timeout=60,
        )
    except requests.RequestException as exc:
        raise RuntimeError(f"Erreur reseau Hugging Face: {exc}") from exc
    if response.status_code >= 400:
        raise RuntimeError(f"Erreur Hugging Face {response.status_code}: {response.text[:500]}")
    payload = response.json()
    if isinstance(payload, list) and payload and isinstance(payload[0], dict):
        generated = payload[0].get("generated_text")
        if isinstance(generated, str):
            try:
                return json.loads(generated)
            except json.JSONDecodeError as exc:
                raise RuntimeError("Hugging Face n'a pas retourne un JSON strict exploitable.") from exc
    if isinstance(payload, dict) and "generated_text" in payload:
        try:
            return json.loads(payload["generated_text"])
        except json.JSONDecodeError as exc:
            raise RuntimeError("Hugging Face n'a pas retourne un JSON strict exploitable.") from exc
    return payload
