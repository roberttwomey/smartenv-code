"""
    lights_mqtt.py

    Control pixel ring on ReSpeaker 6 Mic Array with mqtt comands from broker

    rtwomey@unl.edu | smart environments sp22 | roberttwomey.com

    setup: 
    pip install pixel_ring gpiozero

"""

import time

from pixel_ring import pixel_ring
from gpiozero import LED

# LED
power = LED(5)
power.on()

pixel_ring.set_brightness(10)

# mqtt
import paho.mqtt.client as mqtt

topic = "smartenv/audionode/"
clientName = "smartenv-pi"
serverAddress = "public.cloud.shiftr.io" # problems connecting? try <your server name>.local
mqttClient = mqtt.Client(clientName)
user = "public"
password = "public"

def connectionStatus(client, userdata, flags, rc):
    print("subscribing to {}...".format(topic), end="")
    mqttClient.subscribe(topic)
    print("subscribed")

def messageDecoder(client, userdata, msg):
    message = msg.payload.decode(encoding='UTF-8')
    
    # Feel free to remove the print, but confirmation in the terminal is nice.
    print("^^^ payload message = ", message)
    if message == "wake":
        pixel_ring.wakeup()
        time.sleep(3)
    elif message == "think":
        pixel_ring.think()
        time.sleep(3)
    elif message == "speak":
        pixel_ring.speak()
        time.sleep(6)
    elif message == "off":
        pixel_ring.off()
        time.sleep(3)
    elif message.startswith("color"):
        r, g, b = message.split(" ")[1:]
        pixel_ring.set_color(r=int(r), g=int(g), b=int(b))
    # respond to message, here. if/then to parse out various messages


# Set up calling functions to mqttClient
mqttClient.on_connect = connectionStatus
mqttClient.on_message = messageDecoder

# Connect to the MQTT server & loop forever.
# CTRL-C will stop the program from running.
# mqttClient.tls_set(ca_certs=None, certfile=None, keyfile=None, cert_reqs=ssl.CERT_REQUIRED,
#     tls_version=ssl.PROTOCOL_TLS, ciphers=None)
mqttClient.username_pw_set(user, password=password)
mqttClient.connect(serverAddress)
mqttClient.loop_forever()
