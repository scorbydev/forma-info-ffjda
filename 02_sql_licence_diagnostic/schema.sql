PRAGMA foreign_keys = ON;

CREATE TABLE licencies (
    licencie_id INTEGER PRIMARY KEY,
    numero_licence TEXT UNIQUE,
    nom TEXT,
    prenom TEXT,
    date_naissance TEXT,
    email TEXT
);

CREATE TABLE clubs (
    club_id INTEGER PRIMARY KEY,
    code_club TEXT UNIQUE,
    nom_club TEXT,
    ligue TEXT
);

CREATE TABLE saisons (
    saison_id INTEGER PRIMARY KEY,
    libelle TEXT,
    date_debut TEXT,
    date_fin TEXT,
    active INTEGER
);

CREATE TABLE licences (
    licence_id INTEGER PRIMARY KEY,
    licencie_id INTEGER,
    club_id INTEGER,
    saison_id INTEGER,
    statut TEXT,
    type_licence TEXT,
    date_creation TEXT,
    date_validation TEXT,
    commentaire TEXT,
    FOREIGN KEY (licencie_id) REFERENCES licencies(licencie_id),
    FOREIGN KEY (club_id) REFERENCES clubs(club_id),
    FOREIGN KEY (saison_id) REFERENCES saisons(saison_id)
);

CREATE TABLE paiements (
    paiement_id INTEGER PRIMARY KEY,
    licence_id INTEGER,
    montant REAL,
    date_paiement TEXT,
    statut_paiement TEXT,
    reference_paiement TEXT,
    FOREIGN KEY (licence_id) REFERENCES licences(licence_id)
);

CREATE TABLE historique_corrections (
    correction_id INTEGER PRIMARY KEY,
    licence_id INTEGER,
    action TEXT,
    ancienne_valeur TEXT,
    nouvelle_valeur TEXT,
    motif TEXT,
    date_correction TEXT,
    operateur TEXT,
    FOREIGN KEY (licence_id) REFERENCES licences(licence_id)
);

