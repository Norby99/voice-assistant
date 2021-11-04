import speech_recognition as sr
import os.path
import json

class Vocal():

    def __init__(self):
        with open(os.path.dirname(__file__) + "/../setup.json") as json_file:    # setting up the assistant
            jsonData = json.load(json_file)

        self.assistantName = jsonData["assistantName"].lower()
        self.language = jsonData["language"]

        self.commands = []
        for key, value in list(jsonData.items())[2:]:
            if value["enabled"]:
                self.commands.append({key : value})

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

                for items in self.commands:
                    for value in items.values():
                        for subValue in list(value.values())[1:]:
                            if any(x in text.lower() for x in subValue[:-1]):
                                return subValue[-1]
            except:
                return False

if __name__ == "__main__":
    audio = Vocal()
    print(audio.listen())
