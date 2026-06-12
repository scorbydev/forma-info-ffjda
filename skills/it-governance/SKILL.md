# Skill: it-governance

Utiliser cette skill pour auditer une demande avant execution par un agent IA.

## Classification

Classer la demande dans une categorie:

- autorisee;
- autorisee avec validation;
- a faire en sandbox;
- interdite;
- a reporter vers un cadrage securite/J2.

## Methode

1. Identifier l'objectif metier.
2. Identifier les donnees manipulees.
3. Identifier les systemes touches.
4. Chercher secrets, donnees personnelles, production, connecteurs et actions destructives.
5. Evaluer l'impact si l'agent se trompe.
6. Choisir la categorie de classification.
7. Definir les garde-fous: sandbox, tests, validation, logs, rollback.
8. Dire explicitement ce que l'agent peut faire seul et ce qui demande validation.

## Regles

- Les donnees reelles sensibles sortent du perimetre J1.
- Les connecteurs MCP reels demandent cadrage.
- Les scripts destructifs demandent validation explicite.
- Les corrections SQL demandent diagnostic, transaction et rollback.
- Les secrets ne sont jamais partages dans le prompt.

