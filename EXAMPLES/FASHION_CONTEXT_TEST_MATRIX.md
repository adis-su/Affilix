# Fashion Context Test Matrix

Status: ACTIVE

## Purpose

Validate that Fashion sub-niche, use case, and style context propagates through the shared Affilix pipeline without changing product facts or creator identity.

## Test Matrix

| Test | Sub-Niche | Product Type | Use Case | Style |
|---|---|---|---|---|
| F001 | Modest Fashion | Dress | Work | Minimalist |
| F002 | Hijab | Hijab | Everyday | Natural |
| F003 | Streetwear | Top | Everyday | Street |
| F004 | Activewear | Sports Top | Exercise | Sporty |
| F005 | Bags | Bag | Everyday | Minimalist |
| F006 | Jewelry | Jewelry | Event | Elegant |

## Cross-Test Acceptance Criteria

Every test must verify:

- Fashion resolves as ACTIVE.
- Sub-niche resolves correctly.
- Product type remains independent from sub-niche.
- Use case and style are loaded only when supported.
- Rositasari canonical identity remains stable.
- Canonical hijab remains covered and coherent.
- Product identity remains unchanged.
- Context changes strategy/hook/scene framing where appropriate.
- Context does not create unsupported product claims.
- Storyboard, visual, video, and voice remain synchronized.
- QC validates layered context.
- No invented fit, comfort, fabric, durability, quality, popularity, origin, or personal experience.

## Context Differentiation

A passing implementation must produce materially different contextual treatment where the sub-niche differs, while keeping the same product facts.

For example, Workwear may use an office-ready preparation context when supplied, while Streetwear may use an urban styling context. Neither may invent a workplace, trend popularity, or product performance claim.

## Status

Matrix defined. Individual end-to-end fixtures are added progressively.
