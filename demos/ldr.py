#!/usr/local/bin/python

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)

circuit_pin = 7

def rc_time (circuit_pin):
    count = 0

    GPIO.setup(circuit_pin, GPIO.OUT)
    GPIO.output(circuit_pin, GPIO.LOW)
    
    time.sleep(0.01)

    GPIO.setup(circuit_pin, GPIO.IN)

    while(GPIO.input(circuit_pin) == GPIO.LOW):
        count += 1

    return count

cutoff = 700
def translate (value):
    if(value < cutoff):
        return 1
    else:
        return 0

previousValue = translate(rc_time(circuit_pin))
distance = 0.0
pi = 3.1415
wheel_radius = 1.4375
try:
    while True:
        value = translate(rc_time(circuit_pin));
        if(previousValue != value):
            if(value == 0):
                distance += 2*pi*wheel_radius/5/12.0
        print("%.2f" % distance)   
        previousValue = value
except KeyboardInterrupt:
    GPIO.setup(circuit_pin, GPIO.OUT)
    GPIO.output(circuit_pin, GPIO.LOW)
    GPIO.cleanup()
