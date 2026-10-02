# Affilix — Niche Context Loader

## Canonical Stage Identity

- Canonical workflow stage: Stage 03 — Niche & Context
- Implementation path: `ENGINE/NICHE_CONTEXT_LOADER/`
- The numeric prefix in the implementation directory is NOT a workflow stage ID.
- Do not infer ordering, prerequisites, or downstream dependencies from the directory prefix.
- Resolve workflow stage identity exclusively from `ENGINE/WORKFLOW.md`.

## Purpose

Resolve the product's niche and product type, then load applicable sub-niche and creative context for downstream UGC generation.

This is a context-loading stage, not a separate creative engine.

## Input

- Normalized brief
- Product identity
- Product references
- Creator context when relevant
- PRODUCT_LIBRARY/NICHE_SYSTEM/niche_registry.md
- PRODUCT_LIBRARY/NICHE_SYSTEM/context_schema.md
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

## Precedence

Resolve conflicts using this order:

1. Latest explicit user instruction
2. Campaign requirements
3. Approved Product Library facts and constraints
4. Approved Creator Library identity constraints
5. Niche and sub-niche context rules
6. Product-type rules
7. Platform requirements
8. Creative interpretation

Context is subordinate to explicit product facts. Style labels such as Elegant, Street, Sporty, or Minimalist can guide creative treatment but cannot override a supplied product attribute or become evidence for a product claim.

If two authoritative sources conflict at the same level, do not silently choose one. Mark the conflict as unresolved and route it to clarification/QC.

## UNKNOWN and Evidence

Every resolved dimension must be traceable to evidence.

Allowed evidence sources:

- explicit user brief
- campaign requirement
- approved Product Library
- approved Creator Library
- supplied product/creator reference
- compatible inherited context from an authoritative parent layer

Rules:

- Missing information remains UNKNOWN.
- Do not infer UNKNOWN into a concrete value from visual stereotypes, niche conventions, or desired creative output.
- A low-confidence inference must remain flagged and must not become a product fact.
- Evidence must be sufficient for the downstream use. A style label can support visual direction, but not material, quality, performance, value, or certification claims.

## Context Compatibility

Validate that the resolved dimensions can coexist.

Examples:

Fashion + Modest Fashion + Dress + Workwear + Minimalist

Beauty + Makeup + Lip Product + Everyday Beauty + Natural Look

Do not force compatibility when the brief is ambiguous.

If an explicit user instruction conflicts with a generic compatibility rule, preserve the explicit instruction and flag the compatibility issue for downstream QC unless it changes product identity or creates a safety problem.

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
- Conflict Flags, if any

## Context Loading Contract

The loader must provide one canonical context object to every downstream stage.

Downstream engines must not independently reclassify the product unless the loader explicitly requests reclassification.

The canonical object must preserve:

- resolved values
- UNKNOWN values
- evidence
- confidence
- status
- unresolved fields
- conflict flags
- loaded rule layers

This prevents one stage from silently changing a context dimension and creating cross-engine drift.

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

A reclassification must replace the previous canonical context for the current run. Do not merge stale dimensions from the previous context with newly resolved dimensions.

## Runtime Invariants

The loader must enforce:

1. Single canonical context: downstream stages consume the same resolved context.
2. No stale state: a reclassification invalidates dependent outputs from the previous context.
3. No context leakage: context from one product/run must not be reused for another run unless explicitly carried by the current brief.
4. Identity lock: context cannot modify creator identity or supplied product identity.
5. Claim separation: context labels are not product evidence.
6. UNKNOWN preservation: unknown values remain unknown until authoritative evidence resolves them.
7. Traceability: every non-UNKNOWN dimension has evidence.
8. Conflict visibility: unresolved source conflicts are surfaced instead of silently normalized.

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
