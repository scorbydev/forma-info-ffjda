# Skill: python-ci-review

Utiliser cette skill pour corriger un bug Python avec tests et CI.

## Methode

1. Inspecter les fichiers avant modification.
2. Identifier le comportement attendu et le comportement observe.
3. Proposer un plan court.
4. Garder le correctif minimal.
5. Lancer les tests.
6. Lire les erreurs et corriger iterativement.
7. Verifier ou proposer la CI.
8. Resumer le diff, les tests executes et les limites.

## Contraintes

- Ne pas refactorer hors perimetre.
- Ne pas masquer un test qui devrait echouer apres correction.
- Ne pas ajouter de dependance inutile.

