"""Executable regression tests for Affilix runtime state transitions."""
import unittest

from scripts.affilix_runtime_harness import (
    DOWNSTREAM,
    ContentMode,
    change_content_mode,
    new_isolated_run,
    resolve_stage_plan,
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


    def test_quote_image_routes_static_stages_to_explicit_skips(self):
        plan = resolve_stage_plan(
            "QUOTE_CONTENT",
            selected_format="QUOTE_IMAGE",
            creator_required=False,
            strategy_allows_hook_skip=True,
        )
        for stage in ("06_STORYBOARD", "08_VOICE_SCRIPT", "09_VIDEO_PROMPT"):
            self.assertEqual(plan[stage]["status"], "SKIPPED")
            self.assertEqual(plan[stage]["reason"], "STATIC_IMAGE_FORMAT")
        self.assertEqual(plan["05_HOOK"]["status"], "SKIPPED")
        self.assertEqual(plan["07_VISUAL_PROMPT"]["status"], "REQUIRED")
        self.assertEqual(plan["10_PRODUCTION_OUTPUT"]["status"], "REQUIRED")
        self.assertEqual(plan["03_CREATOR"]["reason"], "NO_ON_SCREEN_CREATOR_REQUIRED")

    def test_quote_image_does_not_skip_hook_without_strategy_permission(self):
        plan = resolve_stage_plan(
            "QUOTE_CONTENT",
            selected_format="QUOTE_IMAGE",
            strategy_allows_hook_skip=False,
        )
        self.assertEqual(plan["05_HOOK"]["status"], "REQUIRED")

    def test_quote_video_no_spoken_voice_skips_voice_with_mode_reason(self):
        plan = resolve_stage_plan(
            "QUOTE_CONTENT",
            selected_format="RELATABLE_STORY_REELS",
            audio_mode="NO_SPOKEN_VOICE",
        )
        self.assertEqual(plan["08_VOICE_SCRIPT"]["status"], "SKIPPED")
        self.assertEqual(plan["08_VOICE_SCRIPT"]["reason"], "NO_SPOKEN_VOICE_REQUIRED")
        self.assertEqual(plan["06_STORYBOARD"]["status"], "REQUIRED")
        self.assertEqual(plan["09_VIDEO_PROMPT"]["status"], "REQUIRED")

    def test_external_dialogue_keeps_voice_script_required_without_on_camera_speech(self):
        plan = resolve_stage_plan(
            "QUOTE_CONTENT",
            selected_format="RELATABLE_STORY_REELS",
            audio_mode="NO_SPOKEN_VOICE",
            external_dialogue_required=True,
        )
        self.assertEqual(plan["08_VOICE_SCRIPT"]["status"], "REQUIRED")

    def test_ugc_cannot_silently_skip_required_creator(self):
        with self.assertRaisesRegex(RuntimeBlocked, "UGC_CREATOR_REQUIREMENT_CANNOT_BE_SKIPPED"):
            resolve_stage_plan(
                "UGC_AFFILIATE",
                selected_format="VIDEO",
                creator_required=False,
            )

    def test_mode_change_requires_new_isolated_run(self):
        state = new_isolated_run(
            run_id="quote-run",
            pinned_commit_sha="commit-a",
            content_mode="QUOTE_CONTENT",
            selected_format="QUOTE_IMAGE",
        )
        self.assertEqual(state.content_mode, ContentMode.QUOTE_CONTENT)
        self.assertEqual(len(state.artifact_source_commits), 0)
        with self.assertRaisesRegex(RuntimeBlocked, "CONTENT_MODE_CHANGE_REQUIRES_NEW_ISOLATED_RUN"):
            change_content_mode(state, "UGC_AFFILIATE")
        other = new_isolated_run(
            run_id="ugc-run",
            pinned_commit_sha="commit-a",
            content_mode="UGC_AFFILIATE",
        )
        self.assertNotEqual(state.run_id, other.run_id)
        self.assertEqual(other.content_mode, ContentMode.UGC_AFFILIATE)

    def test_unsupported_content_mode_or_format_blocks_closed(self):
        with self.assertRaisesRegex(RuntimeBlocked, "UNSUPPORTED_CONTENT_MODE"):
            resolve_stage_plan("UNKNOWN_MODE")
        with self.assertRaisesRegex(RuntimeBlocked, "UNSUPPORTED_QUOTE_CONTENT_FORMAT"):
            resolve_stage_plan("QUOTE_CONTENT", selected_format="UNREGISTERED_FORMAT")

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
