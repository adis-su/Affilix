# Affilix Regression — Canonical Stage vs Engine Directory Numbering

## Purpose

Prevent workflow regressions caused by treating engine directory prefixes as canonical stage IDs.

## Canonical Mapping

| Stage | Canonical Name | Implementation |
|---|---|---|
| 01 | Brief & Product | `ENGINE/01_BRIEF_ANALYZER/` |
| 02 | Niche & Context | `ENGINE/NICHE_CONTEXT_LOADER/` |
| 03 | Creator | `ENGINE/02_CREATOR_SELECTOR/` |
| 04 | Content Strategy | `ENGINE/03_CONTENT_STRATEGY/` |
| 05 | Hook | `ENGINE/04_HOOK_ENGINE/` |
| 06 | Storyboard | `ENGINE/05_STORYBOARD_ENGINE/` |
| 07 | Visual Prompt | `ENGINE/06_VISUAL_PROMPT_ENGINE/` |
| 08 | Voice Script | `ENGINE/08_VOICE_SCRIPT_ENGINE/` |
| 09 | Video Prompt | `ENGINE/07_VIDEO_PROMPT_ENGINE/` |
| 10 | Production Output | `ENGINE/UGC_PRODUCTION_OUTPUT_TEMPLATE.md` |

## Regression Case

### Input

A runtime resolver encounters `ENGINE/08_VOICE_SCRIPT_ENGINE/` and `ENGINE/07_VIDEO_PROMPT_ENGINE/`.

### Required Behavior

1. Resolve Voice Script as canonical Stage 08.
2. Resolve Video Prompt as canonical Stage 09.
3. Require Video Prompt to consume current Voice Script when spoken content exists.
4. Never infer Stage 08 from the `08_` directory prefix.
5. Never infer Stage 09 from the `07_` directory prefix.
6. Never emit a dependency where Voice Script is Stage 09 or Video Prompt is Stage 08.
7. If an artifact declares a stage inconsistent with `ENGINE/WORKFLOW.md`, reject the artifact and do not guess.
8. `/next` progression follows canonical Stage IDs, never directory numbers.

## Failure This Test Prevents

A resolver treating engine-directory numbering as workflow numbering can produce a false dependency error where Voice Script is reported as belonging to Stage 09. That behavior is invalid.

## Pass Criteria

The repository contains one authoritative stage registry in `ENGINE/WORKFLOW.md`, every engine runtime contract declares its canonical stage identity, and runtime resolution is explicitly forbidden from deriving workflow order from directory prefixes.

## Maintenance Rule

If an engine is renamed or its directory number changes, update only the implementation-path mapping. Canonical Stage IDs remain stable unless `ENGINE/WORKFLOW.md` is intentionally changed as a workflow migration.

Do not duplicate the stage registry in a way that can become independently authoritative.
