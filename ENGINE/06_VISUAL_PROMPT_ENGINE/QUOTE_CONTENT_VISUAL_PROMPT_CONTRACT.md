# Affilix Quote Content Visual Prompt Contract

## Canonical Identity

- Canonical workflow stage: Stage 07 — Visual Prompt
- Content mode: `QUOTE_CONTENT`
- Universal implementation: `ENGINE/06_VISUAL_PROMPT_ENGINE/`

## Applicability and Inputs

Required for every supported Quote Content format. Inputs are the current Stage 04 strategy and editorial context; Stage 06 storyboard and its reference graph for video formats; current Hook when applicable; optional creator reference only when explicitly required. No product facts, product references, or product demonstrations are expected unless the user has explicitly reclassified the brief as product-centered.

For `QUOTE_IMAGE`, create one prompt for the single requested static quote image. For video formats, create exactly one image prompt for each Storyboard-declared reference state. Do not collapse references or invent additional states.

## Prompt Authority

Every image prompt represents one frozen visual state, not a motion sequence. Preserve the editorial message and selected format's visible mechanism without adding story beats, unsupported biographical details, or a different message. Text content must be exact and readable if rendered in-image; when image models are unreliable at typography, explicitly specify layout and reserve a clean text-safe area, and carry exact text separately in production metadata.



### Locked Wardrobe and Environment Inheritance

Wardrobe and environment are inherited inputs, not fresh creative decisions, whenever they have already been selected or approved by the user or upstream configuration.

- `WARDROBE`: use the established wardrobe configuration/reference as-is. Do not choose a new outfit, hijab color, fabric, accessories, or styling. Do not restate speculative wardrobe details merely to fill the prompt template.
- `ENVIRONMENT`: use the established environment configuration/reference as-is. Do not invent or redesign the room, background, furniture, props, layout, palette, or location.
- If an approved visual reference is provided, treat it as the visual authority for the attributes it actually shows. Preserve unseen details as UNKNOWN rather than inventing them.
- If the upstream configuration already contains a wardrobe or environment, inherit it and refer to its approved reference/configuration. Do not ask the image model to select a replacement.
- A change is permitted only when explicitly requested or specified by the authoritative Storyboard state. Keep the override scoped to the changed attribute and validate affected downstream references.

### Background Reference Lock

When the user provides an approved background/environment reference, that reference is the sole visual authority for the background. The image prompt must explicitly instruct the image model to preserve the reference background as-is, including location/layout, architecture, furniture, objects, object placement, surface details, colors, perspective, depth, and visible lighting cues. Do not redesign, replace, extend, beautify, declutter, restyle, or invent background elements. The creator may be composited into the referenced environment only as needed; changes to the creator must not cause changes to the background. If no background reference is supplied, use only the established scene environment and do not claim a reference lock. Include the background reference in `environment_references` and continuity metadata when provided. For video, preserve the same background across every reference state and generation segment; only change it when the user explicitly requests a background change.Visual direction may define composition, typography style, contrast, palette, lighting, environment, camera/framing, and emotional tone. It must not invent a creator identity or imply that a fictional scene is a real user's personal experience.

For all Quote Content video formats, use `DIRECT_TO_CAMERA_TALKING_HEAD` by default. Each reference state should show the same creator addressing the camera in a vertical 9:16 medium close-up or close-up, with lens-level gaze, a relevant uncluttered background, and a specific expression/posture/gesture state tied to the storyboard beat. Across reference states, vary only what the action causes: posture, hand gesture, gaze break/return, and restrained expression. Keep creator identity, wardrobe, framing logic, lighting, and environment consistent. Do not substitute B-roll, cinematic scenery, a second character, or a montage for the talking-head performance unless explicitly requested by the user.

## Required Prompt Structure

Each user-facing prompt is one coherent Markdown code block using these sections:

```text
IMAGE PROMPT

REFERENCE STATE
SUBJECT
CREATOR
WARDROBE
PRODUCT
POSE & EXPRESSION
ENVIRONMENT
COMPOSITION
CAMERA
LIGHTING
VISUAL STYLE
NICHE CONTEXT
CONTINUITY
NEGATIVE CONSTRAINTS
FINAL IMAGE GENERATION INSTRUCTION
```

For Quote Content, use `PRODUCT: NOT APPLICABLE` unless product-centered content was explicitly requested. Use `CREATOR: NOT REQUIRED` when no creator is selected. Do not invent placeholder product facts.

For `QUOTE_IMAGE`, ensure the visual supports the primary statement, maintains legible hierarchy, sufficient contrast and negative space, and avoids fake quote marks/attribution. The image itself is a frozen layout, not a sequence.

For video-format reference prompts, explicitly specify `CAMERA: vertical 9:16, medium close-up/close-up, lens-level, stable framing`; `POSE & EXPRESSION` must identify the exact beat-specific delivery state. `WARDROBE` and `ENVIRONMENT` must inherit approved upstream configuration instead of selecting or redesigning them. `CONTINUITY` must preserve creator identity, inherited wardrobe, established environment, framing logic, and lighting baseline across references unless an explicit, validated change is required.

## Reference-State Invariants for Video Formats

Each prompt must map to exactly one declared reference:

- `reference_id`
- `reference_role`
- `reference_version`
- `source_scene_id`
- `source_beat_id`
- `continuity_lock`

Every storyboard-declared reference state produces exactly one prompt. A shared bridge reference uses the same ID and version at both adjacent scene boundaries. Never reinterpret an immutable bridge independently for each scene.

## Validation

Validate single-frame integrity, exact text/message fidelity, format mechanism visibility, continuity, non-fabrication, and reference coverage. Use `NEEDS_REFINEMENT` when the concept is safe but composition or readability is underspecified. Use `BLOCKED` when the source message, required reference, or continuity cannot be established without invention.

```yaml
stage: 07_VISUAL_PROMPT
content_mode: QUOTE_CONTENT
status: COMPLETED | BLOCKED
format_id:
prompts:
  - prompt_id:
    prompt_type: Image
    source_scene_id: null
    reference_id: null
    reference_role: STATIC_IMAGE | START | INTERMEDIATE | END | BRIDGE
    reference_version: null
    exact_text_content: []
    final_prompt:
    validation:
      single_frame: PASS | NEEDS_REFINEMENT
      text_fidelity: PASS | NEEDS_REFINEMENT
      format_mechanism: PASS | NEEDS_REFINEMENT
      continuity: PASS | NEEDS_REFINEMENT
      non_fabrication: PASS | BLOCKED
source_artifacts: []
provenance: []
source_commit_sha:
```

## Invalidation

Changes to editorial message, format, hook where visible, storyboard/reference graph, selected creator, or style constraints invalidate only the dependent prompts and transitions. Mark completed and wait for `/next`.
