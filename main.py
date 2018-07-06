'''
This is the main logic file. It handles all of the other files, and holds the main running logic. 

It incorporates distance travelled from ldrhandler.
It incorporates direction headed from serial connection.
'''
import time
import ldrhandler
import motorhandler
import serial
from threading import Thread
ser = serial.Serial('/dev/ttyACM0',9600)


def getHeading():                       #read the serial input and return heading
    read_serial=ser.readline()
    return read_serial

def findOpposite(heading):              #find the polar opposite direction from target heading.
    if(heading<=180):                   #this is used to find whether to turn left or right
        return heading-180
    else:
        return heading+180

def calibrate():                        #it takes time to initialize the serial connection.
    t_init = time.time()                #wait for 5 seconds. 
    end_time = t_init +5
    while time.time() < end_time:
        read_serial=ser.readline()
        print read_serial
        print("\twaiting\n") 

attHeading = 0                          #target heading
backHeading = findOpposite(attHeading)  #180 degrees from target heading (for turn direction)
headingOffset = 0                       #used to calibrate initial direction to normalize it

try:
    motorhandler.allstop()              #handle bug where motors automatically start on power up

    calibrate()
    headingOffset = float(getHeading())
    
    #main loop
    while True:                         #simple bang bang control system to move straight
        heading=float(getHeading()) - headingOffset
        motorhandler.forwardDrive()
        if(heading<attHeading):
            motorhandler.turnLeft()
        if(heading>attHeading):
            motorhandler.turnRight()
except KeyboardInterrupt: 
    motorhandler.GPIO.cleanup()
    ldrhandler.cleanup()

