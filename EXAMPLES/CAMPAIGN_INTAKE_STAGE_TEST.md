# Affilix Campaign Intake Stage Regression Test

## Test ID
INTAKE-002

## Purpose
Validate that /Affilix opens at Stage 01 and /next after Product Intake exposes Campaign Intake as the explicit Stage 02.

## Stage 01
Expected opening:

STAGE 01 — Product Intake
Silakan isi:
Nama Produk:
Link Produk:

No bootstrap diagnostics, commit SHA, or internal runtime text may appear.

## Stage 02
After Stage 01 is completed and the user sends /next, expected intake:

STAGE 02 — Campaign Intake

Silakan isi:
Platform:
Durasi video:
Tujuan konten:
Target audience:
Creator:
CTA:

## Stage 02 Choice Contract

Platform choices:
- TikTok
- Instagram Reels
- Facebook
- Shopee Video

Duration choices:
- 18 seconds
- Custom exact duration

Content objective choices include:
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
- must be derived from validated Stage 01 product research and product reference
- must distinguish source-supported facts from inferred audience attributes
- must allow user correction/replacement
- must not invent sensitive personal attributes

Creator:
- must enumerate the current `CREATOR_LIBRARY/` records from the pinned repository
- must not expose creator names that do not exist in the repository

CTA choices include:
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

## Validation
Stage 02 must persist:
- platform
- requested video duration
- content objective
- target audience
- requested creator
- CTA

The default 18-second duration must remain exact. Custom durations must remain exact and are feasible only when they can be composed from provider-supported durations `[4,6,8,10]`. If not feasible, mark `duration_feasibility: BLOCKED` rather than changing the requested duration.

The target audience must carry provenance, distinguishing product-source facts from AI-inferred audience attributes.

The requested creator must resolve to a creator present in the pinned repository's `CREATOR_LIBRARY/`.

The requested creator is campaign input. Canonical creator identity is resolved and validated later by Stage 04 Creator.

The requested creator is campaign input. Canonical creator identity is resolved and validated later by Stage 04 Creator.

Requested duration is authoritative campaign input and must remain unchanged by downstream provider segmentation.

## Acceptance
PASS only when:
1. Stage 01 remains the Product Intake entry.
2. Stage 02 is Campaign Intake.
3. All six Stage 02 fields are exposed exactly as specified.
4. /next progresses from Stage 01 to Stage 02.
5. Stage 02 completion progresses to Stage 03 Niche & Context.
6. No approval gate, QC stage, or hidden bootstrap diagnostics are introduced.


## Stage 01 Output Isolation Regression

Stage 01 must not render Campaign Intake fields before Stage 02 is active.

The Stage 01 user-facing response/output must NOT contain:
- Platform
- Durasi video
- Tujuan konten
- Objective
- Target audience
- Creator
- CTA
- campaign status summaries showing these fields as UNKNOWN or "Belum diberikan"

It is valid for these fields to exist internally as UNKNOWN in isolated runtime state. Internal state initialization must not leak into the Stage 01 user-facing output.

## Renderer Contract

Any generic runtime/status renderer must apply the active-stage output scope before presentation. Stage 01 scope is Product Intake only. Stage 02 scope is Campaign Intake only. A regression passes only when later-stage fields remain hidden until their owning stage becomes active.


## Stage 01 Product Research Regression

When Stage 01 receives a product link, it must attempt active product-reference research before presenting the completed stage. A compliant Stage 01 result includes:
- researched product identity
- available brand/category/product-type information
- materially useful product facts, variants, usage, ingredients/materials, benefits/selling points, or other source-supported details when present
- source/provenance distinction
- explicit UNKNOWN only for information that remains genuinely unavailable

The output must not merely state that the link was received or is a reference source.


## Downstream Prompt Dependency Regression

Expected downstream order after Stage 07 Storyboard:

1. Stage 08 Visual Prompt
2. Stage 09 Voice Script when spoken content is required
3. Stage 10 Video Prompt when video output is required
4. Stage 11 Production Output

Acceptance:
- Video Prompt must not execute before a current Voice Script when spoken content exists.
- Voice Script is the canonical source of exact spoken wording.
- Video Prompt must include DIALOGUE SYNC when spoken content exists.
- DIALOGUE SYNC exact dialogue must match the current Voice Script.
- If Voice Script changes, affected Video Prompt becomes STALE and must be revalidated.
- A dialogue-only revision must not automatically invalidate Visual Prompt unless visual or action timing is affected.
- If dialogue crosses a generation segment boundary, the immutable bridge reference remains the continuity anchor.


## Voice Script UGC Conversationality Regression

A Voice Script must translate validated product facts into spoken creator language rather than reproducing product-page copy.

Example input:
- Product fact: contains ceramide complex
- Supported benefit: helps hydrate and support the skin barrier
- Texture: lightweight
- CTA: Buy now

The engine may use the facts, but should flag a line such as:
"Memiliki ceramide complex untuk membantu hidrasi dan mendukung skin barrier dengan sensasi ringan untuk rutinitas skincare. Buy now."

as NEEDS_REFINEMENT because it stacks feature/benefit language and ends with an abrupt promotional CTA.

A conversational alternative may be:
"Yang aku suka dari ini, ada ceramide complex-nya dan teksturnya juga ringan. Jadi enak dipakai sehari-hari."

Acceptance:
1. Product facts remain unchanged and supported.
2. The engine does not invent first-person usage or outcomes.
3. The CTA intent remains represented when a CTA is required.
4. Conversationality validation is advisory and may return NEEDS_REFINEMENT.
5. Voice Script remains canonical for exact spoken wording consumed by Video Prompt.
