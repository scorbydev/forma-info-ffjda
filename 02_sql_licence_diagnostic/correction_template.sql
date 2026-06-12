-- Template de correction securisee - NE PAS EXECUTER TEL QUEL.
--
-- Objectif pedagogique:
-- - montrer la structure d'une correction SQL controlee;
-- - garder un ROLLBACK par defaut;
-- - ne passer en COMMIT qu'apres validation humaine explicite.
--
-- Utilisation recommandee:
-- 1. executer d'abord les SELECT de diagnostic avec run_query.py sans --allow-write;
-- 2. relire ce fichier avec un formateur ou responsable;
-- 3. decommenter uniquement les lignes necessaires;
-- 4. remplacer le ROLLBACK final par COMMIT seulement apres validation.

BEGIN TRANSACTION;

-- Controle avant correction: verifier le cas exact.
SELECT
  l.licence_id,
  li.numero_licence,
  li.nom,
  li.prenom,
  c.nom_club,
  s.libelle AS saison_actuelle,
  l.statut,
  l.date_validation,
  p.statut_paiement,
  p.date_paiement,
  p.reference_paiement,
  l.commentaire
FROM licencies li
JOIN licences l ON l.licencie_id = li.licencie_id
JOIN clubs c ON c.club_id = l.club_id
JOIN saisons s ON s.saison_id = l.saison_id
LEFT JOIN paiements p ON p.licence_id = l.licence_id
WHERE li.numero_licence = 'LIC-2026-0007';

-- Controle anti-doublon avant modification.
SELECT
  nom,
  prenom,
  date_naissance,
  COUNT(*) AS occurrences
FROM licencies
GROUP BY nom, prenom, date_naissance
HAVING COUNT(*) > 1;

-- Correction protegee: garder commente tant que la validation humaine manque.
-- UPDATE licences
-- SET
--   saison_id = (SELECT saison_id FROM saisons WHERE libelle = '2025/2026'),
--   statut = 'ACTIVE',
--   date_validation = DATE('now'),
--   commentaire = 'Correction sandbox: rattachement saison 2025/2026 apres paiement valide.'
-- WHERE licence_id = 7
--   AND statut = 'A_CORRIGER'
--   AND EXISTS (
--     SELECT 1
--     FROM paiements
--     WHERE paiements.licence_id = licences.licence_id
--       AND paiements.statut_paiement = 'VALIDE'
--   );

-- Historique obligatoire: a decommenter avec l'UPDATE.
-- INSERT INTO historique_corrections (
--   licence_id,
--   action,
--   ancienne_valeur,
--   nouvelle_valeur,
--   motif,
--   date_correction,
--   operateur
-- )
-- VALUES (
--   7,
--   'CORRECTION_SAISON_STATUT',
--   'saison=2024/2025; statut=A_CORRIGER; date_validation=NULL',
--   'saison=2025/2026; statut=ACTIVE; date_validation=DATE(now)',
--   'Paiement valide confirme; correction apres validation humaine.',
--   DATETIME('now'),
--   'atelier-sandbox'
-- );

-- Controle apres correction: verifier le resultat avant decision.
SELECT
  l.licence_id,
  li.numero_licence,
  s.libelle AS saison_corrigee,
  l.statut,
  l.date_validation,
  h.action,
  h.date_correction
FROM licences l
JOIN licencies li ON li.licencie_id = l.licencie_id
JOIN saisons s ON s.saison_id = l.saison_id
LEFT JOIN historique_corrections h ON h.licence_id = l.licence_id
WHERE l.licence_id = 7;

-- ROLLBACK par defaut pour eviter toute modification accidentelle.
ROLLBACK;

-- Remplacer uniquement la ligne ci-dessus par COMMIT apres validation humaine.
-- COMMIT;
