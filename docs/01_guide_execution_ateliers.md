# Guide d'execution des ateliers

## Lancer le repo

Installer les dependances puis lancer les tests:

```bash
pip install -r requirements.txt
python -m pytest
```

## Utiliser les prompts

Les prompts sont dans `prompts/`. Copier le prompt de l'atelier dans Codex ou Antigravity, puis laisser l'agent inspecter les fichiers avant toute modification.

## Utiliser les skills

Les skills sont dans `skills/`. Elles decrivent les routines reutilisables pour incident, SQL, CI, OCR et gouvernance.

## Ordre recommande

1. Incident vers ticket.
2. Diagnostic SQL.
3. Correctif Python et CI.
4. Extraction documentaire OCR.
5. Gouvernance IT.

## Verifications

Apres chaque atelier, verifier le livrable attendu, les tests quand il y en a, et l'absence de donnees reelles ou de secrets.

