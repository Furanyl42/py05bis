from .dark_validator import dark_validate_ingredients

_DARK_INGREDIENTS: list[str] = ["bats", "frogs", "arsenic", "eyeball"]


def dark_spell_allowed_ingredients() -> list[str]:
    return list(_DARK_INGREDIENTS)


def dark_spell_record(spell_name: str, ingredients: str) -> str:
    report = dark_validate_ingredients(ingredients)
    outcome = "recorded" if report.endswith(" - VALID") else "rejected"
    return f"Spell {outcome}: {spell_name} ({report})"
