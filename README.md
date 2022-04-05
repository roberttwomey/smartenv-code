# smartenv-code
code examples for EMAR391 009 Smart Environments SP22

Software:
- [p5](#p5) using p5.js on the web to interact via mqtt messaging
- [PureData](/puredata) mqtt messaging with puredata

Hardware: 
- [BLE Sensor Tags](#ble-sensor-tags) event-triggered acceleration, door opening, temperature and humidity
- [IoT Gateway](#iot-gateway) relaying BLE and other sensor signals
- [Particle Photon](/particle) wireless IoT board to do sensors and actuators over wifi
- [Respeaker](/respeaker) circular and linear mic arrays (4-6 mics). can also *play* audio with an attached speaker.
- [e-Ink](/eink) electronic ink displays as "quiet" outputs.
- [NFC tags](/nfc) Near Field Communication as passive sensor readings.
- [Raspberry Pi](#raspberry-pi) media playback controlled by MQTT.
- [Coral Board](#google-coral-board) edge inference (mobilenet, yolo, face detection, etc.)
- [Robots](/xarm) xArm7 co-robotic arm for posing and replaying action.

[MQTT](https://mqtt.org/) Platforms:
- We are exploring [shiftr.io](https://www.shiftr.io/try/) as our mqtt broker. We can use the eclipse mqtt server instead. You can view a live visualization of their public broker here: https://www.shiftr.io/try/. 

# Google Coral Board
AI inference at the edge. Computer vision and speech recognition. 

# Raspberry Pi
Can do a lot. We will primarily use it as an output device (audio, video, etc.) 

# IoT gateway
Reading BLE esensor tags and streaming data to MQTT broker or other cloud system. Minew G1 IoT Gateway

# BLE Sensor Tags


## RPI as IoT Gatweay
Reads BLE advertising packets to parse accelerometer (and other) data. Transmit these to a mqtt broker (shiftr.io). Runs as a service on the Raspbery Pi.
- see files here [ble/](ble)

## Message Broker
We are exploring shiftr.io as our mqtt broker. You can view a live visualization of their public broker here: [https://www.shiftr.io/try/](https://www.shiftr.io/try/)

## p5

These examples explore sending (publishing), receiving (subscribing) and doing other things with the mqtt messages. They require you to be in a room with the G1 gateway in order to function and transmit data to the cloud.

### Simple Message Publishing
<img width="638" alt="image" src="https://user-images.githubusercontent.com/1598545/156566203-1ebb0f9d-8086-47fa-b5db-3a27fc943496.png">

This sketch lets you type in an address ("topic"), and send a message. It is great for testing things out:

[mqttPublisher sketch](https://editor.p5js.org/robert.twomey/full/CEXVmsCBS) ([code](https://editor.p5js.org/robert.twomey/sketches/CEXVmsCBS))

### E8 Sensor Tags
Use the G1 Iot gateway to read tags. Work with accelerometer data.
- tagPublisher_slider: https://editor.p5js.org/robert.twomey/sketches/lkXZ4-Aa8
  - (uses sliders to simluate accelerometers)
- tagSubscriber_bargraph: https://editor.p5js.org/robert.twomey/sketches/dA6aKcBpu9 
  - (receives data and displays accelerometer as a bar graph)

Figure out which side of the tag is facing up:
- tagSubscriber_conditional: https://editor.p5js.org/robert.twomey/sketches/rPfv9jPlM
  - (uses if statements to decide which edge the tag is oriented on) 

Move a teapot:
- tagSubscriber_teapot: https://editor.p5js.org/robert.twomey/sketches/cA0f-c5y0
  - (receives data and uses accelerometer to rotate teapot. the 3DOF accel to pitch/roll is somewhat buggy, so this is inexact)

Use the tag to trigger events: 
- tag_triggered_relay: https://editor.p5js.org/robert.twomey/sketches/EPNmEcFlJ
  - (triggers an action everytime the tag is moved. resets after some interval)
- tag_triggerd_video: https://editor.p5js.org/robert.twomey/sketches/W8ZmOREYX
  - (**play video** when tag moves)

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
