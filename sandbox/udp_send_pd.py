#! /usr/bin/python

""" 
  UDP send from python to PD
   
  check what is using socket: 
    lsof -i :3000

  rtwomey@unl.edu 2022

  use https://pypi.org/project/python-osc/

"""

# from https://stackoverflow.com/questions/64066634/sending-broadcast-in-python

# http://pd-tutorial.com/english/ch04s04.html


import time, socket

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

ip = "127.0.0.1"
port = 3000

sock.connect((ip, port))

count = 1
while True:
    
    tsr = str(count)
    tsr+=";"
    bytes_data =  tsr.encode('utf-8')
    print(tsr, bytes_data)
    
    # bytes_data = count.to_bytes(1, byteorder='big')
    # print(count, bytes_data)

    # sock.sendto(bytes_data, (ip, port))  # send UDP packet
    sock.send(bytes_data)

    time.sleep(1)
    count+=1
    if count>5:
        count=1

# client.send_message("/", [1, 2., "hello"])  # Send message with int, float and string