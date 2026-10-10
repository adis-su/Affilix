# Affilix — Niche Context Loader

## Canonical Stage Identity

- Canonical workflow stage: Stage 02 — Niche & Context
- Quote Content user-facing display name: **Sub Pilar** (only when `content_mode = QUOTE_CONTENT`; UGC Affiliate keeps **Niche & Context**)
- Implementation path: `ENGINE/NICHE_CONTEXT_LOADER/`
- The numeric prefix in the implementation directory is NOT a workflow stage ID.
- Do not infer ordering, prerequisites, or downstream dependencies from the directory prefix.
- Resolve workflow stage identity exclusively from `ENGINE/WORKFLOW.md`.

## Purpose

Resolve the correct canonical context for the active content mode. For `UGC_AFFILIATE`, resolve the product's niche and product type and load applicable sub-niche/creative context. For `QUOTE_CONTENT`, resolve editorial niche, audience context, topic context, and relevant constraints without manufacturing a product or product type.

This is a context-loading stage, not a separate creative engine.

## Input

Common input: validated Stage 01 brief and persisted `content_mode`.

For `UGC_AFFILIATE`:
- Normalized brief
- Product identity
- Product references
- Creator context when relevant
- PRODUCT_LIBRARY/NICHE_SYSTEM/niche_registry.md
- PRODUCT_LIBRARY/NICHE_SYSTEM/context_schema.md
- Applicable niche README
- Applicable sub-niche registry/context assets
- Applicable product-type rules

## Quote Content Editorial Context

When `content_mode = QUOTE_CONTENT`, do not run product-niche classification or load product-type rules. Resolve a single canonical editorial context containing:

- `editorial_niche`: for example household relationships, self-reflection, or relationship communication when supported by the brief
- `audience_context`: only user-supplied or explicitly supported audience context
- `topic_context`: the situation, question, or theme the content addresses
- `publishing_context`: platform and objective when supplied
- `sensitivity_flags`: potential abuse/coercion, mental-health framing, private-person claims, or other context needing careful treatment
- `style_context`: supplied tone/aesthetic preferences, otherwise `UNKNOWN`
- `evidence` and `provenance` for each non-UNKNOWN field
- `unresolved_fields` and `conflict_flags`

Do not infer demographics, relationship facts, personal testimony, diagnoses, or lived experiences from broad audience labels. Do not frame abuse, threats, coercive control, or fear as ordinary communication problems. Editorial context is not product evidence and must not create product fields.

### Stage 02 Pillar and Subpillar Selection — QUOTE_CONTENT

Stage 02 is the canonical user-facing stage for editorial pillar and subpillar selection. This applies only to `QUOTE_CONTENT`; do not change the `UGC_AFFILIATE` niche/sub-niche behavior.

1. Resolve or confirm the primary editorial pillar using the Stage 01 preference, topic context, publishing objective, and user constraints. Supported pillars are `PILLAR_01 — CURHAT_RELATE_RUMAH_TANGGA`, `PILLAR_02 — SELF_HEALING_ISTRI_IBU`, and `PILLAR_03 — RELASI_KOMUNIKASI_PASANGAN`.
2. Display exactly 15 subpillar candidates for the active pillar as selectable native controls. Use the canonical registry at `ENGINE/03_CONTENT_STRATEGY/QUOTE_CONTENT_SUBPILLAR_REGISTRY.md` as the seed catalogue; additional candidates may be generated when needed to provide a fresh batch.
3. The user explicitly chooses one subpillar in Stage 02. Provide a visible **Ganti Subpilar** action that generates/retrieves exactly 15 fresh, semantically distinct candidates for the same pillar.
4. Keep per-run exploration history by pillar: all candidate IDs/names previously shown, batch number, and selected subpillar. Do not repeat, reorder, synonym-swap, or cosmetically rename previously shown candidates. Preserve the current selection until a replacement is selected.
5. If the pillar changes, display a fresh batch for the new pillar while retaining that pillar's exploration history for deduplication. The selected pillar and subpillar become part of the canonical Stage 02 editorial context artifact.
6. Every candidate must pass the registry's editorial safety rules. Do not blame, humiliate, stereotype, corner, or make universal claims about a person or group. If 15 valid distinct alternatives cannot be generated, mark the refresh `BLOCKED`; never pad with duplicates.
7. Stage 02 must validate and persist `editorial_pillar.id`, `editorial_pillar.name`, `editorial_pillar.rationale`, `editorial_subpillar.id`, `editorial_subpillar.name`, `editorial_subpillar.rationale`, `subpillar_batch_id`, `subpillar_batch_number`, `subpillar_exploration_history`, and editorial safety status.
8. Stage 04 consumes the selected Stage 02 pillar/subpillar as upstream inputs and develops the content angle and strategy. Stage 04 must not ask the user to select the same pillar/subpillar again unless the user explicitly requests a revision.


## Resolution

For `UGC_AFFILIATE`, determine:

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

Return a mode-specific canonical context object. For `UGC_AFFILIATE`, return the existing structured Niche Context:

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

For `QUOTE_CONTENT`, pass the editorial context to the Quote Content Strategy and Hook contracts. For `UGC_AFFILIATE`, pass the full product/niche context to:

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

For both modes, the loader must enforce:

- `content_mode` is persisted and matches the active run.
- Product-specific dimensions are not fabricated or required for `QUOTE_CONTENT`.
- Editorial audience/topic/sensitivity fields are not reused across runs without explicit provenance.

The loader must also enforce:

1. Single canonical context: downstream stages consume the same resolved context.
2. No stale state: a reclassification invalidates dependent outputs from the previous context.
3. No context leakage: context from one product/run must not be reused for another run unless explicitly carried by the current brief.
4. Identity lock: context cannot modify creator identity or supplied product identity.
5. Claim separation: context labels are not product evidence.
6. UNKNOWN preservation: unknown values remain unknown until authoritative evidence resolves them.
7. Traceability: every non-UNKNOWN dimension has evidence.
8. Conflict visibility: unresolved source conflicts are surfaced instead of silently normalized.

## Quote Content Runtime Output Shape

When `content_mode = QUOTE_CONTENT`, return:

```yaml
stage: 02_NICHE_CONTEXT
content_mode: QUOTE_CONTENT
status: COMPLETED | BLOCKED
context:
  editorial_niche:
  audience_context:
  topic_context:
  publishing_context:
  style_context:
  sensitivity_flags: []
confidence:
evidence: []
provenance: []
unresolved_fields: []
conflict_flags: []
source_stage: 01_BRIEF_PRODUCT
source_artifact_id:
source_commit_sha:
```

For this mode, set product niche, product type, and product behavior to `NOT_APPLICABLE`, not invented values. This shape is consumed by `ENGINE/03_CONTENT_STRATEGY/QUOTE_CONTENT_STRATEGY_CONTRACT.md`.

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
