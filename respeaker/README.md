# Examples for Respeaker 6-Microphone Array

The best solution I have found is the [speechrecognition](https://pypi.org/project/SpeechRecognition/) package, which uses google speech services by default.

# Setup

[details to come]

# Use
Script that will listen to the microphone, recognize with google speech, and stream to mqtt broker:
`python speechrecognition_mqtt.py`

topic is `smartenv/speechrec`

# P5

- mqtt subscriber that listens for recognized speech: https://editor.p5js.org/robert.twomey/sketches/9rzxlO4Qs

# References
- speechrecognition source code: https://github.com/Uberi/speech_recognition
  - pypi page: https://pypi.org/project/SpeechRecognition/