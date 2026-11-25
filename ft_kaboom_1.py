def ft_kaboom_1() -> None:
    print("=== Kaboom 1 ===")
    print("Access to alchemy/grimoire/dark_spellbook.py directly")
    print(
        "Test import now - THIS WILL RAISE AN UNCAUGHT EXCEPTION", flush=True
    )
    from alchemy.grimoire.dark_spellbook import (
        dark_spell_record,
    )

    print(
        f"Testing record dark spell: "
        f"{dark_spell_record('Avada Kedavra', 'Bats and poo')}"
    )


if __name__ == "__main__":
    ft_kaboom_1()
