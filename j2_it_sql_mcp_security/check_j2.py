from __future__ import annotations

from pathlib import Path
import subprocess
import sys


ROOT = Path(__file__).resolve().parent
REQUIRED = (
    "01_agents_guardrails",
    "02_sql_niveau_2",
    "03_vercel_mcp",
    "04_security_agentique",
    "docs",
    "prompts",
)


def main() -> None:
    missing = [name for name in REQUIRED if not (ROOT / name).exists()]
    if missing:
        raise SystemExit(f"Dossiers manquants: {', '.join(missing)}")

    create_script = ROOT / "02_sql_niveau_2" / "create_db.py"
    subprocess.run([sys.executable, str(create_script)], check=True)

    query_script = ROOT / "02_sql_niveau_2" / "run_query.py"
    query = subprocess.run(
        [sys.executable, str(query_script), "SELECT COUNT(*) AS nb FROM licencies;"],
        check=True,
        capture_output=True,
        text=True,
    )
    if "35" not in query.stdout:
        raise SystemExit(f"Resultat SELECT inattendu:\n{query.stdout}")

    print("Check J2 OK")
    print("- requete SELECT via run_query.py: OK (35 licencies)")
    print("- mini app: cd 03_vercel_mcp/mini_app && npm install && npm run build")
    print("- MCP: npx add-mcp https://mcp.vercel.com")


if __name__ == "__main__":
    main()
