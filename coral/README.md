# Description
[TK]

# Setup
- Follow https://coral.ai/docs/dev-board/get-started#flash-the-board: burn the image, switch the DIP switches, and boot the card. 
- Install the mendel dev tools: `python3 -m pip install --user mendel-development-tool`
- Install the USB drivers for MacOS https://coral.ai/docs/dev-board/serial-console/#connect-with-macos
... more steps
- login `mendel`, pwd `mendel`

- __How to find MAC addresses__: `ip link`
- Show connections: `nmcli connection show`
- Show ethernet address: `ip addr`

# Demo
- Show demo on device: `edgetpu_demo --device`
- Show demo vis a web server: `edgetpu_demo --stream`
- 
