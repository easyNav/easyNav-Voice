

import re

WORDS = ["HELP"]

"""
help, find, route, end, time

"""

#called by jasper client
def handle(text, mic, profile):
    mic.say("Hi...i'm EasyNav.....your friendly navigation assistant....")
    mic.say("To invoke me, please say my Name......and i will beep....then proceed with your command....")
    mic.say("To navigate to a location, please use the...find....command")
    mic.say("During your journey to a destination, to change destination, please use the....change....command")
    mic.say("To find the time now, please use the....time.....command")
    mic. say("To end your Session with EasyNav, please use the....end...command")

#called by jasper client
def isValid(text):
    return bool(re.search(r'\bhelp\b', text, re.IGNORECASE))


#used doctest
if __name__ == "__main__":
    import doctest
    #doctest.testmod()

