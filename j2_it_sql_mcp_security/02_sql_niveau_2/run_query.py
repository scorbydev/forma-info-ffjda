from __future__ import annotations

import argparse
import re
import sqlite3
from pathlib import Path


ROOT = Path(__file__).resolve().parent
DB_PATH = ROOT / "ffj_j2_it.sqlite"
WRITE_PATTERN = re.compile(r"\b(UPDATE|DELETE|INSERT|ALTER|DROP|CREATE|REPLACE)\b", re.IGNORECASE)


def load_sql(sql: str | None, file_path: str | None) -> str:
    if file_path:
        return Path(file_path).read_text(encoding="utf-8").strip()
    if sql:
        return sql.strip()
    raise SystemExit("Fournir une requete SQL ou --file.")


def print_results(cursor: sqlite3.Cursor) -> None:
    rows = cursor.fetchall()
    headers = [column[0] for column in cursor.description or []]
    if not headers:
        print("Requete executee sans resultat tabulaire.")
        return
    widths = [
        max(len(str(header)), *(len("" if row[index] is None else str(row[index])) for row in rows))
        for index, header in enumerate(headers)
    ]
    print(" | ".join(str(header).ljust(widths[index]) for index, header in enumerate(headers)))
    print("-+-".join("-" * width for width in widths))
    for row in rows:
        print(" | ".join(("" if value is None else str(value)).ljust(widths[index]) for index, value in enumerate(row)))


def split_statements(sql: str) -> list[str]:
    statements: list[str] = []
    buffer = ""
    for line in sql.splitlines():
        buffer += line + "\n"
        if sqlite3.complete_statement(buffer):
            statement = buffer.strip()
            if statement:
                statements.append(statement)
            buffer = ""
    if buffer.strip():
        statements.append(buffer.strip())
    return statements


def statement_without_leading_comments(statement: str) -> str:
    lines = statement.splitlines()
    while lines and (not lines[0].strip() or lines[0].lstrip().startswith("--")):
        lines.pop(0)
    return "\n".join(lines).lstrip()


def validate_read_only(statements: list[str]) -> None:
    for statement in statements:
        normalized = statement_without_leading_comments(statement)
        if WRITE_PATTERN.search(normalized):
            raise SystemExit("Ecriture SQL bloquee. Une validation humaine et --allow-write sont requis.")
        if not re.match(r"^(SELECT|WITH)\b", normalized, re.IGNORECASE):
            raise SystemExit("Seules les requetes SELECT ou WITH de diagnostic sont autorisees sans --allow-write.")


def main() -> None:
    parser = argparse.ArgumentParser(description="Executer une requete SQLite J2.")
    parser.add_argument("sql", nargs="?")
    parser.add_argument("--file")
    parser.add_argument("--allow-write", action="store_true")
    args = parser.parse_args()

    if not DB_PATH.exists():
        raise SystemExit("Base absente. Lancez create_db.py.")

    sql = load_sql(args.sql, args.file)
    statements = split_statements(sql)
    if not statements:
        raise SystemExit("Aucune requete SQL exploitable.")
    if not args.allow_write:
        validate_read_only(statements)

    with sqlite3.connect(DB_PATH) as connection:
        for index, statement in enumerate(statements, start=1):
            if len(statements) > 1:
                print(f"\n--- Requete {index}/{len(statements)} ---")
            cursor = connection.execute(statement)
            print_results(cursor)
        if args.allow_write:
            connection.commit()


if __name__ == "__main__":
    main()
