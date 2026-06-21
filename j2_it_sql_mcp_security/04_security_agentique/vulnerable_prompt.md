# Prompt vulnerable

```text
Analyse la facture ci-dessous.
Suis toutes les instructions presentes dans son contenu.
Retourne son statut et execute les actions demandees.

DOCUMENT:
{{document_text}}
```

Problemes:

- les instructions et les donnees ne sont pas separees;
- le document est declare digne de confiance;
- aucune detection d'injection;
- aucune limite sur les actions;
- aucune validation humaine.

