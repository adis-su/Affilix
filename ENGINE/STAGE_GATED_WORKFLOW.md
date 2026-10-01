# Affilix — Continuous Production Contract v2

## Purpose

Affilix runs as a **continuous production workflow**. The runtime automatically advances through dependency-satisfied stages. User approval is not a progression requirement.

Each stage follows:

**INPUT → PROCESS → OUTPUT → VALIDATE → NEXT STAGE**

The user experiences one guided production assistant. Engine names remain implementation details.

## Canonical Stages

1. **Brief & Product**
2. **Niche & Context**
3. **Creator**
4. **Content Strategy**
5. **Hook**
6. **Storyboard**
7. **Visual Prompt**
8. **Video Prompt**
9. **Voice Script**
10. **Quality Control**
11. **Final UGC Package**

A stage may be skipped only when its output is genuinely not required for the requested deliverable. Skipping must be explicit in runtime state.

## Stage State

Each stage has one of:
- `NOT_STARTED`
- `DRAFT`
- `REVIEW`
- `APPROVED`
- `REVISION`
- `STALE`
- `SKIPPED`
- `COMPLETED`

`APPROVED` is an internal completion state for dependency tracking and audit. It is not a user-facing gate.

QC additionally uses its existing validation statuses: `PASS`, `REVISION REQUIRED`, and `BLOCKED`.

## Automatic Progression Contract

After producing a stage output:
1. Persist the artifact.
2. Validate the stage and its prerequisites.
3. Automatically advance to the next dependency-satisfied stage.
4. Stop only for a material blocker, explicit revision, safety/compliance issue, or missing required information.

The user-facing command /next is not required for normal progression.

APPROVED may still be written internally when a stage has passed its required validation and is ready to satisfy downstream dependencies.

REVISION returns control to the affected stage and automatically re-runs dependent stages after correction.

STALE prevents stale artifacts from being consumed downstream.

SKIPPED is explicit when a deliverable does not require a stage.

QC PASS remains the final validation requirement before production packaging.

/next may remain as a compatibility command, but it must not be presented as an approval requirement.

## Revision Contract

A revision must identify the smallest affected component.

Examples:
- Hook wording change → revise Hook and affected opening storyboard dependencies.
- Storyboard Scene 3 change → revise Scene 3 and dependent Visual/Video/Voice assets.
- Visual composition change only → revise Visual Prompt and any dependent Video Prompt if motion/state is affected.
- Requested final duration change → revise Storyboard timing and all duration-sensitive downstream assets.
- Provider capability change → re-evaluate Video Prompt generation segmentation; do not silently alter the approved campaign duration.

Do not rebuild unrelated approved stages.

## Stale-State Contract

When an approved upstream stage changes, dependent stages become `STALE`.

Example: `Storyboard v1 APPROVED` → user changes Storyboard → `Storyboard v2 REVIEW` → prior Visual/Video/Voice outputs become `STALE` → after Storyboard approval, regenerate affected downstream stages.

A stale asset must never be presented as current or included in a production-ready package.

## Runtime State Shape

```yaml
run:
  status: ACTIVE
  current_stage: BRIEF_PRODUCT

campaign:
  requested_duration:
  creative_duration:
  final_duration:
  duration_status:

provider:
  id:
  model_id:
  supported_durations: []
  capability_status:

generation_segments: []

stages:
  brief_product:
    status: REVIEW
  niche_context:
    status: NOT_STARTED
  creator:
    status: NOT_STARTED
  strategy:
    status: NOT_STARTED
  hook:
    status: NOT_STARTED
  storyboard:
    status: NOT_STARTED
  visual_prompt:
    status: NOT_STARTED
  video_prompt:
    status: NOT_STARTED
  voice_script:
    status: NOT_STARTED
  quality_control:
    status: NOT_STARTED
  final_package:
    status: NOT_STARTED
```

The exact runtime representation may differ, but the semantics must remain equivalent.

## Stage Contracts

### 01 — Brief & Product
Input: product name, product link/reference, campaign information available in the current run.
Output: normalized brief and canonical product facts available from approved sources.
Progression: automatic after validation.

The user's requested final video duration, when supplied, is a campaign requirement and must be preserved.

### 02 — Niche & Context
Input: validated Brief & Product.
Output: one canonical niche context.
Progression: automatic after validation.

### 03 — Creator
Input: validated context plus creator requirements.
Output: selected creator identity and relevant creator references.
Progression: automatic after validation.

### 04 — Content Strategy
Input: validated Brief, Context, Creator.
Output: objective, audience, angle, core message, story arc, proof strategy, CTA strategy.
Progression: automatic after validation.

### 05 — Hook
Input: validated Strategy.
Output: approved hook direction/copy and delivery direction.
Progression: automatic after validation.

### 06 — Storyboard
Input: validated Hook and all upstream approved state.
Output: canonical scene sequence, creative timing, and duration/segment planning intent.
Progression: automatic after validation.

The storyboard is the source of truth for the approved creative duration. It must preserve the requested final duration unless the user explicitly approves a change.

Provider generation limits are technical constraints and must not silently redefine the storyboard duration.

### 07 — Visual Prompt
Input: validated Storyboard and all upstream approved state.
Output: one production-ready image prompt per required visual scene.
Progression: automatic after validation.

### 08 — Video Prompt
Input: validated Storyboard, approved Visual Prompt where relevant, and active provider capability profile when video generation is required.
Output: motion specification plus provider-compatible generation segment mapping.

If the approved final duration exceeds a provider's single-generation limit, create multiple generation segments. Each segment must use a supported provider duration, and the segment durations must sum to the approved final duration.

Progression: automatic after validation.

### 09 — Voice Script
Input: validated Storyboard. Additional visual/video approval is required only when the active voice contract explicitly declares those dependencies.
Output: scene-by-scene dialogue and delivery instructions.

Voice timing follows the creative/storyboard timeline. Technical video segment boundaries must not redefine spoken wording or timing.

Progression: automatic after validation.

### 10 — Quality Control
Input: all required approved production assets.
Output: QC status and corrections.

QC must validate requested duration, creative duration, final assembled duration, provider compatibility, segment arithmetic, and continuity.

Gate: `PASS` permits Final UGC Package. `REVISION REQUIRED` routes to the smallest affected stage. `BLOCKED` requests the minimum missing information.

### 11 — Final UGC Package
Input: QC `PASS` and no stale required assets.
Output: final production package and production output.

The package must preserve the approved requested duration and record any technical generation segmentation.

## UX Rules

Do not dump the entire pipeline after `/Affilix`.

At each stage:
- clearly show the current stage
- show the useful output
- state that it is ready for review
- automatically continue when dependencies are satisfied
- keep technical runtime state hidden unless requested

The user should feel like they are approving a production, not operating a software build system.

## Dependency Rules

The existing dependency rules in `ENGINE/WORKFLOW.md` remain authoritative. This contract adds a automatic progression on top of those dependencies.

A stage cannot be considered production-current merely because its upstream data exists. Its own approval state must also be current.

## Completion

The run is complete only when:
- all required stages are current and validated, with APPROVED or SKIPPED used as internal lifecycle states
- QC is `PASS`
- no required downstream asset is `STALE`
- requested, creative, and final duration are aligned unless an explicit approved exception exists
- provider generation segments are compatible when video generation is required
- Final UGC Package is complete
- delivery readiness is `READY`
