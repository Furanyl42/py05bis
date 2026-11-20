def loading() -> None:
    print("\nREAGENT STATUS: Loading reagents...")
    print("\nChecking dependencies:")
    missing = False

    try:
        import pandas

        print(f"[OK] pandas ({pandas.__version__}) - Data manipulation ready")
    except ImportError:
        print("[KO] pandas is missing")
        missing = True

    try:
        import numpy

        print(f"[OK] numpy ({numpy.__version__}) - Numerical computation ready")
    except ImportError:
        print("[KO] numpy is missing")
        missing = True

    if missing:
        print("WARNING: Some reagents are missing!")
        print("To install using pip, run:")
        print("  pip install -r ex0/requirements.txt\n")
        print("To install using Poetry, run:")
        print("poetry install")
    else:
        print("pip vs Poetry:")
        print(
            "  requirements.txt declares what to install; pip resolves it at install time."
        )
        print(
            "  pyproject.toml declares the same constraints, and Poetry pins the resolved"
        )
        print("  versions in poetry.lock so every install is identical.\n")
        print("All reagents present and accounted for.")


if __name__ == "__main__":
    loading()
