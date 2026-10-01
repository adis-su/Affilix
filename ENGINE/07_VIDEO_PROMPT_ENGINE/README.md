# Affilix — Video Prompt Engine

## Purpose

The Video Prompt Engine converts the approved storyboard and visual scene specification into production-ready motion instructions for video generation.

It defines how the approved visual state moves through time.

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
- Scene duration
- Previous and next scene continuity requirements

## Output

Each video scene should contain:

### Motion Metadata

- Scene ID
- Video Prompt ID
- Duration
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

The scene duration must match the storyboard.

Break complex actions into temporal stages when needed:

0–1s: preparation
1–3s: primary action
3–5s: reaction or product emphasis

Use actual scene duration rather than assuming every scene has the same length.

## Dialogue Synchronization

When dialogue exists:

- Align mouth movement with the intended speech.
- Keep facial expression compatible with the spoken meaning.
- Do not add unrequested dialogue.
- Avoid actions that interfere with clear speech when the scene depends on speaking to camera.

The Voice Script Engine owns final wording. The Video Prompt Engine owns visual synchronization.

## Continuity

Across adjacent scenes preserve:

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

## Video QC

Before handoff, verify:

### Identity

- Creator remains consistent from start to end.
- Hijab remains consistent when applicable.

### Product

- Product remains the same object.
- Product interaction is physically plausible.
- No visual morphing.

### Motion

- Primary action is clear.
- Motion intensity fits the scene.
- Camera movement supports the story.
- End state can connect to the next scene.

### Timing

- Actions fit within the scene duration.
- Dialogue timing is plausible.
- No important action is compressed unrealistically.

## Handoff

The video prompt is passed to:

- Video generation workflow
- 09_QUALITY_CONTROL

The storyboard and visual prompt remain the source of truth for scene intent and appearance. The video prompt defines temporal behavior.


## Layered Niche Context Integration

Video prompts now receive Loaded Niche Context. Context may influence motion intensity, interaction pattern, setting, and camera behavior when supported by the storyboard. It must not create unsupported product performance claims. Continuity checks include context-driven wardrobe, environment, and action state.
