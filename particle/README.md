<img width="500" alt="image" src="https://user-images.githubusercontent.com/1598545/156173775-de7fc8b5-dbc1-44ea-a595-46f8b465a160.png">
Wireless IoT microcontroller can operate sensors and actuators. [Particle.io](https://www.particle.io/)

# Setup
Follow particle instructions. Prof. Twomey did this. 

Login to https://build.particle.io/

1. complete the doctor to reinstall firmware and restore default Tinker app:
   - particle device doctor
3. hold down setup for 3 seconds to get into listening mode (blue flash)
4. particle serial mac - to get MAC address
5. register for the NU-IoT network: https://nu-net.nebraska.edu/guest/mac_create.php
6. Run wifi config to get it online with the NU-IoT password produced in the device above
7. Get the device ID: 
   - particle identify
8. Claim the device: 
   - particle device add 2f0026001047343339383037


# Programming
Use Particle Web IDE: https://build.particle.io/

# Examples

## mqttRelay

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
