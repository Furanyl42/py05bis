import os
import site
import sys


def construct() -> None:
    is_venv = False
    lab_status = "You are working in the open"
    venv_name = "None detected"

    if sys.prefix != sys.base_prefix:
        lab_status = "The laboratory is sealed"
        is_venv = True
        venv_name = os.path.basename(sys.prefix)

    print(f"\nLABORATORY STATUS: {lab_status}\n")
    print(f"Current Python: {sys.executable}")
    print(f"Virtual Environment: {venv_name}")

    if is_venv:
        print(f"Environment Path: {sys.prefix}\n")
        print("SUCCESS: You are working in an isolated environment!")
        print("Safe to install reagents without affecting the global system.")
        print(f"\nReagent installation path:\n{site.getsitepackages()[0]}")
    else:
        print("\nWARNING: You are in the global environment!")
        print("Every reagent you install here leaks into the whole system.\n")
        print("To seal the laboratory, run:")
        print("python3 -m venv lab_env")
        print("source lab_env/bin/activate # On Unix")
        print("lab_env\\Scripts\\activate # On Windows\n")
        print("Then run this program again.")


if __name__ == "__main__":
    construct()
