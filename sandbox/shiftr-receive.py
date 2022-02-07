# receiveKindess.py
# once running, you can test with the shell commands:
# To start the robot:
# mosquitto_pub -h talkpi.local -t "talkpi/talk" -m "yes.mp3"
# from https://gist.github.com/gallaugher/849b5cda73004389ebdea38251ccd66d

import paho.mqtt.client as mqtt
import time
import ssl

clientName = "smartenv-test"
serverAddress = "public.cloud.shiftr.io" # problems connecting? try <your server name>.local
mqttClient = mqtt.Client(clientName)
user = "public"
password = "public"

def connectionStatus(client, userdata, flags, rc):
    print("subscribing")
    mqttClient.subscribe("smartenv/*")
    print("subscribed")

def messageDecoder(client, userdata, msg):
    message = msg.payload.decode(encoding='UTF-8')
    # Feel free to remove the print, but confirmation in the terminal is nice.
    print("^^^ payload message = ", message)
    # respond to message, here. if/then to parse out various messages
    time.sleep(1.0) # wait 4 seconds between plays.

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