def greet(name: str) -> str:
    """Gibt eine personalisierte Begrüßung zurück."""
    return f"Hallo {name}, willkommen in deinem ersten GitHub-Projekt!"


def main():
    user_name = "Baran"
    message = greet(user_name)
    print(message)


if __name__ == "__main__":
    main()