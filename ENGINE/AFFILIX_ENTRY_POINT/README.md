# Affilix Entry Point — User Intake Contract

## Purpose

This document defines the user-facing entry point for the Affilix ChatGPT Project.

Affilix is invoked with:

`/Affilix`

The command starts a new isolated production run. Resolve `content_mode` using `ENGINE/CONTENT_MODE_ROUTING_CONTRACT.md` before mode-specific intake unless the user's request already makes the mode explicit. Users do not manually invoke individual engines. The entry point routes the session into the canonical continuous production workflow defined in `ENGINE/WORKFLOW.md`. Each stage completes and is validated before the next dependency-satisfied stage is available; `/next` is the progression command.

## 1. Invocation

When the user invokes `/Affilix` without an explicit mode, start a new isolated run and show this mode selector:

```
STAGE 01 — Content Mode

Pilih mode produksi:
1. UGC Affiliate — konten promosi produk
2. Quote Content — konten editorial dan relatable
```

If the user explicitly requests a mode in the invocation message, do not ask them to select it again. After mode resolution, show only that mode's intake. For `UGC_AFFILIATE`, the Product Intake prompt remains:

```
STAGE 01 — Product Intake
Silakan isi:
Nama Produk:
Link Produk:
```

Do not prepend or append to the active mode's canonical intake:

- welcome text
- production-run headers
- repository or source-of-truth diagnostics
- resolved commit SHA
- commit pinning messages
- bootstrap status
- internal file paths
- internal engine names

Repository resolution and version pinning remain internal runtime operations.

## 2. Mode Selection and Initial Input

Resolve and persist exactly one `run.content_mode` value:

- `UGC_AFFILIATE`
- `QUOTE_CONTENT`

A clear user request may determine the mode directly. Otherwise show the Content Mode Selector above. Never inherit mode from another run.

### UGC Affiliate

Request only the initial product fields:

- Nama Produk
- Link Produk

Natural-language input is supported. Continue to use the existing UGC campaign template and validation rules.

### Quote Content

Do not request product name or product link as mandatory fields. Do not show the UGC campaign template in this mode. Use an interactive, click-to-select intake for Quote Content. Do not present the options below as a plain-text template that users must copy, type, or manually reproduce. In the ChatGPT interface, render native interactive controls (for example, radio groups, segmented controls, or dropdowns) for the fixed-choice fields, and a text input for the optional topic/context. If interactive controls are unavailable in a particular client, show a concise numbered fallback and accept natural-language answers.

### Quote Content Interactive Intake

Render these fields as selectable controls:

- **Platform** — required selection: TikTok, Instagram Reels, Facebook, or other supported platform. Use only platforms supported by the current repository contract.
- **Format** — optional preference; default to **Otomatis (AI memilih)**. Choices: Quote Image, Cinematic Quote Reels, Relatable Story Reels, POV Relationship Reels, Mini Storytelling Reels.
- **Pilar** — optional preference; default to **Otomatis (AI memilih)**. Choices: Curhat Relate Rumah Tangga, Self-Healing Istri & Ibu, Relasi & Komunikasi Pasangan.
- **Pilar dan subpilar konten** — Stage 01 (displayed as **Brief**) may collect an optional pillar preference, but the canonical confirmation/selection happens in Stage 02 (displayed as **Sub Pilar**). In Stage 02, show 15 recommended subpillars from `ENGINE/03_CONTENT_STRATEGY/QUOTE_CONTENT_SUBPILLAR_REGISTRY.md` for the active pillar as native selectable controls. The user explicitly selects one. Include a **Ganti Subpilar** control that requests a fresh batch of exactly 15 alternatives for the same pillar. Each click must generate/retrieve 15 new, semantically distinct candidates, not shuffle, rename, or re-display the previous batch. Preserve prior batches and selected choices in the current run's per-pillar exploration history. If the pillar changes, show a fresh batch for that pillar while retaining its history. Do not require the user to type or copy subpillar names. Stage 04 consumes the Stage 02 selection and must not repeat the picker. Subpillar topics must be developed without blaming, shaming, stereotyping, or cornering anyone.
- **Tujuan publikasi** — required selection, presented as concise clickable options appropriate to editorial content, such as engagement, relatability/community, emotional reflection, or relationship communication/education. Do not expose product-sales objectives in Quote Content mode unless the user explicitly reclassifies the run.
- **Durasi video** — required only for video formats: 18 detik, 28 detik, or 30 detik. For Quote Image, automatically set duration to NOT_APPLICABLE and hide/disable this control.
- **Voice/Audio** — selectable options: Otomatis (default: ngomong langsung ke kamera), Teks saja, Voice-over, Dialog langsung ke kamera. Resolve the selected option into the canonical audio/dialogue state before downstream dependency planning. `Otomatis` resolves to `SPOKEN_ON_CAMERA` for video formats and uses `DIRECT_TO_CAMERA_TALKING_HEAD` as the visual delivery mode. `Dialog langsung ke kamera` also resolves to `SPOKEN_ON_CAMERA`. `Voice-over` and `Teks saja` are explicit audio overrides; they do not silently replace the default visual treatment with montage/B-roll.
- **Topik atau konteks khusus** — optional free-text input. If supplied, use it to recommend a matching pillar/subpillar and angle; do not force a mismatch. The user may leave it blank and let Affilix derive a coherent topic from the selected pillar, objective, and available editorial context.

Use concise labels and sensible defaults. Do not force users to fill optional fields, do not request a content quantity/batch-count field, and do not add a user-selected CTA field. CTA remains an editorial decision only when it serves the objective.

When the interface supports interactive controls, collect selections through those controls and normalize their values into the existing canonical brief schema. Do not change stage IDs, downstream contracts, or the existing UGC Affiliate intake.

Required intake controls are platform, publishing objective, topic/audience context sufficient for a coherent concept, and video duration when a video format is requested. Format and pillar may be left on automatic selection. Audio mode may be inferred from an explicit format/context when safe; otherwise use the minimum-question principle. For static `QUOTE_IMAGE`, duration is `NOT_APPLICABLE`, not a video-duration choice.

Do not collect or require a content quantity/batch-count field or a user-selected CTA field. Affilix may plan batch distribution only when separately requested, and may derive a CTA only when it serves the publishing objective.

For Quote Content video formats, default the visual delivery to `DIRECT_TO_CAMERA_TALKING_HEAD`: the creator speaks to the lens, not as voice-over over B-roll. The selected Voice/Audio option can explicitly override spoken delivery, but must not silently change the visual treatment. Persist `delivery_mode` with the normalized campaign/strategy state and pass it to Storyboard, Visual Prompt, Voice Script, and Video Prompt.

For spoken video, the selected duration is a hard creative constraint for script length and timing:
- 18 seconds: initial target 35–42 spoken words.
- 28 seconds: initial target 55–65 spoken words.
- 30 seconds: initial target 60–70 spoken words.

These are initial conversational-delivery ranges, not a substitute for timing validation. Validate the actual script against delivery pace, pauses, speaker changes, and storyboard timing. Do not pad, rush unnaturally, or change the requested duration to fit an overlong script. Text-only videos do not use a spoken-word target; validate on-screen text readability instead.

## 3. Product Intake State

### User-Facing Stage Isolation

Stage 01 user-facing output begins with the Content Mode Selector only when mode is not explicit. `UGC_AFFILIATE` then begins with Product Intake and collects required campaign requirements before Stage 01 is completed. `QUOTE_CONTENT` begins with its editorial brief intake and does not require product intake. There is no separate Campaign Intake stage. A generic runtime-state renderer must be stage-aware and must never dump the full campaign state during Stage 01.

Initialize isolated state:

```yaml
run:
  entry_command: /Affilix
  status: CONTENT_MODE_SELECTION
  content_mode: UNKNOWN

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
  audio_mode: UNKNOWN
  delivery_mode: DIRECT_TO_CAMERA_TALKING_HEAD
  dialogue:
    enabled: UNKNOWN
    delivery: UNKNOWN
    sync_required: UNKNOWN

editorial_brief:
  topic: UNKNOWN
  audience_context: UNKNOWN
  intended_emotional_response: UNKNOWN
  takeaway: UNKNOWN

niche_context:
  status: NOT_LOADED
```

Do not inherit content mode, product, creator, niche, claims, editorial brief, storyboard, prompts, or production state from another run.

## 4. Stage 01 Completion

Apply the mode-specific intake and validation rules from `ENGINE/CONTENT_MODE_ROUTING_CONTRACT.md`.

1. Normalize through `ENGINE/01_BRIEF_ANALYZER/README.md` using the selected content mode.
2. For `UGC_AFFILIATE`, inspect the supplied product link/reference, reconcile accessible product facts with Product Library records, and preserve genuinely unavailable fields as UNKNOWN.
3. For `QUOTE_CONTENT`, normalize the editorial brief and its provenance without requiring a product reference.
4. Present the Stage 01 output scoped to the active mode.
5. Validate the mode-specific required fields, mark Stage 01 COMPLETED, and wait for `/next`.

## 5. Stage 01 — Campaign Requirements

For `UGC_AFFILIATE`, before Stage 01 is marked complete, collect the structured campaign requirements below. For `QUOTE_CONTENT`, collect and validate the editorial brief instead; do not require product-specific fields.

### Copyable Campaign Template

Provide this minimal template so the user can copy it, fill it, and send it back in one message. Do not require the user to preserve the formatting exactly.

```text
AFFILIX CAMPAIGN

Platform:
Durasi:
Tujuan:
Creator:
Audio/Voice Mode:
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
- No spoken voice + external dialogue

Persist the selected value as one of:
- `SPOKEN_ON_CAMERA`
- `VOICE_OVER`
- `NO_SPOKEN_VOICE`

This choice is a campaign-level native-audio mode and must be resolved before downstream dependency planning. `No spoken voice + external dialogue` persists `audio_mode: NO_SPOKEN_VOICE` plus an enabled `EXTERNAL_PROVIDER` dialogue layer. The combination determines whether Stage 08 Voice Script is required and what kind of synchronization Stage 09 Video Prompt may use.
```

### Platform

Platform is a controlled choice. Persist the selected platform as one of:

- `TIKTOK`
- `INSTAGRAM_REELS`
- `FACEBOOK`
- `SHOPEE_VIDEO`

### Duration

This UGC Affiliate duration rule applies only to `UGC_AFFILIATE`. For `QUOTE_CONTENT` video formats, the only user-selectable durations are 18, 28, and 30 seconds. Their exact segment compositions are respectively `8 + 10`, `10 + 10 + 8`, and `10 + 10 + 10`, using provider-supported segments `[4, 6, 8, 10]`. Preserve the selected final duration exactly. Do not silently change, round, truncate, extend, or pad the video. For static `QUOTE_IMAGE`, duration is `NOT_APPLICABLE`.

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

- `SPOKEN_ON_CAMERA`: creator speaks directly to the camera by default; Stage 08 Voice Script is required and Stage 08 must synchronize canonical dialogue with visible creator speech.
- `VOICE_OVER`: narration exists without requiring the creator to speak on camera; Stage 08 Voice Script is required and Stage 08 must synchronize the canonical voice-over with the visual action.
- `NO_SPOKEN_VOICE`: no native spoken dialogue or voice-over; Stage 08 is skipped only when no dialogue layer is requested.
- `NO_SPOKEN_VOICE + EXTERNAL_PROVIDER`: the video provider generates silent video while Stage 08 authors canonical dialogue/timing for a separate external audio asset. Stage 09 carries synchronization anchors without native voice-generation or lip-sync requirements.

Music, sound effects, or on-screen text remain optional independent layers.

The selected mode and any external dialogue layer must be persisted in campaign state before Stage 01 can be marked `COMPLETED`.

### Validation

For `UGC_AFFILIATE`, Stage 01 must have:

- one supported platform
- one exact requested duration, either the default 18 seconds or an explicit Custom value
- one primary content objective
- one AI-derived or user-corrected target audience
- one requested creator selected from the current repository Creator Library
- one resolved Audio / Voice Mode and dialogue-layer state

For `QUOTE_CONTENT`, validate the editorial brief and applicable controls: platform, objective, topic/audience context, and a supported duration of exactly 18, 28, or 30 seconds for video formats. Static `QUOTE_IMAGE` uses `duration: NOT_APPLICABLE`. Format and pillar can be automatic or explicit; audio mode must be resolved when it changes stage dependencies. Product identity and creator identity are not mandatory by default. Do not add user input fields for content quantity or CTA. Do not use `UNKNOWN` as a substitute for a required user choice when the choice can be presented or derived safely.

After validation, mark Stage 01 COMPLETED and wait for `/next`.

Additional fields such as target audience corrections, aspect ratio, key message, talking points, references, brand requirements, restrictions, and script requirements are collected only when materially relevant and are not part of the copyable campaign template.

## 6. Runtime Handoff

The canonical stage registry is defined only by `ENGINE/WORKFLOW.md`; mode-specific intake and dependencies are defined by `ENGINE/CONTENT_MODE_ROUTING_CONTRACT.md`:

```text
/Affilix
→ STAGE 01 BRIEF (QUOTE_CONTENT) / BRIEF & PRODUCT (UGC_AFFILIATE)
→ /next
→ STAGE 02 SUB PILAR (QUOTE_CONTENT) / NICHE & CONTEXT (UGC_AFFILIATE)
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

When `main` changes after a run is pinned, the active run remains pinned until the next explicit `/next` or revision boundary. At that boundary, resolve the current `main` HEAD, synchronize the active run to the new commit, and revalidate or invalidate affected artifacts before executing the requested progression or revision. This rule is authoritative with `ENGINE/REPOSITORY_RUNTIME/RUNTIME_CONTRACT.md` and `SKILL.md`.

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
