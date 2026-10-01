# Affilix — Continuous Production Contract v2

## Purpose

Affilix runs as a **stage-by-stage production workflow**. Each stage is processed and validated, then the run pauses at the completed stage. The user advances with `/next`. `/next` is a progression command, not an approval action.

Each stage follows:

**INPUT → PROCESS → OUTPUT → VALIDATE → WAIT FOR `/next` → NEXT STAGE**

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
- `REVISION`
- `STALE`
- `SKIPPED`
- `COMPLETED`

QC additionally uses its existing validation statuses: `PASS`, `REVISION REQUIRED`, and `BLOCKED`.

## `/next` Progression Contract

After producing a stage output:
1. Persist the artifact.
2. Validate the stage and its prerequisites.
3. Mark the stage `COMPLETED` when validation passes.
4. Present the completed stage output.
5. Wait for the user to send `/next`.
6. On `/next`, execute the next dependency-satisfied stage.

`/next` is the only progression command needed between completed stages. It does not mean approve, accept, or endorse the output.

`REVISION` returns to the affected stage. After the revision is validated, wait for `/next` again.

STALE prevents stale artifacts from being consumed downstream.

SKIPPED is explicit when a deliverable does not require a stage.

QC PASS remains the final validation requirement before production packaging.

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

Example: `Storyboard v1 COMPLETED` → user requests a Storyboard revision → `Storyboard v2 REVISION` → prior Visual/Video/Voice outputs become `STALE` → after Storyboard v2 is validated, wait for `/next` before continuing.

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
    status: COMPLETED
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
Output: validated hook direction/copy and delivery direction.
Progression: automatic after validation.

### 06 — Storyboard
Input: validated Hook and all upstream completed state.
Output: canonical scene sequence, creative timing, and duration/segment planning intent.
Progression: automatic after validation.

The storyboard is the source of truth for the completed creative duration. It must preserve the requested final duration unless the user explicitly approves a change.

Provider generation limits are technical constraints and must not silently redefine the storyboard duration.

### 07 — Visual Prompt
Input: validated Storyboard and all upstream completed state.
Output: one production-ready image prompt per required visual scene.
Progression: automatic after validation.

### 08 — Video Prompt
Input: validated Storyboard, completed Visual Prompt where relevant, and active provider capability profile when video generation is required.
Output: motion specification plus provider-compatible generation segment mapping.

If the completed final duration exceeds a provider's single-generation limit, create multiple generation segments. Each segment must use a supported provider duration, and the segment durations must sum to the completed final duration.

Progression: automatic after validation.

### 09 — Voice Script
Input: validated Storyboard. Additional visual/video completion is required only when the active voice contract explicitly declares those dependencies.
Output: scene-by-scene dialogue and delivery instructions.

Voice timing follows the creative/storyboard timeline. Technical video segment boundaries must not redefine spoken wording or timing.

Progression: automatic after validation.

### 10 — Quality Control
Input: all required completed production assets.
Output: QC status and corrections.

QC must validate requested duration, creative duration, final assembled duration, provider compatibility, segment arithmetic, and continuity.

Gate: `PASS` permits Final UGC Package. `REVISION REQUIRED` routes to the smallest affected stage. `BLOCKED` requests the minimum missing information.

### 11 — Final UGC Package
Input: QC `PASS` and no stale required assets.
Output: final production package and production output.

The package must preserve the requested duration and record any technical generation segmentation.

## UX Rules

Do not dump the entire pipeline after `/Affilix`.

At each stage:
- clearly show the current stage
- show the useful output
- state that it is ready for review
- automatically continue when dependencies are satisfied
- keep technical runtime state hidden unless requested

The user should feel like they are progressing through a production, not operating a software build system.

## Dependency Rules

The existing dependency rules in `ENGINE/WORKFLOW.md` remain authoritative. This contract adds `/next` progression on top of those dependencies.

A stage cannot be considered production-current merely because its upstream data exists. Its own validation must also be current.

## Completion

The run is complete only when:
- all required stages are current and validated, with COMPLETED or SKIPPED used as internal lifecycle states
- QC is `PASS`
- no required downstream asset is `STALE`
- requested, creative, and final duration are aligned unless an explicit user-requested exception exists
- provider generation segments are compatible when video generation is required
- Final UGC Package is complete
- delivery readiness is `READY`
