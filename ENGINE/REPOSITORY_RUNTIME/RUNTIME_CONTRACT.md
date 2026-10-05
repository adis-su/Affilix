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

The Project is the user-facing host. GitHub `adis-su/Affilix` on `main` is the implementation source of truth. The Project must not maintain a competing workflow contract.

## Canonical Stage Resolution

`ENGINE/WORKFLOW.md` is the sole authority for canonical stage IDs, names, order, prerequisites, and dependencies.

Runtime MUST resolve:

`canonical_stage_id → canonical_stage_name → implementation_path`

It MUST NOT resolve:

`engine_directory_number → stage_id`

Engine directory numbers are implementation identifiers only. In particular, `ENGINE/08_VOICE_SCRIPT_ENGINE/` maps to canonical Stage 09 and `ENGINE/07_VIDEO_PROMPT_ENGINE/` maps to canonical Stage 08.

Every material artifact must carry a canonical `stage` value. Runtime validation must reject an artifact when its declared stage conflicts with the canonical registry or when a dependency is inferred from an engine directory number.

## Run Initialization

Every new `/Affilix` production run must:

1. resolve `adis-su/Affilix`
2. resolve `main`
3. read the current branch HEAD
4. record `repository.commit_sha`
5. pin that commit for the run
6. load `SKILL.md`, `ENGINE/WORKFLOW.md`, the entry contract, and relevant current engine/library files
7. create isolated campaign state
8. start Stage 01

The active run must never silently mix repository files from different commits.

## Repository Freshness

```text
NEW /Affilix RUN
      ↓
CURRENT main HEAD
      ↓
PIN commit SHA
      ↓
LOAD repository contracts
      ↓
RUN against pinned snapshot
```

If `main` changes after pinning, the active run remains on its pinned snapshot. The newer repository state is adopted by the next new run.

For implementation work outside an active production run, resolve the current `main` HEAD immediately before editing or reporting repository status.

If current HEAD or a required file cannot be resolved, do not claim that the repository is current.

## Runtime State Contract

```yaml
run:
  id:
  entry_command: /Affilix
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
  audio_mode:
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
  voice_script: { status:, output: }
  video_prompt: { status:, output: }
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

Stages 01 through 06 execute sequentially. Stage 01 establishes campaign requirements, including `campaign.audio_mode`, before downstream dependency planning. After Stage 06, downstream branches execute according to deliverable requirements:

- Stage 07 Visual Prompt when visual output is required
- Stage 08 Video Prompt when video output is required
- Stage 09 Voice Script when `campaign.audio_mode` is `SPOKEN_ON_CAMERA` or `VOICE_OVER`; otherwise Stage 09 is `SKIPPED` with reason `AUDIO_MODE_NO_SPOKEN_VOICE`
- Stage 08 Production Output

After every completed stage, wait for `/next`.

These are dependency-driven stages, not approval branches.

## Canonical Stage Prerequisites

- Niche Context: Brief & Product COMPLETED.
- Creator: Niche Context + Brief & Product COMPLETED.
- Content Strategy: Brief & Product + Niche Context + Creator COMPLETED.
- Hook: Content Strategy COMPLETED.
- Storyboard: Hook + all required upstream state COMPLETED.
- Visual Prompt: Storyboard COMPLETED.
- Voice Script: Storyboard COMPLETED when Brief & Product `campaign.audio_mode` is `SPOKEN_ON_CAMERA` or `VOICE_OVER`; otherwise Stage 09 is `SKIPPED` with reason `AUDIO_MODE_NO_SPOKEN_VOICE`.
- Video Prompt: Storyboard COMPLETED + current Visual Prompt COMPLETED when visual continuity is required + current Voice Script COMPLETED only when Brief & Product `campaign.audio_mode` is `SPOKEN_ON_CAMERA` or `VOICE_OVER` + provider capability profile when video generation is required.
- Production Output: all required downstream specifications current and non-STALE.

There is no QC prerequisite, Final UGC Package prerequisite, or approval prerequisite.

## Stage State

Each stage uses:

- `NOT_STARTED`
- `DRAFT`
- `REVISION`
- `STALE`
- `SKIPPED`
- `COMPLETED`

There is no `REVIEW` state because Affilix has no approval workflow.

## Progression Contract

`/next` advances the active run after the current stage completes validation. It does not represent approval, acceptance, endorsement, or waiver of validation.

## Dependency and Stale-State Rules

When a completed upstream canonical input changes:

1. identify affected dependents
2. mark affected artifacts STALE
3. preserve unaffected branches
4. regenerate the smallest affected dependency chain
5. validate regenerated outputs
6. wait for `/next`

Examples:

- Creator revision → Strategy, Hook, Storyboard, Visual, Voice, Video become STALE.
- Product or niche revision → all dependent creative stages become STALE.
- Campaign requirement revision → affected Context, Creator, Strategy, Hook, Storyboard, Visual, Voice, Video become STALE.
- `campaign.audio_mode` revision → re-evaluate Stage 09 and Stage 08 dependency state; never leave a stale Voice Script as an implicit dependency when mode is `NO_SPOKEN_VOICE`.
- Strategy revision → Hook, Storyboard, Visual, Voice, Video become STALE.
- Hook revision → affected Storyboard and downstream assets become STALE.
- Storyboard revision → Visual, Voice, Video become STALE.
- Reference-state revision → affected Visual and Video transitions become STALE.
- Visual-only revision → Video becomes STALE only when motion/state continuity is affected.
- Voice dialogue/performance/timing revision → Video becomes STALE when synchronization is affected.
- Provider capability change → Video becomes STALE/re-evaluated without changing creative duration.
- Requested duration change → Storyboard and all duration-sensitive downstream assets become STALE.

A stale artifact must never be presented as current.

## Evidence and Unknowns

Use EXPLICIT, REFERENCE, SUPPORTED, INFERRED, and UNKNOWN.

Only EXPLICIT, REFERENCE, and SUPPORTED information may become authoritative requirements. UNKNOWN remains UNKNOWN until supported.

## Interface Rules

ChatGPT Project:

- presents the current runtime output
- accepts `/next`
- accepts revisions
- preserves run continuity
- does not maintain a competing workflow or creator/product database

## Runtime Traceability

Every material artifact should record:

- run ID
- stage
- source repository commit SHA
- relevant upstream artifact IDs
- relevant creator/product/niche sources
- generation status

## Completion

A run is complete when:

- one repository commit is pinned
- all required stages are current and COMPLETED or SKIPPED
- no required artifact is STALE
- requested duration is preserved exactly
- applicable video segmentation is provider-compatible
- creator/product identity is current
- storyboard and downstream specifications are synchronized
- final Production Output is generated

No separate QC or Final UGC Package stage exists.
