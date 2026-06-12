# Atelier 2 - Diagnostic licence SQLite

Objectif: diagnostiquer un incident de licence dans une base SQLite sandbox.

## Creation de la base

```bash
python 02_sql_licence_diagnostic/create_db.py
```

## Requete de demonstration

```bash
python 02_sql_licence_diagnostic/run_query.py "SELECT name FROM sqlite_master WHERE type='table';"
```

## Template de correction securisee

Le fichier `correction_template.sql` est un support pedagogique. Il ne doit pas etre execute tel quel en atelier sans relecture.

Il montre:

- une transaction explicite;
- des `SELECT` de controle avant modification;
- un `UPDATE` volontairement commente et protege;
- un `INSERT` dans `historique_corrections` volontairement commente;
- un `SELECT` de controle apres correction;
- un `ROLLBACK` par defaut;
- un `COMMIT` uniquement apres validation humaine.

Pour l'utiliser en demonstration, commencez par copier les `SELECT` dans `run_query.py`. Ne lancez une version avec `--allow-write` qu'apres validation explicite du formateur.

## Regles

- Diagnostic en `SELECT` uniquement.
- Aucune modification sans validation humaine.
- Toute correction doit etre en transaction, avec rollback possible et log dans `historique_corrections`.
