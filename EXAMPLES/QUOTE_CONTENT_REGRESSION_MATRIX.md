# Affilix Quote Content Regression & Hardening Matrix

## Purpose

Phase 04 verifies that Quote Content mode contracts, the canonical ten-stage workflow, runtime loader, and production output agree. These cases are test specifications, not evidence of execution.

**Execution status: NOT RUN as an end-to-end runtime suite.** Contract presence and static cross-file consistency may be reviewed separately. Do not mark a case PASS until the specified runtime behavior has actually been exercised and its output inspected.

## Source Contracts

- `ENGINE/CONTENT_MODE_ROUTING_CONTRACT.md`
- `ENGINE/WORKFLOW.md`
- `ENGINE/REPOSITORY_RUNTIME/RUNTIME_CONTRACT.md`
- `ENGINE/REPOSITORY_RUNTIME/README.md`
- `ENGINE/05_STORYBOARD_ENGINE/QUOTE_CONTENT_STORYBOARD_CONTRACT.md`
- `ENGINE/06_VISUAL_PROMPT_ENGINE/QUOTE_CONTENT_VISUAL_PROMPT_CONTRACT.md`
- `ENGINE/08_VOICE_SCRIPT_ENGINE/QUOTE_CONTENT_VOICE_SCRIPT_CONTRACT.md`
- `ENGINE/07_VIDEO_PROMPT_ENGINE/QUOTE_CONTENT_VIDEO_PROMPT_CONTRACT.md`
- `ENGINE/QUOTE_CONTENT_PRODUCTION_OUTPUT_CONTRACT.md`

## Test Matrix

| ID | Scenario | Expected result | Severity if failed | Status |
|---|---|---|---|---|
| QCR-001 | Editorial brief with no product | Stages 01–02 accept editorial inputs; no product or product claims are fabricated | Critical | NOT RUN |
| QCR-002 | Static `QUOTE_IMAGE` | Stage 06, 08, and 09 skip with `STATIC_IMAGE_FORMAT`; Stage 07 and applicable Stage 10 remain required | Critical | NOT RUN |
| QCR-003 | Video format stage dispatch | Stages 06 and 07 are required; Stage 09 is required; Stage 08 depends on dialogue/audio requirements | Critical | NOT RUN |
| QCR-004 | Video prompt count | Exactly one user-facing Video Prompt per Storyboard scene, in the same order | Critical | NOT RUN |
| QCR-005 | Multiple reference states | Stage 07 produces one frozen-state prompt per declared reference state, not one prompt per scene | Major | NOT RUN |
| QCR-006 | Immutable bridge | Adjacent scenes share the same bridge reference ID and version; changing it marks dependent transitions and prompts stale | Critical | NOT RUN |
| QCR-007 | Exact duration composition | Segment durations use only 4, 6, 8, or 10 seconds and sum exactly to requested duration | Critical | NOT RUN |
| QCR-008 | Infeasible duration | Set `duration_feasibility: BLOCKED`; do not round, truncate, extend, or pad | Critical | NOT RUN |
| QCR-009 | Conditional voice | No-spoken output skips Stage 08 only when permitted and records a mode-specific reason; spoken/external dialogue has canonical script anchors | Major | NOT RUN |
| QCR-010 | Dialogue ownership | Stage 09 synchronizes but does not rewrite Stage 08's canonical exact wording | Major | NOT RUN |
| QCR-011 | Editorial causality | Storyboard and Video Prompt preserve trigger → intention → action → resulting state without forced product-demo beats | Critical | NOT RUN |
| QCR-012 | Attribution and lived experience | No invented quote attribution, personal testimony, biography, or unsupported factual claim | Critical | NOT RUN |
| QCR-013 | Stale upstream artifact | Material edits to topic, strategy, hook, storyboard, reference state, duration, or audio mode invalidate affected dependents | Critical | NOT RUN |
| QCR-014 | Cross-mode isolation | Switching between `UGC_AFFILIATE` and `QUOTE_CONTENT` never reuses incompatible artifacts or silently falls back to the other mode's output template | Critical | NOT RUN |
| QCR-015 | Missing required dependency | Stage 10 blocks with `QUOTE_CONTENT_OUTPUT_DEPENDENCY_BLOCKED` when a required artifact is missing, stale, invalid, or contradictory | Critical | NOT RUN |
| QCR-016 | Unsupported format | Unknown format blocks with `QUOTE_CONTENT_FORMAT_UNSUPPORTED`; no closest-format substitution | Major | NOT RUN |
| QCR-017 | Canonical stage registry | IDs remain 01–10; engine folder prefixes never determine workflow order; no QC, approval, or final-package stage appears | Critical | NOT RUN |
| QCR-018 | UGC regression guard | Existing UGC product evidence, creator identity, product claims, action choreography, duration, and output behavior remain unchanged | Critical | NOT RUN |
| QCR-019 | Quote Content intake fields | Intake offers platform, objective, topic/audience context, optional format/pillar, and audio preference; duration is fixed at 20 seconds and no content quantity or CTA input field is requested | Critical | NOT RUN |
| QCR-020 | Fixed Quote Content duration | Video intake does not ask for duration; all video formats use exactly 20 seconds composed as `10 + 10`; static `QUOTE_IMAGE` uses `NOT_APPLICABLE` | Critical | NOT RUN |
| QCR-021 | 20-second spoken word budget | Spoken script targets 38–44 words total, with timing validated against delivery pace, pauses, emotional beats, and both 10-second segments | Critical | NOT RUN |
| QCR-022 | Text-only duration behavior | Text-only output does not invent spoken dialogue or enforce a spoken-word budget; on-screen text legibility and reading time are validated | Major | NOT RUN |

| QCR-023 | Exact wardrobe/environment literals in every Stage 07 prompt | Under `QUOTE_CONTENT`, the entire `WARDROBE` section is exactly `Sesuai referensi gambar yang diupload user.` and the entire `ENVIRONMENT` section is exactly the same sentence; no hijab/outfit details or room/background prose may be appended; violating output is repaired or blocked, never marked complete | Critical | NOT RUN |
| QCR-024 | Storyboard beat timing contract | Every video beat has numeric `time_window.start_time` and `time_window.end_time` within the final 20-second timeline and its owning scene; invalid, missing, or out-of-range windows prevent Stage 06 completion | Critical | NOT RUN |
| QCR-025 | Dialogue anchor alignment | Every Stage 08 line resolves to a current Stage 06 scene, source beat, dialogue anchor, semantic intent, and exact target reference ID/version; line timing stays inside both the anchor action window and scene window and avoids protected pauses/critical visual actions | Critical | NOT RUN |
| QCR-026 | Parallel branch and stale-source integrity | Stage 07 and Stage 08 consume the same current Stage 06 artifact/source commit without depending on each other; a storyboard revision invalidates affected Visual Prompt and Voice Script outputs, and Stage 09 cannot consume mixed or stale source versions | Critical | NOT RUN |

## Execution Protocol

For each case:

1. Pin the repository commit used for the run.
2. Start from an isolated campaign state with the listed input.
3. Execute the applicable stages sequentially, waiting for `/next` after each completed stage.
4. Save the produced stage artifacts and validation results.
5. Compare outputs against the expected result and record the exact failure or evidence.
6. Mark `PASS` only after observed behavior satisfies every expected result. Use `FAIL` for a reproducible mismatch and `BLOCKED` if the runtime or required provider is unavailable.
7. After any contract change, rerun every test whose source contract or dependency graph was affected.

## Release Acceptance

Quote Content regression is accepted only when all Critical cases pass, all applicable Major cases pass or have a documented non-blocking disposition, and the UGC regression guard remains green. A static documentation review is not an end-to-end runtime pass.

There is no separate QC or approval stage in the Affilix production workflow. This matrix is repository-level engineering verification and must not be inserted as a user-facing campaign stage.
