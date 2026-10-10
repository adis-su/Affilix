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
- target audience or audience context
- topic/theme or audience situation
- intended emotional response or takeaway
- requested output constraints when supplied

Persist these under the campaign/editorial brief, with provenance. Keep unresolved non-critical fields as `UNKNOWN`; ask only when a missing field materially blocks a safe, coherent output.

The existing six-field UGC campaign template remains unchanged and is shown only for `UGC_AFFILIATE`.

## Stage Routing and Conditional Dependencies

The canonical stage registry and stage IDs do not change.

| Canonical Stage | UGC Affiliate | Quote Content |
|---|---|---|
| 01 Brief & Product | Required; product and campaign intake | Required; editorial brief intake, no product dependency |
| 02 Niche & Context | Required; canonical product/niche context | Required; resolve editorial niche/audience context without inventing product state |
| 03 Creator | Required when a creator is selected/required by the brief | Optional; select a creator only when the intended format needs an on-screen/persona identity |
| 04 Content Strategy | Existing product-centered strategy contract | Must use editorial strategy, pillar, and format rules; do not invoke product proof scoring |
| 05 Hook | Required for applicable video/story formats; mode contract determines applicability | Required for story/reel formats; may be skipped for static quote image only if the mode-specific strategy contract explicitly says so |
| 06 Storyboard | Required for video output | Required for video/story formats; skipped for static image-only output |
| 07 Visual Prompt | Required | Required; prompt must match the selected static or video reference-state needs |
| 08 Voice Script | Required for spoken dialogue or requested external dialogue; otherwise skip under existing audio rules | Required only when the selected format requires authored spoken/external dialogue; otherwise skip with a mode-specific reason |
| 09 Video Prompt | Required for video output | Required for video output; skipped for static image-only output |
| 10 Production Output | Required; existing UGC output contract | Required; output assembly must be mode-aware and include only applicable, current assets |

A conditional skip is not a failure or approval gate. Record the canonical stage ID, `SKIPPED` status, and a precise reason. Do not treat skipped output as generated.

## Implementation Readiness

Mode selection and state routing are architectural foundations, not proof that every Quote Content engine is already implemented. Current readiness after Phase 01 is:

| Stage | Quote Content readiness | Runtime behavior until implemented |
|---|---|---|
| 01 Brief & Product | Editorial brief normalization contract added | May execute using the mode-aware Brief Analyzer and entry contract |
| 02 Niche & Context | Editorial context adapter not yet implemented | Block with `QUOTE_CONTENT_ENGINE_NOT_IMPLEMENTED`; do not pass an editorial-only brief to a product-only context loader |
| 03 Creator | Existing creator library may be used when a creator is explicitly required; optional otherwise | If not required, mark `SKIPPED`; if required and resolvable through the current creator contract, execute; otherwise block |
| 04 Content Strategy | Not implemented for Quote Content | Block with `QUOTE_CONTENT_ENGINE_NOT_IMPLEMENTED` |
| 05–10 | Mode-specific strategy/production behavior not implemented | Block the next required stage with `QUOTE_CONTENT_ENGINE_NOT_IMPLEMENTED`; do not fall back to UGC behavior |

Until the Quote Content context, strategy, and production contracts are implemented, unsupported downstream Quote Content stages must be reported as `BLOCKED` rather than silently falling back to product-centered UGC logic or claiming a complete production output.

As phases 02 and 03 are implemented, update this contract and the relevant engine contracts together. Do not create a duplicate workflow registry.

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
