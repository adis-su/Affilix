# Affilix — End-to-End Production Workflow v3

## Purpose

This is the **single canonical stage registry and execution contract** for the Affilix production runtime. Mode selection and mode-specific conditional dependencies are defined by `ENGINE/CONTENT_MODE_ROUTING_CONTRACT.md`; this file remains the sole authority for stage IDs, names, order, and implementation paths.

Affilix runs as one continuous, dependency-aware production workflow. Engines are internal implementation components, not separate user-facing commands.

## Entry Point

The user-facing command is `/Affilix`.

A new `/Affilix` run must resolve the current `main` branch head, pin that commit for the run, load the relevant repository contracts, initialize isolated run state, resolve `run.content_mode`, and begin Stage 01 using the intake contract for that mode.

Repository resolution, commit pinning, source loading, and diagnostics are internal. They must never appear in the canonical Stage 01 opening.

## Canonical Stage Registry

The numeric stage ID in this registry is the ONLY workflow ordering and dependency identifier.

| Canonical Stage | Stage Name | Runtime Contract | Implementation Path |
|---|---|---|---|
| 01 | Brief & Product | 01_BRIEF_PRODUCT | `ENGINE/01_BRIEF_ANALYZER/` |
| 02 | Niche & Context | 02_NICHE_CONTEXT | `ENGINE/NICHE_CONTEXT_LOADER/` |
| 03 | Creator | 03_CREATOR | `ENGINE/02_CREATOR_SELECTOR/` |
| 04 | Content Strategy | 04_CONTENT_STRATEGY | `ENGINE/03_CONTENT_STRATEGY/` |
| 05 | Hook | 05_HOOK | `ENGINE/04_HOOK_ENGINE/` |
| 06 | Storyboard | 06_STORYBOARD | `ENGINE/05_STORYBOARD_ENGINE/` |
| 07 | Visual Prompt | 07_VISUAL_PROMPT | `ENGINE/06_VISUAL_PROMPT_ENGINE/` |
| 08 | Voice Script | 08_VOICE_SCRIPT | `ENGINE/08_VOICE_SCRIPT_ENGINE/` |
| 09 | Video Prompt | 09_VIDEO_PROMPT | `ENGINE/07_VIDEO_PROMPT_ENGINE/` |
| 10 | Production Output | 10_PRODUCTION_OUTPUT | `ENGINE/UGC_PRODUCTION_OUTPUT_TEMPLATE.md` |

### Stage/Engine Numbering Invariant

Engine directory prefixes are legacy implementation identifiers, not workflow stage IDs. They MUST NOT be used to infer stage order, prerequisites, handoffs, or progression.

The mapping above is authoritative. Any engine contract, runtime state, parser, resolver, or prompt that attempts to derive workflow order from a directory prefix is invalid and must fail validation rather than guessing.

`ENGINE/08_VOICE_SCRIPT_ENGINE/` is the canonical Stage 08 implementation path, while `ENGINE/07_VIDEO_PROMPT_ENGINE/` is the canonical Stage 09 implementation path. Engine directory prefixes remain implementation identifiers and must not be used as a general rule for deriving workflow order.

## Cross-Stage UGC Naturalism

`ENGINE/UGC_NATURALISM_CONTRACT.md` is a cross-stage production constraint, not a new stage.

Naturalism is validated inside the existing stages:
- Stage 04/05: the strategy and hook must be executable through believable human behavior.
- Stage 06: action choreography must express motivated timing, physical plausibility, bounded micro-motion, gaze, expression, product causality, and camera motivation.
- Stage 07: frozen reference states must preserve plausible posture, grip, gaze, expression, and continuity.
- Stage 08: spoken delivery must be conversational and physically/time aligned without inventing claims or experience.
- Stage 09: motion must express causal action, human timing, gaze behavior, restrained reaction, controlled camera response, and exact reference transitions.
- Stage 10: Production Output preserves naturalism traceability and never invents a missing naturalism correction.

Naturalism validation failure is handled inside the affected stage. It never creates a QC, approval, or additional workflow stage.

## Canonical Pipeline

```text
/Affilix
  ↓
CONTENT MODE SELECTOR (when mode is not explicit)
  ↓
01 BRIEF & PRODUCT / MODE-SPECIFIC BRIEF
  ↓ /next
02 NICHE & CONTEXT
  ↓ /next
03 CREATOR
  ↓ /next
04 CONTENT STRATEGY
  ↓ /next
05 HOOK
  ↓ /next
06 STORYBOARD
  ↓ /next
07 VISUAL PROMPT
  ↓ /next
08 VOICE SCRIPT       [when spoken content is required]
  ↓ /next
09 VIDEO PROMPT       [when video output is required]
  ↓ /next
10 PRODUCTION OUTPUT
```

No QC stage, Final UGC Package stage, or approval gate exists.

For `UGC_AFFILIATE`, the existing UGC stage requirements remain in force. Across modes, conditional stage skips are allowed only where `ENGINE/CONTENT_MODE_ROUTING_CONTRACT.md` or the applicable mode contract explicitly permits them. A skipped stage must record `SKIPPED` plus a reason. A stage whose mode-specific implementation is not yet available must be `BLOCKED`, never silently replaced by an unrelated engine.

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

`/next` means **synchronize the active run with the latest repository contract, then progress to the next dependency-satisfied stage**. It never means approve, accept, endorse, or waive validation.

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

The canonical stage ID and registry entry remain unchanged; the artifact schema is mode-aware.

- `UGC_AFFILIATE`: input is product name and product link/reference. Output is a normalized product brief, researched product facts, evidence/provenance, supported claims, and genuine unknowns.
- `QUOTE_CONTENT`: input is an editorial brief. Product identity, product link, product claims, and product demonstration are not required unless the user explicitly requests product-centered content. Output is a normalized editorial brief with source provenance and genuine unknowns.

Use `ENGINE/CONTENT_MODE_ROUTING_CONTRACT.md` to validate the selected mode and its required inputs.

For `UGC_AFFILIATE`, the supplied product link/reference must be actively inspected when accessible. Unsupported marketing language must not be promoted to fact. `QUOTE_CONTENT` does not require a product reference.

### 02 — Niche & Context

Input: completed Stage 01 brief artifact.

- `UGC_AFFILIATE`: output exactly one canonical niche/product context. Missing values remain `UNKNOWN`.
- `QUOTE_CONTENT`: resolve editorial niche, audience context, and topic context without manufacturing a product or product-type state.

Output and validation must preserve `content_mode` and source provenance.

### 03 — Creator

Input: completed Stage 01 and Stage 02 artifacts.

- `UGC_AFFILIATE`: resolve the requested canonical creator identity and applicable Creator Library references.
- `QUOTE_CONTENT`: select a creator only when the brief or selected editorial direction requires an on-screen/persona identity. If not required, mark Stage 03 `SKIPPED` with an explicit reason.

Any selected creator must come from the current pinned repository. Identity is locked downstream.

### 04 — Content Strategy

Input: completed Stage 01 and Stage 02 artifacts, plus Stage 03 Creator when required by the selected mode.

- `UGC_AFFILIATE`: use the existing product-centered strategy contract and output objective, audience, product role, angle, core message, story arc, and proof strategy.
- `QUOTE_CONTENT`: use the editorial strategy, pillar, and format contract when implemented. Do not invoke product proof scoring. Until that contract is implemented, block with `QUOTE_CONTENT_ENGINE_NOT_IMPLEMENTED`.

### 05 — Hook

Input: completed Strategy when required by the selected mode/format.

Output: validated hook direction/copy and delivery direction. A static format may skip this stage only when the mode-specific contract explicitly permits it.

### 06 — Storyboard

Input: completed Hook and all required upstream state for a video/story format. Static image-only formats may skip this stage only when the mode-specific contract explicitly permits it.

Output: the canonical temporal scene sequence, action choreography, Reference Plan, reference graph, creative timing, and generation-segmentation intent.

For each scene, Storyboard must plan an ordered Reference Trajectory. Reference density is action-complexity-driven. High-complexity scenes should target six meaningful reference states by default when justified; simpler scenes may use fewer. Six references are never a quota and never represent six scenes or six Video Prompts.

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

### 07 — Visual Prompt

Input: completed Storyboard and required reference states for video formats. For static image-only formats, Stage 07 uses the validated content strategy and image-specific brief/reference requirements without inventing a storyboard.

Output: **one static image prompt per required visual reference state**, with every Storyboard-declared reference state rendered exactly once.

A reference state is a frozen visual state, not a generation segment. Bridge references are immutable. If a bridge changes, both adjacent scene boundaries and dependent downstream transitions become stale.

### 08 — Voice Script

Input: completed Storyboard, Strategy, Hook, Creator, Product facts, and campaign constraints when spoken content is required.

Output: canonical scene-by-scene spoken dialogue plus Voice Performance Plan when spoken content is required.

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
- pause/breathing behavior When speech generation is applicable, include a derived Voice Generation Reference inside Dialogue Sync. The Video Prompt must not become a competing voice specification.

Spoken naturalization must preserve factual meaning and campaign intent. Never round, truncate, extend, or silently replace duration. If exact composition is impossible:

`duration_feasibility: BLOCKED`

### 09 — Video Prompt

Execution condition: required when video output is part of the requested deliverable. It is independent of whether spoken audio exists.

- `SPOKEN_ON_CAMERA` or `VOICE_OVER`: consume the current validated Stage 08 Voice Script.
- `NO_SPOKEN_VOICE`: Stage 08 is skipped, but Stage 09 still executes for video output. Do not invent dialogue, lip-sync, or voice-generation requirements.

Input: completed Storyboard, current Visual Prompt, current Voice Script when applicable, Strategy, Hook, Creator, Product facts, campaign constraints, provider capability profile, requested duration, and reference graph.

Output: exactly one user-facing Video Prompt per Storyboard scene, plus technical generation-segment metadata nested under each scene.

Prompt-count invariant:
`video_prompt_count == storyboard_scene_count`.

Multiple 4/6/8/10-second generation segments within one scene do not create additional user-facing Video Prompts. Multiple scenes must not be merged into one Video Prompt.

Storyboard remains the canonical source for scene intent, action choreography, narrative timing, product causality, resulting states, and reference transitions. Visual Prompt owns static appearance. Voice Script, when present, owns exact spoken wording and delivery. Video Prompt owns motion implementation and technical generation segmentation.

Spoken naturalization must preserve factual meaning and campaign intent.

### 10 — Production Output

Input: all required current, non-STALE upstream artifacts for the selected `content_mode`.

Output must be assembled by the applicable mode-specific output contract and include only required, current assets. `UGC_AFFILIATE` retains the existing UGC output contract. `QUOTE_CONTENT` must not use the UGC output template as an implicit fallback until its mode-specific strategy and production contracts are implemented.

Production Output must block final assembly when the selected mode or format is missing, stale, unsupported, or contradicted by a required downstream artifact.

This is the final assembly step, not a separate QC or approval gate.

## Content Mode Routing

`ENGINE/CONTENT_MODE_ROUTING_CONTRACT.md` defines the mode selector, mode-specific intake, conditional stage dependencies, and implementation blockers. The canonical ten-stage registry in this file remains unchanged. Changes to mode selection invalidate all mode-dependent run artifacts; never reuse production artifacts across modes. Where this contract defines mode-specific applicability, stage prerequisites must be interpreted through that routing contract rather than treating every UGC dependency as universal.

## Spoken Audio and External Dialogue

Spoken dialogue is modeled independently from the video provider's native audio-generation capability.

`campaign.audio_mode` answers whether the requested video generation itself must contain spoken audio:

- `SPOKEN_ON_CAMERA` → Stage 08 Voice Script is required; Stage 09 synchronizes visible creator speech with the canonical dialogue.
- `VOICE_OVER` → Stage 08 Voice Script is required; Stage 09 synchronizes the visual timeline with the canonical voice-over.
- `NO_SPOKEN_VOICE` → Stage 08 is skipped by default, but dialogue may still be requested as an external audio asset. When external dialogue is enabled, Stage 08 becomes required for dialogue authoring and timing, while Stage 09 generates silent video and preserves dialogue timing anchors for downstream sync.

Use these controls independently:

```yaml
audio_mode: NO_SPOKEN_VOICE
dialogue:
  enabled: true
  delivery: EXTERNAL_PROVIDER
  sync_required: true
```

`audio_mode` must never be overloaded to mean `dialogue_enabled`. `NO_SPOKEN_VOICE + EXTERNAL_PROVIDER` means the video provider generates no speech, while a separate dialogue provider produces the audio asset that is synchronized during final assembly.

Stage 08 owns exact dialogue wording, speaker, timing, and Voice Performance/Generation Reference. Stage 09 owns visual motion and timing anchors. Stage 10 records the external dialogue asset and synchronization requirement when applicable.

## Dependency Graph

```text
01 Brief & Product
        ↓
02 Niche & Context
        ↓
03 Creator
        ↓
04 Content Strategy
        ↓
05 Hook
        ↓
06 Storyboard
   ┌──────────┬──────────┐
   ↓          ↓          ↓
07 Visual   08 Voice   09 Video [when required]
   │          │          │
   └──────┬───┴─────────┘
          ↓
    10 Production
```

Stage 09 consumes the current Visual Prompt when visual continuity is required and the current Stage 08 Voice Script when dialogue timing is required. Native spoken-audio synchronization applies only to spoken modes; external dialogue synchronization applies when `NO_SPOKEN_VOICE` is paired with an enabled external dialogue layer. Stage 09 must not invent or rewrite canonical spoken wording.

## Downstream Dependency Order

After Stage 06 Storyboard, the workflow intentionally executes the spoken-content branch before motion implementation:

```text
06 Storyboard
   ├──→ 07 Visual Prompt
   └──→ 08 Voice Script [spoken modes only]
             ↓
       09 Video Prompt
             ↓
       10 Production Output
```

Stage 08 Voice Script is a Storyboard descendant and does not depend on Visual Prompt. Stage 09 Video Prompt consumes the current Storyboard, current Visual Prompt when visual continuity is required, and the current Stage 08 Voice Script when spoken content exists. This ordering reflects the actual data dependency rather than treating Voice Script as a final post-processing artifact.

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
- Audio / Voice Mode or dialogue-layer change → re-evaluate Stage 08 and Stage 09. `NO_SPOKEN_VOICE` alone permits Stage 08 to be SKIPPED; `NO_SPOKEN_VOICE + external dialogue enabled` requires Stage 08 for canonical dialogue/timing while Stage 09 remains silent-video generation. Spoken modes require Stage 08 and native dialogue synchronization.
- Creator change → Strategy, Hook, Storyboard, Visual, Voice, Video.
- Strategy change → Hook, Storyboard, Visual, Voice, Video.
- Content Format change → Hook, Storyboard, Visual, Voice, Video, and Production Output.
- Hook change → affected Storyboard and downstream assets.
- Storyboard change → Visual, Voice, Video.
- Reference-state change → affected Visual and Video transitions.
- Visual-only change → Video only when motion/state continuity is affected.
- Voice dialogue/performance/timing change → Video when synchronization is affected.
- Provider capability change → re-evaluate Video segmentation without changing creative duration.

A stale artifact must never be presented as current.

## Stage Resolution Guard

At runtime, resolve every stage by canonical stage ID/name from this document. Engine paths are lookup targets only. A stage artifact is valid only when its declared canonical stage matches the registry and its engine path matches the registry mapping.

If a dependency message, artifact, or runtime state reports a stage relationship that conflicts with this registry, stop the affected operation and correct the contract. Do not infer intent from numeric folder names.

## Repository Freshness Contract

GitHub `adis-su/Affilix` on `main` is the implementation source of truth.

For every new `/Affilix` run:

1. resolve the current `main` HEAD
2. record `repository.commit_sha`
3. pin that commit for the run
4. load `SKILL.md`, this workflow, the entry contract, and only the relevant current engine/library files
5. execute the run against that pinned snapshot

Never silently mix files from different commits.

If `main` changes after a run is pinned, the active run remains on its pinned commit until the next explicit `/next` or revision boundary. At that boundary, resolve the current `main` HEAD, synchronize the active run to the latest commit atomically before loading the next stage files, revalidate or invalidate affected artifacts, and only then execute the next dependency-satisfied stage. Never mix files from the old and new commits within one stage execution.

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
- voice script and performance plan when applicable
- video prompts and generation segments
- production output

Material artifacts should record their source commit SHA and relevant upstream artifact IDs.

## Completion

A run is complete only when all required stages are `COMPLETED` or `SKIPPED`, no required artifact is `STALE`, claims are supported, creator/product identity is current, storyboard and downstream specifications are synchronized, requested duration is preserved exactly, provider segmentation is compatible when required, and the final Production Output is generated.

