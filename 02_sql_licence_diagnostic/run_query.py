from __future__ import annotations

import argparse
import sqlite3
from pathlib import Path


ROOT = Path(__file__).resolve().parent
DB_PATH = ROOT / "ffj_licences.sqlite"
BLOCKED_KEYWORDS = ("UPDATE", "DELETE", "INSERT", "ALTER", "DROP", "CREATE")


def load_sql(args: argparse.Namespace) -> str:
    if args.file:
        return Path(args.file).read_text(encoding="utf-8")
    if args.sql:
        return args.sql
    raise SystemExit("Fournir une requete SQL ou --file.")


def ensure_read_only(sql: str, allow_write: bool) -> None:
    if allow_write:
        return
    normalized = sql.upper()
    blocked = [keyword for keyword in BLOCKED_KEYWORDS if keyword in normalized]
    if blocked:
        raise SystemExit(
            "Requete bloquee sans --allow-write. Mots cles detectes: "
            + ", ".join(blocked)
        )


def print_rows(cursor: sqlite3.Cursor, rows: list[sqlite3.Row]) -> None:
    headers = [description[0] for description in cursor.description or []]
    if not headers:
        print("Requete executee, aucun resultat tabulaire.")
        return
    print(" | ".join(headers))
    print("-" * max(20, len(" | ".join(headers))))
    for row in rows:
        print(" | ".join("" if value is None else str(value) for value in row))


def main() -> None:
    parser = argparse.ArgumentParser(description="Executer une requete SQLite sandbox.")
    parser.add_argument("sql", nargs="?", help="Requete SQL a executer")
    parser.add_argument("--file", help="Fichier contenant la requete SQL")
    parser.add_argument("--allow-write", action="store_true", help="Autoriser les ecritures")
    args = parser.parse_args()

    if not DB_PATH.exists():
        raise SystemExit("Base absente. Lancez d'abord create_db.py.")

    sql = load_sql(args).strip()
    ensure_read_only(sql, args.allow_write)

    with sqlite3.connect(DB_PATH) as connection:
        connection.row_factory = sqlite3.Row
        cursor = connection.execute(sql)
        rows = cursor.fetchall()
        print_rows(cursor, rows)
        if args.allow_write:
            connection.commit()


if __name__ == "__main__":
    main()

