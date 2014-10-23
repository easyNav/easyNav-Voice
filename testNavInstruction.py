import sys
import re
import math
from num2words import num2words
import time
import requests
import json


class testNavInstructions(object):
    
    def __init__(self):
        #interprocess
        self.apple=2
        self.endpoint="http://localhost:1337/"

    def start(self):
    	#lt15 to seminar room 6
		payload = { "x": 0, "y": 1260, "z": 0, "orientation": (0/180.0)*3.142 }
		r = requests.post(self.endpoint + "heartbeat/location", data=payload)
		time.sleep(5)


		payload = { "x": 0, "y": 1260, "z": 0, "orientation": (270/180.0)*3.142 }
		r = requests.post(self.endpoint + "heartbeat/location", data=payload)
		time.sleep(5)
		ctr=0
        
        #simulate movement
		for c in range(0,10):
			ctr+=200
			payload = { "x": ctr, "y": 1260, "z": 0, "orientation": (270/180.0)*3.142 }
			print payload
			r = requests.post(self.endpoint + "heartbeat/location", data=payload)
			print r.json
			time.sleep(5)


			if ctr == 1400:
				ctr+=100
				payload = { "x": ctr, "y": 1260, "z": 0, "orientation": (270/180.0)*3.142 }
				print payload
				r = requests.post(self.endpoint + "heartbeat/location", data=payload)
				print r.json
				time.sleep(5)
				break


		payload = { "x": 1420, "y": 1260, "z": 0, "orientation": (270/180.0)*3.142 }
		print payload
		r = requests.post(self.endpoint + "heartbeat/location", data=payload)
		print r.json
		time.sleep(5)

		ctr=270
		for c in range(0,7):
			ctr+=10
			payload = {"x": 1420, "y": 1260, "z": 0, "orientation": (ctr/180.0)*3.142 }
			print payload
			r = requests.post(self.endpoint + "heartbeat/location", data=payload)
			print r.json
			time.sleep(5)

		ctr+=10
		payload = {"x": 1420, "y": 1260, "z": 0, "orientation": (0/180.0)*3.142 }
		print payload
		r = requests.post(self.endpoint + "heartbeat/location", data=payload)
		print r.json
		time.sleep(5)


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








