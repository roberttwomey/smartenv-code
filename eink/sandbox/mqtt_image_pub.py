import paho.mqtt.publish as publish

path = "angry_raccoon.jpg"

with open(path, 'rb') as f:
    filecontent = f.read()

    byteArr = bytearray(filecontent)
    mqtt_auth = { 'username': "public", 'password': "public" }
    publish.single('/smartenv/eink/image', byteArr, hostname='public.cloud.shiftr.io', auth=mqtt_auth)
    # publish.single('topic', byteArr, qos=1, hostname='m2m.eclipse.org')
