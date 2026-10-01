# Affilix — Storyboard Engine

## Provider-Aware Duration Planning

The storyboard owns creative duration, while the current video provider accepts generation clips of exactly 4s, 6s, 8s, or 10s.

Plan the narrative first, then map it to those technical clip sizes.

Rules:

- requested final duration must be preserved exactly
- generation segments may span one or multiple storyboard beats
- segment durations must be 4, 6, 8, or 10 seconds
- segment boundaries should follow natural creative beats
- never add filler solely to reach a provider duration
- never silently shorten or lengthen the campaign
- if exact composition is impossible, flag duration feasibility as BLOCKED

Examples:

```text
14s → 6s + 8s
18s → 8s + 10s
20s → 10s + 10s
```

A creative scene may contain multiple generation segments. The technical segment plan belongs to Video Prompt; the storyboard remains responsible for narrative timing.
