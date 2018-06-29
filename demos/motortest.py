#!/usr/bin/python

# Import required modules
import time
import RPi.GPIO as GPIO

# Declare the GPIO settings
GPIO.setmode(GPIO.BOARD)

pinPWMA = 35
pinAIN2 = 40
pinAIN1 = 38
pinSTBY = 37
pinBIN1 = 31
pinBIN2 = 29
pinPWMB = 33

# set up GPIO pins
GPIO.setup(pinPWMA, GPIO.OUT) # Connected to PWMA
GPIO.setup(pinAIN2, GPIO.OUT) # Connected to AIN2
GPIO.setup(pinAIN1, GPIO.OUT) # Connected to AIN1
GPIO.setup(pinSTBY, GPIO.OUT) # Connected to STBY
GPIO.setup(pinBIN1, GPIO.OUT) # Connected to BIN1
GPIO.setup(pinBIN2, GPIO.OUT) # Connected to BIN2
GPIO.setup(pinPWMB, GPIO.OUT) # Connected to PWMB



def forwardDrive():
    GPIO.output(pinAIN2, GPIO.LOW)
    GPIO.output(pinAIN1, GPIO.HIGH)
    GPIO.output(pinSTBY, GPIO.HIGH)
    GPIO.output(pinPWMA, GPIO.HIGH)

def backwardDrive():
    GPIO.output(pinAIN1, GPIO.LOW)
    GPIO.output(pinAIN2, GPIO.HIGH)
    GPIO.output(pinSTBY, GPIO.HIGH)
    GPIO.output(pinPWMA, GPIO.HIGH)

def allstop():
    GPIO.output(pinAIN1, GPIO.LOW) # Set AIN1
    GPIO.output(pinAIN2, GPIO.LOW) # Set AIN2
    GPIO.output(pinPWMA, GPIO.LOW) # Set PWMA
    GPIO.output(pinSTBY, GPIO.LOW) # Set STBY
    GPIO.output(pinBIN1, GPIO.LOW) # Set BIN1
    GPIO.output(pinBIN2, GPIO.LOW) # Set BIN2
    GPIO.output(pinPWMB, GPIO.LOW) # Set PWMB

def turnLeft():
    GPIO.output(pinBIN2, GPIO.LOW)
    GPIO.output(pinBIN1, GPIO.HIGH)
    GPIO.output(pinSTBY, GPIO.HIGH)
    GPIO.output(pinPWMB, GPIO.HIGH)

def turnRight():
    GPIO.output(pinBIN1, GPIO.LOW)
    GPIO.output(pinBIN2, GPIO.HIGH)
    GPIO.output(pinSTBY, GPIO.HIGH)
    GPIO.output(pinPWMB, GPIO.HIGH)

try:
    while True:
        forwardDrive()
        print('forward')
        time.sleep(1)
        backwardDrive()
        print('backwards')
        time.sleep(1)
        allstop()
        turnLeft()
        print('left')
        time.sleep(1)
        turnRight()
        print('right')
        time.sleep(1)
        allstop()
except KeyboardInterrupt:
    GPIO.output(pinAIN1, GPIO.LOW) # Set AIN1
    GPIO.output(pinAIN2, GPIO.LOW) # Set AIN2
    GPIO.output(pinPWMA, GPIO.LOW) # Set PWMA
    GPIO.output(pinSTBY, GPIO.LOW) # Set STBY
    GPIO.output(pinBIN1, GPIO.LOW) # Set BIN1
    GPIO.output(pinBIN2, GPIO.LOW) # Set BIN2
    GPIO.output(pinPWMB, GPIO.LOW) # Set PWMB
    GPIO.cleanup()



