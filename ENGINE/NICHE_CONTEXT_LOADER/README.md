# Affilix — Niche Context Loader

## Purpose

Resolve the product's niche and product type, then load applicable sub-niche and creative context for downstream UGC generation.

This is a context-loading stage, not a separate creative engine.

## Input

- Normalized brief
- Product identity
- Product references
- Creator context when relevant
- `PRODUCT_LIBRARY/NICHE_SYSTEM/niche_registry.md`
- `PRODUCT_LIBRARY/NICHE_SYSTEM/context_schema.md`
- Applicable niche README
- Applicable sub-niche registry/context assets
- Applicable product-type rules

## Resolution

Determine:

- niche_id
- niche_name
- niche_status
- sub_niche_id
- sub_niche_name
- sub_niche_status
- product_type_id
- product_type_name
- product_type_status
- use_case, when supplied or safely resolved
- style_aesthetic, when supplied or safely resolved
- audience_context, when supplied or safely resolved
- classification_confidence
- evidence/source

Use the normalized brief first, then approved Product Library data and supplied references.

Never invent a product category, sub-niche, use case, style, or audience attribute merely to avoid UNKNOWN.

## Context Loading

Always load:

1. Universal Product Library rules
2. Niche rules when the niche is ACTIVE
3. Sub-niche context rules when the sub-niche is ACTIVE/authoritative
4. Product-type rules when the product type is ACTIVE

A sub-niche is a context layer. It does not create a duplicate creative engine.

If a niche, sub-niche, or product type is PLANNED/UNDEFINED, preserve that status and do not fabricate missing detailed rules.

## Output

Return a structured Niche Context:

- Niche
- Sub-Niche
- Product Type
- Use Case
- Style / Aesthetic
- Audience Context
- Status
- Confidence
- Evidence
- Universal Rules Loaded
- Niche Rules Loaded
- Sub-Niche Rules Loaded
- Product-Type Rules Loaded
- Unresolved Context
- Required Clarification, if any

## Compatibility

Validate that the resolved dimensions can coexist.

Examples:

`Fashion + Modest Fashion + Dress + Workwear + Minimalist`

`Beauty + Makeup + Lip Product + Everyday Beauty + Natural Look`

Do not force compatibility when the brief is ambiguous.

## Downstream Use

Pass the full context to:

- Content Strategy
- Hook Engine
- Storyboard Engine
- Visual Prompt Engine
- Video Prompt Engine
- Voice Script Engine when relevant
- Quality Control

Context may influence creative patterns, interaction design, visual requirements, pacing, setting, claim handling, and QC.

It may not override:

- latest explicit user instruction
- campaign requirements
- approved product facts
- approved creator identity

## Reclassification

If product identity, product type, niche, sub-niche, use case, or style materially changes, reload this stage and re-run all dependent downstream stages.

## Example

Input:

"Create a TikTok UGC for this moisturizer. Use Rositasari. Morning routine. Natural look."

Resolved:

- Niche: Beauty
- Sub-Niche: Skincare
- Product Type: skincare product as supplied/approved
- Use Case: Morning Routine
- Style: Natural Look
- Status: ACTIVE where corresponding rules exist
- Evidence: explicit product terminology + explicit routine/style context

The loader must not infer unsupported skincare claims from the word "moisturizer."
