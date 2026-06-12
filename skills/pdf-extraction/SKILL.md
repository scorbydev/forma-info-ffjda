# Skill: pdf-extraction

Utiliser cette skill pour extraire des informations depuis un document fictif ou sandbox.

## Methode

1. Verifier le format et la source du document.
2. Choisir le provider: OpenRouter si disponible, Hugging Face comme fallback API, `sample` uniquement pour tests/offline.
3. Extraire les champs attendus.
4. Valider avec un modele Pydantic ou schema equivalent.
5. Signaler les incertitudes dans `warnings`.
6. Ne jamais inventer les champs manquants.
7. Exporter JSON et CSV.
8. Documenter le provider utilise et les limites.

## Contraintes

- Aucune cle API dans le code.
- Les tests unitaires doivent rester offline.
- Les documents de ce repo sont fictifs.

