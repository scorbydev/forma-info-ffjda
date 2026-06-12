Dans 04_pdf_ocr_agent, cree ou ameliore le mini-outil d'extraction documentaire.
Objectif : prendre un document fictif de facture ou licence, extraire les champs attendus en JSON strict, valider les champs, puis exporter un CSV de controle.
Utilise OpenRouter si l'API est configuree et disponible.
Si OpenRouter est indisponible, utilise le provider Hugging Face configure dans .env.
Si aucune API n'est disponible, utilise le provider sample uniquement pour continuer le test technique offline.
Ne mets jamais de cle API dans le code.
Cree aussi ou ameliore la skill pdf-extraction decrivant la methode reutilisable.
Option : proposer une mini app Streamlit locale.

