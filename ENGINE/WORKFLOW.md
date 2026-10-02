# Affilix — End-to-End Production Workflow v3

## Purpose

This is the **single canonical execution contract** for the Affilix production runtime.

Affilix runs as one continuous, dependency-aware production workflow. Engines are internal implementation components, not separate user-facing commands.

## Entry Point

The user-facing command is `/Affilix`.

A new `/Affilix` run must resolve the current `main` branch head, pin that commit for the run, load the relevant repository contracts, initialize isolated run state, and begin Stage 01.

Repository resolution, commit pinning, source loading, and diagnostics are internal. They must never appear in the canonical Stage 01 opening.

## Canonical Pipeline

```text
/Affilix
  ↓
01 BRIEF & PRODUCT
  ↓ /next
02 CAMPAIGN INTAKE
  ↓ /next
03 NICHE & CONTEXT
  ↓ /next
04 CREATOR
  ↓ /next
05 CONTENT STRATEGY
  ↓ /next
06 HOOK
  ↓ /next
07 STORYBOARD
  ↓ /next
08 VISUAL PROMPT
  ↓ /next
09 VOICE SCRIPT       [when spoken content is required]
  ↓ /next
10 VIDEO PROMPT       [when video output is required]
  ↓ /next
11 PRODUCTION OUTPUT
```

No QC stage, Final UGC Package stage, or approval gate exists.

A stage may be skipped only when its output is genuinely not required by the requested deliverable. Skipping is a dependency decision, not an approval decision.

## Stage Execution Contract

Every active stage follows:

```text
INPUT
 ↓
PROCESS
 ↓
OUTPUT
 ↓
VALIDATE
 ↓
MARK COMPLETED
 ↓
WAIT FOR /next
```

`/next` means **progress to the next dependency-satisfied stage**. It never means approve, accept, endorse, or waive validation.

After a revision:

```text
CURRENT STAGE
 ↓
APPLY REVISION
 ↓
REVALIDATE
 ↓
MARK COMPLETED
 ↓
WAIT FOR /next
```

Never advance automatically after a revision.

## Stage State

Use only:

- `NOT_STARTED`
- `DRAFT`
- `REVISION`
- `STALE`
- `SKIPPED`
- `COMPLETED`

There is no `REVIEW` state because Affilix has no approval workflow.

## Canonical Stage Contracts

### 01 — Brief & Product

Input: product name and product link/reference.

Output: normalized product brief plus researched product facts, evidence/provenance, supported claims, and genuine unknowns.

The supplied product link/reference must be actively inspected when accessible. Unsupported marketing language must not be promoted to fact.

### 02 — Campaign Intake

Input: completed Stage 01.

Output: platform, exact requested video duration, primary objective, target audience, requested creator from the current Creator Library, and CTA.

The default duration is 18 seconds. Provider generation limits are technical constraints only. Exact duration feasibility is handled by Video Prompt segmentation.

### 03 — Niche & Context

Input: completed Brief & Product and Campaign Intake.

Output: exactly one canonical niche/product context. Missing values remain `UNKNOWN`.

### 04 — Creator

Input: completed Niche & Context and Campaign Intake.

Output: resolved canonical creator identity and applicable Creator Library references.

Creator selection must come from the current pinned repository. Identity is locked downstream.

### 05 — Content Strategy

Input: completed Brief, Campaign Intake, Context, and Creator.

Output: objective, audience, product role, angle, core message, story arc, proof strategy, and CTA strategy.

### 06 — Hook

Input: completed Strategy.

Output: validated hook direction/copy and delivery direction.

### 07 — Storyboard

Input: completed Hook and all required upstream state.

Output: the canonical temporal scene sequence, action choreography, reference graph, creative timing, and generation-segmentation intent.

Storyboard is the creative source of truth for duration and temporal action.

Scene contract:

```text
SCENE
 ↓
ACTION GRAPH
 ↓
ACTION BEATS
 ├─ Body Motion
 ├─ Hand Motion
 ├─ Product Interaction
 ├─ Gaze
 ├─ Expression
 └─ Camera Behavior
 ↓
REFERENCE STATES
 ↓
TRANSITIONS
```

Use causal action:

```text
TRIGGER
 ↓
INTENTION
 ↓
ACTION
 ↓
PHYSICAL CONSEQUENCE
 ↓
RESULTING STATE
```

Human-looking motion must be controlled, action-coupled, and physically plausible. Do not use random gestures, gaze, product movement, or camera movement.

### 08 — Visual Prompt

Input: completed Storyboard and required reference states.

Output: **one static image prompt per required visual reference state**.

A reference state is a frozen visual state, not a generation segment. Bridge references are immutable. If a bridge changes, both adjacent scene boundaries and dependent downstream transitions become stale.

### 09 — Voice Script

Input: completed Storyboard, Strategy, Hook, Creator, Product facts, and campaign constraints.

Output: canonical scene-by-scene spoken dialogue plus Voice Performance Plan.

Voice Script is the sole source of truth for:

- exact spoken wording
- speaker
- pronunciation guidance
- speech timing
- delivery
- pace
- phrase grouping
- emphasis
- pitch/rhythm
- pause/breathing behavior

Spoken naturalization must preserve factual meaning and campaign intent.

### 10 — Video Prompt

Input: completed Storyboard, current Visual Prompt when visual continuity is required, current Voice Script when spoken content exists, and provider capability profile when generation is required.

Output: provider-compatible motion specifications and exact generation segment mapping.

Video Prompt consumes, but does not rewrite, canonical Voice Script dialogue. When speech generation is applicable, include a derived Voice Generation Reference inside Dialogue Sync. The Video Prompt must not become a competing voice specification.

Generation durations are limited to `[4, 6, 8, 10]` seconds. Final campaign duration is authoritative and must be composed exactly from supported segments. Never round, truncate, extend, or silently replace duration. If exact composition is impossible:

`duration_feasibility: BLOCKED`

### 11 — Production Output

Input: all required current, non-STALE upstream artifacts.

Output: consolidated production output assembled from current runtime state.

This is the final assembly step, not a separate QC or approval gate.

## Dependency Graph

```text
01 Brief & Product
        ↓
02 Campaign Intake
        ↓
03 Niche & Context
        ↓
04 Creator
        ↓
05 Content Strategy
        ↓
06 Hook
        ↓
07 Storyboard
   ┌────┼─────┐
   ↓    ↓     ↓
08     09     10
Visual Voice  Video
       ↓       ↑
       └───────┘
          Voice
        Sync Data
   \\________________/
            ↓
      11 Production
```

Stage 10 requires current Voice Script when spoken content exists. Stage 10 also consumes current visual/reference information when visual continuity is required.

## Revision and Invalidation

When a canonical upstream input changes:

1. identify the changed source
2. mark every affected dependent artifact `STALE`
3. preserve unaffected branches
4. rerun the smallest affected dependency chain
5. validate regenerated outputs
6. stop and wait for `/next`

Examples:

- Product change → Context, Creator when affected, Strategy, Hook, Storyboard, Visual, Voice, Video.
- Campaign requirement change → affected Context, Creator, Strategy, Hook, Storyboard, Visual, Voice, Video.
- Creator change → Strategy, Hook, Storyboard, Visual, Voice, Video.
- Strategy change → Hook, Storyboard, Visual, Voice, Video.
- Hook change → affected Storyboard and downstream assets.
- Storyboard change → Visual, Voice, Video.
- Reference-state change → affected Visual and Video transitions.
- Visual-only change → Video only when motion/state continuity is affected.
- Voice dialogue/performance/timing change → Video when synchronization is affected.
- Provider capability change → re-evaluate Video segmentation without changing creative duration.

A stale artifact must never be presented as current.

## Repository Freshness Contract

GitHub `adis-su/Affilix` on `main` is the implementation source of truth.

For every new `/Affilix` run:

1. resolve the current `main` HEAD
2. record `repository.commit_sha`
3. pin that commit for the run
4. load `SKILL.md`, this workflow, the entry contract, and only the relevant current engine/library files
5. execute the run against that pinned snapshot

Never silently mix files from different commits.

If `main` changes after a run is pinned, the active run remains on its pinned commit. The newer repository state is picked up by the next new run.

For implementation work outside a production run, resolve the current `main` HEAD immediately before editing or reporting repository status.

If current HEAD or a required file cannot be resolved, do not claim the repository is current. Continue only when available rules are sufficient; otherwise block the affected operation.

## Runtime State

Each run must preserve isolated state for:

- repository and pinned commit
- run ID and status
- campaign requirements
- product facts and evidence
- canonical niche context
- creator identity
- strategy
- hook
- storyboard and reference graph
- visual prompts
- voice script and performance plan
- video prompts and generation segments
- production output

Material artifacts should record their source commit SHA and relevant upstream artifact IDs.

## Completion

A run is complete only when all required stages are `COMPLETED` or `SKIPPED`, no required artifact is `STALE`, claims are supported, creator/product identity is current, storyboard and downstream specifications are synchronized, requested duration is preserved exactly, provider segmentation is compatible when required, and the final Production Output is generated.

