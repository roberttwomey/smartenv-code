# smartenv-code
code examples for EMAR391 009 Smart Environments SP22

## RPI as IoT Gatweay
Reads BLE advertising packets to parse accelerometer (and other) data. Transmit these to a mqtt broker (shiftr.io). Runs as a service on the Raspbery Pi.
- see files here [ble/](ble)

## To verify mqtt messaging: 
We are exploring shiftr.io as our mqtt broker. You can view a live visualization of their public broker here: [https://www.shiftr.io/try/](https://www.shiftr.io/try/)

## p5 mqtt examples
These examples explore sending (publishing), receiving (subscribing) and doing other things with the mqtt messages.

- mqtt subscriber: https://editor.p5js.org/robert.twomey/sketches/dojZRNiSP
- mqtt publishers:  https://editor.p5js.org/robert.twomey/sketches/CEXVmsCBS
- mqtt subscriber: https://editor.p5js.org/robert.twomey/sketches/pZNnpo2GOD

__Don't try these (experimental)__
- mqttSubscriber_G1: https://editor.p5js.org/robert.twomey/sketches/-djHYLWZy
- mqttSubscriber_bargraph: https://editor.p5js.org/robert.twomey/sketches/dA6aKcBpu9
- subscribe_3dmodel: https://editor.p5js.org/robert.twomey/sketches/cA0f-c5y0
