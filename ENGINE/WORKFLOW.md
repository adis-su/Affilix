# Affilix — End-to-End Production Workflow v1

## Purpose

This document is the canonical execution contract for the Affilix production runtime.

The runtime should behave as one coherent system rather than exposing independent prompt modules.

## Entry Point

The user-facing entry command is /Affilix.

 /Affilix starts a continuous production run. Affilix automatically advances through dependency-satisfied stages without requiring user approval.

The stage-gating contract is defined in ENGINE/STAGE_GATED_WORKFLOW.md. The entry contract is defined in ENGINE/AFFILIX_ENTRY_POINT/README.md.

The initial product intake requests only Nama Produk and Link Produk. After product intake, request only the minimum additional campaign information needed to continue.

## Pipeline

USER BRIEF
→ STAGE 01 BRIEF & PRODUCT
→ STAGE 02 NICHE & CONTEXT
→ STAGE 03 CREATOR
→ STAGE 04 CONTENT STRATEGY
→ STAGE 05 HOOK
→ STAGE 06 STORYBOARD
→ STAGE 07 VISUAL PROMPT
→ STAGE 08 VIDEO PROMPT when required
→ STAGE 09 VOICE SCRIPT when required
→ STAGE 10 QUALITY CONTROL
→ STAGE 11 FINAL UGC PACKAGE

Engines execute internally within their corresponding stage. Automatically run the next dependency-satisfied stage; do not require user approval between stages.

## Phase 1 — Intake

Accept the user's brief and extract product, creator, campaign objective, audience, platform, format, requested final duration, aspect ratio, key message, talking points, CTA, references, restrictions, and brand requirements.

Do not invent missing requirements.

The requested final duration is a campaign requirement. It is distinct from the technical duration of an individual video-generation request.

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

Use the configured deterministic hook-selection behavior when multiple candidates exist. Do not block the pipeline for approval.

Never invent unsupported claims merely to make a hook stronger.

## Phase 6 — Storyboard

Run 05_STORYBOARD_ENGINE.

Create the canonical scene sequence.

Every scene must have purpose, creative timing, action, creator state, product state, camera, environment, dialogue intent, context requirements, and continuity requirements.

Apply relevant niche, sub-niche, use-case, style, audience, and product-type rules.

Creative scene durations must add up to the requested final duration.

Provider limitations must not silently change the requested final duration. If technical segmentation is needed, the storyboard should preserve natural creative beat boundaries that can later map to provider-supported generation segments.

The storyboard becomes the canonical temporal source for Visual, Video, and Voice. These downstream specifications may execute independently as soon as their branch-specific prerequisites are satisfied.

## Phase 7 — Parallel Production Specifications

Once the storyboard is validated, run:

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

Video Prompt additionally uses the active provider capability profile to translate approved creative timing into technical generation segments. Provider duration constraints may change segmentation, not the approved campaign duration.

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
- requested vs creative vs final duration
- provider generation-duration compatibility
- segment duration arithmetic
- segment continuity
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

Requested final duration change:
- re-run Storyboard timing and affected Visual, Video, Voice, and QC outputs
- invalidate existing generation segment plans

Provider capability change:
- re-evaluate Video Prompt generation segmentation and Video QC
- do not automatically change approved storyboard or campaign duration
- Voice Script remains current unless creative timing changes

Visual-only change:
- re-run Visual, Video when motion or state changes, and QC

Voice-only change:
- re-run Voice and QC

Video-only segment plan change:
- re-run Video and QC
- do not mark Voice STALE unless creative timing or storyboard meaning changes

## Runtime State Rules

Each run must maintain:

- current normalized brief
- requested final duration
- current creative duration
- current final duration when assembled
- active provider capability profile when video generation is required
- current generation segment plan
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

1. Creative Brief: objective, audience, platform, format, requested duration, creative duration, final duration, aspect ratio, product, creator, angle, core message.
2. Creator: identity, relevant wardrobe, expression, pose, reference assets.
3. Product: identity, niche, product type, supported features, benefits, evidence, approved selling points, claim boundaries.
4. Niche Context: niche, sub-niche, product type, use case, style/aesthetic, audience context, confidence, evidence, unresolved fields.
5. Content Strategy: angle, story arc, proof strategy, CTA strategy.
6. Hook: hook concept, spoken hook, visual hook, delivery direction.
7. Storyboard: complete scene-by-scene production plan with creative timing.
8. Visual Prompts: one production-ready prompt per required visual scene.
9. Video Prompts: motion specifications and provider-compatible generation segment mapping.
10. Voice Script: scene-by-scene dialogue and delivery instructions.
11. QC Report: status, issues, corrections, duration validation, and revalidation result.

## Runtime Behavior

When sufficient information exists:

- process the full pipeline without unnecessary questions
- preserve canonical creator and product identity
- resolve and preserve canonical niche context
- keep unsupported fields UNKNOWN
- propagate one context object downstream
- preserve requested final duration
- adapt technical video segmentation to provider capabilities
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
- requested, creative, and final durations match unless an explicit approved exception exists
- all video generation segments are provider-compatible when video generation is required
- no stale context remains
- cross-run isolation passes
- QC status is PASS

## Repository Runtime Contract

Repository loading is governed by ENGINE/REPOSITORY_RUNTIME/README.md.

At runtime, load the current repository specification relevant to each stage. Use progressive loading rather than reading the entire repository. Repository state and production-run state are separate.

If a material repository rule changes, affected downstream assets become STALE and must be regenerated according to the dependency rules below. Never invent missing repository rules or claim that a repository file was consulted when it was not accessible.

## Stage-Gated Execution

The canonical continuous-production contract is ENGINE/STAGE_GATED_WORKFLOW.md.

For every required stage, execute: INPUT → PROCESS → OUTPUT → VALIDATE → NEXT STAGE.

Automatically continue when dependencies are satisfied. Stop only for a material blocker, explicit revision, safety/compliance issue, or missing required information. /next is compatibility-only and is not required for progression.

If the user requests a revision, revise the smallest affected component and keep unrelated approved stages intact. When an upstream approved stage changes, mark all dependent downstream assets STALE and regenerate them only after the revised upstream stage is approved.

A stale asset must never be presented as current or included in a production-ready package.
