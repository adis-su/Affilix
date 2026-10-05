# Affilix Campaign State Model

## Purpose

This document defines the logical runtime-state model for an Affilix production run. It is a state contract, not a requirement for an external campaign database.

GitHub `adis-su/Affilix` remains the implementation source of truth. The ChatGPT Project hosts the active conversational run state.

## Canonical Separation

```text
GitHub
  = implementation rules + engines + schemas + libraries

ChatGPT Project runtime
  = isolated run state + stage progress + production artifacts

External database / Telegram / Edge Functions
  = NOT part of the canonical runtime
```

## Responsibilities

The runtime state may preserve:

- campaign/run identity
- current canonical stage and stage status
- pinned repository commit
- normalized campaign/product/niche state
- decision queue
- production artifacts
- provenance and upstream artifact references

There is no approval state. Validation is performed inside each stage, and `/next` is progression only.

## Canonical Stage Identity

Stage order and dependencies MUST come from `ENGINE/WORKFLOW.md`. Campaign `audio_mode` is a required Stage 02 decision that controls spoken-content dependencies. Engine directory numbers are implementation identifiers only and MUST NOT be interpreted as workflow stage IDs.

## Runtime State Shape

```yaml
run:
  id:
  status:
  entry_command: /Affilix
  current_stage:

repository:
  repository: adis-su/Affilix
  ref: main
  commit_sha:
  loaded_at:
  access_status:

campaign:
  platform:
  requested_duration:
  creative_duration:
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
  campaign_intake: { status:, output: }
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

## Repository Pinning

At run initialization:

1. resolve current `main`
2. record its commit SHA
3. pin that commit for the active run
4. load all relevant repository contracts from that snapshot

Never silently mix repository commits inside one active run.

## Progression

Each stage follows:

`INPUT → PROCESS → OUTPUT → VALIDATE → MARK COMPLETED → WAIT FOR /next`

A revision keeps the current stage active, revalidates it, invalidates affected downstream artifacts, and waits for `/next`.

## Completion

A run is complete only when every required canonical stage is `COMPLETED` or `SKIPPED`, no required artifact is `STALE`, and all required production outputs are current.


## Audio Mode Dependency Contract

Stage 02 must persist exactly one `campaign.audio_mode` value:

- `SPOKEN_ON_CAMERA` → Stage 09 required; Stage 10 consumes canonical spoken dialogue and lip-sync requirements.
- `VOICE_OVER` → Stage 09 required; Stage 10 consumes canonical voice-over timing and voice-generation reference without requiring visible creator speech.
- `NO_SPOKEN_VOICE` → Stage 09 `SKIPPED` with reason `AUDIO_MODE_NO_SPOKEN_VOICE`; Stage 10 has no Voice Script dependency and must declare spoken audio/lip-sync as not applicable.

Changing `audio_mode` is a campaign revision. Recompute Stage 09/10 dependency state and invalidate affected artifacts rather than silently carrying the previous mode forward.
