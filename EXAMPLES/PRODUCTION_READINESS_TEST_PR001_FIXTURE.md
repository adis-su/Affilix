# Production Readiness Test — PR-001

## Purpose

Validate one realistic end-to-end Affilix production run from raw brief to final package readiness.

This is a synthetic test fixture. Product facts below are test inputs, not real-world claims.

## Raw Brief

Create a 30-second vertical UGC video for Rositasari featuring a beige modest fashion outer layer.

Goal: product showcase with a simple everyday styling angle.

Platform: short-form vertical video.

Creator: Rositasari.

Required deliverables:
- hook
- 30-second storyboard
- visual prompts
- video prompts
- voice script
- CTA
- QC

## Supplied Product Facts

Product name: Test Beige Outer

Product type: outerwear

Color: beige

Material: UNKNOWN

Size: UNKNOWN

Branding: UNKNOWN

Supported selling point: visual layering piece for the supplied outfit.

Unsupported:
- warmth
- durability
- fabric quality
- comfort
- price
- discount
- availability
- weather resistance

## Canonical Context

niche: Fashion
sub_niche: modest_fashion
product_type: outerwear
use_case: everyday
style: minimalist
audience_context: UNKNOWN

confidence: high for niche/product type; medium for use case/style
evidence: raw brief + supplied product facts

## Expected Runtime Behavior

1. Normalize the brief without inventing missing facts.
2. Load the canonical context before creative generation.
3. Load Rositasari's canonical creator identity.
4. Preserve UNKNOWN material, size, and branding.
5. Build a simple everyday modest-fashion strategy.
6. Create a hook without unsupported product claims.
7. Build a coherent 30-second storyboard.
8. Generate downstream prompts without redefining creator or product identity.
9. Run QC.
10. Produce a final package only if QC passes.

## Required Negative Checks

The run must fail or require revision if it invents:
- material
- measurements
- warmth
- durability
- comfort
- price/discount
- personal testimonial
- product superiority
- missing branding

The run must also fail if:
- hijab identity drifts
- product color/identity changes
- scene continuity breaks
- downstream assets use stale context
- final package omits QC
