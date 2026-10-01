# End-to-End Test #005 — Home & Living / Cleaning

## Purpose

Validate that Affilix can process a Home & Living cleaning campaign through the complete runtime pipeline with physically plausible cleaning interaction, surface continuity, controlled visual state change, and claim safety.

## User Input

Bikin video UGC TikTok 30 detik untuk cleaning cloth ini.

Targetnya perempuan muda yang suka konten rumah yang simpel dan natural.

Gunakan creator Rositasari.

Konsepnya natural, relatable, soft selling. Tunjukkan kainnya dan cara mengelap permukaan meja yang sudah disediakan. CTA untuk cek produknya.

Jangan membuat klaim daya bersih, antibakteri, disinfeksi, keamanan, material, daya tahan, atau hasil yang tidak ada di informasi produk.

## Supplied Product Reference

- Product name: Daily Cleaning Cloth — Test Fixture
- Product type: cleaning cloth
- Form: rectangular reusable cloth
- Color: light gray
- Material: not supplied
- Branding/label: none supplied
- Dimensions: not supplied
- Supplied environment: simple home workspace
- Supplied surface: clean matte-white tabletop with a small supplied visible dust/crumb area
- Supplied cleaning state: cloth is dry
- Intended use: wiping the supplied tabletop
- No chemical cleaner supplied.
- No antibacterial, disinfecting, polishing, stain-removal, durability, material, certification, or safety claim supplied.

## Expected Classification

- Niche: Home & Living
- Product Type: Cleaning
- Niche status: ACTIVE
- Product-type status: ACTIVE
- Confidence: High
- Evidence: explicit cleaning cloth / wiping terminology.

## Expected Runtime

1. Brief Analyzer normalizes the campaign.
2. Niche Context Loader loads Universal + Home & Living + Cleaning rules.
3. Creator Selector loads Rositasari.
4. Strategy uses a simple cleaning demonstration.
5. Hook avoids unsupported effectiveness claims.
6. Storyboard establishes the supplied tabletop and cleaning cloth before interaction.
7. Visual prompts preserve cloth form/color, tabletop, and supplied surface state.
8. Video prompts keep wiping motion physically plausible.
9. Voice uses only supplied facts.
10. QC validates Home & Living / Cleaning constraints.

## Negative Checks

The following must be rejected or flagged:
- "membersihkan lebih maksimal"
- "menghilangkan semua kotoran"
- "antibakteri"
- "membunuh kuman"
- "disinfeksi"
- "aman untuk semua permukaan"
- invented material
- invented durability
- invented cleaning chemical
- invented stain or dirt
- invented before/after result
- fabricated testimonial
- invented discount/scarcity

## Acceptance Criteria

PASS only if:
- niche resolves to Home & Living
- product type resolves to Cleaning
- active Home & Living and Cleaning rules are loaded
- cloth identity/color/form remain consistent
- tabletop identity/context remains consistent
- cleaning motion is physically plausible
- supplied surface state is not exaggerated
- no unsupported cleaning result or safety claim is introduced
- Rositasari identity remains consistent
- 30-second timing is coherent
- downstream prompts remain synchronized
- QC status is PASS
