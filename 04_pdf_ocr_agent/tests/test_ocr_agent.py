import csv
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from ocr_agent.export_csv import export_result  # noqa: E402
from ocr_agent.pipeline import result_from_api_payload  # noqa: E402
from ocr_agent.provider_sample import extract  # noqa: E402


def test_sample_invoice_extraction():
    result = extract(ROOT / "samples" / "facture_stage_001.txt", "invoice")
    assert result.provider == "sample"
    assert result.extraction.supplier == "Formation Tatami Conseil"
    assert result.extraction.invoice_number == "FAC-2026-001"
    assert result.extraction.amount_ttc == 1440.00


def test_sample_license_extraction():
    result = extract(ROOT / "samples" / "licence_erreur_003.txt", "license")
    assert result.extraction.licence_number == "LIC-2026-0007"
    assert result.extraction.club == "JC Mont-Riviere"
    assert "statut licence" in result.extraction.detected_issue


def test_export_csv():
    result = extract(ROOT / "samples" / "facture_stage_001.txt", "invoice")
    output = ROOT / "output_test.csv"
    try:
        export_result(result, output)
        rows = list(csv.DictReader(output.open(encoding="utf-8")))
        assert len(rows) == 1
        assert rows[0]["invoice_number"] == "FAC-2026-001"
    finally:
        if output.exists():
            output.unlink()


def test_api_payload_validation_for_invoice():
    result = result_from_api_payload(
        {
            "supplier": "Formation Tatami Conseil",
            "invoice_number": "FAC-2026-001",
            "invoice_date": "2026-01-15",
            "amount_ht": 1200,
            "vat": 240,
            "amount_ttc": 1440,
            "cost_center": "FORM-REG-EST",
            "action": "Stage arbitrage regional",
        },
        "openrouter",
        "sample.txt",
        "invoice",
    )
    assert result.provider == "openrouter"
    assert result.extraction.document_type == "invoice"
    assert result.extraction.confidence == 0.0
