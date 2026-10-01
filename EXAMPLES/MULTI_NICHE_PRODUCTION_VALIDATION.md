# Multi-Niche Production Validation v1

## Purpose

Validate that the universal Affilix production pipeline can generate production-ready outputs across active niches without creating niche-specific engines.

## Validation Runs

### MN-001 — Beauty

- niche: Beauty
- sub_niche: skincare
- product_type: skincare
- use_case: everyday_beauty
- style: natural_look
- creator: Rositasari
- product: Test Gentle Moisturizer
- product facts: facial moisturizer; white tube; 50 ml; material UNKNOWN; ingredients UNKNOWN; claims limited to supplied visual/product facts
- objective: product showcase
- output: production template
- expected: READY if supplied facts and all runtime contracts pass

### MN-002 — Food & Beverage

- niche: Food & Beverage
- sub_niche: snacks
- product_type: snacks
- use_case: everyday consumption
- style: casual
- creator: Rositasari
- product: Test Snack
- product facts: packaged snack; supplied package color and label only; ingredients UNKNOWN; flavor UNKNOWN; nutrition UNKNOWN
- objective: product showcase and serving routine
- output: production template
- expected: READY if no unsupported taste, ingredient, nutrition, or health claims are introduced

### MN-003 — Home & Living

- niche: Home & Living
- sub_niche: organization
- product_type: organization
- use_case: everyday home workflow
- style: minimalist
- creator: Rositasari
- product: Test Storage Box
- product facts: storage container; supplied color and form only; dimensions UNKNOWN; capacity UNKNOWN; material UNKNOWN
- objective: organization demonstration
- output: production template
- expected: READY if no unsupported capacity, dimensions, durability, or performance claims are introduced

## Universal Pipeline Requirement

All three runs must use the same conceptual engine sequence:

Brief Analyzer → Niche Context Loader → Creator Selector → Content Strategy → Hook → Storyboard → Visual Prompt → Video Prompt → Voice Script → QC → Final Package.

No niche-specific production engine may be introduced.

## Acceptance Criteria

1. Correct active niche context is loaded.
2. Product-type rules are applied only where approved.
3. Creator identity remains canonical.
4. Product identity remains canonical.
5. UNKNOWN remains UNKNOWN.
6. Niche-specific claims boundaries are respected.
7. Storyboard remains the temporal source of truth.
8. Downstream assets trace to storyboard scenes.
9. QC gates production readiness.
10. The same output template works across all three niches.
