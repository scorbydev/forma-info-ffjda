# BUILD_REPORT

## Plan initial

1. Inspecter le dossier courant et lire `CONTEXT.md`.
2. Creer les fichiers racine, docs, prompts et skills.
3. Creer les ateliers 1 et 2.
4. Creer les ateliers 3 et 4 avec tests offline.
5. Creer l'atelier 5 gouvernance.
6. Executer les verifications et tests.
7. Corriger les problemes detectes.

## Journal

- Inspection initiale: dossier avec `CONTEXT.md`, pas de depot Git initialise.
- `CONTEXT.md` lu: contexte general utile, mission limitee au repo d'ateliers.

## Etapes realisees

### Etape 1 - Racine et documentation

Fichiers crees:

- `README.md`
- `AGENTS.md`
- `.gitignore`
- `.env.example`
- `requirements.txt`
- `pyproject.toml`
- `Makefile`
- `docs/00_prerequis_ateliers.md`
- `docs/01_guide_execution_ateliers.md`
- `docs/02_troubleshooting_ateliers.md`

Verification: presence confirmee par inventaire PowerShell.

### Etape 2 - Atelier 1 incident vers ticket

Fichiers crees:

- `01_incident_to_ticket/README.md`
- `01_incident_to_ticket/mail_incident_001.md`
- `01_incident_to_ticket/expected_ticket_structure.md`
- `prompts/atelier1_incident_to_ticket.md`
- `skills/incident-triage/SKILL.md`

Verification: dossier controle, tous les fichiers attendus sont presents.

### Etape 3 - Atelier 2 SQL licence

Fichiers crees:

- `02_sql_licence_diagnostic/README.md`
- `02_sql_licence_diagnostic/schema.sql`
- `02_sql_licence_diagnostic/sample_data.sql`
- `02_sql_licence_diagnostic/incident_licence_001.md`
- `02_sql_licence_diagnostic/create_db.py`
- `02_sql_licence_diagnostic/run_query.py`
- `02_sql_licence_diagnostic/expected_diagnostic.md`
- `prompts/atelier2_sql_diagnostic.md`
- `skills/sql-diagnostic/SKILL.md`

Verification:

- `python 02_sql_licence_diagnostic/create_db.py` OK.
- Requete diagnostic sur `LIC-2026-0007` OK: saison `2024/2025`, statut `A_CORRIGER`, paiement `VALIDE`.
- Requete de comptage OK: 20 licencies.

### Etape 4 - Atelier 3 Python CI/CD

Fichiers crees:

- `03_devops_ci_cd/README.md`
- `03_devops_ci_cd/src/__init__.py`
- `03_devops_ci_cd/src/license_rules.py`
- `03_devops_ci_cd/tests/test_license_rules.py`
- `03_devops_ci_cd/.github/workflows/ci.yml`
- `03_devops_ci_cd/expected_fix.md`
- `prompts/atelier3_devops_ci.md`
- `skills/python-ci-review/SKILL.md`

Verification: tests inclus dans la suite globale. Un test est marque `xfail` volontairement pour garder le bug pedagogique sans casser le repo initial.

### Etape 5 - Atelier 4 OCR/PDF agentique

Fichiers crees:

- `04_pdf_ocr_agent/README.md`
- `04_pdf_ocr_agent/samples/facture_stage_001.txt`
- `04_pdf_ocr_agent/samples/facture_intervenant_002.txt`
- `04_pdf_ocr_agent/samples/licence_erreur_003.txt`
- `04_pdf_ocr_agent/ocr_agent/__init__.py`
- `04_pdf_ocr_agent/ocr_agent/cli.py`
- `04_pdf_ocr_agent/ocr_agent/models.py`
- `04_pdf_ocr_agent/ocr_agent/pipeline.py`
- `04_pdf_ocr_agent/ocr_agent/provider_sample.py`
- `04_pdf_ocr_agent/ocr_agent/provider_openrouter.py`
- `04_pdf_ocr_agent/ocr_agent/provider_huggingface.py`
- `04_pdf_ocr_agent/ocr_agent/export_csv.py`
- `04_pdf_ocr_agent/tests/test_ocr_agent.py`
- `04_pdf_ocr_agent/app_streamlit.py`
- `04_pdf_ocr_agent/expected_outputs/extractions_expected.csv`
- `prompts/atelier4_pdf_ocr.md`
- `skills/pdf-extraction/SKILL.md`

Verification:

- Demo facture avec provider `sample` OK.
- Demo licence avec provider `sample` OK.
- Tests OCR offline uniquement OK.

### Etape 6 - Atelier 5 gouvernance

Fichiers crees:

- `05_governance/README.md`
- `05_governance/risk_register_template.md`
- `05_governance/doctrine_ia_it_draft.md`
- `05_governance/expected_agents_rules.md`
- `prompts/atelier5_governance.md`
- `skills/it-governance/SKILL.md`

Verification: presence confirmee par inventaire final.

### Etape 7 - Passe qualite complete avant formation

Corrections ajoutees pendant l'audit:

- Ajout de `.github/workflows/ci.yml` a la racine pour que GitHub Actions s'execute vraiment sur le depot public.
- Conservation de `03_devops_ci_cd/.github/workflows/ci.yml` comme support pedagogique de l'atelier 3.
- Ajout de `04_pdf_ocr_agent/ocr_agent/pipeline.py` pour centraliser l'extraction OCR, la validation Pydantic et l'export quel que soit le provider.
- Mise a jour du CLI OCR: `sample`, `openrouter` et `huggingface` passent maintenant par le meme pipeline de validation/export.
- Mise a jour de l'app Streamlit pour utiliser le provider selectionne et afficher une erreur lisible.
- Gestion propre des erreurs reseau OpenRouter/Hugging Face sans stacktrace brute.
- Remplacement des listes par defaut des modeles Pydantic par `Field(default_factory=list)`.
- Ajout d'un test de validation de payload API OCR.
- Documentation de la difference entre CI racine reelle et workflow pedagogique d'atelier.

## Tests lances

Installation:

- `python -m pip install -r requirements.txt` a depasse le delai mais a installe les dependances principales.
- `python -m pip install streamlit` OK pour completer l'environnement.

Commandes de verification:

- `python 02_sql_licence_diagnostic/create_db.py` OK.
- `python 02_sql_licence_diagnostic/run_query.py "SELECT COUNT(*) AS licencies FROM licencies;"` OK.
- `python 04_pdf_ocr_agent/ocr_agent/cli.py --input 04_pdf_ocr_agent/samples/licence_erreur_003.txt --type license --provider sample --output 04_pdf_ocr_agent/output.csv` OK.
- `python -m pytest` OK.

Resultat final tests:

```text
9 passed, 1 xfailed
```

## Corrections appliquees

- Ajustement du test OCR pour ne pas dependre du fixture `tmp_path`, qui provoquait une erreur de permission Windows sur le repertoire temporaire systeme.
- Ajout de `addopts = "-p no:cacheprovider"` dans `pyproject.toml` pour eviter les avertissements de cache pytest sur ce poste.
- Nettoyage des artefacts generes par les tests et demos: base SQLite, CSV de sortie, `__pycache__`, caches temporaires.
- Ajout d'un workflow GitHub Actions racine afin d'eviter la confusion entre support d'atelier et CI reelle.
- Durcissement des providers OCR API pour que les erreurs de configuration, reseau ou JSON soient comprehensibles.

## Verifications finales

- `.env.example` existe.
- `.env` n'a pas ete cree.
- OpenRouter est optionnel.
- Hugging Face est prevu comme fallback API.
- Le provider `sample` permet les tests offline.
- Les tests n'appellent aucune API externe.
- Scan simple de secrets: aucun motif de cle OpenRouter/HF renseignee detecte.
- Le scan signale seulement la variable locale `token = os.getenv("HF_API_TOKEN")`, qui n'est pas un secret en dur.
- `python -m compileall -q 02_sql_licence_diagnostic 03_devops_ci_cd 04_pdf_ocr_agent` OK.
- Le CLI OCR sample facture OK.
- Les providers API sans configuration/reseau retournent des messages d'erreur lisibles.
- Fichiers interdits absents:
  - `docs/02_deroule_journee.md`
  - `docs/03_trame_slides.md`
  - `docs/05_note_j2_it_a_prevoir.md`

## Commandes utiles

```bash
python -m pytest
python 02_sql_licence_diagnostic/create_db.py
python 02_sql_licence_diagnostic/run_query.py "SELECT name FROM sqlite_master WHERE type='table';"
python 04_pdf_ocr_agent/ocr_agent/cli.py --input 04_pdf_ocr_agent/samples/facture_stage_001.txt --type invoice --provider sample --output 04_pdf_ocr_agent/output.csv
```

## Points a verifier manuellement

- Tester le modele OpenRouter gratuit la veille de la formation.
- Renseigner `HF_MODEL_ID` seulement si un fallback Hugging Face est vraiment utilise.
- Initialiser Git et pousser vers GitHub si le depot public doit etre publie.

## Limites restantes

- Le repo n'est pas initialise en Git dans ce dossier local.
- Les providers OpenRouter et Hugging Face sont des squelettes API avec gestion d'erreur; l'extraction validee et testee est volontairement offline via `sample`.
- L'atelier 3 contient un bug volontaire documente par `expected_fix.md` et un test `xfail`.

## Suggestions d'amelioration

- Ajouter un script de correction SQL non execute, commentant transaction et rollback.
- Ajouter des tickets exemples produits par les apprenants apres atelier.
- Ajouter une checklist formateur distincte si necessaire, sans creer les fichiers docs explicitement exclus.

## Passe qualite finale avant gel

Date: 2026-06-12.

### Quick start en environnement propre

Verification effectuee avec un venv dedie `.venv_quality`.

Constat initial: sur cette machine Windows, `python -m venv .venv_quality` a echoue pendant `ensurepip` car Python ne pouvait pas ecrire dans `C:\Users\DELL\AppData\Local\Temp`.

Correction de verification: creation d'un dossier temporaire local `.tmp_quality`, puis definition de `TMP` et `TEMP` vers ce dossier. Avec ce contournement, le venv propre a ete cree correctement.

Commandes lancees:

```powershell
python -m venv .venv_quality
.venv_quality\Scripts\python.exe -m pip install -r requirements.txt
.venv_quality\Scripts\python.exe -m pytest
```

Resultat:

```text
pip install -r requirements.txt : OK
python -m pytest : 9 passed, 1 xfailed
```

`make test`: non execute car `make` n'est pas disponible sur ce poste Windows (`make unavailable`). Le `Makefile` reste present pour les environnements qui disposent de `make`.

Documentation ajoutee: `docs/02_troubleshooting_ateliers.md` indique maintenant le contournement Windows si `ensurepip` echoue sur le repertoire Temp.

### Atelier 2

Ajout de `02_sql_licence_diagnostic/correction_template.sql`.

Le script:

- est non execute par defaut;
- demarre par `BEGIN TRANSACTION`;
- contient des `SELECT` de controle avant correction;
- garde l'`UPDATE` commente et protege;
- garde l'`INSERT` dans `historique_corrections` commente;
- contient un `SELECT` de controle apres correction;
- termine par `ROLLBACK`;
- laisse `COMMIT` commente, a utiliser seulement apres validation humaine.

`02_sql_licence_diagnostic/README.md` mis a jour pour expliquer l'utilisation du template.

### Atelier 3

`03_devops_ci_cd/README.md` renforce:

- bug volontaire explique;
- ordre metier attendu explicite;
- role du test `xfail` explique;
- prompt conseille ajoute;
- consigne claire: apres correction, retirer `@pytest.mark.xfail` pour transformer le test en test normal.

### Atelier 4

`04_pdf_ocr_agent/README.md` clarifie:

- le mode `sample` simule une sortie OCR deja extraite;
- l'exercice porte sur extraction structuree, validation et export;
- OpenRouter reste optionnel;
- Hugging Face reste fallback API;
- `sample` reste le mode offline pour les tests.

Ajout de deux faux fichiers PDF pedagogiques generes a partir des samples texte:

- `04_pdf_ocr_agent/samples/facture_stage_001.pdf`
- `04_pdf_ocr_agent/samples/licence_erreur_003.pdf`

Les tests ne dependent pas des PDF.

### Commandes finales relancees

```powershell
.venv_quality\Scripts\python.exe -m pytest
.venv_quality\Scripts\python.exe -m compileall -q 02_sql_licence_diagnostic 03_devops_ci_cd 04_pdf_ocr_agent
.venv_quality\Scripts\python.exe 02_sql_licence_diagnostic/create_db.py
.venv_quality\Scripts\python.exe 02_sql_licence_diagnostic/run_query.py "SELECT (SELECT COUNT(*) FROM licencies) AS licencies, (SELECT COUNT(*) FROM licences) AS licences, (SELECT COUNT(*) FROM paiements) AS paiements;"
.venv_quality\Scripts\python.exe 04_pdf_ocr_agent/ocr_agent/cli.py --input 04_pdf_ocr_agent/samples/facture_stage_001.txt --type invoice --provider sample --output 04_pdf_ocr_agent/output.csv
```

Resultats:

```text
pytest : 9 passed, 1 xfailed
compileall : OK
demo SQL : 20 licencies, 35 licences, 30 paiements
demo OCR sample : extraction facture OK
```

### Nettoyage avant gel

Artefacts supprimes apres verification:

- `.venv_quality`
- `.tmp_quality`
- `02_sql_licence_diagnostic/ffj_licences.sqlite`
- `04_pdf_ocr_agent/output.csv`
- dossiers `__pycache__`

Controle final:

- `.env` absent;
- base SQLite generee absente;
- CSV de demo absent;
- faux PDF pedagogiques presents;
- scan simple de secrets: pas de secret en dur, uniquement la variable locale `token = os.getenv("HF_API_TOKEN")` et la mention documentee dans ce rapport.
