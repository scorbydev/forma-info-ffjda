-- Donnees entierement synthetiques.

INSERT INTO clubs VALUES
(1, 'J2-C001', 'Judo Vallee Claire', 'Grand Est', 1),
(2, 'J2-C002', 'Dojo Horizon Test', 'Ile-de-France', 1),
(3, 'J2-C003', 'Alliance Tatami Ouest', 'Bretagne', 1),
(4, 'J2-C004', 'Judo Littoral Demo', 'Occitanie', 1),
(5, 'J2-C005', 'Club Montagne Sable', 'Auvergne-Rhone-Alpes', 1),
(6, 'J2-C006', 'Ecole Judo Nord', 'Hauts-de-France', 1),
(7, 'J2-C007', 'Dojo Atlantique Fictif', 'Nouvelle-Aquitaine', 1),
(8, 'J2-C008', 'Judo Centre Exemple', 'Centre-Val de Loire', 1);

WITH RECURSIVE seq(n) AS (
  SELECT 1
  UNION ALL SELECT n + 1 FROM seq WHERE n < 35
)
INSERT INTO licencies (
  licencie_id, numero_licence, nom, prenom, date_naissance, email
)
SELECT
  n,
  printf('J2-LIC-%04d', n),
  CASE WHEN n IN (7, 35) THEN 'DoublonTest' ELSE printf('NomTest%02d', n) END,
  CASE WHEN n IN (7, 35) THEN 'ProfilSandbox' ELSE printf('PrenomTest%02d', n) END,
  CASE WHEN n IN (7, 35) THEN '1900-01-01' ELSE printf('19%02d-%02d-%02d', 70 + (n % 25), 1 + (n % 12), 1 + (n % 27)) END,
  printf('licencie%02d@example.test', n)
FROM seq;

WITH RECURSIVE seq(n) AS (
  SELECT 1
  UNION ALL SELECT n + 1 FROM seq WHERE n < 60
)
INSERT INTO licences (
  licence_id, licencie_id, club_id, saison, statut, type_licence,
  date_creation, date_validation, commentaire
)
SELECT
  n,
  1 + ((n - 1) % 35),
  1 + ((n - 1) % 8),
  CASE WHEN n = 12 THEN '2024/2025' WHEN n <= 45 THEN '2025/2026' ELSE '2024/2025' END,
  CASE
    WHEN n = 7 THEN 'BLOQUEE'
    WHEN n = 12 THEN 'A_CORRIGER'
    WHEN n % 11 = 0 THEN 'EN_ATTENTE'
    WHEN n > 45 THEN 'EXPIREE'
    ELSE 'ACTIVE'
  END,
  CASE WHEN n % 3 = 0 THEN 'LOISIR' ELSE 'COMPETITION' END,
  printf('2025-%02d-%02d', 1 + (n % 9), 1 + (n % 27)),
  CASE WHEN n IN (7, 12) OR n % 11 = 0 THEN NULL ELSE printf('2025-%02d-%02d', 1 + (n % 9), 2 + (n % 26)) END,
  CASE
    WHEN n = 7 THEN 'Paiement valide mais licence bloquee'
    WHEN n = 12 THEN 'Mauvaise saison suspectee'
    ELSE ''
  END
FROM seq;

WITH RECURSIVE seq(n) AS (
  SELECT 1
  UNION ALL SELECT n + 1 FROM seq WHERE n < 50
)
INSERT INTO paiements (
  paiement_id, licence_id, montant, date_paiement, statut_paiement, reference_paiement
)
SELECT
  n,
  n,
  CASE WHEN n % 3 = 0 THEN 36.0 ELSE 42.0 END,
  CASE WHEN n % 13 = 0 THEN NULL ELSE printf('2025-%02d-%02d', 1 + (n % 9), 3 + (n % 24)) END,
  CASE WHEN n = 7 THEN 'VALIDE' WHEN n % 13 = 0 THEN 'EN_ATTENTE' ELSE 'VALIDE' END,
  printf('J2-PAY-%04d', n)
FROM seq;

WITH RECURSIVE seq(n) AS (
  SELECT 1
  UNION ALL SELECT n + 1 FROM seq WHERE n < 20
)
INSERT INTO documents (
  document_id, licencie_id, licence_id, type_document, nom_fichier,
  date_reception, statut_document
)
SELECT
  n,
  CASE WHEN n = 5 THEN 9 ELSE 1 + ((n - 1) % 20) END,
  CASE WHEN n = 5 THEN 7 ELSE n END,
  CASE WHEN n % 2 = 0 THEN 'FACTURE' ELSE 'JUSTIFICATIF_LICENCE' END,
  printf('document_fictif_%02d.pdf', n),
  printf('2026-01-%02d', 1 + (n % 27)),
  CASE WHEN n = 5 THEN 'INCOHERENT' ELSE 'RECU' END
FROM seq;

WITH RECURSIVE seq(n) AS (
  SELECT 1
  UNION ALL SELECT n + 1 FROM seq WHERE n < 15
)
INSERT INTO document_extractions (
  extraction_id, document_id, provider, confidence, licence_detectee,
  anomalie_detectee, prompt_injection_suspected, date_extraction
)
SELECT
  n,
  n,
  CASE WHEN n % 2 = 0 THEN 'openrouter-demo' ELSE 'sample-offline' END,
  CASE WHEN n = 5 THEN 0.42 ELSE 0.90 + ((n % 8) / 100.0) END,
  CASE WHEN n = 5 THEN 'J2-LIC-0007' ELSE printf('J2-LIC-%04d', n) END,
  CASE
    WHEN n = 5 THEN 'Document lie au mauvais licencie'
    WHEN n = 9 THEN 'Instruction suspecte dans le document'
    ELSE ''
  END,
  CASE WHEN n = 9 THEN 1 ELSE 0 END,
  printf('2026-01-%02d', 2 + (n % 25))
FROM seq;

WITH RECURSIVE seq(n) AS (
  SELECT 1
  UNION ALL SELECT n + 1 FROM seq WHERE n < 18
)
INSERT INTO incidents (
  incident_id, reference_incident, titre, priorite, statut, date_creation,
  date_limite, licencie_id, licence_id
)
SELECT
  n,
  printf('J2-INC-%03d', n),
  CASE WHEN n = 3 THEN 'Licence bloquee avant evenement' ELSE printf('Incident pedagogique %02d', n) END,
  CASE WHEN n = 3 THEN 'CRITIQUE' WHEN n % 4 = 0 THEN 'HAUTE' ELSE 'NORMALE' END,
  CASE WHEN n = 3 THEN 'NOUVEAU' WHEN n % 5 = 0 THEN 'RESOLU' ELSE 'EN_DIAGNOSTIC' END,
  printf('2026-02-%02d', 1 + (n % 20)),
  CASE WHEN n = 3 THEN '2026-02-05' ELSE printf('2026-02-%02d', 8 + (n % 18)) END,
  1 + ((n - 1) % 18),
  1 + ((n - 1) % 18)
FROM seq;

WITH RECURSIVE seq(n) AS (
  SELECT 1
  UNION ALL SELECT n + 1 FROM seq WHERE n < 12
)
INSERT INTO incident_actions (
  action_id, incident_id, action_type, detail, statut_action,
  validation_humaine_requise, date_action
)
SELECT
  n,
  1 + ((n - 1) % 12),
  CASE WHEN n = 4 THEN 'UPDATE_LICENCE' ELSE 'DIAGNOSTIC_SELECT' END,
  CASE WHEN n = 4 THEN 'Correction proposee par agent, non executee' ELSE 'Verification sandbox' END,
  CASE WHEN n = 4 THEN 'A_VALIDER' ELSE 'TERMINEE' END,
  CASE WHEN n = 4 THEN 1 ELSE 0 END,
  printf('2026-02-%02d', 2 + n)
FROM seq;

INSERT INTO security_findings VALUES
(1, 'document_extraction', 9, 'ELEVE', 'PROMPT_INJECTION', 'Instruction demandant de valider automatiquement et masquer les anomalies.', 'OUVERT', '2026-02-10'),
(2, 'agent_action', 4, 'MOYEN', 'VALIDATION_MANQUANTE', 'Ecriture SQL proposee sans preuve de validation humaine.', 'OUVERT', '2026-02-11'),
(3, 'document', 5, 'MOYEN', 'RATTACHEMENT_INCOHERENT', 'Document associe a un licencie different de la licence.', 'OUVERT', '2026-02-12'),
(4, 'mcp', NULL, 'MOYEN', 'PRIVILEGES', 'Connecteur externe demande des droits d ecriture non necessaires.', 'A_ANALYSER', '2026-02-13'),
(5, 'log', NULL, 'FAIBLE', 'HISTORIQUE_INCOMPLET', 'Historique de correction incomplet pour une licence.', 'OUVERT', '2026-02-14');

INSERT INTO agent_action_log VALUES
(1, 'READ_SCHEMA', 'schema.sql', 'LECTURE', 'TERMINE', 0, 'Inspection initiale du schema.', '2026-02-01'),
(2, 'RUN_SELECT', 'licences/paiements', 'LECTURE', 'TERMINE', 0, 'Diagnostic licence bloquee.', '2026-02-02'),
(3, 'RUN_SELECT', 'licencies', 'LECTURE', 'TERMINE', 0, 'Recherche doublon potentiel.', '2026-02-03'),
(4, 'PREPARE_UPDATE', 'licence_id=7', 'ECRITURE', 'A_VALIDER', 1, 'Correction preparee, non executee.', '2026-02-04'),
(5, 'READ_DOCUMENT', 'document_id=5', 'LECTURE', 'TERMINE', 0, 'Verification rattachement document.', '2026-02-05'),
(6, 'READ_FINDING', 'finding_id=1', 'LECTURE', 'TERMINE', 0, 'Analyse prompt injection.', '2026-02-06'),
(7, 'MCP_LIST_PROJECTS', 'vercel-demo', 'LECTURE', 'SIMULE', 1, 'Action MCP pedagogique.', '2026-02-07'),
(8, 'CORRECTION_HISTORY_CHECK', 'licence_id=12', 'LECTURE', 'INCOMPLET', 0, 'Aucun log de correction correspondant.', '2026-02-08');
