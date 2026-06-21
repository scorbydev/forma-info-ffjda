# Cas de diagnostic

## Cas 1 - Paiement valide mais licence bloquee

La licence `licence_id=7` est bloquee alors que son paiement est valide. Identifier le licencie, le club, les dates et les incoherences.

## Cas 2 - Doublon potentiel

Deux fiches semblent representer la meme personne: meme nom, prenom et date de naissance. Identifier les numeros de licence concernes sans fusionner les donnees.

## Cas 3 - Document ou extraction incoherente

Le document `document_id=5` est rattache a un licencie different de celui porte par sa licence et l'extraction detecte une autre reference. Expliquer les trois sources.

## Cas 4 - Action agent risquee

Une action `UPDATE_LICENCE` a ete preparee par un agent. Verifier son statut, la validation humaine requise, les findings securite et l'historique disponible.

