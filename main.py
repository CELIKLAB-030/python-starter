import sqlite3


def init_db(db_name: str = "app.db") -> None:
    """Erstellt die Datenbank und die Tabelle, falls sie noch nicht existieren."""
    with sqlite3.connect(db_name) as conn:
        cursor = conn.cursor()
        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                role TEXT NOT NULL
            )
            """
        )
        conn.commit()


def add_user(name: str, role: str, db_name: str = "app.db") -> None:
    """Fügt einen neuen Benutzer in die Datenbank ein."""
    with sqlite3.connect(db_name) as conn:
        cursor = conn.cursor()
        # Wichtig: '?' verhindert SQL-Injections (Best Practice!)
        cursor.execute(
            "INSERT INTO users (name, role) VALUES (?, ?)",
            (name, role)
        )
        conn.commit()


def get_all_users(db_name: str = "app.db") -> list[tuple]:
    """Liest alle Benutzer aus der Datenbank aus."""
    with sqlite3.connect(db_name) as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT id, name, role FROM users")
        return cursor.fetchall()


def main():
    print("Initialisiere Datenbank...")
    init_db()

    print("Füge Test-Nutzer hinzu...")
    add_user("Baran", "Software Engineer")
    add_user("Alex", "Data Analyst")

    print("\nAlle Nutzer aus der SQL-Datenbank:")
    users = get_all_users()
    for user_id, name, role in users:
        print(f"[{user_id}] {name} - Rolle: {role}")


if __name__ == "__main__":
    main()