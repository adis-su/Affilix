"""Executable regression tests for Affilix runtime state transitions."""
import unittest

from scripts.affilix_runtime_harness import (
    DOWNSTREAM,
    STAGES,
    RunState,
    RuntimeBlocked,
    StageStatus,
    complete_current_stage,
    mark_completed,
    next_stage,
    revise_stage,
    synchronize_repository,
)


def active_run():
    return RunState(run_id="run-test-01", pinned_commit_sha="commit-a")


class RuntimeProgressionTests(unittest.TestCase):
    def test_completed_stage_waits_for_next_and_advances_exactly_one(self):
        state = active_run()
        complete_current_stage(state, valid=True)
        self.assertEqual(state.progression, "WAITING_FOR_NEXT")
        self.assertEqual(state.current_stage, STAGES[0])
        with self.assertRaisesRegex(RuntimeBlocked, "STAGE_ALREADY_COMPLETED"):
            complete_current_stage(state, valid=True)
        result = next_stage(state, resolved_main_sha="commit-a")
        self.assertEqual(result, STAGES[1])
        self.assertEqual(state.progression, "ACTIVE")

    def test_invalid_stage_cannot_advance(self):
        state = active_run()
        with self.assertRaisesRegex(RuntimeBlocked, "STAGE_VALIDATION_FAILED"):
            complete_current_stage(state, valid=False)
        with self.assertRaisesRegex(RuntimeBlocked, "CURRENT_STAGE_NOT_VALIDATED"):
            next_stage(state, resolved_main_sha="commit-a")
        self.assertEqual(state.current_stage, STAGES[0])

    def test_next_checks_prerequisites(self):
        state = active_run()
        complete_current_stage(state, valid=True)
        state.stages[STAGES[0]].status = StageStatus.STALE
        with self.assertRaisesRegex(RuntimeBlocked, "CURRENT_STAGE_NOT_VALIDATED"):
            next_stage(state, resolved_main_sha="commit-a")
        self.assertEqual(state.current_stage, STAGES[0])

    def test_repository_sync_failure_does_not_change_pin_or_advance(self):
        state = active_run()
        complete_current_stage(state, valid=True)
        with self.assertRaisesRegex(RuntimeBlocked, "REPOSITORY_SYNC_FAILURE"):
            next_stage(state, resolved_main_sha="commit-b", repository_load_ok=False)
        self.assertEqual(state.pinned_commit_sha, "commit-a")
        self.assertEqual(state.current_stage, STAGES[0])
        self.assertEqual(state.progression, "WAITING_FOR_NEXT")

    def test_new_commit_invalidates_completed_artifacts_before_progression(self):
        state = active_run()
        complete_current_stage(state, valid=True)
        mark_completed(state, STAGES[1])
        state.current_stage = STAGES[1]
        state.progression = "WAITING_FOR_NEXT"
        with self.assertRaisesRegex(RuntimeBlocked, "CURRENT_STAGE_NOT_VALIDATED"):
            next_stage(state, resolved_main_sha="commit-b")
        self.assertEqual(state.pinned_commit_sha, "commit-b")
        self.assertEqual(state.stages[STAGES[0]].status, StageStatus.STALE)
        self.assertEqual(state.stages[STAGES[1]].status, StageStatus.STALE)
        self.assertEqual(state.current_stage, STAGES[1])

    def test_artifact_from_other_commit_is_rejected(self):
        state = active_run()
        with self.assertRaisesRegex(RuntimeBlocked, "ARTIFACT_SOURCE_COMMIT_MISMATCH"):
            complete_current_stage(state, valid=True, artifact_commit_sha="commit-old")
        self.assertEqual(state.stages[STAGES[0]].status, StageStatus.DRAFT)

    def test_revision_invalidates_only_declared_downstream_and_waits(self):
        state = active_run()
        state.current_stage = "06_STORYBOARD"
        state.progression = "WAITING_FOR_NEXT"
        mark_completed(state, "06_STORYBOARD")
        for stage in ("07_VISUAL_PROMPT", "08_VOICE_SCRIPT", "09_VIDEO_PROMPT", "10_PRODUCTION_OUTPUT"):
            mark_completed(state, stage)
        affected = revise_stage(state, "06_STORYBOARD", valid=True)
        self.assertEqual(affected, DOWNSTREAM["06_STORYBOARD"])
        for stage in affected:
            self.assertEqual(state.stages[stage].status, StageStatus.STALE)
        self.assertEqual(state.stages["06_STORYBOARD"].status, StageStatus.COMPLETED)
        self.assertEqual(state.progression, "WAITING_FOR_NEXT")
        self.assertEqual(state.current_stage, "06_STORYBOARD")

    def test_revision_never_advances_even_when_valid(self):
        state = active_run()
        state.current_stage = "05_HOOK"
        state.progression = "WAITING_FOR_NEXT"
        mark_completed(state, "05_HOOK")
        revise_stage(state, "05_HOOK", valid=True)
        self.assertEqual(state.current_stage, "05_HOOK")
        self.assertEqual(state.progression, "WAITING_FOR_NEXT")

    def test_revision_failure_keeps_current_stage_and_blocks(self):
        state = active_run()
        state.current_stage = "06_STORYBOARD"
        state.progression = "WAITING_FOR_NEXT"
        mark_completed(state, "06_STORYBOARD")
        mark_completed(state, "07_VISUAL_PROMPT")
        with self.assertRaisesRegex(RuntimeBlocked, "REVISION_VALIDATION_FAILED"):
            revise_stage(state, "06_STORYBOARD", valid=False)
        self.assertEqual(state.current_stage, "06_STORYBOARD")
        self.assertEqual(state.stages["07_VISUAL_PROMPT"].status, StageStatus.STALE)
        self.assertEqual(state.progression, "ACTIVE")

    def test_final_stage_completes_run_without_adding_stage(self):
        state = active_run()
        state.current_stage = STAGES[-1]
        state.progression = "WAITING_FOR_NEXT"
        mark_completed(state, STAGES[-2])
        mark_completed(state, STAGES[-1])
        result = next_stage(state, resolved_main_sha="commit-a")
        self.assertEqual(result, STAGES[-1])
        self.assertEqual(state.progression, "RUN_COMPLETED")
        self.assertEqual(len(state.stages), 10)


if __name__ == "__main__":
    unittest.main()
