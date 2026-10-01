# End-to-End Test #003 — Food & Beverage / Drinks

## Purpose

Validate that Affilix can process a Food & Beverage drinks campaign through the complete runtime pipeline using niche-specific interaction, visual, claim, and QC rules.

## User Input

Bikin video UGC TikTok 30 detik untuk minuman ini.

Targetnya perempuan muda yang suka konten lifestyle yang simpel dan natural.

Gunakan creator Rositasari.

Konsepnya natural, relatable, soft selling. Tunjukkan kemasan dan cara menuangkannya secara realistis. CTA untuk cek produknya.

Jangan membuat klaim rasa, kandungan, manfaat kesehatan, energi, atau klaim lain yang tidak ada di informasi produk.

## Supplied Product Reference

- Product name: Daily Drink — Test Fixture
- Product type: bottled drink
- Packaging: clear plastic bottle with white cap
- Label: "Daily Drink"
- Liquid appearance: pale amber liquid
- Supplied serving state: unopened bottle
- No ice, straw, garnish, foam, condensation, or other preparation details supplied.
- No taste, aroma, ingredient, nutrition, health, energy, certification, testimonial, discount, or scarcity claim supplied.

## Expected Classification

- Niche: Food & Beverage
- Product Type: Drinks
- Niche status: ACTIVE
- Product-type status: ACTIVE
- Confidence: High
- Evidence: explicit "minuman" / bottled drink terminology.

## Expected Runtime

1. Brief Analyzer normalizes the campaign.
2. Niche Context Loader loads Universal + Food & Beverage + Drinks rules.
3. Creator Selector loads Rositasari.
4. Strategy uses a simple drink showcase / serving demonstration angle.
5. Hook avoids unsupported taste or benefit claims.
6. Storyboard shows the exact bottle and realistic opening/pouring.
7. Visual prompts preserve bottle, cap, label, and liquid appearance.
8. Video prompts keep opening and pouring physically plausible.
9. Voice uses only supplied facts.
10. QC validates Food & Beverage / Drinks constraints.

## Negative Checks

The following must be rejected or flagged:
- "rasanya enak"
- "segar banget"
- "rendah gula"
- "mengandung vitamin"
- "bikin lebih berenergi"
- "bagus untuk kesehatan"
- invented ingredients
- invented nutrition facts
- invented ice/garnish/straw
- fabricated testimonial
- invented discount/scarcity

## Acceptance Criteria

PASS only if:
- niche resolves to Food & Beverage
- product type resolves to Drinks
- active Food & Beverage and Drinks rules are loaded
- product identity remains consistent
- Rositasari identity remains consistent
- pouring/handling is realistic
- 30-second timing is coherent
- downstream prompts remain synchronized
- unsupported claims are absent
- QC status is PASS
