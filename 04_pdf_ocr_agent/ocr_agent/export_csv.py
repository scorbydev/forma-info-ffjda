from __future__ import annotations

import csv
from pathlib import Path

from .models import ExtractionResult


def export_result(result: ExtractionResult, output_path: str | Path) -> Path:
    output = Path(output_path)
    output.parent.mkdir(parents=True, exist_ok=True)
    payload = result.extraction.model_dump()
    row = {
        "provider": result.provider,
        "source_file": result.source_file,
        **payload,
        "warnings": "; ".join(payload.get("warnings", [])),
    }
    with output.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(row.keys()))
        writer.writeheader()
        writer.writerow(row)
    return output

