# forma-info-ffjda

Depot pedagogique sandbox pour les ateliers pratiques de la formation "IA agentique pour l'IT FFJDA".

Ce repo sert a apprendre a piloter un agent de developpement type Codex App/CLI dans un workspace controle: lire, diagnostiquer, modifier, tester, documenter, creer des skills et cadrer l'usage agentique.

Tout est fictif. Aucune donnee personnelle reelle, aucun secret, aucune connexion a un systeme FFJDA reel, Azure DevOps reel ou SQL Server reel.

## Quick start

```bash
cd /scorbydev/forma-info-ffjda
python -m venv .venv
```

Windows:

```bash
.venv\Scripts\activate
```

macOS/Linux:

```bash
source .venv/bin/activate
```

Puis:

```bash
pip install -r requirements.txt
python -m pytest
```

Si `make` est disponible:

```bash
make test
make sql-db
```

## Outils

- Outil principal: Codex App / CLI.
- Fallback: Google Antigravity App / CLI.
- Tests: `pytest`.
- Base sandbox: SQLite.
- OCR/API: OpenRouter optionnel, Hugging Face fallback API, provider `sample` pour tests offline.

## Ateliers

1. `01_incident_to_ticket`: transformer un mail incident flou en ticket technique.
2. `02_sql_licence_diagnostic`: diagnostiquer un probleme de licence dans SQLite.
3. `03_devops_ci_cd`: corriger une regle Python avec tests et CI.
4. `04_pdf_ocr_agent`: extraire des champs depuis documents fictifs avec providers optionnels.
5. `05_governance`: formaliser une doctrine d'usage agentique IT.

Les prompts prets a copier-coller sont dans `prompts/`. Les corriges et attendus formateur restent dans chaque dossier d'atelier.

## Skills

Les skills reutilisables sont dans `skills/`:

- `incident-triage`
- `sql-diagnostic`
- `python-ci-review`
- `pdf-extraction`
- `it-governance`

Chaque skill decrit une methode reproductible pour cadrer le travail de l'agent.

## Secrets et donnees sensibles

Ne jamais commiter de secret. Copier `.env.example` vers `.env` seulement en local si besoin. Le fichier `.env` est ignore par Git.

Les donnees sont fictives. Si vous adaptez ce repo, remplacez toute donnee reelle par des exemples anonymises ou synthetiques.

## OCR: OpenRouter vision, Hugging Face et offline

L'atelier OCR vise une demo OpenRouter vision sur PDF/image: le PDF est rendu en images, envoye au modele via OpenRouter, puis la reponse JSON est validee et exportee en CSV. OpenRouter doit etre teste la veille de la formation, notamment le modele gratuit configure dans `.env.example` et les alternatives listees dans `04_pdf_ocr_agent/README.md`.

Si OpenRouter est indisponible, Hugging Face est le fallback API prevu via `HF_API_TOKEN` et `HF_MODEL_ID`. Si aucune API n'est disponible, le provider `sample` permet de continuer offline a partir de sorties OCR texte simulees.

Mode offline:

```bash
python 04_pdf_ocr_agent/ocr_agent/cli.py --input 04_pdf_ocr_agent/samples/facture_stage_001.txt --type invoice --provider sample --output 04_pdf_ocr_agent/output.csv
```

Mode OpenRouter vision PDF:

```bash
python 04_pdf_ocr_agent/ocr_agent/cli.py --input 04_pdf_ocr_agent/samples/facture_stage_001.pdf --type invoice --provider openrouter --output 04_pdf_ocr_agent/openrouter_facture.csv
```

## Tests

```bash
python -m pytest
```

Les tests n'appellent aucune API externe. Ils utilisent uniquement le provider `sample`.

## CI/CD

Le repo contient une CI GitHub Actions reelle dans `.github/workflows/ci.yml`. L'atelier 3 contient aussi un workflow pedagogique dans `03_devops_ci_cd/.github/workflows/ci.yml` pour l'exercice de revue et d'amelioration CI.
