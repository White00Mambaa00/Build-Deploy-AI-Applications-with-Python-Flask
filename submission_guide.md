# Submission map: Question 1 to Question 16

**Do not submit invented terminal output, GitHub URLs, or screenshots.** Code files are supplied here. Execute the commands in your own environment and capture the resulting outputs; live model evidence requires the Watson endpoint to work in the IBM course lab.

| Question | Type | What to submit |
|---|---|---|
| Q1 | URL | `https://github.com/<YOUR_USERNAME>/oaqjp-final-project-emb-ai/blob/main/README.md` after uploading |
| Q2 | TEXT | Copy the full text from `submission_snippets/2a_emotion_detection.py` |
| Q3 | TEXT | Actual terminal output from command A below, save as `2b_application_creation.txt` |
| Q4 | TEXT | Copy the full text from `submission_snippets/3a_output_formatting.py` |
| Q5 | TEXT | Actual terminal output from command B, save as `3b_formatted_output.txt` |
| Q6 | URL | `https://github.com/<YOUR_USERNAME>/oaqjp-final-project-emb-ai/blob/main/EmotionDetection/__init__.py` after uploading |
| Q7 | TEXT | Actual terminal output from command C, save as `4b_packaging_test.txt` |
| Q8 | TEXT | Copy the full text from `submission_snippets/5a_unit_testing.py` |
| Q9 | TEXT | Actual terminal output from command D, save as `5b_unit_testing_result.txt` |
| Q10 | TEXT | Copy the full text from `submission_snippets/6a_server.py` |
| Q11 | UPLOAD | Capture the live browser with text `I think I am having fun`, visible result and `dominant emotion is joy`; save `6b_deployment_test.png` |
| Q12 | TEXT | Copy the full text from `submission_snippets/7a_error_handling_function.py` |
| Q13 | TEXT | Copy the full text from `submission_snippets/7b_error_handling_server.py` |
| Q14 | UPLOAD | Capture the live browser after analyzing blank input showing `Invalid text! Please try again!`; save `7c_error_handling_interface.png` |
| Q15 | TEXT | Copy the full text from `submission_snippets/8a_server.py` |
| Q16 | TEXT | Actual terminal output from command E, save as `8b_static_code_analysis.txt` |

## Evidence commands

Run these inside the project root (`cd EmotionDetector_FinalProject`).

### A: Question 3 — application creation

```bash
python3 -c "from EmotionDetection import emotion_detector; print(emotion_detector('I love this new technology'))" 2>&1 | tee 2b_application_creation.txt
```

### B: Question 5 — formatting

```bash
python3 -c "from EmotionDetection import emotion_detector; print(emotion_detector('I am glad this happened'))" 2>&1 | tee 3b_formatted_output.txt
```

Check that the actual dict has six fields and `dominant_emotion` is `joy`.

### C: Question 7 — package validation

```bash
python3 -c "from EmotionDetection.emotion_detection import emotion_detector; print(emotion_detector('I am really mad about this'))" 2>&1 | tee 4b_packaging_test.txt
```

Check that `dominant_emotion` is `anger` in the actual API response.

### D: Question 9 — unit tests

```bash
python3 -m unittest -v test_emotion_detection.py 2>&1 | tee 5b_unit_testing_result.txt
```

This suite uses a **mocked** Watson response to test Python logic. It proves parsing/error handling but is **not** evidence that the live IBM Watson service has responded.

### E: Question 16 — Pylint

```bash
pylint server.py 2>&1 | tee 8b_static_code_analysis.txt
```

Verify the actual score shown by Pylint before submission; no particular numeric score is pre-assumed here.

## Screenshots for Questions 11 and 14

Start Flask with `python3 server.py` and open `http://127.0.0.1:5000`.

1. For Q11, type `I think I am having fun`, click **Analyze emotion**, and capture both the entered text and generated result. You need the course Watson endpoint to respond for the joy result.
2. For Q14, clear all the text, click **Analyze emotion**, verify the page displays `Invalid text! Please try again!`, and capture this as `7c_error_handling_interface.png`.

## GitHub CLI instructions

Create a **public** empty GitHub repository with the exact required name via the GitHub website. Then run from the project folder (replace `<YOUR_USERNAME>`):

```bash
git init
git add .
git commit -m "Complete IBM emotion detector final project"
git branch -M main
git remote add origin https://github.com/<YOUR_USERNAME>/oaqjp-final-project-emb-ai.git
git push -u origin main
```

If your existing course fork already has a remote, use its actual public repository URL instead of adding a duplicate remote.
