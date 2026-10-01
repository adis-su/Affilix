# Affilix — Niche Context Loader

## Purpose

Resolve the product's niche and product type, then load the applicable context for downstream UGC generation.

This is a context-loading stage, not a separate creative engine.

## Input

- Normalized brief
- Product identity
- Product references
- PRODUCT_LIBRARY/NICHE_SYSTEM/niche_registry.md
- Applicable niche README
- Applicable product-type rules

## Resolution

Determine:

- niche_id
- niche_name
- niche_status
- product_type_id
- product_type_name
- product_type_status
- classification_confidence
- evidence/source

Use the normalized brief first, then approved Product Library data and supplied references.

Never invent a product category merely to avoid UNKNOWN.

## Context Loading

Always load:
1. Universal Product Library rules
2. Niche rules when the niche is ACTIVE
3. Product-type rules when the product type is ACTIVE

If a niche or product type is PLANNED, preserve that status and do not fabricate missing detailed rules.

## Output

Return a structured Niche Context:

- Niche
- Product Type
- Status
- Confidence
- Evidence
- Universal Rules Loaded
- Niche Rules Loaded
- Product-Type Rules Loaded
- Unresolved Context
- Required Clarification, if any

## Downstream Use

Pass the context to:

- Content Strategy
- Hook Engine
- Storyboard Engine
- Visual Prompt Engine
- Video Prompt Engine
- Voice Script Engine when relevant
- Quality Control

The context may influence creative patterns, interaction design, visual requirements, claim handling, and QC.

It may not override:
- latest explicit user instruction
- campaign requirements
- approved product facts
- approved creator identity

## Reclassification

If product identity, product type, or niche changes, reload this stage and re-run all dependent downstream stages.

## Example

Input:
"Create a TikTok UGC for this moisturizer. Use Rositasari. Morning routine."

Resolved:
- Niche: Beauty
- Product Type: Skincare
- Status: ACTIVE
- Evidence: explicit product terminology
- Loaded: universal + Beauty + Skincare rules

The loader must not infer unsupported skincare claims from the word "moisturizer."
