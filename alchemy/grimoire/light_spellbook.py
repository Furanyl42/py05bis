from .light_validator import validate_ingredients


def light_spell_allowed_ingredients() -> list[str]:
    return ["earth", "air", "fire", "water"]


def light_spell_record(spell_name: str, ingredients: str) -> str:
    validate_str = validate_ingredients(ingredients)
    valid = "INVALID" not in validate_str
    spell = "recorded" if valid else "rejected"
    return f"Spell {spell}: {spell_name} ({validate_str})"
