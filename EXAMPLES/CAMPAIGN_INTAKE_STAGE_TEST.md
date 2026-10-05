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
Audio / Voice Mode:
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

## Audio / Voice Mode Contract

Stage 02 must require exactly one:
- `SPOKEN_ON_CAMERA`
- `VOICE_OVER`
- `NO_SPOKEN_VOICE`

The selected mode must be persisted before Stage 02 is marked `COMPLETED`.

## Validation
Stage 02 must persist:
- platform
- requested video duration
- content objective
- target audience
- requested creator
- audio mode
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
3. All seven Stage 02 fields are exposed exactly as specified, including Audio / Voice Mode.
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
- Video Prompt must not execute before a current Voice Script when `audio_mode` is `SPOKEN_ON_CAMERA` or `VOICE_OVER`.
- When `audio_mode` is `NO_SPOKEN_VOICE`, Stage 09 is `SKIPPED` with reason `AUDIO_MODE_NO_SPOKEN_VOICE` and Video Prompt must not require or invent Voice Script content.
- Voice Script is the canonical source of exact spoken wording.
- Video Prompt must include DIALOGUE SYNC when spoken content exists.
- DIALOGUE SYNC exact dialogue must match the current Voice Script.
- If Voice Script changes, affected Video Prompt becomes STALE and must be revalidated.
- A dialogue-only revision must not automatically invalidate Visual Prompt unless visual or action timing is affected.
- If dialogue crosses a generation segment boundary, the immutable bridge reference remains the continuity anchor.



## Video Generation Segment Determinism Regression

A production-ready generation segment must specify a deterministic reference-to-reference transition rather than relying on a compressed action summary.

Required acceptance criteria:

1. Segment duration is exact and is one of the provider-supported durations [4,6,8,10].
2. Start reference state is explicitly described.
3. Every material visual change is represented as an ordered action beat with a physical cause and resulting state.
4. An immutable bridge reference has an explicit physical state contract when present.
5. Product interaction identifies physical contact and state change, including hand ownership where relevant.
6. Gaze changes are bounded to action beats or timing intervals.
7. Camera behavior is tied to the active action and preserves required face/product visibility.
8. Target/end state explicitly identifies posture, hand, product, gaze, expression, and framing state.
9. Every dialogue/voice-over interval fits completely inside the exact segment duration.
10. Voice-over explicitly defines mouth behavior when lip-sync is not required.
11. `NO_SPOKEN_VOICE` explicitly disables spoken dialogue, lip-sync, and voice-generation requirements.
12. Audio mode changes trigger Stage 09/10 dependency re-evaluation.
13. Dialogue is synchronized to the visual action and does not introduce a competing wording version of the canonical Voice Script.
14. Negative constraints cover skipped/reversed/duplicated beats, unexplained product state changes, hand swapping, and premature target-state matching.

Example failure:

    Duration: exactly 8 seconds
    Voice-over: 00:04.2–00:08.2

This fails because the dialogue exceeds the segment boundary.

Example bridge requirement:

    R02:
    - container open
    - supporting hand holds the product upright
    - opposite fingertip carries a small visible amount of moisturizer
    - label orientation remains unchanged
    - gaze is directed toward the fingertip
    - framing remains consistent with the canonical bridge state

The bridge state must be reused exactly wherever R02 is the shared boundary between generation segments.


## Video Generation Naturalization Regression

Naturalization must function as a bounded realism layer over the canonical Action Graph and Reference Graph, not as an independent source of random movement.

Required acceptance criteria:

1. Baseline human micro-motion is restrained and subordinate to the primary action.
2. Action-coupled naturalization identifies a physical cause for relevant wrist, finger, posture, gaze, or fabric/hijab adjustments.
3. Naturalization does not introduce independent gestures, random gaze changes, unrelated hand movement, or independent camera motion.
4. Naturalization does not alter hand ownership, product state, action timing, or immutable bridge references.
5. Naturalization does not cause the target reference state to be reached prematurely.
6. Naturalization preserves continuity across reference-state transitions.
7. The prompt must not rely on generic wording such as “move naturally” as the sole naturalization instruction.

Example compliant pattern:

    PRIMARY ACTION:
    Creator brings the moisturizer closer to camera.

    ACTION-COUPLED NATURALIZATION:
    Wrist rotates slightly to preserve label visibility, fingers adjust pressure to maintain grip, and the shoulder follows the reach subtly as a physical consequence of the movement.

Example failure:

    NATURALIZATION:
    Move naturally, blink, look around, and make small random movements.

This fails because it introduces unconstrained motion without causal ownership and may interfere with reference continuity.

Naturalization validation must be performed together with action-beat, product-causality, gaze, camera, and reference-state validation.


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


## Voice Script Spoken Naturalization Regression

Voice Script must preserve canonical dialogue while adding a separate spoken-delivery layer for technical terms, mixed-language terminology, acronyms, and non-obvious brand/product names.

Example input:
- Product fact: contains ceramide complex
- Supported benefit: helps support the skin barrier
- Audience/context: Indonesian beauty/skincare
- Creator language: Indonesian with established beauty terminology

Expected behavior:
- Canonical dialogue may retain "ceramide complex" and "skin barrier" when natural for the selected creator and audience.
- The engine must not silently replace established niche terminology with formal Indonesian solely to avoid English.
- Pronunciation guidance, when needed, is stored as delivery metadata and does not mutate canonical dialogue.
- Technical terms should normally appear inside a conversational sentence rather than as isolated marketing keywords.
- Mixed Indonesian-English terminology must not be inserted merely to make the script sound premium or persuasive.
- Ambiguous acronyms and non-obvious brand/product names require pronunciation treatment when needed.

Example compliant pattern:

    CANONICAL DIALOGUE:
    "Yang aku suka dari ini, ada ceramide complex-nya,
    jadi bantu jaga skin barrier."

    SPOKEN DELIVERY:
    - ceramide complex: natural English pronunciation
    - skin barrier: natural English pronunciation
    - emphasis: restrained
    - context: embedded in Indonesian sentence

Example failure:

    CANONICAL DIALOGUE:
    "Ceramide complex. Skin barrier. Lightweight texture."

This should be flagged as NEEDS_REFINEMENT unless the storyboard explicitly calls for fragmented delivery.

Acceptance:
1. Canonical dialogue remains exact and factually supported.
2. Pronunciation notes do not replace or alter canonical dialogue.
3. Established niche terminology may remain in its original language when contextually natural.
4. Forced Indonesian phonetics and exaggerated foreign accents are avoided.
5. Unnecessary English marketing language is not introduced.
6. Pronunciation review is triggered only when pronunciation, acronym treatment, brand/product naming, or TTS handling is materially ambiguous.
7. Spoken naturalization does not invent personal experience, outcomes, or claims.


## Voice Performance Plan Regression

The Voice Script Engine must produce a structured performance layer without mutating canonical dialogue.

Acceptance:
1. Canonical dialogue remains byte-for-byte equivalent to the approved spoken wording unless the campaign explicitly revises the script.
2. Performance metadata may define pace, phrase grouping, pauses, emphasis, pitch variation, breath opportunities, emotional intensity, articulation, and delivery context when materially useful.
3. Performance direction must not rely on "sound human" as the sole instruction.
4. Emphasis must be sparse and intentional rather than equal across all words.
5. Pause and breathing instructions must support semantic boundaries and timing rather than occur mechanically at every punctuation mark.
6. Standard beauty UGC defaults toward conversational warmth and restrained enthusiasm unless creator or scene direction requires otherwise.
7. Voice Profile characteristics are kept separate from per-line Voice Performance instructions.
8. A real person's or celebrity's name must not be converted into a voice-cloning instruction; authorized voice assets are represented by their permitted reference/identifier.
9. Performance timing must fit the owning scene and must remain compatible with Video Prompt dialogue synchronization.
10. NEEDS_REFINEMENT is advisory for monotone, uniform emphasis, excessive pauses, exaggerated enthusiasm, announcer delivery, conspicuous breathing, or other unnatural performance direction.

Example compliant pattern:

    CANONICAL DIALOGUE:
    "Yang aku suka dari ini, ada ceramide complex-nya, jadi bantu jaga skin barrier."

    VOICE PERFORMANCE:
    - delivery: conversational UGC
    - pace: conversational, slightly relaxed
    - phrase grouping: three semantic phrases
    - emphasis: restrained emphasis on "ceramide complex" and "skin barrier"
    - pauses: short semantic pauses, not every comma
    - pitch: moderate natural variation
    - warmth: medium
    - enthusiasm: restrained
    - breath: subtle opportunity at a natural phrase boundary

Example failure:

    VOICE PERFORMANCE:
    - every word equally emphasized
    - fixed pitch
    - maximum excitement
    - audible inhale after every phrase
    - "sound human"

This should be flagged as NEEDS_REFINEMENT.

## Voice Generation Integration Regression

When Video Prompt contains spoken content, it must carry the validated Voice Script into video execution without making Video Prompt its own source of truth.

Acceptance:
1. DIALOGUE SYNC contains the exact canonical dialogue from Voice Script.
2. DIALOGUE SYNC contains a VOICE GENERATION REFERENCE when the provider can generate speech or when voice-generation timing must be synchronized.
3. VOICE GENERATION REFERENCE includes the applicable authorized voice profile/reference, delivery, pace, phrase grouping when defined, emphasis, pitch/rhythm when defined, pause/breathing when defined, pronunciation when defined, and on-camera/voice-over context.
4. Voice Generation Reference is derived from the current validated Voice Script and Voice Performance Plan, not independently invented by Video Prompt.
5. Video Prompt does not rewrite, paraphrase, translate, shorten, expand, or alter canonical dialogue.
6. If audio is generated externally, the same Voice Generation Reference remains the synchronization contract for the audio asset.
7. If Voice Script or Voice Performance changes, affected Video Prompt artifacts become STALE and must be revalidated.
8. Voice identity uses only an authorized voice profile/reference; a real person's or celebrity's name must not become a cloning instruction.
9. Voice-generation timing must fit the exact generation segment and remain synchronized with mouth visibility, action, gaze, expression, and camera behavior.

Example compliant pattern:

    DIALOGUE SYNC
    Exact dialogue:
    "Kalau penasaran, cek di keranjang kuning."

    Timing:
    26.0–29.4

    VOICE GENERATION REFERENCE
    - authorized voice profile/reference
    - warm, clear conversational UGC delivery
    - natural conversational pace
    - restrained emphasis on "keranjang kuning"
    - natural Indonesian pronunciation
    - subtle semantic pauses
    - friendly, non-aggressive closing delivery
    - on-camera context

Example failure:

    DIALOGUE SYNC
    Exact dialogue: "Kalau penasaran, cek di keranjang kuning."
    Delivery: sound human

This fails because the Video Prompt lacks the structured Voice Generation Reference required to carry the validated voice performance into generation.
