# Niche Registry

| ID | Niche | Status | Initial Product Types | Sub-Niche Layer |
|---|---|---|---|---|
| fashion | Fashion | ACTIVE | clothing, hijab, shoes, bags, accessories, jewelry | ACTIVE |
| beauty | Beauty | ACTIVE | skincare, makeup, haircare, bodycare | ACTIVE |
| food_beverage | Food & Beverage | ACTIVE | snacks, drinks, coffee, cooking | Not expanded yet |
| home_living | Home & Living | ACTIVE | kitchen, organization, cleaning, decor | Not expanded yet |
| electronics | Electronics | PLANNED | smartphone accessories, audio, gadgets, smart devices | PLANNED |
| lifestyle | Lifestyle | PLANNED | daily essentials, travel, productivity, hobbies | PLANNED |
| baby_kids | Baby & Kids | PLANNED | baby, kids, parenting products | PLANNED |
| pet | Pet | PLANNED | pet food, pet accessories, pet care | PLANNED |
| sports_outdoor | Sports & Outdoor | PLANNED | fitness, running, outdoor, sports accessories | PLANNED |
| automotive | Automotive | PLANNED | car accessories, motorcycle, maintenance | PLANNED |

## Status

- ACTIVE: detailed niche and product-type rules are defined enough for runtime use.
- PLANNED: taxonomy exists, but detailed rules are not yet authoritative.

## Context Model

Active niches may expose a layered runtime context:

`Niche → Sub-Niche → Product Type → Use Case → Style / Aesthetic → Audience Context`

Sub-niche is a context layer, not a separate creative engine.

## Expansion Rule

A new niche must be registered before detailed product-type assets are added. Activation requires niche rules, product-type rules, runtime loading compatibility, and an end-to-end test case.

Sub-niche expansion follows the same principle: taxonomy is only authoritative when its context rules are defined and the runtime loader can pass the context downstream.
