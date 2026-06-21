# Troubleshooting J2

## Codex bloque

Relire `AGENTS.md`, reduire la demande et reprendre avec une seule verification a la fois.

## DB Browser non installe

Utiliser `run_query.py` en terminal. L'atelier SQL reste complet.

## Python absent

Installer Python 3.10+ puis verifier `python --version`.

## SQLite non cree

```bash
python 02_sql_niveau_2/create_db.py
```

## Node absent

Installer une version LTS de Node.js puis rouvrir le terminal.

## `npm install` echoue

Verifier le reseau, le proxy et le registre npm. Le code source reste lisible sans installation.

## Vercel login bloque

Continuer avec `03_vercel_mcp/fallback_without_mcp.md`.

## Vercel MCP OAuth bloque

Ne pas insister avec des tokens manuels. Utiliser Vercel CLI ou la demonstration de secours.

## `npx add-mcp` echoue

Verifier Node/npm et le reseau, puis expliquer le playbook sans connexion reelle.

## Fallback sans MCP

Construire localement, deployer avec Vercel CLI si possible, lire la sortie terminal et demander a Codex de l'expliquer.

## Secrets

Ne jamais afficher ou coller les variables d'environnement, tokens OAuth ou fichiers de configuration d'authentification.

