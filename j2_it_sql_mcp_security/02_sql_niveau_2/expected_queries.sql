-- Cas 1: licence bloquee malgre paiement valide.
SELECT
  l.licence_id,
  li.numero_licence,
  c.nom_club,
  l.saison,
  l.statut,
  l.date_validation,
  p.statut_paiement,
  p.date_paiement,
  l.commentaire
FROM licences l
JOIN licencies li ON li.licencie_id = l.licencie_id
JOIN clubs c ON c.club_id = l.club_id
LEFT JOIN paiements p ON p.licence_id = l.licence_id
WHERE l.licence_id = 7;

-- Cas 2: doublons potentiels.
SELECT nom, prenom, date_naissance, COUNT(*) AS occurrences,
       GROUP_CONCAT(numero_licence) AS numeros
FROM licencies
GROUP BY nom, prenom, date_naissance
HAVING COUNT(*) > 1;

-- Cas 3: coherence document/licence/licencie/extraction.
SELECT
  d.document_id,
  d.licencie_id AS document_licencie,
  l.licencie_id AS licence_licencie,
  li.numero_licence,
  de.licence_detectee,
  de.confidence,
  de.anomalie_detectee
FROM documents d
LEFT JOIN licences l ON l.licence_id = d.licence_id
LEFT JOIN licencies li ON li.licencie_id = d.licencie_id
LEFT JOIN document_extractions de ON de.document_id = d.document_id
WHERE d.document_id = 5;

-- Cas 4: action agent a valider et findings associes.
SELECT
  ia.action_id,
  i.reference_incident,
  ia.action_type,
  ia.statut_action,
  ia.validation_humaine_requise,
  aal.statut AS log_statut,
  aal.detail
FROM incident_actions ia
JOIN incidents i ON i.incident_id = ia.incident_id
LEFT JOIN agent_action_log aal
  ON aal.action_type = 'PREPARE_UPDATE' AND aal.cible = 'licence_id=7'
WHERE ia.action_id = 4;

