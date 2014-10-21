#!/usr/bin/env python2
import os
import sys
import traceback
import shutil
import yaml

from client.diagnose import Diagnostics
from client import vocabcompiler, stt
from client import speaker 
from client.conversation import Conversation
from client.mic import Mic
from client import GetLocations

#for interprocess communication
import smokesignal
from easyNav_pi_dispatcher import DispatcherClient
import json


class Voice(object):

    def __init__(self): 
        # Set $JASPER_HOME
        if not os.getenv('VOICE'):
            os.environ["VOICE"]  = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))

        # # for testing
        # if len(sys.argv) > 1 and "--local" in sys.argv[1:]:
        #     from client.local_mic import Mic
        # else:
        #     from client.mic import Mic

        # Change CWD to $JASPER_HOME/jasper/client
        client_path = os.path.join(os.getenv("VOICE"), "easyNav-Voice", "client")
        os.chdir(client_path)
        # Add $JASPER_HOME/jasper/client to sys.path
        sys.path.append(client_path)

        self.speaker = speaker.newSpeaker()

        #interprocess 
        self.DISPATCHER_PORT = 9002
        self.dispatcherClient = DispatcherClient(port=self.DISPATCHER_PORT)

        ## Attach event listeners
        # self.attachEvents(self.speaker)

    def start(self):

        def testConnection():
            if Diagnostics.check_network_connection():
                print "CONNECTED TO INTERNET"
            else:
                print "COULD NOT CONNECT TO NETWORK"
                self.speaker.say(
                    "Warning: I was unable to connect to a network. Parts of the system may not work correctly, depending on your setup.")


        def fail(message):
            traceback.print_exc()
            self.speaker.say(message)
            sys.exit(1)


        def configure():
            try:
                print "COMPILING DICTIONARY FOR MODULES"
                vocabcompiler.compile(
                    "sentences.txt", "dictionary.dic", "languagemodel.lm")

                print "COMPILING DICTIONARY OF LOCATIONS OPTIONS"
                vocabcompiler.compileLocations(
                    "sentences_locations.txt", "dictionary_locations.dic", "languagemodel_locations.lm");

                print "STARTING CLIENT PROGRAM"

            except OSError:
                print "BOOT FAILURE: OSERROR"
                fail(
                    "There was a problem starting EasyNav. You may be missing the language model and associated files. Please read the documentation to configure your Raspberry Pi.")

            except IOError:
                print "BOOT FAILURE: IOERROR"
                fail(
                    "There was a problem starting EasyNav. You may have set permissions incorrectly on some part of the filesystem. Please read the documentation to configure your Raspberry Pi.")

            except:
                print "BOOT FAILURE"
                fail(
                    "There was a problem starting EasyNav.")

        old_client = os.path.abspath(os.path.join(os.pardir, "old_client"))
        if os.path.exists(old_client):
            shutil.rmtree(old_client)


        print "==========================================================="
        print " JASPER The Talking Computer                               "
        print " Copyright 2013 Shubhro Saha & Charlie Marsh               "
        print "==========================================================="

        self.speaker.say("Hello.... I am EASYNAV... Please wait one moment while I configure.")

        configure()
        
        profile = yaml.safe_load(open("profile.yml", "r"))

        try:
            api_key = profile['keys']['GOOGLE_SPEECH']
        except KeyError:
            api_key = None

        try:
            stt_engine_type = profile['stt_engine']
        except KeyError:
            print "stt_engine not specified in profile, defaulting to PocketSphinx"
            stt_engine_type = "sphinx"

        mic = Mic(self.speaker, stt.PocketSphinxSTT(),
                  stt.newSTTEngine(stt_engine_type, api_key=api_key))

        mic.say("Hi...i'm EasyNav.....your friendly navigation assistant....")
        mic.say("To invoke me, please say my Name......and i will beep....then proceed with your command")
        mic.say("To find out about commands...please say help......")

        self.dispatcherClient.start()

        #GetLocations.getLoc()
        conversation = Conversation("EASYNAV", mic, profile, self.dispatcherClient)
        conversation.handleForever()
        

    # def attachEvents(self, mic):
    #     ## clear all signals
    #     smokesignal.clear()
    #     text = ""
    #     @smokesignal.on('say')
    #     def onSay(args):
    #         print "Info from Nav"
    #         infoFromNav = eval(args.get('payload'))
    #         print infoFromNav
    #         infotosay = infoFromNav["text"]
    #         print infotosay
    #         print "Info from Nav before Mic"
    #         mic.say(infotosay)


def runMain():

    voice = Voice()
    voice.start()

if __name__ == '__main__':
    runMain()


