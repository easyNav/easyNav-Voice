import sys
import re
import math
from num2words import num2words
import time
import requests
import json

from easyNav_pi_dispatcher import DispatcherClient


class testNavInstructions(object):
    
    def __init__(self):
        #interprocess
        self.apple=2
        self.endpoint="http://192.249.57.162:1337/"
        #interprocess 
        self.DISPATCHER_PORT = 9002
        self.dispatcherClient = DispatcherClient(port=self.DISPATCHER_PORT)


    def start(self):
		self.dispatcherClient.start()
		self.dispatcherClient.send(9001, "newPath", {"from":1, "to": 6})    	#lt15 to P2

		# ctr=90
		# for c in range(0,17)
		# 	ctr-=5
		# 	payload = { "x": 0, "y": 2558, "z": 0, "orientation": (ctr/180.0)*3.142}
		# 	r = requests.post(self.endpoint + "heartbeat/location", data=payload)
		# 	time.sleep(5)
		# 	print payload
		
		payload = { "x": 0, "y": 2436, "z": 0, "orientation": (0/180.0)*3.142 }
		print payload
		r = requests.post(self.endpoint + "heartbeat/location", data=payload)
		time.sleep(3)

		#simulate orientation
		ctr=0
		for c in range(0,8):
			ctr+=10

			if(ctr > 90):
				payload = { "x": 0, "y": 2436, "z": 0, "orientation": (90/180.0)*3.142}
				r = requests.post(self.endpoint + "heartbeat/location", data=payload)
				time.sleep(3)
				print payload
				break
			else:
				payload = { "x": 0, "y": 2436, "z": 0, "orientation": (ctr/180.0)*3.142 }
				r = requests.post(self.endpoint + "heartbeat/location", data=payload)
				time.sleep(3)
				print payload


		# payload = { "x": 0, "y": 2558, "z": 0, "orientation": (0/180.0)*3.142 }
		# r = requests.post(self.endpoint + "heartbeat/location", data=payload)
		# time.sleep(5)
		# ctr=0
		# print payload

		# payload = { "x": 50, "y": 2580, "z": 0, "orientation": (0/180.0)*3.142 }
		# print payload
		# r = requests.post(self.endpoint + "heartbeat/location", data=payload)
		# print r.json
		# time.sleep(5)


        #simulate movement
		ctr=0
		for c in range(0,29):
			ctr+=100
			payload = { "x": ctr, "y": 2436, "z": 0, "orientation": (90/180.0)*3.142 }
			print payload
			r = requests.post(self.endpoint + "heartbeat/location", data=payload)
			print r.json
			time.sleep(3)
			print payload

			if ctr == 2800:
				ctr+=83
				payload = { "x": ctr, "y": 2436, "z": 0, "orientation": (90/180.0)*3.142 }
				print payload
				r = requests.post(self.endpoint + "heartbeat/location", data=payload)
				print r.json
				time.sleep(3)
				print payload
				break
		ctr=90
		for c in range(0,9):
			ctr-=10

			if(ctr < 0):
				payload = {"x": 2883, "y": 2436, "z": 0, "orientation": (0/180.0)*3.142}
				r = requests.post(self.endpoint + "heartbeat/location", data=payload)
				time.sleep(3)
				print payload
				break
			else:
				payload = {"x": 2883, "y": 2436, "z": 0, "orientation": (ctr/180.0)*3.142 }
				r = requests.post(self.endpoint + "heartbeat/location", data=payload)
				time.sleep(3)
				print payload

		ctr=2436
		for c in range(0,9):
			ctr+=100

			payload = {"x": 2883, "y": ctr, "z": 0, "orientation": (0/180.0)*3.142 }
			r = requests.post(self.endpoint + "heartbeat/location", data=payload)
			time.sleep(3)
			print payload

			if(ctr == 2836):
				payload = {"x": 2883, "y": 2924, "z": 0, "orientation": (0/180.0)*3.142}
				r = requests.post(self.endpoint + "heartbeat/location", data=payload)
				time.sleep(3)
				print payload
				break
		
				

		
		# payload = { "x": 1420, "y": 1260, "z": 0, "orientation": (270/180.0)*3.142 }
		# print payload
		# r = requests.post(self.endpoint + "heartbeat/location", data=payload)
		# print r.json
		# time.sleep(5)

		# ctr=270
		# for c in range(0,7):
		# 	ctr+=10
		# 	payload = {"x": 1420, "y": 1260, "z": 0, "orientation": (ctr/180.0)*3.142 }
		# 	print payload
		# 	r = requests.post(self.endpoint + "heartbeat/location", data=payload)
		# 	print r.json
		# 	time.sleep(5)

		# ctr+=10
		# payload = {"x": 1420, "y": 1260, "z": 0, "orientation": (0/180.0)*3.142 }
		# print payload
		# r = requests.post(self.endpoint + "heartbeat/location", data=payload)
		# print r.json
		# time.sleep(5)


		# ctr=0
		# for c in range(0,17):
		# 	payload = {"x": 1420, "y": 1260, "z": 0, "orientation": (ctr/180.0)*3.142 }
		# 	print payload
		# 	r = requests.post(self.endpoint + "heartbeat/location", data=payload)
		# 	print r.json
		# 	time.sleep(5)


		
		# ctr=1160
		# for c in range(0,2):
		# 	ctr+=100
		# 	payload = { "x": 1420, "y": ctr, "z": 0, "orientation": (180/180.0)*3.142 }
		# 	print payload
		# 	r = requests.post(self.endpoint + "heartbeat/location", data=payload)
		# 	print r.json
		# 	time.sleep(5)
			
		# 	if ctr == 1360:
		# 		payload = { "x": 1420, "y": 1440, "z": 0, "orientation": (180/180.0)*3.142 }
		# 		print payload
		# 		r = requests.post(self.endpoint + "heartbeat/location", data=payload)
  #       		print r.json
  #       		time.sleep(5)
  #       		break

def runMain():

	TestNavInstructions = testNavInstructions()
 	TestNavInstructions.start()

if __name__ == '__main__':
	runMain()








