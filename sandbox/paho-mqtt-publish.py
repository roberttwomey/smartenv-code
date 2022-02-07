'''
    quick MQTT test to publish messages from rpi to shiftr public cloud
    view the shiftr public cloud here: https://www.shiftr.io/try/

    rtwomey@unl.edu 2022

    adapted from this: https://techtutorialsx.com/2017/04/14/python-publishing-messages-to-mqtt-topic/
'''

import paho.mqtt.client as mqttClient
import time
import certifi
 
def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Connected to broker")
        global Connected                #Use global variable
        Connected = True                #Signal connection 
    else: 
        print("Connection failed")
 
Connected = False   #global variable for the state of the connection
 
broker_address= "public.cloud.shiftr.io"
broker_port = 443
user = "public"
password = "public"
client_name = "smartenv-py-client" 

client = mqttClient.Client(client_name)               #create new instance

client.on_connect= on_connect                      #attach function to callback

print("trying to connect")
client.username_pw_set(user, password=password)    #set username and password
client.connect(broker_address)          #connect to broker
client.loop_start()        #start the loop
 
while Connected != True:    #Wait for connection
    time.sleep(0.1)
 
try:
    while True:
        value = input('Enter the message:')
        client.publish("smartenv/test",value)
except KeyboardInterrupt:
    client.disconnect()
    client.loop_stop()