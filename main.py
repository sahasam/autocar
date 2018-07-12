'''
This is the main logic file. It handles all of the other files, and holds the main running logic. 

It incorporates distance travelled from ldrhandler.
It incorporates direction headed from serial connection.
'''
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD);

GPIO.setup(18, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.wait_for_edge(18, GPIO.FALLING)
print("starting code")

GPIO.setup(16, GPIO.IN, pull_up_down=GPIO.PUD_UP)

def my_callback (channel):
    motorhandler.allstop()
    raise SystemExit
GPIO.add_event_detect(16, GPIO.RISING, callback=my_callback)

import time
import ldrhandler
import motorhandler
import serial
import constants
import pathcontroller
ser = serial.Serial('/dev/ttyACM0',9600)

instructions = [('ne', '49'), ('n', '200'), ('e', '43'), ('se', '9'), ('s', '157')];

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

directions = {"n":0, "ne":45, "e":90, "se":135, "s":180, "sw":235, "w":270, "nw":315}


try:
    motorhandler.allstop()              #handle bug where motors automatically start on power up

    calibrate()
    headingOffset = float(getHeading())

    cur_instruction = 0
    attHeading = directions[instructions[0][0]]
    targetdistance = int(instructions[0][1])/12.0

    
    #main loop
    while True:                         #simple bang bang control system to move straight
        heading=float(getHeading()) - headingOffset
        motorhandler.forwardDrive()
        
        #if done with current instruction, move to next
        #if done with all instructions, end program
        if(constants.distance >= targetdistance):
            cur_instruction += 1
            if(cur_instruction == len(instructions)):
               break 
            print(instructions[cur_instruction])
            constants.distance = 0;
            attHeading = directions[instructions[cur_instruction][0]]
            targetdistance = int(instructions[cur_instruction][1])/12.0


        if(heading<attHeading):
            motorhandler.turnLeft()
        if(heading>attHeading):
            motorhandler.turnRight()
    
    motorhandler.GPIO.cleanup()
    motorhandler.allstop()
    ldrhandler.cleanup()
except KeyboardInterrupt, SystemExit:               #cleanly exit the program
    motorhandler.GPIO.cleanup()
    motorhandler.allstop()
    ldrhandler.cleanup()

