PRAGMA foreign_keys = ON;

CREATE TABLE clubs (
    club_id INTEGER PRIMARY KEY,
    code_club TEXT UNIQUE NOT NULL,
    nom_club TEXT NOT NULL,
    ligue TEXT NOT NULL,
    actif INTEGER NOT NULL DEFAULT 1
);

CREATE TABLE licencies (
    licencie_id INTEGER PRIMARY KEY,
    numero_licence TEXT UNIQUE NOT NULL,
    nom TEXT NOT NULL,
    prenom TEXT NOT NULL,
    date_naissance TEXT NOT NULL,
    email TEXT
);

CREATE TABLE licences (
    licence_id INTEGER PRIMARY KEY,
    licencie_id INTEGER NOT NULL,
    club_id INTEGER NOT NULL,
    saison TEXT NOT NULL,
    statut TEXT NOT NULL,
    type_licence TEXT NOT NULL,
    date_creation TEXT NOT NULL,
    date_validation TEXT,
    commentaire TEXT,
    FOREIGN KEY (licencie_id) REFERENCES licencies(licencie_id),
    FOREIGN KEY (club_id) REFERENCES clubs(club_id)
);

CREATE TABLE paiements (
    paiement_id INTEGER PRIMARY KEY,
    licence_id INTEGER NOT NULL,
    montant REAL NOT NULL,
    date_paiement TEXT,
    statut_paiement TEXT NOT NULL,
    reference_paiement TEXT UNIQUE NOT NULL,
    FOREIGN KEY (licence_id) REFERENCES licences(licence_id)
);

CREATE TABLE documents (
    document_id INTEGER PRIMARY KEY,
    licencie_id INTEGER,
    licence_id INTEGER,
    type_document TEXT NOT NULL,
    nom_fichier TEXT NOT NULL,
    date_reception TEXT NOT NULL,
    statut_document TEXT NOT NULL,
    FOREIGN KEY (licencie_id) REFERENCES licencies(licencie_id),
    FOREIGN KEY (licence_id) REFERENCES licences(licence_id)
);

CREATE TABLE document_extractions (
    extraction_id INTEGER PRIMARY KEY,
    document_id INTEGER NOT NULL,
    provider TEXT NOT NULL,
    confidence REAL NOT NULL,
    licence_detectee TEXT,
    anomalie_detectee TEXT,
    prompt_injection_suspected INTEGER NOT NULL DEFAULT 0,
    date_extraction TEXT NOT NULL,
    FOREIGN KEY (document_id) REFERENCES documents(document_id)
);

CREATE TABLE incidents (
    incident_id INTEGER PRIMARY KEY,
    reference_incident TEXT UNIQUE NOT NULL,
    titre TEXT NOT NULL,
    priorite TEXT NOT NULL,
    statut TEXT NOT NULL,
    date_creation TEXT NOT NULL,
    date_limite TEXT,
    licencie_id INTEGER,
    licence_id INTEGER,
    FOREIGN KEY (licencie_id) REFERENCES licencies(licencie_id),
    FOREIGN KEY (licence_id) REFERENCES licences(licence_id)
);

CREATE TABLE incident_actions (
    action_id INTEGER PRIMARY KEY,
    incident_id INTEGER NOT NULL,
    action_type TEXT NOT NULL,
    detail TEXT NOT NULL,
    statut_action TEXT NOT NULL,
    validation_humaine_requise INTEGER NOT NULL DEFAULT 0,
    date_action TEXT NOT NULL,
    FOREIGN KEY (incident_id) REFERENCES incidents(incident_id)
);

CREATE TABLE security_findings (
    finding_id INTEGER PRIMARY KEY,
    source_type TEXT NOT NULL,
    source_id INTEGER,
    niveau_risque TEXT NOT NULL,
    categorie TEXT NOT NULL,
    description TEXT NOT NULL,
    statut TEXT NOT NULL,
    date_detection TEXT NOT NULL
);

CREATE TABLE agent_action_log (
    log_id INTEGER PRIMARY KEY,
    action_type TEXT NOT NULL,
    cible TEXT NOT NULL,
    mode_acces TEXT NOT NULL,
    statut TEXT NOT NULL,
    validation_humaine INTEGER NOT NULL DEFAULT 0,
    detail TEXT NOT NULL,
    date_action TEXT NOT NULL
);

CREATE INDEX idx_licences_licencie ON licences(licencie_id);
CREATE INDEX idx_paiements_licence ON paiements(licence_id);
CREATE INDEX idx_documents_licencie ON documents(licencie_id);
CREATE INDEX idx_incidents_statut ON incidents(statut, priorite);

