# Affilix — Skill Runtime Regression Matrix

## Purpose

Validate the canonical ten-stage Skill workflow across active niches and failure-prone state conditions.

## Matrix

| ID | Scenario | Expected Result |
|---|---|---|
| R001 | Fashion normal | Canonical context + downstream stages remain synchronized |
| R002 | Beauty normal | Canonical context + downstream stages remain synchronized |
| R003 | Food normal | Canonical context + downstream stages remain synchronized |
| R004 | Home normal | Canonical context + downstream stages remain synchronized |
| R005 | UNKNOWN preservation | Missing evidence remains UNKNOWN |
| R006 | Source conflict | Explicit fact wins and conflict is surfaced |
| R007 | Cross-run isolation | Previous run state cannot leak into current run |
| R008 | Reclassification | Dependents become STALE and regenerate from the new canonical context |
| R009 | Action choreography | Scene action graph contains causal action beats and resulting states |
| R010 | Reference graph | Bridge references preserve exact scene-boundary continuity |
| R011 | Duration composition | Final duration equals requested duration exactly |
| R012 | Provider limitation | Unsupported duration composition becomes BLOCKED rather than silently rounded |
| R013 | Content Format selection | Stage 04 selects format using product behavior, proof, objective, creator, platform, and action clarity |
| R014 | Content Format evidence block | Format requiring unavailable proof is rejected rather than forced |
| R015 | Content Format conditional | Conditional selection records its explicit satisfiable condition |
| R016 | Content Format propagation | Selected format remains a downstream constraint until Stage 04 revision |

## Acceptance Rules

A runtime regression passes only if:
1. canonical stage order is respected,
2. niche context is created before downstream creative decisions,
3. creator and product identity remain locked,
4. UNKNOWN values remain UNKNOWN without evidence,
5. explicit facts outrank contextual interpretation,
6. material upstream changes invalidate affected downstream assets,
7. reclassification replaces rather than merges prior context,
8. no cross-run state leaks into the current run,
9. storyboard remains the canonical temporal/action source,
10. reference states and bridge references remain consistent,
11. requested final duration is preserved exactly,
12. Production Output contains only current, non-STALE required artifacts.
13. Format selection follows the registered algorithm and evidence constraints.
14. Blocked format selection remains blocked rather than inventing a creative choice.
15. Content Format and Content Angle remain distinct.
16. Downstream artifacts preserve the selected Content Format.

There is no QC stage or Final UGC Package contract in this regression matrix.

## Regression Result

Baseline: PASS by contract review against current `SKILL.md`, `WORKFLOW.md`, stage contracts, action/reference contracts, duration contract, and production output template.


### R017 — Content Format propagation to Visual Prompt
- Given a valid selected Content Format and completed Storyboard, Visual Prompt carries the same format constraint.
- Visual output remains a single frozen state and does not introduce a different format.

### R018 — Content Format propagation to Video Prompt
- Given a valid selected Content Format, Video Prompt preserves the format mechanism through action, product interaction, proof, and resulting state where applicable.
- A format revision invalidates affected Video Prompt artifacts.

### R019 — Content Format propagation to Voice Script
- Given a valid selected Content Format and spoken audio mode, Voice Script structures dialogue to support the selected format without inventing claims or experience.
- A format revision invalidates affected Voice Script artifacts.

13–16 remain valid for Stage 04 selection and propagation into Hook/Storyboard.
17–19 require Content Format continuity across Visual Prompt, Video Prompt, and Voice Script; a changed format must invalidate affected downstream artifacts.


### R020 — Content Format traceability at Production Output
- Production Output carries the selected Content Format and propagation status across required downstream artifacts.
- Missing, stale, or contradicted format state blocks final assembly.

### R021 — Content Format revision invalidation to Production Output
- A Stage 04 Content Format change makes affected downstream artifacts, including Production Output, STALE.

### R022 — Content Format mechanism in Hook
- A selected format must be materially expressed by the Hook's opening mechanism; metadata alone is insufficient.

### R023 — Content Format mechanism in Storyboard
- A selected format must be materially expressed through scene mechanism, product role, proof, and action; metadata alone is insufficient.

### R024 — Content Format revision invalidation to Storyboard
- Changing the selected format after Storyboard completion makes the affected Storyboard STALE rather than silently relabeling it.

### R025 — Content Format mechanism in Visual Prompt
- Frozen reference states must visibly preserve the selected format mechanism without temporal language or metadata-only compliance.

### R026 — Content Format revision invalidation to Visual Prompt
- Changing the selected format after Visual Prompt completion makes affected prompts STALE.

### R027 — Content Format mechanism in Video Prompt
- Video Prompt must preserve the selected format through causal action, product interaction, proof, and resulting state.

### R028 — Format-compatible motion beats generic catchiness
- Attention-grabbing motion cannot substitute for the selected format's causal mechanism.

### R029 — Content Format revision invalidation to Video Prompt
- Changing the selected format after Video Prompt completion makes affected prompts STALE.

### R030 — Content Format mechanism in Voice Script
- For spoken modes, Voice Script must materially express the selected format through dialogue structure, product role, proof language, and action alignment.
- Metadata-only format labeling fails validation.

### R031 — Format revision invalidation to Voice Script
- Changing the selected Content Format after Voice Script completion makes the Voice Script STALE.
- Existing dialogue must not be silently relabeled with the new format.

### R032 — No-spoken-voice exception

### R033 — Naturalism Is Not Generic Realism
- A prompt containing only "photorealistic", "realistic human movement", or "move naturally" without motivated action fails naturalism validation.
- Expected: `NEEDS_REFINEMENT`.

### R034 — Causal Human Timing
- A storyboard/video prompt that expresses notice → reach → grip adjustment → product action → reaction → resulting state when context supports it passes naturalism validation.
- Arbitrary fidgeting or random hesitation fails.
- Expected: causal timing `PASS`; arbitrary imperfection `NEEDS_REFINEMENT`.

### R035 — Bounded Micro-Motion
- Breathing, limited blinking, weight shift, posture adjustment, grip correction, restrained expression change, and realistic fabric/hijab response may support the primary action.
- Micro-motion must not invent a competing action or alter a reference state.
- Expected: bounded support motion `PASS`; uncontrolled/random motion `NEEDS_REFINEMENT`.

### R036 — Product Physical Causality
- Product state, position, orientation, grip, and contact must change only through explicit physical interaction.
- Drift, teleportation, duplication, unexplained morphing, or unexplained state change fails.
- Expected: causal interaction `PASS`; unsupported transition `BLOCKED`.

### R037 — Gaze and Camera Motivation
- Gaze changes and camera reframing must respond to the creator/product/camera relationship.
- Random shake, excessive jitter, locked gaze without context, or unexplained zoom fails naturalism validation.
- Expected: motivated behavior `PASS`; arbitrary behavior `NEEDS_REFINEMENT`.

### R038 — Frozen Visual Naturalism
- Visual Prompt must show a plausible frozen human state with deterministic posture, grip, gaze, expression, and product relationship.
- It must not encode motion sequences to simulate naturalism.
- Expected: plausible frozen state `PASS`; ambiguous or synthetic pose `NEEDS_REFINEMENT`.

### R039 — Spoken Naturalism Without Fabrication
- Voice naturalization may improve phrasing, rhythm, pauses, breathing, and emphasis.
- It must not invent personal experience, unsupported outcomes, urgency, scarcity, or claims.
- Expected: conversational supported delivery `PASS`; mechanically promotional delivery `NEEDS_REFINEMENT`; unsupported factual invention `BLOCKED`.

### R040 — Naturalism Revision Invalidation
- A material naturalism change to Storyboard invalidates affected Visual Prompt, Video Prompt, Voice Script, and Production Output artifacts as required by dependency.
- Existing downstream artifacts must not be silently relabeled as naturalized.
- Expected: affected artifacts `STALE`.

### R041 — Naturalism Preserves Content Format
- Naturalism may improve action realism but cannot replace the selected Content Format mechanism with generic attention-grabbing motion.
- Expected: format mechanism preserved and naturalism `PASS`; format substitution `NEEDS_REFINEMENT`.

- When audio_mode=NO_SPOKEN_VOICE, Stage 09 is SKIPPED and Content Format voice validation is NOT_REQUIRED.
### R042 — Storyboard Beat Timing Contract
- Major sequential storyboard actions expose narrative timing windows without confusing them with provider generation segments.
- Expected: explicit timing PASS; ambiguous ordering NEEDS_REFINEMENT.

### R043 — Storyboard Action Priority
- Primary action, secondary responsive action, supporting motion, and bounded micro-motion are distinguishable.
- Expected: priority hierarchy PASS; competing/random secondary motion NEEDS_REFINEMENT.

### R044 — Storyboard Product/Hand/Contact State
- Product manipulation preserves hand ownership, contact state, product state, and product-follow-hand behavior.
- Expected: complete causal state PASS; missing or contradictory ownership/contact state NEEDS_REFINEMENT.

### R045 — Storyboard Uncaused Product State Blocks
- A product position, orientation, or state change without corresponding physical interaction is invalid.
- Expected: BLOCKED.

### R046 — Storyboard Transition Contract
- Reference transitions declare allowed changes, invariants, and resulting reference.
- Expected: deterministic transition PASS; silent downstream state invention NEEDS_REFINEMENT.

### R047 — Storyboard Dialogue Anchors
- Spoken meaning is anchored to an action window and target reference without replacing Stage 09 Voice Script.
- Expected: anchor PASS; storyboard-authored final dialogue NEEDS_REFINEMENT.

### R048 — Product Has a Job Requires Action
- PRODUCT_HAS_A_JOB must stage concrete need → product performs assigned job → resulting task state.
- Expected: product-job mechanism PASS; pickup/presentation-only sequence NEEDS_REFINEMENT.

### R049 — Storyboard Production Readiness Gate
- Storyboard with missing material timing, state, transition, proof, or action-causality fields cannot advance to downstream prompt generation.
- Expected: NEEDS_REFINEMENT; impossible/unsupported behavior remains BLOCKED.

### R050 — Storyboard Is Downstream Creative Authority
- Visual Prompt, Video Prompt, and Voice Script must implement the current Storyboard rather than reinterpret it.
- Expected: downstream elaboration preserves Storyboard semantics; new creative decisions make the affected artifact STALE/invalid and require Storyboard revision.

### R051 — Visual Prompt Cannot Override Storyboard State
- A Visual Prompt that depicts a different product/creator/reference state than the current Storyboard fails downstream authority validation.
- Expected: NEEDS_REFINEMENT or STALE; no silent state substitution.

### R052 — Video Prompt Cannot Invent Story Actions
- A Video Prompt may add technical motion detail only when it preserves Storyboard action, causality, timing, and resulting state.
- Expected: bounded implementation detail PASS; new story action NEEDS_REFINEMENT/STALE until Storyboard is revised.

### R053 — Downstream Elaboration Is Allowed
- Visual Prompt may refine frozen composition; Video Prompt may refine motion timing/technical segmentation; Voice Script may refine wording/delivery, provided Storyboard semantic state remains unchanged.
- Expected: implementation elaboration PASS.


### R054 — Video Prompt Count Matches Scene Count
- Given a completed Storyboard with N scenes, Stage 09 produces exactly N user-facing Video Prompts.
- Multiple technical generation segments inside a scene do not create additional user-facing prompts.
- Multiple scenes must not be merged into one Video Prompt.
- Expected: `scene_count == video_prompt_count`; mismatch is `NEEDS_REFINEMENT` and blocks Stage 09 completion.

### R055 — High-Complexity Scene Reference Density
- Given a high-complexity scene with multiple material action states, Storyboard plans a meaningful multi-reference trajectory and targets six reference states when justified.
- Expected: ordered reference plan `PASS`; redundant quota-driven references `NEEDS_REFINEMENT`.

### R056 — Visual Prompt Reference Cardinality
- Given a Storyboard scene with N declared reference states, Stage 07 produces exactly N static image prompts.
- Expected: `reference_prompt_count == declared_reference_state_count`.

### R057 — Video Prompt Uses Full Reference Trajectory
- Given a scene with ordered references R01 → R02 → R03 → R04 → R05 → R06, Stage 09 preserves the trajectory inside one scene-level Video Prompt and does not skip or create additional prompts for intermediate states.
- Expected: one Video Prompt, complete trajectory preserved, critical states protected.

### R058 — Reference Revision Invalidation
- Changing any material reference state or the Reference Plan makes affected Visual Prompt and Video Prompt artifacts STALE, including transitions touching the changed state.
- Expected: affected downstream artifacts `STALE`.

### R059 — Bridge Reference Remains Immutable
- Scene N END and Scene N+1 START use the exact same bridge reference version.
- Expected: bridge continuity `PASS`; version mismatch `NEEDS_REFINEMENT`.

### R060 — Six References Do Not Change Video Prompt Count
- A scene containing six visual reference states still produces exactly one user-facing Video Prompt.
- Expected: scene-level prompt count remains `1`.

### R061 — Intermediate Reference Is Not a Generation Segment
- A reference state is a frozen visual checkpoint, not a provider generation segment.
- Expected: reference count and generation-segment count remain independently validated.
