#!/usr/bin/env python3
"""Executable checks for Affilix runtime orchestration contracts.

This validates that the repository documents required runtime invariants.
It does NOT execute the conversational Skill or prove runtime behavior.
"""
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
FILES = {
    "skill": "SKILL.md",
    "workflow": "ENGINE/WORKFLOW.md",
    "runtime": "ENGINE/REPOSITORY_RUNTIME/RUNTIME_CONTRACT.md",
    "adapter": "ENGINE/REPOSITORY_RUNTIME/GITHUB_RUNTIME_ADAPTER.md",
    "runtime_readme": "ENGINE/REPOSITORY_RUNTIME/README.md",
    "state": "ENGINE/REPOSITORY_RUNTIME/CAMPAIGN_STATE_PERSISTENCE.md",
    "authority": "ENGINE/05_STORYBOARD_ENGINE/DOWNSTREAM_AUTHORITY_CONTRACT.md",
    "audit": "RUNTIME_EXECUTION_BOUNDARY_AUDIT.md",
}
errors = []
checks = 0

def check(ok, message):
    global checks
    checks += 1
    print(f"{'PASS' if ok else 'FAIL'}: {message}")
    if not ok:
        errors.append(message)

docs = {}
for key, rel in FILES.items():
    path = ROOT / rel
    check(path.is_file(), f"runtime source exists: {rel}")
    docs[key] = path.read_text(encoding="utf-8") if path.is_file() else ""

runtime = docs["runtime"]
readme = docs["runtime_readme"]
adapter = docs["adapter"]
skill = docs["skill"]
workflow = docs["workflow"]
authority = docs["authority"]
state = docs["state"]

# Repository pinning and atomic synchronization.
check("resolve the current `main` HEAD SHA" in runtime and
      "compare it with the active run's pinned" in runtime,
      "runtime contract requires current-main versus active-pin comparison")
check("synchronize the active run's repository pin" in runtime and
      "reload the canonical runtime contracts" in runtime,
      "runtime contract requires pin synchronization and contract reload before stage execution")
check("REPOSITORY_SYNC_FAILURE" in runtime and "REPOSITORY_SYNC_FAILURE" in adapter,
      "failed atomic synchronization blocks progression with the canonical error")
check("mix files from different repository commits" in readme and
      "mix files from different repository commits" in adapter,
      "repository loaders forbid mixed-commit stage execution")
check("source_commit_sha" in state and "source repository commit SHA" in runtime,
      "run and artifact traceability include the pinned source commit")

# Explicit progression hold and command semantics.
check("`/next` means **synchronize the active run with the latest repository contract, then progress" in workflow,
      "/next is progression after repository synchronization, not approval")
check("WAITING_FOR_NEXT" in runtime and "do not draft, preview, or partially execute Storyboard" in workflow,
      "completed stages remain held until an explicit /next")
check("Revisions must revalidate the current stage" in runtime and
      "never advance automatically" in runtime,
      "revision flow revalidates in-place and never auto-advances")
check("current stage completes validation" in runtime and "all Stage 06 prerequisites are satisfied" in runtime,
      "progression requires validated current stage and dependency checks")

# Invalidation semantics and lineage integrity.
check("mark affected artifacts STALE" in runtime and
      "preserve unaffected branches" in runtime,
      "dependency invalidation marks only affected artifacts stale")
check("A material Stage 06 revision invalidates affected Stage 07 prompts" in authority and
      "A Stage 07 revision invalidates Stage 09 and Stage 10" in authority and
      "A Stage 08 revision invalidates Stage 09" in authority,
      "downstream invalidation matrix covers Storyboard, Visual, Voice, and Video dependencies")
check("Never silently mix artifacts from different Storyboard versions" in authority and
      "exact upstream artifact versions" in authority,
      "cross-stage handoffs require exact upstream artifact lineage")
check("If a canonical input changes, dependent state becomes STALE" in skill,
      "Skill declares stale propagation when canonical inputs change")

# Architecture boundary and honest capability statement.
check("MUST NOT require or introduce Supabase" in adapter and
      "Do not persist campaign state to an external service as a fallback" in adapter,
      "repository adapter remains access-only and does not add external state persistence")
check("not evidence that a separate program enforces the transition" in docs.get("audit", ""),
      "repository clearly distinguishes contract checks from conversational runtime execution")

print(f"\nRuntime contract checks: {checks - len(errors)}/{checks} passed.")
if errors:
    print(f"Failures: {len(errors)}")
    sys.exit(1)
print("Scope: documented runtime invariants only; this script does not simulate or execute /next.")
