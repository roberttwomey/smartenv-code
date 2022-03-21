#!/usr/bin/python
# speechrecognition_mqtt.py
#
# listens for audio on a respeaker 6 mic array, and uses google speech recognition to retrieve text
#
# example for UNL Smart Environments sp2022 | rtwomey@unl.edu | roberttwomey.com
#
# Based on this example from the Uberi SpeechRecognition package:
# from https://github.com/Uberi/speech_recognition/blob/master/speech_recognition/__main__.py
# Plus some mqtt magic

import speech_recognition as sr
import paho.mqtt.client as paho
from datetime import datetime
from uuid import getnode as get_mac
import json

import time
from pixel_ring import pixel_ring
from gpiozero import LED
import socket

# myhostname = socket.gethostname()

clientName = "smartenv4-pi"
publishTopic = "/smartenv/respeaker4/speech"
subscribeTopic = "/smartenv/respeaker4/lights"
bDoListen = True

# -------- mqtt helpers --------
def on_publish(client, userdata, result):
    print("published: "+str(userdata))
    pass

def connectionStatus(client, userdata, flags, rc):
    print("subscribing to {}...".format(subscribeTopic), end="")
    mqttClient.subscribe(subscribeTopic)
    print("subscribed")

# -------- message helpers --------

def create_json(text):
    this_time = datetime.now()
    timestamp = this_time.isoformat()+"Z"
    msg = {
        "timestamp": timestamp,
        #"type": "speech",
        #"mac": my_mac,
        "text": text
    } 
    return "["+json.dumps(msg)+"]"
    #return json.dumps(msg)
      
def messageDecoder(client, userdata, msg):
    global bDoListen
    message = msg.payload.decode(encoding='UTF-8')
    
    # Feel free to remove the print, but confirmation in the terminal is nice.
    print("received: ", message)
    if message == "wake":
        pixel_ring.wakeup()
        time.sleep(0.1)
    elif message == "listen":
        pixel_ring.listen()
        time.sleep(0.1)
        bDoListen = True
    elif message == "think":
        pixel_ring.think()
        time.sleep(0.1)
    elif message == "speak":
        pixel_ring.speak()
        time.sleep(0.1)
    elif message == "off":
        pixel_ring.off()
        time.sleep(0.1)
    elif message == "mute":
        pixel_ring.set_color(r=0, g=0, b=128)
        bDoListen = False
    elif message == "echo":
        pixel_ring.change_pattern('echo')
        time.sleep(0.1)
    elif message == 'google':
        pixel_ring.change_pattern('google')
        time.sleep(0.1)
    elif message == 'smartenv':
        pixel_ring.change_pattern('smartenv')
        time.sleep(0.1)
    elif message.startswith("color"):
        r, g, b = message.split(" ")[1:]
        pixel_ring.set_color(r=int(r), g=int(g), b=int(b))

    # respond to message, here. if/then to parse out various messages

# -------- initialize MQTT --------
    
mqttClient = None
broker_addr= "public.cloud.shiftr.io"
#broker_addr= "34.77.13.55"
#broker_port = 443 # ignored, https not working right now
mqtt_user = "public"
mqtt_password = "public"

mqttClient = paho.Client(clientName)
mqttClient.on_connect = connectionStatus
mqttClient.on_message = messageDecoder

# client1.on_publish = on_publish # doesn't seem to work
mqttClient.username_pw_set(mqtt_user, password=mqtt_password)
print("connecting...", end="")
mqttClient.connect(broker_addr)
print("done.")
mqttClient.loop_start()

# -------- globals ---------
# mac address
mac = get_mac()
my_mac = hex(mac).upper()[2:]
print("my mac is:" + my_mac)

# -------- start leds --------
pixel_ring.set_brightness(10)
pixel_ring.change_pattern("smartenv")
pixel_ring.wakeup()

# time.sleep(5)

# -------- start audio --------
# speech recognition  
r = sr.Recognizer()
m = sr.Microphone()

# -------- main program ---------
try:
    # turn on LEDs
    power = LED(5)
    power.on()
    pixel_ring.set_brightness(10)
    pixel_ring.change_pattern("smartenv")
    
    print("A moment of silence, please...")
    with m as source: r.adjust_for_ambient_noise(source)
    print("Set minimum energy threshold to {}".format(r.energy_threshold))
    while True:
        # print("listening.", end=" ")
        
        if bDoListen == True:

            # listening
            pixel_ring.listen()
            # pixel_ring.set_color(r=255, g=0, b=0)
            # time.sleep(0.1)

            with m as source: audio = r.listen(source)
            if bDoListen == False:
                continue

            # thinking
            pixel_ring.think()
            # pixel_ring.set_color(r=255, g=0, b=128)
            # time.sleep(0.1)

            if bDoListen == False:
                continue

            try:
                # recognize speech using Google Speech Recognition
                value = r.recognize_google(audio)

                # we need some special handling here to correctly print unicode characters to standard output
                if str is bytes:  # this version of Python uses bytes for strings (Python 2)
                    print(u"heard: {}".format(value).encode("utf-8"))
                else:  # this version of Python uses unicode for strings (Python 3+)
                    print("heard: {}".format(value))
                    message = create_json(value)

                    # publish to mqtt
                    ret = mqttClient.publish(publishTopic, message)
                    print("published to {}: {}".format(publishTopic, message))
                    pixel_ring.set_color(r=255, g=0, b=0) # flash red
                    time.sleep(0.25)

            except sr.UnknownValueError:
                print("no results.")
            except sr.RequestError as e:
                print("Couldn't request results from Google Speech Recognition service; {0}".format(e))
        else:
            time.sleep(0.1)
except KeyboardInterrupt:
    print("exiting")
    pixel_ring.off()
    time.sleep(3)
    pass
