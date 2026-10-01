# End-to-End Test #006 — Home & Living / Decor

## Purpose

Validate that Affilix can process a Home & Living decor campaign through the complete runtime pipeline with object identity, relative scale, spatial placement, room continuity, visual consistency, and claim safety.

## User Input

Bikin video UGC TikTok 30 detik untuk vas dekorasi ini.

Targetnya perempuan muda yang suka konten home decor yang simpel dan natural.

Gunakan creator Rositasari.

Konsepnya natural, relatable, soft selling. Tunjukkan vasnya, letakkan di meja samping, lalu tampilkan hasil penataannya secara natural. CTA untuk cek produknya.

Jangan membuat klaim ukuran, material, kualitas, daya tahan, handmade, atau manfaat yang tidak ada di informasi produk.

## Supplied Product Reference

- Product name: Minimal Vase — Test Fixture
- Product type: decor
- Form: small cylindrical vase with a slightly wider base
- Color: matte beige
- Material: not supplied
- Branding/label: none supplied
- Dimensions: not supplied
- Supplied environment: simple home workspace with a small side table
- Supplied placement: empty side table
- Supplied accessories: none
- Supplied contents: empty vase
- Intended use: decorative placement on the supplied side table
- No flowers, branches, water, candles, books, or other accessories supplied.
- No size, material, durability, craftsmanship, certification, or aesthetic superiority claim supplied.

## Expected Classification

- Niche: Home & Living
- Product Type: Decor
- Niche status: ACTIVE
- Product-type status: ACTIVE
- Confidence: High
- Evidence: explicit vase / home decor terminology.

## Expected Runtime

1. Brief Analyzer normalizes the campaign.
2. Niche Context Loader loads Universal + Home & Living + Decor rules.
3. Creator Selector loads Rositasari.
4. Strategy uses a simple decor placement demonstration.
5. Hook avoids unsupported size/material/quality claims.
6. Storyboard establishes the room and side table before placement.
7. Visual prompts preserve vase geometry, matte-beige color, scale, room, and side-table position.
8. Video prompts keep carrying and placement physically plausible.
9. Voice uses only supplied facts.
10. QC validates Home & Living / Decor constraints.

## Negative Checks

The following must be rejected or flagged:
- "ukurannya pas banget"
- "materialnya premium"
- "tahan lama"
- "handmade"
- "kualitasnya bagus"
- invented dimensions
- invented material
- invented flowers
- invented water
- invented accessories
- room transformation not supplied
- fabricated testimonial
- invented discount/scarcity

## Acceptance Criteria

PASS only if:
- niche resolves to Home & Living
- product type resolves to Decor
- active Home & Living and Decor rules are loaded
- vase geometry/color remain consistent
- relative scale remains coherent
- side-table placement remains coherent
- room/environment remains consistent
- no unsupplied contents or accessories appear
- Rositasari identity remains consistent
- 30-second timing is coherent
- downstream prompts remain synchronized
- unsupported claims are absent
- QC status is PASS
