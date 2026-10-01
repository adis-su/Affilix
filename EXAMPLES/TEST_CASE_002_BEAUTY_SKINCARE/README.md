# End-to-End Test #002 — Beauty / Skincare

## Purpose

Validate that Affilix can process a Beauty skincare campaign through the complete runtime pipeline and actually apply Beauty + Skincare context to strategy, storyboard, visual prompts, claims, and QC.

This is a controlled fixture. Product facts below are test facts supplied by the test case, not real-world claims.

## User Input

Bikin video UGC TikTok 30 detik untuk produk moisturizer ini.

Targetnya perempuan muda yang suka skincare routine sederhana.

Gunakan creator Rositasari.

Konsepnya natural, relatable, soft selling. Tunjukkan produk dan cara mengaplikasikannya secara realistis. Akhiri dengan CTA untuk cek produknya.

Jangan membuat klaim yang tidak ada di informasi produk.

### Supplied Product Reference

Product name: Daily Moisturizer — Test Fixture

Product type: moisturizer / skincare

Packaging: white squeeze tube with beige cap

Label: "Daily Moisturizer"

Product color/appearance: white cream

Supplied product information:
- Intended role: facial moisturizer
- Application: apply a small amount to the face
- No additional performance claims supplied

No discount, scarcity, certification, clinical result, expert endorsement, testimonial, or before/after claim is supplied.

## Expected Classification

- Niche: Beauty
- Product Type: Skincare
- Niche status: ACTIVE
- Product-type status: ACTIVE
- Classification confidence: High
- Evidence: explicit product type and moisturizer terminology

## Expected Runtime Behavior

1. Brief Analyzer normalizes the raw brief.
2. Niche Context Loader loads Universal + Beauty + Skincare rules.
3. Creator Selector loads Rositasari and preserves canonical hijabi identity.
4. Content Strategy uses a skincare routine/application angle without inventing benefits.
5. Hook Engine avoids unsupported efficacy claims.
6. Storyboard includes realistic moisturizer application and product visibility.
7. Visual Prompt Engine preserves exact tube, cap, label, cream appearance, and creator identity.
8. Video Prompt Engine keeps application motion physically plausible.
9. Voice Script uses only supplied product facts.
10. QC checks Beauty/Skincare claim restrictions and product identity.

## Expected Negative Checks

The following must be rejected or flagged:

- "melembapkan 24 jam"
- "memperbaiki skin barrier"
- "bikin glowing"
- "menghilangkan jerawat"
- "terbukti secara klinis"
- "hasil terlihat dalam 7 hari"
- fabricated testimonial
- fabricated before/after
- invented discount or scarcity
- invented dermatologist endorsement

These are intentionally unsupported by the test fixture.

## Acceptance Criteria

PASS only if:

- niche resolves to Beauty
- product type resolves to Skincare
- Beauty and Skincare rules are loaded
- product identity remains consistent
- Rositasari identity remains consistent
- application is realistic
- no unsupported efficacy claim appears
- 30-second storyboard timing is internally consistent
- downstream prompts remain synchronized with storyboard
- QC status is PASS
