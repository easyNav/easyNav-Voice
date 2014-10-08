

def findValidLocations(text):
	class possibleLocations():
		noOfLocations = 0
		listofLoc = []
			
	text.upper()

	#get a list of locations
	filename = "../static/locations.txt"
	locationFile = open(filename, "r")
	print "Opened file!!"

	locations = []
	frequencyList = []

	for line in locationFile.readlines():
		line = line.replace("\n", "")
		locations.append(line)
		frequencyList.append(0)

	
	wordsInInput = text.split(" ")

	index=0

	for index,location in enumerate(locations):
    	#test if there is a match

		location = location.split(" ")
		for word in wordsInInput:
			if word in location:
				frequencyList[index] = frequencyList[index] + 1

	sizeOfInput = len(wordsInInput)

    #create a object
	obj = possibleLocations()

   	#check frequency table for matches
	for i,entry in enumerate(frequencyList):
		if entry == sizeOfInput:				#look for perfect matches
   			#save the location
			obj.noOfLocations = obj.noOfLocations + 1
			obj.listofLoc.append(locations[i])

	print obj.noOfLocations
	print obj.listofLoc

	if obj.noOfLocations == 1: #a perfect match is found
		print "Found unique location`"	
		return obj

	#reaching here imples no perfect location found
	i=0
	for i,entry in enumerate(frequencyList):
		if entry > sizeOfInput or (entry < sizeOfInput and entry != 0):
			obj.noOfLocations = obj.noOfLocations + 1
			obj.listofLoc.append(locations[i])


	print obj.noOfLocations
	print obj.listofLoc

	return obj

#open locations file
filename = "../static/locations.txt"
locationFile = open(filename, "r")
print "Opened file!!"

locations = []

for line in locationFile.readlines():
    line = line.replace("\n", "")
    locations.append(line)

#finding unique words and store it to words
words = []
unique = []

#getting unique words from list
for location in locations:
	unique = location.split(" ")
	for word in words:
		if word in unique:
			index =  words.index(word)
			words.pop(index) #pop out existing words

	words.extend(unique)

#print unique words

findValidLocations("ENTRANCE TOILET")
findValidLocations("MALE TOILET")
findValidLocations("FEMALE TOILET")






    


