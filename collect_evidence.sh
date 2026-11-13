#!/usr/bin/env bash
# Run in the course environment where Watson NLP endpoint is reachable.
set -u
python3 -c "from EmotionDetection import emotion_detector; print(emotion_detector('I love this new technology'))" 2>&1 | tee 2b_application_creation.txt
python3 -c "from EmotionDetection import emotion_detector; print(emotion_detector('I am glad this happened'))" 2>&1 | tee 3b_formatted_output.txt
python3 -c "from EmotionDetection.emotion_detection import emotion_detector; print(emotion_detector('I am really mad about this'))" 2>&1 | tee 4b_packaging_test.txt
python3 -m unittest -v test_emotion_detection.py 2>&1 | tee 5b_unit_testing_result.txt
pylint server.py 2>&1 | tee 8b_static_code_analysis.txt
echo 'Capture the real web page for Questions 11 and 14 manually.'
