# J2 IT FFJDA - SQL, MCP et securite agentique

En J1, Codex a montre sa puissance. En J2, on apprend a le cadrer, le connecter et le securiser.

Cette extension de quatre heures reste entierement sandboxee. Elle prolonge les ateliers J1 sans utiliser de donnees FFJDA reelles ni de systeme metier reel.

## Objectifs

1. Utiliser `AGENTS.md` comme garde-fou permanent.
2. Diagnostiquer des cas SQL plus denses avec SQLite et DB Browser.
3. Comprendre et tester une connexion MCP avec Vercel.
4. Identifier les risques de prompt injection documentaire.

## Hors perimetre

- Pas de donnees personnelles reelles.
- Pas de vrai SI FFJDA.
- Pas d'Azure DevOps.
- Pas de Zoho.
- Pas de Playwright.
- Pas de secret dans le repo.

## Lancer les ateliers

Depuis la racine du repo:

```bash
cd j2_it_sql_mcp_security
python 02_sql_niveau_2/create_db.py
python 02_sql_niveau_2/run_query.py "SELECT COUNT(*) AS nb FROM licencies;"
python check_j2.py
```

Mini app:

```bash
cd 03_vercel_mcp/mini_app
npm install
npm run build
npm run dev
```

## Fichiers a ouvrir

- Bloc 1: `AGENTS.md`, puis `01_agents_guardrails/`.
- Bloc 2: `02_sql_niveau_2/diagnostic_cases.md`, le schema et DB Browser.
- Bloc 3: `03_vercel_mcp/vercel_mcp_playbook.md`.
- Bloc 4: `04_security_agentique/prompt_injection_scenario.md`.

## Utiliser Codex

Ouvrir ce dossier comme workspace, demander a Codex d'inspecter avant d'agir et utiliser les prompts dans `prompts/`. Les regles de ce dossier s'appliquent a toute la matiere J2.

## Verification

- La base contient les dix tables attendues et les volumes annonces.
- `run_query.py` autorise les `SELECT` et bloque les ecritures sans `--allow-write`.
- `check_j2.py` termine sans erreur.
- `npm run build` produit `mini_app/dist`.
- L'atelier reste comprehensible si Vercel OAuth ou MCP bloque.

