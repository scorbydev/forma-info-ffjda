# Atelier 2 - SQL niveau 2

Objectif: conduire un diagnostic multi-tables dans SQLite, avec Codex et DB Browser, sans autoriser de correction implicite.

## Creer la base

```bash
python 02_sql_niveau_2/create_db.py
```

Ouvrir ensuite `ffj_j2_it.sqlite` dans DB Browser for SQLite.

## Executer un SELECT

```bash
python 02_sql_niveau_2/run_query.py "SELECT COUNT(*) AS nb FROM licencies;"
```

## Methode

1. Lire `diagnostic_cases.md`.
2. Inspecter le schema.
3. Proposer une requete `SELECT`.
4. Executer et commenter le resultat.
5. Preparer une correction dans `correction_transaction_template.sql`.
6. Garder `ROLLBACK` par defaut.

Les ecritures sont bloquees par `run_query.py` sans `--allow-write`.

