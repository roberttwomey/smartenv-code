#!/usr/bin/python
# -*- coding:utf-8 -*-
import sys
import os

picdir = os.path.realpath('./pic/')
# libdir = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), 'lib')

# if os.path.exists(libdir):
    # sys.path.append(libdir)

import logging
from waveshare_epd import epd5in83_V2
import time
from PIL import Image,ImageDraw,ImageFont
import traceback
import textwrap


# -------- mqtt stuff -------- #
import paho.mqtt.client as mqtt
import json

topic = "smartenv/eink2/image"
clientName = "eink2"
serverAddress = "public.cloud.shiftr.io" # problems connecting? try <your server name>.local
mqttClient = mqtt.Client(clientName)
user = "public"
password = "public"

def connectionStatus(client, userdata, flags, rc):
    print("subscribing to {}...".format(topic), end="")
    mqttClient.subscribe(topic)
    print("subscribed")

def is_json(myjson):
    try:
        json_object = json.loads(myjson)
    except ValueError as e:
        return False
    return True

def messageDecoder(client, userdata, msg):
    message = msg.payload.decode(encoding='UTF-8')
    
    # Feel free to remove the print, but confirmation in the terminal is nice.
    print("received: ", message)

    text = ""
    # print("clear eink")
    if is_json(message):
        text = json.loads(message)[0]["image"]
        # print(text)
    else: 
        text = message

    logging.info("displaying payload message = ", text)

    # load image from message filename
    # Himage = Image.new('1', (epd.width, epd.height), 255)  # 255: clear the frame
    # draw = ImageDraw.Draw(Himage)

    # margin = 10
    # offset = 20
    # #draw.text((margin, 0), "received: ", font = font24, fill = 0)
    # for line in textwrap.wrap(text, width=28):
    #     draw.text((margin, offset), line, font=font48, fill=0)
    #     offset += font48.getsize(line)[1]

    Himage = Image.open(text)
    epd.display(epd.getbuffer(Himage))
    Himage.save("image.jpg")

    # time.sleep(2)
    print("display message")


# Set up calling functions to mqttClient
mqttClient.on_connect = connectionStatus
mqttClient.on_message = messageDecoder

# Connect to the MQTT server & loop forever.
# CTRL-C will stop the program from running.
# mqttClient.tls_set(ca_certs=None, certfile=None, keyfile=None, cert_reqs=ssl.CERT_REQUIRED,
#     tls_version=ssl.PROTOCOL_TLS, ciphers=None)
mqttClient.username_pw_set(user, password=password)
mqttClient.connect(serverAddress)

# -------- e paper stuff -------- #
font48 = ImageFont.truetype(os.path.join(picdir, 'Font.ttc'), 48)
font24 = ImageFont.truetype(os.path.join(picdir, 'Font.ttc'), 24)
font18 = ImageFont.truetype(os.path.join(picdir, 'Font.ttc'), 18)



epd = epd5in83_V2.EPD()
logging.info("init and Clear")
epd.init()
# epd.Clear()



try: 
    # e-ink hello world
    logging.info("1.Drawing on the Horizontal image...")
    Himage = Image.new('1', (epd.width, epd.height), 255)  # 255: clear the frame
    draw = ImageDraw.Draw(Himage)
    draw.text((10, 0), 'hello world', font = font24, fill = 0)
    draw.text((10, 20), '5.83inch e-Paper', font = font24, fill = 0)
    draw.text((150, 0), u'微雪电子', font = font24, fill = 0)    
    draw.text((0, 100), 'smartenv.roberttwomey.com', font = font48, fill = 0)
    draw.text((0, 150), topic, font = font48, fill = 0)
    draw.line((20, 50, 70, 100), fill = 0)
    draw.line((70, 50, 20, 100), fill = 0)
    draw.rectangle((20, 50, 70, 100), outline = 0)
    draw.line((165, 50, 165, 100), fill = 0)
    draw.line((140, 75, 190, 75), fill = 0)
    draw.arc((140, 50, 190, 100), 0, 360, fill = 0)
    draw.rectangle((80, 50, 130, 100), fill = 0)
    draw.chord((200, 50, 250, 100), 0, 360, fill = 0)
    epd.display(epd.getbuffer(Himage))
    # time.sleep(2)

    Himage.save("image.jpg")

    mqttClient.loop_forever()



except IOError as e:
    logging.info(e)
    
except KeyboardInterrupt:    
    logging.info("ctrl + c:")
    epd5in83_V2.epdconfig.module_exit()
    exit()


# # -------- main program -------- #
# logging.basicConfig(level=logging.DEBUG)

# try:
#     logging.info("epd5in83_V2 Demo")
    
#     epd = epd5in83_V2.EPD()
#     logging.info("init and Clear")
#     epd.init()
#     # epd.Clear()
    
#     font24 = ImageFont.truetype(os.path.join(picdir, 'Font.ttc'), 24)
#     font18 = ImageFont.truetype(os.path.join(picdir, 'Font.ttc'), 18)
    
#     # Drawing on the Horizontal image
#     logging.info("1.Drawing on the Horizontal image...")
#     Himage = Image.new('1', (epd.width, epd.height), 255)  # 255: clear the frame
#     draw = ImageDraw.Draw(Himage)
#     draw.text((10, 0), 'hello world', font = font24, fill = 0)
#     draw.text((10, 20), '5.83inch e-Paper', font = font24, fill = 0)
#     draw.text((150, 0), u'微雪电子', font = font24, fill = 0)    
#     draw.line((20, 50, 70, 100), fill = 0)
#     draw.line((70, 50, 20, 100), fill = 0)
#     draw.rectangle((20, 50, 70, 100), outline = 0)
#     draw.line((165, 50, 165, 100), fill = 0)
#     draw.line((140, 75, 190, 75), fill = 0)
#     draw.arc((140, 50, 190, 100), 0, 360, fill = 0)
#     draw.rectangle((80, 50, 130, 100), fill = 0)
#     draw.chord((200, 50, 250, 100), 0, 360, fill = 0)
#     epd.display(epd.getbuffer(Himage))
#     time.sleep(2)
    
#     # Drawing on the Vertical image
#     logging.info("2.Drawing on the Vertical image...")
#     Limage = Image.new('1', (epd.height, epd.width), 255)  # 255: clear the frame
#     draw = ImageDraw.Draw(Limage)
#     draw.text((2, 0), 'hello world', font = font18, fill = 0)
#     draw.text((2, 20), '5.83inch epd', font = font18, fill = 0)
#     draw.text((20, 50), u'微雪电子', font = font18, fill = 0)
#     draw.line((10, 90, 60, 140), fill = 0)
#     draw.line((60, 90, 10, 140), fill = 0)
#     draw.rectangle((10, 90, 60, 140), outline = 0)
#     draw.line((95, 90, 95, 140), fill = 0)
#     draw.line((70, 115, 120, 115), fill = 0)
#     draw.arc((70, 90, 120, 140), 0, 360, fill = 0)
#     draw.rectangle((10, 150, 60, 200), fill = 0)
#     draw.chord((70, 150, 120, 200), 0, 360, fill = 0)
#     epd.display(epd.getbuffer(Limage))
#     time.sleep(2)
    
#     logging.info("3.read bmp file")
#     Himage = Image.open(os.path.join(picdir, '5in83_V2.bmp'))
#     epd.display(epd.getbuffer(Himage))
#     time.sleep(2)
    
#     logging.info("4.read bmp file on window")
#     Himage2 = Image.new('1', (epd.height, epd.width), 255)  # 255: clear the frame
#     bmp = Image.open(os.path.join(picdir, '100x100.bmp'))
#     Himage2.paste(bmp, (50,10))
#     epd.display(epd.getbuffer(Himage2))
#     time.sleep(2)

#     logging.info("Clear...")
#     epd.Clear()
    
#     logging.info("Goto Sleep...")
#     epd.sleep()
    
# except IOError as e:
#     logging.info(e)
    
# except KeyboardInterrupt:    
#     logging.info("ctrl + c:")
#     epd5in83_V2.epdconfig.module_exit()
#     exit()
