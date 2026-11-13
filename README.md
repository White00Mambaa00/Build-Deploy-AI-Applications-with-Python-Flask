# Emotion Detector — IBM Skills Network Final Project

A Flask application that sends input text to IBM Skills Network's Watson NLP EmotionPredict service and returns anger, disgust, fear, joy, sadness, and the dominant emotion.

## Contents

- `EmotionDetection/emotion_detection.py` — Watson NLP integration and output formatting
- `EmotionDetection/__init__.py` — package export
- `server.py` — Flask website with `/emotionDetector?textToAnalyze=...`
- `test_emotion_detection.py` — offline unit tests (mocked Watson API)
- `templates/index.html` and `static/*` — UI
- `submission_guide.md` — exact answers and evidence commands for questions 1–16
- `submission_snippets/` — saved copies of code for the named submission questions

## Installation

```bash
python3 -m pip install -r requirements.txt
python3 -m unittest -v test_emotion_detection.py
python3 server.py
```

Open http://127.0.0.1:5000 and enter `I think I am having fun`.
The web interface calls the Watson NLP endpoint when it analyzes text.

**Important:** The `sn-watson-emotion.labs.skills.network` endpoint is supplied by the IBM Skills Network labs. It may not be reachable outside the course's cloud environment. The mocked tests can run without network access; live score evidence must be captured where the endpoint actually works.

The Flask development server binds on port 5000 so the cloud lab preview can reach it. Do not use the Flask development server as a public production server.

## Example package import

```bash
python3 -c "from EmotionDetection.emotion_detection import emotion_detector; print(emotion_detector('I am really mad about this'))"
```

## Static code analysis

```bash
pylint server.py
```

## GitHub submission

Create a public repository named `oaqjp-final-project-emb-ai`, upload the actual project, and submit your own links to `README.md` and `EmotionDetection/__init__.py`. This template does **not** create a remote repository or fabricate any grader screenshots.
