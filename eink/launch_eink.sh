#!/bin/bash
sleep 5
cd /home/pi/smartenv-code/eink
/usr/bin/screen -dmS eink ./epaperMqtt.py
echo "...done"
