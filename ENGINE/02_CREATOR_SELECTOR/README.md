# Affilix — Creator Selector

## Canonical Stage Identity

- Canonical workflow stage: Stage 04 — Creator
- Implementation path: `ENGINE/02_CREATOR_SELECTOR/`
- The numeric prefix in the implementation directory is NOT a workflow stage ID.
- Do not infer ordering, prerequisites, or downstream dependencies from the directory prefix.
- Resolve workflow stage identity exclusively from `ENGINE/WORKFLOW.md`.

## Purpose

The Creator Selector chooses and loads the appropriate creator identity from CREATOR_LIBRARY based on the normalized campaign brief.

It does not redesign the creator. It matches the brief to an existing approved creator identity.

## Input

The selector receives:

- Normalized brief from 01_BRIEF_ANALYZER
- Available creator records
- Creator identity data
- Creator profile data
- Visual references
- Wardrobe data
- Expression library
- Pose library

## Output

Return:

### Selected Creator

- Creator ID
- Creator name
- Selection status: Selected / Needs Clarification / No Match
- Match rationale
- Loaded identity sources
- Loaded style/profile sources
- Required references

### Creator Constraints

- Identity locks
- Appearance locks
- Body locks
- Hijab/headwear requirements when applicable
- Style constraints
- Speaking/persona constraints
- Campaign-specific constraints

### Unresolved Requirements

List only creator requirements that cannot be resolved from the available library.

## Selection Logic

Evaluate creator compatibility against:

1. Explicit campaign creator requirement
2. Explicit demographic requirement
3. Required niche or content category
4. Platform/content-format compatibility
5. Visual style compatibility
6. Persona and communication compatibility
7. Product/category compatibility
8. Required wardrobe or appearance constraints
9. Reference availability

Explicit requirements have higher priority than inferred creative preferences.

## Match Status

### Selected

Use when one approved creator satisfies the required constraints.

### Needs Clarification

Use when multiple creators satisfy a mandatory requirement but the brief does not specify which one to use.

### No Match

Use when no approved creator can satisfy a mandatory requirement.

Do not create a new creator automatically.

## Creator Loading

When a creator is selected, load the relevant assets:

1. character_identity.md
2. creator_profile.md
3. visual_reference/README.md
4. Approved visual references relevant to the brief
5. wardrobe/README.md
6. Approved wardrobe assets relevant to the scene
7. expressions/README.md and approved expression assets when required
8. poses/README.md and approved pose assets when required

The selected creator becomes the identity source for downstream engines.

## Identity Preservation

Creator selection must never silently alter:

- Face identity
- Apparent age
- Core body proportions
- Skin identity
- Canonical hijab identity
- Other approved identity locks

Wardrobe, expression, pose, lighting, camera, and environment may vary within approved rules.

## Hijabi Creator Handling

If a selected creator has a canonical hijab identity:

- Preserve hijab coverage in standard scenes.
- Do not expose hair or uncovered neck unless explicitly requested.
- Treat hijab styling as a controlled wardrobe/style variable.
- Do not treat a change in hijab color, fabric, or drape as a new creator identity.

## Reference Priority

When creator references conflict:

1. Latest explicit user instruction
2. Approved canonical creator identity
3. Approved dedicated attribute reference
4. Approved style/wardrobe reference
5. Scene-specific reference
6. Older supporting reference

A scene-specific reference may modify scene styling but must not silently replace canonical identity.

## No Invented Creator Data

If a required creator attribute is marked [DEFINE], unknown, or missing:

- Keep it unknown.
- Do not infer it from stereotypes.
- Do not invent a biography, personality trait, body measurement, speaking style, or lifestyle fact.

## Match Rationale

Rationale must be factual and traceable.

Good:
- "Rositasari matches the explicit requirement for a young female fashion creator and has an approved hijabi identity."

Bad:
- "Rositasari is the perfect creator."

The selector describes compatibility, not subjective superiority.

## Handoff

The selected creator package is passed to:

- 03_CONTENT_STRATEGY
- 04_HOOK_ENGINE
- 05_STORYBOARD_ENGINE
- 06_VISUAL_PROMPT_ENGINE
- 07_VIDEO_PROMPT_ENGINE
- 08_VOICE_SCRIPT_ENGINE
- 09_QUALITY_CONTROL
