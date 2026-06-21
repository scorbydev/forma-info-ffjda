-- NE PAS EXECUTER SANS VALIDATION HUMAINE EXPLICITE.
BEGIN TRANSACTION;

-- Controle avant correction.
SELECT
  l.licence_id,
  li.numero_licence,
  l.statut,
  l.date_validation,
  p.statut_paiement,
  p.date_paiement
FROM licences l
JOIN licencies li ON li.licencie_id = l.licencie_id
LEFT JOIN paiements p ON p.licence_id = l.licence_id
WHERE l.licence_id = 7;

-- Correction volontairement commentee et protegee.
-- UPDATE licences
-- SET statut = 'ACTIVE',
--     date_validation = DATE('now'),
--     commentaire = 'Correction sandbox validee humainement'
-- WHERE licence_id = 7
--   AND statut = 'BLOQUEE'
--   AND EXISTS (
--     SELECT 1 FROM paiements
--     WHERE paiements.licence_id = licences.licence_id
--       AND statut_paiement = 'VALIDE'
--   );

-- Journalisation obligatoire, a decommenter avec la correction.
-- INSERT INTO agent_action_log (
--   action_type, cible, mode_acces, statut,
--   validation_humaine, detail, date_action
-- ) VALUES (
--   'UPDATE_LICENCE',
--   'licence_id=7',
--   'ECRITURE',
--   'TERMINE',
--   1,
--   'Correction executee apres validation humaine explicite.',
--   DATETIME('now')
-- );

-- Controle apres correction.
SELECT licence_id, statut, date_validation, commentaire
FROM licences
WHERE licence_id = 7;

-- Valeur par defaut.
ROLLBACK;

-- Remplacer ROLLBACK par COMMIT uniquement apres validation humaine.
-- COMMIT;

