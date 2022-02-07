#!/usr/bin/python

# gist example
# https://gist.github.com/tomconte/eef8c9bfb4434787672c303153eee500

from time import gmtime, strftime, sleep, time
from bluepy.btle import Scanner, DefaultDelegate, BTLEException
import paho.mqtt.client as paho
import sys

valid_e8_addr = [
				"ac:23:3f:a2:2b:16",
				"ac:23:3f:a2:2b:0e",
				"ac:23:3f:a2:2b:0f",
				"ac:23:3f:a2:2b:11",
				"ac:23:3f:a2:2b:12",
				"ac:23:3f:ab:e7:49", # new E8s
				]

valid_s4_addr = [
				"ac:23:3f:aa:77:d2" # S4 door sensor
]

clientName = "smartenv"
broker_addr= "public.cloud.shiftr.io"
broker_port = 443
topic = "smartenv/"

# MQTT functions
def on_publish(client,userdata,result):
    print("published: "+userdata)
    pass

client1= paho.Client(clientName)
client1.on_publish = on_publish
client1.connect(broker_addr,broker_port)

# BLE functions
def toDecimal(word):
	integer = int(word[:2], 16)
	decimal = int(word[2:], 16)/256.0
	if integer >= 127:
		return (integer-256)+decimal
	return integer+decimal

def parse_accel(data, addr):
	addr_reversed = "".join(addr.split(":")[::-1])

	# check that we are getting a minew E-8 acceleration broadcast
	if data.startswith('e1ff') and data.endswith(addr_reversed):
		# print(data, addr_reversed)
		uuid = data[2:4]+data[0:2]
		frameType = data[4:6]
		productModel = data[6:8]
		batteryLevel = int(data[8:10], 16)
		accel_x = toDecimal(data[10:14])#float.fromhex(data[10:14])
		accel_y = toDecimal(data[14:18])#float.fromhex(data[10:14])
		accel_z = toDecimal(data[18:22])#float.fromhex(data[10:14])
		addr = "".join([data[22+i:22+i+2] for i in range(0, len(data[22:]), 2)][::-1])
		# print(uuid, frameType, productModel, batteryLevel, accel_x, accel_y, accel_z, addr)
		return (addr, accel_x, accel_y, accel_z, batteryLevel)

	return None

def parse_door(data, addr):
	addr_reversed = "".join(addr.split(":")[::-1])

	# check that we are getting a minew E-8 acceleration broadcast

	# example 3906a40164000101ffd277aa3f23ac3c52

	# if data.startswith('e1ff') and data.endsiwth(addr_reversed):
	if data.startswith('3906') and len(data)==34:
		# print(data, addr_reversed)
		uuid = data[2:4]+data[0:2]
		frameType = data[4:6]
		productModel = data[6:8]
		batteryLevel = int(data[8:10], 16)

		# door, button, and changed are all in data[10:16]
		door_state = int(data[11])
		button_state = int(data[13])
		state_changed = int(data[15])

		# address is data[18:30], in reversed pairs
		addr = "".join([data[18+i:18+i+2] for i in range(0, len(data[18:30]), 2)][::-1])
	
		tail = data[30:]
	
		# print(uuid, frameType, productModel, batteryLevel, door_state, button_state, state_changed, data[12:18], addr, tail)
		return (addr, door_state, button_state, state_changed, batteryLevel)

	return None

class ScanDelegate(DefaultDelegate):

	def handleDiscovery(self, dev, isNewDev, isNewData):
		# filtering by address

		# sensor tags
		if dev.addr in valid_e8_addr:
			# print(strftime("%Y-%m-%d %H:%M:%S", gmtime()), dev.addr, dev.getScanData())
			for (adtype, desc, value) in dev.getScanData():
				# print("  %s = %s" % (desc, value))
				# print(value)
				accel_data = parse_accel(value, dev.addr)
				if accel_data is not None:
					# addr, accel_x, accel_y, accel_z, battery = accel_data
					print("%s:\t%f\t%f\t%f\t%f\ttag" % accel_data)

					# publish to mqtt
					ret = client1.publish("smartenv/"+accel_data[0]," ".join(str(x) for x in accel_data[1:]))

				sys.stdout.flush()

		# door sensor
		if dev.addr in valid_s4_addr:
			# print(strftime("%Y-%m-%d %H:%M:%S", gmtime()), dev.addr, dev.getScanData())
			for (adtype, desc, value) in dev.getScanData():
				# print("  %s = %s" % (desc, value))

				# print(value)
				door_data = parse_door(value, dev.addr)
				if door_data is not None:
					addr, door_state, button_state, state_changed, batteryLevel = door_data
					print("%s:\t%d\t%d\t%d\t%f\tdoor" % door_data)

					# publish to mqtt
					ret= client1.publish("smartenv/"+door_data[0]," ".join(str(x) for x in door_data[1:]))

				sys.stdout.flush()

		# no filtering
		# print(strftime("%Y-%m-%d %H:%M:%S", gmtime()), dev.addr, dev.getScanData())
		# sys.stdout.flush()

def main():

	scanner = Scanner().withDelegate(ScanDelegate())

	# listen for ADV_IND packages for 10s, then exit
	# scanner.scan(10.0, passive=True)
	try:
		# scanner.start(passive=True)
		# lasttime = time()
		# scanner.process(1.0)
		while True:
			# do nothing
			# if(time()-lasttime > 1.0):
			scanner.scan(10.0, passive=True)

			# add thinking dot
			# print(".", end=" ")
			# sys.stdout.flush()

				# lasttime =time()
	except KeyboardInterrupt:
		scanner.stop()
	print("exiting...")


if __name__ == "__main__":
    main()


