from .dark_validator import dark_validate_ingredients


def dark_spell_allowed_ingredients() -> list[str]:
    return ["bats", "frogs", "arsenic", "eyeball"]


def dark_spell_record(spell_name: str, ingredients: str) -> str:
    validate_str = dark_validate_ingredients(ingredients)
    valid = "INVALID" not in validate_str
    spell = "recorded" if valid else "rejected"
    return f"Spell {spell}: {spell_name} ({validate_str})"
