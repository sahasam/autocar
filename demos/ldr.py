#!/usr/local/bin/python
'''
this programs is for using capacitors to measure fill/discharge time to determine
brightness of the ldr

I used this initially, but it was hard to establish interrupts with this specific
circuit.

As a result, I moved to using a potentiometer to set up a voltage divider and use
that as a more accurate determinant of light/dark.

Look at demos/potentiometer.py for more final-project-accurate code
'''

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)

circuit_pin = 7

def rc_time (circuit_pin):
    starttime = time.clock()
    count = 0

    GPIO.setup(circuit_pin, GPIO.OUT)
    GPIO.output(circuit_pin, GPIO.LOW)
    
    time.sleep(0.01)

    GPIO.setup(circuit_pin, GPIO.IN)

    while(GPIO.input(circuit_pin) == GPIO.LOW):
        count += 1
    print(time.clock() - starttime)
    return count

cutoff = 600 
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
