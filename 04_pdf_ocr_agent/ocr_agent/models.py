from __future__ import annotations

from typing import Literal

from pydantic import BaseModel, Field


class InvoiceExtraction(BaseModel):
    document_type: Literal["invoice"]
    supplier: str
    invoice_number: str
    invoice_date: str
    amount_ht: float
    vat: float
    amount_ttc: float
    cost_center: str
    action: str
    confidence: float = Field(ge=0.0, le=1.0)
    warnings: list[str] = Field(default_factory=list)


class LicenseExtraction(BaseModel):
    document_type: Literal["license"]
    licence_number: str
    first_name: str
    last_name: str
    club: str
    season: str
    detected_issue: str
    confidence: float = Field(ge=0.0, le=1.0)
    warnings: list[str] = Field(default_factory=list)


class ExtractionResult(BaseModel):
    provider: str
    source_file: str
    extraction: InvoiceExtraction | LicenseExtraction
