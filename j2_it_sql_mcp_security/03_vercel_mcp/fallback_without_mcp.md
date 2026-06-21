# Fallback sans MCP

Si OAuth ou MCP bloque:

1. Construire la mini app avec `npm run build`.
2. Deployer avec Vercel CLI si le login fonctionne.
3. Lire les logs avec les commandes Vercel CLI disponibles.
4. Copier uniquement les messages d'erreur non sensibles dans Codex.
5. Demander a Codex d'expliquer la sortie terminal et de proposer un diagnostic.

Le MCP aurait permis a Codex de:

- lister directement les projets;
- retrouver les derniers deploiements;
- consulter les metadonnees et logs autorises;
- relier le contexte du repo au contexte Vercel.

Message cle: le MCP simplifie l'acces aux outils, mais ne remplace ni les permissions minimales ni la validation humaine.

