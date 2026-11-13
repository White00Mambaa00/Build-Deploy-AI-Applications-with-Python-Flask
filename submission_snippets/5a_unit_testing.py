"""Unit tests for Watson emotion parsing, output, and invalid input."""

import unittest
from unittest.mock import Mock, patch

from EmotionDetection import emotion_detector

EXAMPLES = {
    "joy": "I am glad this happened",
    "anger": "I am really mad about this",
    "disgust": "I feel disgusted just hearing about this",
    "sadness": "I am so sad about this",
    "fear": "I am really afraid that this will happen",
}
EMOTIONS = ("anger", "disgust", "fear", "joy", "sadness")


class TestEmotionDetector(unittest.TestCase):
    """Verify API parsing without requiring live network access."""

    @patch("EmotionDetection.emotion_detection.requests.post")
    def test_five_emotions(self, mock_post):
        """Each of the five example texts can map to its expected emotion."""
        for target_emotion, text in EXAMPLES.items():
            with self.subTest(emotion=target_emotion):
                scores = {name: 0.025 for name in EMOTIONS}
                scores[target_emotion] = 0.9
                response = Mock(status_code=200)
                response.json.return_value = {
                    "emotionPredictions": [{"emotion": scores}]
                }
                mock_post.return_value = response
                actual = emotion_detector(text)
                self.assertEqual(actual["dominant_emotion"], target_emotion)
                self.assertEqual(actual[target_emotion], 0.9)
                self.assertEqual(len(actual), 6)

    @patch("EmotionDetection.emotion_detection.requests.post")
    def test_watson_request_format(self, mock_post):
        """Send text and model ID to the expected Watson endpoint."""
        response = Mock(status_code=200)
        response.json.return_value = {
            "emotionPredictions": [{
                "emotion": {name: 0.2 for name in EMOTIONS}
            }]
        }
        mock_post.return_value = response
        emotion_detector(EXAMPLES["joy"])
        _, kwargs = mock_post.call_args
        self.assertEqual(kwargs["json"]["raw_document"]["text"],
                         EXAMPLES["joy"])
        self.assertIn("grpc-metadata-mm-model-id", kwargs["headers"])
        self.assertEqual(kwargs["timeout"], 20)

    @patch("EmotionDetection.emotion_detection.requests.post")
    def test_blank_text(self, mock_post):
        """Blank input produces six None values without a network call."""
        for invalid in ("", "   ", None):
            with self.subTest(input_text=invalid):
                result = emotion_detector(invalid)
                self.assertEqual(set(result), set(EMOTIONS) |
                                 {"dominant_emotion"})
                self.assertTrue(all(value is None for value in result.values()))
        mock_post.assert_not_called()

    @patch("EmotionDetection.emotion_detection.requests.post")
    def test_http_400(self, mock_post):
        """Watson bad-request responses produce six None values."""
        mock_post.return_value = Mock(status_code=400)
        result = emotion_detector("invalid")
        self.assertTrue(all(value is None for value in result.values()))

    @patch("EmotionDetection.emotion_detection.requests.post")
    def test_http_500_is_not_disguised_as_success(self, mock_post):
        """HTTP 500 should propagate a network/service error."""
        from requests import HTTPError

        response = Mock(status_code=500)
        response.raise_for_status.side_effect = HTTPError("server error")
        mock_post.return_value = response
        with self.assertRaises(HTTPError):
            emotion_detector("Hello")


if __name__ == "__main__":
    unittest.main(verbosity=2)
