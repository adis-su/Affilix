# Affilix — Content Mode Routing Regression Fixtures

## Purpose

These fixtures validate the Phase 01 routing foundation. They do not claim that the Quote Content strategy or production engines are complete.

Canonical routing contract: `ENGINE/CONTENT_MODE_ROUTING_CONTRACT.md`.

## CM-001 — Explicit UGC Request Preserves Existing Intake

**Input**

- User invokes `/Affilix` and explicitly asks to make a product affiliate video.
- User supplies a product name and product reference.

**Expected**

- `run.content_mode = UGC_AFFILIATE`
- Do not show the mode selector again.
- Require existing UGC Product Intake and campaign requirements.
- Product reference research, claims validation, creator resolution, and existing downstream contracts remain in force.
- No UGC stage or validation is removed by the routing change.

**Fail if**

- Product intake is bypassed.
- The run is silently classified as `QUOTE_CONTENT`.
- Existing UGC requirements are weakened.

## CM-002 — Ambiguous New Run Requires Mode Selection

**Input**

- User invokes `/Affilix` without a product brief or explicit content mode.

**Expected**

- Show the Content Mode Selector.
- Do not inherit content mode or artifacts from another run.
- Do not begin product research until `UGC_AFFILIATE` is selected or explicitly established by the user.

**Fail if**

- The runtime silently assumes UGC mode.
- Product, creator, storyboard, or prompt state leaks from another run.

## CM-003 — Quote Content Does Not Require a Product

**Input**

- User selects `QUOTE_CONTENT`.
- User provides a topic about the emotional load of household responsibilities and a target audience of wives and mothers.
- No product name or product URL is supplied.

**Expected**

- `run.content_mode = QUOTE_CONTENT`
- Stage 01 accepts the editorial brief without requesting product identity.
- Preserve explicit and inferred provenance.
- Do not create product facts, product claims, product demonstrations, or fake product references.
- Editorial context may proceed only through implemented mode-specific contracts.

**Fail if**

- Product fields are treated as mandatory.
- The runtime fabricates a product to satisfy the UGC schema.

## CM-004 — Unsupported Quote Engine Must Block

**Input**

- Quote Content Stage 01 and Stage 02 are complete.
- The next required mode-specific stage has no implemented Quote Content contract.

**Expected**

- Block the affected stage with `QUOTE_CONTENT_ENGINE_NOT_IMPLEMENTED`.
- Preserve completed upstream artifacts.
- Do not invoke a product-centered engine as a fallback.
- Do not claim that the production output is complete.

**Fail if**

- UGC product-proof scoring runs on an editorial quote brief.
- A complete production output is claimed without required current assets.

## CM-005 — Content Mode Revision Invalidates Cross-Mode State

**Input**

- An active `UGC_AFFILIATE` run has completed stages and downstream assets.
- The user changes the run to `QUOTE_CONTENT`.

**Expected**

- Treat the mode change as a new isolated run state or invalidate every mode-dependent artifact.
- Do not reuse product, claims, creator, strategy, storyboard, visual, voice, video, or production artifacts unless independently regenerated and validated under the new mode.
- Record the mode and source repository commit for traceability.

**Fail if**

- UGC artifacts remain marked current in the Quote Content run.
- The runtime silently mutates the old run's mode while preserving incompatible artifacts.

## CM-006 — Canonical Stage Registry Remains Stable

**Input**

- Runtime resolves a stage for either supported mode.

**Expected**

- Stage IDs remain 01–10 and resolve only through `ENGINE/WORKFLOW.md`.
- Mode-specific routing controls applicability, skips, and blockers.
- Engine directory prefixes are never used as stage IDs.
- `/next` remains progression only, never approval.

**Fail if**

- A new numbered stage is introduced for mode selection.
- Stage order is inferred from folder names.
- A skip is treated as generated output or approval.

## Phase 01 Acceptance

Phase 01 is accepted when the mode contract, entrypoint, Skill, canonical workflow, runtime state contract, Brief Analyzer, and repository loader agree on:

- the two registered mode values,
- isolated mode-specific intake,
- no product requirement in Quote Content,
- unchanged canonical ten-stage IDs,
- explicit conditional dependencies and blockers,
- no cross-mode artifact reuse,
- preserved UGC compatibility.

Phase 01 does not certify Quote Content end-to-end production. That depends on Phase 02 strategy and Phase 03 production implementation.
