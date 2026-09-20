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


# --- NEUES FEATURE: SQL WHERE-Filterung ---
def get_users_by_role(role: str, db_name: str = "app.db") -> list[tuple]:
    """Liest nur Benutzer mit einer bestimmten Rolle aus (SQL WHERE-Klausel)."""
    with sqlite3.connect(db_name) as conn:
        cursor = conn.cursor()
        cursor.execute(
            "SELECT id, name, role FROM users WHERE role = ?",
            (role,)
        )
        return cursor.fetchall()


def main():
    print("Initialisiere Datenbank...")
    init_db()

    print("Füge Test-Nutzer hinzu...")
    add_user("Baran", "Software Engineer")
    add_user("Alex", "Data Analyst")
    add_user("Sarah", "Software Engineer")

    print("\n--- Alle Nutzer ---")
    for user in get_all_users():
        print(f"[{user[0]}] {user[1]} - Rolle: {user[2]}")

    print("\n--- Gefiltert: Nur Software Engineers ---")
    engineers = get_users_by_role("Software Engineer")
    for eng in engineers:
        print(f"[{eng[0]}] {eng[1]} - Rolle: {eng[2]}")


if __name__ == "__main__":
    main()