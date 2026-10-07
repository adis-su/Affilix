# Affilix — UGC Naturalism Fixtures v1

## Purpose
Deterministic fixtures for validating behaviorally believable UGC across Storyboard, Visual Prompt, Video Prompt, Voice Script, and Production Output.

## F001 — Generic Realism Must Not Pass
Input: photorealistic creator moves naturally and presents the product, with no trigger, intention, causal interaction, gaze logic, or resulting state.
Expected: NEEDS_REFINEMENT. Generic realism language is insufficient.

## F002 — Causal Action Passes
Input: creator notices the product, briefly keeps attention on the mirror, reaches with the right hand, adjusts grip once, glances at the label, turns the product toward camera, then returns toward a relaxed hand position.
Expected: PASS. Trigger, intention, action, gaze, grip, timing, and resulting state are explicit.

## F003 — Random Imperfection Fails
Input: creator randomly fidgets, shakes head, blinks repeatedly, changes gaze, and shifts weight without relation to the action.
Expected: NEEDS_REFINEMENT. Naturalism is bounded and motivated, not random.

## F004 — Product Causality Passes
Input: hand contacts product, grip changes before lifting, product orientation follows the hand, product state changes only after explicit manipulation, target reference matches resulting state.
Expected: PASS.

## F005 — Product Teleportation Blocks
Input: product changes position or orientation without hand contact or another physical cause.
Expected: BLOCKED.

## F006 — Camera and Gaze Are Motivated
Input: creator looks from product to camera during presentation; camera performs a small product-following reframing adjustment; no random shake or abrupt zoom.
Expected: PASS.

## F007 — Frozen Visual State
Input: Visual Prompt shows one deterministic posture, hand grip, gaze, expression, product state, and environment.
Expected: PASS. No temporal motion sequence is encoded.

## F008 — Spoken Naturalization Without Fabrication
Input: Voice Script uses shorter phrases, natural pauses, restrained emphasis, and conversational rhythm without invented experience or unsupported product result.
Expected: PASS.

## F009 — Naturalism Cannot Replace Content Format
Input: selected format BEAUTY_CRIME_SCENE, but video uses realistic handheld movement and expressive gestures without the required case/problem or investigation mechanism.
Expected: NEEDS_REFINEMENT. Naturalism does not excuse Content Format failure.

## F010 — Upstream Naturalism Revision
Input: completed Storyboard contains synthetic-looking action timing and is revised to change trigger, action timing, and resulting state.
Expected: affected Visual Prompt, Video Prompt, Voice Script, and Production Output become STALE as required by dependency.

## Validation Rules
1. Naturalism is cross-stage, not a separate workflow stage.
2. Physical plausibility and action causality outrank generic realism wording.
3. Human timing may be imperfect but must remain motivated.
4. Micro-motion is bounded and cannot invent new actions.
5. Product interaction must obey physical causality.
6. Gaze and camera behavior must have contextual motivation.
7. Visual Prompt remains a frozen state.
8. Voice naturalization never authorizes unsupported claims or invented experience.
9. Naturalism cannot replace Content Format or Creator/Product identity constraints.
10. Final Production Output may only preserve validated upstream naturalism state.