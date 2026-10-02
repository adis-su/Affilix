# Affilix — Video Prompt Engine

## Purpose

The Video Prompt Engine converts the completed storyboard, visual scene specification, and canonical Voice Script into production-ready motion instructions for video generation.

It is the final prompt-integration layer before video generation. It explains how reference states change through physical action and how spoken dialogue synchronizes with that action.

The Video Prompt Engine does not own spoken wording. **Voice Script owns the exact spoken content, pronunciation guidance, and Voice Performance Plan.** Video Prompt owns the visual synchronization of that canonical voice content with action, gaze, expression, product interaction, and camera behavior. When the downstream video provider can generate speech, Video Prompt carries a derived **VOICE GENERATION REFERENCE** inside DIALOGUE SYNC so the video generator receives the validated voice-generation inputs without creating a competing voice specification.

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
- Voice Performance Plan from Voice Script
- Pronunciation guidance from Voice Script
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

Video Prompt integrates these sources. It must not create an independent competing version of the dialogue or voice performance. When native voice generation is part of the video provider, the Video Prompt exposes these validated Voice Script fields through DIALOGUE SYNC → VOICE GENERATION REFERENCE.

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

Naturalization is a realism layer, not an independent action layer. It may add bounded micro-motion only when that motion supports the defined action or preserves continuity between canonical reference states.

Action-coupled naturalization should explain the physical cause of relevant micro-motion, for example:

    PRODUCT MOVES CLOSER
        ↓
    wrist rotation + finger pressure adjustment + subtle shoulder response

    PRODUCT IS OPENED
        ↓
    grip correction + finger repositioning caused by lid manipulation

    FINGERTIP CONTACTS PRODUCT
        ↓
    controlled fingertip movement + small wrist adjustment caused by contact

Naturalization must never create a new action, alter an immutable reference state, change product state without physical cause, change hand ownership, invent a gaze target, or introduce unrelated camera movement.

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

    VOICE GENERATION REFERENCE
    - Voice profile: [authorized voice profile/reference only]
    - Delivery: [canonical Voice Performance delivery]
    - Pace: [canonical pace]
    - Phrase grouping: [canonical phrase grouping when defined]
    - Emphasis: [canonical emphasis]
    - Pitch/rhythm: [canonical pitch and rhythm direction when defined]
    - Pause/breathing: [canonical pause and breathing direction when defined]
    - Pronunciation: [canonical pronunciation notes when defined]
    - Context: [on-camera / voice-over / scene context]

    Audio generation rule:
    Use the current validated Voice Script and Voice Performance Plan as the sole source for spoken audio.
    Do not rewrite, paraphrase, translate, shorten, expand, or independently reinterpret the dialogue or delivery.
    If the provider does not generate audio, use the same reference to synchronize the external voice-generation asset.

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
    [bounded baseline human micro-motion]

    ACTION-COUPLED NATURALIZATION
    [micro-motion caused by or supporting the active physical action]

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
- canonical Voice Performance timing/delivery
- pronunciation guidance when defined
- mouth visibility and lip movement
- creator gaze
- facial expression
- hand movement
- product demonstration
- camera movement
- scene transitions

Dialogue should not be scheduled over an action that materially obscures the mouth or makes the spoken content visually implausible unless the storyboard intentionally requires that behavior.

The Voice Script remains the wording, pronunciation, and delivery authority. If wording changes, the Video Prompt becomes STALE and must be regenerated or revalidated.

If dialogue timing changes but visual action does not, revalidate the affected Video Prompt timing before production.


## Generation Segment Motion Contract

When the Video Prompt is materialized into a technical generation segment, the segment must describe a deterministic state transition rather than a compressed scene summary.

Each segment must explicitly define:

- exact segment duration
- start reference and its observable physical state
- ordered action beats with enough detail to establish causality
- immutable bridge reference when the segment participates in a multi-segment transition
- target/end reference and its observable physical state
- product interaction as a physical action chain
- baseline natural micro-motion
- action-coupled naturalization with physical causes
- gaze timing tied to action beats
- expression behavior tied to action beats
- camera behavior tied to the active action, not as an independent generic movement
- dialogue timing that fits entirely inside the segment
- action/dialogue synchronization
- off-camera voice behavior when voice-over is used
- negative constraints for state-transition failures

### Reference State Contract

A reference identifier alone is not sufficient.

For every start, bridge, and target reference used by a generation segment, define the state variables that must remain stable or change:

- creator body orientation and posture
- hand positions and which hand holds the product
- product position, orientation, open/closed state, and visible label
- fingertip/product contact state
- gaze target
- facial expression
- camera framing and spatial relationship
- relevant environment and lighting continuity

An immutable bridge reference is a physical state contract. It must not be treated as a loose visual suggestion.

### Action Beat Contract

Write action as an ordered causal sequence:

    TRIGGER / INTENTION
        ↓
    ACTION
        ↓
    PHYSICAL RESULT
        ↓
    NEXT ACTION

Avoid compressed instructions such as “then opens the product and takes some moisturizer” when multiple visually important transitions occur. Split them into explicit beats.

Example:

    BEAT 01
    Product is held beside the face with the container closed.

    BEAT 02
    Creator moves the product slightly toward camera while maintaining label visibility.

    BEAT 03
    Creator opens the container with the other hand; lid movement is caused by visible hand contact.

    BEAT 04
    Creator brings fingertip to the moisturizer and collects a small visible amount.

    BEAT 05
    Fingertip separates from the product with the sampled moisturizer visible, matching the bridge reference.

Every beat must have a plausible resulting state. The generator must not skip, reverse, or invent intermediate states.

### Naturalization Contract

Naturalization must operate as a bounded realism layer over the canonical Action Graph and Reference Graph.

Define two classes of naturalization:

1. **Baseline human micro-motion**
   - breathing
   - occasional blinking
   - subtle posture settling
   - restrained facial settling
   - realistic fabric/hijab response

2. **Action-coupled naturalization**
   - wrist rotation caused by reaching or presenting a product
   - finger repositioning caused by grip or lid manipulation
   - small shoulder or torso response caused by an arm movement
   - gaze adjustment caused by the active object of attention
   - minor balance or weight shift caused by the body movement

For action-coupled naturalization, preserve the causal chain:

    PRIMARY ACTION
        ↓
    PHYSICAL CONSEQUENCE
        ↓
    NATURALIZATION

Naturalization must remain subordinate to the primary action. It must not:

- introduce independent gestures
- create random head turns or gaze changes
- add unrelated hand movement
- change hand ownership
- alter an immutable bridge state
- change product state without physical cause
- modify the intended action timing
- create independent camera motion
- make the creator reach a target reference prematurely

A compliant prompt should describe naturalization specifically enough to be bounded, but must not prescribe excessive frame-by-frame randomness. The goal is controlled human realism, not stochastic motion.

### Product Causality Contract

Product interaction must explicitly define:

- acting hand
- supporting hand when applicable
- contact point
- direction of movement
- object state before action
- object state after action
- visible label/orientation constraint
- quantity/state changes caused by the action

Disallow unexplained product rotation, hand swapping, lid-state changes, texture appearing before contact, duplicated product instances, or state changes without physical cause.

### Gaze & Expression Timeline

Gaze is a motion channel and must be tied to the action timeline.

When gaze changes materially, provide bounded timing or beat ownership, for example:

    00:00–02.4  camera
    02.4–04.2   product
    04.2–06.2   fingertip / product
    06.2–08.0   camera

Expression changes should remain restrained and action-related. Do not leave gaze as an unconstrained list such as “camera → product → fingertip” without indicating when the changes occur.

### Camera-Action Relationship

Camera behavior must explain how framing responds to the active action:

- opening framing
- controlled reframing or product-following when required
- preservation of face/product readability
- visibility of the relevant hand/product interaction
- final framing matching the target reference
- no digital zoom, random shake, abrupt perspective change, or unexplained camera movement

Camera motion must support the action rather than create an independent motion track.

### Dialogue Timing & Sync

All dialogue or voice-over intervals must fit completely inside the exact segment duration.

For an 8-second segment, an interval ending at 08.2 is invalid.

When multiple dialogue lines exist, each line must specify:

- exact canonical wording
- speaker or voice-over status
- start and end timing
- delivery
- lip-sync requirement
- action being performed while the line is spoken
- whether the mouth must remain naturally inactive for voice-over

Do not claim that dialogue “continues across a segment boundary” unless the same canonical utterance actually crosses that boundary. Separate adjacent lines should instead preserve conversational flow without restart, duplication, or paraphrase.

### End-State Contract

Do not rely only on “finish in R03.”

Explicitly state the required end state for:

- creator posture
- hand positions
- product state
- product orientation/label visibility
- fingertip state
- gaze
- expression
- camera framing

The segment is valid only when the resulting state matches the canonical target reference.

### Segment Validation

Before a generation segment is accepted, verify:

- duration is exactly 4, 6, 8, or 10 seconds
- all dialogue intervals are within segment bounds
- action beats are ordered and causally connected
- start/bridge/target references are canonical
- bridge states are explicitly defined when present
- product state changes have physical causes
- baseline naturalization remains bounded
- action-coupled naturalization has an explicit physical cause and does not create new actions
- naturalization does not alter bridge or target reference states
- gaze changes are tied to action beats
- camera behavior responds to the action
- end state is explicitly specified
- voice-over mouth behavior is defined when applicable
- negative constraints cover state-transition failures
- no beat is skipped, reversed, duplicated, or invented
- no upstream dependency is stale

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
- Voice Generation Reference matches the current Voice Script Performance Plan when speech generation is required
- pronunciation guidance is preserved when defined
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
