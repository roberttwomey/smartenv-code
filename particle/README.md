<img width="500" alt="image" src="https://user-images.githubusercontent.com/1598545/156173775-de7fc8b5-dbc1-44ea-a595-46f8b465a160.png">
[Particle.io](https://www.particle.io/) makes wireless IoT microcontroller that can operate sensors and actuators. 

We are using the Particle [Photon](https://docs.particle.io/photon/), their WiFi development board. They also make BLE, Mesh, 3G cellular, and other devices.



# Setup
You should not need to do this. I have pre-programmed these to work with MQTT, so they are running "firmware" (no need to change it). These instructions are for reference.

Login to https://build.particle.io/ with your particle account.

1. complete the doctor to reinstall firmware and restore default Tinker app:
   - `particle device doctor`
   - you can select the WiFi network, and put in a dummy password. 
2. hold down setup for 3 seconds to get into listening mode (blue flash)
3. to get MAC address:
   - `particle serial mac`
4. register for the NU-IoT network: https://nu-net.nebraska.edu/guest/mac_create.php
5. Run wifi config:
   - `particle serial wifi`
   - Yes scan
   - NU-IoT
   - Yes detect security
   - enter the password from the IoT registration above
6. Get the device ID: 
   - particle identify
7. Claim the device: 
   - particle device add 2f0026001047343339383037
8. It should now show up in your console: https://console.particle.io/devices/

# Programming

The particle devices are a lot like arduinos, except you can program and flash them over the internet. Use Particle Web IDE to write new code: https://build.particle.io/

I have preprogrammed these to interact via MQTT (same as our BLE tags), so you won't need to reprogram for basic stuff.

# Examples

## Electroechanical Relay

Source code link: https://go.particle.io/shared_apps/621c4137366a9b0009b32c69

The particle photon connects to NU-IoT and then subscribes to an MQTT topic.

We can use the p5 [mqttPublisher](https://editor.p5js.org/robert.twomey/full/CEXVmsCBS) to test it out. ([edit link](https://editor.p5js.org/robert.twomey/sketches/CEXVmsCBS)).

__Topic__: `/smartenv/photon1`

__Messages__

Relay control: 
- (attached to pin D0)
- `on` turns relay on
  -  <img width="312" alt="image" src="https://user-images.githubusercontent.com/1598545/155919888-d36e200e-ebb1-4f62-a16a-ae6e84618ad5.png">
- `off` turns realy off
  - <img width="310" alt="image" src="https://user-images.githubusercontent.com/1598545/155919901-c60193ac-b4ea-4248-90b1-6887a44c5053.png">

Indicator light: 
- `red` turns indicator LED red
- `blue` turns indicator LED blue
- `green` turns indicator LED green
- `white` (or anything that is not the above 5 commands) turns the indicator LED white

## Servo
Moving a motor.
