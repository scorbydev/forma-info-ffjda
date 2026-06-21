from pathlib import Path
import sqlite3


ROOT = Path(__file__).resolve().parent
DB_PATH = ROOT / "ffj_j2_it.sqlite"
TABLES = (
    "clubs",
    "licencies",
    "licences",
    "paiements",
    "documents",
    "document_extractions",
    "incidents",
    "incident_actions",
    "security_findings",
    "agent_action_log",
)


def main() -> None:
    if DB_PATH.exists():
        DB_PATH.unlink()

    with sqlite3.connect(DB_PATH) as connection:
        connection.executescript((ROOT / "schema.sql").read_text(encoding="utf-8"))
        connection.executescript((ROOT / "sample_data.sql").read_text(encoding="utf-8"))
        counts = {
            table: connection.execute(f"SELECT COUNT(*) FROM {table}").fetchone()[0]
            for table in TABLES
        }

    print(f"Base creee: {DB_PATH}")
    for table, count in counts.items():
        print(f"- {table}: {count}")


if __name__ == "__main__":
    main()

