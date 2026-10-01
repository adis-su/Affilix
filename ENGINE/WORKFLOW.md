# Affilix — End-to-End Production Workflow v2

## Purpose

This document is the canonical execution contract for the Affilix production runtime.

The runtime behaves as one coherent system rather than exposing independent prompt modules.

## Entry Point

The user-facing entry command is `/Affilix`.

`/Affilix` starts a stage-by-stage production run. Affilix completes and validates one stage at a time, then waits for `/next` before advancing to the next dependency-satisfied stage.

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
→ STAGE 10 PRODUCTION OUTPUT

After each stage is validated and completed, wait for `/next`. `/next` is not an approval action.

## Intake

Accept the user's brief and extract product, creator, campaign objective, audience, platform, format, requested final duration, aspect ratio, key message, talking points, CTA, references, restrictions, and brand requirements.

Do not invent missing requirements.

## Brief and Context

Run Brief Analyzer, then Niche Context Loader. Classify information as EXPLICIT, REFERENCE, SUPPORTED, INFERRED, or UNKNOWN.

Create exactly one canonical runtime context. Missing values remain UNKNOWN. Context labels cannot override explicit product facts or creator identity.

## Creator and Product

Run Creator Selector and load the applicable Creator Library records. Load Product Library identity, selling points, claims rules, niche context, and product-type rules.

Preserve creator and product identity across all downstream assets. Never invent unsupported facts, performance, reviews, testimonials, discounts, scarcity, guarantees, certifications, or personal experience.

## Strategy and Hook

Run Content Strategy before scenes or prompts. Define objective, audience, product role, angle, core message, story arc, proof strategy, and CTA strategy.

Generate hooks from the validated strategy and canonical context. Do not invent unsupported claims or urgency.

## Storyboard

Run Storyboard Engine and create the canonical scene sequence. Scene durations must add up to the requested creative duration.

Provider limitations must not silently change campaign duration. Technical generation segmentation belongs to Video Prompt and remains subordinate to storyboard timing.

## Downstream Production Specifications

After Storyboard is completed and the user sends `/next`, run the applicable downstream engines:

- Visual Prompt
- Video Prompt when video output is required
- Voice Script when spoken content is required

These outputs remain subordinate to the Storyboard and all upstream source-of-truth rules.

## Production Output

After all required downstream production specifications are complete, the user sends `/next` and Affilix generates the final Production Output.

The Production Output is a direct assembly of current runtime state. It is not a separate QC report or Final UGC Package.

## Revision and Invalidation

When an upstream source changes:

1. identify the changed source
2. mark dependent downstream assets STALE
3. rerun affected engines
4. validate the revised assets
5. wait for `/next` before continuing

Dependency examples:

- Creator change → Strategy, Hook, Storyboard, Visual, Video, Voice
- Product change → Niche Context, Strategy, Hook, Storyboard, Visual, Video, Voice
- Niche/Product Type change → Strategy, Hook, Storyboard, Visual, Video, Voice
- Strategy change → Hook, Storyboard, Visual, Video, Voice
- Hook change → affected Storyboard and downstream production specs
- Storyboard change → Visual, Video, Voice
- Duration change → Storyboard and duration-sensitive downstream specs
- Visual change → Video when motion/state is affected
- Voice change → Voice only unless creative timing changes
- Video segment-plan change → Video only unless creative timing changes

## Runtime State

Each run maintains:

- current normalized brief
- requested final duration
- current creative duration
- active provider capability profile when video generation is required
- current generation segment plan
- current canonical creator
- current canonical product
- current canonical niche context
- current strategy
- current hook
- current storyboard
- current downstream production specifications
- current production output

State is isolated per run.

## Source-of-Truth Hierarchy

1. Latest explicit user instruction
2. Campaign requirements
3. Product Library data
4. Creator Library data
5. Canonical Niche Context
6. Platform requirements
7. Strategy
8. Creative interpretation

Downstream prompts cannot silently override upstream canonical information.

## Completion Rule

Affilix is complete when:

- mandatory requirements are satisfied
- creator identity is current
- product identity is current
- canonical niche context is sufficiently resolved
- claims are supported
- storyboard is coherent
- applicable visual/video/voice specifications are synchronized
- requested creative duration is preserved
- provider generation segments are compatible when video generation is required
- no stale context or downstream asset remains
- final Production Output is generated

There is no QC stage and no Final UGC Package stage.

## Repository Runtime

Repository loading is governed by ENGINE/REPOSITORY_RUNTIME/README.md. At runtime, load the current repository specification relevant to each stage using progressive loading.

If a material repository rule changes, affected downstream assets become STALE and must be regenerated according to the dependency rules.
