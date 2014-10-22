import sys
import re
import math
from num2words import num2words
import time


WORDS = ["MAP"]
ONGOING_NAVIGATION = 0


def getInput(mic):

	def validateCommandMentioned(text, mic):

		#try to get a valid response in two rounds, else present menu again
		ctr = 3

		valid = False
		while(not valid and ctr > 0):

			if ctr != 3:
				text = mic.routeListen()

			if text == "":
				if ctr !=  1:
					mic.say("Pardon?")
				else:
					mic.say("Sorry, presenting the locations again")

				valid = False
				ctr -=1
				print ctr
				continue
			
			text.upper()
			commandMentioned = text.split(" ")

			print len(commandMentioned)
			
			if len(commandMentioned) > 1 :
				if ctr != 1:
					mic.say("I didn't quite get that? Please repeat the number or option")
				else:
					mic.say("Sorry, presenting the locations again")

				valid = False
				ctr-=1
				continue

			valid = True

		if ctr == 0:
			text = "INVALID"

		return text

		#check for validity in his command

	cancel = False
	valid = False
	chunkNumber = 1

	locations = getLocations()

	#TODO:get rid of this magic number!!!
	maxChunkSize = math.ceil(float(len(locations))/5)

	while(not (cancel or valid)):
		prompt(chunkNumber, maxChunkSize, locations, mic)
		command = validateCommandMentioned(mic.routeListen(), mic)
		chosenLocation = ""
		index = ""

		if command == "INVALID":
			continue

		if command == "CANCEL":
			cancel = True

		elif command == "MORE":
			if chunkNumber == maxChunkSize:
				mic.say("No more locations. Presenting menu again")
			else:
				chunkNumber+=1
			
		elif command == "PREVIOUS":
			if chunkNumber == 1:
				mic.say("No previous menu, say .... more.... for other locations. Presenting menu again")
			else:
				chunkNumber-=1
		else:
			#save location
			numInWords = {"ONE":1, "TWO":2, "THREE":3, "FOUR":4, "FIVE":5}

			#TODO: get some intelligence into this piece of code
			number = numInWords[command]
			print number

			#get index
			locationInChunk = chunkNumber * 5

			if (locationInChunk-5) + number-1 > len(locations)-1:
				mic.say("Invalid Choice, presenting menu again..")
			else:
				idxChosen = (locationInChunk-5) + number-1
				chosenLocation = locations[idxChosen]
				index = idxChosen
				valid = True
			
	return cancel, chosenLocation, index	



#called by jasper client
def handle(text, mic, profile, dispatcherClient):

	#make network request and get possible buildings and maps

	mic.say("")	





#called by jasper client
def isValid(text):
    return bool(re.search(r'\bfind|change\b', text, re.IGNORECASE)) # searches for to and from

