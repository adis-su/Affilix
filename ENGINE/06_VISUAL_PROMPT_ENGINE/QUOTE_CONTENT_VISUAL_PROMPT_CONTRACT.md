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

Visual direction may define composition, typography style, contrast, palette, lighting, environment, camera/framing, and emotional tone. It must not invent a creator identity or imply that a fictional scene is a real user's personal experience.

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
status: COMPLETED | NEEDS_REFINEMENT | BLOCKED
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
