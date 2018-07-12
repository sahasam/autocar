'''
This file establishes the interrupts used for sensing how far the car has traveled

Instead of polling every time the loop runs for sensing if the wheel has turned, it
uses interrupts

interrupts are controlled by the kernel (the very basic operating system) to quickly
handle things like polling. It is used for key presses and mouse clicks, for example.

'''
import RPi.GPIO as GPIO
import time
import constants
import math

GPIO.setmode(GPIO.BOARD)

#this is the event handler for the interrupt.
#whenever the event is triggered, the kernel calls this function
def ldrEvent(channel):
    #increment distance by 1/5 of wheel circumference
    constants.distance+=2*math.pi*constants.WHEEL_RADIUS/48
    print('distance: %.2d',constants.distance)

#establish interrupts
GPIO.setup(constants.LDR_PIN, GPIO.IN)
GPIO.add_event_detect(constants.LDR_PIN, GPIO.FALLING, ldrEvent, bouncetime = 100)

#cleanup after program destroy
def cleanup():
   GPIO.cleanup() 
