# smartenv-code
code examples for EMAR391 009 Smart Environments SP22

Technologies: 
- [Respeaker](#respeaker) circular and linear mic arrays (4-6 mics)
- [Coral Board](#google-coral-board) edge inference (mobilenet, yolo, face detection, etc.)
- [Raspberry Pi](#raspberry-pi) media playback
- [IoT Gateway](#iot-gateway) relaying BLE and other sensor signals
- [Particle Photon](#particle-photon) actuators
- [BLE Sensor Tags](#ble-sensor-tags) event-triggered acceleration, door opening, temperature and humidity

# Respeaker

- wake word detection
- live speech transcription (ASR)
- live speech transcription and Direction of Arrival (DOA)
- ODAS (Open embeddeD Audition System) https://github.com/introlab/odas
- controlling the pixel ring on the respeaker, from [respeaker pixel_ring examples](https://github.com/respeaker/pixel_ring/blob/master/examples/respeaker_4mic_array.py):
  - `/smartenv/respeaker/wakeup`
  - `/smartenv/respeaker/think`
  - `/smartenv/respeaker/sleep`
  - `/smartenv/respeaker/off`
## Picovoice Porcupine
- picovoice porcupine respeaker demo: https://github.com/Picovoice/porcupine/tree/master/demo/respeaker/ppnrespeakerdemo
- 
 
__References__
- pixel_ring repository https://github.com/respeaker/pixel_ring

# Google Coral Board
AI inference at the edge. Computer vision and speech recognition. 

# Raspberry Pi
Can do a lot. We will primarily use it as an output device (audio, video, etc.) 

# IoT gateway
Reading BLE esensor tags and streaming data to MQTT broker or other cloud system. Minew G1 IoT Gateway

# Particle Photon
Wireless-enabled microcontroller. Can use to operate actuators. 

# BLE Sensor Tags

## RPI as IoT Gatweay
Reads BLE advertising packets to parse accelerometer (and other) data. Transmit these to a mqtt broker (shiftr.io). Runs as a service on the Raspbery Pi.
- see files here [ble/](ble)

## Message Broker
We are exploring shiftr.io as our mqtt broker. You can view a live visualization of their public broker here: [https://www.shiftr.io/try/](https://www.shiftr.io/try/)

## p5 examples

These examples explore sending (publishing), receiving (subscribing) and doing other things with the mqtt messages. They require you to be in a room with the G1 gateway in order to function and transmit data to the cloud.

### E8 Sensor Tags
Use the G1 Iot gateway to read tags. Work with accelerometer data.
- tagPublisher_slider: https://editor.p5js.org/robert.twomey/sketches/lkXZ4-Aa8
  - (uses sliders to simluate accelerometers)
- tagSubscriber_bargraph: https://editor.p5js.org/robert.twomey/sketches/dA6aKcBpu9 
  - (receives data and displays accelerometer as a bar graph)
- tagSubscriber_teapot: https://editor.p5js.org/robert.twomey/sketches/cA0f-c5y0
  - (receives data and uses accelerometer to rotate teapot)

### S1 Temperature/Humidity
- tempSubscriber_mqtt: https://editor.p5js.org/robert.twomey/sketches/z4lshxu06
  - (reads and displays values from temp/humidity sensor)

### S4 Door Sensors
- doorSubscriber_mqtt: https://editor.p5js.org/robert.twomey/sketches/UWiFQoxSg
  - (reads and displays open/shut, uninstalled, changed from door sensor)

### Leftovers
__Tests__
- mqttPublisher_JSON: https://editor.p5js.org/robert.twomey/sketches/uaCayQRDB
  - (sends a static data packet in JSON format, as it were the G1 gateway)
- mqttSubscriber_G1: https://editor.p5js.org/robert.twomey/sketches/-djHYLWZy
  - (receives data in JSON format from G1 gateway)

__Old Sketches (v1)__
These do not use the G1 gateway, and do not send messages as JSON:

- mqtt publisher:  https://editor.p5js.org/robert.twomey/sketches/CEXVmsCBS
- mqtt subscriber: https://editor.p5js.org/robert.twomey/sketches/dojZRNiSP
- mqtt logger: https://editor.p5js.org/robert.twomey/sketches/pZNnpo2GOD
