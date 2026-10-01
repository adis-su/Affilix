# Affilix — Visual Prompt Engine

## Purpose

The Visual Prompt Engine converts each approved storyboard scene into a production-ready image generation prompt while preserving creator identity, product identity, scene continuity, and visual intent.

It generates prompts from structured data. It must not replace missing facts with creative guesses.

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

## Output

For every visual scene, return:

### Prompt Metadata

- Scene ID
- Prompt ID
- Prompt type: Image / Keyframe / Reference
- Aspect ratio
- Creator references
- Product references
- Style references
- Environment references

### Prompt Components

- Subject identity
- Creator appearance
- Hijab identity and styling when applicable
- Outfit
- Pose
- Expression
- Product identity
- Product interaction
- Environment
- Composition
- Camera
- Lens/look when specified
- Lighting
- Color treatment
- Depth of field when specified
- Action state
- Continuity requirements
- Negative constraints

## Prompt Assembly

Build prompts in this conceptual order:

Creator Identity
+
Product Identity
+
Wardrobe
+
Pose / Expression
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
Continuity Constraints

Do not let aesthetic language override identity or product facts.

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

Use the approved product reference as the visual authority.

Do not add decorative details that could be mistaken for actual product features.

## Reference Priority

1. Latest explicit user instruction
2. Approved canonical creator identity
3. Approved canonical product reference
4. Dedicated creator/product attribute reference
5. Approved wardrobe/pose/expression reference
6. Scene-specific visual reference
7. General aesthetic direction

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

### Creator

- Identity matches canonical reference.
- Age presentation is consistent.
- Hijab identity is preserved.
- Body proportions remain consistent.

### Product

- Product matches reference.
- Color and shape are correct.
- Branding/labels are not invented.
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

## Handoff

Visual prompts are passed to:

- Image generation workflow
- 07_VIDEO_PROMPT_ENGINE
- 09_QUALITY_CONTROL

The storyboard remains the canonical source for scene intent. The visual prompt is an implementation layer, not a replacement for the storyboard.
