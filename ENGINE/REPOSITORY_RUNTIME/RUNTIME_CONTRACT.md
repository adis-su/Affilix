# Affilix Runtime Contract

## Purpose

This contract defines the state boundary between the ChatGPT Project interface and the canonical Affilix production runtime.

## Runtime Architecture

```text
ChatGPT Project
    ↓
Affilix Skill
    ├── Repository Runtime
    ├── Campaign State
    ├── Stage Manager
    ├── /next Progression / Revision Manager
    └── Production Artifacts
```

## Run Initialization

Every new production run must:
1. resolve `adis-su/Affilix`,
2. resolve `main`,
3. read the current branch head,
4. record `repository.commit_sha`,
5. pin that commit for the run,
6. load repository rules from the pinned commit,
7. create isolated campaign state,
8. start Stage 01 and wait for `/next` after each completed stage.

## Runtime State Contract

```yaml
run:
  id:
  entry_command:
  status:
  current_stage:
  created_at:

repository:
  repository: adis-su/Affilix
  ref: main
  commit_sha:
  loaded_at:
  access_status:

campaign:
  platform:
  format:
  requested_duration:
  creative_duration:
  aspect_ratio:
  objective:
  audience:
  creator:
  cta:
  key_message:
  talking_points:
  references:
  restrictions:

product:
  identity:
  facts:
  selling_points:
  claims:
  evidence:
  unknowns:

niche_context:
  status:
  niche:
  sub_niche:
  product_type:
  use_case:
  style:
  audience_context:
  confidence:
  evidence:
  unresolved_fields:
  conflict_flags:

stages:
  brief_product: { status:, output: }
  campaign_intake: { status:, output: }
  niche_context: { status:, output: }
  creator: { status:, output: }
  content_strategy: { status:, output: }
  hook: { status:, output: }
  storyboard: { status:, output: }
  visual_prompt: { status:, output: }
  video_prompt: { status:, output: }
  voice_script: { status:, output: }
  production_output: { status:, output: }

artifacts:
  - id:
    type:
    stage:
    status:
    source_commit_sha:
    source_inputs:
```

## Stage Orchestration

Stages 01 through 07 execute in sequence, including the explicit Campaign Intake stage after Brief & Product. After each stage is validated and completed, wait for `/next`.

After Storyboard, downstream stages execute according to deliverable requirements:
- Visual Prompt when visual output is required.
- Video Prompt when video output is required.
- Voice Script when spoken content is required.

These are dependency-driven stages, not approval branches.

## Canonical Stage Prerequisites

- Campaign Intake: Brief & Product COMPLETED.
- Niche Context: Brief & Product + Campaign Intake COMPLETED.
- Creator: Niche Context + Campaign Intake COMPLETED.
- Content Strategy: Brief & Product + Campaign Intake + Niche Context + Creator COMPLETED.
- Visual Prompt: Storyboard COMPLETED.
- Video Prompt: Storyboard COMPLETED + current Visual Prompt COMPLETED when visual continuity is required + provider capability profile when video is required.
- Voice Script: Storyboard COMPLETED.
- Production Output: all required downstream specifications current and non-STALE.

There is no QC prerequisite and no Final UGC Package prerequisite.

## Stage State

Each stage uses:
- `NOT_STARTED`
- `DRAFT`
- `REVIEW`
- `REVISION`
- `STALE`
- `SKIPPED`
- `COMPLETED`

## Progression Contract

`/next` advances the active run after the current stage completes validation. It does not represent approval or endorsement.

## Dependency and Stale-State Rules

When a completed upstream canonical input changes:
1. identify affected dependents,
2. mark them STALE,
3. preserve unaffected branches,
4. regenerate the smallest affected dependency chain,
5. wait for `/next` before continuing the affected chain.

Examples:
- Creator revision → Strategy, Hook, Storyboard, Visual, Video, Voice become STALE.
- Product or niche revision → all dependent creative stages become STALE.
- Campaign requirement revision → Niche Context, Creator, Strategy, Hook, Storyboard, Visual, Video, and Voice become STALE as applicable.
- Strategy revision → Hook, Storyboard, Visual, Video, Voice become STALE.
- Hook revision → affected Storyboard and downstream assets become STALE.
- Storyboard revision → Visual, Video, Voice become STALE.
- Visual-only revision → Video becomes STALE only when motion/state continuity is affected.
- Voice-only revision → Voice becomes REVISION/REVIEW; other branches remain current.
- Provider capability change → Video becomes STALE/re-evaluated without changing creative duration.
- Requested duration change → Storyboard and all duration-sensitive downstream assets become STALE.

A stale artifact must never be presented as current.

## Evidence and Unknowns

Use EXPLICIT, REFERENCE, SUPPORTED, INFERRED, and UNKNOWN. Only EXPLICIT, REFERENCE, and SUPPORTED information may become authoritative requirements. UNKNOWN remains UNKNOWN until supported.

## Interface Rules

ChatGPT Project presents runtime outputs, accepts `/next` and revision instructions, and never maintains competing workflow logic.

## Runtime Traceability

Every material artifact should record:
- run ID,
- stage,
- source repository commit SHA,
- relevant upstream artifact IDs,
- relevant creator/product/niche sources,
- generation status.

## Completion

A run is complete when:
- one repository commit is pinned,
- all required stages are current and COMPLETED or SKIPPED,
- no required artifact is STALE,
- requested duration is preserved exactly,
- applicable video segmentation is provider-compatible,
- the final Production Output is generated.

No separate QC or Final UGC Package stage exists.
