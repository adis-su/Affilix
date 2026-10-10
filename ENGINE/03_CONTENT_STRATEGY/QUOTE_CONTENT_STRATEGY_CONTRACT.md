# Affilix Quote Content Strategy Contract

## Canonical Stage Identity

- Canonical workflow stage: Stage 04 — Content Strategy
- Implementation directory: `ENGINE/03_CONTENT_STRATEGY/`
- Content mode: `QUOTE_CONTENT`
- Canonical stage registry: `ENGINE/WORKFLOW.md`

This contract is the mode-specific editorial strategy authority. It does not create a second workflow, new numbered stage, or product-centered fallback.

## Purpose

Convert a validated editorial brief and Stage 02 editorial context into one coherent content strategy that can guide Hook and downstream production. The strategy chooses the audience-facing idea, pillar, format, emotional movement, and takeaway. It does not write a full scene-by-scene storyboard or image/video prompt.

## Required Inputs

- Stage 01 editorial brief with source/provenance
- Stage 02 editorial context
- Publishing platform and objective when known
- Audience or audience context
- Topic/theme or relatable situation
- Intended emotional response and takeaway when supplied
- User constraints and any explicit format preference

Stage 03 Creator is optional. If the selected format requires a visible on-screen persona, a valid Creator artifact becomes a dependency. Do not invent a repository creator or personal experience.

## Editorial Pillar Registry

### PILLAR_01 — CURHAT_RELATE_RUMAH_TANGGA

- Purpose: make the audience recognize an everyday household or marital experience.
- Audience response: “Kok sama banget dengan yang aku alami?”
- Suitable topics: invisible household workload, mental load, feeling unheard, expectations, small recurring misunderstandings, everyday emotional labor.
- Emotional approach: recognition and specificity before advice.
- Avoid: universal claims about husbands or wives, humiliation, rage-bait, fabricated first-person testimony, and treating coercion or abuse as a normal disagreement.

### PILLAR_02 — SELF_HEALING_ISTRI_IBU

- Purpose: encourage self-reflection, self-compassion, and awareness of identity beyond family roles.
- Audience response: “Aku juga perlu memperhatikan diriku sendiri.”
- Suitable topics: rest without guilt, asking for support, boundaries, identity, emotional needs, small acts of self-care.
- Emotional approach: compassionate, grounded, non-clinical reflection.
- Avoid: diagnosing the audience, promising healing, implying that positive thinking fixes structural or unsafe situations, or shaming people who cannot simply change their circumstances.

### PILLAR_03 — RELASI_KOMUNIKASI_PASANGAN

- Purpose: offer a useful way to understand communication, conflict, emotional needs, and shared responsibility.
- Audience response: “Ternyata ada cara lain untuk memahami pasangan.”
- Suitable topics: asking clearly, listening, repair after conflict, division of labor, assumptions, appreciation, and respectful boundaries.
- Emotional approach: specific and balanced without forcing false equivalence.
- Avoid: presenting abuse, threats, coercive control, or fear as ordinary communication issues. Prioritize safety and support where such dynamics are explicit.

### Subpillar Selection

The canonical subpillar catalogue and exploration rules live in `ENGINE/03_CONTENT_STRATEGY/QUOTE_CONTENT_SUBPILLAR_REGISTRY.md`. Stage 02 owns user-facing pillar/subpillar selection and the `Ganti Subpilar` action. Stage 04 consumes the validated Stage 02 pillar/subpillar, chooses the content format, and defines the content angle, editorial message, emotional strategy, and takeaway. Do not display a duplicate subpillar picker in Stage 04 unless the user explicitly requests a revision. Stage 04 records the consumed Stage 02 subpillar ID/name and provenance alongside the angle and editorial safety validation. A refresh in Stage 02 alone does not invalidate Stage 04 until the user selects a different subpillar; changing the selected pillar/subpillar invalidates Stage 04 and affected downstream artifacts.
### Editorial Mix

The initial batch-planning hypothesis is:

- PILLAR_01: 40%
- PILLAR_02: 20%
- PILLAR_03: 40%

These percentages apply to a planned batch, not every individual post. They are an editable editorial hypothesis, not a claim about platform-algorithm preference. Rebalance only using actual performance evidence and editorial goals; do not fabricate performance findings.

## Format Registry

Platform and format are separate dimensions. `FACEBOOK_PRO` is a platform value, not a content format.

### QUOTE_IMAGE

- Output: one static editorial quote/statement image plus caption/publishing copy when requested.
- Best for: a concise, original, self-contained thought with one emotional or practical takeaway.
- Requirements: one primary message, readable text hierarchy, sufficient negative space, intentional typography and contrast, no fabricated quote attribution.
- Storyboard: skipped with reason `STATIC_IMAGE_FORMAT`.
- Hook: skipped only if the chosen image concept itself supplies the opening statement and the format contract marks Hook not required.
- Voice and Video Prompt: skipped with reason `STATIC_IMAGE_FORMAT`.

### CINEMATIC_QUOTE_REELS

- Output: short-form video built around an original quote or reflective statement, with visual atmosphere and readable text timing.
- Best for: self-reflection and emotional resonance where imagery supports rather than distracts from the statement.
- Requirements: one primary statement, a clear visual progression, legible text safe areas, controlled camera behavior, no arbitrary stock emotion.
- Storyboard and Video Prompt: required.
- Voice Script: conditional on requested spoken narration or external dialogue.

### RELATABLE_STORY_REELS

- Output: a short relatable situation with a recognizable trigger, emotional development, and grounded takeaway.
- Best for: everyday household or relationship moments that benefit from a small narrative arc.
- Requirements: concrete situation, clear trigger/intention/action/result, plausible behavior, one central emotional turn, and no unsupported claim that the story is a real personal testimony.
- Storyboard and Video Prompt: required.
- Voice Script: conditional on selected audio mode and user requirements.

### POV_RELATIONSHIP_REELS

- Output: a relationship scenario framed through a clear point of view, followed by a grounded perspective or communication insight.
- Best for: showing the difference between an assumption, an action, and its interpersonal consequence.
- Requirements: identify the POV, keep actions causally coherent, avoid caricatures and gender stereotypes, distinguish fictionalized scenarios from real testimony.
- Storyboard and Video Prompt: required.
- Voice Script: conditional on selected audio mode and user requirements.

### MINI_STORYTELLING_REELS

- Output: a slightly fuller short-form narrative with setup, turning point, and resolution or open reflection.
- Best for: topics that need more context than a quote or one-beat relatable Reel.
- Requirements: one narrative spine, a motivated turning point, no filler beats, and exact requested duration.
- Availability: supported as a strategy classification; downstream production must still satisfy the current Storyboard/Visual/Voice/Video contracts. If an applicable downstream contract is not mode-ready, block rather than fallback.

## Default Video Delivery: Direct-to-Camera Talking Head

For every video format in `QUOTE_CONTENT`, the default visual delivery is `DIRECT_TO_CAMERA_TALKING_HEAD`: the creator addresses the camera lens and delivers the message as spoken, conversational content. This is the delivery format, while the selected editorial format still determines the narrative mechanism. Do not default to cinematic montage, unrelated B-roll, acted scenes between multiple characters, or quote-only visuals as a substitute for the creator speaking to camera.

- `CINEMATIC_QUOTE_REELS`: the creator speaks the central reflection directly to camera; use restrained lighting/framing and subtle visual development rather than replacing speech with a montage.
- `RELATABLE_STORY_REELS`: the creator recounts a relatable situation directly to camera, with the trigger and emotional turn carried primarily by spoken delivery and motivated expression/gestures.
- `POV_RELATIONSHIP_REELS`: the creator explains the POV directly to camera; do not stage a second-person scene unless the user explicitly requests that treatment.
- `MINI_STORYTELLING_REELS`: the creator tells the compact story directly to camera, with setup, turning point, and takeaway expressed in the spoken narrative and controlled performance.

Default composition is vertical 9:16, medium close-up or close-up, lens-level eye contact, clean and relevant background, and stable framing with only motivated subtle reframing. Use natural but bounded breathing, blinking, posture/weight shifts, small head movements, restrained facial changes, and purposeful hand gestures. The creator should visibly speak when the resolved audio mode is `SPOKEN_ON_CAMERA`; spoken wording and mouth movement must synchronize to the canonical Stage 08 script. Subtitles/captions, if requested or part of the platform treatment, must match the spoken words exactly. An explicit user choice of `VOICE_OVER` or `NO_SPOKEN_VOICE` overrides native on-camera speech but does not silently change the visual concept; retain direct-to-camera presence unless the user explicitly requests another visual treatment.

## Strategy Selection

1. Validate the brief and editorial context. Preserve unknowns rather than inventing audience facts.
2. Select exactly one primary pillar using the topic, audience need, and intended takeaway. Record secondary pillar only when it materially contributes.
3. Select one primary format based on message complexity, emotional arc, platform, and requested output. An explicit user format preference takes precedence when feasible.
4. Keep platform separate from format.
5. Define one primary message and one clear takeaway.
6. Define the intended emotional movement (for example: recognition → reflection, or tension → clearer understanding) without manipulating the audience with shame or false urgency.
7. Define a story arc only when the selected format needs one.
8. Define CTA only when it serves the publishing objective. Do not force “comment/share/follow” into every post.
9. Validate that the concept is original or has clear source/permission. Never attribute a generated quote to a real person without reliable sourcing.
10. Record provenance for explicit user inputs and model-inferred recommendations.

## Editorial Quality Validation

A strategy is valid only if:

- content mode is `QUOTE_CONTENT`;
- exactly one primary pillar is selected from the registry;
- exactly one primary format is selected from the registry;
- platform and format are separate fields;
- audience and topic are sufficiently defined for a coherent concept;
- exactly one subpillar is selected under the primary pillar and a concrete content angle is defined;
- the content angle passes the subpillar registry's non-blaming editorial safety rules;
- one primary message and takeaway are present;
- format-specific dependencies and skipped stages are recorded;
- no product claim, fake testimonial, fabricated quote attribution, or unsupported performance claim is introduced;
- emotional framing does not normalize abuse, coercion, or unsafe dynamics;
- downstream output is consistent with the selected pillar, format, audience, and message.

If a required field is materially missing, return `BLOCKED` and ask only for the minimum clarification. Otherwise retain `UNKNOWN` for non-critical fields and proceed.

## Runtime Output Shape

```yaml
stage: 04_CONTENT_STRATEGY
content_mode: QUOTE_CONTENT
status: COMPLETED | BLOCKED
campaign_objective:
  primary:
  secondary:
  desired_audience_action:
platform:
pillar:
  id:
  name:
  rationale:
secondary_pillar:
format:
  id:
  name:
  output_type:
  requirements: []
  delivery_mode: DIRECT_TO_CAMERA_TALKING_HEAD | USER_OVERRIDE
  rationale:
audience:
  target:
  context:
  core_need:
  awareness_level:
editorial_topic:
subpillar:
  id:
  name:
  rationale:
content_angle:
editorial_safety_validation:
  status:
  issues: []
  corrections: []
primary_message:
takeaway:
emotional_strategy:
  intended_response:
  emotional_movement: []
story_arc: []
hook_direction:
caption_direction:
cta_strategy:
editorial_mix_note:
  applies_to_batch_planning_only: true
source_provenance: []
unresolved_requirements: []
decision_queue: []
source_artifacts: []
source_commit_sha:
```

For static `QUOTE_IMAGE`, storyboard, voice, and video fields must be marked `SKIPPED` with a reason in run state, not fabricated as empty generated artifacts.

## Invalidation

Changes to editorial topic, audience, platform when format-sensitive, primary pillar, primary format, primary message, or takeaway invalidate all dependent downstream artifacts. Changes to batch-level pillar percentages affect batch planning, not an already validated single post unless the user explicitly requests rebalancing.

## Handoff

The validated artifact is consumed by the Quote Content Hook contract for formats that require Stage 05. It then follows the canonical workflow and the mode-specific dependencies in `ENGINE/CONTENT_MODE_ROUTING_CONTRACT.md`. Completing this strategy does not imply downstream production is complete.
