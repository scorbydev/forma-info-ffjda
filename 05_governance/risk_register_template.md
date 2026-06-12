# Registre de risques

| risque | scenario | gravite | probabilite | garde-fou | responsable | statut |
| --- | --- | --- | --- | --- | --- | --- |
| Donnees personnelles exposees | Un prompt contient une vraie fiche licencie | Elevee | Moyenne | Donnees fictives ou anonymisees, validation humaine | RSI | A cadrer |
| Secret commite | Une cle API est ajoutee au repo | Elevee | Moyenne | `.env`, `.gitignore`, revue diff | Dev | A surveiller |
| SQL destructif | L'agent propose un `UPDATE` sans diagnostic | Elevee | Moyenne | SELECT d'abord, transaction, validation | DBA/IT | A cadrer |
| Hallucination de correction | L'agent invente une cause | Moyenne | Moyenne | Questions de clarification, preuves, tests | Support IT | A surveiller |
| Appel API non maitrise | Document envoye a un provider externe | Elevee | Faible | Sandbox, documents fictifs, doctrine | RSI | A cadrer |

