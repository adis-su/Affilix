# Affilix — Visual Prompt Engine

## Canonical Stage Identity

- Canonical workflow stage: Stage 07 — Visual Prompt
- Implementation path: `ENGINE/06_VISUAL_PROMPT_ENGINE/`
- The numeric prefix in the implementation directory is NOT a workflow stage ID.
- Do not infer ordering, prerequisites, or downstream dependencies from the directory prefix.
- Resolve workflow stage identity exclusively from `ENGINE/WORKFLOW.md`.

## UGC Naturalism Constraint

Visual Prompt must implement `ENGINE/UGC_NATURALISM_CONTRACT.md` at the frozen-state level. Naturalism here means a plausible human state, not motion language.

Validate every reference state for:
- believable posture and weight distribution
- plausible hand/product contact and grip
- motivated gaze direction
- restrained expression appropriate to the action
- realistic clothing/hijab state and environmental relationship
- continuity of product, creator, and bridge reference invariants
- no synthetic-looking pose that exists only to display the product

Do not encode blinking, breathing, hand movement, or other temporal motion as a sequence. Freeze the resulting state that the video action will use. If a state cannot be made physically plausible without inventing facts or changing the storyboard, mark it `NEEDS_REFINEMENT` or `BLOCKED` rather than improvising.

## Content Format Continuity

The selected Content Format from Stage 04 is an upstream creative constraint carried through Storyboard into every required visual reference state.

Visual Prompt must preserve the format's visible mechanism without turning a static image prompt into a sequence. The format may determine product role, proof visibility, setup, composition, or required state, but all output must remain one frozen visual state.

If the Content Format changes, affected Visual Prompts become STALE and require revalidation or regeneration.

## Format Mechanism → Frozen Visual State

Content Format must remain visually legible at the reference-state level without turning the image prompt into motion or sequence.

For each required reference state, validate:

- **Format evidence:** the frame contains the visible setup, product role, or proof state required by the selected format.
- **Storyboard state fidelity:** the frame is the deterministic visual result of the corresponding storyboard beat.
- **Static integrity:** format meaning is expressed through what is visible in one frozen state, never through temporal wording.
- **Continuity:** the same product identity, creator identity, wardrobe, and bridge reference version are preserved.
- **No format invention:** the image prompt must not introduce a different format mechanism merely because it is visually convenient.

Examples:

| Content Format | Valid frozen-state emphasis |
|---|---|
| BEAUTY_CRIME_SCENE | visible problem/case setup or evidence/intervention state |
| PRODUCT_HAS_A_JOB | product visibly positioned at the specific task area/action state |
| BEAUTY_MYTH_LAB | controlled test setup or test-result state |
| PRODUCT_INTERROGATION | product inspection/demonstration state |
| ONE_PRODUCT_THREE_PERSONALITIES | one product visibly preserved within the specific mode/context state |
| SILENT_BEAUTY_TEST | visually self-explanatory test/action state |
| BEAUTY_ROUTINE_UNDER_PRESSURE | constrained routine context and resulting usable state |
| ANTI-TUTORIAL | visually grounded expectation/reframe state |
| LIFESTYLE_INTEGRATION | believable lifestyle context with product naturally integrated |
| PROBLEM_SOLUTION_MISSION | concrete problem state or resulting task state |

A prompt that merely names the selected format while depicting a generic product portrait does not pass.

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

- Completed storyboard scene, including selected Content Format
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

For every required visual reference state in every visual scene, return one prompt artifact per reference state. A scene is not automatically one prompt.

For example, if Scene 01 contains R01, R02, and R03 as required static reference states, Stage 07 must produce three image prompts: one for R01, one for R02, and one for R03.

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
| Creator holds product | Creator visibly holds the product in the specified hand and position |
| Creator looks at product | Creator's gaze is directed toward the visible product |
| Creator walks into frame | Do not depict walking motion; depict the approved still pose/state if a keyframe is required |
| Creator turns toward camera | Show the creator already facing the camera in the resulting frame |

Do not carry temporal verbs into the image prompt when they imply motion.


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

## Background Reference Lock

When an approved environment/background reference is supplied, treat it as a locked source-of-truth asset, not inspiration. The final prompt must explicitly preserve the same background geometry, layout, architecture, furniture, props, object positions, textures, colors, perspective, depth, and visible lighting cues. Do not generate a replacement setting, add/remove/move objects, extend the room, change the camera viewpoint to reveal unseen areas, or apply stylistic redesign. The creator may be integrated into the reference while the background remains unchanged. If the reference does not reveal a detail, do not invent it. The environment reference must be tracked separately from creator, wardrobe, product, and style references. For video, lock the background across all reference states, transitions, and generation segments; changes are permitted only when explicitly requested by the user. Add explicit negative constraints such as `no background replacement, no background redesign, no object relocation, no new props, no layout changes`.

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

## Reference Density

Visual Prompt follows the Storyboard Reference Plan exactly. Every declared reference state becomes one static prompt, and one scene may therefore produce multiple image prompts. Reference density is action-complexity-driven.

For high-complexity scenes, six meaningful reference states are the default target when justified by the action graph. Simpler scenes may use fewer. Never invent redundant states merely to reach six.

## Runtime Invariants

- One final prompt per required visual reference state.
- A scene containing N required reference states produces N static image prompts.
- Prompt count must equal the number of required reference states, not the number of scenes.
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

## Prompt Cardinality Contract

Reference-state cardinality is authoritative for Visual Prompt generation.

    SCENE 01
    R01 → R02 → R03

    ↓

    PROMPT 01 → R01
    PROMPT 02 → R02
    PROMPT 03 → R03

Rules:

1. Every required reference state produces exactly one static image prompt.
2. A single prompt must never represent multiple reference states.
3. `Reference: R01/R02/R03` is invalid as a final prompt target because it collapses three distinct frozen states into one artifact.
4. Each prompt must carry exactly one `reference_id` in its metadata.
5. Bridge references are not exceptions. If a bridge reference is required as a renderable state, it receives its own canonical image prompt.
6. Prompt numbering is per generated prompt artifact, not per scene.
7. The engine must not silently collapse multiple reference states into one prompt to satisfy a one-prompt-per-scene rule.

Validation:

    required_reference_states = [R01, R02, R03]
    generated_prompts = [P01, P02, P03]
    assert len(generated_prompts) == len(required_reference_states)
    assert generated_prompts[i].reference_id == required_reference_states[i]


## Quote Content Mode Dispatch

When `content_mode = QUOTE_CONTENT`, load `QUOTE_CONTENT_VISUAL_PROMPT_CONTRACT.md`. `QUOTE_IMAGE` uses one static image prompt without a Storyboard dependency. Video formats produce exactly one image prompt per declared Storyboard reference state. Product references are `NOT_APPLICABLE` unless the brief explicitly changes to product-centered content. The universal frozen-state and bridge-reference invariants still apply.
