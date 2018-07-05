'''
This file is to read the BNO055 Sensor connected to arduino that is 
connected to the PI through the serial connector
'''
import serial
import time
currentHeading = 720
ser = serial.Serial('/dev/ttyACM0',9600)

def getHeading():
    read_serial=ser.readline()
    print read_serial
    return read_serial

time.sleep(5)

