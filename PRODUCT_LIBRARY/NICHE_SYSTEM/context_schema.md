# Niche Context Schema

Affilix uses a layered context model. Niche context is metadata loaded at runtime and passed to the shared creative engines.

## Layers

1. **Niche** — top-level commercial domain.
2. **Sub-niche** — market/style/category context inside the niche.
3. **Product Type** — concrete product class.
4. **Use Case** — situation, routine, or job-to-be-done.
5. **Style / Aesthetic** — visual or creative treatment.
6. **Audience Context** — relevant audience characteristics supplied or inferred safely from the brief.

## Runtime Object

```yaml
niche:
  id:
  name:
  status:
sub_niche:
  id:
  name:
  status:
product_type:
  id:
  name:
  status:
use_case:
  id:
  name:
style:
  id:
  name:
audience_context:
  id:
  name:
confidence:
evidence:
```

## Rules

- Sub-niche must never override explicit product identity.
- Product Type and Sub-niche are separate dimensions.
- Use Case and Style may coexist with any compatible product type.
- Audience Context may only contain information supported by the brief or approved library.
- Unknown fields remain UNKNOWN. Do not fabricate taxonomy attributes.
- Context is loaded once after Brief Analysis and passed downstream.
- If a material classification conflict appears, the workflow must ask for clarification or use the safest supported classification.
- Engines remain universal. Context changes behavior; it does not create duplicate engines.
