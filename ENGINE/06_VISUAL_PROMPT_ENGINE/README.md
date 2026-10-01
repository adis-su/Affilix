# Affilix — Visual Prompt Engine

## Purpose

The Visual Prompt Engine converts each completed storyboard scene into a production-ready **static image-generation prompt**.

Its job is to describe **what must be visible in one generated frame**. It is not a video prompt, motion specification, or temporal scene description.

The engine must preserve creator identity, product identity, wardrobe, pose, expression, environment, composition, visual style, and other visual requirements from the completed storyboard without inventing unsupported facts.

The storyboard remains the canonical source of scene intent and temporal context. The image prompt is a visual implementation layer for **one frame** of that scene.

## Core Principle

An image prompt answers:

> **What should the generated frame look like?**

It does not answer:

> How does the subject move over time?

Temporal behavior belongs to `07_VIDEO_PROMPT_ENGINE`.

Therefore:

- Describe a **single visual state**, not a sequence of actions.
- Convert storyboard actions into the **resulting visible pose/state**.
- Do not describe start state → motion → end state.
- Do not include camera movement.
- Do not include duration as a generation instruction.
- Do not describe what happens before or after the frame.
- Do not use ambiguous alternatives such as "pointing or presenting".
- Do not turn narrative metadata into visual instructions unless it materially affects the frame.

## Input

- Completed storyboard scene
- Selected creator package
- Canonical creator identity
- Approved creator visual references
- Product identity
- Approved product references
- Wardrobe selection
- Expression selection
- Pose selection
- Scene environment
- Composition requirements
- Camera requirements
- Lighting requirements
- Platform/aspect-ratio requirements
- Loaded niche context when applicable

## Output Contract

For every visual scene, return:

### Prompt Metadata

Metadata may contain:

- Scene ID
- Timecode
- Duration
- Story purpose
- Narrative beat
- Prompt ID
- Prompt type: Image / Keyframe / Reference
- Aspect ratio
- Creator references
- Product references
- Wardrobe references
- Pose/expression references
- Environment references
- Style references

Metadata is for traceability. It must not make the final image-generation prompt behave like a video prompt.

### Final Prompt

The final image-generation prompt must be delivered as **one coherent structured prompt inside a single code block**.

Use this canonical order:

```text
IMAGE PROMPT

SUBJECT
[who/what is visibly present]

CREATOR
[canonical identity and visible appearance]

WARDROBE
[visible outfit and hijab]

PRODUCT
[visible product identity, state, and appearance]

POSE & EXPRESSION
[one deterministic visible pose, gesture, gaze, and expression]

ENVIRONMENT
[visible setting, background, and supported props]

COMPOSITION
[shot size, framing, subject placement, product placement, negative space]

CAMERA
[static image perspective, angle, orientation, and only specified lens characteristics]

LIGHTING
[visible lighting characteristics]

VISUAL STYLE
[approved visual aesthetic and realism]

NICHE CONTEXT
[only scene-relevant visual context]

CONTINUITY
[visual attributes that must match approved references]

NEGATIVE CONSTRAINTS
[image-specific visual risks to avoid]

FINAL IMAGE GENERATION INSTRUCTION
[generate one coherent static frame]
```

## Static Frame Rule

Every final prompt must represent **one moment frozen in time**.

### Correct

```text
Rositasari faces the camera with a subtle friendly smile and points naturally downward with her right index finger toward the lower portion of the frame.
```

### Incorrect

```text
Rositasari raises her hand, looks at the camera, points downward, then maintains the gesture.
```

The second version describes a sequence and belongs to video direction.

## Deterministic Visual State

Generation-critical visual fields must have one clear interpretation.

Do not write:

- "pointing or presenting"
- "standing or slightly leaning"
- "smiling or neutral"
- "looking at camera or slightly off-camera"

Choose the approved visual state.

If the storyboard itself is ambiguous, resolve it from approved references or mark it UNKNOWN rather than silently inventing a second option.

## Storyboard Translation

Storyboard action must be translated into a **visible final pose/state**.

Examples:

| Storyboard intent | Image prompt translation |
|---|---|
| Creator points toward CTA | Creator is posed facing camera with one hand clearly pointing downward toward the lower frame |
| Creator holds product | Creator visibly holds the product in the specified hand and position |
| Creator looks at product | Creator's gaze is directed toward the visible product |
| Creator walks into frame | Do not depict walking motion; depict the approved still pose/state if a keyframe is required |
| Creator turns toward camera | Show the creator already facing the camera in the resulting frame |

Do not carry temporal verbs into the image prompt when they imply motion.

## CTA and Overlay Rule

When a scene requires CTA text or UI to be added later:

- Describe only the physical pose and composition needed to support the CTA.
- Reserve clean negative space where the overlay will be composited.
- Do not bake CTA text into the generated image unless explicitly requested.
- Do not generate shopping-cart icons, yellow basket graphics, badges, prices, discounts, or interface elements unless they are explicitly part of the physical visual reference.

Example:

```text
Leave clean lower-frame negative space for a separately composited CTA overlay.
```

## Timecode and Duration

Timecode and duration may remain in prompt metadata for traceability.

They are **not generation instructions**.

Do not write:

- "for 6 seconds"
- "during 00:24–00:30"
- "before the next scene"
- "at the end of the video"

inside the visual description unless required solely as metadata.

## Output Specificity

The final prompt should be detailed enough to produce the intended frame, but only with information relevant to visual generation.

Prioritize:

1. Creator identity
2. Product identity
3. Visible wardrobe
4. Pose and expression
5. Environment
6. Composition
7. Camera perspective
8. Lighting
9. Visual style
10. Scene-relevant niche context
11. Continuity constraints

Do not duplicate the entire storyboard merely to make the prompt look comprehensive.

## Creator Identity Lock

Every prompt involving the selected creator must preserve the approved canonical identity.

Preserve:

- Face structure
- Facial proportions
- Apparent age
- Skin identity
- Body proportions
- Canonical hijab identity
- Other approved identity locks

Allowed visual variation may include:

- Expression
- Eye direction
- Pose
- Gesture
- Camera angle
- Lighting
- Outfit
- Hijab color
- Hijab fabric
- Hijab drape
- Makeup intensity when approved

Audience context must never change the creator's canonical age, identity, or physical characteristics.

## Hijab Rules

When the selected creator has a canonical hijab identity:

- Keep hair covered in standard scenes.
- Keep neck coverage consistent with approved styling.
- Preserve realistic hijab construction and fabric behavior.
- Treat color, fabric, folds, and draping as controlled style variables.
- Do not convert a hijabi creator into an uncovered hairstyle unless explicitly requested.

## Product Identity Lock

Preserve:

- Product shape
- Product color
- Material appearance
- Size/proportion
- Packaging
- Branding
- Labels
- Key physical details
- Configuration
- Product state when visually specified

Use the approved product reference as the visual authority.

Do not add decorative details that could be mistaken for actual product features.

Incomplete visual product detail is not, by itself, a reason to block prompt generation. Preserve unavailable attributes as UNKNOWN internally.

## Product Visibility

Avoid vague instructions such as:

- "product sufficiently visible"
- "product visible alongside creator"

Instead specify the actual visual requirement, for example:

- "the complete cardigan and culotte pants are clearly visible"
- "the product is held at chest height with the front face visible"
- "the product occupies the right side of the frame"

Only use details supported by the storyboard or approved references.

## Environment and Props

Describe only visible, supported scene elements.

Do not invent:

- Decorative props
- Furniture
- Brand signage
- Product packaging
- UI elements
- Additional people

If the setting is inherited from a previous approved scene, state that the frame must visually match the established environment without inventing new objects.

## Composition

Translate storyboard composition into deterministic visual framing.

Specify when relevant:

- Shot size
- Framing
- Subject position
- Product position
- Negative space
- Camera angle
- Orientation
- Perspective

When both a complete outfit and lower-frame negative space are required, resolve the composition explicitly. For example:

```text
Medium-full portrait framing, showing the complete outfit from head to below the knees, with the creator positioned slightly above vertical center and clean negative space preserved in the lower frame.
```

Do not create contradictory framing requirements.

## Camera

Camera instructions describe the **static image perspective** only.

Allowed:

- Eye-level perspective
- Low/high angle
- Portrait orientation
- Natural smartphone perspective
- Specified lens/focal character

Do not use video instructions such as:

- Camera pans
- Camera pushes in
- Camera follows subject
- Camera tracks movement
- Camera rotates

Those belong to the Video Prompt Engine.

## Lighting

Describe only the visible lighting state:

- Lighting type
- Direction when known
- Soft/hard quality
- Shadow behavior
- Exposure
- Color temperature when known

When lighting continuity matters, instruct the image to visually match the established approved lighting. Do not invent a new lighting setup.

## Visual Style

Style language must describe observable visual treatment.

"Korean-style" or similar style labels may describe aesthetic direction only. They must not imply unsupported product origin, manufacturing origin, branding, certification, or cultural provenance.

Avoid unsupported evaluative claims such as "premium", "luxury", or "high quality" unless they are explicitly part of the approved visual direction.

## Niche Context

Only scene-relevant niche context belongs in the final image prompt.

Niche context may influence:

- Styling
- Setting
- Composition
- Visual language
- Audience-appropriate presentation

It must not override creator identity or product facts.

## Continuity

Continuity in an image prompt is **visual continuity**, not temporal narration.

Use continuity to preserve:

- Creator identity
- Product identity
- Outfit
- Hijab styling
- Accessories
- Environment
- Lighting appearance
- Product state
- Relevant spatial relationships

Do not include "next scene" instructions.

Do not describe what the creator will do afterward.

## Negative Constraints

Use image-specific constraints that prevent real generation failures.

Examples:

- No identity drift
- No uncovered hair or neck when prohibited
- No altered outfit configuration
- No distorted hands
- No extra fingers
- No duplicated hands
- No cropped pointing hand
- No duplicate product
- No unsupported accessories
- No invented logos or text
- No promotional UI
- No baked-in CTA overlay
- No additional people
- No inconsistent environment

Avoid generic negative keyword dumps.

## Reference Priority

1. Latest explicit user instruction
2. Approved canonical creator identity
3. Approved canonical product reference
4. Dedicated creator/product attribute reference
5. Approved wardrobe/pose/expression reference
6. Scene-specific visual reference
7. Loaded niche context
8. General aesthetic direction

## Reference Separation

Keep reference roles distinct:

- Creator reference controls creator identity.
- Product reference controls product identity.
- Wardrobe reference controls clothing.
- Pose reference controls body positioning.
- Expression reference controls facial expression.
- Environment reference controls scene setting.
- Style reference controls overall visual treatment.

One reference must not silently override unrelated attributes.

## Output Formatting Rule

The final image-generation prompt is always emitted as one standalone Markdown code block:

```text
[complete image prompt]
```

Do not split one image prompt across multiple code blocks. Metadata stays outside the code block.

## Handoff

Visual prompts are passed to:

- Image generation workflow
- 07_VIDEO_PROMPT_ENGINE
- downstream production output

The storyboard remains the canonical source for scene intent. The visual prompt is an implementation layer for a static frame and does not replace the storyboard.

## Layered Niche Context Integration

Visual prompts receive Loaded Niche Context. Sub-niche, use case, and style may influence setting, styling, composition, and visual language.

Product and creator identity remain higher-priority source-of-truth layers.

Context labels must never become unsupported product attributes, origin claims, branding, or creator identity changes.

## Runtime Invariants

- One final prompt per visual scene.
- Final prompt is always delivered in one code block.
- Final prompt describes one static visual state.
- Storyboard remains the temporal source of truth.
- Creator identity remains locked.
- Product identity remains locked.
- References retain their defined roles.
- Unsupported facts are never invented.
- UNKNOWN is preserved internally when information is unavailable.
- Incomplete visual product detail alone does not block prompt generation.
- Image prompts do not contain video motion direction.
- Image prompts do not contain temporal sequence instructions.
- Downstream image generation can trace the prompt back to its storyboard scene.


## Reference-State Architecture

Visual prompts are generated from Storyboard reference states rather than from scenes as a whole. One scene may produce multiple static prompts because it contains multiple meaningful states.

```text
R01 → R02 → R03 → R04
```

Each prompt freezes exactly one state. It must preserve creator, product, wardrobe, camera, environment, lighting, and continuity-critical attributes from the reference contract. See `REFERENCE_STATE_CONTRACT.md`.

A bridge reference is rendered as one canonical state and reused by both adjacent scenes. The Visual Prompt Engine must never invent a different boundary state.
