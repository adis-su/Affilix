# Affilix — Video Prompt Engine

## Purpose

The Video Prompt Engine converts the completed storyboard and visual scene specification into production-ready motion instructions for video generation.

It defines how the completed visual state moves through time while adapting each generation request to the current provider's supported durations.

## Current Provider Duration Policy

The current provider supports exactly four generation durations:

- 4 seconds
- 6 seconds
- 8 seconds
- 10 seconds

Every generated clip must use one of these durations.

If a campaign is longer than 10 seconds, Affilix uses multiple generation segments. The final assembled duration must remain exactly equal to the requested duration.

## Input

- Completed storyboard
- Visual prompt for the scene
- Creator identity
- Product identity
- Pose and expression
- Product interaction
- Environment
- Camera composition
- Lighting
- Dialogue timing when available
- Creative scene duration
- Provider capability profile
- Generation segment plan
- Previous and next scene continuity requirements

## Duration Policy

Generation duration is selected from `[4, 6, 8, 10]` seconds.

Examples:

```text
12s final → 6s + 6s
14s final → 6s + 8s
18s final → 8s + 10s
20s final → 10s + 10s
```

Choose segment boundaries based on natural creative beats.

If the requested final duration cannot be composed exactly from the available durations, mark the duration as infeasible rather than changing it silently.

## Motion Construction

Build each segment from:

Start State
+
Primary Action
+
Secondary Natural Motion
+
Camera Behavior
+
End State

Each segment must end in a state that can transition naturally into the next segment.

## Output Formatting Rule

The final video-generation prompt is always emitted as one standalone Markdown code block:

```text
[complete video prompt]
```

Do not split one video prompt across multiple code blocks. Metadata and generation-segment records stay outside the code block.

## Motion Rules

Preserve:

- creator identity
- body proportions
- hijab identity
- outfit identity
- product identity
- product geometry
- physical plausibility
- scene continuity

Camera movement may be static, subtle handheld, push-in, pull-back, pan, tilt, tracking, follow, or reframe when supported by the storyboard.

Avoid excessive movement, identity morphing, product morphing, impossible body motion, or filler motion.

## Dialogue Synchronization

When dialogue exists:

- align mouth movement with intended speech
- keep facial expression compatible with spoken meaning
- do not add dialogue
- avoid actions that interfere with speech when speaking to camera

Voice Script owns wording. Video Prompt owns visual synchronization.

## Continuity

Across adjacent scenes and technical segments preserve:

- creator identity
- outfit
- hijab styling
- product state
- environment
- lighting
- spatial direction
- narrative time

## Validation

Before handoff verify:

- every generation duration is 4/6/8/10 seconds
- segment durations sum exactly to requested final duration
- segment boundaries are coherent
- creator and product remain consistent
- physical motion is plausible
- dialogue fits creative timing
- no filler motion exists

## Handoff

The Video Prompt becomes the technical motion specification for video generation. Storyboard remains the canonical source for scene intent and timing. Visual Prompt remains the canonical source for static appearance.
