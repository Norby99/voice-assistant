import serial
import platform

class Arduino():

    def __init__(self):
        val = False
        if platform.system() == "Windows":
            i = 1
            while i < 6:
                try:
                    self.port = serial.Serial('COM'+str(i), 9600)
                    val = True
                    break
                except:
                    i += 1
        else:
            i = 6
            while 0 <= i:
                try:
                    self.port = serial.Serial('/dev/ttyUSB'+str(i), 9600)
                    val = True
                    break
                except:
                    i -= 1
        if val == False:
            raise ConnectionError("No Arduino detected!")
   
    def ReadSignal(self):
        message = self.port.readline().decode('utf-8', errors='ignore')
        return message

    def WriteSignal(self, msg): # it writes the signal and terminate it with a '\v'. Make sure to set that caracter as a terminator on ure Arduino script!!!
        self.port.write((msg.upper()+"\v").encode())

if __name__ == "__main__":
    arduino = Arduino()
    while True:
        print(arduino.ReadSignal())
 
