# Local verification (not submission proof of live Watson NLP)

- The project was syntax-compiled with Python 3.13.
- Five `unittest` methods ran and passed, including subtests for all five emotions.
- Watson API responses were **mocked** in the tests, so this does **not** verify live model accuracy or model-service availability.
- Flask and Pylint were unavailable in the local execution environment; you must install dependencies in your course lab, verify the Flask interface, and collect the real Pylint output yourself.

See `local_test_output.txt` for the actual local test run.
