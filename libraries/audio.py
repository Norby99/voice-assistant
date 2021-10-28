import speech_recognition as sr

class Vocal():

    assistantName = "patric"  # the assistant name. Change it as u like
    language = "it-IT"
    # this are the commands that can be executed by the bot
    coldAir = ["ho caldo", "fa caldo", "aria fredda"]
    hotAir = ["ho freddo", "fa freddo", "aria calda"]
    conditionerPowerOff = ["spegni il condizionatore", "spegni l'aria condizionata", "stacca il condizionatore", "stacca l'aria condizionata"]

    def __init__(self):
        self.r = sr.Recognizer()

    def listen(self):   # short example function
        with sr.Microphone() as source:
            self.r.adjust_for_ambient_noise(source)
            print("In ascolto...")
            audio = self.r.listen(source)
            try:
                text = self.r.recognize_google(audio, language="it-IT")
                if text.lower() == "ciao" or ((assistantName in text.lower() and "ciao" in text.lower())):     #saluto
                    return "Ciao"
                else:                                                                                  #non saluto
                    if assistantName.lower() not in text.lower():
                        
                        return text
                    else:
                        return "Si signore!", text
            except:
                return "Non ho capito!"

    def wakeUp(self):   # checks if raul is called
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

    def Commands(self):
        with sr.Microphone() as source:
            self.r.adjust_for_ambient_noise(source)
            audio = self.r.listen(source)
            try:
                text = self.r.recognize_google(audio, language=self.language)
                if any(x in text.lower() for x in self.coldAir):
                    return ["conditioner", "cold"]
                elif any(x in text.lower() for x in self.hotAir):
                    return ["conditioner", "hot"]
                elif any(x in text.lower() for x in self.conditionerPowerOff):
                    return ["conditioner", "off"]
                else:
                    print("No command identified: " + text.lower())
            except:
                return False

if __name__ == "__main__":
    audio = Vocal()
    print(audio.listen())
