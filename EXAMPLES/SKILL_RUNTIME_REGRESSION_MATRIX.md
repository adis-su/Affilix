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
- For spoken modes, Voice Script must materially express the selected format through dialogue structure, product role, proof language, action alignment, and compatible CTA.
- Metadata-only format labeling fails validation.

### R031 — Format revision invalidation to Voice Script
- Changing the selected Content Format after Voice Script completion makes the Voice Script STALE.
- Existing dialogue must not be silently relabeled with the new format.

### R032 — No-spoken-voice exception
- When audio_mode=NO_SPOKEN_VOICE, Stage 09 is SKIPPED and Content Format voice validation is NOT_REQUIRED.