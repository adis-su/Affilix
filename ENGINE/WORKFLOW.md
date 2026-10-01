# Affilix — End-to-End Production Workflow v1

## Purpose

This document is the canonical execution contract for the Affilix production runtime.

The runtime should behave as one coherent system rather than exposing independent prompt modules.

## Entry Point

The user-facing entry command is `/Affilix`.

`/Affilix` → Product Intake → Brief Analysis → Niche Context → Creator → Product → Strategy → Hook → Storyboard → Visual/Video/Voice → QC → Final Package.

The entry contract is defined in `ENGINE/AFFILIX_ENTRY_POINT/README.md`.

The initial product intake requests only `Nama Produk` and `Link Produk`. After product intake, request only the minimum additional campaign information needed to continue.

## Pipeline

USER BRIEF
→ 01 BRIEF ANALYZER
→ NICHE CONTEXT LOADER
→ 02 CREATOR SELECTOR
→ 03 CONTENT STRATEGY
→ 04 HOOK ENGINE
→ 05 STORYBOARD ENGINE
→ 06 VISUAL PROMPT ENGINE
→ 07 VIDEO PROMPT ENGINE
→ 08 VOICE SCRIPT ENGINE
→ 09 QUALITY CONTROL
→ FINAL UGC PACKAGE

## Phase 1 — Intake

Accept the user's brief and extract product, creator, campaign objective, audience, platform, format, duration, aspect ratio, key message, talking points, CTA, references, restrictions, and brand requirements.

Do not invent missing requirements.

## Phase 2 — Brief Analysis

Run 01_BRIEF_ANALYZER.

Classify information as EXPLICIT, REFERENCE, SUPPORTED, INFERRED, or UNKNOWN.

Only EXPLICIT, REFERENCE, and SUPPORTED information can become authoritative production requirements.

If a missing item materially affects production, request the minimum required information.

The normalized brief becomes the input contract for all following stages.

## Phase 2B — Niche Context Loading

Run NICHE_CONTEXT_LOADER immediately after brief normalization.

Resolve:

- niche
- sub-niche
- product type
- use case
- style/aesthetic
- audience context
- status
- confidence
- evidence
- applicable universal, niche, sub-niche, and product-type rules
- unresolved context
- conflict flags

Create exactly one canonical runtime context for the current run.

Rules:

- Missing values remain UNKNOWN.
- Do not infer context merely to avoid UNKNOWN.
- Context labels cannot override explicit product facts or creator identity.
- PLANNED/UNDEFINED layers cannot be represented as authoritative active rules.
- Downstream engines consume the canonical context instead of independently reclassifying it.

## Phase 3 — Creator Selection

Run 02_CREATOR_SELECTOR.

Load character_identity.md, creator_profile.md, relevant visual references, wardrobe, expressions, and poses.

If a creator is explicitly specified, preserve that selection.

Do not create a new creator when no library creator matches.

Creator selection is part of the current run state. A creator from a previous run must not leak into a new run unless explicitly selected or supported by the current brief.

## Phase 4 — Content Strategy

Run 03_CONTENT_STRATEGY.

Define primary objective, audience, product role, content angle, core message, supporting messages, proof strategy, emotional strategy, story arc, and CTA strategy.

Use canonical niche context as creative input.

Do not turn context labels into unsupported product facts or claims.

## Phase 5 — Hook

Run 04_HOOK_ENGINE.

Generate viable hook candidates based on the approved strategy and canonical niche context.

Select or request approval for a hook when the campaign workflow requires explicit user selection.

Never invent unsupported claims merely to make a hook stronger.

## Phase 6 — Storyboard

Run 05_STORYBOARD_ENGINE.

Create the canonical scene sequence.

Every scene must have purpose, timing, action, creator state, product state, camera, environment, dialogue intent, context requirements, and continuity requirements.

Apply relevant niche, sub-niche, use-case, style, audience, and product-type rules.

Scene durations must fit the requested total duration.

The storyboard becomes the canonical temporal source for Visual, Video, and Voice.

## Phase 7 — Parallel Production Specifications

Once the storyboard is approved, run:

- 06_VISUAL_PROMPT_ENGINE
- 07_VIDEO_PROMPT_ENGINE
- 08_VOICE_SCRIPT_ENGINE

These are parallel downstream specifications, but all remain subordinate to:

1. Latest explicit user instruction
2. Campaign requirements
3. Product facts
4. Creator identity
5. Canonical niche context
6. Storyboard

No parallel engine may silently reclassify context or change a canonical fact.

## Phase 8 — Quality Control

Run 09_QUALITY_CONTROL.

Validate:

- brief compliance
- canonical runtime context
- creator identity
- product identity
- claims
- strategy
- hook
- storyboard continuity
- visual prompts
- video prompts
- voice script
- CTA
- production feasibility
- reclassification integrity
- cross-run isolation

QC is the final validation gate.

## Phase 9 — Revision Loop

### PASS

Proceed to final packaging.

Preserve all validated assets.

### REVISION REQUIRED

1. Identify the failing asset.
2. Identify its upstream source of truth.
3. Correct only the affected component.
4. Re-run dependent downstream stages.
5. Run QC again.

Do not rebuild unaffected parts of the package.

### BLOCKED

1. Stop production.
2. Identify the blocking requirement.
3. Ask only for the minimum information needed.
4. Resume from the affected stage after the missing information is resolved.

## Phase 10 — Reclassification

Reclassification is mandatory when any material context dimension changes:

- product identity
- product type
- niche
- sub-niche
- use case
- style/aesthetic
- audience context

Execution:

RECLASSIFY
→ REPLACE CANONICAL CONTEXT
→ INVALIDATE DEPENDENT OUTPUTS
→ RE-RUN AFFECTED ENGINES
→ QC

Never merge old and new context values unless the current brief explicitly carries both.

## Source-of-Truth Hierarchy

1. Latest explicit user instruction
2. Campaign requirements
3. Approved Product Library data
4. Approved Creator Library data
5. Canonical Niche Context
6. Platform requirements
7. Approved strategy
8. Creative interpretation

Niche rules are contextual rules. They cannot override a higher source-of-truth item.

Downstream prompts cannot silently override upstream canonical information.

## Dependency Rules

Creator identity change:
- re-run Creator Selector
- re-run dependent Strategy, Hook, Storyboard, Visual, Video, Voice, and QC

Product identity change:
- revalidate Product Library
- reload Niche Context
- re-run dependent Strategy, Hook, Storyboard, Visual, Video, Voice, and QC

Niche or Sub-Niche change:
- reload Niche Context
- re-run Strategy, Hook, Storyboard, Visual, Video, Voice, and QC

Product type change:
- reload Niche Context
- re-run all downstream stages dependent on product-type behavior

Use case, Style, or Audience Context change:
- reload or update canonical Niche Context
- re-run all downstream stages materially affected by the changed context
- QC must verify no stale context remains

Strategy change:
- re-run Hook, Storyboard, Visual, Video, Voice, and QC

Hook change:
- re-run affected opening storyboard scenes and their downstream Visual, Video, Voice, and QC

Storyboard change:
- re-run affected Visual, Video, Voice, and QC

Visual-only change:
- re-run Visual, Video when motion or state changes, and QC

Voice-only change:
- re-run Voice and QC

## Runtime State Rules

Each run must maintain:

- current normalized brief
- current canonical creator
- current canonical product
- current canonical niche context
- current approved strategy
- current approved hook
- current canonical storyboard
- current downstream specifications
- current QC state

State must be isolated per run.

A prior run may not supply context, product facts, creator identity, claims, or scene assumptions to the current run unless explicitly supported by current-run evidence.

When a canonical state changes, dependent state becomes STALE until regenerated and revalidated.

## Final UGC Package

A production-ready package should contain:

1. Creative Brief: objective, audience, platform, format, duration, aspect ratio, product, creator, angle, core message.
2. Creator: identity, relevant wardrobe, expression, pose, reference assets.
3. Product: identity, niche, product type, supported features, benefits, evidence, approved selling points, claim boundaries.
4. Niche Context: niche, sub-niche, product type, use case, style/aesthetic, audience context, confidence, evidence, unresolved fields.
5. Content Strategy: angle, story arc, proof strategy, CTA strategy.
6. Hook: hook concept, spoken hook, visual hook, delivery direction.
7. Storyboard: complete scene-by-scene production plan.
8. Visual Prompts: one production-ready prompt per required visual scene.
9. Video Prompts: one motion specification per required video scene.
10. Voice Script: scene-by-scene dialogue and delivery instructions.
11. QC Report: status, issues, corrections, and revalidation result.

## Runtime Behavior

When sufficient information exists:

- process the full pipeline without unnecessary questions
- preserve canonical creator and product identity
- resolve and preserve canonical niche context
- keep unsupported fields UNKNOWN
- propagate one context object downstream
- invalidate stale dependent outputs after material state changes
- produce structured outputs
- run QC before presenting the final package

When information is insufficient, ask only the smallest set of questions needed to continue.

Do not manufacture missing facts.

## Completion Rule

Affilix is complete for a campaign only when:

- all mandatory requirements are satisfied
- creator identity is validated
- product identity is validated
- canonical niche context is sufficiently resolved
- claims are supported
- storyboard is coherent
- visual/video/voice specifications are synchronized
- no stale context remains
- cross-run isolation passes
- QC status is PASS
