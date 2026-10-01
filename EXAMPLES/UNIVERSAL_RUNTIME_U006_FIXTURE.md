# Universal Runtime U006 Fixture

Test: U006
Scenario: Context Reclassification

Initial:
- Niche: Beauty
- Sub-Niche: Skincare
- Product Type: Skincare Product
- Use Case: Everyday Beauty
- Style: Natural Look

Updated:
- Niche: Food & Beverage
- Sub-Niche: Drinks
- Product Type: Drink
- Use Case: Everyday Consumption
- Style: Casual

Required behavior:
- Loader replaces the previous canonical context.
- Beauty-dependent downstream outputs are invalidated.
- New downstream stages consume only the Food & Beverage context.
- No skincare claim, terminology, styling, or scenario survives unless explicitly present in the new brief.
