#!/bin/bash
sleep 5
cd /home/pi/smartenv-code/respeaker
/usr/bin/screen -dmS respeaker ./respeaker_service.py
echo "...done"