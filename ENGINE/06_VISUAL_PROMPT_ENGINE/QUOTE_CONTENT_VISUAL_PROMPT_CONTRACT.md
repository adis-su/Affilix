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

- The final prompt's `WARDROBE` section must contain exactly this sentence and no additional description: `Sesuai referensi gambar yang diupload user.`
- The final prompt's `ENVIRONMENT` section must contain exactly this sentence and no additional description: `Sesuai referensi gambar yang diupload user.`
- These are fixed literal output strings, not paraphrasable guidance. Do not replace them with an English translation, synonyms, inferred details, or an expanded description.
- "Gambar yang diupload user" means the reference image the user uploads directly to the external AI image-generation provider, not an image stored in the Affilix GitHub repository or uploaded into Affilix.
- Affilix only emits these literal prompt instructions. It does not need to host, store, fetch, inspect, or verify the provider-side image, and must not claim it can access that image.
- The external image-generation provider must receive the user's reference image separately through its own upload/reference-image interface. The generated prompt tells that provider to use the uploaded image as the visual authority for wardrobe and environment.
- Do not choose a new outfit, hijab color, fabric, accessories, styling, room, background, furniture, props, layout, palette, or location in the prompt.
- Do not block or alter the required literal strings just because Affilix cannot see the provider-side upload. Do not claim that Affilix has inspected or verified the image.
- If an approved visual reference is provided, treat it as the visual authority for the attributes it actually shows. Preserve unseen details as UNKNOWN rather than inventing them.
- If the upstream configuration already contains a wardrobe or environment, inherit it and refer to its approved reference/configuration. Do not ask the image model to select a replacement.
- A change is permitted only when explicitly requested or specified by the authoritative Storyboard state. Keep the override scoped to the changed attribute and validate affected downstream references.

### Background Reference Lock

When the user uploads an approved background/environment reference directly to the external AI image-generation provider, that provider-side reference is the sole visual authority for the background. Affilix does not host or inspect this image; the user supplies it separately to the provider. The fixed `ENVIRONMENT` prompt sentence instructs the provider to use that image. Do not redesign, replace, extend, beautify, declutter, restyle, or invent background elements. For video, the user must supply the same reference image to the provider for every relevant generation request unless they explicitly authorize a change.Visual direction may define composition, typography style, contrast, palette, lighting, environment, camera/framing, and emotional tone. It must not invent a creator identity or imply that a fictional scene is a real user's personal experience.

For all Quote Content video formats, use `DIRECT_TO_CAMERA_TALKING_HEAD` by default. Each reference state should show the same creator addressing the camera in a vertical 9:16 medium close-up or close-up, with lens-level gaze, a relevant uncluttered background, and a specific expression/posture/gesture state tied to the storyboard beat. Across reference states, vary only what the action causes: posture, hand gesture, gaze break/return, and restrained expression. Keep creator identity, wardrobe, framing logic, lighting, and environment consistent. Do not substitute B-roll, cinematic scenery, a second character, or a montage for the talking-head performance unless explicitly requested by the user.

## Required Prompt Structure

Each user-facing prompt is one coherent Markdown code block using these sections:

```text
IMAGE PROMPT

REFERENCE STATE
SUBJECT
CREATOR
WARDROBE
Sesuai referensi gambar yang diupload user.
PRODUCT
POSE & EXPRESSION
ENVIRONMENT
Sesuai referensi gambar yang diupload user.
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

For video-format reference prompts, explicitly specify `CAMERA: vertical 9:16, medium close-up/close-up, lens-level, stable framing`; `POSE & EXPRESSION` must identify the exact beat-specific delivery state. The `WARDROBE` and `ENVIRONMENT` sections must each contain only the exact sentence `Sesuai referensi gambar yang diupload user.` This refers to an image the user uploads separately to the external AI image-generation provider, not to an Affilix repository asset. Affilix emits the prompt but does not access or verify the provider-side upload. `CONTINUITY` must preserve creator identity, wardrobe/environment as shown in the provider-side reference, framing logic, and lighting baseline across references unless an explicit, validated change is required.

## Reference-State Invariants for Video Formats

Each prompt MUST map to exactly one complete, declared Stage 06 reference state and carry:
- `reference_id`
- `reference_role`
- `reference_version`
- `source_scene_id`
- `source_beat_id`
- `sequence_index`
- `state_summary`
- `continuity_lock`
- the applicable ordered `reference_trajectory` and transition IDs as traceability metadata

The incoming video storyboard MUST expose `metadata.storyboard_id` and `metadata.storyboard_version`; `source_commit_sha` alone is not artifact identity. Stage 07 records the exact `(storyboard_id, storyboard_version)` pair in `source_artifacts` and binds every prompt to that same pair. Mixing states across storyboard versions is invalid. Stage 07 must first validate the incoming storyboard. If a required reference ID, version, source beat, sequence index, state summary, ordered trajectory, or transition is missing, do not invent it in the image prompt and do not report Stage 07 as completed. Return a specific `NEEDS_REFINEMENT` dependency report identifying the exact scene and missing fields, and require Stage 06 to regenerate/revalidate its reference plan. If a value can be deterministically populated from the current storyboard's existing beat IDs and states without changing creative meaning, that repair belongs in Stage 06, followed by revalidation.

Every storyboard-declared reference state produces exactly one prompt; no missing or extra prompts are allowed. A shared bridge reference uses the same ID and version at both adjacent scene boundaries. Never reinterpret an immutable bridge independently for each scene. Validate `prompt_count == declared_reference_state_count` across the entire active storyboard artifact, not merely per scene, and preserve storyboard ordering. If a bridge appears at both scene boundaries, generate one prompt for the one canonical bridge state; do not duplicate it because it is referenced by two scenes. Validate the unique canonical reference-state count after bridge deduplication.

## Deterministic Reference Coverage Validation

Before generation, validate the full Stage 06 artifact: every state has non-empty `reference_id`, `reference_version`, `source_scene_id`, `source_beat_id`, `sequence_index`, `state_summary`, and `continuity_invariants`; every source scene and beat resolves within the pinned storyboard artifact; sequence indices are unique and contiguous per scene; the ordered trajectory exactly equals the Reference Plan; for each scene with n states there are exactly n−1 valid adjacent transition records; every `reference_after` resolves; and bridge identity/version matches at both scene boundaries. Then generate exactly one prompt per unique declared canonical state, preserving source order. If any check fails, return `NEEDS_REFINEMENT` with scene ID and missing/invalid fields and do not claim completion. Do not repair Stage 06 data inside Stage 07.

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
source_artifacts:
  - artifact_type: 06_STORYBOARD
    artifact_id: required storyboard_id from source
    artifact_version: required storyboard_version from source
    source_commit_sha: exact source commit SHA
provenance: []
source_commit_sha:
```

## Source Freshness and Cross-Stage Handoff

For video formats, Stage 07 must record the exact current Stage 06 storyboard artifact ID/version in `source_artifacts` and preserve its `source_commit_sha`. Validate that every prompt maps to a declared reference state in that exact storyboard artifact, including `reference_id`, `reference_version`, `source_scene_id`, `source_beat_id`, and `sequence_index`. Do not combine reference states from multiple storyboard versions or repository commits. If the storyboard source is missing, stale, or from a different pinned commit, block completion until Stage 06 is current and valid.

Stage 07 and Stage 08 are parallel descendants of Stage 06. Stage 07 must not require a Voice Script, and Stage 08 must not require Visual Prompt. Stage 09 is the integration point and may consume only current, mutually compatible Stage 06/07/08 artifacts. A Stage 06 revision invalidates affected Stage 07 prompts and Stage 08 dialogue assets; Stage 09 must not combine a current visual artifact with a stale script or a script tied to a different storyboard source.

## Invalidation

Changes to editorial message, format, hook where visible, storyboard/reference graph, selected creator, or style constraints invalidate only the dependent prompts and transitions. Mark completed and wait for `/next`.
