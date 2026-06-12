# Doctrine IA agentique IT - brouillon

## Usages autorises

- Reformuler un incident fictif.
- Creer un ticket Markdown.
- Lire un schema sandbox.
- Proposer des requetes de diagnostic.
- Ecrire des tests sur donnees fictives.
- Produire de la documentation technique.

## Usages avec validation

- Modifier du code applicatif.
- Proposer une correction SQL.
- Executer un script qui modifie des fichiers.
- Ajouter une dependance.
- Utiliser une API externe avec documents sandbox.

## Usages interdits

- Traiter de vraies donnees personnelles dans ce repo.
- Envoyer des documents internes reels a une API externe.
- Executer une commande destructive sans validation explicite.
- Commettre une cle API, un mot de passe ou un token.
- Donner un acces direct a une base de production.

## Donnees interdites

- Donnees nominatives reelles de licencies.
- Documents financiers reels.
- Extraits de bases internes.
- Secrets, tokens, mots de passe.

## Secrets

Les secrets restent dans `.env` local ou dans un coffre approuve. Ils ne sont jamais presents dans le code, les tests, les prompts ou les captures.

## SQL

Diagnostic par `SELECT`, correction en transaction, rollback possible, log obligatoire et validation humaine.

## Scripts shell

Les scripts doivent etre lisibles, limites et non destructifs. Les suppressions, deplacements massifs et changements systeme demandent validation.

## CI/CD

Les pipelines doivent executer les tests et ne pas exposer de secrets dans les logs.

## OCR/documents

OpenRouter est optionnel, Hugging Face est le fallback API, `sample` sert au test offline. Aucun document reel ne doit etre envoye sans cadrage.

## MCP/connecteurs

Les connecteurs vers Jira, Azure DevOps, GitHub, email ou base interne demandent un cadrage securite, des permissions minimales et des logs.

## Logs

Les logs doivent aider l'audit sans contenir de donnees sensibles inutiles.

## Revue humaine

Toute action a impact metier, donnees, production ou securite doit etre revue par un humain responsable.

