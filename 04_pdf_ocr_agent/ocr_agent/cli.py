from __future__ import annotations

import argparse
from pathlib import Path

if __package__ in (None, ""):
    import sys

    sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
    from ocr_agent.export_csv import export_result
    from ocr_agent.pipeline import extract_with_provider
else:
    from .export_csv import export_result
    from .pipeline import extract_with_provider


def main() -> None:
    parser = argparse.ArgumentParser(description="Extraction documentaire pedagogique.")
    parser.add_argument("--input", required=True, help="Fichier texte OCR fictif")
    parser.add_argument("--type", required=True, choices=["invoice", "license"], help="Type document")
    parser.add_argument(
        "--provider",
        default="sample",
        choices=["sample", "openrouter", "huggingface"],
        help="Provider d'extraction",
    )
    parser.add_argument("--output", required=True, help="CSV de sortie")
    args = parser.parse_args()

    try:
        result = extract_with_provider(args.input, args.type, args.provider)
    except Exception as exc:
        raise SystemExit(f"Extraction impossible avec provider={args.provider}: {exc}") from exc
    output = export_result(result, args.output)
    print(f"Extraction OK: provider={result.provider}, type={args.type}, output={output}")
    print(result.extraction.model_dump_json(indent=2))


if __name__ == "__main__":
    main()
