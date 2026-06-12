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

## Modeles API a tester pour la demo OCR/vision

La disponibilite des modeles gratuits peut changer. Tester le modele retenu la veille de la formation avec un vrai appel API sur `facture_stage_001.pdf`.

### 1. Qwen2.5-VL 32B via OpenRouter

- Endpoint: `https://openrouter.ai/api/v1/chat/completions`
- Modele: `qwen/qwen2.5-vl-32b-instruct:free`
- Usage: tres bon candidat principal pour OCR/vision gratuit.
- Points forts: compatible API OpenAI/OpenRouter, vision native, bon niveau OCR dans le tier gratuit.
- Limite: quotas et throttling possibles en free, a verifier avant atelier.

### 2. Qwen2.5-VL 72B via OpenRouter

- Endpoint: `https://openrouter.ai/api/v1/chat/completions`
- Modele: `qwen/qwen2.5-vl-72b-instruct:free`
- Usage: variante plus puissante pour comparer deux tailles de modele.
- Limite: disponibilite parfois plus variable, throttling plus frequent.

### 3. Mistral Small 3.1 24B via OpenRouter

- Endpoint: `https://openrouter.ai/api/v1/chat/completions`
- Modele: `mistralai/mistral-small-3.1-24b-instruct:free`
- Usage: bon modele multimodal pour documents textuels et captures.
- Angle pedagogique: modele Mistral, pertinent pour une formation en France.

### 4. Kimi VL A3B via OpenRouter

- Endpoint: `https://openrouter.ai/api/v1/chat/completions`
- Modele: `moonshotai/kimi-vl-a3b-thinking:free`
- Usage: modele leger pour montrer OCR + comprehension visuelle avec un cout faible.
- Limite: verifier la disponibilite et la qualite sur factures scannees.

### 5. Hugging Face Inference API

- Endpoint: `https://api-inference.huggingface.co/models/{model_id}`
- Variables: `HF_API_TOKEN` et `HF_MODEL_ID`
- Usage: fallback API si OpenRouter est indisponible.
- Modeles a explorer: familles vision/OCR comme InternVL, GOT-OCR 2.0 ou autre modele compatible Inference API.
- Limite: le format exact de reponse depend du modele choisi; verifier avec un test court avant atelier.

Ordre conseille pour la formation:

1. Tester `qwen/qwen2.5-vl-32b-instruct:free`.
2. Garder `mistralai/mistral-small-3.1-24b-instruct:free` comme alternative pedagogique.
3. Garder `sample` comme fallback offline garanti.

## Demo offline

```bash
python 04_pdf_ocr_agent/ocr_agent/cli.py --input 04_pdf_ocr_agent/samples/facture_stage_001.txt --type invoice --provider sample --output 04_pdf_ocr_agent/output.csv
```

## Streamlit optionnel

```bash
streamlit run 04_pdf_ocr_agent/app_streamlit.py
```

Les tests n'appellent aucune API externe.
