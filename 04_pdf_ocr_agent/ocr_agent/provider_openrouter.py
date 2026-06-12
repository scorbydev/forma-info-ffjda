from __future__ import annotations

import base64
import json
import mimetypes
import os
from pathlib import Path
from typing import Any

import requests
from dotenv import load_dotenv


OPENROUTER_URL = "https://openrouter.ai/api/v1/chat/completions"
IMAGE_EXTENSIONS = {".png", ".jpg", ".jpeg", ".webp"}


def _data_url_from_bytes(data: bytes, mime_type: str) -> str:
    encoded = base64.b64encode(data).decode("ascii")
    return f"data:{mime_type};base64,{encoded}"


def _image_file_to_data_url(path: Path) -> str:
    mime_type = mimetypes.guess_type(path.name)[0] or "image/png"
    return _data_url_from_bytes(path.read_bytes(), mime_type)


def _pdf_pages_to_data_urls(path: Path, max_pages: int) -> list[str]:
    try:
        import fitz
    except ImportError as exc:
        raise RuntimeError("PyMuPDF est requis pour envoyer un PDF a OpenRouter. Lancez pip install -r requirements.txt.") from exc

    data_urls: list[str] = []
    with fitz.open(path) as document:
        page_count = min(len(document), max_pages)
        if page_count == 0:
            raise RuntimeError("PDF vide: aucune page a envoyer au modele vision.")
        for index in range(page_count):
            page = document.load_page(index)
            pixmap = page.get_pixmap(matrix=fitz.Matrix(2, 2), alpha=False)
            data_urls.append(_data_url_from_bytes(pixmap.tobytes("png"), "image/png"))
    return data_urls


def _build_content(path: Path, document_type: str) -> list[dict[str, Any]] | str:
    instruction = (
        "Tu es un extracteur OCR/vision pour documents administratifs fictifs. "
        "Lis le document fourni, extrais uniquement les champs attendus et retourne un JSON strict, sans markdown. "
        f"Type attendu: {document_type}."
    )
    suffix = path.suffix.lower()
    if suffix == ".txt":
        text = path.read_text(encoding="utf-8")
        return f"{instruction}\n\nContenu OCR texte:\n{text}"
    if suffix == ".pdf":
        max_pages = int(os.getenv("OCR_MAX_PAGES", "2"))
        content: list[dict[str, Any]] = [{"type": "text", "text": instruction}]
        for data_url in _pdf_pages_to_data_urls(path, max_pages):
            content.append({"type": "image_url", "image_url": {"url": data_url}})
        return content
    if suffix in IMAGE_EXTENSIONS:
        return [
            {"type": "text", "text": instruction},
            {"type": "image_url", "image_url": {"url": _image_file_to_data_url(path)}},
        ]
    raise RuntimeError("Format non supporte par OpenRouter: utilisez .pdf, .png, .jpg, .jpeg, .webp ou .txt.")


def _parse_json_content(content: str) -> dict:
    cleaned = content.strip()
    if cleaned.startswith("```"):
        cleaned = cleaned.strip("`")
        if cleaned.lower().startswith("json"):
            cleaned = cleaned[4:].strip()
    try:
        return json.loads(cleaned)
    except json.JSONDecodeError as exc:
        raise RuntimeError("OpenRouter n'a pas retourne un JSON strict exploitable.") from exc


def extract(path: str | Path, document_type: str) -> dict:
    load_dotenv()
    api_key = os.getenv("OPENROUTER_API_KEY")
    model = os.getenv("OPENROUTER_MODEL", "mistralai/mistral-small-3.1-24b-instruct:free")
    if not api_key:
        raise RuntimeError("OPENROUTER_API_KEY absent. Configurez .env ou utilisez sample/huggingface.")

    source = Path(path)
    try:
        response = requests.post(
            OPENROUTER_URL,
            headers={
                "Authorization": f"Bearer {api_key}",
                "Content-Type": "application/json",
            },
            json={
                "model": model,
                "messages": [{"role": "user", "content": _build_content(source, document_type)}],
                "temperature": 0,
            },
            timeout=90,
        )
    except requests.RequestException as exc:
        raise RuntimeError(f"Erreur reseau OpenRouter: {exc}") from exc
    if response.status_code >= 400:
        raise RuntimeError(f"Erreur OpenRouter {response.status_code}: {response.text[:500]}")
    content = response.json()["choices"][0]["message"]["content"]
    return _parse_json_content(content)
