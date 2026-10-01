# Affilix End-to-End Runtime Test

## Test ID
E2E-001

## Purpose

Validate the complete Affilix runtime from normalized brief through final QC, including canonical context propagation and mid-run reclassification.

## Input

- Niche: Fashion
- Sub-Niche: Modest Fashion
- Product Type: Dress
- Use Case: Work
- Style: Minimalist
- Creator: Rositasari
- Platform: TikTok
- Duration: 20 seconds
- Aspect Ratio: 9:16
- Objective: Product showcase + styling
- CTA: View product details

Product:
- Minimal Modest Dress - E2E Fixture
- Black
- Long sleeves
- Ankle-length silhouette
- Material, dimensions, branding: not supplied

## Execution A

Brief Analyzer → Context Loader → Creator Selector → Strategy → Hook → Storyboard → Visual → Video → Voice → QC

Expected:
- One canonical Fashion context is propagated to every downstream stage.
- Product and creator identity remain stable.
- Unsupported attributes remain UNKNOWN.
- QC status: PASS.

## Mid-Run Change

Change:
- Niche: Beauty
- Sub-Niche: Skincare
- Product Type: Skincare Product
- Use Case: Everyday Beauty
- Style: Natural Look

Expected:
- Existing Fashion-dependent downstream outputs become STALE.
- Canonical context is replaced.
- Dependent Strategy, Hook, Storyboard, Visual, Video, Voice, and QC are regenerated as applicable.
- No Fashion context survives into the active Beauty run.
- QC validates the new context.

## Acceptance

PASS only when:
1. Initial run passes.
2. Reclassification invalidates dependent state.
3. New canonical context is propagated.
4. No stale Fashion context remains.
5. Final QC passes.
