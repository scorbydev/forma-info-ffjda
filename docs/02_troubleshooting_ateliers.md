# Troubleshooting ateliers

## Codex quota atteint

Basculer vers Antigravity ou travailler en binome avec un poste disposant encore de quota.

## Bascule vers Antigravity

Ouvrir le meme dossier repo, relire `AGENTS.md`, puis reprendre le prompt de l'atelier.

## Probleme Python venv

Recreer l'environnement:

```bash
python -m venv .venv
```

Sur Windows, si la creation du venv echoue pendant `ensurepip` avec une erreur d'acces a `AppData\Local\Temp`, utiliser un dossier temporaire local au repo:

```powershell
New-Item -ItemType Directory -Force -Path .tmp_venv | Out-Null
$env:TMP=(Resolve-Path .tmp_venv).Path
$env:TEMP=(Resolve-Path .tmp_venv).Path
python -m venv .venv
```

## pytest introuvable

Installer les dependances:

```bash
pip install -r requirements.txt
```

## SQLite

Recreer la base:

```bash
python 02_sql_licence_diagnostic/create_db.py
```

## OpenRouter API erreur

Verifier `OPENROUTER_API_KEY`, le modele et les quotas. Si l'erreur persiste, utiliser Hugging Face ou `sample`.

## Hugging Face API erreur

Verifier `HF_API_TOKEN` et `HF_MODEL_ID`. Si le modele n'est pas configure, le provider doit retourner une erreur claire.

## Streamlit

Lancer:

```bash
streamlit run 04_pdf_ocr_agent/app_streamlit.py
```

## Windows PowerShell

Activer l'environnement:

```powershell
.venv\Scripts\activate
```

## `.env` absent

Copier `.env.example` vers `.env` uniquement en local.

## Cle API non chargee

Verifier que le terminal est lance depuis la racine du repo et que `.env` contient les variables attendues.
