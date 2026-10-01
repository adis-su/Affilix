# Affilix End-to-End Runtime Test

## Test ID
E2E-001

## Purpose

Validate the complete current Affilix runtime from normalized brief through Production Output, including canonical context propagation, stale-state invalidation, action/reference continuity, and exact-duration handling.

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

## Execution A

Product Intake → Campaign Intake → Context Loader → Creator Selector → Strategy → Hook → Storyboard → Visual → Video → Voice → Production Output

Expected:
- One canonical Fashion context is propagated downstream.
- Product and creator identity remain stable.
- Unsupported attributes remain UNKNOWN.
- Storyboard owns temporal/action continuity.
- Visual and Video preserve reference-state continuity.
- Video segments sum exactly to 20 seconds.
- Production Output assembles current state without introducing new facts.

## Mid-Run Change

Change:
- Niche: Beauty
- Sub-Niche: Skincare
- Product Type: Skincare Product
- Use Case: Everyday Beauty
- Style: Natural Look

Expected:
- Existing Fashion-dependent outputs become STALE.
- Canonical context is replaced.
- Dependent Strategy, Hook, Storyboard, Visual, Video, and Voice are regenerated as applicable.
- No Fashion context survives in the active Beauty state.
- Production Output is regenerated from the current state.

## Acceptance

PASS only when:
1. Initial run passes.
2. Reclassification invalidates affected dependents.
3. New canonical context is propagated.
4. No stale Fashion context remains.
5. Action/reference continuity remains valid.
6. Requested duration remains exact.
7. Final Production Output contains only current required artifacts.
