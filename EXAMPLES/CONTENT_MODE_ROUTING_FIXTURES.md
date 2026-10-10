# Affilix — Content Mode Routing Regression Fixtures

## Purpose

These fixtures cover mode selection, cross-mode isolation, and Quote Content stage routing through the current mode-specific contracts. They are behavioral test specifications; their presence does not claim end-to-end execution. For production-specific cases, use `EXAMPLES/QUOTE_CONTENT_REGRESSION_MATRIX.md`.

Canonical routing contract: `ENGINE/CONTENT_MODE_ROUTING_CONTRACT.md`.

## CM-001 — Explicit UGC Request Preserves Existing Intake

**Input**

- User invokes `/Affilix` and explicitly asks to make a product affiliate video.
- User supplies a product name and product reference.

**Expected**

- `run.content_mode = UGC_AFFILIATE`
- Do not show the mode selector again.
- Require existing UGC Product Intake and campaign requirements.
- Product reference research, claims validation, creator resolution, and existing downstream contracts remain in force.
- No UGC stage or validation is removed by the routing change.

**Fail if**

- Product intake is bypassed.
- The run is silently classified as `QUOTE_CONTENT`.
- Existing UGC requirements are weakened.

## CM-002 — Ambiguous New Run Requires Mode Selection

**Input**

- User invokes `/Affilix` without a product brief or explicit content mode.

**Expected**

- Show the Content Mode Selector.
- Do not inherit content mode or artifacts from another run.
- Do not begin product research until `UGC_AFFILIATE` is selected or explicitly established by the user.

**Fail if**

- The runtime silently assumes UGC mode.
- Product, creator, storyboard, or prompt state leaks from another run.

## CM-003 — Quote Content Does Not Require a Product

**Input**

- User selects `QUOTE_CONTENT`.
- User provides a topic about the emotional load of household responsibilities and a target audience of wives and mothers.
- No product name or product URL is supplied.

**Expected**

- `run.content_mode = QUOTE_CONTENT`
- Stage 01 accepts the editorial brief without requesting product identity.
- Preserve explicit and inferred provenance.
- Do not create product facts, product claims, product demonstrations, or fake product references.
- Editorial context may proceed only through implemented mode-specific contracts.

**Fail if**

- Product fields are treated as mandatory.
- The runtime fabricates a product to satisfy the UGC schema.

## CM-004 — Unsupported Quote Engine Must Block

**Input**

- Quote Content Stage 01 and Stage 02 are complete.
- The next required mode-specific stage has no implemented Quote Content contract.

**Expected**

- Block the affected stage with `QUOTE_CONTENT_ENGINE_NOT_IMPLEMENTED`.
- Preserve completed upstream artifacts.
- Do not invoke a product-centered engine as a fallback.
- Do not claim that the production output is complete.

**Fail if**

- UGC product-proof scoring runs on an editorial quote brief.
- A complete production output is claimed without required current assets.

## CM-005 — Content Mode Revision Invalidates Cross-Mode State

**Input**

- An active `UGC_AFFILIATE` run has completed stages and downstream assets.
- The user changes the run to `QUOTE_CONTENT`.

**Expected**

- Treat the mode change as a new isolated run state or invalidate every mode-dependent artifact.
- Do not reuse product, claims, creator, strategy, storyboard, visual, voice, video, or production artifacts unless independently regenerated and validated under the new mode.
- Record the mode and source repository commit for traceability.

**Fail if**

- UGC artifacts remain marked current in the Quote Content run.
- The runtime silently mutates the old run's mode while preserving incompatible artifacts.

## CM-006 — Canonical Stage Registry Remains Stable

**Input**

- Runtime resolves a stage for either supported mode.

**Expected**

- Stage IDs remain 01–10 and resolve only through `ENGINE/WORKFLOW.md`.
- Mode-specific routing controls applicability, skips, and blockers.
- Engine directory prefixes are never used as stage IDs.
- `/next` remains progression only, never approval.

**Fail if**

- A new numbered stage is introduced for mode selection.
- Stage order is inferred from folder names.
- A skip is treated as generated output or approval.

## Routing Fixture Acceptance

Phase 01 is accepted when the mode contract, entrypoint, Skill, canonical workflow, runtime state contract, Brief Analyzer, and repository loader agree on:

- the two registered mode values,
- isolated mode-specific intake,
- no product requirement in Quote Content,
- unchanged canonical ten-stage IDs,
- explicit conditional dependencies and blockers,
- no cross-mode artifact reuse,
- preserved UGC compatibility.

Phase 01 does not certify Quote Content end-to-end production. That depends on Phase 02 strategy and Phase 03 production implementation.


## CM-007 — Quote Content Editorial Context Does Not Require Product

**Input**

- User selects `QUOTE_CONTENT`.
- Topic: emotional load of household responsibilities.
- Audience context: wives and mothers.
- No product identity or product reference is supplied.

**Expected**

- Stage 02 resolves editorial niche, audience context, topic context, and relevant sensitivity flags.
- Product niche, product type, and product behavior are `NOT_APPLICABLE`, not invented.
- Preserve source provenance and unknown fields.

**Fail if**

- The product-oriented context loader requests a product.
- Demographic, psychological, or personal facts are inferred without evidence.

## CM-008 — Editorial Strategy Selects One Pillar and One Format

**Input**

- A validated Quote Content brief about feeling unseen in household responsibilities.
- No explicit format preference.

**Expected**

- Stage 04 selects one primary editorial pillar and one primary format from the Quote Content registries.
- Platform is recorded separately from format.
- One primary message and takeaway are defined.
- No product proof scoring or product claims are generated.

**Fail if**

- More than one primary pillar or format is selected.
- `FACEBOOK_PRO` is treated as a content format.
- The strategy invents a product, personal testimony, or audience demographic.

## CM-009 — Quote Content Hook Preserves Editorial Strategy

**Input**

- Current Stage 04 strategy selects `PILLAR_01` and `RELATABLE_STORY_REELS`.

**Expected**

- Stage 05 hook establishes a recognizable situation or story trigger.
- Hook records pillar, format, and primary-message connections.
- Language remains specific without claiming every husband or wife behaves the same way.

**Fail if**

- Hook uses generic engagement bait unrelated to the selected strategy.
- Hook fabricates lived experience or a real quote attribution.
- Hook normalizes abuse or coercion as ordinary communication trouble.

## CM-010 — Static Quote Image Has Explicit Stage Skips

**Input**

- Current Stage 04 strategy selects `QUOTE_IMAGE`.

**Expected**

- Stage 05 may be `SKIPPED` only when strategy explicitly permits it and records a reason.
- Stage 06, Stage 08, and Stage 09 are marked `SKIPPED` with `STATIC_IMAGE_FORMAT` where their outputs are not applicable.
- Stage 07 remains required for the image prompt, and Stage 10 remains blocked until Quote Content output assembly is implemented.

**Fail if**

- A skipped stage is represented as generated output.
- Video prompts or voice scripts are invented for a static-only deliverable.
- UGC Production Output Template is used as a fallback.

## CM-011 — Batch Pillar Mix Is Not an Individual Post Constraint

**Input**

- A batch plan uses the initial editorial mix 40% `PILLAR_01`, 20% `PILLAR_02`, 40% `PILLAR_03`.
- One individual post has a clear fit for `PILLAR_02`.

**Expected**

- The individual post is assigned according to topic/audience/message fit.
- The percentages guide batch-level planning only.
- No algorithmic-performance claim is made without actual analytics.

**Fail if**

- Every individual post is forced to meet batch percentages.
- The mix is described as a proven platform algorithm requirement.


## CM-012 — Quote Content Storyboard Preserves Editorial Format

**Input**

- `QUOTE_CONTENT` strategy selects `RELATABLE_STORY_REELS`.
- Current hook identifies a concrete, non-sensitive household situation.

**Expected**

- Stage 06 uses `QUOTE_CONTENT_STORYBOARD_CONTRACT.md`.
- Each scene expresses trigger → intention → action → resulting state.
- No product demo, invented testimony, or generic UGC product sequence is introduced.
- Reference trajectory and immutable bridge IDs are preserved.

**Fail if**

- The storyboard invokes product-proof requirements without a product brief.
- A changed bridge reference is not propagated to dependent transitions.

## CM-013 — Quote Content Visual Prompt Coverage

**Input**

- A video storyboard declares multiple reference states across scenes, including one shared bridge reference.

**Expected**

- Stage 07 emits exactly one static image prompt per declared reference state.
- Every prompt describes one frozen state.
- Shared bridge references use the same ID and version.

**Fail if**

- References are collapsed into one image prompt per scene.
- Image prompts contain temporal motion instructions or invent visual story beats.

## CM-014 — Quote Content Video Prompt Count and Duration

**Input**

- A video storyboard has N scenes and a requested final duration that is exactly composable from 4s, 6s, 8s, and 10s segments.

**Expected**

- Stage 09 emits exactly N standalone user-facing Video Prompt code blocks.
- Generation segment durations sum exactly to the requested final duration.
- Segment count and reference count do not change the Video Prompt count.
- Dialogue is synchronized only when the current audio mode requires it.

**Fail if**

- Video Prompt count differs from scene count.
- Duration is rounded, extended, truncated, or padded with filler.
- Product-centered UGC actions are inserted into an editorial-only story.

## CM-015 — Quote Content Voice Is Conditional and Non-Fabricated

**Input**

- A Quote Content brief requests `VOICE_OVER` for a mini-story, or explicitly selects `NO_SPOKEN_VOICE`.

**Expected**

- Spoken mode uses the canonical Voice Script contract and storyboard anchors.
- No-spoken mode skips Stage 08 with `NO_SPOKEN_VOICE_REQUIRED` when permitted.
- First-person testimony is not fabricated and video prompts do not rewrite canonical dialogue.

**Fail if**

- A voice script is created for a static quote image.
- Dialogue invents lived experience, quote attribution, or unsupported factual claims.

## CM-016 — Quote Content Production Output Never Falls Back to UGC

**Input**

- A valid `QUOTE_CONTENT` static image or video run has current applicable upstream artifacts.

**Expected**

- Stage 10 assembles with `ENGINE/QUOTE_CONTENT_PRODUCTION_OUTPUT_CONTRACT.md`.
- Explicitly skipped stages preserve their reasons and are not represented as generated artifacts.
- Output preserves platform, format, pillar, message, provenance, prompt counts, and exact duration where applicable.

**Fail if**

- UGC production output template is used.
- A required artifact is missing/stale or a validation blocker is suppressed.


## Phase 02–04 Acceptance

- Phase 02 contracts: editorial context, strategy, and hook contracts are present and mode-dispatched.
- Phase 03 contracts: storyboard, visual prompt, conditional voice, video prompt, and Quote Content Production Output contracts are present and mode-dispatched.
- Phase 04 regression: see `EXAMPLES/QUOTE_CONTENT_REGRESSION_MATRIX.md`. End-to-end acceptance remains NOT RUN until runtime cases are executed and observed results are recorded.


## CM-017 — Quote Content Recommends a Subpillar Under the Primary Pillar

**Input**

- A validated Quote Content brief is ready for Stage 04.
- The user has not manually selected a subpillar.

**Expected**

- Stage 04 selects exactly one primary pillar and exactly one matching subpillar from `ENGINE/03_CONTENT_STRATEGY/QUOTE_CONTENT_SUBPILLAR_REGISTRY.md`.
- Affilix states the recommended subpillar and a concise fit rationale.
- A concrete content angle is defined separately from the subpillar.
- The strategy artifact records subpillar ID/name/rationale and the angle's editorial safety validation.

**Fail if**

- No subpillar is recorded.
- The subpillar belongs to a different primary pillar.
- Subpillar is treated as the final hook or script.
- A batch-level pillar percentage overrides the topic's actual fit.

## CM-018 — Subpillar Angle Does Not Blame or Corner People

**Input**

- A selected subpillar is developed into a content angle about household or couple dynamics.

**Expected**

- The angle focuses on a situation, need, action, or impact rather than a person's inherent character.
- It avoids universal gender/family-role claims, humiliation, shame, fabricated testimony, and unsupported claims.
- It does not force equal responsibility when the facts do not support it.
- Explicit abuse, threats, coercive control, or fear are not reframed as ordinary communication problems.
- Any failed angle is rewritten and revalidated before Stage 04 is completed.

**Fail if**

- A person or group is stereotyped, blamed, or shamed as the default framing.
- Unsafe dynamics are normalized.
- The stage is marked completed while an editorial safety issue remains unresolved.

## CM-019 — Subpillar Revision Invalidates Dependent Outputs

**Input**

- A completed strategy's primary subpillar or content angle changes.

**Expected**

- Stage 04 is revised and revalidated.
- Dependent Hook, Storyboard, Visual Prompt, Voice Script, Video Prompt, and Production Output artifacts are marked stale as applicable.
- The workflow waits for `/next` after the revision and does not advance automatically.

**Fail if**

- Downstream assets remain marked current after a material strategy change.
- Revision silently triggers the next stage.
