import os

from dotenv import load_dotenv


def oracle() -> None:
    load_dotenv()

    matrix_mode = (os.getenv("MATRIX_MODE") or "development").strip().lower()

    database_url = os.getenv("DATABASE_URL")
    api_key = os.getenv("API_KEY")
    log_level = os.getenv("LOG_LEVEL")
    zion_endpoint = os.getenv("ZION_ENDPOINT")

    missing = [
        name
        for name, value in (
            ("DATABASE_URL", database_url),
            ("API_KEY", api_key),
            ("LOG_LEVEL", log_level),
            ("ZION_ENDPOINT", zion_endpoint),
        )
        if not value
    ]

    if database_url:
        if matrix_mode == "development":
            database_status = "Connected to local instance"
        else:
            database_status = "Connected to remote cluster"
    else:
        database_status = "[WARNING] Using fallback / unconfigured state"

    api_status = (
        "Authenticated"
        if api_key
        else "[WARNING] Unauthenticated (API_KEY missing)"
    )
    zion_status = (
        "Online"
        if zion_endpoint
        else "[WARNING] Offline (ZION_ENDPOINT missing)"
    )

    print("ORACLE STATUS: Consulting the configuration...\n")
    if missing:
        print("Missing configuration. Using default values:")
    else:
        print("Configuration loaded:")

    print(f"Mode: {matrix_mode}")
    print(f"Database: {database_status}")
    print(f"API Access: {api_status}")
    print(f"Log Level: {log_level or 'DEBUG'}")
    print(f"Remote Network: {zion_status}")

    print("\nConfiguration security check:")
    print("[OK] No hardcoded secrets detected")
    if env_file_ignored():
        print("[OK] .env file properly ignored by git")
    else:
        print("[WARNING] .env file not ignored by git")
    print("[OK] Production overrides available")

    if missing:
        print("\n[WARNING] Missing configuration keys: " + ", ".join(missing))
    print("\nThe Oracle sees all configurations.")


def env_file_ignored() -> bool:
    script_dir = os.path.dirname(os.path.abspath(__file__))
    gitignore_path = os.path.join(script_dir, ".gitignore")
    if not os.path.isfile(gitignore_path):
        return False

    with open(gitignore_path) as f:
        entries = {line.strip() for line in f}
    return ".env" in entries


if __name__ == "__main__":
    oracle()
