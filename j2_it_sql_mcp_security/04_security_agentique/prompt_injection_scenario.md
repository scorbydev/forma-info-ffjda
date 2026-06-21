# Scenario de prompt injection documentaire

Une application envoie le texte extrait d'un PDF ou d'un ticket a un LLM afin de produire un JSON de controle.

Le document contient une instruction malveillante. Si le prompt de l'application melange les consignes de traitement et le contenu documentaire sans separation claire, le modele peut confondre une donnee avec une instruction.

Consequences possibles:

- mauvaise classification;
- document valide a tort;
- anomalie non signalee;
- recommandation dangereuse;
- tentative d'affichage de secrets;
- action automatique sans validation.

Le PDF ne pirate pas l'application tout seul. Le risque apparait dans la chaine:

```text
document -> extraction OCR -> LLM -> JSON -> decision ou action
```

La protection doit donc exister a plusieurs niveaux: prompt durci, schema de sortie, detection d'instructions suspectes, validation humaine et absence d'action automatique sensible.

