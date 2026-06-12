# Skill: sql-diagnostic

Utiliser cette skill pour diagnostiquer un incident SQL avant toute correction.

## Methode obligatoire

1. Lire le schema et identifier les tables.
2. Lire l'incident et extraire l'identifiant de recherche.
3. Produire uniquement des requetes `SELECT` pour le diagnostic initial.
4. Expliquer les jointures et les resultats.
5. Demander validation humaine avant toute modification.
6. Preparer une transaction explicite.
7. Prevoir un `ROLLBACK` possible.
8. Inserer une ligne dans une table d'historique ou de log.
9. Executer une requete de controle apres correction.
10. Documenter les risques.

## Interdits

- Pas de `UPDATE`, `DELETE`, `INSERT`, `ALTER`, `DROP` sans accord explicite.
- Pas de modification destructive.
- Pas de correction sur donnees reelles dans ce repo.

