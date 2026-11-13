"""Analyze text with the IBM Skills Network Watson NLP emotion API."""

import requests

EMOTION_URL = (
    "https://sn-watson-emotion.labs.skills.network/"
    "v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"
)
HEADERS = {
    "grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"
}
EMOTIONS = ("anger", "disgust", "fear", "joy", "sadness")


def _empty_result():
    """Return the required six keys when input is invalid (HTTP 400)."""
    return {**dict.fromkeys(EMOTIONS), "dominant_emotion": None}


def emotion_detector(text_to_analyze):
    """Return five emotion scores and the dominant emotion for input text.

    Blank text and a Watson HTTP 400 response return None for every field.
    Network or server errors are propagated so the Flask layer can report
    service unavailability without pretending an emotion was detected.
    """
    if not isinstance(text_to_analyze, str) or not text_to_analyze.strip():
        return _empty_result()

    payload = {"raw_document": {"text": text_to_analyze}}
    response = requests.post(
        EMOTION_URL, headers=HEADERS, json=payload, timeout=20
    )
    if response.status_code == 400:
        return _empty_result()

    response.raise_for_status()
    predictions = response.json()["emotionPredictions"]
    raw_emotions = predictions[0]["emotion"]
    scores = {emotion: float(raw_emotions[emotion]) for emotion in EMOTIONS}
    return {**scores, "dominant_emotion": max(scores, key=scores.get)}
