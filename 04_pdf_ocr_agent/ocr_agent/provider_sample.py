from __future__ import annotations

from pathlib import Path

from .models import ExtractionResult, InvoiceExtraction, LicenseExtraction


def _parse_key_values(text: str) -> dict[str, str]:
    values: dict[str, str] = {}
    for line in text.splitlines():
        if ":" in line:
            key, value = line.split(":", 1)
            values[key.strip().lower()] = value.strip()
    return values


def extract(path: str | Path, document_type: str) -> ExtractionResult:
    source = Path(path)
    text = source.read_text(encoding="utf-8")
    values = _parse_key_values(text)

    if document_type == "invoice":
        extraction = InvoiceExtraction(
            document_type="invoice",
            supplier=values["fournisseur"],
            invoice_number=values["facture"],
            invoice_date=values["date"],
            amount_ht=float(values["montant ht"]),
            vat=float(values["tva"]),
            amount_ttc=float(values["montant ttc"]),
            cost_center=values["centre de cout"],
            action=values["action"],
            confidence=0.98,
            warnings=[],
        )
    elif document_type == "license":
        extraction = LicenseExtraction(
            document_type="license",
            licence_number=values["numero licence"],
            first_name=values["prenom"],
            last_name=values["nom"],
            club=values["club"],
            season=values["saison"],
            detected_issue=values["anomalie"],
            confidence=0.96,
            warnings=[],
        )
    else:
        raise ValueError("document_type doit etre invoice ou license")

    return ExtractionResult(provider="sample", source_file=str(source), extraction=extraction)

