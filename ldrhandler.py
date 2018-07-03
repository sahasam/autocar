import RPi.GPIO as GPIO
import time
import constants
import math

GPIO.setmode(GPIO.BOARD)

def ldrEvent(channel):
    #increment distance by 1/5 of wheel circumference
    constants.distance+=2*math.pi*constants.WHEEL_RADIUS/60
    print('distance: %.2d',constants.distance)

#establish interrupts
GPIO.setup(constants.LDR_PIN, GPIO.IN)
GPIO.add_event_detect(constants.LDR_PIN, GPIO.FALLING, ldrEvent, bouncetime = 100)

#cleanup after program destroy
def cleanup():
   GPIO.cleanup() 
