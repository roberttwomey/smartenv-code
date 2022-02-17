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
- Show ethernet addresses: `ip addr`
  - show address for device: `ip addr show dev wlan0`

# Demo
- Show demo on device: `edgetpu_demo --device`
- Show demo vis a web server: `edgetpu_demo --stream`

# Camera
- https://coral.ai/docs/dev-board/camera/#connect-the-coral-camera

## whole-image classification: 
Rates what is in the image:
```
edgetpu_classify_server \
--model ${DEMO_FILES}/mobilenet_v2_1.0_224_quant_edgetpu.tflite \
--labels ${DEMO_FILES}/imagenet_labels.txt
```

## Face detection: 
```
edgetpu_detect \
--model ${DEMO_FILES}/ssd_mobilenet_v2_face_quant_postprocess_edgetpu.tflite
```

## additional camera examples:
https://github.com/google-coral/examples-camera
