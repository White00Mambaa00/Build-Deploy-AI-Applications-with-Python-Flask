# Emotion Detector — AI Application Using Python & Flask

## Project Overview

This project is developed as part of the Coursera course **Build & Deploy AI Applications with Python & Flask**.

The Emotion Detector is an AI-powered web application that analyzes text using IBM Watson NLP and identifies the dominant emotion expressed.

## Features

- Detects five emotions: anger, disgust, fear, joy, and sadness.
- Identifies the dominant emotion.
- Provides a web interface using Flask.
- Handles invalid or empty inputs.
- Includes Python unit tests.
- Supports static code analysis using Pylint.

## Technologies Used

- Python
- Flask
- IBM Watson NLP
- REST API
- Python Unittest
- Pylint
- HTML and JavaScript

## Project Structure

```text
oaqjp-final-project-emb-ai/
├── EmotionDetection/
│   ├── __init__.py
│   └── emotion_detection.py
├── templates/
│   └── index.html
├── static/
├── server.py
├── test_emotion_detection.py
├── requirements.txt
└── README.md
```

## Installation and Execution

Install dependencies:

```bash
python3 -m pip install -r requirements.txt
```

Run the Flask application:

```bash
python3 server.py
```

Open the application:

`http://localhost:5000`

Run unit tests:

```bash
python3 -m unittest -v test_emotion_detection.py
```

Run static code analysis:

```bash
pylint server.py
```

## Note

Live emotion detection requires access to the IBM Skills Network Watson NLP service, which may be limited to the course lab environment.

## Course Information

**Course:** Build & Deploy AI Applications with Python & Flask

**Platform:** Coursera

**Project:** Emotion Detector — Final Project

**Purpose:** Educational and practical implementation of AI application development using Python and Flask.
