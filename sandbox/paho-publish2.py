import paho.mqtt.client as mqtt #import the client1

broker_address="public.cloud.shiftr.io" #use external broker
port = 443
user = "public"
password = "public"

client = mqtt.Client("P1") #create new instance
client.username_pw_set(user, password=password)#set username and password
client.connect(broker_address) #connect to broker

client.publish("smartenv/tag","on") #publish