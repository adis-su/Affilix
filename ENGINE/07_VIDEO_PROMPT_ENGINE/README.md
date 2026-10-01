# Affilix — Video Prompt Engine

## Purpose

The Video Prompt Engine converts the completed storyboard, visual scene specification, and canonical Voice Script into production-ready motion instructions for video generation.

It is the final prompt-integration layer before video generation. It explains how reference states change through physical action and how spoken dialogue synchronizes with that action.

The Video Prompt Engine does not own spoken wording. **Voice Script owns the exact spoken content and delivery direction.** Video Prompt owns the visual synchronization of that canonical voice content with action, gaze, expression, product interaction, and camera behavior.

## Inputs

- Completed storyboard
- Completed Visual Prompt for the applicable scene
- Completed Voice Script when spoken content exists
- Creator identity
- Product identity
- Pose and expression
- Product interaction
- Environment
- Camera composition
- Lighting
- Dialogue timing and delivery from Voice Script
- Creative scene duration
- Provider capability profile
- Generation segment plan
- Previous and next scene continuity requirements
- Canonical reference graph and immutable bridge references

## Canonical Dependency

For video output, the downstream dependency is:

    STORYBOARD
        │
        ├──→ VISUAL PROMPT
        │
        └──→ VOICE SCRIPT
                  │
                  ↓
            VIDEO PROMPT
                  ↓
           VIDEO GENERATION

Storyboard remains the canonical source for scene intent, action choreography, and creative timing.

Visual Prompt provides the canonical frozen visual state/reference for the applicable scene.

Voice Script provides the canonical spoken wording, speaker, delivery, and speech timing.

Video Prompt integrates these sources. It must not create an independent competing version of the dialogue.

## Provider Duration Policy

The current provider supports exactly:

- 4 seconds
- 6 seconds
- 8 seconds
- 10 seconds

Every generated clip must use one of these durations.

If a campaign is longer than 10 seconds, Affilix uses multiple generation segments. The assembled duration must remain exactly equal to the requested creative duration.

Examples:

    12s → 6s + 6s
    14s → 6s + 8s
    18s → 8s + 10s
    20s → 10s + 10s

If the requested final duration cannot be composed exactly, mark:

    duration_feasibility: BLOCKED

Never silently round, truncate, extend, or replace the requested duration.

## Motion Construction

Build each transition from:

    START REFERENCE
    +
    TRIGGER / INTENTION
    +
    ACTION BEATS
    +
    DIALOGUE SYNC when applicable
    +
    SECONDARY NATURAL MOTION
    +
    CAMERA BEHAVIOR
    +
    END REFERENCE

Every visible state change must have a physically plausible cause.

Product interaction must preserve physical causality. The product must not drift, teleport, duplicate, or morph without an explicit physical action.

Controlled micro-motion may include breathing, blinking, subtle weight shifting, posture adjustment, grip adjustment, small head movement, restrained expression changes, and realistic fabric/hijab response.

Do not use "move naturally" as the only motion instruction.

## Dialogue Synchronization

When the Voice Script contains spoken content, every affected Video Prompt must include a dedicated DIALOGUE SYNC section.

The section must identify:

- Speaker
- Exact dialogue from the canonical Voice Script
- Start timing
- End timing
- Delivery
- Lip-sync requirement
- Emotional intent
- Action/dialogue relationship

Example structure:

    DIALOGUE SYNC
    Speaker: Creator

    Exact dialogue:
    "[exact Voice Script dialogue]"

    Timing:
    - [start]–[end]

    Delivery:
    [canonical delivery direction]

    Lip-sync requirement:
    Accurate lip synchronization with the exact dialogue.

    Emotional intent:
    [canonical emotional intent]

    Action/dialogue relationship:
    [how speech aligns with the storyboard action and product interaction]

The exact dialogue must be copied from the current validated Voice Script, not rewritten independently by the Video Prompt Engine.

If a scene has no spoken content:

    DIALOGUE SYNC
    NONE

When dialogue crosses a generation-segment boundary, preserve the same canonical dialogue sequence and use the immutable bridge reference as the visual continuity anchor. Do not duplicate, omit, or rewrite dialogue merely because a technical segment boundary exists.

## Output Contract

The final Video Prompt must be one standalone Markdown code block.

Use this canonical order:

    VIDEO PROMPT

    SCENE
    [scene identity and purpose]

    START REFERENCE
    [canonical starting reference state]

    ACTION BEATS
    [ordered physical action beats]

    PRIMARY ACTION
    [main action causing the state change]

    SECONDARY NATURAL MOTION
    [bounded micro-motion]

    PRODUCT INTERACTION
    [physically causal product interaction]

    GAZE & EXPRESSION
    [gaze and expression changes]

    DIALOGUE SYNC
    [synchronized canonical Voice Script content, or NONE]

    CAMERA BEHAVIOR
    [controlled camera behavior]

    TARGET REFERENCE
    [canonical target reference state]

    END STATE
    [resulting visual state]

    CONTINUITY
    [identity, product, wardrobe, environment, lighting, spatial and bridge continuity]

    NEGATIVE MOTION CONSTRAINTS
    [video-specific failure constraints]

    FINAL VIDEO GENERATION INSTRUCTION
    [generate the continuous physically plausible transition]

Do not split one Video Prompt across multiple code blocks. Generation-segment metadata stays outside the code block.

## Voice-Video Synchronization Rules

The Video Prompt must synchronize:

- exact canonical dialogue
- mouth visibility and lip movement
- creator gaze
- facial expression
- hand movement
- product demonstration
- camera movement
- scene transitions

Dialogue should not be scheduled over an action that materially obscures the mouth or makes the spoken content visually implausible unless the storyboard intentionally requires that behavior.

The Voice Script remains the wording authority. If wording changes, the Video Prompt becomes STALE and must be regenerated or revalidated.

If dialogue timing changes but visual action does not, revalidate the affected Video Prompt timing before production.

## Continuity

Across adjacent scenes and technical segments preserve:

- creator identity
- outfit
- hijab styling
- product identity and state
- environment
- lighting
- spatial direction
- narrative time
- reference-state continuity
- immutable bridge references

A shared bridge reference must remain identical at both sides of the boundary.

If a bridge reference changes, invalidate the transitions and downstream video segments that depend on it.

## Validation

Before handoff verify:

- storyboard dependency is current
- applicable Visual Prompt is current
- Voice Script is current when spoken content exists
- every spoken dialogue string exactly matches the canonical Voice Script
- dialogue timing fits the storyboard and scene duration
- lip-sync requirements are present when dialogue exists
- every generation duration is 4/6/8/10 seconds
- segment durations sum exactly to requested final duration
- segment boundaries follow coherent creative beats
- start/end references are canonical
- bridge references are immutable and consistent
- creator and product remain consistent
- physical motion is plausible
- product interaction is causally grounded
- camera behavior is controlled
- no filler or unexplained motion exists
- no stale upstream dependency is consumed

## Handoff

The Video Prompt becomes the technical motion specification for video generation.

The dependency chain is:

    Storyboard + Visual Prompt + Voice Script
                        ↓
                  Video Prompt
                        ↓
                Video Generation
                        ↓
              Production Output

Storyboard remains canonical for temporal intent. Visual Prompt remains canonical for static appearance. Voice Script remains canonical for spoken content and delivery.
