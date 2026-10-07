# Affilix — Hook Engine

## Canonical Stage Identity

- Canonical workflow stage: Stage 05 — Hook
- Implementation path: `ENGINE/04_HOOK_ENGINE/`
- The numeric prefix in the implementation directory is NOT a workflow stage ID.
- Do not infer ordering, prerequisites, or downstream dependencies from the directory prefix.
- Resolve workflow stage identity exclusively from `ENGINE/WORKFLOW.md`.

## Purpose

Generate opening concepts that capture attention while remaining faithful to approved strategy, creator identity, product facts, campaign constraints, and loaded niche context.

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

Approved hook becomes the opening beat for:

- 05_STORYBOARD_ENGINE
- 06_VISUAL_PROMPT_ENGINE
- 07_VIDEO_PROMPT_ENGINE
- 08_VOICE_SCRIPT_ENGINE
