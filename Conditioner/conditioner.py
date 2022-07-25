import time
import threading
import sys
import os

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__)) # I must do in this way to use it both as a library and a separate program
sys.path.append(os.path.dirname(SCRIPT_DIR))

from libraries.arduino_interface import *

class Conditioner():

    def __init__(self):
        self.arduino = Arduino()
        self.powerStatus = 0
        time.sleep(2)

    def execute(self, command, repeat=True):   # takes a comand and executes it
        self.arduino.WriteSignal(command)
        if repeat:
            threading.Thread(target = self.repeatCommand, args=(command,)).start()

    def debug(self):    # it's used just to print the signal input
        print(self.arduino.ReadSignal())

    def repeatCommand(self, command):   # this function repeats the last istruction twice, because sometimes the conditioner doesn't execute it at first
        time.sleep(2)
        self.execute(command, False)

if __name__ == "__main__":

    cond = Conditioner()
    cond.execute("COLD")
    #cond.execute("off")
