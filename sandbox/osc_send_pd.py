#! /usr/bin/python

""" 
  broadcasting from python to PD
   
  check what is using socket: 
    lsof -i :9000

  rtwomey@unl.edu 2022

  use https://pypi.org/project/python-osc/

"""

# from https://stackoverflow.com/questions/64066634/sending-broadcast-in-python

# http://pd-tutorial.com/english/ch04s04.html


from pythonosc.udp_client import SimpleUDPClient
import time

ip = "127.0.0.1"
port = 3000

client = SimpleUDPClient(ip, port)  # Create client

# client.send_message("/some/address", 123)   # Send float message
# client.send_message("/some/address", [1, 2., "hello"])  # Send message with int, float and string

# client.send_message("/", [1, 2, 3, 4, 5])

count = 1
while True:
    client.send_message("/", float(count))
    time.sleep(1)
    count+=1
    if count>5:
        count=0

# client.send_message("/", [1, 2., "hello"])  # Send message with int, float and string