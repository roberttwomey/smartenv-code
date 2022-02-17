# smartenv-code
code examples for EMAR391 009 Smart Environments SP22

## RPI as IoT Gatweay
Reads BLE advertising packets to parse accelerometer (and other) data. Transmit these to a mqtt broker (shiftr.io). Runs as a service on the Raspbery Pi.
- see files here [ble/](ble)

## To verify mqtt messaging: 
We are exploring shiftr.io as our mqtt broker. You can view a live visualization of their public broker here: [https://www.shiftr.io/try/](https://www.shiftr.io/try/)

## p5 mqtt examples

These examples explore sending (publishing), receiving (subscribing) and doing other things with the mqtt messages.

- mqtt publisher:  https://editor.p5js.org/robert.twomey/sketches/CEXVmsCBS
- mqtt subscriber: https://editor.p5js.org/robert.twomey/sketches/dojZRNiSP
- mqtt logger: https://editor.p5js.org/robert.twomey/sketches/pZNnpo2GOD

__Don't try these (experimental)__
These use the G1 IoT gateway and should be much less buggy than the raspberry pi.
- mqttPublisher_slider: uses sliders to simluate accelerometers
  - https://editor.p5js.org/robert.twomey/sketches/lkXZ4-Aa8
- mqttSubscriber_G1: https://editor.p5js.org/robert.twomey/sketches/-djHYLWZy
  - (receives data in JSON format)
- mqttSubscriber_bargraph: https://editor.p5js.org/robert.twomey/sketches/dA6aKcBpu9 
  - (receives data and displays accelerometer as a bar graph)
- mqttSubscriber_teapot: https://editor.p5js.org/robert.twomey/sketches/cA0f-c5y0
  - (receives data and uses accelerometer to rotate teapot)

__Leftovers__
- mqttPublisher_JSON: https://editor.p5js.org/robert.twomey/sketches/uaCayQRDB
  - (sends a static data packet in JSON format)
