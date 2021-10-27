from libraries.audio import *
from libraries.conditioner import *

def executeCommand(command):
    if command[0] == "conditioner":
        conditioner.setStatus(command[1])

audio = Vocal()
conditioner = Conditioner()
command = ""

if __name__ == "__main__":
    
    print("Hi! I'm fully functional!")
    while True:
        if audio.wakeUp():
            print("How can i help you...")
            command = audio.Commands()
            if command:
                print(command)
                executeCommand(command)
