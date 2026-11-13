"""Flask interface for the IBM Watson NLP emotion-detection project."""

from flask import Flask, render_template, request
from requests import RequestException

from EmotionDetection import emotion_detector

app = Flask(__name__)


@app.route("/")
def home():
    """Render the emotion-detection web interface."""
    return render_template("index.html")


@app.route("/emotionDetector", methods=["GET"])
def emotion_detector_route():
    """Analyze the textToAnalyze parameter and display the five scores."""
    text_to_analyze = request.args.get("textToAnalyze", "")
    if not text_to_analyze.strip():
        return "Invalid text! Please try again!"

    try:
        result = emotion_detector(text_to_analyze)
    except RequestException:
        app.logger.exception("Watson NLP request failed")
        return "Emotion detection service is temporarily unavailable.", 503
    except (ValueError, KeyError, IndexError, TypeError):
        app.logger.exception("Watson NLP returned an invalid response")
        return "Emotion detection service returned an invalid response.", 502

    if result["dominant_emotion"] is None:
        return "Invalid text! Please try again!"

    return (
        "For the given statement, the system response is "
        f"'anger': {result['anger']}, "
        f"'disgust': {result['disgust']}, "
        f"'fear': {result['fear']}, "
        f"'joy': {result['joy']}, "
        f"'sadness': {result['sadness']}. "
        f"The dominant emotion is {result['dominant_emotion']}."
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
