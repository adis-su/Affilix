# Universal Runtime U008 Fixture

Test: U008
Scenario: Precedence Conflict

Input contains:
- An explicit product fact.
- A campaign requirement.
- A style/context label that could imply a conflicting creative interpretation.

Required behavior:
- Latest explicit user instruction and campaign requirements outrank creative interpretation.
- Approved product facts cannot be overridden by style labels.
- Conflicts are surfaced when authoritative sources disagree at the same level.
- Downstream engines receive the resolved context plus conflict flags.
