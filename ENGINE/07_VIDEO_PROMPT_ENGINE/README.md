# Affilix — Video Prompt Engine

## Purpose

The Video Prompt Engine converts the completed storyboard and visual scene specification into production-ready motion instructions for video generation.

It defines how the completed visual state moves through time.

The engine must preserve creator identity, product identity, physical plausibility, and scene continuity.

## Input

- Approved storyboard
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
- Generation segment plan when applicable
- Previous and next scene continuity requirements

## Duration and Provider Capability

Video duration has two distinct layers:

1. **Creative duration**: how long the completed storyboard beat should exist in the final video.
2. **Generation duration**: the technical duration requested from the selected video provider for one generated clip.

The provider capability profile defines supported generation durations. It may contain discrete values such as [4, 6, 8, 10] seconds, but Affilix must never assume those values are universal.

### Duration Rules

- Preserve the user's approved requested final duration.
- Do not silently replace an 18-second request with a 10-second output because a provider has a 10-second maximum.
- When one generation cannot cover a required duration, create multiple generation segments.
- Each generation segment must use a provider-supported duration.
- Segment durations must sum to the requested final duration.
- Segment boundaries should align with natural visual beats.
- If a scene's creative duration does not map cleanly to provider durations, restructure or redistribute the creative beat intentionally before generation.
- Never add meaningless filler merely to consume provider duration.
- Never compress a material action without checking narrative and dialogue timing.
- Technical generation duration must be recorded separately from creative duration.

### Example

For an approved 18-second video and a provider supporting [4, 6, 8, 10] seconds:

4s + 6s + 8s = 18s

is a valid three-segment production plan.

Another valid plan may be 8s + 10s = 18s when the storyboard contains two clean visual beats.

The selected segmentation must follow the storyboard, not arithmetic convenience alone.

## Output

Each video scene should contain:

### Motion Metadata

- Scene ID
- Video Prompt ID
- Creative duration
- Generation segment ID when applicable
- Generation duration
- Segment start/end time in final video
- Provider ID
- Start state
- End state
- Motion intensity
- Camera movement
- Creator movement
- Product movement
- Environmental movement
- Transition

### Motion Instructions

Specify:

- Starting pose
- Starting gaze
- Initial product position
- Creator body movement
- Head movement
- Facial movement
- Hand movement
- Product handling
- Camera movement
- Camera speed
- Focus behavior
- Background movement
- End pose
- End product state
- Transition state

## Motion Construction

Build motion from:

Start State
+
Primary Action
+
Secondary Natural Motion
+
Camera Behavior
+
End State

Every movement should have a reason within the scene.

## Creator Motion Rules

Preserve:

- Face identity
- Body proportions
- Hijab identity
- Outfit identity
- Physical plausibility

Use natural motion:

- Blinking
- Breathing
- Subtle head movement
- Natural hand movement
- Realistic weight shifting
- Appropriate facial reaction

Avoid excessive movement that changes the creator's identity or creates anatomical distortion.

## Hijab Motion

When the selected creator wears hijab:

- Preserve hair coverage.
- Maintain realistic fabric attachment.
- Allow natural fabric movement when caused by body or environmental motion.
- Do not let fabric detach, float unnaturally, or reveal covered areas without an explicit scene requirement.

## Product Motion Rules

Product movement must follow realistic interaction.

Preserve:

- Shape
- Color
- Material
- Scale
- Branding
- Configuration

Do not morph the product between frames.

When the creator picks up, rotates, opens, wears, or demonstrates a product, specify the physical sequence clearly.

## Camera Movement

Supported camera behavior may include:

- Static
- Handheld subtle movement
- Slow push-in
- Slow pull-back
- Pan
- Tilt
- Tracking
- Follow movement
- Reframe

Camera movement must support the storyboard purpose.

Do not use dramatic camera motion simply because a video model enjoys chaos.

## Motion Intensity

Use:

- Subtle
- Moderate
- Dynamic

Select intensity based on:

- Scene purpose
- Creator persona
- Product interaction
- Platform format
- Emotional beat

## Timing

Creative scene timing must match the completed storyboard.

For segmented generation:

- Map each generation segment to a final-video time range.
- Ensure the segment starts and ends in a visually coherent state.
- Preserve continuity between adjacent generated clips.
- Do not assume every generation segment has the same length.
- Dialogue timing must remain compatible with the creative scene timing, regardless of provider segment boundaries.

## Dialogue Synchronization

When dialogue exists:

- Align mouth movement with the intended speech.
- Keep facial expression compatible with the spoken meaning.
- Do not add unrequested dialogue.
- Avoid actions that interfere with clear speech when the scene depends on speaking to camera.

The Voice Script Engine owns final wording. The Video Prompt Engine owns visual synchronization.

## Continuity

Across adjacent scenes and generation segments preserve:

- Creator identity
- Outfit
- Hijab styling
- Product state
- Product position when continuity requires it
- Location
- Lighting
- Spatial direction
- Narrative time

A transition may intentionally change these only when the storyboard specifies the change.

## Physical Plausibility

Validate:

- Hands connect correctly to objects.
- Product scale remains realistic.
- Body movement follows believable joint motion.
- Camera movement matches the environment.
- Clothing and hijab respond plausibly to motion.
- Objects do not teleport between positions.

## Negative Motion Constraints

Use only relevant constraints, such as:

- No identity morphing
- No face distortion
- No extra fingers
- No duplicated hands
- No product morphing
- No duplicate product
- No floating objects
- No sudden outfit change
- No uncovered hair
- No unnatural hijab detachment
- No impossible body movement
- No arbitrary filler motion to consume provider duration

## Output Formatting Rule

The final video-generation prompt is always emitted as one standalone Markdown code block:

```text
[complete video prompt]
```

Do not split one video prompt across multiple code blocks. Metadata and generation-segment tables stay outside the code block.

## Handoff

The video prompt is passed to:

- Video generation workflow
- 09_QUALITY_CONTROL

The storyboard and visual prompt remain the source of truth for scene intent and appearance. The video prompt defines temporal behavior and provider-compatible generation segmentation.

## Layered Niche Context Integration

Video prompts now receive Loaded Niche Context. Context may influence motion intensity, interaction pattern, setting, and camera behavior when supported by the storyboard. It must not create unsupported product performance claims. Continuity checks include context-driven wardrobe, environment, and action state.
