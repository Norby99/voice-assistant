from libraries.audio import *

with open(os.path.dirname(__file__) + "/setup.json") as json_file:    # setting up the assistant
    jsonData = json.load(json_file)

commands = []
for key, value in list(jsonData.items())[2:]:
    feature = Feature([key, value])
    if feature.getStatus():
        commands.append(feature)

audio = Vocal(jsonData["assistantName"].lower(), jsonData["language"], commands)

if __name__ == "__main__":
    
    print("Hi! I'm fully functional!")
    while True:
        if audio.wakeUp():
            print("How can i help you...")
            
            result = audio.Commands()
            if result:
                com, arg = result
                print(arg)
                com.execute(arg[1])

        print("---")
