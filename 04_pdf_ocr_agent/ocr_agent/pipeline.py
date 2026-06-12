from __future__ import annotations

from pathlib import Path
from typing import Any

from .models import ExtractionResult, InvoiceExtraction, LicenseExtraction
from .provider_sample import extract as sample_extract


def _coerce_payload(raw: Any, document_type: str) -> dict[str, Any]:
    if not isinstance(raw, dict):
        raise ValueError("Le provider API doit retourner un objet JSON.")
    if "extraction" in raw and isinstance(raw["extraction"], dict):
        raw = raw["extraction"]
    if document_type == "invoice":
        raw.setdefault("document_type", "invoice")
    elif document_type == "license":
        raw.setdefault("document_type", "license")
    else:
        raise ValueError("document_type doit etre invoice ou license")
    raw.setdefault("confidence", 0.0)
    raw.setdefault("warnings", ["Extraction API a controler manuellement."])
    return raw


def result_from_api_payload(
    raw: Any,
    provider: str,
    source_file: str | Path,
    document_type: str,
) -> ExtractionResult:
    payload = _coerce_payload(raw, document_type)
    if document_type == "invoice":
        extraction = InvoiceExtraction.model_validate(payload)
    else:
        extraction = LicenseExtraction.model_validate(payload)
    return ExtractionResult(
        provider=provider,
        source_file=str(source_file),
        extraction=extraction,
    )


def extract_with_provider(
    path: str | Path,
    document_type: str,
    provider: str,
) -> ExtractionResult:
    if provider == "sample":
        if Path(path).suffix.lower() != ".txt":
            raise ValueError("Le provider sample lit uniquement les fichiers .txt OCR simules. Utilisez openrouter pour PDF/image.")
        return sample_extract(path, document_type)
    if provider == "openrouter":
        from .provider_openrouter import extract

        return result_from_api_payload(extract(path, document_type), provider, path, document_type)
    if provider == "huggingface":
        from .provider_huggingface import extract

        return result_from_api_payload(extract(path, document_type), provider, path, document_type)
    raise ValueError("provider doit etre sample, openrouter ou huggingface")
