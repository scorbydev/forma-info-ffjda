# Atelier 4 - PDF/OCR agentique

Objectif: faire tourner un modele vision/OCR sur un PDF ou une image de document fictif, extraire des champs structures, valider le resultat et exporter un CSV.

Le scenario nominal utilise OpenRouter avec un modele vision compatible. Le script convertit les pages PDF en images PNG, les envoie au modele via l'API OpenRouter, puis valide la reponse JSON avec Pydantic.

Le mode `sample` est uniquement le fallback offline: il simule une sortie OCR deja extraite sous forme texte. Il sert a continuer l'atelier si l'API, le reseau ou les quotas ne sont pas disponibles.

Le dossier `samples/` contient:

- des fichiers `.txt` utilises par les tests et demos offline avec `sample`;
- de faux fichiers `.pdf` pedagogiques, utilisables avec `openrouter` pour la demo vision/OCR.

Les tests ne dependent pas des PDF reels.

Providers:

- `openrouter`: provider nominal pour vision/OCR PDF ou image via `OPENROUTER_API_KEY`.
- `huggingface`: fallback API via `HF_API_TOKEN` et `HF_MODEL_ID`.
- `sample`: fallback offline deterministe pour tests et demo sans API; il lit les sorties OCR texte deja fournies.

OpenRouter est configurable dans `.env`. Le modele gratuit configure dans `.env.example` doit etre verifie la veille de la formation, car disponibilite et support vision peuvent changer.

## Demo OpenRouter vision sur PDF

Preparer `.env`:

```text
OPENROUTER_API_KEY=...
OPENROUTER_MODEL=mistralai/mistral-small-3.1-24b-instruct:free
OCR_MAX_PAGES=2
```

Puis lancer:

```bash
python 04_pdf_ocr_agent/ocr_agent/cli.py --input 04_pdf_ocr_agent/samples/facture_stage_001.pdf --type invoice --provider openrouter --output 04_pdf_ocr_agent/openrouter_facture.csv
```

Si le modele OpenRouter choisi ne supporte pas les images, choisir un modele vision disponible dans le dashboard OpenRouter et mettre a jour `OPENROUTER_MODEL`.

## Demo offline

```bash
python 04_pdf_ocr_agent/ocr_agent/cli.py --input 04_pdf_ocr_agent/samples/facture_stage_001.txt --type invoice --provider sample --output 04_pdf_ocr_agent/output.csv
```

## Streamlit optionnel

```bash
streamlit run 04_pdf_ocr_agent/app_streamlit.py
```

Les tests n'appellent aucune API externe.
