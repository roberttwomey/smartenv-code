# Respeaker 6-Microphone Array
<img src="https://user-images.githubusercontent.com/1598545/157468792-177624b7-5c33-4fd7-a845-4401881f29e2.png" width=600>

Capabilities:
- [Speech Recognition](#speech-recognition) - listening for audio and transcribing it / pushing it to shiftr
  - [speechSubscriber p5](#speech-subscriber-p5)
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

Publishes to `/smartenv/respeaker/speech`

### Speech Subscriber p5
This sketch subscribes to the respeaker and listens for recognition results:

[speechSubscriber_mqtt](https://editor.p5js.org/robert.twomey/full/9rzxlO4Qs) ([code](https://editor.p5js.org/robert.twomey/sketches/9rzxlO4Qs))

## Indicator Lights
Use the p5 [mqttPublisher](https://editor.p5js.org/robert.twomey/full/CEXVmsCBS) ([code](https://editor.p5js.org/robert.twomey/sketches/CEXVmsCBS)) to control the light ring.

Subscribes to topic: `/smartenv/respeaker/lights`

Control Messages:
  - `/smartenv/respeaker/lights` with value `wake`
  - `/smartenv/respeaker/lights` with value `listen`
  - `/smartenv/respeaker/lights` with value `think`
  - `/smartenv/respeaker/lights` with value `sleep`
  - `/smartenv/respeaker/lights` with value `off`
  - `/smartenv/respeaker/lights` with value `color R G B` where you specify Red, Green, and Blue as 0-255 integers
    - <img width="369" alt="image" src="https://user-images.githubusercontent.com/1598545/155913062-76b7b920-d800-406c-818c-178ca0fb44b7.png">


Example adapted from [respeaker pixel_ring examples](https://github.com/respeaker/pixel_ring/blob/master/examples/respeaker_4mic_array.py) with some MQTT special sauce.


## Wakeword Detection
[Not yet implemented]

# Setup

__Install Respeaker__
(NOTE: this only runs on raspbian 32bit right now ca. March 2022)

from https://wiki.seeedstudio.com/ReSpeaker_6-Mic_Circular_Array_kit_for_Raspberry_Pi/

```
sudo apt-get update
sudo apt-get upgrade
git clone https://github.com/respeaker/seeed-voicecard.git
cd seeed-voicecard
sudo ./install.sh   
sudo reboot
```

__Install pypi SpeechRecognition__
(multi-platform, defaults to google voice services, for free!)

packages: 
```
sudo apt-get install flac
sudo apt-get install libfftw3-dev libconfig-dev libasound2-dev libgconf-2-4
sudo apt-get install libportaudio2
```

python modules:
```
pip instal pyaudio
pip install SpeechRecognition
pip install paho-mqtt
```

__Install this code__
```
git clone https://github.com/roberttwomey/smartenv-code
```

run the respeaker service (lights and speech rec):
```
cd ~/smartenv-code/respeaker
python respeaker_service.py
```

# References
- speechrecognition source code: https://github.com/Uberi/speech_recognition
  - pypi page: https://pypi.org/project/SpeechRecognition/
- pixel_ring source code: https://github.com/respeaker/pixel_ring
- picovoice porcupine respeaker demo: https://github.com/Picovoice/porcupine/tree/master/demo/respeaker/ppnrespeakerdemo
