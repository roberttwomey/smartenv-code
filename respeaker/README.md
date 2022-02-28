# Examples for Respeaker 6-Microphone Array
The product: 

Capabilities:
- wake word detection
- live speech transcription (ASR)
- live speech transcription and Direction of Arrival (DOA)
- ODAS (Open embeddeD Audition System) https://github.com/introlab/odas
- controlling the pixel ring on the respeaker
- 


# Setup

[details to come]

# Use

## Speech Recognition
The best solution I have found is the [speechrecognition](https://pypi.org/project/SpeechRecognition/) package, which uses google speech services by default.

This script will listen to the microphone, recognize with google speech, and stream to an mqtt broker:

`python speechrecognition_mqtt.py`

the topic is `smartenv/speechrec`

__Speech Subscriber in p5__ 

- speechSubscriber_mqtt: https://editor.p5js.org/robert.twomey/sketches/9rzxlO4Qs
  - (mqtt subscriber that listens for recognized speech)

## Indicator Lights
Use our p5 [mqttPublisher](https://editor.p5js.org/robert.twomey/sketches/CEXVmsCBS) example with the following topic and message: 
<img width="600" alt="image" src="https://user-images.githubusercontent.com/1598545/155911682-2b705b31-fd37-4f91-b8c5-f247b3f44e58.png">

Topic: `/smartenv/audionode`

Control Messages:
  - `/smartenv/audionode` with value `wake`
  - `/smartenv/audionode` with value `think`
  - `/smartenv/audionode` with value `sleep`
  - `/smartenv/audionode` with value `off`
  - `/smartenv/audionode` with value `color R G B` NOT YET IMPLEMENTED

Example adapted from [respeaker pixel_ring examples](https://github.com/respeaker/pixel_ring/blob/master/examples/respeaker_4mic_array.py) with some MQTT special sauce.


## Wakeword Detection
[Not yet implemented]

# References
- speechrecognition source code: https://github.com/Uberi/speech_recognition
  - pypi page: https://pypi.org/project/SpeechRecognition/
- picovoice porcupine respeaker demo: https://github.com/Picovoice/porcupine/tree/master/demo/respeaker/ppnrespeakerdemo
