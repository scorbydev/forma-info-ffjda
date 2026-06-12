# AGENTS.md

Regles projet pour tout agent IA travaillant dans ce depot.

## Regles generales

- Toujours commencer par inspecter les fichiers pertinents.
- Toujours proposer un plan avant modification.
- Ne jamais utiliser de vraies donnees personnelles.
- Ne jamais executer d'action destructive sans validation explicite.
- Ne jamais mettre de cle API dans le code.
- Utiliser `.env` local et `.env.example`.
- En fin de tache, fournir resume, fichiers modifies, tests executes et limites restantes.

## SQL

- Diagnostic d'abord, correction ensuite.
- Utiliser des requetes `SELECT` pour comprendre le probleme.
- Obtenir validation humaine avant toute correction.
- Correction en transaction obligatoire.
- Prevoir rollback possible.
- Inserer une ligne dans `historique_corrections`.
- Produire un log clair de la correction.

## Code

- Modification minimale.
- Tests obligatoires.
- Diff lisible.
- Ne pas refactorer hors perimetre.
- Documenter les hypotheses si le besoin est ambigu.

## OCR et API

- OpenRouter est optionnel.
- Hugging Face est le fallback API.
- Les tests doivent rester offline.
- Le provider `sample` sert uniquement a la demonstration locale et aux tests sans API.
- Ne jamais inventer les champs manquants: signaler les incertitudes.

## Gouvernance

- Documenter les limites et les risques.
- Classer les demandes sensibles avant execution.
- Reporter tout usage de donnees reelles, connecteurs metier ou actions destructives vers un cadrage securite.

