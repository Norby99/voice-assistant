import importlib

class Feature():

    def __init__(self, feature):
        self.name = feature[0]
        self.commands = []  # stores all the commands that can be executed by the feature
        self.statusEnabled = feature[1]["enabled"]

        if self.getStatus():
            for name in feature[1]["features"]:     # generates all commands that can be executed by the feature
                self.commands.append(Command(name, feature[1]["features"][name][0], feature[1]["features"][name][1]))
            
        self.library = feature[1]["library"]
        
        if self.library != "Null":
            exec("self.obj = importlib.import_module(self.library)."+self.library.split(".")[0]+"()")   # creates the requered object

    def getName(self):  # returns the name of the Feature
        return self.name

    def getStatus(self):    # returns true if the feature is enabled
        return self.statusEnabled
    
    def getLibrary(self):   # returns the library that is required by the feature
        return self.library

    def recogniseInput(self, input, text=True):    # returns the response if the "input" is in any of the feature command
        for command in self.commands:
            if any(x in input for x in command.getVoiceInputs()):
                if text:
                    return self, command.getResponse()

        return None

    def execute(self, arg):
        self.obj.execute(arg)


class Command():

    def __init__(self, name, voiceInputs, response):
        self.name = name
        self.voiceInputs = voiceInputs
        self.response = response

    def getName(self):
        return self.name

    def getVoiceInputs(self):
        return self.voiceInputs

    def getResponse(self):
        return self.response
