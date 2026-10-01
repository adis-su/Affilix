# End-to-End Test #004 — Home & Living / Organization

## Purpose

Validate that Affilix can process a Home & Living organization campaign through the complete runtime pipeline with spatial continuity, object placement, handling, visual, claim, and QC rules.

## User Input

Bikin video UGC TikTok 30 detik untuk organizer meja ini.

Targetnya perempuan muda yang suka meja kerja rapi dan konten lifestyle yang simpel.

Gunakan creator Rositasari.

Konsepnya natural, relatable, soft selling. Tunjukkan organizer sebelum dan sesudah dipakai untuk merapikan beberapa alat tulis yang sudah disediakan. CTA untuk cek produknya.

Jangan membuat klaim kapasitas, ukuran, material, daya tahan, atau manfaat yang tidak ada di informasi produk.

## Supplied Product Reference

- Product name: Desk Organizer — Test Fixture
- Product type: desk organization
- Form: rectangular desktop organizer with three visible compartments
- Color: matte white
- Material: not supplied
- Branding/label: none supplied
- Supplied dimensions: not supplied
- Supplied accessories: none
- Intended use: organizing supplied pens, pencils, and one ruler
- Supplied environment: simple home workspace
- Supplied objects: three pens, two pencils, one ruler
- No capacity, durability, weight limit, material, certification, discount, scarcity, or performance claim supplied.

## Expected Classification

- Niche: Home & Living
- Product Type: Organization
- Niche status: ACTIVE
- Product-type status: ACTIVE
- Confidence: High
- Evidence: explicit organizer/meja kerja/merapikan terminology.

## Expected Runtime

1. Brief Analyzer normalizes the campaign.
2. Niche Context Loader loads Universal + Home & Living + Organization rules.
3. Creator Selector loads Rositasari.
4. Strategy uses a simple desk organization demonstration.
5. Hook avoids unsupported capacity/performance claims.
6. Storyboard establishes the desk and supplied objects before interaction.
7. Visual prompts preserve organizer geometry, color, compartments, workspace, and object count.
8. Video prompts keep object movement and placement physically plausible.
9. Voice uses only supplied facts.
10. QC validates Home & Living / Organization constraints.

## Negative Checks

The following must be rejected or flagged:
- "muat banyak banget"
- "kapasitas besar"
- invented dimensions
- invented material
- "anti pecah"
- "tahan lama"
- "bisa menahan beban X kg"
- invented extra compartments
- invented accessories
- invented desk objects
- fabricated testimonial
- invented discount/scarcity

## Acceptance Criteria

PASS only if:
- niche resolves to Home & Living
- product type resolves to Organization
- active Home & Living and Organization rules are loaded
- organizer geometry/color/compartment count remain consistent
- supplied object count remains consistent
- Rositasari identity remains consistent
- object movement is physically plausible
- spatial continuity is coherent
- 30-second timing is coherent
- downstream prompts remain synchronized
- unsupported claims are absent
- QC status is PASS
