"""Regression tests using the canonical Stage 06–10 artifact field layout."""
import unittest

from scripts.validate_quote_content_artifacts import validate_bundle


def sb_source():
    return {"artifact_type": "STORYBOARD", "artifact_id": "SB-01",
            "artifact_version": "v1", "source_commit_sha": "commit-sb-1"}


def valid_bundle():
    storyboard = {
        "stage": "06_STORYBOARD", "content_mode": "QUOTE_CONTENT", "status": "COMPLETED",
        "metadata": {"storyboard_id": "SB-01", "storyboard_version": "v1",
                     "source_commit_sha": "commit-sb-1"},
        "scenes": [
            {"scene_id": "SC01", "time_window": {"start_time": 0, "end_time": 10},
             "action_graph": {"beats": [
                 {"beat_id": "B01", "time_window": {"start_time": 2, "end_time": 5},
                  "reference_after": {"reference_id": "R02", "reference_version": "v1"},
                  "dialogue_anchor": {"anchor_id": "A01", "semantic_intent": "explain",
                                      "action_window": {"start_time": 2, "end_time": 5},
                                      "target_reference": {"reference_id": "R02", "reference_version": "v1"}}}]},
             "reference_plan": {"states": [
                 {"reference_id": "R01", "reference_version": "v1", "source_scene_id": "SC01",
                  "source_beat_id": "B01", "sequence_index": 0, "reference_role": "START",
                  "state_summary": "Starting state", "continuity_invariants": ["identity"]},
                 {"reference_id": "R02", "reference_version": "v1", "source_scene_id": "SC01",
                  "source_beat_id": "B01", "sequence_index": 1, "reference_role": "END",
                  "state_summary": "Result state", "continuity_invariants": ["identity"]}]},
             "reference_trajectory": {"ordered_reference_ids": ["R01", "R02"],
                                      "transitions": [{"transition_id": "T01", "from_reference_id": "R01",
                                                       "to_reference_id": "R02", "causal_action": "turns",
                                                       "resulting_state": "faces camera"}]}},
            {"scene_id": "SC02", "time_window": {"start_time": 10, "end_time": 20},
             "action_graph": {"beats": [
                 {"beat_id": "B02", "time_window": {"start_time": 12, "end_time": 15},
                  "reference_after": {"reference_id": "R03", "reference_version": "v1"},
                  "dialogue_anchor": {"anchor_id": "A02", "semantic_intent": "conclude",
                                      "action_window": {"start_time": 12, "end_time": 15},
                                      "target_reference": {"reference_id": "R03", "reference_version": "v1"}}}]},
             "reference_plan": {"states": [
                 {"reference_id": "R03", "reference_version": "v1", "source_scene_id": "SC02",
                  "source_beat_id": "B02", "sequence_index": 0, "reference_role": "START",
                  "state_summary": "Final state", "continuity_invariants": ["identity"]}]},
             "reference_trajectory": {"ordered_reference_ids": ["R03"], "transitions": []}},
        ],
    }
    visual = {
        "stage": "07_VISUAL_PROMPT", "status": "COMPLETED",
        "artifact_id": "VP-01", "artifact_version": "v1", "source_artifacts": [sb_source()],
        "prompts": [
            {"reference_id": "R01", "reference_version": "v1", "source_scene_id": "SC01",
             "source_beat_id": "B01", "source_storyboard_id": "SB-01", "source_storyboard_version": "v1"},
            {"reference_id": "R02", "reference_version": "v1", "source_scene_id": "SC01",
             "source_beat_id": "B01", "source_storyboard_id": "SB-01", "source_storyboard_version": "v1"},
            {"reference_id": "R03", "reference_version": "v1", "source_scene_id": "SC02",
             "source_beat_id": "B02", "source_storyboard_id": "SB-01", "source_storyboard_version": "v1"},
        ],
    }
    voice = {
        "stage": "08_VOICE_SCRIPT", "status": "COMPLETED",
        "artifact_id": "VS-01", "artifact_version": "v1", "source_artifacts": [sb_source()],
        "dialogue": {"lines": [
            {"line_id": "L01", "scene_id": "SC01", "source_beat_id": "B01",
             "dialogue_anchor": {"beat_id": "B01", "anchor_id": "A01"},
             "intended_meaning": "explain", "start_time": 2, "end_time": 4},
            {"line_id": "L02", "scene_id": "SC02", "source_beat_id": "B02",
             "dialogue_anchor": {"beat_id": "B02", "anchor_id": "A02"},
             "intended_meaning": "conclude", "start_time": 12, "end_time": 14},
        ]},
    }
    video = {
        "stage": "09_VIDEO_PROMPT", "status": "COMPLETED",
        "artifact_id": "VID-01", "artifact_version": "v1",
        "source_artifacts": [sb_source(),
                             {"artifact_type": "VISUAL_PROMPT", "artifact_id": "VP-01", "artifact_version": "v1"},
                             {"artifact_type": "VOICE_SCRIPT", "artifact_id": "VS-01", "artifact_version": "v1"}],
        "scenes": [{"scene_id": "SC01"}, {"scene_id": "SC02"}],
        "generation_segments": [
            {"segment_id": "SEG01", "final_start_time": 0, "final_end_time": 10,
             "generation_duration": 10, "source_scene_ids": ["SC01"],
             "start_reference_id": "R01", "start_reference_version": "v1",
             "target_reference_id": "R02", "target_reference_version": "v1", "transition_ids": ["T01"]},
            {"segment_id": "SEG02", "final_start_time": 10, "final_end_time": 20,
             "generation_duration": 10, "source_scene_ids": ["SC02"],
             "start_reference_id": "R02", "start_reference_version": "v1",
             "target_reference_id": "R03", "target_reference_version": "v1", "transition_ids": []},
        ],
    }
    output = {
        "stage": "10_PRODUCTION_OUTPUT", "status": "COMPLETED",
        "source_artifacts": {
            "stage_06": {"artifact_id": "SB-01", "artifact_version": "v1"},
            "stage_07": {"artifact_id": "VP-01", "artifact_version": "v1"},
            "stage_08": {"artifact_id": "VS-01", "artifact_version": "v1"},
            "stage_09": {"artifact_id": "VID-01", "artifact_version": "v1"},
        },
        "validation": {"reference_coverage": "PASS", "duration_integrity": "PASS"},
    }
    return {"storyboard": storyboard, "visual_prompt": visual, "voice_script": voice,
            "video_prompt": video, "production_output": output}


class QuoteContentArtifactIntegrationTests(unittest.TestCase):
    def test_valid_bundle_passes(self):
        self.assertEqual(validate_bundle(valid_bundle()), [])

    def test_mismatched_storyboard_version_is_blocked(self):
        bundle = valid_bundle()
        bundle["visual_prompt"]["source_artifacts"][0]["artifact_version"] = "v0"
        self.assertIn("visual_prompt_storyboard_lineage_mismatch", validate_bundle(bundle))

    def test_missing_reference_prompt_is_blocked(self):
        bundle = valid_bundle()
        bundle["visual_prompt"]["prompts"].pop(1)
        self.assertIn("visual_prompt_reference_coverage_mismatch", validate_bundle(bundle))

    def test_wrong_segment_composition_is_blocked(self):
        bundle = valid_bundle()
        bundle["video_prompt"]["generation_segments"][1]["final_start_time"] = 9
        self.assertIn("generation_segment_composition_not_exact_10_plus_10", validate_bundle(bundle))

    def test_unresolved_dialogue_anchor_is_blocked(self):
        bundle = valid_bundle()
        bundle["voice_script"]["dialogue"]["lines"][0]["source_beat_id"] = "MISSING"
        self.assertIn("voice_line_anchor_unresolved", validate_bundle(bundle))

    def test_stale_artifact_is_blocked(self):
        bundle = valid_bundle()
        bundle["video_prompt"]["status"] = "STALE"
        self.assertIn("video_prompt_is_stale", validate_bundle(bundle))

    def test_production_output_must_match_current_assets(self):
        bundle = valid_bundle()
        bundle["production_output"]["source_artifacts"]["stage_07"]["artifact_version"] = "v0"
        self.assertIn("production_output_stage_07_lineage_mismatch", validate_bundle(bundle))


if __name__ == "__main__":
    unittest.main()
