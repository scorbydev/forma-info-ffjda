# Diagnostic attendu

## Tables a consulter

- `licencies`: identifier le numero de licence et detecter un doublon possible.
- `licences`: verifier saison, statut, dates et commentaire.
- `saisons`: confirmer la saison active 2025/2026.
- `clubs`: verifier le rattachement club.
- `paiements`: verifier statut, date et reference du paiement.
- `historique_corrections`: tracer toute correction.

## Jointures probables

```sql
SELECT
  li.numero_licence,
  li.nom,
  li.prenom,
  c.nom_club,
  s.libelle AS saison,
  l.statut,
  l.date_validation,
  p.statut_paiement,
  p.date_paiement,
  p.reference_paiement,
  l.commentaire
FROM licencies li
JOIN licences l ON l.licencie_id = li.licencie_id
JOIN clubs c ON c.club_id = l.club_id
JOIN saisons s ON s.saison_id = l.saison_id
LEFT JOIN paiements p ON p.licence_id = l.licence_id
WHERE li.numero_licence = 'LIC-2026-0007';
```

## Resultat attendu

La licence `LIC-2026-0007` a un paiement valide, mais elle est rattachee a la saison 2024/2025 avec le statut `A_CORRIGER` et sans date de validation.

## Risques

- Corriger le mauvais licencie en presence d'un doublon possible.
- Modifier une licence sans preuve de paiement.
- Ne pas tracer la correction.
- Exposer des donnees personnelles.

## Logique de correction securisee

1. Verifier le doublon possible.
2. Verifier le paiement.
3. Demander validation humaine.
4. Ouvrir une transaction.
5. Mettre a jour saison, statut et date de validation.
6. Inserer une ligne dans `historique_corrections`.
7. Controler le resultat.
8. Commit si valide, rollback sinon.

