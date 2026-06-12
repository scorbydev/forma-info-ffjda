Dans 04_pdf_ocr_agent, cree ou ameliore le mini-outil d'extraction documentaire.
Objectif : prendre un PDF ou une image fictive de facture ou licence, utiliser un modele vision/OCR via OpenRouter, extraire les champs attendus en JSON strict, valider les champs, puis exporter un CSV de controle.
Utilise OpenRouter si l'API est configuree et disponible. Le provider doit accepter PDF/image, convertir les PDF en images si necessaire, puis envoyer ces images au modele vision.
Si OpenRouter est indisponible, utilise le provider Hugging Face configure dans .env.
Si aucune API n'est disponible, utilise le provider sample uniquement comme fallback offline a partir des fichiers texte OCR simules.
Ne mets jamais de cle API dans le code.
Cree aussi ou ameliore la skill pdf-extraction decrivant la methode reutilisable.
Option : proposer une mini app Streamlit locale.
