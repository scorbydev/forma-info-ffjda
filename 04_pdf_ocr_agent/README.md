# Atelier 4 - PDF/OCR agentique

Objectif: extraire des champs structures depuis des documents fictifs, valider le resultat et exporter un CSV.

L'exercice ne porte pas sur la qualite OCR brute. Le mode `sample` simule une sortie OCR deja extraite sous forme texte. Le travail principal est l'extraction structuree, la validation des champs et l'export de controle.

Le dossier `samples/` contient:

- des fichiers `.txt` utilises par les tests et demos offline;
- de faux fichiers `.pdf` pedagogiques, generes a partir des memes contenus texte, uniquement pour montrer le type de document attendu.

Les tests ne dependent pas des PDF reels.

Providers:

- `sample`: provider offline deterministe pour tests et demo sans API; il lit les sorties OCR texte deja fournies.
- `openrouter`: provider optionnel via `OPENROUTER_API_KEY`.
- `huggingface`: fallback API via `HF_API_TOKEN` et `HF_MODEL_ID`.

OpenRouter est optionnel. Le modele gratuit configure dans `.env.example` doit etre verifie la veille de la formation.

## Demo offline

```bash
python 04_pdf_ocr_agent/ocr_agent/cli.py --input 04_pdf_ocr_agent/samples/facture_stage_001.txt --type invoice --provider sample --output 04_pdf_ocr_agent/output.csv
```

## Streamlit optionnel

```bash
streamlit run 04_pdf_ocr_agent/app_streamlit.py
```

Les tests n'appellent aucune API externe.
