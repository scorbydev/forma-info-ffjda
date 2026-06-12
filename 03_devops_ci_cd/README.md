# Atelier 3 - Correctif Python, tests et CI/CD

Objectif: inspecter une regle metier volontairement imparfaite, proposer un correctif minimal, lancer les tests et ameliorer la CI.

Le fichier `src/license_rules.py` contient un bug pedagogique: l'ordre des controles peut retourner `EXPIRED_SEASON` avant des blocages plus prioritaires.

## Bug volontaire

La regle metier attendue est:

1. si `payment_status != "PAID"` alors `PENDING_PAYMENT`;
2. si `certificate_valid is False` alors `PENDING_CERTIFICATE`;
3. si `mutation_pending is True` alors `PENDING_MUTATION`;
4. si `season != current_season` alors `EXPIRED_SEASON`;
5. sinon `ACTIVE`.

Le code actuel teste la saison trop tot. Un cas avec paiement non paye et mauvaise saison retourne donc `EXPIRED_SEASON`, alors que la priorite metier attendue est `PENDING_PAYMENT`.

## Role du test xfail

Les tests globaux passent grace a un test marque `xfail`. Ce test documente le comportement attendu apres correction sans casser le repo initial.

Pendant l'atelier, l'apprenant doit demander a l'agent de corriger le bug minimalement. Une fois le code corrige, le test `test_payment_priority_before_expired_season_after_fix` doit devenir un test normal: retirer le marqueur `@pytest.mark.xfail` et verifier que toute la suite passe.

## Prompt conseille pour l'apprenant

Demander a l'agent:

```text
Dans 03_devops_ci_cd, inspecte d'abord src/license_rules.py et tests/test_license_rules.py.
Explique le bug lie a l'ordre des regles sans modifier.
Propose un plan court.
Applique le correctif minimal dans compute_license_status.
Retire le xfail du test qui documentait le bug.
Lance python -m pytest.
Si les tests passent, resume le diff et la raison metier de la correction.
```

Le fichier `.github/workflows/ci.yml` dans ce dossier est un support d'atelier. Le repo contient aussi une CI racine dans `.github/workflows/ci.yml`, qui est celle que GitHub executera automatiquement.

```bash
python -m pytest 03_devops_ci_cd/tests
```
