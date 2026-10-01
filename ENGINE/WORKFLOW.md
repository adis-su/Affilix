# Affilix — End-to-End Production Workflow

## Purpose

This document connects all Affilix engines into one production workflow.

The runtime should behave as one coherent system rather than exposing independent prompt modules.

## Pipeline

USER BRIEF → 01 BRIEF ANALYZER → NICHE CONTEXT LOADER → 02 CREATOR SELECTOR → 03 CONTENT STRATEGY → 04 HOOK ENGINE → 05 STORYBOARD ENGINE

After the storyboard:
- 06 VISUAL PROMPT ENGINE
- 07 VIDEO PROMPT ENGINE
- 08 VOICE SCRIPT ENGINE

All three downstream specifications feed into 09 QUALITY CONTROL.

## Phase 1 — Intake

Accept the user's brief and extract product, creator, campaign objective, audience, platform, format, duration, aspect ratio, key message, talking points, CTA, references, restrictions, and brand requirements.

Do not invent missing requirements.

## Phase 2 — Brief Analysis

Run 01_BRIEF_ANALYZER.

Classify information as EXPLICIT, REFERENCE, SUPPORTED, INFERRED, or UNKNOWN.

Only EXPLICIT, REFERENCE, and SUPPORTED information can become authoritative production requirements.

If a missing item materially affects production, request the minimum required information.

## Phase 2B — Niche Context Loading

Run NICHE_CONTEXT_LOADER.

Resolve:
- niche
- product type
- niche status
- product-type status
- applicable universal rules
- applicable niche rules
- applicable product-type rules

Use explicit brief data, approved Product Library data, and supplied references.

Do not infer unsupported product characteristics merely to force a niche classification.

If the niche is PLANNED, do not pretend detailed rules exist.

The resolved niche context is passed to strategy, hook, storyboard, visual, video, voice, and QC as contextual input.

## Phase 3 — Creator Selection

Run 02_CREATOR_SELECTOR.

Load character_identity.md, creator_profile.md, relevant visual references, wardrobe, expressions, and poses.

If a creator is explicitly specified, preserve that selection.

Do not create a new creator when no library creator matches.

## Phase 4 — Content Strategy

Run 03_CONTENT_STRATEGY.

Define primary objective, audience, product role, content angle, core message, supporting messages, proof strategy, emotional strategy, story arc, and CTA strategy.

Use niche/product-type patterns as optional creative context, never as unsupported product facts.

One primary message should dominate the creative direction.

## Phase 5 — Hook

Run 04_HOOK_ENGINE.

Generate viable hook candidates based on the approved strategy and loaded niche context.

Select or request approval for a hook when the campaign workflow requires explicit user selection.

Never invent unsupported claims merely to make a hook stronger.

## Phase 6 — Storyboard

Run 05_STORYBOARD_ENGINE.

Create the canonical scene sequence. Every scene must have purpose, timing, action, creator state, product state, camera, environment, dialogue intent, and continuity requirements.

Apply relevant niche/product-type interaction and visual rules.

Scene durations must fit the requested total duration.

## Phase 7 — Parallel Production Specifications

Once the storyboard is approved, run 06_VISUAL_PROMPT_ENGINE, 07_VIDEO_PROMPT_ENGINE, and 08_VOICE_SCRIPT_ENGINE.

These outputs are parallel downstream specifications, but all remain subordinate to the storyboard and resolved niche context.

## Phase 8 — Quality Control

Run 09_QUALITY_CONTROL.

Validate brief compliance, niche/product-type context, creator identity, product identity, claims, strategy, hook, storyboard continuity, visual prompts, video prompts, voice script, CTA, and production feasibility.

## Phase 9 — Revision Loop

If QC status is PASS, proceed to final packaging.

If QC status is REVISION REQUIRED: identify the affected asset, identify its source of truth, correct only the affected component, re-run dependent downstream checks, then run QC again.

If QC status is BLOCKED: stop production, identify the blocking requirement, ask only for the minimum missing information, then resume from the affected stage.

If niche or product type changes, reload NICHE_CONTEXT_LOADER and re-run all dependent downstream stages.

## Source-of-Truth Hierarchy

1. Latest explicit user instruction
2. Campaign requirements
3. Approved Product Library data
4. Approved Creator Library data
5. Platform requirements
6. Approved strategy
7. Creative interpretation

Niche rules are contextual rules. They cannot override a higher source-of-truth item.

Downstream prompts cannot silently override upstream canonical information.

## Dependency Rules

Creator identity change: re-run Creator Selector, and re-run downstream strategy, hook, storyboard, visual, video, voice, and QC as applicable.

Product identity change: revalidate Product Library, reload niche context, and re-run affected strategy, hook, storyboard, visual, video, voice, and QC.

Niche change: re-run Niche Context Loader, then Strategy, Hook, Storyboard, Visual, Video, Voice, and QC as applicable.

Product type change: re-run Niche Context Loader, then all downstream stages that depend on product-type behavior.

Strategy change: re-run Hook, Storyboard, Visual, Video, Voice, and QC.

Hook change: re-run affected opening storyboard scenes and their downstream visual, video, voice, and QC.

Storyboard change: re-run affected Visual, Video, Voice, and QC.

Visual-only change: re-run Visual, Video when motion or state changes, and QC.

Voice-only change: re-run Voice and QC.

## Final UGC Package

A production-ready package should contain:

1. Creative Brief: objective, audience, platform, format, duration, aspect ratio, product, creator, angle, core message.
2. Creator: identity, relevant wardrobe, expression, pose, reference assets.
3. Product: identity, niche, product type, supported features, benefits, evidence, approved selling points, claim boundaries.
4. Content Strategy: angle, story arc, proof strategy, CTA strategy.
5. Hook: hook concept, spoken hook, visual hook, delivery direction.
6. Storyboard: complete scene-by-scene production plan.
7. Visual Prompts: one production-ready prompt per required visual scene.
8. Video Prompts: one motion specification per required video scene.
9. Voice Script: scene-by-scene dialogue and delivery instructions.
10. QC Report: status, issues, corrections, revalidation result.

## Runtime Behavior

When sufficient information exists, process the full pipeline without unnecessary questions, preserve canonical creator and product identity, resolve niche context, keep unsupported fields unknown, produce structured outputs, and run QC before presenting the final package.

When information is insufficient, ask only the smallest set of questions needed to continue. Do not manufacture missing facts.

## Completion Rule

Affilix is considered complete for a campaign only when all mandatory requirements are satisfied, creator identity is validated, product identity is validated, niche/product-type context is resolved sufficiently, claims are supported, storyboard is coherent, visual/video/voice specifications are synchronized, and QC status is PASS.
