# Skill: pdf-extraction

Utiliser cette skill pour extraire des informations depuis un document fictif ou sandbox.

## Methode

1. Verifier le format et la source du document.
2. Choisir le provider: OpenRouter vision si disponible, Hugging Face comme fallback API, `sample` uniquement pour tests/offline.
3. Pour PDF/image avec OpenRouter, convertir le PDF en images si necessaire puis envoyer les images au modele vision.
4. Extraire les champs attendus.
5. Valider avec un modele Pydantic ou schema equivalent.
6. Signaler les incertitudes dans `warnings`.
7. Ne jamais inventer les champs manquants.
8. Exporter JSON et CSV.
9. Documenter le provider utilise et les limites.

## Contraintes

- Aucune cle API dans le code.
- Les tests unitaires doivent rester offline.
- Les documents de ce repo sont fictifs.
