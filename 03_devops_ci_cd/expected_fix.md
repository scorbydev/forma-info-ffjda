# Correctif attendu

## Bug

`compute_license_status` teste `season != current_season` avant les blocages paiement, certificat et mutation. Or les regles metier attendues indiquent l'ordre suivant:

1. paiement non paye;
2. certificat invalide;
3. mutation en attente;
4. mauvaise saison;
5. actif.

## Correction minimale

Deplacer le test de saison apres les controles paiement, certificat et mutation.

## Tests a passer

```bash
python -m pytest
```

Apres correction, retirer le marqueur `xfail` du test `test_payment_priority_before_expired_season_after_fix`.

## Amelioration CI attendue

Conserver un workflow GitHub Actions qui installe les dependances et lance `python -m pytest`.

