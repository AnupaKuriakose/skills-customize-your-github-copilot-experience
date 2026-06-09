#!/usr/bin/env python3
import argparse
import sqlite3
from datetime import datetime
from typing import List, Tuple, Optional

DB_FILE = "data.db"


def get_conn(db_file: str = DB_FILE) -> sqlite3.Connection:
    conn = sqlite3.connect(db_file)
    conn.row_factory = sqlite3.Row
    return conn


def init_db(db_file: str = DB_FILE) -> None:
    conn = get_conn(db_file)
    with conn:
        conn.execute(
            """
            CREATE TABLE IF NOT EXISTS notes (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL,
                content TEXT,
                created_at TEXT NOT NULL
            )
            """
        )
    conn.close()


def create_note(title: str, content: str, db_file: str = DB_FILE) -> int:
    conn = get_conn(db_file)
    with conn:
        cur = conn.execute(
            "INSERT INTO notes (title, content, created_at) VALUES (?, ?, ?)",
            (title, content, datetime.utcnow().isoformat()),
        )
        note_id = cur.lastrowid
    conn.close()
    return note_id


def list_notes(db_file: str = DB_FILE) -> List[Tuple]:
    conn = get_conn(db_file)
    cur = conn.execute("SELECT id, title, content, created_at FROM notes ORDER BY id DESC")
    rows = cur.fetchall()
    conn.close()
    return rows


def get_note(note_id: int, db_file: str = DB_FILE) -> Optional[sqlite3.Row]:
    conn = get_conn(db_file)
    cur = conn.execute("SELECT id, title, content, created_at FROM notes WHERE id = ?", (note_id,))
    row = cur.fetchone()
    conn.close()
    return row


def update_note(note_id: int, title: str, content: str, db_file: str = DB_FILE) -> bool:
    conn = get_conn(db_file)
    with conn:
        cur = conn.execute(
            "UPDATE notes SET title = ?, content = ? WHERE id = ?", (title, content, note_id)
        )
        updated = cur.rowcount > 0
    conn.close()
    return updated


def delete_note(note_id: int, db_file: str = DB_FILE) -> bool:
    conn = get_conn(db_file)
    with conn:
        cur = conn.execute("DELETE FROM notes WHERE id = ?", (note_id,))
        deleted = cur.rowcount > 0
    conn.close()
    return deleted


def main():
    parser = argparse.ArgumentParser(description="Simple SQLite notes demo")
    parser.add_argument("--init-db", action="store_true", help="Initialize the database file")
    parser.add_argument("--add", nargs=2, metavar=("TITLE", "CONTENT"), help="Add a new note")
    parser.add_argument("--list", action="store_true", help="List notes")
    parser.add_argument("--get", type=int, metavar="ID", help="Get note by ID")
    parser.add_argument("--update", nargs=3, metavar=("ID", "TITLE", "CONTENT"), help="Update a note")
    parser.add_argument("--delete", type=int, metavar="ID", help="Delete note by ID")
    args = parser.parse_args()

    if args.init_db:
        init_db()
        print("Initialized database.")
        return

    if args.add:
        title, content = args.add
        nid = create_note(title, content)
        print(f"Created note {nid}")
        return

    if args.list:
        rows = list_notes()
        for r in rows:
            print(f"{r['id']}: {r['title']} ({r['created_at']})")
        return

    if args.get:
        r = get_note(args.get)
        if r:
            print(f"{r['id']}: {r['title']}\n{r['content']}\nCreated: {r['created_at']}")
        else:
            print("Not found")
        return

    if args.update:
        nid_str, title, content = args.update
        nid = int(nid_str)
        ok = update_note(nid, title, content)
        print("Updated" if ok else "Not found")
        return

    if args.delete:
        ok = delete_note(args.delete)
        print("Deleted" if ok else "Not found")
        return

    parser.print_help()


if __name__ == "__main__":
    main()
