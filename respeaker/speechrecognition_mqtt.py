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

# speech recognition  
r = sr.Recognizer()
m = sr.Microphone()

# mqtt
def on_publish(client, userdata, result):
    print("published: "+str(userdata))
    pass

def on_connect():
    print("connected...")
    pass

client1 = None

clientName = "smartenv"
broker_addr= "public.cloud.shiftr.io"
#broker_addr= "34.77.13.55"
broker_port = 443 # ignored, https not working right now
topic = "smartenv/speech"
mqtt_user = "public"
mqtt_password = "public"

client1 = paho.Client(clientName)
client1.on_connect = on_connect
# client1.on_publish = on_publish # doesn't seem to work
client1.username_pw_set(mqtt_user, password=mqtt_password)
print("connecting...", end="")
client1.connect(broker_addr)
print("done.")


try:
    print("A moment of silence, please...")
    with m as source: r.adjust_for_ambient_noise(source)
    print("Set minimum energy threshold to {}".format(r.energy_threshold))
    while True:
        print("Say something!")
        with m as source: audio = r.listen(source)
        print("Got it! Now to recognize it...")
        try:
            # recognize speech using Google Speech Recognition
            value = r.recognize_google(audio)

            # we need some special handling here to correctly print unicode characters to standard output
            if str is bytes:  # this version of Python uses bytes for strings (Python 2)
                print(u"You said {}".format(value).encode("utf-8"))
            else:  # this version of Python uses unicode for strings (Python 3+)
                print("You said {}".format(value))
                
                # publish to mqtt
                ret = client1.publish(topic, value)
                print("published {} to mqtt {}".format(topic, value)))
                
        except sr.UnknownValueError:
            print("Oops! Didn't catch that")
        except sr.RequestError as e:
            print("Uh oh! Couldn't request results from Google Speech Recognition service; {0}".format(e))
except KeyboardInterrupt:
    pass
