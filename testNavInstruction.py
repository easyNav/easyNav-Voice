import sys
import re
import math
from num2words import num2words
import time


from easyNav_pi_dispatcher import DispatcherClient
import json



class testNavInstructions(object):
    
    def __init__(self):
        #interprocess
        self.DISPATCHER_PORT = 9002
        self.dispatcherClient = DispatcherClient(port=self.DISPATCHER_PORT)

        ## Attach event listeners
        self.attachEvents(self.speaker)


    def start(self):
    	#lt15 to seminar room 6
		self.dispatcherClient.send(9001, "newPath", {"from":1, "to": 28})

		payload = { "x": 0, "y": 1260, "z": 0, "orientation": 90*3.142 }
		r = requests.post(self.endpoint + "heartbeat/location", data=payload)
		ctr=0
        
        #simulate movement
		for c in range(0,20):
			ctr+=100
			payload = { "x": ctr, "y": 1260, "z": 0, "orientation": 90*3.142 }
			r = requests.post(self.endpoint + "heartbeat/location", data=payload)
			print r.json
			time.sleep(1)


			if ctr == 1400:
				ctr+=20
				payload = { "x": ctr, "y": 1260, "z": 0, "orientation": 90*3.142 }
				r = requests.post(self.endpoint + "heartbeat/location", data=payload)
				print r.json
				break


		ctr=90
		for c in range(0,9):
			ctr-=10
			payload = { "x": ctr, "y": 1260, "z": 0, "orientation": ctr*3.142 }
			r = requests.post(self.endpoint + "heartbeat/location", data=payload)
			print r.json
			time.sleep(1)
		
		ctr=1260
		for c in range(0,2):
			ctr+=100
			payload = { "x": 1420, "y": ctr, "z": 0, "orientation": 90*3.142 }
			r = requests.post(self.endpoint + "heartbeat/location", data=payload)
			print r.json
			time.sleep(1)
			
			if ctr == 1360:
				payload = { "x": 1420, "y": 1440, "z": 0, "orientation": 90*3.142 }
				r = requests.post(self.endpoint + "heartbeat/location", data=payload)
        		print r.json
        		time.sleep(1)
        		break
    def attachEvents(self, mic):
		## clear all signals
		smokesignal.clear()
		text = ""
		@smokesignal.on('say')
		def onSay(args):
			print "Info from Nav"
			infoFromNav = eval(args.get('payload'))
			print infoFromNav
			infotosay = infoFromNav["text"]
			print infotosay
			print "Info from Nav before Mic"
			mic.say(infotosay)


def runMain():

	TestNavInstructions = testNavInstructions()
 	TestNavInstructions.start()

if __name__ == '__main__':
	runMain()








