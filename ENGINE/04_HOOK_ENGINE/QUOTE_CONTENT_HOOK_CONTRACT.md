# Affilix Quote Content Hook Contract

## Canonical Stage Identity

- Canonical workflow stage: Stage 05 — Hook
- Content mode: `QUOTE_CONTENT`
- Strategy source: `ENGINE/03_CONTENT_STRATEGY/QUOTE_CONTENT_STRATEGY_CONTRACT.md`

## Purpose

Create opening lines or opening visual concepts that earn attention through recognition, curiosity, emotional specificity, or a useful perspective. The hook must serve the selected editorial pillar and format, not distort the underlying message for engagement.

## Required Inputs

- Current validated Stage 04 Quote Content Strategy
- Current Stage 02 editorial context
- Selected pillar and format
- Primary message and takeaway
- Platform and audience context
- Creator artifact only if the selected format requires an on-screen persona
- User constraints and provenance

## Hook Families

Select hook types that fit the concept, not a fixed quota:

- RELATABLE_OBSERVATION: a specific everyday moment the audience may recognize
- INNER_THOUGHT: a restrained articulation of a feeling or conflict
- GENTLE_REFRAME: a perspective shift that does not invalidate the audience's experience
- QUESTION: a focused question with a meaningful answer path
- POV_SETUP: establish the point of view and situation
- STORY_TRIGGER: a concrete event that causes the story to begin
- QUOTE_STATEMENT: a concise original statement suitable for a static quote or cinematic text opening
- CONTRAST: distinguish two interpretations or actions without manufacturing a false binary
- PRACTICAL_INSIGHT: introduce a useful communication or reflection idea

## Format-Specific Opening Requirements

| Format | Required opening behavior |
|---|---|
| `QUOTE_IMAGE` | If Stage 05 is run, create the primary statement that carries the image; otherwise mark Hook skipped with `EDITORIAL_FORMAT_CONTRACT_PERMITS_SKIP`. |
| `CINEMATIC_QUOTE_REELS` | Establish the central statement or emotional question immediately; keep on-screen text readable and synchronized with the visual progression. |
| `RELATABLE_STORY_REELS` | Establish a recognizable situation or trigger before explaining the lesson. |
| `POV_RELATIONSHIP_REELS` | Make the point of view and interpersonal situation clear without caricature. |
| `MINI_STORYTELLING_REELS` | Establish a concrete story trigger that creates a reason for the next beat. |

## Editorial Hook Rules

1. Preserve the selected pillar, format, primary message, and takeaway.
2. Prefer concrete situations and emotionally precise language over generic engagement bait.
3. Do not use false absolutes such as “semua suami”, “semua istri”, or “tidak ada yang pernah” unless the wording is explicitly a character's bounded opinion and is not presented as fact.
4. Do not fabricate a first-person lived experience, confession, testimonial, quotation attribution, or specific real-person event.
5. Do not shame the audience for staying, leaving, struggling, being tired, or needing help.
6. Do not present abuse, coercive control, threats, or fear as a normal communication problem.
7. Do not imply diagnosis, treatment, or guaranteed emotional healing.
8. Do not create false urgency, rage bait, or misleading “secret” framing.
9. A question must be answerable by the selected content, not merely a comment trap.
10. Keep language appropriate to the selected audience and requested platform; use the language of the brief unless the user asks otherwise.

## Candidate Output

Each candidate records:

- `hook_id`
- `hook_type`
- `hook_text_or_visual_concept`
- `opening_trigger`
- `audience_recognition`
- `pillar_connection`
- `format_connection`
- `message_connection`
- `emotional_risk`
- `visual_action` when applicable
- `status: VIABLE | BLOCKED`
- `rationale`
- `provenance`

Return multiple candidates only when they represent materially different approaches. Do not assign pseudo-scientific virality scores or claim that one wording will perform best without actual data.

## Validation

A candidate is `VIABLE` only when:

- it is consistent with the current strategy and editorial context;
- it establishes the selected format's required opening mechanism;
- it has a coherent path to the primary message/takeaway;
- it does not fabricate lived experience, quote attribution, or facts;
- it does not use unsafe, stigmatizing, or manipulative framing;
- any required visual action is executable under the selected format.

If no candidate passes, return `BLOCKED` and preserve the unresolved requirement. Do not silently rewrite the strategy.

## Runtime Output Shape

```yaml
stage: 05_HOOK
content_mode: QUOTE_CONTENT
status: COMPLETED | BLOCKED | SKIPPED
skip_reason:
candidates:
  - hook_id:
    hook_type:
    hook_text_or_visual_concept:
    opening_trigger:
    audience_recognition:
    pillar_connection:
    format_connection:
    message_connection:
    emotional_risk:
    visual_action: []
    status: VIABLE | BLOCKED
    rationale:
    provenance: []
selection:
  selected_hook_id:
  rationale:
unresolved_requirements: []
source_artifacts: []
source_commit_sha:
```

## Invalidation

Any material change to Stage 04 pillar, format, audience, primary message, takeaway, or Stage 02 editorial context invalidates this Hook artifact and affected downstream artifacts.
