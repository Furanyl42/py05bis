from .dark_spellbook import dark_spell_allowed_ingredients


def dark_validate_ingredients(ingredients: str) -> str:
    lowered = ingredients.lower()
    is_valid = any(
        ingredient in lowered
        for ingredient in dark_spell_allowed_ingredients()
    )
    verdict = "VALID" if is_valid else "INVALID"
    return f"{ingredients} - {verdict}"
