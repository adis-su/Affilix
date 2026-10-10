# Affilix — Hook Engine

## Canonical Stage Identity

- Canonical workflow stage: Stage 05 — Hook
- Implementation path: `ENGINE/04_HOOK_ENGINE/`
- The numeric prefix in the implementation directory is NOT a workflow stage ID.
- Do not infer ordering, prerequisites, or downstream dependencies from the directory prefix.
- Resolve workflow stage identity exclusively from `ENGINE/WORKFLOW.md`.

## Purpose

Generate opening concepts that capture attention while remaining faithful to the active mode's validated strategy and context. For `UGC_AFFILIATE`, preserve product facts and campaign constraints. For `QUOTE_CONTENT`, preserve editorial pillar, format, audience, message, takeaway, and sensitivity constraints without inventing personal testimony.

## Mode Routing

- `UGC_AFFILIATE`: use the existing product-aware hook contract below.
- `QUOTE_CONTENT`: use the editorial hook contract in `QUOTE_CONTENT_HOOK_CONTRACT.md`. Do not require product identity, product connection, product proof, or a creator unless the selected format requires one.

## Input

- Content strategy, including selected Content Format and Content Angle
- Normalized brief
- Selected creator
- Product identity
- Verified product facts
- Supported benefits
- Available evidence
- Platform requirements
- Campaign constraints
- Loaded Niche Context

## Context-Aware Hooking

Use authoritative:

- Sub-Niche
- Product Type
- Use Case
- Style / Aesthetic
- Audience Context

to shape the opening situation, language, visual trigger, and product connection.

Example:

`Fashion + Workwear + Dress + Minimalist`

may produce a hook around getting ready for a simple work outfit.

It must not produce unsupported claims such as comfort, premium material, perfect fit, or suitability for every workplace.

## Output

Each candidate contains:

- Hook ID
- Hook type
- Hook text or visual concept
- Delivery mode
- Audience trigger
- Product connection
- Context connection
- Strategy connection
- Required visual action
- Required proof
- Claim risk
- Status

## Content Format Constraint

The selected Content Format is a required upstream creative constraint.

Hooks MUST:

- reinforce the selected format's story mechanism
- satisfy the format's requirements
- use hook patterns compatible with the selected format
- avoid introducing a different content format through the opening beat

The Hook Engine may vary the hook type and wording, but it must not silently replace the selected Content Format.

Record the selected format connection in each candidate's `strategy_connection`.

## Format Mechanism Validation

Content Format is not satisfied by copying `format_id` into metadata. The hook's opening action and narrative trigger must make the selected format recognizable in the first beat.

For every selected format, validate the hook against its registered mechanism:

| Content Format | Hook must establish |
|---|---|
| BEAUTY_CRIME_SCENE | a recognizable problem/case and an investigative or evidence-oriented opening |
| PRODUCT_HAS_A_JOB | a concrete need/mission that gives the product a specific job |
| BEAUTY_MYTH_LAB | a testable question or beauty assumption that can be examined |
| PRODUCT_INTERROGATION | a product question/property that will be inspected or demonstrated |
| ONE_PRODUCT_THREE_PERSONALITIES | the premise that one product will serve multiple legitimate modes/contexts |
| SILENT_BEAUTY_TEST | a visually legible action that can carry meaning without relying on spoken explanation |
| BEAUTY_ROUTINE_UNDER_PRESSURE | a real situational constraint that triggers the routine task |
| ANTI_TUTORIAL | a truthful expectation/qualification that reframes product fit |
| LIFESTYLE_INTEGRATION | a believable context or routine in which the product naturally belongs |
| PROBLEM_SOLUTION_MISSION | a concrete problem and mission-oriented action path |

### Hook Format Validation

A Hook is `VIABLE` only when:

1. the opening beat visibly or verbally establishes the selected format mechanism;
2. the required action is executable with the supplied product and creator;
3. required proof is available or explicitly marked as conditional;
4. the hook does not imply a different registered format;
5. the hook preserves the selected Content Angle and campaign objective;
6. format-specific claim constraints remain intact.

A hook that merely contains the product name while using a generic attention pattern does **not** pass Content Format validation.

If the selected format is changed, existing Hook candidates become STALE and must be regenerated or revalidated.

## Hook Types

- Problem
- Curiosity
- Relatable
- Demonstration
- Product
- Pattern Interrupt
- Question
- Story
- Objection

## Hook Selection Logic

Evaluate:

1. Selected Content Format alignment
2. Campaign objective
2. Audience relevance
3. Sub-niche/context relevance
4. Content-angle alignment
5. Product relevance
6. Evidence availability
7. Creator fit
8. Platform suitability
9. Clarity
10. Claim safety
11. Visual execution feasibility

Do not rank hooks as objectively best or worst. Return viable candidates with factual rationale.

## Hook Truth Rules

Never use unsupported:

- Superlatives
- Guaranteed outcomes
- Exact performance numbers
- Medical outcomes
- Fabricated testimonials
- Fake scarcity
- Fake discounts
- Fake urgency
- False comparisons
- False personal experience

Context labels are not product evidence.

## Creator Fit

Respect:

- Creator persona
- Speaking style
- Visual identity
- Hijab identity when applicable
- Approved expression range
- Approved pose range

Do not invent signature phrases or personal experiences.

## Visual Hook

Specify:

- Initial frame
- Creator action
- Product visibility
- Camera framing
- Viewer-facing action
- Context cues
- Transition into next beat

The hook must be physically and visually executable.

## Handoff

For `QUOTE_CONTENT`, the selected hook becomes the opening editorial beat for the applicable format. For video formats it passes to Storyboard and downstream production. For `QUOTE_IMAGE`, Stage 05 may be skipped only as explicitly permitted by the editorial strategy contract.

For `UGC_AFFILIATE`, the approved hook becomes the opening beat for:

- 05_STORYBOARD_ENGINE
- 06_VISUAL_PROMPT_ENGINE
- 07_VIDEO_PROMPT_ENGINE
- 08_VOICE_SCRIPT_ENGINE
