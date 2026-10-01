# Affilix — UGC Production Output Template v2

## Purpose

Standardize the final production output emitted by Affilix after all required production stages are complete.

This template is an output contract, not a creative engine. It assembles current runtime state without inventing facts, changing identity, or hiding uncertainty.

## 1. Run Metadata

- run_id:
- status:
- platform:
- format:
- requested_duration:
- creative_duration:
- duration_status:
- language:

Unknown values remain UNKNOWN.

## 2. Creative Brief

- objective:
- audience:
- content_format:
- mandatory_requirements:
- restrictions:
- CTA:
- source_notes:

## 3. Creator

- creator_id:
- creator_name:
- role:
- canonical_identity_reference:
- wardrobe:
- hijab:
- expression_direction:
- continuity_constraints:

Creator attributes must come from the Creator Library or explicit run input.

## 4. Product

- product_id:
- product_name:
- product_type:
- color:
- material:
- size:
- branding:
- configuration:
- approved_selling_points:
- claim_constraints:

UNKNOWN must remain UNKNOWN.

## 5. Canonical Niche Context

- niche:
- sub_niche:
- product_type:
- use_case:
- style:
- audience_context:
- confidence:
- evidence:

This is the single canonical runtime context for the run.

## 6. Content Strategy

- content_angle:
- narrative_formula:
- hook_strategy:
- demonstration_strategy:
- proof_strategy:
- reaction_strategy:
- CTA_strategy:
- claim_dependencies:

## 7. Hook

- hook_text:
- visual_hook:
- delivery_intent:
- duration_target:
- claim_dependencies:

## 8. Storyboard

Each scene contains:

- scene_id
- timecode
- duration
- story_purpose
- narrative_beat
- environment
- shot_type
- framing
- camera_angle
- camera_movement
- creator_action
- creator_orientation
- pose
- gesture
- expression
- gaze
- product_visibility
- product_interaction
- wardrobe
- hijab
- lighting
- background
- dialogue_intent
- on_screen_text
- sound_cue
- transition
- continuity_constraints
- reference_requirements
- claim_dependencies

Storyboard is the canonical creative temporal source for downstream production assets.

## 9. Visual Prompts

For every visual asset:

- asset_id:
- source_scene:
- creator_identity:
- product_identity:
- wardrobe:
- pose_expression:
- action:
- environment:
- composition:
- camera:
- lighting:
- visual_style:
- continuity_constraints:
- reference_priority:
- negative_constraints:

Visual prompts must not introduce unsupported physical attributes or product claims.

## 10. Video Prompts

For every video asset:

- asset_id:
- source_scene:
- creative_duration:
- generation_segment_id:
- generation_duration:
- provider_id:
- model_id:
- final_start_time:
- final_end_time:
- start_state:
- primary_action:
- secondary_natural_motion:
- camera_behavior:
- end_state:
- continuity_constraints:
- negative_motion_constraints:

Video prompts must preserve identity, product geometry, wardrobe/hijab coherence, and physical plausibility.

### Generation Segments

When provider duration limits require multiple clips, list:

- segment_id
- source_scene_id
- final_start_time
- final_end_time
- creative_duration
- generation_duration
- provider_id
- model_id
- assembly_order
- start_visual_state
- end_visual_state
- continuity_anchor
- status

Generation durations must be supported by the active provider profile.

## 11. Voice Script

For every spoken line:

- scene_id:
- exact_dialogue:
- delivery_intent:
- emotion:
- pace:
- emphasis:
- pause:
- lip_sync_note:
- CTA_note:
- claim_dependencies:

Voice must not fabricate personal experience or unsupported claims.

Voice timing follows the creative/storyboard timeline, not arbitrary provider segment boundaries.

## 12. CTA

- exact_text:
- delivery_intent:
- visual_support:
- offer_dependency:
- urgency_dependency:

Unsupported offer, discount, scarcity, or urgency remains UNKNOWN or is excluded.

## Assembly Rules

1. Assemble only from the current runtime state.
2. Never invent missing facts during assembly.
3. Never reclassify niche context during assembly.
4. Never modify creator identity.
5. Never modify product identity.
6. Never upgrade UNKNOWN into a fact.
7. Preserve source/provenance information where available.
8. The storyboard remains the creative temporal source of truth.
9. All downstream assets must trace back to a storyboard scene.
10. Provider constraints may change technical generation segmentation, not campaign duration.

## Completion

This output is emitted when all required production stages are current and validated. It is the final user-facing production output for the run.
