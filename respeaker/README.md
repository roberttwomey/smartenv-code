# Examples for Respeaker 6-Microphone Array

The best solution I have found is the [speechrecognition](https://pypi.org/project/SpeechRecognition/) package, which uses google speech services by default.

# Setup

[details to come]

# Use

## Live Speech Recognition
This script that will listen to the microphone, recognize with google speech, and stream to an mqtt broker:

`python speechrecognition_mqtt.py`

the topic is `smartenv/speechrec`

__Speech Subscriber in p5__ 

- speechSubscriber_mqtt: https://editor.p5js.org/robert.twomey/sketches/9rzxlO4Qs
  - (mqtt subscriber that listens for recognized speech)

## Control The Lights
Use our p5 mqtt publisher example with the following address and message: https://editor.p5js.org/robert.twomey/sketches/CEXVmsCBS
<img width="600" alt="image" src="https://user-images.githubusercontent.com/1598545/155911682-2b705b31-fd37-4f91-b8c5-f247b3f44e58.png">


# References
- speechrecognition source code: https://github.com/Uberi/speech_recognition
  - pypi page: https://pypi.org/project/SpeechRecognition/
