def validate_ingredients(ingredients: str) -> str:
    from .light_spellbook import light_spell_allowed_ingredients

    valid = " - INVALID"
    for allowed in light_spell_allowed_ingredients():
        if allowed in ingredients.lower():
            valid = " - VALID"
    return ingredients + valid
