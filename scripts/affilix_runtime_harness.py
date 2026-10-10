#!/usr/bin/env python3
"""Deterministic state-transition harness for Affilix orchestration contracts.

This is a test harness, not the ChatGPT Skill runtime and not a persistence service.
It models one isolated run in memory so progression, synchronization, and stale
propagation rules can be exercised as executable regression tests.
"""
from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum
from typing import Iterable


STAGES = (
    "01_BRIEF_PRODUCT",
    "02_NICHE_CONTEXT",
    "03_CREATOR",
    "04_CONTENT_STRATEGY",
    "05_HOOK",
    "06_STORYBOARD",
    "07_VISUAL_PROMPT",
    "08_VOICE_SCRIPT",
    "09_VIDEO_PROMPT",
    "10_PRODUCTION_OUTPUT",
)

DOWNSTREAM: dict[str, tuple[str, ...]] = {
    "01_BRIEF_PRODUCT": STAGES[1:],
    "02_NICHE_CONTEXT": STAGES[2:],
    "03_CREATOR": STAGES[3:],
    "04_CONTENT_STRATEGY": STAGES[4:],
    "05_HOOK": STAGES[5:],
    "06_STORYBOARD": STAGES[6:],
    "07_VISUAL_PROMPT": ("09_VIDEO_PROMPT", "10_PRODUCTION_OUTPUT"),
    "08_VOICE_SCRIPT": ("09_VIDEO_PROMPT", "10_PRODUCTION_OUTPUT"),
    "09_VIDEO_PROMPT": ("10_PRODUCTION_OUTPUT",),
    "10_PRODUCTION_OUTPUT": (),
}


class StageStatus(str, Enum):
    NOT_STARTED = "NOT_STARTED"
    DRAFT = "DRAFT"
    REVISION = "REVISION"
    STALE = "STALE"
    SKIPPED = "SKIPPED"
    COMPLETED = "COMPLETED"


class RuntimeBlocked(RuntimeError):
    """A fail-closed runtime transition."""


@dataclass
class StageRecord:
    status: StageStatus = StageStatus.NOT_STARTED
    artifact_version: int = 0
    validated: bool = False


@dataclass
class RunState:
    run_id: str
    pinned_commit_sha: str
    current_stage: str = STAGES[0]
    progression: str = "ACTIVE"
    stages: dict[str, StageRecord] = field(
        default_factory=lambda: {stage: StageRecord() for stage in STAGES}
    )
    artifact_source_commits: dict[str, str] = field(default_factory=dict)
    events: list[str] = field(default_factory=list)


def _validate_sha(sha: str) -> None:
    if not isinstance(sha, str) or not sha.strip():
        raise RuntimeBlocked("REPOSITORY_SYNC_FAILURE: resolved commit SHA is empty")


def synchronize_repository(state: RunState, resolved_main_sha: str, *, load_ok: bool = True) -> None:
    """Atomically pin a new snapshot, or leave state untouched on failure."""
    _validate_sha(resolved_main_sha)
    if not load_ok:
        raise RuntimeBlocked("REPOSITORY_SYNC_FAILURE: canonical snapshot could not be loaded")
    # All operations that can fail occur before mutating the active pin.
    previous = state.pinned_commit_sha
    if resolved_main_sha == previous:
        state.events.append(f"SYNC_UNCHANGED:{previous}")
        return
    state.pinned_commit_sha = resolved_main_sha
    for stage, record in state.stages.items():
        if record.status == StageStatus.COMPLETED:
            record.status = StageStatus.STALE
            record.validated = False
            state.artifact_source_commits.pop(stage, None)
    state.events.append(f"SYNC_COMMITTED:{previous}->{resolved_main_sha}")


def complete_current_stage(state: RunState, *, valid: bool, artifact_commit_sha: str | None = None) -> None:
    stage = state.current_stage
    record = state.stages[stage]
    if state.progression == "WAITING_FOR_NEXT":
        raise RuntimeBlocked("STAGE_ALREADY_COMPLETED: /next is required before another stage can execute")
    if not valid:
        record.status = StageStatus.DRAFT
        record.validated = False
        raise RuntimeBlocked(f"STAGE_VALIDATION_FAILED:{stage}")
    commit = artifact_commit_sha or state.pinned_commit_sha
    if commit != state.pinned_commit_sha:
        record.status = StageStatus.DRAFT
        record.validated = False
        raise RuntimeBlocked("ARTIFACT_SOURCE_COMMIT_MISMATCH")
    record.status = StageStatus.COMPLETED
    record.artifact_version += 1
    record.validated = True
    state.artifact_source_commits[stage] = commit
    state.progression = "WAITING_FOR_NEXT"
    state.events.append(f"STAGE_COMPLETED:{stage}:v{record.artifact_version}")


def next_stage(
    state: RunState,
    *,
    resolved_main_sha: str,
    repository_load_ok: bool = True,
    prerequisite_stages: Iterable[str] | None = None,
) -> str:
    """Synchronize first, then advance exactly one stage if the current stage is valid."""
    synchronize_repository(state, resolved_main_sha, load_ok=repository_load_ok)
    current = state.stages[state.current_stage]
    if state.progression != "WAITING_FOR_NEXT" or current.status != StageStatus.COMPLETED or not current.validated:
        raise RuntimeBlocked("CURRENT_STAGE_NOT_VALIDATED_OR_NOT_WAITING_FOR_NEXT")
    required = tuple(prerequisite_stages) if prerequisite_stages is not None else (
        () if state.current_stage == STAGES[0] else (STAGES[STAGES.index(state.current_stage) - 1],)
    )
    for dependency in required:
        if dependency not in state.stages:
            raise RuntimeBlocked(f"UNKNOWN_PREREQUISITE:{dependency}")
        dep = state.stages[dependency]
        if dep.status not in (StageStatus.COMPLETED, StageStatus.SKIPPED) or not dep.validated:
            raise RuntimeBlocked(f"PREREQUISITE_NOT_SATISFIED:{dependency}")
    index = STAGES.index(state.current_stage)
    if index == len(STAGES) - 1:
        state.progression = "RUN_COMPLETED"
        state.events.append("RUN_COMPLETED")
        return state.current_stage
    state.current_stage = STAGES[index + 1]
    state.progression = "ACTIVE"
    state.events.append(f"ADVANCED_TO:{state.current_stage}")
    return state.current_stage


def revise_stage(state: RunState, stage: str, *, valid: bool) -> tuple[str, ...]:
    """Revalidate in-place, invalidate affected dependents, and never auto-advance."""
    if stage not in state.stages:
        raise RuntimeBlocked(f"UNKNOWN_STAGE:{stage}")
    if stage != state.current_stage:
        raise RuntimeBlocked("REVISION_MUST_TARGET_CURRENT_STAGE")
    record = state.stages[stage]
    record.status = StageStatus.REVISION
    record.validated = False
    affected = DOWNSTREAM[stage]
    for dependent in affected:
        downstream = state.stages[dependent]
        if downstream.status in (StageStatus.COMPLETED, StageStatus.SKIPPED, StageStatus.DRAFT):
            downstream.status = StageStatus.STALE
            downstream.validated = False
            state.artifact_source_commits.pop(dependent, None)
    if not valid:
        state.progression = "ACTIVE"
        state.events.append(f"REVISION_BLOCKED:{stage}")
        raise RuntimeBlocked(f"REVISION_VALIDATION_FAILED:{stage}")
    record.status = StageStatus.COMPLETED
    record.artifact_version += 1
    record.validated = True
    state.artifact_source_commits[stage] = state.pinned_commit_sha
    state.progression = "WAITING_FOR_NEXT"
    state.events.append(f"REVISION_COMPLETED_WAITING:{stage}:v{record.artifact_version}")
    return affected


def mark_completed(state: RunState, stage: str, *, commit_sha: str | None = None) -> None:
    """Fixture helper to seed upstream state for focused tests."""
    if stage not in state.stages:
        raise RuntimeBlocked(f"UNKNOWN_STAGE:{stage}")
    record = state.stages[stage]
    record.status = StageStatus.COMPLETED
    record.validated = True
    record.artifact_version = max(1, record.artifact_version)
    state.artifact_source_commits[stage] = commit_sha or state.pinned_commit_sha
