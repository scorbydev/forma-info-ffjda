from __future__ import annotations

import json
from pathlib import Path
import tempfile

import streamlit as st

from ocr_agent.export_csv import export_result
from ocr_agent.pipeline import extract_with_provider


st.set_page_config(page_title="OCR agentique sandbox", layout="wide")
st.title("OCR agentique sandbox")

uploaded = st.file_uploader("Document fictif", type=["txt", "pdf", "png", "jpg", "jpeg", "webp"])
document_type = st.selectbox("Type document", ["invoice", "license"])
provider = st.selectbox("Provider", ["sample", "openrouter", "huggingface"])

if uploaded and st.button("Extraire"):
    with tempfile.TemporaryDirectory() as tmp:
        input_path = Path(tmp) / uploaded.name
        input_path.write_bytes(uploaded.read())

        try:
            result = extract_with_provider(input_path, document_type, provider)
            csv_path = export_result(result, Path(tmp) / "extraction.csv")
        except Exception as exc:
            st.error(f"Extraction impossible avec provider={provider}: {exc}")
            st.stop()

        st.json(json.loads(result.extraction.model_dump_json()))
        st.download_button(
            "Telecharger CSV",
            data=csv_path.read_bytes(),
            file_name="extraction.csv",
            mime="text/csv",
        )
