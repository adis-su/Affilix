# Affilix Runtime Contract

## Purpose

This contract defines the state boundary between Affilix interfaces (ChatGPT Project) and the canonical Affilix production runtime.

Interfaces are adapters. They must not become independent sources of workflow logic, production state, or repository rules.

## Runtime Architecture

```
Client Interface
    ↓
Affilix Runtime
    ├── Repository Runtime
    ├── Campaign State
    ├── Stage Manager
    ├── `/next` Progression / Revision Manager
    └── Production Artifacts
```

This runtime contract is designed for the ChatGPT Project Affilix Skill.

## Run Initialization

Every new production run must:

1. Resolve canonical repository `adis-su/Affilix`.
2. Resolve canonical branch `main`.
3. Read the current branch head.
4. Record the resolved commit SHA as `repository.commit_sha`.
5. Pin that commit for the lifetime of the production run.
6. Load repository rules from the pinned commit.
7. Create isolated campaign state.
8. Start Stage 01 and wait for `/next` after each completed stage.

A new run uses the latest available `main` commit at initialization.

## Runtime State Contract

The runtime state must distinguish the user-facing current stage from readiness of independent downstream branches.

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
  final_duration:
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
  niche_context: { status:, output: }
  creator: { status:, output: }
  content_strategy: { status:, output: }
  hook: { status:, output: }
  storyboard: { status:, output: }
  visual_prompt: { status:, output: }
  video_prompt: { status:, output: }
  voice_script: { status:, output: }
  quality_control: { status:, output: }
  final_package: { status:, output: }

decision_queue:
  - id:
    field:
    reason:
    blocking_stage:
    status:

artifacts:
  - id:
    type:
    stage:
    status:
    source_commit_sha:
    source_inputs:
```

## Stage Orchestration

`current_stage` is a user-facing pointer, not a database lock.

Stages 01 through 06 execute in sequence. After each stage is validated and completed, the run waits for `/next` before starting the next stage.

After Storyboard is completed and the user sends `/next`, the runtime may activate the independent downstream branches concurrently:

- `visual_prompt`
- `video_prompt`, when video generation is required
- `voice_script`, when voice is required

Each branch has its own stage status. Completion of one branch must not prevent another active branch from executing.

The runtime must never use a single `current_stage` value as the prerequisite for all three branches. Branch prerequisites are evaluated from the relevant stage statuses and artifact freshness.

Canonical branch prerequisites:

- Visual Prompt: Storyboard COMPLETED.
- Video Prompt: Storyboard COMPLETED + current Visual Prompt COMPLETED when visual continuity is required + provider capability profile when video is required.
- Voice Script: Storyboard COMPLETED. Additional visual/video completion is required only when the voice contract explicitly declares a dependency.
- Quality Control: all required branches COMPLETED or explicitly SKIPPED.
- Final Package: QC PASS + all required assets current and non-STALE.

If a required branch is skipped, the skip must be explicit and recorded in runtime state.

## Stage State

Each stage has one of:

- `NOT_STARTED`
- `DRAFT`
- `REVIEW`
- `REVISION`
- `STALE`
- `SKIPPED`
- `COMPLETED`

QC additionally uses `PASS`, `REVISION REQUIRED`, and `BLOCKED`.

A stage output is current only when its own status, upstream dependencies, and repository commit are current.

## Progression Contract

The runtime does not require or track user approval between stages. `/next` only advances the active run after the current stage has completed validation. Revision instructions are handled separately and invalidate affected downstream assets.

## Dependency and Stale-State Rules

When a completed upstream canonical input changes:

1. identify affected dependents,
2. mark them STALE,
3. preserve unaffected branches,
4. regenerate the smallest affected dependency chain,
5. wait for `/next` before continuing the affected chain.

Examples:

- Storyboard revision → Visual, Video, and Voice become STALE.
- Visual-only revision → Visual becomes REVISION/REVIEW; Video becomes STALE only if visual motion/state continuity is affected; Voice remains current.
- Voice-only revision → Voice becomes REVISION/REVIEW; other branches remain current.
- Provider capability change → Video becomes STALE/re-evaluated; completed creative duration remains unchanged.
- Requested duration change → Storyboard and all duration-sensitive downstream assets become STALE.

A stale asset must never be presented as current or included in a production-ready package.

## Evidence and Unknowns

Use:

- EXPLICIT
- REFERENCE
- SUPPORTED
- INFERRED
- UNKNOWN

Only EXPLICIT, REFERENCE, and SUPPORTED information may become authoritative campaign or product requirements. INFERRED information may guide reasoning but must not silently become authoritative. UNKNOWN remains UNKNOWN until supported.

## Decision Queue

Create a decision-queue item only when missing information materially affects a required stage.

Each item records the missing field, why it matters, first blocked stage, whether a safe default exists, and resolution status.

Interfaces should present only decisions relevant to the current interaction.

## Interface Rules

ChatGPT Project must present runtime outputs, accept `/next` progression commands and revision instructions, and never maintain competing canonical workflow logic.

## Repository Access Failure

If the canonical repository cannot be accessed, do not claim it was loaded. Preserve affected fields as UNKNOWN and continue only where higher-level rules are sufficient.

## Runtime Traceability

Every material artifact should record:

- run ID
- stage
- source repository commit SHA
- relevant upstream artifact IDs
- relevant creator/product/niche sources
- generation status

## Completion

A production run is complete only when:

- one repository commit is pinned,
- all required stages are current and completed or explicitly skipped,
- no required artifact is STALE,
- QC is PASS,
- the final package is traceable to the run and pinned repository commit.
