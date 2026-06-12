from pathlib import Path
import sqlite3


ROOT = Path(__file__).resolve().parent
DB_PATH = ROOT / "ffj_licences.sqlite"


def main() -> None:
    if DB_PATH.exists():
        DB_PATH.unlink()

    with sqlite3.connect(DB_PATH) as connection:
        connection.executescript((ROOT / "schema.sql").read_text(encoding="utf-8"))
        connection.executescript((ROOT / "sample_data.sql").read_text(encoding="utf-8"))

    print(f"Base SQLite creee avec succes: {DB_PATH}")


if __name__ == "__main__":
    main()

