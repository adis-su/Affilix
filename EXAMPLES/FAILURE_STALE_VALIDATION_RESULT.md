# Affilix — Failure / Stale Validation Result

## Scope

Source-level validation of the stage lifecycle and dependency rules.

## Checks

| ID | Scenario | Expected |
|---|---|---|
| F001 | Approve STALE stage | Reject |
| F002 | Approve stage not in REVIEW/DRAFT | Reject |
| F003 | Storyboard revision | Visual, Video, Voice, QC, Final become STALE |
| F004 | Visual revision | Video, QC, Final become STALE |
| F005 | Video revision | QC, Final become STALE |
| F006 | Voice revision | QC, Final become STALE |
| F007 | Video continuity approval without approved Visual | Reject |
| F008 | QC before required branches are ready | Reject downstream progression |
| F009 | Final Package without QC PASS | Reject |
| F010 | Parallel branch approval | Sibling branch remains independently actionable |
| F011 | Stale asset in Final Package | Reject |
| F012 | Explicit skip | Stage becomes SKIPPED and is excluded from required-branch gating |

## Result

F001–F012: validated against the current lifecycle and downstream contracts.

The lifecycle explicitly supports independent branch states and stale propagation. Final Package and QC contracts reject stale or incomplete required assets.

## Live Test Limitation

A live HTTP invocation could not be executed with the available Supabase tool surface because no Edge Function invocation operation is exposed.

Therefore this document is a static/contract validation result, not proof of live HTTP execution.
