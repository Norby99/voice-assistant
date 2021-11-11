import speech_recognition as sr
import os.path
import json
import sys

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__)) # I must do in this way to use it both as a library and a separate program
sys.path.append(os.path.dirname(SCRIPT_DIR))
from libraries.features import *

class Vocal():

    def __init__(self, name, language, commands):
        self.commands = commands
        self.assistantName = name
        self.language = language

        self.r = sr.Recognizer()

    def listen(self):   # short example function
        with sr.Microphone() as source:
            self.r.adjust_for_ambient_noise(source)
            print("In ascolto...")
            audio = self.r.listen(source)
            try:
                text = self.r.recognize_google(audio, language="it-IT")
                if text.lower() == "ciao" or ((self.assistantName in text.lower() and "ciao" in text.lower())):     #saluto
                    return "Ciao"
                else:                                                                                  #non saluto
                    if self.assistantName.lower() not in text.lower():
                        
                        return text
                    else:
                        return "Si signore!", text
            except:
                return "Non ho capito!"

    def wakeUp(self):   # checks if patric is called
        with sr.Microphone() as source:
            self.r.adjust_for_ambient_noise(source)
            audio = self.r.listen(source)
            try:
                text = self.r.recognize_google(audio, language=self.language)
                if self.assistantName in text.lower():     #saluto
                    return True
            except:
                pass
        return False

    def Commands(self): # tries to listen for a command given in the json file
        with sr.Microphone() as source:
            self.r.adjust_for_ambient_noise(source)
            audio = self.r.listen(source)
            try:
                text = self.r.recognize_google(audio, language=self.language)

                for command in self.commands:
                    return command.recogniseInput(text.lower())
     
            except:
                return False

if __name__ == "__main__":
    with open(os.path.dirname(__file__) + "/../setup.json") as json_file:    # setting up the assistant
        jsonData = json.load(json_file)

    commands = []
    for key, value in list(jsonData.items())[2:]:
        feature = Feature([key, value])
        if feature.getStatus():
            commands.append(feature)

    audio = Vocal(jsonData["assistantName"].lower(), jsonData["language"], commands)
    print(audio.Commands())
