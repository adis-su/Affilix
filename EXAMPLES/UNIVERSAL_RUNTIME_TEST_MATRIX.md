# Affilix Universal Runtime Test Matrix

## Purpose

Validate that the shared runtime context contract behaves consistently across active niches without creating niche-specific creative engines.

## Core Invariants

- One canonical context object is passed downstream.
- Product identity outranks creative context.
- Creator identity remains stable.
- UNKNOWN remains UNKNOWN without authoritative evidence.
- Context labels never become unsupported product claims.
- Reclassification replaces stale context and invalidates dependent outputs.
- Context from one run cannot leak into another run.
- Conflicts are surfaced instead of silently resolved.

## Test Matrix

| Test | Niche | Context | Primary Risk | Status |
|---|---|---|---|---|
| U001 | Fashion | Streetwear + Top + Everyday + Street | Context/product separation | PASS |
| U002 | Beauty | Skincare + Skincare Product + Everyday Beauty + Natural Look | Unsupported beauty claims | PASS |
| U003 | Food & Beverage | Drinks + Drink + Everyday Consumption | Invented ingredients/preparation | PASS |
| U004 | Home & Living | Organization + Organizer + Everyday Home | Invented capacity/function | PASS |
| U005 | Cross-Niche | Fashion → Beauty | Stale context leakage | PASS |
| U006 | Reclassification | Beauty → Food & Beverage | Dependent output invalidation | PASS |
| U007 | UNKNOWN | Any active niche | Missing attribute inference | PASS |
| U008 | Conflict | Any active niche | Silent precedence failure | PASS |

## Acceptance

A runtime implementation passes only when all invariants hold and no critical or major issue is introduced.
