import React from "react";
import { createRoot } from "react-dom/client";
import "./style.css";

const metrics = [
  { label: "Incidents", value: "18", detail: "3 prioritaires", tone: "red" },
  { label: "Documents", value: "20", detail: "15 extractions", tone: "blue" },
  { label: "Alertes", value: "5", detail: "1 injection suspectee", tone: "amber" },
  { label: "Deploiement", value: "Pret", detail: "Build local requis", tone: "green" },
];

const checks = [
  ["Build frontend", "A verifier"],
  ["Donnees reelles", "Absentes"],
  ["Secrets", "Absents"],
  ["Validation humaine", "Requise"],
];

function App() {
  return (
    <main>
      <header className="topbar">
        <div>
          <span className="eyebrow">ENVIRONNEMENT SANDBOX</span>
          <h1>FFJ IT MCP Demo</h1>
        </div>
        <span className="status"><i /> Service local</span>
      </header>

      <section className="intro">
        <p>
          Tableau de bord pedagogique pour observer un build, un deploiement et
          les informations accessibles via Vercel MCP.
        </p>
        <strong>Aucune donnee FFJDA reelle.</strong>
      </section>

      <section className="metrics" aria-label="Indicateurs pedagogiques">
        {metrics.map((metric) => (
          <article className="metric" key={metric.label}>
            <span className={`marker ${metric.tone}`} />
            <div>
              <p>{metric.label}</p>
              <h2>{metric.value}</h2>
              <small>{metric.detail}</small>
            </div>
          </article>
        ))}
      </section>

      <section className="workspace">
        <div>
          <h2>Controle avant publication</h2>
          <p className="muted">Les actions externes restent soumises a validation humaine.</p>
          <div className="checks">
            {checks.map(([label, value]) => (
              <div className="check" key={label}>
                <span>{label}</span>
                <strong>{value}</strong>
              </div>
            ))}
          </div>
        </div>
        <aside>
          <span className="step">ETAPE SUIVANTE</span>
          <h2>Inspecter le deploiement</h2>
          <p>Construire localement, puis utiliser Vercel CLI ou MCP en lecture seule.</p>
          <code>npm run build</code>
        </aside>
      </section>
    </main>
  );
}

createRoot(document.getElementById("root")).render(
  <React.StrictMode>
    <App />
  </React.StrictMode>,
);

