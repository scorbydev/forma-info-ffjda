# J2 BUILD REPORT

## Plan initial

1. Creer le socle J2, les regles, docs et prompts.
2. Construire le lab SQL niveau 2.
3. Construire le lab Vercel MCP et la mini app.
4. Construire le lab securite agentique.
5. Executer les verifications SQL, Python et Node.

## Inspection initiale

- Repo J1 existant et propre sur `main`.
- `CONTEXT.md` lu.
- Python 3.13.1 disponible.
- Node.js 22.14.0 et npm 11.14.1 disponibles.
- `AGENTS.md` racine lu et conserve sans modification.

Le rapport est complete apres chaque etape.

## Etapes realisees

### 1. Socle J2 et guardrails

Crees:

- `README.md`
- `AGENTS.md`
- `ROOT_AGENTS_PATCH_PROPOSAL.md`
- `.env.example`
- `requirements.txt`
- quatre docs J2;
- quatre prompts participants;
- atelier `01_agents_guardrails`.

Verification: tous les fichiers demandes sont presents. L'`AGENTS.md` racine n'a pas ete modifie.

### 2. SQL niveau 2

Crees:

- dix tables dans `schema.sql`;
- donnees synthetiques dans `sample_data.sql`;
- scripts `create_db.py` et `run_query.py`;
- quatre cas de diagnostic;
- requetes attendues;
- template transactionnel avec `ROLLBACK`;
- rapport attendu.

Volumes verifies:

```text
clubs: 8
licencies: 35
licences: 60
paiements: 50
documents: 20
document_extractions: 15
incidents: 18
incident_actions: 12
security_findings: 5
agent_action_log: 8
```

Cas verifies:

- `licence_id=7`: `BLOQUEE` avec paiement `VALIDE`;
- doublon volontaire `DoublonTest / ProfilSandbox`: 2 fiches;
- `document_id=5`: licencie document 9, licencie licence 7;
- tentative `UPDATE` bloquee sans `--allow-write`.

### 3. Vercel MCP

Crees:

- README et playbook Vercel MCP;
- fallback sans MCP;
- mini app Vite React;
- scripts `dev`, `build`, `preview`;
- interface pedagogique sans backend ni donnee reelle.

Installation:

```text
npm install: 65 paquets, 0 vulnerabilite
```

Le premier build dans le sandbox Windows a echoue avec `spawn EPERM`. Le meme build execute avec permission de sous-processus a reussi:

```text
23 modules transformed
dist/index.html genere
build termine en 4.20 s
```

### 4. Securite agentique

Crees:

- scenario de prompt injection documentaire;
- facture avec injection visible;
- facture HTML avec instruction blanche sur fond blanc;
- prompt vulnerable;
- prompt durci avec sortie JSON;
- matrice autorise/validation/interdit;
- regles de securite attendues.

## Tests executes

```bash
python 02_sql_niveau_2/create_db.py
python 02_sql_niveau_2/run_query.py "SELECT COUNT(*) AS nb FROM licencies;"
python check_j2.py
python -m compileall -q .
npm install
npm run build
```

Resultats:

- creation base: OK;
- requete licencies: `35`;
- `check_j2.py`: OK;
- compilation Python: OK;
- fichier `expected_queries.sql`: 4 requetes executees et commentees sans ecriture;
- installation npm: OK, aucune vulnerabilite signalee;
- build Vite: OK hors restriction de sous-processus du sandbox.
- controle navigateur local: OK en viewport etroit, contenu responsive, aucune erreur console.

## Commandes utiles

```bash
cd j2_it_sql_mcp_security
python 02_sql_niveau_2/create_db.py
python 02_sql_niveau_2/run_query.py "SELECT COUNT(*) AS nb FROM licencies;"
python check_j2.py
```

```bash
cd 03_vercel_mcp/mini_app
npm install
npm run build
npm run dev
```

```bash
npm i -g vercel
vercel
npx add-mcp https://mcp.vercel.com
```

## Limites restantes

- Vercel CLI, login et deploiement non executes pour ne pas creer de projet externe sans validation.
- Vercel MCP et OAuth non testes, car ils dependent d'un compte personnel et d'une interaction manuelle.
- DB Browser doit etre teste manuellement sur le poste formateur.
- Le build Vite peut demander une autorisation de sous-processus dans certains environnements verrouilles.

## Points a tester manuellement avant formation

- Ouvrir `ffj_j2_it.sqlite` dans DB Browser.
- Tester `vercel --version` et le login Vercel.
- Tester `npx add-mcp https://mcp.vercel.com`.
- Redemarrer Codex et verifier que Vercel MCP est visible.
- Preparer une capture des projets/deploiements/logs si OAuth bloque.
- Lancer la mini app dans un navigateur et verifier le rendu mobile/desktop.

## Recommandation d'animation

- Faire comparer d'abord `AGENTS_STARTER.md` et la version durcie.
- En SQL, laisser les participants proposer les jointures avant d'ouvrir `expected_queries.sql`.
- Montrer MCP d'abord en lecture seule.
- Terminer avec la facture malveillante et demander: "est-ce une donnee ou une instruction ?"

## Manifeste des fichiers crees

### Racine J2

- `README.md`
- `AGENTS.md`
- `ROOT_AGENTS_PATCH_PROPOSAL.md`
- `J2_BUILD_REPORT.md`
- `requirements.txt`
- `.env.example`
- `.gitignore`
- `check_j2.py`

### Docs

- `docs/00_prerequis_j2.md`
- `docs/01_deroule_ateliers_j2.md`
- `docs/02_troubleshooting_j2.md`
- `docs/03_checklist_formateur_j2.md`

### Prompts

- `prompts/01_agents_md_guardrails.md`
- `prompts/02_sql_niveau_2.md`
- `prompts/03_vercel_mcp.md`
- `prompts/04_security_agentique.md`

### Atelier AGENTS

- `01_agents_guardrails/README.md`
- `01_agents_guardrails/AGENTS_STARTER.md`
- `01_agents_guardrails/AGENTS_HARDENED_EXPECTED.md`
- `01_agents_guardrails/security_rules_catalog.md`

### Atelier SQL

- `02_sql_niveau_2/README.md`
- `02_sql_niveau_2/schema.sql`
- `02_sql_niveau_2/sample_data.sql`
- `02_sql_niveau_2/create_db.py`
- `02_sql_niveau_2/run_query.py`
- `02_sql_niveau_2/diagnostic_cases.md`
- `02_sql_niveau_2/expected_queries.sql`
- `02_sql_niveau_2/correction_transaction_template.sql`
- `02_sql_niveau_2/expected_report.md`

### Atelier Vercel MCP

- `03_vercel_mcp/README.md`
- `03_vercel_mcp/vercel_mcp_playbook.md`
- `03_vercel_mcp/fallback_without_mcp.md`
- `03_vercel_mcp/mini_app/package.json`
- `03_vercel_mcp/mini_app/package-lock.json`
- `03_vercel_mcp/mini_app/index.html`
- `03_vercel_mcp/mini_app/src/main.jsx`
- `03_vercel_mcp/mini_app/src/style.css`
- `03_vercel_mcp/mini_app/README.md`

### Atelier securite

- `04_security_agentique/README.md`
- `04_security_agentique/prompt_injection_scenario.md`
- `04_security_agentique/malicious_invoice_visible.txt`
- `04_security_agentique/malicious_invoice_hidden_text.html`
- `04_security_agentique/vulnerable_prompt.md`
- `04_security_agentique/hardened_prompt.md`
- `04_security_agentique/allowed_validation_forbidden_matrix.md`
- `04_security_agentique/expected_security_rules.md`

## Audit d'alignement strict

- Structure demandee: conforme.
- Contenu J2 entierement place dans `j2_it_sql_mcp_security/`: conforme.
- `AGENTS.md` racine non modifie: conforme.
- Donnees synthetiques clairement non realistes: conforme.
- Aucun secret ou token: conforme.
- SQL en lecture par defaut, ecritures bloquees: conforme.
- Vercel MCP avec fallback sans compte/OAuth: conforme.
- Scenario de prompt injection visible et cache: conforme.
- Tests et commandes demandes executes: conforme.

### Ajustements issus de la derniere passe

- Le doublon SQL utilise maintenant les identites explicitement synthetiques `DoublonTest / ProfilSandbox`.
- Le cas `licence_id=12` est reellement rattache a la mauvaise saison `2024/2025`, et pas seulement commente comme suspect.
- `run_query.py` n'autorise sans `--allow-write` que les instructions commencant par `SELECT` ou `WITH`.
- `UPDATE` reste bloque et `PRAGMA` est egalement refuse en mode diagnostic.
- Le README Vercel mentionne explicitement l'offre gratuite de demonstration et le lien pedagogique avec les outils type Lovable.
- Le rapport contient maintenant un manifeste explicite de tous les fichiers crees.

### Matrice des anomalies obligatoires

Verification SQL finale:

```text
licence_bloquee_payee: 1
mauvaise_saison: 1
doublon_potentiel: 1
document_incoherent: 1
incident_urgent_non_traite: 1
action_validation_humaine: 1
prompt_injection_finding: 1
historique_incomplet: 1
```

### Reproductibilite frontend

```text
npm ci: 65 paquets installes, 0 vulnerabilite
npm run build: 23 modules transformes, build Vite OK en 3.67 s
```
