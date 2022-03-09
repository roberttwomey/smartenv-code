# Examples for the Respeaker 6-Microphone Array
[this product]

Capabilities:
- [Speech Recognition](#speech-recognition) - listening for audio and transcribing it / pushing it to shiftr
- [Indicator Lights](#indicator-lights) - controlling the indicator lights / pixel ring on the respeaker
- Wake Word Detection
- Direction of Arrival (DOA) — where did sound come from
- ODAS (Open embeddeD Audition System) https://github.com/introlab/odas

# Setup

[details to come]

# Use

## Speech Recognition
The best solution I have found is the [speechrecognition](https://pypi.org/project/SpeechRecognition/) package, which uses google speech services by default.

This script will listen to the microphone, recognize anything it hears, and send the result to an mqtt broker. To start the script on the pi use:

To run the script on the pi: 
`python speechrecognition_mqtt.py`

Publishes to `smartenv/audionode/speech`

### Speech Subscriber p5

- speechSubscriber_mqtt: https://editor.p5js.org/robert.twomey/sketches/9rzxlO4Qs
  - (mqtt subscriber that listens for recognized speech)

## Indicator Lights
Use the p5 [mqttPublisher](https://editor.p5js.org/robert.twomey/sketches/CEXVmsCBS) example to control the light ring.

MQTT Topic: `/smartenv/audionode`

Control Messages:
  - `/smartenv/audionode` with value `wake`
    - <img width="600" alt="image" src="https://user-images.githubusercontent.com/1598545/155911682-2b705b31-fd37-4f91-b8c5-f247b3f44e58.png">
  - `/smartenv/audionode` with value `think`
  - `/smartenv/audionode` with value `sleep`
  - `/smartenv/audionode` with value `off`
  - `/smartenv/audionode` with value `color R G B`
    - <img width="369" alt="image" src="https://user-images.githubusercontent.com/1598545/155913062-76b7b920-d800-406c-818c-178ca0fb44b7.png">


Example adapted from [respeaker pixel_ring examples](https://github.com/respeaker/pixel_ring/blob/master/examples/respeaker_4mic_array.py) with some MQTT special sauce.


## Wakeword Detection
[Not yet implemented]

# References
- speechrecognition source code: https://github.com/Uberi/speech_recognition
  - pypi page: https://pypi.org/project/SpeechRecognition/
- pixel_ring source code: https://github.com/respeaker/pixel_ring
- picovoice porcupine respeaker demo: https://github.com/Picovoice/porcupine/tree/master/demo/respeaker/ppnrespeakerdemo
