"""Integration tests for serialized Quote Content Stage 06–10 artifacts."""
import copy
import unittest

from scripts.validate_quote_content_artifacts import validate_bundle


def source(kind, artifact_id, version, commit="commit-sb-1"):
    return {
        "artifact_type": kind,
        "artifact_id": artifact_id,
        "artifact_version": version,
        "source_commit_sha": commit,
    }


def valid_bundle():
    storyboard = {
        "storyboard_id": "SB-01",
        "storyboard_version": "v1",
        "source_commit_sha": "commit-sb-1",
        "scenes": [
            {
                "scene_id": "SC01",
                "time_window": {"start_time": 0, "end_time": 10},
                "beats": [
                    {"beat_id": "B01", "reference_after": {"reference_id": "R02", "reference_version": "v1"},
                     "time_window": {"start_time": 2, "end_time": 5}}
                ],
            },
            {
                "scene_id": "SC02",
                "time_window": {"start_time": 10, "end_time": 20},
                "beats": [
                    {"beat_id": "B02", "reference_after": {"reference_id": "R03", "reference_version": "v1"},
                     "time_window": {"start_time": 12, "end_time": 15}}
                ],
            },
        ],
        "reference_plan": {"states": [
            {"reference_id": "R01", "reference_version": "v1"},
            {"reference_id": "R02", "reference_version": "v1"},
            {"reference_id": "R03", "reference_version": "v1"},
        ]},
        "reference_trajectory": {"transitions": [
            {"transition_id": "T01"}, {"transition_id": "T02"}
        ]},
    }
    sb_source = source("STORYBOARD", "SB-01", "v1")
    visual = {
        "artifact_id": "VP-01", "artifact_version": "v1", "status": "COMPLETED",
        "source_artifacts": [sb_source],
        "prompts": [
            {"reference_id": "R01", "reference_version": "v1"},
            {"reference_id": "R02", "reference_version": "v1"},
            {"reference_id": "R03", "reference_version": "v1"},
        ],
    }
    voice = {
        "artifact_id": "VS-01", "artifact_version": "v1", "status": "COMPLETED",
        "source_artifacts": [sb_source],
        "lines": [
            {"scene_id": "SC01", "source_beat_id": "B01", "target_reference_id": "R02",
             "target_reference_version": "v1", "time_window": {"start_time": 2, "end_time": 4}},
            {"scene_id": "SC02", "source_beat_id": "B02", "target_reference_id": "R03",
             "target_reference_version": "v1", "time_window": {"start_time": 12, "end_time": 14}},
        ],
    }
    video = {
        "artifact_id": "VID-01", "artifact_version": "v1", "status": "COMPLETED",
        "source_artifacts": [sb_source, source("VISUAL_PROMPT", "VP-01", "v1"),
                             source("VOICE_SCRIPT", "VS-01", "v1")],
        "scenes": [{"scene_id": "SC01"}, {"scene_id": "SC02"}],
        "generation_segments": [
            {"segment_id": "SEG01", "final_start_time": 0, "final_end_time": 10,
             "generation_duration": 10, "source_scene_ids": ["SC01"],
             "start_reference_id": "R01", "start_reference_version": "v1",
             "target_reference_id": "R02", "target_reference_version": "v1", "transition_ids": ["T01"]},
            {"segment_id": "SEG02", "final_start_time": 10, "final_end_time": 20,
             "generation_duration": 10, "source_scene_ids": ["SC02"],
             "start_reference_id": "R02", "start_reference_version": "v1",
             "target_reference_id": "R03", "target_reference_version": "v1", "transition_ids": ["T02"]},
        ],
    }
    output = {
        "artifact_id": "OUT-01", "artifact_version": "v1", "status": "COMPLETED",
        "source_artifacts": [
            source("STORYBOARD", "SB-01", "v1"),
            source("VISUAL_PROMPT", "VP-01", "v1"),
            source("VOICE_SCRIPT", "VS-01", "v1"),
            source("VIDEO_PROMPT", "VID-01", "v1"),
        ],
        "reference_coverage": "PASS", "duration_integrity": "PASS",
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

    def test_missing_bridge_reference_prompt_is_blocked(self):
        bundle = valid_bundle()
        bundle["visual_prompt"]["prompts"].pop(1)
        self.assertIn("visual_prompt_reference_coverage_mismatch", validate_bundle(bundle))

    def test_wrong_segment_composition_is_blocked(self):
        bundle = valid_bundle()
        bundle["video_prompt"]["generation_segments"][1]["final_start_time"] = 9
        self.assertIn("generation_segment_composition_not_exact_10_plus_10", validate_bundle(bundle))

    def test_unresolved_dialogue_anchor_is_blocked(self):
        bundle = valid_bundle()
        bundle["voice_script"]["lines"][0]["source_beat_id"] = "MISSING"
        self.assertIn("voice_line_anchor_unresolved", validate_bundle(bundle))

    def test_stale_artifact_is_blocked(self):
        bundle = valid_bundle()
        bundle["video_prompt"]["status"] = "STALE"
        self.assertIn("video_prompt_is_stale", validate_bundle(bundle))

    def test_production_output_must_match_current_assets(self):
        bundle = valid_bundle()
        bundle["production_output"]["source_artifacts"][1]["artifact_version"] = "v0"
        self.assertIn("production_output_visual_prompt_lineage_mismatch", validate_bundle(bundle))


if __name__ == "__main__":
    unittest.main()
