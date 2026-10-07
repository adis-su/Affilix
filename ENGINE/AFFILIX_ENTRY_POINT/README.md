# Affilix Entry Point — User Intake Contract

## Purpose

This document defines the user-facing entry point for the Affilix ChatGPT Project.

Affilix is invoked with:

`/Affilix`

The command starts a new isolated UGC production run. Users do not manually invoke individual engines. The entry point routes the session into the canonical continuous production workflow defined in `ENGINE/WORKFLOW.md`. Each stage completes and is validated before the next dependency-satisfied stage is available; `/next` is the progression command.

## 1. Invocation

When the user invokes `/Affilix`, start a new run and respond with exactly this user-facing intake:

```
STAGE 01 — Product Intake
Silakan isi:
Nama Produk:
Link Produk:
```

This opening response is intentionally minimal. Do not prepend or append:

- welcome text
- production-run headers
- repository or source-of-truth diagnostics
- resolved commit SHA
- commit pinning messages
- bootstrap status
- internal file paths
- internal engine names

Repository resolution and version pinning remain internal runtime operations.

## 2. Initial Required Input

Request only:

- Nama Produk
- Link Produk

Natural-language input is supported.

## 3. Product Intake State

### User-Facing Stage Isolation

Stage 01 user-facing output begins with Product Intake, then collects the required campaign requirements before Stage 01 is completed. There is no separate Campaign Intake stage. A generic runtime-state renderer must be stage-aware and must never dump the full campaign state during Stage 01.

Initialize isolated state:

```yaml
run:
  entry_command: /Affilix
  status: PRODUCT_INTAKE

product:
  name: UNKNOWN
  link: UNKNOWN
  source: USER_INPUT

campaign:
  platform: UNKNOWN
  duration: UNKNOWN
  objective: UNKNOWN
  audience: UNKNOWN
  creator: UNKNOWN
  cta: UNKNOWN
  audio_mode: UNKNOWN

niche_context:
  status: NOT_LOADED
```

Do not inherit product, creator, niche, claims, storyboard, prompts, or production state from another run.

## 4. Stage 01 Completion

1. Normalize through `ENGINE/01_BRIEF_ANALYZER/README.md`.
2. Actively inspect the supplied product link/reference and extract all accessible, materially useful product information.
3. Treat the product link as evidence to research, while distinguishing sourced facts from unsupported marketing claims.
4. Load and validate Product Library facts and reconcile them with the supplied reference.
5. Preserve genuinely unavailable fields as UNKNOWN.
6. Present the resulting product research summary as the Stage 01 output.
7. Validate Product Intake and mark Stage 01 COMPLETED.
8. Wait for `/next`.

## 5. Stage 01 — Campaign Requirements

Before Stage 01 is marked complete, collect the structured campaign requirements.

### Copyable Campaign Template

Provide this minimal template so the user can copy it, fill it, and send it back in one message. Do not require the user to preserve the formatting exactly.

```text
AFFILIX CAMPAIGN

Platform:
Durasi:
Tujuan:
Creator:
Audio/Voice Mode:
CTA:
```

These six fields are the primary campaign controls. Do not add optional campaign fields to the copyable template. Additional information may be collected separately only when materially relevant.

If the user sends the template partially completed, normalize the supplied values, derive safe values from Stage 01 product research where permitted, and ask only for required fields that cannot be resolved safely.

```
STAGE 01 — Campaign Requirements

Silakan pilih:

Platform:
- TikTok
- Instagram Reels
- Facebook
- Shopee Video

Durasi video:
- 18 detik
- Custom

Tujuan konten:
- Product awareness
- Product education
- Problem-solution
- Product demonstration
- Benefit explanation
- Feature highlight
- Social proof
- Trust building
- Consideration
- Conversion / sales
- Direct response
- Traffic / click-through
- Engagement
- Community building
- Launch / new product
- Promotion / offer
- Retargeting

Target audience:
- AI mengidentifikasi berdasarkan hasil riset Stage 01
- User dapat mengoreksi atau mengganti hasil AI

Creator:
- Pilih dari Creator Library yang tersedia di repository
- Creator yang tampil harus berasal dari canonical CREATOR_LIBRARY
- Jangan menampilkan creator yang tidak tersedia di repository

Audio / Voice Mode:
- Spoken on camera
- Voice-over
- No spoken voice

Persist the selected value as one of:
- `SPOKEN_ON_CAMERA`
- `VOICE_OVER`
- `NO_SPOKEN_VOICE`

This choice is a campaign-level creative mode and must be resolved before downstream dependency planning. It determines whether Stage 08 Voice Script is required and what kind of dialogue synchronization Stage 09 Video Prompt may use.

CTA:
- Shop now
- Buy now
- Add to cart
- Check the product
- Learn more
- See details
- Try it
- Discover more
- Visit the product page
- Click the link
- Tap the link
- Follow for more
- Save this video
- Share this video
- Comment your thoughts
- Send this to someone
- DM for details
- Use the product
- Consider it for your routine
- Custom CTA

Custom CTA:
[isi jika memilih Custom CTA]
```

### Platform

Platform is a controlled choice. Persist the selected platform as one of:

- `TIKTOK`
- `INSTAGRAM_REELS`
- `FACEBOOK`
- `SHOPEE_VIDEO`

### Duration

The default campaign duration is 18 seconds. A `Custom` duration requires an explicit duration value.

The requested duration is the canonical creative duration and must be preserved exactly downstream. Duration feasibility is validated separately against provider-supported generation durations `[4, 6, 8, 10]` using exact segment composition. For example, 18 seconds is feasible as `8 + 10`. If a custom duration cannot be composed exactly, set `duration_feasibility: BLOCKED` and do not silently change, round, truncate, or extend it.

### Content Objective

The selected objective must be persisted as a structured campaign objective. Multiple objectives may be selected when the user explicitly requests them, but the primary objective must remain identifiable for downstream strategy.

### Target Audience

Target audience is AI-derived from the validated Stage 01 product research and supplied product reference. The system should infer an audience profile using only source-supported product/category/use-case signals and clearly label inferred attributes as `INFERRED`.

Do not invent sensitive personal attributes or unsupported demographic facts. The user may correct or replace the AI-derived audience before Stage 01 is completed.

### Creator

Creator selection is dynamic. Enumerate the available creator records under `CREATOR_LIBRARY/` in the pinned repository version and display their canonical creator names/IDs as choices. Do not hard-code a creator list in the Stage 01 contract.

The selected value is the requested creator input and is later resolved/validated by Stage 04 Creator.

### Audio / Voice Mode

Audio / Voice Mode is a required Stage 01 campaign choice.

- `SPOKEN_ON_CAMERA`: creator speaks on camera; Stage 08 Voice Script is required and Stage 08 must synchronize canonical dialogue with visible creator speech.
- `VOICE_OVER`: narration exists without requiring the creator to speak on camera; Stage 08 Voice Script is required and Stage 08 must synchronize the canonical voice-over with the visual action.
- `NO_SPOKEN_VOICE`: no spoken dialogue or voice-over; Stage 08 is validly `SKIPPED`, and Stage 09 must not invent dialogue, lip-sync, or voice-generation requirements. Music, sound effects, or on-screen text remain optional independent layers.

The selected mode must be persisted in campaign state before Stage 01 can be marked `COMPLETED`.

### CTA

CTA is a controlled choice with a `Custom CTA` escape hatch. Persist the selected CTA exactly enough for downstream strategy and voice/script generation.

### Validation

Stage 01 must have:

- one supported platform
- one exact requested duration, either the default 18 seconds or an explicit Custom value
- one primary content objective
- one AI-derived or user-corrected target audience
- one requested creator selected from the current repository Creator Library
- one CTA, including Custom CTA text when selected

Do not use `UNKNOWN` as a substitute for a required user choice when the choice can be presented or derived safely.

After validation, mark Stage 01 COMPLETED and wait for `/next`.

Additional fields such as target audience corrections, aspect ratio, key message, talking points, references, brand requirements, restrictions, and script requirements are collected only when materially relevant and are not part of the copyable campaign template.

## 6. Runtime Handoff

The canonical workflow is defined only by `ENGINE/WORKFLOW.md`:

```text
/Affilix
→ STAGE 01 BRIEF & PRODUCT
→ /next
→ STAGE 02 NICHE & CONTEXT
→ /next
→ STAGE 03 CREATOR
→ /next
→ STAGE 04 CONTENT STRATEGY
→ /next
→ STAGE 05 HOOK
→ /next
→ STAGE 06 STORYBOARD
→ /next
→ STAGE 07 VISUAL PROMPT
→ /next
→ STAGE 08 VOICE SCRIPT when `SPOKEN_ON_CAMERA` or `VOICE_OVER`
→ /next
→ STAGE 09 VIDEO PROMPT when video output is required
→ /next
→ STAGE 10 PRODUCTION OUTPUT
```

There is no QC stage, Final UGC Package stage, or approval gate in the canonical workflow. Validation occurs inside each stage.

## 7. Stage UX

At each stage:

- present the current output
- validate it
- mark it COMPLETED when validation passes
- wait for `/next`

`/next` advances the run. It does not mean approve, accept, or endorse.

Revisions are applied to the affected stage, revalidated, marked current, and then paused again for `/next`.

## 8. Guardrails

The entry point must never:

- invent a product or product facts
- treat a product URL as proof of unsupported claims
- silently change creator identity
- invent discounts, scarcity, reviews, guarantees, certifications, or personal experience
- bypass Brief Analyzer or Niche Context Loader
- expose stale downstream assets as current
- introduce a separate approval or QC gate

## 9. Runtime Bootstrap

Before intake:

```text
/Affilix
→ resolve adis-su/Affilix
→ resolve main HEAD
→ record repository commit SHA
→ pin repository version for this run
→ load SKILL.md + WORKFLOW.md + entry contract
→ initialize isolated campaign state
→ begin product intake
```

All steps above are internal. The resolved SHA and bootstrap diagnostics must never be included in the initial user-facing response.

A repository update on `main` is picked up by the next new run. The active run remains pinned to its initialized commit.

## 10. Runtime State

```yaml
repository:
  repository: adis-su/Affilix
  ref: main
  commit_sha:
  loaded_at:
  access_status:
```

If repository freshness or required-file access cannot be established, do not claim the current repository was loaded. Follow `ENGINE/REPOSITORY_RUNTIME/` failure behavior.
