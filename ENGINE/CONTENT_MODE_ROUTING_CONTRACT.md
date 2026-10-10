# Affilix Content Mode Routing Contract

## Purpose

This contract defines mode selection and routes each run to the correct production behavior without creating a second Affilix system or changing the canonical ten-stage registry.

The canonical workflow stage IDs remain 01–10 as defined in `ENGINE/WORKFLOW.md`. Mode-specific requirements determine which inputs and stage outputs are required. A stage may be marked `SKIPPED` only when this contract or the relevant mode-specific contract explicitly permits it.

## Supported Content Modes

### `UGC_AFFILIATE`

Product-centered UGC production. Requires a product identity/reference and retains the existing product evidence, claims, creator identity, action choreography, reference continuity, voice, video duration, and production-output constraints.

This is the compatibility default when the user explicitly supplies a product brief and requests affiliate/product-promotion content. If the intent is ambiguous, ask the user to choose a mode rather than silently guessing.

### `QUOTE_CONTENT`

Editorial social content centered on relatable experiences, emotional reflection, relationship communication, or quote-led storytelling. A product is not required and must not be fabricated as a dependency.

Initial editorial context may include platform, audience, topic/theme, intended emotional response, publishing objective, and user-supplied constraints. The mode-specific strategy determines the final content format.

For every Quote Content video format, the default visual delivery is `DIRECT_TO_CAMERA_TALKING_HEAD`: the creator addresses the lens as the primary on-screen speaker. Resolve `Otomatis` to `audio_mode: SPOKEN_ON_CAMERA` plus this delivery mode. Explicit `VOICE_OVER` or `NO_SPOKEN_VOICE` selections override the audio behavior but do not silently switch the visual treatment to B-roll or montage. Carry `delivery_mode` through Strategy, Storyboard, Visual Prompt, Voice Script, and Video Prompt. `QUOTE_IMAGE` is unaffected.

## Mode Selection

For a new `/Affilix` run without an explicit mode, present the Content Mode Selector before requesting mode-specific fields:

```text
STAGE 01 — Content Mode

Pilih mode produksi:
1. UGC Affiliate — konten promosi produk
2. Quote Content — konten editorial dan relatable
```

Persist exactly one value in `run.content_mode`:

- `UGC_AFFILIATE`
- `QUOTE_CONTENT`

Do not inherit the mode from another run. A direct user request that clearly identifies one mode may select it without asking the user to repeat the choice.

## Mode-Specific Intake

### UGC Affiliate

Use the existing Product Intake and campaign requirements contract in `ENGINE/AFFILIX_ENTRY_POINT/README.md`. Product name and product reference remain required. Preserve all current product evidence and campaign validation rules.

### Quote Content

Do not request or require product name, product URL, product claims, product library records, or a product demonstration unless the user explicitly changes the brief to product-centered content.

Collect only the inputs materially needed to establish the editorial brief:

- platform
- publishing objective
- target audience/context and topic/theme or audience situation
- intended emotional response or takeaway
- optional format preference (automatic selection is allowed)
- optional editorial pillar preference (automatic selection is allowed)
- fixed final video duration: exactly 20 seconds for video formats; not a user-selectable field; generation composition is exactly `10 + 10` seconds
- audio/voice preference when it affects stage dependencies
- optional additional context or constraints

For static `QUOTE_IMAGE`, duration is `NOT_APPLICABLE`. Do not request or require a content quantity/batch-count field or a user-selected CTA field. CTA is an editorial decision and is included only when it serves the publishing objective. Persist supplied values and their provenance under the campaign/editorial brief. Keep unresolved non-critical fields as `UNKNOWN`; ask only when a missing field materially blocks a safe, coherent output.

The existing six-field UGC campaign template remains unchanged and is shown only for `UGC_AFFILIATE`.

## Stage Routing and Conditional Dependencies

The canonical stage registry and stage IDs do not change. User-facing display names are mode-specific: for `QUOTE_CONTENT`, Stage 01 is **Brief** and Stage 02 is **Sub Pilar**; for `UGC_AFFILIATE`, keep **Brief & Product** and **Niche & Context**. These aliases apply only to presentation and must not alter IDs, dependencies, or runtime contracts.

| Canonical Stage | UGC Affiliate | Quote Content |
|---|---|---|
| 01 Brief & Product | Required; product and campaign intake | Required; editorial brief intake, no product dependency |
| 02 Niche & Context | Required; canonical product/niche context | Required; use the editorial context branch in `ENGINE/NICHE_CONTEXT_LOADER/README.md` |
| 03 Creator | Required when a creator is selected/required by the brief | Optional; select a creator only when the intended format needs an on-screen/persona identity |
| 04 Content Strategy | Existing product-centered strategy contract | Use `ENGINE/03_CONTENT_STRATEGY/QUOTE_CONTENT_STRATEGY_CONTRACT.md`; do not invoke product proof scoring |
| 05 Hook | Required for applicable video/story formats; mode contract determines applicability | Use `ENGINE/04_HOOK_ENGINE/QUOTE_CONTENT_HOOK_CONTRACT.md` for story/reel formats; may be skipped for static quote image only when strategy explicitly permits |
| 06 Storyboard | Required for video output | Required for video/story formats; skipped for static image-only output |
| 07 Visual Prompt | Required | Required; prompt must match the selected static or video reference-state needs |
| 08 Voice Script | Required for spoken dialogue or requested external dialogue; otherwise skip under existing audio rules | Required only when the selected format requires authored spoken/external dialogue; otherwise skip with a mode-specific reason |
| 09 Video Prompt | Required for video output | Required for video output; skipped for static image-only output |
| 10 Production Output | Required; existing UGC output contract | Required; output assembly must be mode-aware and include only applicable, current assets |

A conditional skip is not a failure or approval gate. Record the canonical stage ID, `SKIPPED` status, and a precise reason. Do not treat skipped output as generated.

## Implementation Readiness

Readiness means a current mode-specific contract exists and is wired into the canonical engine/runtime references. It does not claim that external image/video generation has been run for a particular campaign.

| Stage | Quote Content readiness | Runtime behavior |
|---|---|---|
| 01 Brief & Product | Implemented in Phase 01 | Execute mode-aware editorial intake; no product dependency |
| 02 Niche & Context | Implemented in Phase 02 | Use editorial context; preserve provenance and unknowns |
| 03 Creator | Conditional; existing Creator Library integration | Skip with reason when no visible creator/persona is needed; block if required but unresolved |
| 04 Content Strategy | Implemented in Phase 02 | Use `QUOTE_CONTENT_STRATEGY_CONTRACT.md` |
| 05 Hook | Implemented in Phase 02 | Use `QUOTE_CONTENT_HOOK_CONTRACT.md`; static format may skip only with explicit reason |
| 06 Storyboard | Implemented in Phase 03 | Use `QUOTE_CONTENT_STORYBOARD_CONTRACT.md`; `QUOTE_IMAGE` skips with `STATIC_IMAGE_FORMAT` |
| 07 Visual Prompt | Implemented in Phase 03 | Use `QUOTE_CONTENT_VISUAL_PROMPT_CONTRACT.md`; one prompt per required visual/reference state |
| 08 Voice Script | Implemented in Phase 03, conditional | Use `QUOTE_CONTENT_VOICE_SCRIPT_CONTRACT.md`; skip only under its explicit audio/format rules |
| 09 Video Prompt | Implemented in Phase 03, conditional | Use `QUOTE_CONTENT_VIDEO_PROMPT_CONTRACT.md`; one prompt per scene and exact duration composition |
| 10 Production Output | Implemented in Phase 03 | Use `ENGINE/QUOTE_CONTENT_PRODUCTION_OUTPUT_CONTRACT.md`; never fall back to UGC template |

Mode-specific contracts do not replace the universal engine; they select the applicable behavior and schema. A required artifact that is missing, stale, contradictory, or unsupported still blocks the affected stage. Phase 04 regression and hardening remains required before claiming end-to-end regression acceptance.

## Revision and Invalidation

Changing `run.content_mode` invalidates all mode-dependent campaign inputs and production artifacts. Start a fresh isolated run state for the newly selected mode rather than reusing product, creator, editorial, strategy, storyboard, prompt, voice, or production artifacts from the prior mode.

Within a mode, follow the existing dependency invalidation rules in `ENGINE/WORKFLOW.md`. Changes to editorial topic, audience, pillar, or format invalidate every downstream artifact that depends on that field.

## Validation

Before completing Stage 01:

- `content_mode` is one of the two registered values.
- Mode-specific required inputs are present or safely resolved.
- Fields irrelevant to the selected mode are not treated as mandatory.
- The selected mode is persisted in run state and provenance.
- No state is inherited from another production run.

Before any downstream stage executes, verify that the selected mode has an implemented contract for that stage. If not, block that stage with the defined implementation blocker. Never use an unrelated engine as an implicit fallback.
