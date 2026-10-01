# Affilix — Continuous Production Contract v3

## Purpose

Affilix runs as a stage-by-stage production workflow. Each stage is processed and validated, then the run pauses at the completed stage. The user advances with `/next`. `/next` is a progression command, not an approval action.

Each stage follows:

**INPUT → PROCESS → OUTPUT → VALIDATE → WAIT FOR `/next` → NEXT STAGE**

## Canonical Stages

1. Brief & Product
2. Niche & Context
3. Creator
4. Content Strategy
5. Hook
6. Storyboard
7. Visual Prompt
8. Video Prompt
9. Voice Script
10. Production Output

A stage may be skipped only when its output is genuinely not required for the requested deliverable.

## Stage State

Each stage has one of:
- `NOT_STARTED`
- `DRAFT`
- `REVIEW`
- `REVISION`
- `STALE`
- `SKIPPED`
- `COMPLETED`

## `/next` Progression Contract

After producing a stage output:
1. persist the artifact
2. validate the stage and prerequisites
3. mark the stage `COMPLETED` when validation passes
4. present the completed stage output
5. wait for `/next`
6. on `/next`, execute the next dependency-satisfied stage

`/next` does not mean approve, accept, or endorse the output.

If the user requests a revision, revise the affected stage. After the revision is validated, wait for `/next` again.

STALE prevents stale artifacts from being consumed downstream.

## Runtime State Shape

```yaml
run:
  status: ACTIVE
  current_stage: BRIEF_PRODUCT

campaign:
  requested_duration:
  creative_duration:
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
  production_output:
    status: NOT_STARTED
```

## Stage Contracts

### 01 — Brief & Product
Input: product name, product link/reference, campaign information available in the current run.
Output: normalized brief and canonical product facts.

### 02 — Niche & Context
Input: validated Brief & Product.
Output: one canonical niche context.

### 03 — Creator
Input: validated context plus creator requirements.
Output: selected creator identity and relevant creator references.

### 04 — Content Strategy
Input: validated Brief, Context, Creator.
Output: objective, audience, angle, core message, story arc, proof strategy, CTA strategy.

### 05 — Hook
Input: validated Strategy.
Output: validated hook direction/copy and delivery direction.

### 06 — Storyboard
Input: validated Hook and all upstream completed state.
Output: canonical scene sequence, creative timing, and duration/segment planning intent.

The storyboard is the source of truth for the requested creative duration. Provider limits are technical constraints and must not silently redefine campaign duration.

### 07 — Visual Prompt
Input: validated Storyboard and upstream completed state.
Output: one production-ready image prompt per required visual scene.

### 08 — Video Prompt
Input: validated Storyboard, completed Visual Prompt where relevant, and provider capability profile when video generation is required.
Output: motion specification plus provider-compatible generation segment mapping.

### 09 — Voice Script
Input: validated Storyboard and declared dependencies.
Output: scene-by-scene dialogue and delivery instructions.

### 10 — Production Output
Input: all required current upstream production assets.
Output: consolidated production output containing the current campaign brief, creator, product, niche context, strategy, hook, storyboard, and applicable visual/video/voice specifications.

This stage does not perform a separate approval or readiness gate. It is the final output assembly step.

## Revision Contract

A revision must identify the smallest affected component.

Examples:
- Hook wording change → revise Hook and affected opening storyboard dependencies.
- Storyboard Scene 3 change → revise Scene 3 and dependent Visual/Video/Voice assets.
- Visual composition change → revise Visual Prompt and dependent Video Prompt when motion/state is affected.
- Requested duration change → revise Storyboard timing and all duration-sensitive downstream assets.
- Provider capability change → re-evaluate Video Prompt segmentation without silently changing campaign duration.

Do not rebuild unrelated completed stages.

## Completion

The run is complete when all required stages are current and validated, with `COMPLETED` or `SKIPPED` used as internal lifecycle states, and the final Production Output is generated.

There is no QC stage and no Final UGC Package stage.


## Action-Choreography Stage Contract

Stage 06 Storyboard now produces three canonical layers: action choreography, reference graph, and creative timing.

Stage 07 renders reference states. Stage 08 converts reference-to-reference transitions into provider-compatible generation segments.

A stage is processed, validated, marked `COMPLETED`, then paused for `/next`. No approval gate is implied.
