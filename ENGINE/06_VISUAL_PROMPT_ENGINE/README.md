# Affilix — Visual Prompt Engine

## Purpose

The Visual Prompt Engine converts each approved storyboard scene into a production-ready image generation prompt while preserving creator identity, product identity, scene continuity, and visual intent.

It generates prompts from structured data. It must not replace missing facts with creative guesses.

The storyboard is the canonical temporal source of truth. The final image prompt is a structured implementation of one storyboard scene and must carry all relevant scene data forward.

## Input

- Approved storyboard
- Selected creator package
- Canonical creator identity
- Approved creator visual references
- Product identity
- Approved product references
- Wardrobe selection
- Expression selection
- Pose selection
- Scene environment
- Camera requirements
- Lighting requirements
- Platform/aspect-ratio requirements
- Loaded niche context when applicable

## Output Contract

For every visual scene, return:

### Prompt Metadata

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

### Final Prompt Format

The final image-generation prompt must be delivered as a single structured prompt inside a code block.

Use this canonical order:

```text
IMAGE PROMPT

SCENE
Scene ID: [scene_id]
Timecode: [start - end]
Duration: [duration]
Story Purpose: [story_purpose]
Narrative Beat: [narrative_beat]

CREATOR
Identity: [canonical creator identity]
Age: [age if available]
Gender: [gender if available]
Appearance: [approved physical appearance]
Face: [canonical face details]
Body / Build: [approved body identity]
Hijab: [canonical hijab requirements]
Expression: [expression]
Gaze: [gaze direction]
Pose: [pose]
Gesture: [gesture]
Orientation: [body orientation]

WARDROBE
Outfit: [exact approved outfit]
Color: [color if available]
Material: [material if available]
Accessories: [approved accessories only]
Wardrobe Continuity: [continuity requirement]

PRODUCT
Product Name: [product name]
Product Type: [product type]
Appearance: [available product appearance]
Color: [available color]
Material: [available material]
Shape / Form: [available shape/form]
Size / Proportion: [available information]
Branding / Label: [available branding]
Configuration: [available configuration]
Product State: [state in this scene]
Product Visibility: [how product must appear]
Product Interaction: [how creator interacts with product]

ACTION
Primary Action: [primary creator action]
Secondary Action: [secondary natural action]
Interaction Details: [specific interaction]
Physical Logic: [physically plausible interaction]

ENVIRONMENT
Location / Setting: [approved setting]
Background: [background]
Objects / Props: [approved objects only]
Spatial Placement: [creator/product/object placement]
Environment Continuity: [continuity requirement]

COMPOSITION
Shot Type: [shot type]
Framing: [framing]
Camera Angle: [angle]
Subject Position: [position in frame]
Product Position: [product position]
Visual Focus: [primary visual focus]
Depth: [depth/composition information]

CAMERA
Camera Behavior: [camera behavior]
Lens / Focal Character: [if specified]
Perspective: [perspective]
Image Orientation: [portrait/landscape if specified]
Aspect Ratio: [aspect ratio if specified]

LIGHTING
Lighting Type: [lighting]
Light Direction: [direction]
Light Quality: [soft/hard/etc.]
Shadow Behavior: [shadow]
Exposure: [exposure requirement]
Color Temperature: [if specified]

VISUAL STYLE
Style: [approved visual style]
Aesthetic: [approved aesthetic]
Realism Level: [realistic/stylized if specified]
Texture: [visual texture]
Color Treatment: [approved color treatment]

NICHE CONTEXT
Niche: [loaded niche]
Sub-Niche: [loaded sub-niche if available]
Use Case: [loaded use case if available]
Style / Aesthetic Context: [loaded style if available]
Audience Context: [loaded audience context if available]
Context Constraints: [scene-relevant constraints only]

CONTINUITY
Previous Scene Continuity: [what must remain consistent]
Current Scene Continuity: [identity/product/environment continuity]
Next Scene Continuity: [what must remain ready for next scene]
Creator Consistency: [identity lock]
Product Consistency: [product identity lock]

NEGATIVE CONSTRAINTS
Do not change creator identity.
Do not change facial features.
Do not change hijab coverage or canonical hijab requirements.
Do not change product identity.
Do not alter product color, shape, material, branding, or configuration when supplied.
Do not add unsupported product features.
Do not add unsupported accessories or props.
Do not invent text, labels, logos, or packaging details.
Do not create anatomically incorrect hands or body proportions.
Do not create physically impossible product interactions.
Do not introduce objects that are not specified or supported.
Do not create visual inconsistencies with previous or following scenes.

REFERENCE PRIORITY
1. Latest explicit user instruction
2. Approved canonical creator identity
3. Approved canonical product reference
4. Dedicated creator/product attribute reference
5. Approved wardrobe/pose/expression reference
6. Scene-specific visual reference
7. Loaded niche context
8. General aesthetic direction

FINAL IMAGE GENERATION INSTRUCTION
Generate one coherent image for this scene.
Follow the storyboard exactly.
Preserve creator identity, product identity, wardrobe continuity, spatial continuity, and scene continuity.
Use only supplied or approved information.
Where information is unavailable, preserve it as UNKNOWN internally and do not invent additional defining details.
```

The code-block structure is mandatory for the final prompt output. Do not split one scene's final prompt into unrelated prose sections outside the code block.

## Prompt Data Completeness

The final prompt must carry forward all storyboard information that materially affects image generation.

At minimum, preserve:

- Scene identity and timing
- Story purpose and narrative beat
- Creator identity
- Creator action
- Orientation
- Pose
- Gesture
- Expression
- Gaze
- Outfit and hijab
- Product identity
- Product state
- Product visibility
- Product interaction
- Environment
- Object/prop placement
- Shot type
- Framing
- Camera angle
- Camera behavior
- Lighting
- Visual style
- Relevant niche context
- Continuity constraints
- Reference requirements
- Negative constraints

Do not silently drop a storyboard field that materially changes the generated image.

Fields that are not available must not be replaced with invented specifics. Preserve the unavailable information as UNKNOWN internally and continue when the image can still be generated safely.

## Prompt Assembly

Build prompts in this conceptual order:

Scene Metadata
+
Creator Identity
+
Wardrobe
+
Product Identity
+
Action
+
Environment
+
Composition
+
Camera
+
Lighting
+
Visual Style
+
Niche Context
+
Continuity
+
Negative Constraints
+
Reference Priority
+
Final Generation Instruction

Do not let aesthetic language override identity, product facts, storyboard intent, or explicit user requirements.

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

Controlled variations may include:

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

## Hijab Rules

When the selected creator has a canonical hijab identity:

- Keep hair covered in standard scenes.
- Keep neck coverage consistent with the approved styling.
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
- Product state when specified by the storyboard

Use the approved product reference as the visual authority.

Do not add decorative details that could be mistaken for actual product features.

Incomplete visual product detail is not, by itself, a reason to block prompt generation. Use available references and preserve unavailable attributes internally as UNKNOWN.

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
- Style reference controls overall visual styling.

One reference must not silently override unrelated attributes.

## Prompt Specificity

Prompts should be specific enough to preserve required details but not overloaded with unsupported information.

Prefer observable descriptions over vague adjectives.

Weak:

"beautiful, perfect, stunning woman."

Better:

"young adult hijabi woman with the approved canonical facial structure, natural skin texture, calm approachable expression, wearing the approved outfit, holding the approved product in her right hand."

## Camera and Composition

Translate storyboard requirements into explicit visual instructions:

- Shot size
- Camera angle
- Camera height when relevant
- Subject placement
- Product placement
- Negative space
- Orientation
- Perspective
- Depth of field
- Lens characteristics when specified

Do not invent camera specifications when they materially change the intended composition.

## Continuity

Visual prompts for sequential scenes must preserve:

- Creator identity
- Product identity
- Outfit unless a change is scripted
- Hijab styling unless a change is scripted
- Accessories
- Environment when unchanged
- Lighting continuity when appropriate
- Product state
- Spatial relationships
- Relevant visual state from the preceding scene

The prompt must explicitly carry continuity requirements from the storyboard rather than relying on the image model to infer them.

## Negative Constraints

Use negative constraints only when they protect an important requirement.

Examples:

- No uncovered hair
- No altered product shape
- No extra product components
- No incorrect logo
- No additional people
- No inconsistent outfit
- No distorted hands
- No duplicate product
- No identity drift

Do not fill prompts with generic negative keywords that do not address an actual production risk.

## Visual QC

Before handoff, verify:

### Prompt Structure

- Final prompt is inside a code block.
- Scene metadata is present.
- All materially relevant storyboard data is represented.
- Product and creator references are included.
- Continuity constraints are explicit.
- Negative constraints address real risks.

### Creator

- Identity matches canonical reference.
- Age presentation is consistent.
- Hijab identity is preserved.
- Body proportions remain consistent.
- Pose, expression, gaze, and action match the storyboard.

### Product

- Product matches reference.
- Color and shape are correct when supplied.
- Branding/labels are not invented.
- Product state matches the storyboard.
- Interaction is physically plausible.

### Scene

- Composition matches storyboard.
- Pose matches storyboard.
- Expression matches intended emotional beat.
- Environment matches storyboard.
- Lighting is coherent.

### Continuity

- Scene connects logically to previous and next scene.
- Outfit and product state are consistent.
- No unexplained visual changes.
- Creator and product identity remain locked.

## Handoff

Visual prompts are passed to:

- Image generation workflow
- 07_VIDEO_PROMPT_ENGINE
- 09_QUALITY_CONTROL

The storyboard remains the canonical source for scene intent. The visual prompt is an implementation layer, not a replacement for the storyboard.

## Layered Niche Context Integration

Visual prompts receive Loaded Niche Context. Sub-niche, use case, and style may control setting, styling, composition, and visual language. Product and creator identity remain higher-priority source-of-truth layers. Context labels must never become unsupported product attributes.

Only scene-relevant niche context should be carried into the final prompt. Context must not override explicit storyboard instructions.

## Runtime Invariants

- One final prompt per visual scene.
- Final prompt is always delivered in a code block.
- Storyboard remains the temporal source of truth.
- Creator identity remains locked.
- Product identity remains locked.
- References retain their defined roles.
- Unsupported facts are never invented.
- UNKNOWN is preserved internally when information is unavailable.
- Incomplete visual product detail alone does not block prompt generation.
- Downstream image generation must be able to trace the prompt back to its storyboard scene.
