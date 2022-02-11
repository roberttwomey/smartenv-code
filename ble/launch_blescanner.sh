#!/bin/bash
sleep 5
cd /home/pi/smartenv-code/ble/
/usr/bin/screen -dmS blescanner sudo /usr/bin/python3 /home/pi/smartenv-code/ble/ble_to_mqtt.py
