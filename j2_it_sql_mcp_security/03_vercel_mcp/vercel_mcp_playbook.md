# Playbook Vercel MCP

## 1. Verifier Node et npm

```bash
node --version
npm --version
```

## 2. Ouvrir la mini app

```bash
cd 03_vercel_mcp/mini_app
```

## 3. Installer

```bash
npm install
```

## 4. Construire

```bash
npm run build
```

## 5. Installer Vercel CLI si necessaire

```bash
npm i -g vercel
vercel --version
```

## 6. Deployer

```bash
vercel
```

Verifier le projet, l'equipe cible et l'absence de secret avant confirmation.

## 7. Installer Vercel MCP

```bash
npx add-mcp https://mcp.vercel.com
```

## 8. Redemarrer Codex

Redemarrer l'application ou la session si le nouveau MCP n'apparait pas.

## 9. Questions a poser a Codex

- Liste mes projets Vercel.
- Trouve le dernier deploiement de la mini app.
- Explique les logs ou erreurs du dernier deploiement.
- Que faut-il verifier avant de publier une app interne ?

## Garde-fous

- Commencer par la lecture.
- Ne pas redeployer ou supprimer sans validation humaine.
- Ne jamais copier de token dans le chat.
- Documenter les actions executees via MCP.

