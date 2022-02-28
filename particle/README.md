Wireless IoT microcontroller can operate sensors and actuators.
# Setup
Follow particle instructions: [TK]

# Programming
Use Particle Web IDE: https://build.particle.io/

# Examples

## mqttRelay

Source code link: https://go.particle.io/shared_apps/621c4137366a9b0009b32c69

Subscribes to MQTT topic `/smartenv/photon1`

Messages:

Indicator light: 
- `red` turns indicator LED red
- `blue` turns indicator LED blue
- `green` turns indicator LED green

Relay control (attached to pin D0): 
- `on` turns relay on
- `off` turns realy off

__Usage__

Turn relay on: 
<img width="312" alt="image" src="https://user-images.githubusercontent.com/1598545/155919888-d36e200e-ebb1-4f62-a16a-ae6e84618ad5.png">

Turn relay off:

<img width="310" alt="image" src="https://user-images.githubusercontent.com/1598545/155919901-c60193ac-b4ea-4248-90b1-6887a44c5053.png">

